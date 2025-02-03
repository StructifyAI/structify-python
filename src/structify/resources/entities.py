# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ..types import (
    KnowledgeGraph,
    entity_add_params,
    entity_get_params,
    entity_view_params,
    entity_merge_params,
    entity_delete_params,
    entity_search_params,
    entity_verify_params,
    entity_add_batch_params,
    entity_list_jobs_params,
    entity_summarize_params,
    entity_trigger_merge_params,
    entity_update_property_params,
    entity_get_local_subgraph_params,
    entity_get_source_entities_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.knowledge_graph import KnowledgeGraph
from ..types.entity_add_response import EntityAddResponse
from ..types.entity_get_response import EntityGetResponse
from ..types.entity_view_response import EntityViewResponse
from ..types.entity_merge_response import EntityMergeResponse
from ..types.knowledge_graph_param import KnowledgeGraphParam
from ..types.entity_delete_response import EntityDeleteResponse
from ..types.entity_search_response import EntitySearchResponse
from ..types.entity_add_batch_response import EntityAddBatchResponse
from ..types.entity_list_jobs_response import EntityListJobsResponse
from ..types.entity_summarize_response import EntitySummarizeResponse
from ..types.entity_trigger_merge_response import EntityTriggerMergeResponse
from ..types.entity_update_property_response import EntityUpdatePropertyResponse
from ..types.entity_get_local_subgraph_response import EntityGetLocalSubgraphResponse
from ..types.entity_get_source_entities_response import EntityGetSourceEntitiesResponse

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        dataset_name: str,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityDeleteResponse:
        """
        Delete an entity manually

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/entity/delete",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "entity_id": entity_id,
                },
                entity_delete_params.EntityDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityDeleteResponse,
        )

    def add(
        self,
        *,
        dataset_name: str,
        kg: KnowledgeGraphParam,
        attempt_merge: bool | NotGiven = NOT_GIVEN,
        source: entity_add_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityAddResponse:
        """
        Args:
          kg: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a Neo4j DB

          attempt_merge: If true, attempt to merge with existing entities in the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entity/add",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "kg": kg,
                    "attempt_merge": attempt_merge,
                    "source": source,
                },
                entity_add_params.EntityAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityAddResponse,
        )

    def add_batch(
        self,
        *,
        dataset_name: str,
        kgs: Iterable[KnowledgeGraphParam],
        attempt_merge: bool | NotGiven = NOT_GIVEN,
        source: entity_add_batch_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityAddBatchResponse:
        """
        Args:
          attempt_merge: If true, attempt to merge with existing entities in the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entity/add_batch",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "kgs": kgs,
                    "attempt_merge": attempt_merge,
                    "source": source,
                },
                entity_add_batch_params.EntityAddBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityAddBatchResponse,
        )

    def get(
        self,
        *,
        id: str,
        resolve_id: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityGetResponse:
        """
        Get entity with a given id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/entity/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "resolve_id": resolve_id,
                    },
                    entity_get_params.EntityGetParams,
                ),
            ),
            cast_to=EntityGetResponse,
        )

    def get_local_subgraph(
        self,
        *,
        id: str,
        radius: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityGetLocalSubgraphResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/entity/get_local_subgraph",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "radius": radius,
                    },
                    entity_get_local_subgraph_params.EntityGetLocalSubgraphParams,
                ),
            ),
            cast_to=EntityGetLocalSubgraphResponse,
        )

    def get_source_entities(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityGetSourceEntitiesResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/entity/get_source_entities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, entity_get_source_entities_params.EntityGetSourceEntitiesParams),
            ),
            cast_to=EntityGetSourceEntitiesResponse,
        )

    def list_jobs(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListJobsResponse:
        """
        list jobs for a given entity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/entity/list_jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, entity_list_jobs_params.EntityListJobsParams),
            ),
            cast_to=EntityListJobsResponse,
        )

    def merge(
        self,
        *,
        entity_1_id: str,
        entity_2_id: str,
        debug: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityMergeResponse:
        """
        merge an entity manually

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entity/merge",
            body=maybe_transform(
                {
                    "entity_1_id": entity_1_id,
                    "entity_2_id": entity_2_id,
                    "debug": debug,
                },
                entity_merge_params.EntityMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityMergeResponse,
        )

    def search(
        self,
        *,
        dataset_name: str,
        query: str,
        table_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntitySearchResponse:
        """
        Search for entities based on the given query

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entity/search",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "query": query,
                    "table_name": table_name,
                },
                entity_search_params.EntitySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitySearchResponse,
        )

    def summarize(
        self,
        *,
        dataset_name: str,
        entity_id: str,
        properties: List[str],
        extra_instructions: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntitySummarizeResponse:
        """
        Search for entities based on the given query

        Args:
          extra_instructions: A list of instructions for each property to guide the summarization process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entity/summarize",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "entity_id": entity_id,
                    "properties": properties,
                    "extra_instructions": extra_instructions,
                },
                entity_summarize_params.EntitySummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitySummarizeResponse,
        )

    def trigger_merge(
        self,
        *,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityTriggerMergeResponse:
        """
        Trigger our merge process for a given entity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entity/trigger_merge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"entity_id": entity_id}, entity_trigger_merge_params.EntityTriggerMergeParams),
            ),
            cast_to=EntityTriggerMergeResponse,
        )

    def update_property(
        self,
        *,
        dataset_name: str,
        entity_id: str,
        prop_name: str,
        prop_value: entity_update_property_params.PropValue,
        source: entity_update_property_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityUpdatePropertyResponse:
        """
        update an entity manually

        Args:
          prop_name: The name of the property to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entity/update",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "entity_id": entity_id,
                    "prop_name": prop_name,
                    "prop_value": prop_value,
                    "source": source,
                },
                entity_update_property_params.EntityUpdatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityUpdatePropertyResponse,
        )

    def verify(
        self,
        *,
        dataset_name: str,
        kg: KnowledgeGraphParam,
        fix: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeGraph:
        """
        verify a kg against the dataset

        Args:
          kg: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a Neo4j DB

          fix: Whether to apply fixes to the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entity/verify",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "kg": kg,
                    "fix": fix,
                },
                entity_verify_params.EntityVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeGraph,
        )

    def view(
        self,
        *,
        id: str,
        resolve_id: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityViewResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/entity/view",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "resolve_id": resolve_id,
                    },
                    entity_view_params.EntityViewParams,
                ),
            ),
            cast_to=EntityViewResponse,
        )


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        dataset_name: str,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityDeleteResponse:
        """
        Delete an entity manually

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/entity/delete",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "entity_id": entity_id,
                },
                entity_delete_params.EntityDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityDeleteResponse,
        )

    async def add(
        self,
        *,
        dataset_name: str,
        kg: KnowledgeGraphParam,
        attempt_merge: bool | NotGiven = NOT_GIVEN,
        source: entity_add_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityAddResponse:
        """
        Args:
          kg: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a Neo4j DB

          attempt_merge: If true, attempt to merge with existing entities in the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entity/add",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "kg": kg,
                    "attempt_merge": attempt_merge,
                    "source": source,
                },
                entity_add_params.EntityAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityAddResponse,
        )

    async def add_batch(
        self,
        *,
        dataset_name: str,
        kgs: Iterable[KnowledgeGraphParam],
        attempt_merge: bool | NotGiven = NOT_GIVEN,
        source: entity_add_batch_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityAddBatchResponse:
        """
        Args:
          attempt_merge: If true, attempt to merge with existing entities in the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entity/add_batch",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "kgs": kgs,
                    "attempt_merge": attempt_merge,
                    "source": source,
                },
                entity_add_batch_params.EntityAddBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityAddBatchResponse,
        )

    async def get(
        self,
        *,
        id: str,
        resolve_id: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityGetResponse:
        """
        Get entity with a given id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/entity/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "resolve_id": resolve_id,
                    },
                    entity_get_params.EntityGetParams,
                ),
            ),
            cast_to=EntityGetResponse,
        )

    async def get_local_subgraph(
        self,
        *,
        id: str,
        radius: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityGetLocalSubgraphResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/entity/get_local_subgraph",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "radius": radius,
                    },
                    entity_get_local_subgraph_params.EntityGetLocalSubgraphParams,
                ),
            ),
            cast_to=EntityGetLocalSubgraphResponse,
        )

    async def get_source_entities(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityGetSourceEntitiesResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/entity/get_source_entities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id": id}, entity_get_source_entities_params.EntityGetSourceEntitiesParams
                ),
            ),
            cast_to=EntityGetSourceEntitiesResponse,
        )

    async def list_jobs(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListJobsResponse:
        """
        list jobs for a given entity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/entity/list_jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, entity_list_jobs_params.EntityListJobsParams),
            ),
            cast_to=EntityListJobsResponse,
        )

    async def merge(
        self,
        *,
        entity_1_id: str,
        entity_2_id: str,
        debug: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityMergeResponse:
        """
        merge an entity manually

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entity/merge",
            body=await async_maybe_transform(
                {
                    "entity_1_id": entity_1_id,
                    "entity_2_id": entity_2_id,
                    "debug": debug,
                },
                entity_merge_params.EntityMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityMergeResponse,
        )

    async def search(
        self,
        *,
        dataset_name: str,
        query: str,
        table_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntitySearchResponse:
        """
        Search for entities based on the given query

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entity/search",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "query": query,
                    "table_name": table_name,
                },
                entity_search_params.EntitySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitySearchResponse,
        )

    async def summarize(
        self,
        *,
        dataset_name: str,
        entity_id: str,
        properties: List[str],
        extra_instructions: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntitySummarizeResponse:
        """
        Search for entities based on the given query

        Args:
          extra_instructions: A list of instructions for each property to guide the summarization process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entity/summarize",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "entity_id": entity_id,
                    "properties": properties,
                    "extra_instructions": extra_instructions,
                },
                entity_summarize_params.EntitySummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitySummarizeResponse,
        )

    async def trigger_merge(
        self,
        *,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityTriggerMergeResponse:
        """
        Trigger our merge process for a given entity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entity/trigger_merge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"entity_id": entity_id}, entity_trigger_merge_params.EntityTriggerMergeParams
                ),
            ),
            cast_to=EntityTriggerMergeResponse,
        )

    async def update_property(
        self,
        *,
        dataset_name: str,
        entity_id: str,
        prop_name: str,
        prop_value: entity_update_property_params.PropValue,
        source: entity_update_property_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityUpdatePropertyResponse:
        """
        update an entity manually

        Args:
          prop_name: The name of the property to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entity/update",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "entity_id": entity_id,
                    "prop_name": prop_name,
                    "prop_value": prop_value,
                    "source": source,
                },
                entity_update_property_params.EntityUpdatePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityUpdatePropertyResponse,
        )

    async def verify(
        self,
        *,
        dataset_name: str,
        kg: KnowledgeGraphParam,
        fix: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeGraph:
        """
        verify a kg against the dataset

        Args:
          kg: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a Neo4j DB

          fix: Whether to apply fixes to the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entity/verify",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "kg": kg,
                    "fix": fix,
                },
                entity_verify_params.EntityVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeGraph,
        )

    async def view(
        self,
        *,
        id: str,
        resolve_id: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityViewResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/entity/view",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "resolve_id": resolve_id,
                    },
                    entity_view_params.EntityViewParams,
                ),
            ),
            cast_to=EntityViewResponse,
        )


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.delete = to_raw_response_wrapper(
            entities.delete,
        )
        self.add = to_raw_response_wrapper(
            entities.add,
        )
        self.add_batch = to_raw_response_wrapper(
            entities.add_batch,
        )
        self.get = to_raw_response_wrapper(
            entities.get,
        )
        self.get_local_subgraph = to_raw_response_wrapper(
            entities.get_local_subgraph,
        )
        self.get_source_entities = to_raw_response_wrapper(
            entities.get_source_entities,
        )
        self.list_jobs = to_raw_response_wrapper(
            entities.list_jobs,
        )
        self.merge = to_raw_response_wrapper(
            entities.merge,
        )
        self.search = to_raw_response_wrapper(
            entities.search,
        )
        self.summarize = to_raw_response_wrapper(
            entities.summarize,
        )
        self.trigger_merge = to_raw_response_wrapper(
            entities.trigger_merge,
        )
        self.update_property = to_raw_response_wrapper(
            entities.update_property,
        )
        self.verify = to_raw_response_wrapper(
            entities.verify,
        )
        self.view = to_raw_response_wrapper(
            entities.view,
        )


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.delete = async_to_raw_response_wrapper(
            entities.delete,
        )
        self.add = async_to_raw_response_wrapper(
            entities.add,
        )
        self.add_batch = async_to_raw_response_wrapper(
            entities.add_batch,
        )
        self.get = async_to_raw_response_wrapper(
            entities.get,
        )
        self.get_local_subgraph = async_to_raw_response_wrapper(
            entities.get_local_subgraph,
        )
        self.get_source_entities = async_to_raw_response_wrapper(
            entities.get_source_entities,
        )
        self.list_jobs = async_to_raw_response_wrapper(
            entities.list_jobs,
        )
        self.merge = async_to_raw_response_wrapper(
            entities.merge,
        )
        self.search = async_to_raw_response_wrapper(
            entities.search,
        )
        self.summarize = async_to_raw_response_wrapper(
            entities.summarize,
        )
        self.trigger_merge = async_to_raw_response_wrapper(
            entities.trigger_merge,
        )
        self.update_property = async_to_raw_response_wrapper(
            entities.update_property,
        )
        self.verify = async_to_raw_response_wrapper(
            entities.verify,
        )
        self.view = async_to_raw_response_wrapper(
            entities.view,
        )


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.delete = to_streamed_response_wrapper(
            entities.delete,
        )
        self.add = to_streamed_response_wrapper(
            entities.add,
        )
        self.add_batch = to_streamed_response_wrapper(
            entities.add_batch,
        )
        self.get = to_streamed_response_wrapper(
            entities.get,
        )
        self.get_local_subgraph = to_streamed_response_wrapper(
            entities.get_local_subgraph,
        )
        self.get_source_entities = to_streamed_response_wrapper(
            entities.get_source_entities,
        )
        self.list_jobs = to_streamed_response_wrapper(
            entities.list_jobs,
        )
        self.merge = to_streamed_response_wrapper(
            entities.merge,
        )
        self.search = to_streamed_response_wrapper(
            entities.search,
        )
        self.summarize = to_streamed_response_wrapper(
            entities.summarize,
        )
        self.trigger_merge = to_streamed_response_wrapper(
            entities.trigger_merge,
        )
        self.update_property = to_streamed_response_wrapper(
            entities.update_property,
        )
        self.verify = to_streamed_response_wrapper(
            entities.verify,
        )
        self.view = to_streamed_response_wrapper(
            entities.view,
        )


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.delete = async_to_streamed_response_wrapper(
            entities.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            entities.add,
        )
        self.add_batch = async_to_streamed_response_wrapper(
            entities.add_batch,
        )
        self.get = async_to_streamed_response_wrapper(
            entities.get,
        )
        self.get_local_subgraph = async_to_streamed_response_wrapper(
            entities.get_local_subgraph,
        )
        self.get_source_entities = async_to_streamed_response_wrapper(
            entities.get_source_entities,
        )
        self.list_jobs = async_to_streamed_response_wrapper(
            entities.list_jobs,
        )
        self.merge = async_to_streamed_response_wrapper(
            entities.merge,
        )
        self.search = async_to_streamed_response_wrapper(
            entities.search,
        )
        self.summarize = async_to_streamed_response_wrapper(
            entities.summarize,
        )
        self.trigger_merge = async_to_streamed_response_wrapper(
            entities.trigger_merge,
        )
        self.update_property = async_to_streamed_response_wrapper(
            entities.update_property,
        )
        self.verify = async_to_streamed_response_wrapper(
            entities.verify,
        )
        self.view = async_to_streamed_response_wrapper(
            entities.view,
        )
