# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from __future__ import annotations

import io
import json
import time
import uuid
from typing import Any, Dict, List, Iterable, Optional, cast
from pathlib import Path

import polars as pl
from polars import LazyFrame

from structify.types.entity_param import EntityParam
from structify.types.knowledge_graph_param import KnowledgeGraphParam

from ..types import TableParam
from .._compat import cached_property
from .._resource import SyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from .deprecated import DeprecatedPolarsMixin
from .._base_client import make_request_options
from .polars_helpers import (
    get_node_id,
    properties_to_schema,
    schema_to_properties,
    dtype_to_structify_type,
    merge_column_properties,
    _merge_schema_with_suffix,
    structify_type_to_polars_dtype,
)
from ..types.table_param import Property
from ..types.strategy_param import StrategyParam
from ..lib.cost_confirmation import request_cost_confirmation_if_needed
from .external_dataframe_proxy import ServicesProxy
from ..types.structure_response import StructureResponse
from ..types.property_type_param import PropertyTypeParam
from ..types.dataset_descriptor_param import DatasetDescriptorParam

__all__ = ["PolarsResource"]


class PolarsResource(DeprecatedPolarsMixin, SyncAPIResource):
    @cached_property
    def external(self) -> ServicesProxy:
        """Access external whitelabel services with DataFrame batch processing."""
        return ServicesProxy(self._client)

    @cached_property
    def with_raw_response(self) -> PolarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return PolarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return PolarsResourceWithStreamingResponse(self)

    def _add_single_entity(self, dataset_name: str, entity: EntityParam) -> tuple[str, EntityParam]:
        """Add a single entity to the given dataset and return (entity_id, entity).

        Always seeds with id=0 in the KnowledgeGraph to ensure consistent server-side ID assignment.
        """
        kg_param = KnowledgeGraphParam(
            entities=[EntityParam(type=entity["type"], id=0, properties=entity["properties"])],
            relationships=[],
        )
        entity_ids = self._client.entities.add_batch(
            dataset=dataset_name,
            entity_graphs=[kg_param],
        )
        return entity_ids[0], entity

    def structure(
        self,
        *,
        df: LazyFrame | pl.DataFrame,
        new_columns: Dict[str, Dict[str, Any]] | List[Dict[str, Any]] | List[Property],
        table_name: str,
        table_description: str = "",
        instruction: Optional[str] = None,
        allow_expand_rows: bool = False,
        browser: Optional[Dict[str, Any] | bool] = None,
        sandbox: Optional[Dict[str, Any] | bool] = None,
        nsteps: Optional[int] = None,
        model: Optional[str] = None,
        node_id: Optional[str] = None,
    ) -> LazyFrame:
        lazy_df = df.lazy() if isinstance(df, pl.DataFrame) else df

        input_schema = lazy_df.collect_schema()
        reserved_columns = {"_original_index", "_job_id", "_explanation"}
        for reserved in reserved_columns:
            if reserved in input_schema:
                raise ValueError(f"Column '{reserved}' is reserved for Structify metadata.")

        if browser is True:
            raise ValueError("browser must be False, None, or a BrowserConfig dict.")

        def normalize_new_columns(
            columns: Dict[str, Dict[str, Any]] | List[Dict[str, Any]] | List[Property],
        ) -> List[Property]:
            column_entries = (
                [{"name": name, **spec} for name, spec in columns.items()] if isinstance(columns, dict) else columns
            )
            properties: list[Property] = []
            for entry in column_entries:
                entry_data = cast(dict[str, Any], entry)
                name = entry_data.get("name")
                if not name:
                    raise ValueError("Each new column must include a 'name'.")
                description = entry_data.get("description", "")
                prop_type: PropertyTypeParam
                if "prop_type" in entry_data:
                    raw_prop_type = entry_data.get("prop_type")
                    if raw_prop_type is None:
                        raise ValueError("Each new column must include a non-null 'prop_type'.")
                    prop_type = cast(PropertyTypeParam, raw_prop_type)
                elif "type" in entry_data:
                    dtype = entry_data.get("type")
                    if dtype is None:
                        raise ValueError("Each new column must include a non-null 'type'.")
                    prop_type = dtype_to_structify_type(cast(pl.DataType, dtype))
                else:
                    raise ValueError("Each new column must include 'type' or 'prop_type'.")
                prop: Property = {"name": name, "description": description, "prop_type": prop_type}
                merge_strategy = entry_data.get("merge_strategy")
                if merge_strategy is not None:
                    prop["merge_strategy"] = cast(StrategyParam, merge_strategy)
                properties.append(prop)
            return properties

        new_properties = normalize_new_columns(new_columns)
        for prop in new_properties:
            if prop["name"] in reserved_columns:
                raise ValueError(f"Column '{prop['name']}' is reserved for Structify metadata.")
        existing_properties = schema_to_properties(input_schema)
        merged_properties = merge_column_properties(existing_properties, new_properties)
        metadata_properties = [
            Property(name="_original_index", description="Input row index", prop_type="Integer"),
            Property(name="_job_id", description="Job id", prop_type="String"),
            Property(name="_explanation", description="Job exit explanation", prop_type="String"),
        ]
        all_properties = merged_properties + metadata_properties
        expected_schema = properties_to_schema(all_properties)

        missing_new_columns = [prop for prop in new_properties if prop["name"] not in input_schema]
        if missing_new_columns:
            lazy_df = lazy_df.with_columns(
                [
                    pl.lit(None, dtype=structify_type_to_polars_dtype(prop.get("prop_type"))).alias(prop["name"])
                    for prop in missing_new_columns
                ]
            )

        lazy_df = lazy_df.with_row_index(name="_original_index")
        lazy_df = lazy_df.with_columns(
            [
                pl.col("_original_index").cast(pl.Int64),
                pl.lit(None, dtype=pl.String).alias("_job_id"),
                pl.lit(None, dtype=pl.String).alias("_explanation"),
            ]
        )

        resolved_node_id = node_id if node_id is not None else get_node_id()

        def structure_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            if batch_df.is_empty():
                return pl.DataFrame(schema=expected_schema)

            if not request_cost_confirmation_if_needed(self._client, batch_df.height):
                raise Exception(f"User cancelled structuring for {table_name}")

            dataset_name = f"structure_{table_name}_{uuid.uuid4().hex}"
            dataset_descriptor = DatasetDescriptorParam(
                name=dataset_name,
                description="",
                tables=[
                    TableParam(
                        name=table_name,
                        description=table_description,
                        properties=all_properties,
                    )
                ],
                relationships=[],
            )

            params: Dict[str, Any] = {
                "dataset_descriptor": dataset_descriptor,
                "table_name": table_name,
                "new_columns": new_properties,
                "allow_expand_rows": allow_expand_rows,
            }
            if instruction is not None:
                params["instruction"] = instruction
            if browser is not None:
                params["browser"] = browser
            if sandbox is not None:
                params["sandbox"] = sandbox
            if nsteps is not None:
                params["nsteps"] = nsteps
            if model is not None:
                params["model"] = model
            if resolved_node_id is not None:
                params["node_id"] = resolved_node_id

            parquet_bytes = io.BytesIO()
            batch_df.write_parquet(parquet_bytes)
            parquet_bytes.seek(0)

            response = self._post(
                "/structure",
                body={"params": json.dumps(params)},
                files={"file": ("data.parquet", parquet_bytes.getvalue(), "application/octet-stream")},
                options=make_request_options(extra_headers={"Content-Type": "multipart/form-data"}),
                cast_to=StructureResponse,
            )

            title = f"Structuring {table_name}"
            self._client.jobs.wait_for_jobs(
                dataset_name=response["dataset_name"],
                title=title,
                node_id=resolved_node_id,
            )

            results: list[dict[str, Any]] = [
                dict(entity.properties)
                for entity in self._client.datasets.view_table(
                    dataset=response["dataset_name"], name=response["table_name"]
                )
            ]
            for result_row in results:
                for col_name in expected_schema.names():
                    if col_name not in result_row:
                        result_row[col_name] = None

            if not results:
                return pl.DataFrame(schema=expected_schema)

            structured_df = pl.DataFrame(results, schema=expected_schema)
            if "_original_index" in structured_df.columns:
                structured_df = structured_df.sort("_original_index")
            return structured_df

        return lazy_df.map_batches(structure_batch, schema=expected_schema, no_optimizations=True)

    def upload_files(self, *, paths: Iterable[str | Path]) -> pl.DataFrame:
        path_list = [Path(path) for path in paths]
        schema = pl.Schema(
            {
                "file_path": pl.String(),
                "file_name": pl.String(),
                "file_extension": pl.String(),
                "file_size_bytes": pl.Int64(),
                "local_path": pl.String(),
            }
        )
        if not path_list:
            return pl.DataFrame(schema=schema)

        rows: list[dict[str, Any]] = []
        for path in path_list:
            if not path.exists():
                raise ValueError(f"File does not exist: {path}")
            if not path.is_file():
                raise ValueError(f"Path is not a file: {path}")
            extension = path.suffix.lower()
            if extension != ".pdf":
                raise ValueError(f"Unsupported file type '{extension}' for {path}")

            document_name = f"{uuid.uuid4().hex}_{path.name}"
            with path.open("rb") as handle:
                self._client.documents.upload(
                    content=handle,
                    file_type="PDF",
                    path=document_name.encode(),
                )

            rows.append(
                {
                    "file_path": document_name,
                    "file_name": path.name,
                    "file_extension": extension.lstrip("."),
                    "file_size_bytes": path.stat().st_size,
                    "local_path": str(path),
                }
            )

        return pl.DataFrame(rows, schema=schema)

    def enhance_relationships(
        self,
        *,
        lazy_df: LazyFrame,
        relationship_name: str,
        relationship_description: str,
        target_table_name: str,
        target_schema: Dict[str, Dict[str, Any]],
        target_schema_override: TableParam | None = None,
        source_table_name: str = "source_table",
    ) -> LazyFrame:
        input_schema = lazy_df.collect_schema()

        target_columns: dict[str, pl.DataType] = {}
        target_properties: list[Property] = []
        if target_schema_override:
            for prop in target_schema_override["properties"]:
                prop_type = prop.get("prop_type")
                if prop_type is None:
                    raise ValueError("target_schema_override properties must include 'prop_type'.")
                target_columns[prop["name"]] = structify_type_to_polars_dtype(prop_type)
                target_property: Property = {
                    "name": prop["name"],
                    "description": prop.get("description", ""),
                    "prop_type": prop_type,
                }
                merge_strategy = prop.get("merge_strategy")
                if merge_strategy is not None:
                    target_property["merge_strategy"] = merge_strategy
                target_properties.append(target_property)
        else:
            for col_name, col_info in target_schema.items():
                dtype = col_info.get("type", pl.String())
                target_columns[col_name] = dtype
                target_properties.append(
                    Property(
                        name=col_name,
                        description=col_info.get("description", ""),
                        prop_type=dtype_to_structify_type(dtype),
                    )
                )

        output_schema = _merge_schema_with_suffix(input_schema, target_columns, suffix=target_table_name)

        effective_properties: list[Property] = []
        for prop in target_properties:
            effective_name = prop["name"] if prop["name"] not in input_schema else f"{prop['name']}_{target_table_name}"
            prop_type = prop.get("prop_type")
            if prop_type is None:
                raise ValueError("Missing prop_type in target properties.")
            effective_prop: Property = {
                "name": effective_name,
                "description": prop.get("description", ""),
                "prop_type": prop_type,
            }
            merge_strategy = prop.get("merge_strategy")
            if merge_strategy is not None:
                effective_prop["merge_strategy"] = merge_strategy
            effective_properties.append(effective_prop)

        instruction_parts = [
            f"Find {relationship_name} for each row and return one row per related entity.",
            relationship_description,
        ]
        instruction = " ".join([part for part in instruction_parts if part])

        structured = self.structure(
            df=lazy_df,
            new_columns=effective_properties,
            table_name=source_table_name,
            table_description=relationship_description,
            instruction=instruction,
            allow_expand_rows=True,
        )

        structured = structured.drop(["_original_index", "_job_id", "_explanation"])
        return structured.select(output_schema.names())

    def tag(
        self,
        *,
        df: LazyFrame,
        new_property_name: str,
        dtype: pl.DataType,
        instructions: str,
        dataframe_name: str,
        dataframe_description: str,
    ) -> LazyFrame:
        """
        Tag entities in a LazyFrame by deriving a new property value based on all existing properties.

        This function uses the derive endpoint to generate new property values based on all existing
        properties in each row, using the provided instructions.

        Args:
            df: The input `polars.LazyFrame` to tag.
            new_property_name: Name of the new property to derive.
            dtype: Polars DataType for the new property (e.g. pl.String(), pl.Int64()).
            instructions: Instructions for how to derive the new property value.
            dataframe_name: Logical name of the dataframe (e.g. "Company", "Invoice").
            dataframe_description: Description providing context for the dataframe.

        Returns:
            LazyFrame with the original columns plus the new derived property column.
        """
        # We need to collect the DataFrame in order to guarantee starting all jobs doesn't double dip
        collected_df = df.collect()

        # Build Structify `Property` objects for existing columns
        existing_properties = schema_to_properties(collected_df.schema)

        # Add the new property to derive
        new_property = Property(
            name=new_property_name, description=instructions, prop_type=dtype_to_structify_type(dtype)
        )

        all_properties = existing_properties + [new_property]

        expected_schema = properties_to_schema(all_properties)
        if collected_df.is_empty():
            return pl.DataFrame(schema=expected_schema).lazy()

        collected_df = collected_df.with_columns([pl.lit(None, dtype=dtype).alias(new_property_name)])

        dataset_name = f"tag_{dataframe_name}_{uuid.uuid4().hex}"

        self._client.datasets.create(
            name=dataset_name,
            description="",
            tables=[
                TableParam(
                    name=dataframe_name,
                    description=dataframe_description,
                    properties=all_properties,
                )
            ],
            relationships=[],
            ephemeral=True,
        )

        node_id = get_node_id()

        # Request cost confirmation before uploading
        if not request_cost_confirmation_if_needed(self._client, len(collected_df)):
            raise Exception(f"User cancelled tagging of {dataframe_name}")

        self._upload_df(collected_df, dataset_name, dataframe_name)

        # 2. Derive the new property for each entity in the dataset
        self._client.entities.derive_all(
            dataset=dataset_name,
            derived_property=new_property_name,
            instructions=instructions,
            table_name=dataframe_name,
            node_id=node_id,
        )

        # 3. Collect the results
        title = f"Tagging {new_property_name} for {dataframe_name}"
        self._client.jobs.wait_for_jobs(dataset_name=dataset_name, title=title, node_id=node_id)
        results = [
            entity.properties for entity in self._client.datasets.view_table(dataset=dataset_name, name=dataframe_name)
        ]

        # 4. Return the results
        return pl.DataFrame(results, schema=expected_schema).lazy()

    def match(
        self,
        *,
        df1: LazyFrame,
        df2: LazyFrame,
        conditioning: str,
        df1_columns: Optional[List[str]] = None,
        df2_columns: Optional[List[str]] = None,
    ) -> LazyFrame:
        """Match rows between two DataFrames based on the provided instructions.

        NOTE: This will match the smaller dataframe to the larger one.

        Args:
            df1: First LazyFrame to match
            df2: Second LazyFrame to match
            conditioning: Natural language instructions describing how to match rows
            df1_columns: Optional list of columns to use from df1 to consider matching
            df2_columns: Optional list of columns to use from df2 to consider matching

        Returns:
            LazyFrame with three columns:
            - `idx1`: Row index from df1
            - `idx2`: Row index from df2
            - `match_reason`: AI-generated explanation of why the rows match
        """
        if df1_columns:
            df1 = df1.select(df1_columns)
        if df2_columns:
            df2 = df2.select(df2_columns)
        collected_df1 = df1.collect()
        collected_df2 = df2.collect()

        # Determine which dataframe is bigger (more rows)
        # Use the smaller one as source (table1) for cost optimization
        if len(collected_df1) > len(collected_df2):
            # df1 is bigger, so use it as reference (table2/target)
            df = collected_df2
            reference_df = collected_df1
            swapped = True
        else:
            # df2 is bigger or equal, so use it as reference (table2/target)
            df = collected_df1
            reference_df = collected_df2
            swapped = False

        table1_properties = schema_to_properties(df.schema)
        table2_properties = schema_to_properties(reference_df.schema)

        dataset_name = f"match_{uuid.uuid4().hex}"

        self._client.datasets.create(
            name=dataset_name,
            description="",
            tables=[
                TableParam(
                    name="table1",
                    description="",
                    properties=table1_properties,
                ),
                TableParam(
                    name="table2",
                    description="",
                    properties=table2_properties,
                ),
            ],
            relationships=[],
            ephemeral=True,
        )

        # Request cost confirmation before uploading
        # Cost is based on the smaller dataframe (source) which determines number of match operations
        if not request_cost_confirmation_if_needed(self._client, len(df)):
            raise Exception("User cancelled matching operation")

        self._upload_df(df, dataset_name, "table1")
        self._upload_df(reference_df, dataset_name, "table2")

        # Wait for all embeddings to be added
        TIMEOUT_SECONDS = 60
        start_time = time.monotonic()

        while time.monotonic() - start_time < TIMEOUT_SECONDS:
            remaining_embeddings = self._client.datasets.count_missing_embeddings(name=dataset_name).count
            if remaining_embeddings == 0:
                break
            time.sleep(0.5)

        node_id = get_node_id()

        self._client.match.create_jobs(
            dataset=dataset_name,
            source_table="table1",
            target_table="table2",
            conditioning=conditioning,
            node_id=node_id,
        )

        self._client.jobs.wait_for_jobs(dataset_name=dataset_name, title="Matching tables", node_id=node_id)

        matches = self._client.match.list_results(dataset=dataset_name, source_table="table1")

        if swapped:
            # If we swapped inputs, swap the results back
            # table1 was df2, table2 was df1
            # We want idx1 → df1, idx2 → df2
            matches_in_schema = {
                "idx1": [match.target_entity_index for match in matches],
                "idx2": [match.source_entity_index for match in matches],
                "match_reason": [match.match_reason for match in matches],
            }
        else:
            # No swap, return as normal
            matches_in_schema = {
                "idx1": [match.source_entity_index for match in matches],
                "idx2": [match.target_entity_index for match in matches],
                "match_reason": [match.match_reason for match in matches],
            }

        return pl.DataFrame(matches_in_schema).lazy()

    def _upload_df(
        self,
        df: pl.DataFrame,
        dataset_name: str,
        table_name: str,
    ) -> None:
        parquet_bytes = io.BytesIO()
        df.write_parquet(parquet_bytes)
        parquet_bytes.seek(0)

        response = self._client._client.post(
            "/entity/upload_parquet",
            params={"dataset": dataset_name, "table_name": table_name},
            files={"file": ("data.parquet", parquet_bytes.getvalue(), "application/octet-stream")},
            headers={"Authorization": f"Bearer {self._client.session_token}"},
        )
        response.raise_for_status()

        pass


class PolarsResourceWithRawResponse:
    def __init__(self, dataframe: PolarsResource) -> None:
        self._dataframe = dataframe

        self.enhance_columns = to_raw_response_wrapper(
            dataframe.enhance_columns,
        )
        self.tag = to_raw_response_wrapper(
            dataframe.tag,
        )


class PolarsResourceWithStreamingResponse:
    def __init__(self, dataframe: PolarsResource) -> None:
        self._dataframe = dataframe

        self.enhance_columns = to_streamed_response_wrapper(
            dataframe.enhance_columns,
        )
        self.tag = to_streamed_response_wrapper(
            dataframe.tag,
        )
