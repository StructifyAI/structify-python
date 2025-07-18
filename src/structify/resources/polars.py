# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from __future__ import annotations

import os
import uuid
from typing import Any, Dict, Optional

import polars as pl
from polars import LazyFrame

from structify.types.entity_param import EntityParam
from structify.types.property_type_param import PropertyTypeParam

from ..types import TableParam
from .._types import FileTypes
from .._compat import cached_property
from .._resource import SyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..types.table_param import Property, TableParam
from ..types.dataset_descriptor_param import DatasetDescriptorParam
from ..types.structure_run_async_params import SourcePdf

__all__ = ["PolarsResource"]


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
        new_columns: list[Property],
        dataframe_name: str,
        dataframe_description: str,
    ) -> LazyFrame:
        """
        Enhance a column in a LazyFrame using Structify's AI capabilities.

        Args:
          df: The polars LazyFrame to enhance
          new_columns: List of column schemas to enhance
          dataframe_name: Name of the dataframe (e.g. "Company", "Invoice", …)
          dataframe_description: Specific description of the dataframe that provides the context needed for the Structify AI to understand the data to look for. (e.g. "Companies that are in the food industry")
        """
        schema = df.collect_schema()
        pre_existing_properties = [
            Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype))
            for col_name, dtype in schema.items()
        ]
        all_properties = pre_existing_properties + new_columns
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
        )
        # For new columns, add a null value to the dataframe with proper types
        missing_new_columns = [
            col for col in new_columns if col["name"] not in {p["name"] for p in pre_existing_properties}
        ]
        if missing_new_columns:
            df = df.with_columns(
                [
                    pl.lit(None, dtype=structify_type_to_polars_dtype(col.get("prop_type"))).alias(col["name"])
                    for col in missing_new_columns
                ]
            )

        # Get the node ID when the function is called, not when the batch is processed
        node_id = get_node_id()

        # Create the expected output schema
        expected_schema = properties_to_schema(all_properties)

        # Apply Structify enrich on the dataframe
        def enhance_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            # 1. Add all the entities to the structify dataset
            entity_ids = self._client.entities.add_batch(
                dataset=dataset_name,
                entity_graphs=[
                    {
                        "entities": [
                            EntityParam(
                                type=dataframe_name,
                                id=i,
                                properties={col["name"]: str(row[col["name"]]) for col in all_properties},
                            )
                            for i, row in enumerate(batch_df.to_dicts())
                        ],
                        "relationships": [],
                    }
                ],
            )
            # 2. Enhance the entities
            job_ids: list[str] = []
            for entity_id in entity_ids:
                for col in new_columns:
                    job_ids.append(
                        self._client.structure.enhance_property(
                            entity_id=entity_id,
                            property_name=col["name"],
                            allow_extra_entities=False,
                            node_id=node_id,
                        )
                    )
            # 3. Wait for all jobs to complete
            self._client.jobs.wait_for_jobs(job_ids)
            # 4. Collect the results
            results = [
                entity.properties
                for entity in self._client.datasets.view_table(dataset=dataset_name, name=dataframe_name)
            ]
            # 5. Return the results
            return pl.DataFrame(results, schema=expected_schema)

        return df.map_batches(enhance_batch, schema=expected_schema)

    def scrape_urls(
        self,
        *,
        lazy_df: LazyFrame,
        url_column: str,
        table_name: str,
        scrape_schema: Dict[str, Dict[str, Any]],
        scrape_schema_override: TableParam | None = None,
        original_column_map: Dict[str, str] = {},
    ) -> LazyFrame:
        """
        Scrape data from URLs in a LazyFrame column and return structured results, with a column `source_url` that contains the original URL.

        Args:
          lazy_df: LazyFrame containing URLs to scrape
          url_column: Name of the column containing URLs (Must exist in the input LazyFrame)
          table_name: Name of the table for the structured data
          scrape_schema: Schema definition with descriptions, format: {"column_name": {"description": "...", "type": polars_dtype}}
          original_column_map: Mapping of original column names to new names
        """
        input_schema = lazy_df.collect_schema()

        if url_column not in input_schema:
            raise ValueError(f"Column '{url_column}' not found in LazyFrame")

        output_schema = input_schema.copy()

        if scrape_schema_override:
            for prop in scrape_schema_override["properties"]:
                prop_type = structify_type_to_polars_dtype(prop.get("prop_type"))
                if prop["name"] in original_column_map:
                    output_schema[original_column_map[prop["name"]]] = prop_type
                else:
                    output_schema[prop["name"]] = prop_type
        else:
            for col_name, col_info in scrape_schema.items():
                col_type = col_info.get("type", pl.String())
                output_schema[col_name] = col_type

        # Create properties with descriptions from the new schema format
        properties: list[Property] = []
        for col_name, col_info in scrape_schema.items():
            polars_type = col_info.get("type", pl.String())
            structify_type = dtype_to_structify_type(polars_type)
            properties.append(
                Property(name=col_name, description=col_info.get("description", ""), prop_type=structify_type)
            )

        # Add existing columns from input schema
        for col_name, dtype in input_schema.items():
            if col_name not in scrape_schema:
                properties.append(Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype)))

        dataset_descriptor = DatasetDescriptorParam(
            name=f"scrape_{table_name}_{uuid.uuid4().hex}",
            description="",
            tables=[
                TableParam(
                    name=table_name,
                    description="",
                    properties=properties,
                )
            ],
            relationships=[],
        )

        node_id = get_node_id()

        def scrape_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            # 1. Get the unique URLs in the batch
            batch_urls = batch_df.select(url_column).drop_nulls().unique().to_series().to_list()

            # 2. Scrape the URLs
            job_ids: list[str] = []  # List of job IDs for the scrape jobs to wait for
            url_to_dataset: dict[str, str] = {}  # Each URL is scraped into a separate dataset

            for url in batch_urls:
                scrape_list_response = self._client.scrape.list(
                    url=str(url),
                    table_name=table_name,
                    dataset_descriptor=dataset_descriptor,
                    node_id=node_id,
                )
                job_ids.append(scrape_list_response.job_id)
                url_to_dataset[str(url)] = scrape_list_response.dataset_name

            self._client.jobs.wait_for_jobs(job_ids)

            # 3. Collect the results and join them with the original dataframe using url_column and url
            all_results: list[dict[str, Any]] = []
            for url, dataset_name in url_to_dataset.items():
                entities_result = self._client.datasets.view_table(dataset=dataset_name, name=table_name)
                for entity in entities_result:
                    result_row = {**entity.properties, url_column: url}
                    # Join the result row with the original dataframe
                    result_row = {
                        **result_row,
                        **{k: v for k, v in batch_df.to_dicts()[0].items() if k not in result_row},
                    }
                    all_results.append(result_row)

            # 4. Return the results
            return pl.DataFrame(all_results, schema=output_schema)

        return lazy_df.map_batches(scrape_batch, schema=output_schema)

    def structure_pdf(
        self,
        *,
        document: FileTypes,
        table_name: str,
        schema: Dict[str, Dict[str, Any]],
    ) -> LazyFrame:
        """
        Extract structured data from a PDF document and return as a LazyFrame.

        Args:
          document: The PDF document to process. Can be:
                   - File-like object (open file handle, BytesIO, etc.)
                   - Raw bytes
                   - Tuple with (filename, content, [content_type], [headers])
          table_name: Name of the table for the structured data
          schema: Schema definition with descriptions, format: {"column_name": {"description": "...", "type": polars_dtype}}

        Returns:
          LazyFrame: Structured data extracted from the PDF
        """

        column_names = list(schema.keys())
        polars_schema = pl.Schema(
            {col_name: col_info.get("type", pl.String()) for col_name, col_info in schema.items()}
        )
        node_id = get_node_id()

        # For structure_pdf, we don't need input data - just process the PDF document directly
        dataset_name = f"structure_pdf_{table_name}_{uuid.uuid4().hex}"

        # Create properties with descriptions from the new schema format
        properties: list[Property] = []
        for col_name, col_info in schema.items():
            polars_type = col_info.get("type", pl.String())
            structify_type = dtype_to_structify_type(polars_type)
            properties.append(
                Property(name=col_name, description=col_info.get("description", ""), prop_type=structify_type)
            )

        self._client.datasets.create(
            name=dataset_name,
            description="",
            tables=[
                TableParam(
                    name=table_name,
                    description="",
                    properties=properties,
                )
            ],
            relationships=[],
        )

        self._client.documents.upload(
            content=document,
            file_type="PDF",
            dataset=dataset_name,
            path=f"{dataset_name}.pdf".encode(),
        )

        job_id = self._client.structure.run_async(
            dataset=dataset_name,
            source=SourcePdf(pdf={"path": f"{dataset_name}.pdf"}),
            node_id=node_id,
        )
        error_message = self._client.jobs.wait_for_jobs([job_id])
        if error_message:
            raise Exception(error_message)
        entities_result = self._client.datasets.view_table(dataset=dataset_name, name=table_name)

        # Build the data as a list of dicts, using None for missing properties
        data = [{col_name: entity.properties.get(col_name) for col_name in column_names} for entity in entities_result]
        # If no data, return empty DataFrame with correct dtypes
        if not data:
            result_df = pl.DataFrame({col: pl.Series([], dtype=polars_schema[col]) for col in column_names})
        else:
            # Otherwise, construct DataFrame with explicit schema to avoid Null dtypes
            result_df = pl.DataFrame(data, schema=polars_schema)

        return result_df.lazy()


class PolarsResourceWithRawResponse:
    def __init__(self, dataframe: PolarsResource) -> None:
        self._dataframe = dataframe

        self.enhance_column = to_raw_response_wrapper(
            dataframe.enhance_columns,
        )


class PolarsResourceWithStreamingResponse:
    def __init__(self, dataframe: PolarsResource) -> None:
        self._dataframe = dataframe

        self.enhance_column = to_streamed_response_wrapper(
            dataframe.enhance_columns,
        )


def get_node_id() -> Optional[str]:
    """
    Helper function to get node_id from STRUCTIFY_NODE_ID environment variable.

    Returns:
      The node ID from environment variable if available, otherwise None.
    """
    return os.environ.get("STRUCTIFY_NODE_ID")


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
    else:
        return pl.String()


def properties_to_schema(properties: list[Property]) -> pl.Schema:
    return pl.Schema({prop["name"]: structify_type_to_polars_dtype(prop.get("prop_type")) for prop in properties})


def as_table_param(table_name: str, schema: pl.Schema) -> TableParam:
    return TableParam(
        name=table_name,
        description="",
        properties=[
            Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype))
            for col_name, dtype in schema.items()
        ],
    )
