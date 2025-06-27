# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from __future__ import annotations

import uuid
from typing import Any, Optional, cast

import pandas as pd

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
from ..types.structure_enhance_property_params import RunMetadata

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

    # type: ignore
    def enhance_column(
        self,
        *,
        df: pd.DataFrame,
        column_name: str,
        column_description: str,
        table_name: Optional[str] | NotGiven = NOT_GIVEN,
        table_description: Optional[str] | NotGiven = NOT_GIVEN,
        node_metadata: Any | NotGiven = NOT_GIVEN,
    ) -> pd.DataFrame:
        """
        Enhance a column in a DataFrame using Structify's AI capabilities.

        Args:
          df: The pandas DataFrame to enhance
          column_name: Name of the column to enhance
          column_description: Description of what the column should contain
          table_name: Name of the table (optional)
          table_description: Description of the table (optional)
          node_metadata: Optional node metadata to group related jobs (optional)
        """
        column_names: list[str] = df.columns.tolist()
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

        if column_name not in df.columns:
            df[column_name] = None

        entities: list[dict[str, Any]] = []
        for index, row in df.iterrows():  # type: ignore
            entity_properties: dict[str, Any] = {}
            for col in column_names:
                value = row[col]  # type: ignore
                if pd.notna(value):  # type: ignore
                    entity_properties[col] = str(value)  # type: ignore
            entities.append(
                {
                    "id": index,
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
            run_metadata = get_run_metadata(node_metadata)

            job_id: str = self._client.structure.enhance_property(
                entity_id=entity_id, property_name=column_name, allow_extra_entities=False, run_metadata=run_metadata
            )  # type: ignore
            job_ids.append(job_id)

        error_message = self._client.jobs.wait_for_jobs(job_ids)
        if error_message:
            raise Exception(error_message)

        entities_result = self._client.datasets.view_table(dataset=dataset_name, name=table_name_resolved)
        data = [{col: entity.properties.get(col) for col in column_names} for entity in entities_result]
        df_result = pd.DataFrame(data)
        for col in column_names:
            if col not in df_result.columns:
                df_result[col] = None
        return df_result[column_names]

    # type: ignore
    def scrape_url(
        self,
        *,
        url: str,
        table_name: str,
        schema: TableParam,
        node_metadata: Optional[Any] | NotGiven = NOT_GIVEN,
    ) -> pd.DataFrame:
        """
        Scrape data from a URL and return as a DataFrame.

        Args:
          url: The URL to scrape
          table_name: Name of the table for the structured data
          schema: Schema definition for the data to extract
          node_metadata: Optional node metadata to group related jobs (optional)
        """
        dataset_descriptor = DatasetDescriptorParam(
            name=f"scrape_{table_name}_{uuid.uuid4().hex}",
            description="",
            tables=[schema],
            relationships=[],
        )
        run_metadata = get_run_metadata(node_metadata)
        job_id: str = self._client.scrape.list(  # type: ignore
            url=url,
            table_name=table_name,
            dataset_descriptor=dataset_descriptor,
            run_metadata=run_metadata,  # type: ignore
        )  # type: ignore
        error_message = self._client.jobs.wait_for_jobs([job_id])  # type: ignore
        if error_message:
            raise Exception(error_message)

        entities_result = self._client.datasets.view_table(dataset=dataset_descriptor["name"], name=table_name)
        data = [
            {col["name"]: entity.properties.get(col["name"]) for col in schema["properties"]}
            for entity in entities_result
        ]
        df_result = pd.DataFrame(data)
        for col in schema["properties"]:
            if col["name"] not in df_result.columns:
                df_result[col["name"]] = None
        return df_result

    # type: ignore
    def structure_pdf(
        self,
        *,
        document: FileTypes,
        table_name: str,
        schema: TableParam,
        node_metadata: Optional[Any] | NotGiven = NOT_GIVEN,
    ) -> pd.DataFrame:
        """
        Extract structured data from a PDF document and return as a DataFrame.

        Args:
          document: The PDF document to process. Can be:
                   - File-like object (open file handle, BytesIO, etc.)
                   - Raw bytes
                   - Tuple with (filename, content, [content_type], [headers])
          table_name: Name of the table for the structured data
          schema: Schema definition for the data to extract
          node_metadata: Optional node metadata to group related jobs (optional)

        Returns:
          pd.DataFrame: Structured data extracted from the PDF
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

        run_metadata = get_run_metadata(node_metadata)

        job_id: str = self._client.structure.run_async(  # type: ignore
            dataset=dataset_name,
            source=SourcePdf(pdf={"path": f"{dataset_name}.pdf"}),
            run_metadata=run_metadata,  # type: ignore
        )  # type: ignore
        error_message = self._client.jobs.wait_for_jobs([job_id])  # type: ignore
        if error_message:
            raise Exception(error_message)
        entities_result = self._client.datasets.view_table(dataset=dataset_name, name=table_name)

        column_names = [prop["name"] for prop in schema["properties"]]

        data = [{col_name: entity.properties.get(col_name) for col_name in column_names} for entity in entities_result]

        df_result = pd.DataFrame(data, columns=column_names)

        return df_result


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


def get_run_metadata(node_metadata: Optional[Any] | NotGiven) -> Optional[RunMetadata]:
    """
    Helper function to cast node_metadata to run_metadata.

    Args:
      node_metadata: Optional node metadata to group related jobs.

    Returns:
      A dictionary with node_id and session_id if node_metadata is provided, otherwise None.
    """
    if node_metadata is NOT_GIVEN or node_metadata is None:
        return None
    if hasattr(node_metadata, "value"):
        if isinstance(node_metadata.value, dict):  # type: ignore
            node_id = node_metadata.value.get("NODE_ID")  # type: ignore
            session_id = node_metadata.value.get("SESSION_ID")  # type: ignore
            if node_id is None or session_id is None:
                return None
            return RunMetadata(node_id=cast(str, node_id), session_id=cast(str, session_id))
    return None
