# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import connector_clone_params
from ..._base_client import make_request_options
from ...types.admin.clone_connectors_response import CloneConnectorsResponse
from ...types.admin.clone_connector_item_param import CloneConnectorItemParam

__all__ = ["ConnectorResource", "AsyncConnectorResource"]


class ConnectorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return ConnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return ConnectorResourceWithStreamingResponse(self)

    def clone(
        self,
        *,
        connectors: Iterable[CloneConnectorItemParam],
        source_membership_id: str,
        source_team_id: str,
        target_team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloneConnectorsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/connector/clone",
            body=maybe_transform(
                {
                    "connectors": connectors,
                    "source_membership_id": source_membership_id,
                    "source_team_id": source_team_id,
                    "target_team_id": target_team_id,
                },
                connector_clone_params.ConnectorCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloneConnectorsResponse,
        )


class AsyncConnectorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncConnectorResourceWithStreamingResponse(self)

    async def clone(
        self,
        *,
        connectors: Iterable[CloneConnectorItemParam],
        source_membership_id: str,
        source_team_id: str,
        target_team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloneConnectorsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/connector/clone",
            body=await async_maybe_transform(
                {
                    "connectors": connectors,
                    "source_membership_id": source_membership_id,
                    "source_team_id": source_team_id,
                    "target_team_id": target_team_id,
                },
                connector_clone_params.ConnectorCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloneConnectorsResponse,
        )


class ConnectorResourceWithRawResponse:
    def __init__(self, connector: ConnectorResource) -> None:
        self._connector = connector

        self.clone = to_raw_response_wrapper(
            connector.clone,
        )


class AsyncConnectorResourceWithRawResponse:
    def __init__(self, connector: AsyncConnectorResource) -> None:
        self._connector = connector

        self.clone = async_to_raw_response_wrapper(
            connector.clone,
        )


class ConnectorResourceWithStreamingResponse:
    def __init__(self, connector: ConnectorResource) -> None:
        self._connector = connector

        self.clone = to_streamed_response_wrapper(
            connector.clone,
        )


class AsyncConnectorResourceWithStreamingResponse:
    def __init__(self, connector: AsyncConnectorResource) -> None:
        self._connector = connector

        self.clone = async_to_streamed_response_wrapper(
            connector.clone,
        )
