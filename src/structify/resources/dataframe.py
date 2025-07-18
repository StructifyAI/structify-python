# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from __future__ import annotations

import os
import uuid
from typing import Any, Dict, Optional

import polars as pl
from polars import LazyFrame

from ..types import TableParam, KnowledgeGraph
from .._types import NOT_GIVEN, NotGiven, FileTypes
from .._compat import cached_property
from .._resource import SyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..types.table_param import Property
from ..types.dataset_descriptor_param import DatasetDescriptorParam
from ..types.structure_run_async_params import SourcePdf

__all__ = ["DataFrameResource"]


class DataFrameResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataFrameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return DataFrameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataFrameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return DataFrameResourceWithStreamingResponse(self)

    def enhance_column(
        self,
        *,
        df: LazyFrame,
        column_name: str,
        column_description: str,
        table_name: Optional[str] | NotGiven = NOT_GIVEN,
        table_description: Optional[str] | NotGiven = NOT_GIVEN,
    ) -> LazyFrame:
        """
        Enhance a column in a LazyFrame using Structify's AI capabilities.

        Args:
          df: The polars LazyFrame to enhance
          column_name: Name of the column to enhance
          column_description: Description of what the column should contain
          table_name: Name of the table (optional)
          table_description: Description of the table (optional)
        """
        # Get column names from schema without collecting
        column_names: list[str] = df.columns
        if column_name not in column_names:
            column_names.append(column_name)

        dataset_name = f"enhance_{column_name}_{uuid.uuid4().hex}"
        table_name_resolved = (
            str(table_name) if table_name is not NOT_GIVEN and table_name is not None else "No table name provided"
        )
        table_description_resolved = (
            str(table_description)
            if table_description is not NOT_GIVEN and table_description is not None
            else "No description provided"
        )

        self._client.datasets.create(
            name=dataset_name,
            description=f"",
            tables=[
                TableParam(
                    name=table_name_resolved,
                    description=table_description_resolved,
                    properties=[
                        Property(name=name, description=column_description if name == column_name else f"")
                        for name in column_names
                    ],
                )
            ],
            relationships=[],
        )

        # Add column if it doesn't exist, then collect only once for processing
        df_with_column = df
        if column_name not in df.columns:
            df_with_column = df.with_columns(pl.lit(None).alias(column_name))

        # Only collect when we need to iterate for entity creation
        collected_df = df_with_column.collect()

        entities: list[dict[str, Any]] = []
        for i, row in enumerate(collected_df.iter_rows(named=True)):
            entity_properties: dict[str, Any] = {}
            for col in column_names:
                value = row.get(col)
                if value is not None and not (isinstance(value, float) and pl.Float64.is_nan(value)):
                    entity_properties[col] = str(value)
            entities.append(
                {
                    "id": i,
                    "type": table_name_resolved,
                    "properties": entity_properties,
                }
            )

        entity_ids = self._client.entities.add_batch(
            dataset=dataset_name,
            entity_graphs=[
                KnowledgeGraph(
                    entities=entities,  # type: ignore
                    relationships=[],
                ),
            ],
        )

        job_ids: list[str] = []
        for entity_id in entity_ids:
            node_id = get_node_id()

            job_id = self._client.structure.enhance_property(
                entity_id=entity_id, property_name=column_name, allow_extra_entities=False, node_id=node_id
            )
            job_ids.append(job_id)

        error_message = self._client.jobs.wait_for_jobs(job_ids)
        if error_message:
            raise Exception(error_message)

        entities_result = self._client.datasets.view_table(dataset=dataset_name, name=table_name_resolved)
        data = [{col: entity.properties.get(col) for col in column_names} for entity in entities_result]
        df_result = pl.DataFrame(data)

        # Ensure all columns exist
        for col in column_names:
            if col not in df_result.columns:
                df_result = df_result.with_columns(pl.lit(None).alias(col))

        return df_result.select(column_names).lazy()

    def scrape_urls(
        self,
        *,
        lazy_df: LazyFrame,
        url_column: str,
        table_name: str,
        ScrapeSchema: TableParam,
        original_column_map: Dict[str, str],
    ) -> LazyFrame:
        """
        Scrape data from URLs in a LazyFrame column and return structured results, with a column `source_url` that contains the original URL.

        Args:
          lazy_df: LazyFrame containing URLs to scrape
          url_column: Name of the column containing URLs
          table_name: Name of the table for the structured data
          ScrapeSchema: Schema definition for the data to extract
          original_column_map: Mapping of original column names to new names
        """
        if url_column not in lazy_df.columns:
            raise ValueError(f"Column '{url_column}' not found in LazyFrame")

        # Filter out rows with null/empty URLs and get unique URLs without full collect
        unique_urls_df = (
            lazy_df.filter(pl.col(url_column).is_not_null() & (pl.col(url_column) != ""))
            .select(pl.col(url_column))
            .unique()
        )

        # Only collect the unique URLs, not the entire dataset
        unique_urls: list[str] = unique_urls_df.collect().to_series().to_list()

        if not unique_urls:
            # Return empty LazyFrame with mapped schema columns plus source_url if no valid URLs
            mapped_column_names = [
                original_column_map.get(prop["name"], prop["name"]) for prop in ScrapeSchema["properties"]
            ] + ["source_url"]
            return pl.DataFrame({col: [] for col in mapped_column_names}).lazy()

        all_results: list[dict[str, Any]] = []
        job_ids: list[str] = []
        url_to_dataset: dict[str, str] = {}
        node_id = get_node_id()

        # Create scraping jobs for each unique URL
        for url in unique_urls:
            dataset_descriptor = DatasetDescriptorParam(
                name=f"scrape_{table_name}_{uuid.uuid4().hex}",
                description="",
                tables=[ScrapeSchema],
                relationships=[],
            )

            scrape_list_response = self._client.scrape.list(
                url=str(url),
                table_name=table_name,
                dataset_descriptor=dataset_descriptor,
                node_id=node_id,
            )
            job_ids.append(scrape_list_response.job_id)
            url_to_dataset[str(url)] = scrape_list_response.dataset_name

        # Wait for all jobs to complete
        error_message = self._client.jobs.wait_for_jobs(job_ids)
        if error_message:
            raise Exception(error_message)

        # Collect results from all datasets
        for url, dataset_name in url_to_dataset.items():
            entities_result = self._client.datasets.view_table(dataset=dataset_name, name=table_name)

            for entity in entities_result:
                # Apply column mapping using original_column_map
                result_row = {}
                for col in ScrapeSchema["properties"]:
                    original_name = col["name"]
                    mapped_name = original_column_map.get(original_name, original_name)
                    result_row[mapped_name] = entity.properties.get(original_name)
                result_row["source_url"] = url
                all_results.append(result_row)

        # Create LazyFrame with all results using mapped column names
        mapped_column_names = [
            original_column_map.get(prop["name"], prop["name"]) for prop in ScrapeSchema["properties"]
        ] + ["source_url"]
        if all_results:
            df_result = pl.DataFrame(all_results)
        else:
            df_result = pl.DataFrame({col: [] for col in mapped_column_names})

        # Ensure all mapped schema columns exist even if empty
        for col in ScrapeSchema["properties"]:
            mapped_name = original_column_map.get(col["name"], col["name"])
            if mapped_name not in df_result.columns:
                df_result = df_result.with_columns(pl.lit(None).alias(mapped_name))

        return df_result.lazy()

    def structure_pdf(
        self,
        *,
        document: FileTypes,
        table_name: str,
        schema: TableParam,
    ) -> LazyFrame:
        """
        Extract structured data from a PDF document and return as a LazyFrame.

        Args:
          document: The PDF document to process. Can be:
                   - File-like object (open file handle, BytesIO, etc.)
                   - Raw bytes
                   - Tuple with (filename, content, [content_type], [headers])
          table_name: Name of the table for the structured data
          schema: Schema definition for the data to extract

        Returns:
          LazyFrame: Structured data extracted from the PDF
        """
        dataset_name = f"structure_pdf_{table_name}_{uuid.uuid4().hex}"
        self._client.datasets.create(
            name=dataset_name,
            description="",
            tables=[schema],
            relationships=[],
        )

        # Upload the PDF document using the FileTypes interface
        self._client.documents.upload(
            content=document,
            file_type="PDF",
            dataset=dataset_name,
            path=f"{dataset_name}.pdf".encode(),
        )

        node_id = get_node_id()

        job_id = self._client.structure.run_async(
            dataset=dataset_name,
            source=SourcePdf(pdf={"path": f"{dataset_name}.pdf"}),
            node_id=node_id,
        )
        error_message = self._client.jobs.wait_for_jobs([job_id])
        if error_message:
            raise Exception(error_message)
        entities_result = self._client.datasets.view_table(dataset=dataset_name, name=table_name)

        column_names = [prop["name"] for prop in schema["properties"]]

        data = [{col_name: entity.properties.get(col_name) for col_name in column_names} for entity in entities_result]

        df_result = pl.DataFrame(data if data else {col: [] for col in column_names})

        return df_result.lazy()


class DataFrameResourceWithRawResponse:
    def __init__(self, dataframe: DataFrameResource) -> None:
        self._dataframe = dataframe

        self.enhance_column = to_raw_response_wrapper(
            dataframe.enhance_column,
        )


class DataFrameResourceWithStreamingResponse:
    def __init__(self, dataframe: DataFrameResource) -> None:
        self._dataframe = dataframe

        self.enhance_column = to_streamed_response_wrapper(
            dataframe.enhance_column,
        )


def get_node_id() -> Optional[str]:
    """
    Helper function to get node_id from STRUCTIFY_NODE_ID environment variable.

    Returns:
      The node ID from environment variable if available, otherwise None.
    """
    return os.environ.get("STRUCTIFY_NODE_ID")
