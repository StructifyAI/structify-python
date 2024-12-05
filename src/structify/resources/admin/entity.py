# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import KnowledgeGraph
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import entity_verify_params
from ..._base_client import make_request_options
from ...types.knowledge_graph import KnowledgeGraph
from ...types.knowledge_graph_param import KnowledgeGraphParam

__all__ = ["EntityResource", "AsyncEntityResource"]


class EntityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return EntityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return EntityResourceWithStreamingResponse(self)

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
            "/admin/entity/verify",
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


class AsyncEntityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncEntityResourceWithStreamingResponse(self)

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
            "/admin/entity/verify",
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


class EntityResourceWithRawResponse:
    def __init__(self, entity: EntityResource) -> None:
        self._entity = entity

        self.verify = to_raw_response_wrapper(
            entity.verify,
        )


class AsyncEntityResourceWithRawResponse:
    def __init__(self, entity: AsyncEntityResource) -> None:
        self._entity = entity

        self.verify = async_to_raw_response_wrapper(
            entity.verify,
        )


class EntityResourceWithStreamingResponse:
    def __init__(self, entity: EntityResource) -> None:
        self._entity = entity

        self.verify = to_streamed_response_wrapper(
            entity.verify,
        )


class AsyncEntityResourceWithStreamingResponse:
    def __init__(self, entity: AsyncEntityResource) -> None:
        self._entity = entity

        self.verify = async_to_streamed_response_wrapper(
            entity.verify,
        )
