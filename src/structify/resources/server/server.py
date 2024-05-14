# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .version import (
    VersionResource,
    AsyncVersionResource,
    VersionResourceWithRawResponse,
    AsyncVersionResourceWithRawResponse,
    VersionResourceWithStreamingResponse,
    AsyncVersionResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ServerResource", "AsyncServerResource"]


class ServerResource(SyncAPIResource):
    @cached_property
    def version(self) -> VersionResource:
        return VersionResource(self._client)

    @cached_property
    def with_raw_response(self) -> ServerResourceWithRawResponse:
        return ServerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServerResourceWithStreamingResponse:
        return ServerResourceWithStreamingResponse(self)


class AsyncServerResource(AsyncAPIResource):
    @cached_property
    def version(self) -> AsyncVersionResource:
        return AsyncVersionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncServerResourceWithRawResponse:
        return AsyncServerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServerResourceWithStreamingResponse:
        return AsyncServerResourceWithStreamingResponse(self)


class ServerResourceWithRawResponse:
    def __init__(self, server: ServerResource) -> None:
        self._server = server

    @cached_property
    def version(self) -> VersionResourceWithRawResponse:
        return VersionResourceWithRawResponse(self._server.version)


class AsyncServerResourceWithRawResponse:
    def __init__(self, server: AsyncServerResource) -> None:
        self._server = server

    @cached_property
    def version(self) -> AsyncVersionResourceWithRawResponse:
        return AsyncVersionResourceWithRawResponse(self._server.version)


class ServerResourceWithStreamingResponse:
    def __init__(self, server: ServerResource) -> None:
        self._server = server

    @cached_property
    def version(self) -> VersionResourceWithStreamingResponse:
        return VersionResourceWithStreamingResponse(self._server.version)


class AsyncServerResourceWithStreamingResponse:
    def __init__(self, server: AsyncServerResource) -> None:
        self._server = server

    @cached_property
    def version(self) -> AsyncVersionResourceWithStreamingResponse:
        return AsyncVersionResourceWithStreamingResponse(self._server.version)
