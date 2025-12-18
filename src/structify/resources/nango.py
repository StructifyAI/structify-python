# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.nango_create_session_response import NangoCreateSessionResponse
from ..types.nango_list_integrations_response import NangoListIntegrationsResponse

__all__ = ["NangoResource", "AsyncNangoResource"]


class NangoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NangoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return NangoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NangoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return NangoResourceWithStreamingResponse(self)

    def create_session(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NangoCreateSessionResponse:
        return self._post(
            "/nango/session",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NangoCreateSessionResponse,
        )

    def list_integrations(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NangoListIntegrationsResponse:
        return self._get(
            "/nango/integrations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NangoListIntegrationsResponse,
        )


class AsyncNangoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNangoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNangoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNangoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncNangoResourceWithStreamingResponse(self)

    async def create_session(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NangoCreateSessionResponse:
        return await self._post(
            "/nango/session",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NangoCreateSessionResponse,
        )

    async def list_integrations(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NangoListIntegrationsResponse:
        return await self._get(
            "/nango/integrations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NangoListIntegrationsResponse,
        )


class NangoResourceWithRawResponse:
    def __init__(self, nango: NangoResource) -> None:
        self._nango = nango

        self.create_session = to_raw_response_wrapper(
            nango.create_session,
        )
        self.list_integrations = to_raw_response_wrapper(
            nango.list_integrations,
        )


class AsyncNangoResourceWithRawResponse:
    def __init__(self, nango: AsyncNangoResource) -> None:
        self._nango = nango

        self.create_session = async_to_raw_response_wrapper(
            nango.create_session,
        )
        self.list_integrations = async_to_raw_response_wrapper(
            nango.list_integrations,
        )


class NangoResourceWithStreamingResponse:
    def __init__(self, nango: NangoResource) -> None:
        self._nango = nango

        self.create_session = to_streamed_response_wrapper(
            nango.create_session,
        )
        self.list_integrations = to_streamed_response_wrapper(
            nango.list_integrations,
        )


class AsyncNangoResourceWithStreamingResponse:
    def __init__(self, nango: AsyncNangoResource) -> None:
        self._nango = nango

        self.create_session = async_to_streamed_response_wrapper(
            nango.create_session,
        )
        self.list_integrations = async_to_streamed_response_wrapper(
            nango.list_integrations,
        )
