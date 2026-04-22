# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from __future__ import annotations

import io
import os
import time
import uuid
from typing import Any, Dict, List, Tuple, Literal, Optional, cast
from concurrent.futures import Future, ThreadPoolExecutor, as_completed

import pypdf
import polars as pl
from tqdm import tqdm  # type: ignore
from polars import LazyFrame

from structify import Structify
from structify.types.property_type_param import PropertyTypeParam
from structify.types.dataset_create_params import Relationship as CreateRelationshipParam

from ..types import TableParam
from .._types import Omit, omit
from .._compat import cached_property
from .._resource import SyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..types.table_param import Property
from ..lib.cost_confirmation import request_cost_confirmation_if_needed
from ..types.structure_run_async_params import Source, SourceScrape, SourceScrapeScrape

__all__ = ["PolarsResource"]

MAX_PARALLEL_REQUESTS = 20
STRUCTIFY_JOB_ID_COLUMN = "structify_job_id"


def _collect_entities_with_job_ids(client: Structify, dataset_name: str, table_name: str) -> List[Dict[str, Any]]:
    """Collect entity properties with their job_id."""
    entities = client.datasets.view_table(dataset=dataset_name, name=table_name)
    results: List[Dict[str, Any]] = []
    for entity in entities:
        row: Dict[str, Any] = dict(entity.properties)
        row[STRUCTIFY_JOB_ID_COLUMN] = entity.job_id
        results.append(row)
    return results


