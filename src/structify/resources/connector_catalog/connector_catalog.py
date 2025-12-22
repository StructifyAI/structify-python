# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .admin import (
    AdminResource,
    AsyncAdminResource,
    AdminResourceWithRawResponse,
    AsyncAdminResourceWithRawResponse,
    AdminResourceWithStreamingResponse,
    AsyncAdminResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.connector_catalog_with_methods import ConnectorCatalogWithMethods
from ...types.connector_catalog_list_response import ConnectorCatalogListResponse

__all__ = ["ConnectorCatalogResource", "AsyncConnectorCatalogResource"]


class ConnectorCatalogResource(SyncAPIResource):
    @cached_property
    def admin(self) -> AdminResource:
        return AdminResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectorCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return ConnectorCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return ConnectorCatalogResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCatalogListResponse:
        """List all connector catalog entries with their active auth methods"""
        return self._get(
            "/connector-catalog",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCatalogListResponse,
        )

    def get(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCatalogWithMethods:
        """
        Get a connector catalog entry by slug with its active auth methods

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            f"/connector-catalog/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCatalogWithMethods,
        )


class AsyncConnectorCatalogResource(AsyncAPIResource):
    @cached_property
    def admin(self) -> AsyncAdminResource:
        return AsyncAdminResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectorCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncConnectorCatalogResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCatalogListResponse:
        """List all connector catalog entries with their active auth methods"""
        return await self._get(
            "/connector-catalog",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCatalogListResponse,
        )

    async def get(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCatalogWithMethods:
        """
        Get a connector catalog entry by slug with its active auth methods

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            f"/connector-catalog/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCatalogWithMethods,
        )


class ConnectorCatalogResourceWithRawResponse:
    def __init__(self, connector_catalog: ConnectorCatalogResource) -> None:
        self._connector_catalog = connector_catalog

        self.list = to_raw_response_wrapper(
            connector_catalog.list,
        )
        self.get = to_raw_response_wrapper(
            connector_catalog.get,
        )

    @cached_property
    def admin(self) -> AdminResourceWithRawResponse:
        return AdminResourceWithRawResponse(self._connector_catalog.admin)


class AsyncConnectorCatalogResourceWithRawResponse:
    def __init__(self, connector_catalog: AsyncConnectorCatalogResource) -> None:
        self._connector_catalog = connector_catalog

        self.list = async_to_raw_response_wrapper(
            connector_catalog.list,
        )
        self.get = async_to_raw_response_wrapper(
            connector_catalog.get,
        )

    @cached_property
    def admin(self) -> AsyncAdminResourceWithRawResponse:
        return AsyncAdminResourceWithRawResponse(self._connector_catalog.admin)


class ConnectorCatalogResourceWithStreamingResponse:
    def __init__(self, connector_catalog: ConnectorCatalogResource) -> None:
        self._connector_catalog = connector_catalog

        self.list = to_streamed_response_wrapper(
            connector_catalog.list,
        )
        self.get = to_streamed_response_wrapper(
            connector_catalog.get,
        )

    @cached_property
    def admin(self) -> AdminResourceWithStreamingResponse:
        return AdminResourceWithStreamingResponse(self._connector_catalog.admin)


class AsyncConnectorCatalogResourceWithStreamingResponse:
    def __init__(self, connector_catalog: AsyncConnectorCatalogResource) -> None:
        self._connector_catalog = connector_catalog

        self.list = async_to_streamed_response_wrapper(
            connector_catalog.list,
        )
        self.get = async_to_streamed_response_wrapper(
            connector_catalog.get,
        )

    @cached_property
    def admin(self) -> AsyncAdminResourceWithStreamingResponse:
        return AsyncAdminResourceWithStreamingResponse(self._connector_catalog.admin)
