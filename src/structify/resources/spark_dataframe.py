from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Iterator, Optional, Sequence, cast

# NOTE: PySpark may not be available in every runtime that imports this library
# (e.g. documentation builds).  We therefore ignore type-checking complaints and
# provide a soft-fallback that lets the module be imported without PySpark
# present.  Any attempt to *use* the Spark helpers without PySpark will still
# fail at runtime – which is fine.
#
# ruff: noqa: F401 – we intentionally re-export these names
# type: ignore

if TYPE_CHECKING:
    # Statically treat all PySpark objects as ``Any`` so that the project can
    # be type-checked without PySpark (and its stubs) installed.
    # Provide a callable stub for ``Row`` that matches the runtime signature.
    # This avoids static analysers flagging invocations like ``Row(**kwargs)``.
    from typing import (  # noqa: WPS433 – re-import for TYPE_CHECKING only
        Any,
        Any as F,  # type: ignore
        Any as SparkDF,  # type: ignore
        Any as SparkSession,  # type: ignore
        Any as T,  # type: ignore
        Callable,
    )

    Row: Callable[..., Any]  # type: ignore[type-arg]
else:  # pragma: no cover – runtime import that may fail if PySpark is absent.
    try:
        from pyspark.sql import Row, DataFrame as SparkDF, SparkSession, types as T, functions as F  # type: ignore
    except ModuleNotFoundError:  # Only triggered in non-Spark runtimes.
        # Fall back to "Any" so that attribute access passes type-checking even
        # when PySpark is not installed.  At runtime the code paths that rely
        # on these objects will raise if they are actually used.
        SparkSession = cast(Any, None)  # type: ignore
        SparkDF = cast(Any, None)  # type: ignore
        F = cast(Any, None)  # type: ignore
        T = cast(Any, None)  # type: ignore

        def Row(**kwargs: Any):  # type: ignore
            """Fallback ``Row`` implementation for non-Spark environments."""
            return kwargs


from structify.types.dataset_descriptor_param import DatasetDescriptorParam
from structify.types.structure_run_async_params import SourcePdf

from ..types import TableParam, KnowledgeGraph
from .._types import NOT_GIVEN, NotGiven, FileTypes
from .._compat import cached_property
from .._resource import SyncAPIResource
from .._response import to_raw_response_wrapper, to_streamed_response_wrapper
from ..types.table_param import Property

__all__ = ["SparkDataFrameResource"]


def _extract_client_kwargs(client: Any) -> dict[str, Any]:
    """Extract minimal kwargs from an existing Structify client so that a new
    client can be instantiated inside executors.  The current public client
    keeps these fields private so we rely on best-effort attribute inspection.
    """
    out: dict[str, Any] = {}
    for attr in ("_api_key", "api_key", "_key"):
        if hasattr(client, attr):
            out["api_key"] = getattr(client, attr)
            break
    for attr in ("_base_url", "base_url"):
        if hasattr(client, attr):
            out["base_url"] = str(getattr(client, attr))
            break
    return {k: v for k, v in out.items() if v is not None}