class PolarsResource(SyncAPIResource):
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

    def enhance_columns(
        self,
        *,
        df: LazyFrame,
        new_columns: Dict[str, Dict[str, Any]],
        dataframe_name: str,
        dataframe_description: str,
        instructions: Optional[str] = None,
        use_no_resources: bool = False,
        url_column: Optional[str] = None,
        use_proxy: bool = False,
    ) -> LazyFrame:
        """
        Enhance one or more columns of a `LazyFrame` by letting Structify populate the
        values.

            • ``"type"`` (required):  a **Polars DataType *class*** (e.g. ``pl.Int64``)
            • ``"description"`` (optional): a human-readable string

        Example::

            new_cols = {
                "net_amount": {"type": pl.Float64, "description": "Net amount after tax"},
                "due_date": {"type": pl.Date},
            }

        Descriptions are optional but improve Structify's understanding of the
        data to infer.

        Args:
            df: The input `polars.LazyFrame` to enhance.
            new_columns: Schema describing the *new* columns. Accepts either a
                `polars.Schema` or a plain mapping from column name to dtype.
            dataframe_name: Logical name of the dataframe (e.g. "Company",
                "Invoice", …) – used as the Structify *entity type*.
            dataframe_description: Free-form description that provides the
                necessary context for Structify (e.g. "Companies that are in the
                food industry").
            instructions: Optional free-form instructions to guide Structify's enrichment
            use_no_resources: When True, queue text-only structuring jobs by
                omitting `source` instead of using the default web source.
        """

        # Existing columns & their dtypes from the LazyFrame
        existing_schema_dict: Dict[str, pl.DataType] = df.collect_schema()

        # Normalise to Dict[str, Tuple[dtype, description]]
        new_columns_dict: Dict[str, tuple[pl.DataType, str]] = {}
        for col_name, val in new_columns.items():
            if "type" not in val:
                raise TypeError("Each new column must be a dict with a 'type' key containing a polars.DataType")
            dtype = val["type"]
            desc = val.get("description", "")
            new_columns_dict[col_name] = (dtype, desc)

        # ------------------------------------------------------------------
        # Build Structify `Property` objects for existing & new columns
        # ------------------------------------------------------------------
        pre_existing_properties = [
            Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype))
            for col_name, dtype in existing_schema_dict.items()
        ]

        new_column_properties = [
            Property(name=col_name, description=desc, prop_type=dtype_to_structify_type(dtype))
            for col_name, (dtype, desc) in new_columns_dict.items()
        ]

        all_properties = merge_column_properties(pre_existing_properties, new_column_properties)

        dataset_name = f"enhance_{dataframe_name}_{uuid.uuid4().hex}"
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
        # For new columns, add a null value to the dataframe with proper types
        missing_new_columns = [col_name for col_name in new_columns_dict.keys() if col_name not in existing_schema_dict]
        if missing_new_columns:
            df = df.with_columns(
                [pl.lit(None, dtype=new_columns_dict[col_name][0]).alias(col_name) for col_name in missing_new_columns]
            )

        # Get the node ID when the function is called, not when the batch is processed
        node_id = get_node_id()
        run_async_source: Source | Omit = omit if use_no_resources else "Web"
        if url_column is not None:
            run_async_source = SourceScrape(scrape=SourceScrapeScrape(url_column=url_column))
        run_async_use_proxy: bool | Omit = use_proxy if url_column is not None else omit

        # Create the expected output schema with single job_id column
        expected_schema = properties_to_schema(all_properties)
        expected_schema[STRUCTIFY_JOB_ID_COLUMN] = pl.String

        property_list = list(new_columns_dict.keys())
        property_names = _join_and(property_list)

        def enhance_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            if batch_df.is_empty():
                return pl.DataFrame(schema=expected_schema)

            if url_column is not None:
                batch_df = batch_df.drop_nulls(subset=[url_column]).unique()

            if not request_cost_confirmation_if_needed(self._client, len(batch_df), "web"):
                raise Exception(f"User cancelled enhancement of {dataframe_name}")

            self._upload_df(batch_df, dataset_name, dataframe_name)

            self._client.structure.bulk_enhance(
                dataset=dataset_name,
                table_name=dataframe_name,
                target={"Properties": {"property_names": property_list}},
                source=run_async_source,
                instructions=instructions,
                use_proxy=run_async_use_proxy,
                node_id=node_id,
            )

            title = f"Enriching {property_names} for {dataframe_name}"
            self._client.jobs.wait_for_jobs(dataset_name=dataset_name, title=title, node_id=node_id)
            results = _collect_entities_with_job_ids(self._client, dataset_name, dataframe_name)
            return pl.DataFrame(results, schema=expected_schema)

        return df.map_batches(enhance_batch, schema=expected_schema, no_optimizations=True)

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
        instructions: Optional[str] = None,
        use_no_resources: bool = False,
        url_column: Optional[str] = None,
        use_proxy: bool = False,
    ) -> LazyFrame:
        """
        Enhance a LazyFrame by finding related entities and creating a one-to-many relationship.

        Args:
            lazy_df: LazyFrame containing source entities
            relationship_name: Name of the relationship to create
            relationship_description: Description of the relationship to create
            target_table_name: Name of the target table for related entities
            target_schema: Schema definition for target entities, format: {"column_name": {"description": "...", "type": polars_dtype}}
            target_schema_override: Optional override for the target table schema (e.g. to add merge criteria)
            source_table_name: Name of the source table for related entities (e.g. "Company", "Person", etc.) (default: "source_table")

        Returns:
            LazyFrame with original columns plus new columns from related entities
        """
        input_schema = lazy_df.collect_schema()

        if url_column is not None and url_column not in input_schema:
            raise ValueError(f"Column '{url_column}' not found in LazyFrame")

        target_columns: dict[str, pl.DataType] = {}
        if target_schema_override:
            for prop in target_schema_override["properties"]:
                target_columns[prop["name"]] = structify_type_to_polars_dtype(prop.get("prop_type"))
        else:
            for col_name, col_info in target_schema.items():
                target_columns[col_name] = col_info.get("type", pl.String())

        output_schema = _merge_schema_with_suffix(input_schema, target_columns, suffix=target_table_name)
        output_schema[STRUCTIFY_JOB_ID_COLUMN] = pl.String

        target_properties: list[Property] = [
            Property(
                name=col_name,
                description=col_info.get("description", ""),
                prop_type=dtype_to_structify_type(col_info.get("type", pl.String())),
            )
            for col_name, col_info in target_schema.items()
        ]

        node_id = get_node_id()
        run_async_source: Source | Omit = omit if use_no_resources else "Web"
        if url_column is not None:
            run_async_source = SourceScrape(scrape=SourceScrapeScrape(url_column=url_column))
        run_async_use_proxy: bool | Omit = use_proxy if url_column is not None else omit

        def enhance_relationship_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            if batch_df.is_empty():
                return pl.DataFrame(schema=output_schema)

            # Create dataset for this batch
            dataset_name = f"enhance_relationships_{relationship_name}_{uuid.uuid4().hex}"

            # Create source table properties from existing schema
            source_properties = [
                Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype))
                for col_name, dtype in input_schema.items()
            ]

            self._client.datasets.create(
                name=dataset_name,
                description="",
                tables=[
                    TableParam(
                        name=source_table_name,
                        description="Source entities for relationship enhancement",
                        properties=source_properties,
                    ),
                    TableParam(
                        name=target_table_name,
                        description=f"Target entities for {relationship_name} relationship",
                        properties=target_properties,
                    ),
                ],
                relationships=[
                    CreateRelationshipParam(
                        name=relationship_name,
                        description=relationship_description,
                        source_table=source_table_name,
                        target_table=target_table_name,
                        properties=[],
                    )
                ],
                ephemeral=True,
            )

            if url_column is not None:
                batch_df = batch_df.drop_nulls(subset=[url_column]).unique()

            if not request_cost_confirmation_if_needed(self._client, len(batch_df), "web"):
                raise Exception(f"User cancelled enhancement of {source_table_name}")

            self._upload_df(batch_df, dataset_name, source_table_name)

            self._client.structure.bulk_enhance(
                dataset=dataset_name,
                table_name=source_table_name,
                target={"Relationship": {"relationship_name": relationship_name}},
                source=run_async_source,
                instructions=instructions,
                use_proxy=run_async_use_proxy,
                node_id=node_id,
            )

            title = f"Finding {relationship_name} for {source_table_name}"
            self._client.jobs.wait_for_jobs(dataset_name=dataset_name, title=title, node_id=node_id)

            response = self._client.datasets.view_tables_with_relationships(
                dataset=dataset_name, name=source_table_name
            )

            result_rows: list[dict[str, Any]] = []

            # A little caching to avoid looking up the same entity multiple times
            source_entity_id_to_entity = {entity.id: entity for entity in response.entities}
            for relationship in response.relationships:
                target_entity = next(
                    (entity for entity in response.connected_entities if entity.id == relationship.to_id), None
                )
                source_entity = source_entity_id_to_entity.get(relationship.from_id)

                if target_entity and source_entity:
                    result_row: dict[str, Any] = cast(dict[str, Any], source_entity.properties.copy())
                    for prop_name in target_schema.keys():
                        eff = (
                            prop_name if prop_name not in input_schema else f"{prop_name}_{target_table_name}"
                        )  # If the column already exists in the input schema, we need to suffix it with the target table name
                        result_row[eff] = target_entity.properties.get(prop_name)
                    result_row[STRUCTIFY_JOB_ID_COLUMN] = target_entity.job_id
                    result_rows.append(result_row)

            # Handle source rows without relationships
            source_ids_with_relationships = {rel.from_id for rel in response.relationships}
            for source_id, source_entity in source_entity_id_to_entity.items():
                if source_id not in source_ids_with_relationships:
                    orphan_row: dict[str, Any] = cast(dict[str, Any], source_entity.properties.copy())
                    for prop_name in target_schema.keys():
                        eff = prop_name if prop_name not in input_schema else f"{prop_name}_{target_table_name}"
                        orphan_row[eff] = None
                    orphan_row[STRUCTIFY_JOB_ID_COLUMN] = None
                    result_rows.append(orphan_row)

            if not result_rows:
                return pl.DataFrame(schema=output_schema)

            return pl.DataFrame(result_rows, schema=output_schema)

        return lazy_df.map_batches(enhance_relationship_batch, schema=output_schema, no_optimizations=True)

    def scrape_columns(
        self,
        *,
        df: LazyFrame,
        url_column: str,
        new_columns: Dict[str, Dict[str, Any]],
        dataframe_name: str,
        dataframe_description: str,
        use_proxy: bool = False,
    ) -> LazyFrame:
        """
        Enhance one or more columns of a `LazyFrame` directly from a URL.

        Adds a `structify_job_id` column with the job id for each row.
        """
        return self.enhance_columns(
            df=df,
            new_columns=new_columns,
            dataframe_name=dataframe_name,
            dataframe_description=dataframe_description,
            url_column=url_column,
            use_proxy=use_proxy,
        )

    def scrape_relationships(
        self,
        *,
        lazy_df: LazyFrame,
        url_column: str,
        table_name: str,
        scrape_schema: Dict[str, Dict[str, Any]],
        scrape_schema_override: TableParam | None = None,
        source_table_name: str = "source_table",
        relationship_name: str = "scraped",
        relationship_description: str = "",
        use_proxy: bool = False,
    ) -> LazyFrame:
        """
        Scrape data from URLs in a LazyFrame column and return structured results, with a column `source_url` that contains the original URL.

        Args:
          lazy_df: LazyFrame containing URLs to scrape
          url_column: Name of the column containing URLs (Must exist in the input LazyFrame)
          table_name: Name of the table to scrape. This will be the target table for the relationship.
          scrape_schema: Schema definition with descriptions, format: {"column_name": {"description": "...", "type": polars_dtype}}. If the column name is the same as the table name, it will be suffixed by the table name, e.g. "name_Person"
        """
        enhanced_df = self.enhance_relationships(
            lazy_df=lazy_df,
            relationship_name=relationship_name,
            relationship_description=relationship_description,
            target_table_name=table_name,
            target_schema=scrape_schema,
            target_schema_override=scrape_schema_override,
            source_table_name=source_table_name,
            url_column=url_column,
            use_proxy=use_proxy,
        )
        input_schema = lazy_df.collect_schema()
        enhanced_schema = enhanced_df.collect_schema()
        scraped_columns = [
            url_column,
            *[
                col_name
                for col_name in enhanced_schema.names()
                if col_name not in input_schema and col_name != STRUCTIFY_JOB_ID_COLUMN
            ],
            STRUCTIFY_JOB_ID_COLUMN,
        ]
        return lazy_df.join(
            enhanced_df.select(scraped_columns),
            on=url_column,
            how="left",
            suffix=f"_{table_name}",
        )

    def scrape_urls(
        self,
        *,
        lazy_df: LazyFrame,
        url_column: str,
        table_name: str,
        scrape_schema: Dict[str, Dict[str, Any]],
        scrape_schema_override: TableParam | None = None,
        use_proxy: bool = False,
    ) -> LazyFrame:
        """
        DEPRECATED: Use `scrape_relationships` instead.
        """
        return self.scrape_relationships(
            lazy_df=lazy_df,
            url_column=url_column,
            table_name=table_name,
            scrape_schema=scrape_schema,
            scrape_schema_override=scrape_schema_override,
            use_proxy=use_proxy,
        )

    def structure_pdfs(
        self,
        *,
        document_paths: LazyFrame,
        path_column: str,
        table_name: str,
        schema: Dict[str, Dict[str, Any]],
        conditioning: str = "",  # Kept for backward compatibility
        instructions: str | LazyFrame | None = None,
        model: str | None = None,
        mode: Literal["single", "all_pages"] = "all_pages",
    ) -> LazyFrame:
        """
        Extract structured data from PDF documents and return as a LazyFrame.

        Args:
        document_paths: LazyFrame containing a column with paths to the PDF documents to process
        path_column: Name of the column containing PDF file paths
        table_name: Name of the table for the structured data
        schema: Schema definition with descriptions, format: {"column_name": {"description": "...", "type": polars_dtype}}
        instructions: Optional instructions for the extraction. Can be a string (applied to all PDFs)
            or a LazyFrame with the same rows as document_paths containing per-PDF instructions.
        model: Optional model name to use for extraction
        mode: Whether to dispatch a single high-agency agent or one low-agency agent per page.

        Returns:
        LazyFrame: Structured data extracted from the PDFs
        """
        for key, value in schema.items():
            if "type" not in value:
                raise ValueError(f"Missing 'type' for column '{key}' in schema")

        polars_schema = pl.Schema(
            [(path_column, pl.String())]
            + [(col_name, col_info.get("type", pl.String())) for col_name, col_info in schema.items()]
            + [(STRUCTIFY_JOB_ID_COLUMN, pl.String())]
        )

        assert path_column in document_paths.collect_schema(), (
            f"Path column {path_column} must be in the input dataframe, got {document_paths.collect_schema()}"
        )

        table_param = as_table_param(table_name, schema)

        paths_df = document_paths.collect()

        page_count_map: dict[str, int] = {}
        if mode == "all_pages":
            for pdf_path in paths_df[path_column].to_list():
                if pdf_path is not None:
                    with open(pdf_path, "rb") as f:
                        pdf = pypdf.PdfReader(f)
                        page_count_map[pdf_path] = len(pdf.pages)
        else:
            for pdf_path in paths_df[path_column].to_list():
                # TODO: this is a hack to note that we cost twice as much for single page mode
                page_count_map[pdf_path] = 2

        total_pages = sum(page_count_map.values())
        if not request_cost_confirmation_if_needed(self._client, total_pages, "pdf"):
            raise Exception(f"User cancelled PDF extraction for {table_name}")

        # Create dataset for this PDF
        dataset_name = f"structure_pdfs_{table_name}_{uuid.uuid4().hex}"
        self._client.datasets.create(
            name=dataset_name,
            description="",
            tables=[table_param],
            relationships=[],
            ephemeral=True,
        )

        node_id = get_node_id()

        instructions_list: list[str | None] = []

        if instructions is not None and not isinstance(instructions, str):
            instr_df = instructions.collect()
            if instr_df.shape[0] != paths_df.shape[0]:
                raise ValueError(f"instructions shape {instr_df.shape} != document_paths shape {paths_df.shape}")
            instructions_list = cast(List[Optional[str]], instr_df[instr_df.columns[0]].to_list())

        job_to_pdf_path: dict[str, str] = {}

        # Process each PDF document
        def upload_pdf(pdf_path: str) -> None:
            # Upload the PDF document
            with open(pdf_path, "rb") as pdf_file:
                try:
                    self._client.documents.upload(
                        content=pdf_file,
                        file_type="PDF",
                        dataset=dataset_name,
                        path=pdf_path.encode(),
                    )
                except Exception as e:
                    if "Document already exists" not in str(e):
                        raise e

        with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
            upload_futures: List[Future[None]] = []
            for pdf_path in paths_df[path_column].to_list():
                if isinstance(pdf_path, str):
                    upload_futures.append(executor.submit(upload_pdf, pdf_path))
            for future in tqdm(as_completed(upload_futures), total=len(upload_futures), desc="Uploading PDFs"):
                future.result()

        def structure_pdf(pdf_path: str, instructions: str | None) -> Tuple[List[str], str]:
            pages: List[int] | None = None
            if mode == "all_pages":
                pages = list(range(page_count_map[pdf_path]))

            job_ids = self._client.structure.pdf(
                dataset=dataset_name,
                path=pdf_path,
                node_id=node_id,
                instructions=instructions,
                model=model,
                pages=pages,
            ).job_ids
            return job_ids, pdf_path

        with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
            futures: List[Future[Tuple[List[str], str]]] = []
            for i in range(paths_df.shape[0]):
                path = paths_df[path_column][i]
                pdf_instructions: str | None = None
                if isinstance(instructions, str):
                    pdf_instructions = instructions
                elif instructions_list:
                    pdf_instructions = instructions_list[i]
                if pdf_instructions is None and conditioning:
                    pdf_instructions = conditioning
                if isinstance(path, str):
                    futures.append(executor.submit(structure_pdf, path, pdf_instructions))
            for future in tqdm(as_completed(futures), total=len(futures), desc="Submitting PDFs for parsing"):
                job_ids, pdf_path = future.result()
                for job_id in job_ids:
                    job_to_pdf_path[job_id] = pdf_path

        # Wait for all PDF processing jobs to complete
        self._client.jobs.wait_for_jobs(dataset_name=dataset_name, title=f"Parsing PDF pages", node_id=node_id)

        # Get all of the entities with their job_ids
        entities = self._client.datasets.view_table(dataset=dataset_name, name=table_name)
        structured_results: List[Dict[str, Any]] = []
        for entity in entities:
            job_id = entity.job_id
            result_row: Dict[str, Any] = {
                **entity.properties,
                path_column: job_to_pdf_path.get(job_id) if job_id else None,
                STRUCTIFY_JOB_ID_COLUMN: job_id,
            }
            structured_results.append(result_row)

        # Ensure all columns are present with None for missing values
        for result_row in structured_results:
            for col_name in polars_schema.names():
                if col_name not in result_row:
                    result_row[col_name] = None

        # Build result dataframe directly from structured_results without joining
        # Each entity is already tagged with path_column from its source PDF
        return pl.DataFrame(structured_results, schema=polars_schema).lazy()

    def tag(
        self,
        *,
        df: LazyFrame,
        new_property_name: str,
        new_property_description: str = "",
        dtype: pl.DataType,
        instructions: str,
        dataframe_name: str = "default_table",  # Only exists for back compat, not shown to agent
        dataframe_description: str = "",  # Only exists for back compat, not shown to agent
        model: str | None = None,
    ) -> LazyFrame:
        """
        Tag entities in a LazyFrame by deriving a new property value based on all existing properties.

        This function uses the derive endpoint to generate new property values based on all existing
        properties in each row, using the provided instructions.

        Args:
            df: The input `polars.LazyFrame` to tag.
            new_property_name: Name of the new property to derive.
            new_property_description: Description of the new property.
            dtype: Polars DataType for the new property (e.g. pl.String(), pl.Int64()).
            instructions: Instructions for how to derive the new property value.
            model: Optional model name to use for tagging.

        Returns:
            LazyFrame with the original columns plus the new derived property column.
        """
        # We need to collect the DataFrame in order to guarantee starting all jobs doesn't double dip
        collected_df = df.collect()

        # Build Structify `Property` objects for existing columns
        existing_properties = schema_to_properties(collected_df.schema)

        # Add the new property to derive
        new_property = Property(
            name=new_property_name, description=new_property_description, prop_type=dtype_to_structify_type(dtype)
        )

        all_properties = existing_properties + [new_property]

        expected_schema = properties_to_schema(all_properties)
        expected_schema[STRUCTIFY_JOB_ID_COLUMN] = pl.String
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
        if not request_cost_confirmation_if_needed(self._client, len(collected_df), "tag"):
            raise Exception(f"User cancelled tagging of {dataframe_name}")

        self._upload_df(collected_df, dataset_name, dataframe_name)

        # 2. Derive the new property for each entity in the dataset
        self._client.entities.derive_all(
            dataset=dataset_name,
            derived_property=new_property_name,
            instructions=instructions,
            table_name=dataframe_name,
            model=model,
            node_id=node_id,
        )

        # 3. Collect the results with job_ids
        title = f"Tagging {new_property_name} for {dataframe_name}"
        self._client.jobs.wait_for_jobs(dataset_name=dataset_name, title=title, node_id=node_id)
        results = _collect_entities_with_job_ids(self._client, dataset_name, dataframe_name)

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
        no_swap: bool = False,
    ) -> LazyFrame:
        """Match rows between two DataFrames based on the provided instructions.

        NOTE: This will match the smaller dataframe to the larger one.

        Args:
            df1: First LazyFrame to match
            df2: Second LazyFrame to match
            conditioning: Natural language instructions describing how to match rows
            df1_columns: Optional list of columns to use from df1 to consider matching
            df2_columns: Optional list of columns to use from df2 to consider matching
            no_swap: A flag on whether to block automatically swapping the first
                dataframe with the second internally for efficient matching.

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
        if len(collected_df1) > len(collected_df2) and not no_swap:
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
        if not request_cost_confirmation_if_needed(self._client, len(df), "match"):
            raise Exception("User cancelled matching operation")

        self._upload_df(df, dataset_name, "table1", embed=True)
        self._upload_df(reference_df, dataset_name, "table2", embed=True)

        # Wait for all embeddings to be added
        tqdm_marker = tqdm(total=df.height + reference_df.height, desc="Waiting for embeddings")
        total_embeddings = df.height + reference_df.height
        count_history: list[int] = []
        while True:
            remaining_embeddings = self._client.datasets.count_missing_embeddings(name=dataset_name).count
            count_history.append(remaining_embeddings)
            tqdm_marker.n = total_embeddings - remaining_embeddings
            tqdm_marker.refresh()
            if remaining_embeddings == 0:
                break
            # If we haven't updated any entities in a while, consider the embeddings as not updating and break
            # with a helpful log message
            STALL_TIMEOUT = 60
            SLEEP_TIME = 0.5
            stall_count = int(STALL_TIMEOUT // SLEEP_TIME)
            time.sleep(SLEEP_TIME)

            if len(count_history) > stall_count and all(
                count == remaining_embeddings for count in count_history[-stall_count:]
            ):
                raise RuntimeError(f"Failed to match due to embedding failure. Please try again.")
        tqdm_marker.close()

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
                STRUCTIFY_JOB_ID_COLUMN: [match.job_id for match in matches],
            }
        else:
            # No swap, return as normal
            matches_in_schema = {
                "idx1": [match.source_entity_index for match in matches],
                "idx2": [match.target_entity_index for match in matches],
                "match_reason": [match.match_reason for match in matches],
                STRUCTIFY_JOB_ID_COLUMN: [match.job_id for match in matches],
            }

        return pl.DataFrame(matches_in_schema).lazy()

    def _upload_df(
        self,
        df: pl.DataFrame,
        dataset_name: str,
        table_name: str,
        embed: bool = False,
    ) -> None:
        parquet_bytes = io.BytesIO()
        df.write_parquet(parquet_bytes)
        parquet_bytes.seek(0)

        response = self._client._client.post(
            "/entity/upload_parquet",
            params={"dataset": dataset_name, "table_name": table_name, "start_embedding": embed},
            files={"file": ("data.parquet", parquet_bytes.getvalue(), "application/octet-stream")},
            headers=self._client.auth_headers,
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


def get_node_id() -> Optional[str]:
    """
    Helper function to get node_id from STRUCTIFY_NODE_ID environment variable.

    Returns:
      The node ID from environment variable if available, otherwise None.
    """
    return os.environ.get("STRUCTIFY_NODE_ID")


def merge_column_properties(
    existing_properties: List[Property],
    new_properties: List[Property],
) -> List[Property]:
    """
    Merge existing and new column properties, taking the union of columns.

    If a column exists in both existing and new properties with different types,
    raises a helpful error message indicating the type mismatch.

    Args:
        existing_properties: Properties from existing DataFrame columns
        new_properties: Properties for new columns to add

    Returns:
        List of merged properties with new properties taking precedence for existing columns

    Raises:
        ValueError: If a column exists in both with different types
    """
    # Start with a copy of existing properties (so we add new properties on the right)
    all_properties = existing_properties.copy()

    # Add new properties that aren't in existing properties
    for new_prop in new_properties:
        for prop in all_properties:
            if prop["name"] == new_prop["name"]:
                existing_type = prop.get("prop_type")
                new_type = new_prop.get("prop_type")
                if existing_type != new_type:
                    raise ValueError(
                        f"Column '{prop['name']}' type mismatch: existing column has type '{existing_type}' "
                        f"but new column specifies type '{new_type}'. "
                        f"Please ensure the new column type matches the existing column type, "
                        f"or use a different column name."
                    )
                prop["description"] = new_prop["description"]
                break
        else:
            # Add new property since it's not in properties yet
            all_properties.append(new_prop)

    return all_properties


def _join_and(names: List[str]) -> str:
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return f"{', '.join(names[:-1])}, and {names[-1]}"


def dtype_to_structify_type(dtype: pl.DataType) -> PropertyTypeParam:
    """
    Convert a Polars dtype to a Structify type.
    Map a Polars dtype to a Structify PropertyTypeParam.

    Args:
        dtype: The Polars data type to convert.

    Returns:
        The corresponding Structify PropertyTypeParam value.

    Notes:
        - Defaults to PropertyTypeParam.STRING for unknown types.
        - This mapping is intentionally explicit to avoid silent mismatches as Structify and Polars evolve.
    """
    if dtype == pl.Int64:
        return "Integer"
    elif dtype == pl.Float64:
        return "Float"
    elif dtype == pl.Boolean:
        return "Boolean"
    elif dtype == pl.String:
        return "String"
    elif dtype == pl.Date:
        return "Date"
    elif isinstance(dtype, pl.Enum):
        return {"enum": list(dtype.categories)}
    else:
        return "String"


def structify_type_to_polars_dtype(structify_type: PropertyTypeParam | None) -> pl.DataType:
    if structify_type == "Integer":
        return pl.Int64()
    elif structify_type == "Float":
        return pl.Float64()
    elif structify_type == "Boolean":
        return pl.Boolean()
    elif structify_type == "String":
        return pl.String()
    elif structify_type == "Date":
        return pl.Date()
    elif isinstance(structify_type, dict) and "enum" in structify_type:
        return pl.Enum(categories=structify_type["enum"])
    else:
        return pl.String()


def properties_to_schema(properties: list[Property]) -> pl.Schema:
    """Convert a list of Structify properties to a Polars schema."""
    return pl.Schema({prop["name"]: structify_type_to_polars_dtype(prop.get("prop_type")) for prop in properties})


def schema_to_properties(schema: pl.Schema) -> list[Property]:
    """Convert a Polars schema to a list of Structify properties."""
    return [
        Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype))
        for col_name, dtype in schema.items()
    ]


def _merge_schema_with_suffix(
    input_schema: pl.Schema,
    new_columns: dict[str, pl.DataType],
    *,
    suffix: str,
) -> pl.Schema:
    """Merge *new_columns* into *input_schema*.

    If a column already exists in *input_schema*, the column name gets
    `_<suffix>` appended to avoid collisions.

    Returns the merged Polars schema.
    """

    merged: dict[str, pl.DataType] = dict(input_schema)
    for col, dtype in new_columns.items():
        effective = col if (col not in input_schema) else f"{col}_{suffix}"
        merged[effective] = dtype

    return pl.Schema(merged)


def as_table_param(table_name: str, schema: Dict[str, Dict[str, Any]]) -> TableParam:
    return TableParam(
        name=table_name,
        description="",
        properties=[
            Property(
                name=col_name,
                description=type_and_desc.get("description", ""),
                prop_type=dtype_to_structify_type(type_and_desc["type"]),
            )
            for col_name, type_and_desc in schema.items()
        ],
    )
