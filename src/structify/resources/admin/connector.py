# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import (
    DatahubIngestionType,
    connector_clone_params,
    connector_set_datahub_config_params,
)
from ..._base_client import make_request_options
from ...types.connector import Connector
from ...types.admin.datahub_ingestion_type import DatahubIngestionType
from ...types.admin.datahub_secret_map_param import DatahubSecretMapParam
from ...types.admin.clone_connectors_response import CloneConnectorsResponse
from ...types.admin.clone_connector_item_param import CloneConnectorItemParam
from ...types.admin.admin_list_connectors_response import AdminListConnectorsResponse

__all__ = ["ConnectorResource", "AsyncConnectorResource"]


class ConnectorResource(SyncAPIResource):
    """Admin endpoints"""

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

    def list_team_connectors(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminListConnectorsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._get(
            path_template("/admin/connector/team/{team_id}", team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminListConnectorsResponse,
        )

    def set_datahub_config(
        self,
        *,
        connector_id: str,
        datahub_ingestion_type: Optional[DatahubIngestionType] | Omit = omit,
        datahub_secret_map: Optional[DatahubSecretMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connector:
        """
        Args:
          datahub_secret_map: Maps DatahubIngestionKey to the name of the connector secret that holds the
              value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/connector/datahub-config",
            body=maybe_transform(
                {
                    "connector_id": connector_id,
                    "datahub_ingestion_type": datahub_ingestion_type,
                    "datahub_secret_map": datahub_secret_map,
                },
                connector_set_datahub_config_params.ConnectorSetDatahubConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connector,
        )


class AsyncConnectorResource(AsyncAPIResource):
    """Admin endpoints"""

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

    async def list_team_connectors(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminListConnectorsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._get(
            path_template("/admin/connector/team/{team_id}", team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminListConnectorsResponse,
        )

    async def set_datahub_config(
        self,
        *,
        connector_id: str,
        datahub_ingestion_type: Optional[DatahubIngestionType] | Omit = omit,
        datahub_secret_map: Optional[DatahubSecretMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connector:
        """
        Args:
          datahub_secret_map: Maps DatahubIngestionKey to the name of the connector secret that holds the
              value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/connector/datahub-config",
            body=await async_maybe_transform(
                {
                    "connector_id": connector_id,
                    "datahub_ingestion_type": datahub_ingestion_type,
                    "datahub_secret_map": datahub_secret_map,
                },
                connector_set_datahub_config_params.ConnectorSetDatahubConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connector,
        )


class ConnectorResourceWithRawResponse:
    def __init__(self, connector: ConnectorResource) -> None:
        self._connector = connector

        self.clone = to_raw_response_wrapper(
            connector.clone,
        )
        self.list_team_connectors = to_raw_response_wrapper(
            connector.list_team_connectors,
        )
        self.set_datahub_config = to_raw_response_wrapper(
            connector.set_datahub_config,
        )


class AsyncConnectorResourceWithRawResponse:
    def __init__(self, connector: AsyncConnectorResource) -> None:
        self._connector = connector

        self.clone = async_to_raw_response_wrapper(
            connector.clone,
        )
        self.list_team_connectors = async_to_raw_response_wrapper(
            connector.list_team_connectors,
        )
        self.set_datahub_config = async_to_raw_response_wrapper(
            connector.set_datahub_config,
        )


class ConnectorResourceWithStreamingResponse:
    def __init__(self, connector: ConnectorResource) -> None:
        self._connector = connector

        self.clone = to_streamed_response_wrapper(
            connector.clone,
        )
        self.list_team_connectors = to_streamed_response_wrapper(
            connector.list_team_connectors,
        )
        self.set_datahub_config = to_streamed_response_wrapper(
            connector.set_datahub_config,
        )


class AsyncConnectorResourceWithStreamingResponse:
    def __init__(self, connector: AsyncConnectorResource) -> None:
        self._connector = connector

        self.clone = async_to_streamed_response_wrapper(
            connector.clone,
        )
        self.list_team_connectors = async_to_streamed_response_wrapper(
            connector.list_team_connectors,
        )
        self.set_datahub_config = async_to_streamed_response_wrapper(
            connector.set_datahub_config,
        )
