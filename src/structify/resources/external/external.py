# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .news import (
    NewsResource,
    AsyncNewsResource,
    NewsResourceWithRawResponse,
    AsyncNewsResourceWithRawResponse,
    NewsResourceWithStreamingResponse,
    AsyncNewsResourceWithStreamingResponse,
)
from .people import (
    PeopleResource,
    AsyncPeopleResource,
    PeopleResourceWithRawResponse,
    AsyncPeopleResourceWithRawResponse,
    PeopleResourceWithStreamingResponse,
    AsyncPeopleResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .search_api import (
    SearchAPIResource,
    AsyncSearchAPIResource,
    SearchAPIResourceWithRawResponse,
    AsyncSearchAPIResourceWithRawResponse,
    SearchAPIResourceWithStreamingResponse,
    AsyncSearchAPIResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ExternalResource", "AsyncExternalResource"]


class ExternalResource(SyncAPIResource):
    @cached_property
    def news(self) -> NewsResource:
        return NewsResource(self._client)

    @cached_property
    def search_api(self) -> SearchAPIResource:
        return SearchAPIResource(self._client)

    @cached_property
    def people(self) -> PeopleResource:
        return PeopleResource(self._client)

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


class AsyncExternalResource(AsyncAPIResource):
    @cached_property
    def news(self) -> AsyncNewsResource:
        return AsyncNewsResource(self._client)

    @cached_property
    def search_api(self) -> AsyncSearchAPIResource:
        return AsyncSearchAPIResource(self._client)

    @cached_property
    def people(self) -> AsyncPeopleResource:
        return AsyncPeopleResource(self._client)

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


class ExternalResourceWithRawResponse:
    def __init__(self, external: ExternalResource) -> None:
        self._external = external

    @cached_property
    def news(self) -> NewsResourceWithRawResponse:
        return NewsResourceWithRawResponse(self._external.news)

    @cached_property
    def search_api(self) -> SearchAPIResourceWithRawResponse:
        return SearchAPIResourceWithRawResponse(self._external.search_api)

    @cached_property
    def people(self) -> PeopleResourceWithRawResponse:
        return PeopleResourceWithRawResponse(self._external.people)


class AsyncExternalResourceWithRawResponse:
    def __init__(self, external: AsyncExternalResource) -> None:
        self._external = external

    @cached_property
    def news(self) -> AsyncNewsResourceWithRawResponse:
        return AsyncNewsResourceWithRawResponse(self._external.news)

    @cached_property
    def search_api(self) -> AsyncSearchAPIResourceWithRawResponse:
        return AsyncSearchAPIResourceWithRawResponse(self._external.search_api)

    @cached_property
    def people(self) -> AsyncPeopleResourceWithRawResponse:
        return AsyncPeopleResourceWithRawResponse(self._external.people)


class ExternalResourceWithStreamingResponse:
    def __init__(self, external: ExternalResource) -> None:
        self._external = external

    @cached_property
    def news(self) -> NewsResourceWithStreamingResponse:
        return NewsResourceWithStreamingResponse(self._external.news)

    @cached_property
    def search_api(self) -> SearchAPIResourceWithStreamingResponse:
        return SearchAPIResourceWithStreamingResponse(self._external.search_api)

    @cached_property
    def people(self) -> PeopleResourceWithStreamingResponse:
        return PeopleResourceWithStreamingResponse(self._external.people)


class AsyncExternalResourceWithStreamingResponse:
    def __init__(self, external: AsyncExternalResource) -> None:
        self._external = external

    @cached_property
    def news(self) -> AsyncNewsResourceWithStreamingResponse:
        return AsyncNewsResourceWithStreamingResponse(self._external.news)

    @cached_property
    def search_api(self) -> AsyncSearchAPIResourceWithStreamingResponse:
        return AsyncSearchAPIResourceWithStreamingResponse(self._external.search_api)

    @cached_property
    def people(self) -> AsyncPeopleResourceWithStreamingResponse:
        return AsyncPeopleResourceWithStreamingResponse(self._external.people)
