# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..types import source_list_sources_params
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
from .._base_client import (
    make_request_options,
)
from ..types.source import Source

__all__ = ["SourceResource", "AsyncSourceResource"]


class SourceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SourceResourceWithRawResponse:
        return SourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourceResourceWithStreamingResponse:
        return SourceResourceWithStreamingResponse(self)

    def list_sources(
        self,
        *,
        id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Source:
        """
        Get all sources for a given entity

        Args:
          id: Id of the entity to get sources for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Source,
            self._get(
                "/source/get_sources",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"id": id}, source_list_sources_params.SourceListSourcesParams),
                ),
                cast_to=cast(Any, Source),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncSourceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSourceResourceWithRawResponse:
        return AsyncSourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourceResourceWithStreamingResponse:
        return AsyncSourceResourceWithStreamingResponse(self)

    async def list_sources(
        self,
        *,
        id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Source:
        """
        Get all sources for a given entity

        Args:
          id: Id of the entity to get sources for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Source,
            await self._get(
                "/source/get_sources",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform({"id": id}, source_list_sources_params.SourceListSourcesParams),
                ),
                cast_to=cast(Any, Source),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SourceResourceWithRawResponse:
    def __init__(self, source: SourceResource) -> None:
        self._source = source

        self.list_sources = to_raw_response_wrapper(
            source.list_sources,
        )


class AsyncSourceResourceWithRawResponse:
    def __init__(self, source: AsyncSourceResource) -> None:
        self._source = source

        self.list_sources = async_to_raw_response_wrapper(
            source.list_sources,
        )


class SourceResourceWithStreamingResponse:
    def __init__(self, source: SourceResource) -> None:
        self._source = source

        self.list_sources = to_streamed_response_wrapper(
            source.list_sources,
        )


class AsyncSourceResourceWithStreamingResponse:
    def __init__(self, source: AsyncSourceResource) -> None:
        self._source = source

        self.list_sources = async_to_streamed_response_wrapper(
            source.list_sources,
        )
