# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from __future__ import annotations

from typing import Optional

import pandas as pd

from ..types import Table, KnowledgeGraph
from .._types import NOT_GIVEN, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..types.table import Property

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
        df: pd.DataFrame,
        column_name: str,
        column_description: str,
        table_name: Optional[str] | NotGiven = NOT_GIVEN,
        table_description: Optional[str] | NotGiven = NOT_GIVEN,
    ) -> pd.DataFrame:
        """
        Enhance a column in a DataFrame using Structify's AI capabilities.

        Args:
          df: The pandas DataFrame to enhance
          column_name: Name of the column to enhance
          column_description: Description of what the column should contain
          column_type: The type of the column property
          table_name: Name of the table (optional)
          table_description: Description of the table (optional)
          extra_headers: Send extra headers
          extra_query: Add additional query parameters to the request
          extra_body: Add additional JSON properties to the request
          timeout: Override the client-level default timeout for this request, in seconds
        """
        column_names = df.columns.values.tolist()
        if column_name not in column_names:
            column_names.append(column_name)

        import time

        dataset_name = f"enhance_{column_name}_{int(time.time() * 1000)}"
        table_name_resolved = table_name if table_name is not NOT_GIVEN else "default_table"
        table_description_resolved = (
            table_description if table_description is not NOT_GIVEN else "default_table_description"
        )

        self._client.datasets.create(
            name=dataset_name,
            description=f"Enhanced {column_name} column",
            tables=[
                Table(
                    name=table_name_resolved,
                    description=table_description_resolved,
                    properties=[Property(name=name, description=f"Enhanced {name} column") for name in column_names],
                )
            ],
            relationships=[],
        )

        # Ensure the column exists in the DataFrame, and if not, fill with None
        if column_name not in df.columns:
            df[column_name] = None

        entities = [
            {
                "id": index,
                "type": table_name_resolved,
                "properties": {col: str(row[col]) for col in column_names if pd.notnull(row[col])},
            }
            for index, row in df.iterrows()
        ]

        entity_ids = self._client.entities.add_batch(
            dataset=dataset_name,
            entity_graphs=[KnowledgeGraph(entities=entities, relationships=[])],
        )

        job_ids = []
        for entity_id in entity_ids:
            job_id = self._client.structure.enhance_property(
                entity_id=entity_id,
                property_name=column_name,
                allow_extra_entities=True,
                special_job_type="HumanLLM",
                starting_searches=[column_description],
            )
            job_ids.append(job_id)

        self._client.jobs.wait_for_jobs(job_ids)
        entities = self._client.datasets.view_table(dataset=dataset_name, name=table_name_resolved)
        data = [{col: entity.properties.get(col) for col in column_names} for entity in entities]
        return pd.DataFrame(data, columns=column_names)


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
