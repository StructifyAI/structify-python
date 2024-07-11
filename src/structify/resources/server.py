# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.server_information import ServerInformation

__all__ = ["ServerResource", "AsyncServerResource"]


class ServerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServerResourceWithRawResponse:
        return ServerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServerResourceWithStreamingResponse:
        return ServerResourceWithStreamingResponse(self)

    def version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServerInformation:
        """Gets the version of the API server."""
        return self._get(
            "/server/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerInformation,
        )


class AsyncServerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServerResourceWithRawResponse:
        return AsyncServerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServerResourceWithStreamingResponse:
        return AsyncServerResourceWithStreamingResponse(self)

    async def version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServerInformation:
        """Gets the version of the API server."""
        return await self._get(
            "/server/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerInformation,
        )


class ServerResourceWithRawResponse:
    def __init__(self, server: ServerResource) -> None:
        self._server = server

        self.version = to_raw_response_wrapper(
            server.version,
        )


class AsyncServerResourceWithRawResponse:
    def __init__(self, server: AsyncServerResource) -> None:
        self._server = server

        self.version = async_to_raw_response_wrapper(
            server.version,
        )


class ServerResourceWithStreamingResponse:
    def __init__(self, server: ServerResource) -> None:
        self._server = server

        self.version = to_streamed_response_wrapper(
            server.version,
        )


class AsyncServerResourceWithStreamingResponse:
    def __init__(self, server: AsyncServerResource) -> None:
        self._server = server

        self.version = async_to_streamed_response_wrapper(
            server.version,
        )
