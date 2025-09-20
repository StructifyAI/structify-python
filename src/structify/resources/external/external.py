# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .apollo import (
    ApolloResource,
    AsyncApolloResource,
    ApolloResourceWithRawResponse,
    AsyncApolloResourceWithRawResponse,
    ApolloResourceWithStreamingResponse,
    AsyncApolloResourceWithStreamingResponse,
)
from ...types import external_search_params
from .newsapi import (
    NewsapiResource,
    AsyncNewsapiResource,
    NewsapiResourceWithRawResponse,
    AsyncNewsapiResourceWithRawResponse,
    NewsapiResourceWithStreamingResponse,
    AsyncNewsapiResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .searchapi import (
    SearchapiResource,
    AsyncSearchapiResource,
    SearchapiResourceWithRawResponse,
    AsyncSearchapiResourceWithRawResponse,
    SearchapiResourceWithStreamingResponse,
    AsyncSearchapiResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.external_search_response import ExternalSearchResponse

__all__ = ["ExternalResource", "AsyncExternalResource"]


class ExternalResource(SyncAPIResource):
    @cached_property
    def newsapi(self) -> NewsapiResource:
        return NewsapiResource(self._client)

    @cached_property
    def searchapi(self) -> SearchapiResource:
        return SearchapiResource(self._client)

    @cached_property
    def apollo(self) -> ApolloResource:
        return ApolloResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExternalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return ExternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return ExternalResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalSearchResponse:
        """
        This endpoint provides web search functionality by leveraging the existing agent
        search infrastructure.

        Args:
          query: The search query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/search",
            body=maybe_transform({"query": query}, external_search_params.ExternalSearchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalSearchResponse,
        )


class AsyncExternalResource(AsyncAPIResource):
    @cached_property
    def newsapi(self) -> AsyncNewsapiResource:
        return AsyncNewsapiResource(self._client)

    @cached_property
    def searchapi(self) -> AsyncSearchapiResource:
        return AsyncSearchapiResource(self._client)

    @cached_property
    def apollo(self) -> AsyncApolloResource:
        return AsyncApolloResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExternalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncExternalResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalSearchResponse:
        """
        This endpoint provides web search functionality by leveraging the existing agent
        search infrastructure.

        Args:
          query: The search query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/search",
            body=await async_maybe_transform({"query": query}, external_search_params.ExternalSearchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalSearchResponse,
        )


class ExternalResourceWithRawResponse:
    def __init__(self, external: ExternalResource) -> None:
        self._external = external

        self.search = to_raw_response_wrapper(
            external.search,
        )

    @cached_property
    def newsapi(self) -> NewsapiResourceWithRawResponse:
        return NewsapiResourceWithRawResponse(self._external.newsapi)

    @cached_property
    def searchapi(self) -> SearchapiResourceWithRawResponse:
        return SearchapiResourceWithRawResponse(self._external.searchapi)

    @cached_property
    def apollo(self) -> ApolloResourceWithRawResponse:
        return ApolloResourceWithRawResponse(self._external.apollo)


class AsyncExternalResourceWithRawResponse:
    def __init__(self, external: AsyncExternalResource) -> None:
        self._external = external

        self.search = async_to_raw_response_wrapper(
            external.search,
        )

    @cached_property
    def newsapi(self) -> AsyncNewsapiResourceWithRawResponse:
        return AsyncNewsapiResourceWithRawResponse(self._external.newsapi)

    @cached_property
    def searchapi(self) -> AsyncSearchapiResourceWithRawResponse:
        return AsyncSearchapiResourceWithRawResponse(self._external.searchapi)

    @cached_property
    def apollo(self) -> AsyncApolloResourceWithRawResponse:
        return AsyncApolloResourceWithRawResponse(self._external.apollo)


class ExternalResourceWithStreamingResponse:
    def __init__(self, external: ExternalResource) -> None:
        self._external = external

        self.search = to_streamed_response_wrapper(
            external.search,
        )

    @cached_property
    def newsapi(self) -> NewsapiResourceWithStreamingResponse:
        return NewsapiResourceWithStreamingResponse(self._external.newsapi)

    @cached_property
    def searchapi(self) -> SearchapiResourceWithStreamingResponse:
        return SearchapiResourceWithStreamingResponse(self._external.searchapi)

    @cached_property
    def apollo(self) -> ApolloResourceWithStreamingResponse:
        return ApolloResourceWithStreamingResponse(self._external.apollo)


class AsyncExternalResourceWithStreamingResponse:
    def __init__(self, external: AsyncExternalResource) -> None:
        self._external = external

        self.search = async_to_streamed_response_wrapper(
            external.search,
        )

    @cached_property
    def newsapi(self) -> AsyncNewsapiResourceWithStreamingResponse:
        return AsyncNewsapiResourceWithStreamingResponse(self._external.newsapi)

    @cached_property
    def searchapi(self) -> AsyncSearchapiResourceWithStreamingResponse:
        return AsyncSearchapiResourceWithStreamingResponse(self._external.searchapi)

    @cached_property
    def apollo(self) -> AsyncApolloResourceWithStreamingResponse:
        return AsyncApolloResourceWithStreamingResponse(self._external.apollo)