class SparkDataFrameResource(SyncAPIResource):
    """Spark-native helper that mirrors the pandas-centric `DataFrameResource`.

    Heavy API calls are dispatched from the executors via `mapPartitions` so the
    workload scales with the cluster.  All operations are added to the query
    plan lazily – nothing triggers an action on the driver side.
    """

    # ---------------------------------------------------------------------
    # Column enhancement ----------------------------------------------------
    # ---------------------------------------------------------------------

    def enhance_column(
        self,
        *,
        df: Any,
        column_name: str,
        column_description: str,
        table_name: Optional[str] | NotGiven = NOT_GIVEN,
        table_description: Optional[str] | NotGiven = NOT_GIVEN,
    ) -> Any:
        spark = df.sparkSession  # type: ignore[attr-defined]
        if column_name not in df.columns:
            df = df.withColumn(column_name, F.lit(None))  # type: ignore[attr-defined]

        client_kwargs_b = spark.sparkContext.broadcast(_extract_client_kwargs(self._client))

        col_names = df.columns
        table_name_resolved = (
            str(table_name) if table_name is not NOT_GIVEN and table_name is not None else "No table name provided"
        )
        table_desc_resolved = (
            str(table_description)
            if table_description is not NOT_GIVEN and table_description is not None
            else "No description provided"
        )

        def _partition(it: Iterator[Any]) -> Iterator[Any]:
            import importlib

            structify_mod = importlib.import_module("structify")
            Structify = getattr(structify_mod, "Structify", None) or getattr(structify_mod, "Client", None)
            if Structify is None:
                raise RuntimeError("Could not locate Structify client class in executor.")
            client = Structify(**client_kwargs_b.value)

            rows = list(it)
            if not rows:
                return iter([])

            dataset_name = f"enhance_{column_name}_{uuid.uuid4().hex}"
            client.datasets.create(
                name=dataset_name,
                description="",
                tables=[
                    TableParam(
                        name=table_name_resolved,
                        description=table_desc_resolved,
                        properties=[
                            Property(name=n, description=column_description if n == column_name else "")
                            for n in col_names
                        ],
                    )
                ],
                relationships=[],
            )

            entities = []
            for idx, r in enumerate(rows):
                props = {c: str(r[c]) for c in col_names if r[c] is not None}
                entities.append({"id": idx, "type": table_name_resolved, "properties": props})  # type: ignore[arg-type]

            entity_ids = client.entities.add_batch(
                dataset=dataset_name, entity_graphs=[KnowledgeGraph(entities=entities, relationships=[])]
            )  # type: ignore[arg-type]

            # Issue enhancement requests concurrently to reduce latency.
            import concurrent.futures

            def _launch(enhance_id: str) -> str:  # noqa: WPS430 – nested function is fine here
                """Submit an enhancement job for a single entity and return the Job ID."""
                return client.structure.enhance_property(
                    entity_id=enhance_id,
                    property_name=column_name,
                    allow_extra_entities=False,
                )

            max_workers = min(32, len(entity_ids)) or 1
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as pool:
                job_ids = list(pool.map(_launch, entity_ids))

            err = client.jobs.wait_for_jobs(job_ids)
            if err:
                raise RuntimeError(err)

            result_entities = client.datasets.view_table(dataset=dataset_name, name=table_name_resolved)
            lookup = {e.id: e.properties.get(column_name) for e in result_entities}

            for idx, r in enumerate(rows):
                rd = r.asDict()
                rd[column_name] = lookup.get(idx)
                yield Row(**rd)  # type: ignore[call-arg]

        new_schema = df.schema
        if column_name not in df.columns:
            new_schema = new_schema.add(column_name, T.StringType(), nullable=True)  # type: ignore[attr-defined]
        return spark.createDataFrame(df.rdd.mapPartitions(_partition), schema=new_schema)  # type: ignore[attr-defined]

    # ------------------------------------------------------------------
    # URL scraping ------------------------------------------------------
    # ------------------------------------------------------------------

    def scrape_url(
        self,
        *,
        url: str,
        table_name: str,
        schema: TableParam,
        spark: Optional[Any] = None,
    ) -> Any:
        ds_desc = DatasetDescriptorParam(
            name=f"scrape_{table_name}_{uuid.uuid4().hex}", description="", tables=[schema], relationships=[]
        )
        job_id = self._client.scrape.list(url=url, table_name=table_name, dataset_descriptor=ds_desc)  # type: ignore[attr-defined]
        err = self._client.jobs.wait_for_jobs([job_id])
        if err:
            raise RuntimeError(err)
        ents = self._client.datasets.view_table(dataset=ds_desc["name"], name=table_name)
        data = [{p["name"]: e.properties.get(p["name"]) for p in schema["properties"]} for e in ents]
        spark = spark or SparkSession.getActiveSession() or SparkSession.builder.getOrCreate()  # type: ignore[attr-defined]
        return spark.createDataFrame(data)  # type: ignore[attr-defined]

    # ------------------------------------------------------------------
    # PDF structuring ---------------------------------------------------
    # ------------------------------------------------------------------

    def structure_pdf(
        self,
        *,
        document: FileTypes,
        table_name: str,
        schema: TableParam,
        spark: Optional[Any] = None,
    ) -> Any:
        ds_name = f"structure_pdf_{table_name}_{uuid.uuid4().hex}"
        self._client.datasets.create(name=ds_name, description="", tables=[schema], relationships=[])
        self._client.documents.upload(
            content=document, file_type="PDF", dataset=ds_name, path=f"{ds_name}.pdf".encode()
        )
        job_id = self._client.structure.run_async(dataset=ds_name, source=SourcePdf(pdf={"path": f"{ds_name}.pdf"}))
        err = self._client.jobs.wait_for_jobs([job_id])
        if err:
            raise RuntimeError(err)
        ents = self._client.datasets.view_table(dataset=ds_name, name=table_name)
        cols: Sequence[str] = [p["name"] for p in schema["properties"]]
        data = [{c: e.properties.get(c) for c in cols} for e in ents]
        spark = spark or SparkSession.getActiveSession() or SparkSession.builder.getOrCreate()  # type: ignore[attr-defined]
        return spark.createDataFrame(data, schema=cols)  # type: ignore[attr-defined]

    # ------------------------------------------------------------------
    # Convenience wrappers ---------------------------------------------
    # ------------------------------------------------------------------

    @cached_property
    def with_raw_response(self) -> "SparkDataFrameResourceWithRawResponse":
        return SparkDataFrameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> "SparkDataFrameResourceWithStreamingResponse":
        return SparkDataFrameResourceWithStreamingResponse(self)


class SparkDataFrameResourceWithRawResponse:
    def __init__(self, dataframe: SparkDataFrameResource):
        self._dataframe = dataframe
        self.enhance_column = to_raw_response_wrapper(dataframe.enhance_column)


class SparkDataFrameResourceWithStreamingResponse:
    def __init__(self, dataframe: SparkDataFrameResource):
        self._dataframe = dataframe
        self.enhance_column = to_streamed_response_wrapper(dataframe.enhance_column)
