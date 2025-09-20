# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime

import httpx

from ...types import (
    dataset_get_params,
    dataset_match_params,
    dataset_create_params,
    dataset_delete_params,
    dataset_view_table_params,
    dataset_add_property_params,
    dataset_export_to_csv_params,
    dataset_export_to_excel_params,
    dataset_remove_property_params,
    dataset_update_property_params,
    dataset_reorder_properties_params,
    dataset_set_primary_column_params,
    dataset_view_relationships_params,
    dataset_enrichment_progress_params,
    dataset_update_relationship_params,
    dataset_view_tables_with_relationships_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .evaluate import (
    EvaluateResource,
    AsyncEvaluateResource,
    EvaluateResourceWithRawResponse,
    AsyncEvaluateResourceWithRawResponse,
    EvaluateResourceWithStreamingResponse,
    AsyncEvaluateResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncJobsList, AsyncJobsList
from ..._base_client import AsyncPaginator, make_request_options
from ...types.table_param import TableParam
from ...types.strategy_param import StrategyParam
from ...types.property_type_param import PropertyTypeParam
from ...types.dataset_get_response import DatasetGetResponse
from ...types.dataset_list_response import DatasetListResponse
from ...types.knowledge_graph_param import KnowledgeGraphParam
from ...types.dataset_match_response import DatasetMatchResponse
from ...types.dataset_view_table_response import DatasetViewTableResponse
from ...types.relationship_merge_strategy_param import RelationshipMergeStrategyParam
from ...types.dataset_view_relationships_response import DatasetViewRelationshipsResponse
from ...types.dataset_enrichment_progress_response import DatasetEnrichmentProgressResponse
from ...types.dataset_view_tables_with_relationships_response import DatasetViewTablesWithRelationshipsResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def evaluate(self) -> EvaluateResource:
        return EvaluateResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        name: str,
        relationships: Iterable[dataset_create_params.Relationship],
        tables: Iterable[TableParam],
        ephemeral: bool | Omit = omit,
        generate_merge_criteria: bool | Omit = omit,
        llm_override_field: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Creates a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataset/create",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "relationships": relationships,
                    "tables": tables,
                    "ephemeral": ephemeral,
                    "generate_merge_criteria": generate_merge_criteria,
                    "llm_override_field": llm_override_field,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetListResponse:
        """Gets all datasets owned by the current user"""
        return self._get(
            "/dataset/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListResponse,
        )

    def delete(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently delete a dataset and all its contents

        Args:
          name: The name of the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/dataset/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, dataset_delete_params.DatasetDeleteParams),
            ),
            cast_to=NoneType,
        )

    def add_property(
        self,
        *,
        dataset_name: str,
        property: dataset_add_property_params.Property,
        table_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add a property descriptor to a table in the dataset schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/dataset/add_property",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "property": property,
                    "table_name": table_name,
                },
                dataset_add_property_params.DatasetAddPropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def enrichment_progress(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetEnrichmentProgressResponse:
        """
        Get the enrichment progress for a dataset

        Args:
          name: Enrichment progress for the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dataset/enrichment_progress",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"name": name}, dataset_enrichment_progress_params.DatasetEnrichmentProgressParams
                ),
            ),
            cast_to=DatasetEnrichmentProgressResponse,
        )

    def export_to_csv(
        self,
        *,
        dataset: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        You need to specify a dataset and a table_name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/dataset/export_to_csv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "name": name,
                    },
                    dataset_export_to_csv_params.DatasetExportToCsvParams,
                ),
            ),
            cast_to=NoneType,
        )

    def export_to_excel(
        self,
        *,
        dataset: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Each table and relationship type will be in its own sheet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/dataset/export_to_excel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset": dataset}, dataset_export_to_excel_params.DatasetExportToExcelParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetGetResponse:
        """
        Grab a dataset by its name.

        Args:
          name: Information about the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dataset/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, dataset_get_params.DatasetGetParams),
            ),
            cast_to=DatasetGetResponse,
        )

    def match(
        self,
        *,
        dataset: str,
        query_kg: KnowledgeGraphParam,
        match_threshold: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetMatchResponse:
        """
        Returns: The matched subgraph and a score for the match.

        Args:
          dataset: The dataset to match against

          query_kg: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a DB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataset/match",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "query_kg": query_kg,
                    "match_threshold": match_threshold,
                },
                dataset_match_params.DatasetMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetMatchResponse,
        )

    def remove_property(
        self,
        *,
        dataset_name: str,
        property_name: str,
        table_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a property descriptor from a table in the dataset schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/dataset/remove_property",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "property_name": property_name,
                    "table_name": table_name,
                },
                dataset_remove_property_params.DatasetRemovePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def reorder_properties(
        self,
        *,
        dataset_name: str,
        property_names: SequenceNotStr[str],
        table_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/dataset/reorder_properties",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "property_names": property_names,
                    "table_name": table_name,
                },
                dataset_reorder_properties_params.DatasetReorderPropertiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set_primary_column(
        self,
        *,
        dataset_name: str,
        property_name: str,
        table_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/dataset/set_primary_column",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "property_name": property_name,
                    "table_name": table_name,
                },
                dataset_set_primary_column_params.DatasetSetPrimaryColumnParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_property(
        self,
        *,
        dataset_name: str,
        property_name: str,
        table_name: str,
        new_property_description: Optional[str] | Omit = omit,
        new_property_merge_strategy: Optional[StrategyParam] | Omit = omit,
        new_property_type: Optional[PropertyTypeParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a property descriptor in a table in the dataset schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/dataset/update_property",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "property_name": property_name,
                    "table_name": table_name,
                    "new_property_description": new_property_description,
                    "new_property_merge_strategy": new_property_merge_strategy,
                    "new_property_type": new_property_type,
                },
                dataset_update_property_params.DatasetUpdatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_relationship(
        self,
        *,
        dataset_name: str,
        relationship_name: str,
        new_description: Optional[str] | Omit = omit,
        new_merge_strategy: Optional[RelationshipMergeStrategyParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a relationship descriptor in the dataset schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/dataset/update_relationship",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "relationship_name": relationship_name,
                    "new_description": new_description,
                    "new_merge_strategy": new_merge_strategy,
                },
                dataset_update_relationship_params.DatasetUpdateRelationshipParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def view_relationships(
        self,
        *,
        dataset: str,
        name: str,
        job_id: Optional[str] | Omit = omit,
        last_updated: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: dataset_view_relationships_params.SortBy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncJobsList[DatasetViewRelationshipsResponse]:
        """
        You need to specify a dataset and the name of the relationship

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dataset/view_relationships",
            page=SyncJobsList[DatasetViewRelationshipsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "name": name,
                        "job_id": job_id,
                        "last_updated": last_updated,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    dataset_view_relationships_params.DatasetViewRelationshipsParams,
                ),
            ),
            model=DatasetViewRelationshipsResponse,
        )

    def view_table(
        self,
        *,
        dataset: str,
        name: str,
        job_id: Optional[str] | Omit = omit,
        last_updated: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: dataset_view_table_params.SortBy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncJobsList[DatasetViewTableResponse]:
        """
        You need to specify a dataset and a table_name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dataset/view_table",
            page=SyncJobsList[DatasetViewTableResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "name": name,
                        "job_id": job_id,
                        "last_updated": last_updated,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    dataset_view_table_params.DatasetViewTableParams,
                ),
            ),
            model=DatasetViewTableResponse,
        )

    def view_tables_with_relationships(
        self,
        *,
        dataset: str,
        name: str,
        job_id: Optional[str] | Omit = omit,
        last_updated: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: dataset_view_tables_with_relationships_params.SortBy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetViewTablesWithRelationshipsResponse:
        """
        the relationships for each entity and the targets for each relationship.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dataset/view_tables_with_relationships",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "name": name,
                        "job_id": job_id,
                        "last_updated": last_updated,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    dataset_view_tables_with_relationships_params.DatasetViewTablesWithRelationshipsParams,
                ),
            ),
            cast_to=DatasetViewTablesWithRelationshipsResponse,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def evaluate(self) -> AsyncEvaluateResource:
        return AsyncEvaluateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        name: str,
        relationships: Iterable[dataset_create_params.Relationship],
        tables: Iterable[TableParam],
        ephemeral: bool | Omit = omit,
        generate_merge_criteria: bool | Omit = omit,
        llm_override_field: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Creates a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataset/create",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "relationships": relationships,
                    "tables": tables,
                    "ephemeral": ephemeral,
                    "generate_merge_criteria": generate_merge_criteria,
                    "llm_override_field": llm_override_field,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetListResponse:
        """Gets all datasets owned by the current user"""
        return await self._get(
            "/dataset/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListResponse,
        )

    async def delete(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently delete a dataset and all its contents

        Args:
          name: The name of the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/dataset/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"name": name}, dataset_delete_params.DatasetDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def add_property(
        self,
        *,
        dataset_name: str,
        property: dataset_add_property_params.Property,
        table_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add a property descriptor to a table in the dataset schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/dataset/add_property",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "property": property,
                    "table_name": table_name,
                },
                dataset_add_property_params.DatasetAddPropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def enrichment_progress(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetEnrichmentProgressResponse:
        """
        Get the enrichment progress for a dataset

        Args:
          name: Enrichment progress for the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dataset/enrichment_progress",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"name": name}, dataset_enrichment_progress_params.DatasetEnrichmentProgressParams
                ),
            ),
            cast_to=DatasetEnrichmentProgressResponse,
        )

    async def export_to_csv(
        self,
        *,
        dataset: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        You need to specify a dataset and a table_name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/dataset/export_to_csv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset": dataset,
                        "name": name,
                    },
                    dataset_export_to_csv_params.DatasetExportToCsvParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def export_to_excel(
        self,
        *,
        dataset: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Each table and relationship type will be in its own sheet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/dataset/export_to_excel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset": dataset}, dataset_export_to_excel_params.DatasetExportToExcelParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetGetResponse:
        """
        Grab a dataset by its name.

        Args:
          name: Information about the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dataset/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"name": name}, dataset_get_params.DatasetGetParams),
            ),
            cast_to=DatasetGetResponse,
        )

    async def match(
        self,
        *,
        dataset: str,
        query_kg: KnowledgeGraphParam,
        match_threshold: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetMatchResponse:
        """
        Returns: The matched subgraph and a score for the match.

        Args:
          dataset: The dataset to match against

          query_kg: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a DB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataset/match",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "query_kg": query_kg,
                    "match_threshold": match_threshold,
                },
                dataset_match_params.DatasetMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetMatchResponse,
        )

    async def remove_property(
        self,
        *,
        dataset_name: str,
        property_name: str,
        table_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a property descriptor from a table in the dataset schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/dataset/remove_property",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "property_name": property_name,
                    "table_name": table_name,
                },
                dataset_remove_property_params.DatasetRemovePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def reorder_properties(
        self,
        *,
        dataset_name: str,
        property_names: SequenceNotStr[str],
        table_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/dataset/reorder_properties",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "property_names": property_names,
                    "table_name": table_name,
                },
                dataset_reorder_properties_params.DatasetReorderPropertiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set_primary_column(
        self,
        *,
        dataset_name: str,
        property_name: str,
        table_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/dataset/set_primary_column",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "property_name": property_name,
                    "table_name": table_name,
                },
                dataset_set_primary_column_params.DatasetSetPrimaryColumnParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_property(
        self,
        *,
        dataset_name: str,
        property_name: str,
        table_name: str,
        new_property_description: Optional[str] | Omit = omit,
        new_property_merge_strategy: Optional[StrategyParam] | Omit = omit,
        new_property_type: Optional[PropertyTypeParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a property descriptor in a table in the dataset schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/dataset/update_property",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "property_name": property_name,
                    "table_name": table_name,
                    "new_property_description": new_property_description,
                    "new_property_merge_strategy": new_property_merge_strategy,
                    "new_property_type": new_property_type,
                },
                dataset_update_property_params.DatasetUpdatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_relationship(
        self,
        *,
        dataset_name: str,
        relationship_name: str,
        new_description: Optional[str] | Omit = omit,
        new_merge_strategy: Optional[RelationshipMergeStrategyParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a relationship descriptor in the dataset schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/dataset/update_relationship",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "relationship_name": relationship_name,
                    "new_description": new_description,
                    "new_merge_strategy": new_merge_strategy,
                },
                dataset_update_relationship_params.DatasetUpdateRelationshipParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def view_relationships(
        self,
        *,
        dataset: str,
        name: str,
        job_id: Optional[str] | Omit = omit,
        last_updated: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: dataset_view_relationships_params.SortBy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DatasetViewRelationshipsResponse, AsyncJobsList[DatasetViewRelationshipsResponse]]:
        """
        You need to specify a dataset and the name of the relationship

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dataset/view_relationships",
            page=AsyncJobsList[DatasetViewRelationshipsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "name": name,
                        "job_id": job_id,
                        "last_updated": last_updated,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    dataset_view_relationships_params.DatasetViewRelationshipsParams,
                ),
            ),
            model=DatasetViewRelationshipsResponse,
        )

    def view_table(
        self,
        *,
        dataset: str,
        name: str,
        job_id: Optional[str] | Omit = omit,
        last_updated: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: dataset_view_table_params.SortBy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DatasetViewTableResponse, AsyncJobsList[DatasetViewTableResponse]]:
        """
        You need to specify a dataset and a table_name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dataset/view_table",
            page=AsyncJobsList[DatasetViewTableResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "name": name,
                        "job_id": job_id,
                        "last_updated": last_updated,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    dataset_view_table_params.DatasetViewTableParams,
                ),
            ),
            model=DatasetViewTableResponse,
        )

    async def view_tables_with_relationships(
        self,
        *,
        dataset: str,
        name: str,
        job_id: Optional[str] | Omit = omit,
        last_updated: Union[str, datetime, None] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: dataset_view_tables_with_relationships_params.SortBy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetViewTablesWithRelationshipsResponse:
        """
        the relationships for each entity and the targets for each relationship.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dataset/view_tables_with_relationships",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset": dataset,
                        "name": name,
                        "job_id": job_id,
                        "last_updated": last_updated,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    dataset_view_tables_with_relationships_params.DatasetViewTablesWithRelationshipsParams,
                ),
            ),
            cast_to=DatasetViewTablesWithRelationshipsResponse,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_raw_response_wrapper(
            datasets.create,
        )
        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = to_raw_response_wrapper(
            datasets.delete,
        )
        self.add_property = to_raw_response_wrapper(
            datasets.add_property,
        )
        self.enrichment_progress = to_raw_response_wrapper(
            datasets.enrichment_progress,
        )
        self.export_to_csv = to_raw_response_wrapper(
            datasets.export_to_csv,
        )
        self.export_to_excel = to_raw_response_wrapper(
            datasets.export_to_excel,
        )
        self.get = to_raw_response_wrapper(
            datasets.get,
        )
        self.match = to_raw_response_wrapper(
            datasets.match,
        )
        self.remove_property = to_raw_response_wrapper(
            datasets.remove_property,
        )
        self.reorder_properties = to_raw_response_wrapper(
            datasets.reorder_properties,
        )
        self.set_primary_column = to_raw_response_wrapper(
            datasets.set_primary_column,
        )
        self.update_property = to_raw_response_wrapper(
            datasets.update_property,
        )
        self.update_relationship = to_raw_response_wrapper(
            datasets.update_relationship,
        )
        self.view_relationships = to_raw_response_wrapper(
            datasets.view_relationships,
        )
        self.view_table = to_raw_response_wrapper(
            datasets.view_table,
        )
        self.view_tables_with_relationships = to_raw_response_wrapper(
            datasets.view_tables_with_relationships,
        )

    @cached_property
    def evaluate(self) -> EvaluateResourceWithRawResponse:
        return EvaluateResourceWithRawResponse(self._datasets.evaluate)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_raw_response_wrapper(
            datasets.create,
        )
        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            datasets.delete,
        )
        self.add_property = async_to_raw_response_wrapper(
            datasets.add_property,
        )
        self.enrichment_progress = async_to_raw_response_wrapper(
            datasets.enrichment_progress,
        )
        self.export_to_csv = async_to_raw_response_wrapper(
            datasets.export_to_csv,
        )
        self.export_to_excel = async_to_raw_response_wrapper(
            datasets.export_to_excel,
        )
        self.get = async_to_raw_response_wrapper(
            datasets.get,
        )
        self.match = async_to_raw_response_wrapper(
            datasets.match,
        )
        self.remove_property = async_to_raw_response_wrapper(
            datasets.remove_property,
        )
        self.reorder_properties = async_to_raw_response_wrapper(
            datasets.reorder_properties,
        )
        self.set_primary_column = async_to_raw_response_wrapper(
            datasets.set_primary_column,
        )
        self.update_property = async_to_raw_response_wrapper(
            datasets.update_property,
        )
        self.update_relationship = async_to_raw_response_wrapper(
            datasets.update_relationship,
        )
        self.view_relationships = async_to_raw_response_wrapper(
            datasets.view_relationships,
        )
        self.view_table = async_to_raw_response_wrapper(
            datasets.view_table,
        )
        self.view_tables_with_relationships = async_to_raw_response_wrapper(
            datasets.view_tables_with_relationships,
        )

    @cached_property
    def evaluate(self) -> AsyncEvaluateResourceWithRawResponse:
        return AsyncEvaluateResourceWithRawResponse(self._datasets.evaluate)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_streamed_response_wrapper(
            datasets.create,
        )
        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = to_streamed_response_wrapper(
            datasets.delete,
        )
        self.add_property = to_streamed_response_wrapper(
            datasets.add_property,
        )
        self.enrichment_progress = to_streamed_response_wrapper(
            datasets.enrichment_progress,
        )
        self.export_to_csv = to_streamed_response_wrapper(
            datasets.export_to_csv,
        )
        self.export_to_excel = to_streamed_response_wrapper(
            datasets.export_to_excel,
        )
        self.get = to_streamed_response_wrapper(
            datasets.get,
        )
        self.match = to_streamed_response_wrapper(
            datasets.match,
        )
        self.remove_property = to_streamed_response_wrapper(
            datasets.remove_property,
        )
        self.reorder_properties = to_streamed_response_wrapper(
            datasets.reorder_properties,
        )
        self.set_primary_column = to_streamed_response_wrapper(
            datasets.set_primary_column,
        )
        self.update_property = to_streamed_response_wrapper(
            datasets.update_property,
        )
        self.update_relationship = to_streamed_response_wrapper(
            datasets.update_relationship,
        )
        self.view_relationships = to_streamed_response_wrapper(
            datasets.view_relationships,
        )
        self.view_table = to_streamed_response_wrapper(
            datasets.view_table,
        )
        self.view_tables_with_relationships = to_streamed_response_wrapper(
            datasets.view_tables_with_relationships,
        )

    @cached_property
    def evaluate(self) -> EvaluateResourceWithStreamingResponse:
        return EvaluateResourceWithStreamingResponse(self._datasets.evaluate)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_streamed_response_wrapper(
            datasets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            datasets.delete,
        )
        self.add_property = async_to_streamed_response_wrapper(
            datasets.add_property,
        )
        self.enrichment_progress = async_to_streamed_response_wrapper(
            datasets.enrichment_progress,
        )
        self.export_to_csv = async_to_streamed_response_wrapper(
            datasets.export_to_csv,
        )
        self.export_to_excel = async_to_streamed_response_wrapper(
            datasets.export_to_excel,
        )
        self.get = async_to_streamed_response_wrapper(
            datasets.get,
        )
        self.match = async_to_streamed_response_wrapper(
            datasets.match,
        )
        self.remove_property = async_to_streamed_response_wrapper(
            datasets.remove_property,
        )
        self.reorder_properties = async_to_streamed_response_wrapper(
            datasets.reorder_properties,
        )
        self.set_primary_column = async_to_streamed_response_wrapper(
            datasets.set_primary_column,
        )
        self.update_property = async_to_streamed_response_wrapper(
            datasets.update_property,
        )
        self.update_relationship = async_to_streamed_response_wrapper(
            datasets.update_relationship,
        )
        self.view_relationships = async_to_streamed_response_wrapper(
            datasets.view_relationships,
        )
        self.view_table = async_to_streamed_response_wrapper(
            datasets.view_table,
        )
        self.view_tables_with_relationships = async_to_streamed_response_wrapper(
            datasets.view_tables_with_relationships,
        )

    @cached_property
    def evaluate(self) -> AsyncEvaluateResourceWithStreamingResponse:
        return AsyncEvaluateResourceWithStreamingResponse(self._datasets.evaluate)
