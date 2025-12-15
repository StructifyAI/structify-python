# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, overload

import httpx

from ...types import (
    connector_list_params,
    connector_create_params,
    connector_update_params,
    connector_explore_params,
    connector_update_table_params,
    connector_create_secret_params,
    connector_search_tables_params,
    connector_update_column_params,
    connector_get_explorer_chat_params,
    connector_list_with_snippets_params,
    connector_delete_schema_object_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncJobsList, AsyncJobsList
from .type_snippets import (
    TypeSnippetsResource,
    AsyncTypeSnippetsResource,
    TypeSnippetsResourceWithRawResponse,
    AsyncTypeSnippetsResourceWithRawResponse,
    TypeSnippetsResourceWithStreamingResponse,
    AsyncTypeSnippetsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.connector import Connector
from ...types.list_tables_response import ListTablesResponse
from ...types.update_table_response import UpdateTableResponse
from ...types.connector_get_response import ConnectorGetResponse
from ...types.connector_with_secrets import ConnectorWithSecrets
from ...types.explorer_chat_response import ExplorerChatResponse
from ...types.explore_status_response import ExploreStatusResponse
from ...types.connector_store_response import ConnectorStoreResponse
from ...types.exploration_runs_response import ExplorationRunsResponse
from ...types.delete_schema_object_response import DeleteSchemaObjectResponse
from ...types.connector_search_tables_response import ConnectorSearchTablesResponse
from ...types.connector_list_with_snippets_response import ConnectorListWithSnippetsResponse
from ...types.connector_get_clarification_requests_response import ConnectorGetClarificationRequestsResponse

__all__ = ["ConnectorsResource", "AsyncConnectorsResource"]


class ConnectorsResource(SyncAPIResource):
    @cached_property
    def type_snippets(self) -> TypeSnippetsResource:
        return TypeSnippetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return ConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return ConnectorsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        known_connector_type: str,
        name: str,
        team_id: str,
        description: Optional[str] | Omit = omit,
        nango_connection_id: Optional[str] | Omit = omit,
        nango_integration_id: Optional[str] | Omit = omit,
        pipedream_account_id: Optional[str] | Omit = omit,
        pipedream_external_id: Optional[str] | Omit = omit,
        pipedream_project_id: Optional[str] | Omit = omit,
        refresh_script: Optional[str] | Omit = omit,
        secrets: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connector:
        """
        Args:
          nango_connection_id: Nango connection ID for OAuth token management

          nango_integration_id: Nango integration ID (e.g., "linear", "slack")

          pipedream_external_id: Unique external ID for Pipedream routing (required for Pipedream connectors)

          secrets: Optional secrets/environment variables for the connector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/connectors",
            body=maybe_transform(
                {
                    "known_connector_type": known_connector_type,
                    "name": name,
                    "team_id": team_id,
                    "description": description,
                    "nango_connection_id": nango_connection_id,
                    "nango_integration_id": nango_integration_id,
                    "pipedream_account_id": pipedream_account_id,
                    "pipedream_external_id": pipedream_external_id,
                    "pipedream_project_id": pipedream_project_id,
                    "refresh_script": refresh_script,
                    "secrets": secrets,
                },
                connector_create_params.ConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connector,
        )

    def update(
        self,
        connector_id: str,
        *,
        description: Optional[str] | Omit = omit,
        known_connector_type: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        refresh_script: Optional[str] | Omit = omit,
        usage_snippet_override: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/connectors/{connector_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "known_connector_type": known_connector_type,
                    "name": name,
                    "refresh_script": refresh_script,
                    "usage_snippet_override": usage_snippet_override,
                },
                connector_update_params.ConnectorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        team_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncJobsList[ConnectorWithSecrets]:
        """
        Args:
          team_id: Team ID to list connectors for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/connectors",
            page=SyncJobsList[ConnectorWithSecrets],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "team_id": team_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    connector_list_params.ConnectorListParams,
                ),
            ),
            model=ConnectorWithSecrets,
        )

    def delete(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_secret(
        self,
        connector_id: str,
        *,
        secret_name: str,
        secret_value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/connectors/{connector_id}/secrets",
            body=maybe_transform(
                {
                    "secret_name": secret_name,
                    "secret_value": secret_value,
                },
                connector_create_secret_params.ConnectorCreateSecretParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    def delete_schema_object(
        self,
        connector_id: str,
        *,
        id: str,
        type: Literal["column"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteSchemaObjectResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def delete_schema_object(
        self,
        connector_id: str,
        *,
        id: str,
        type: Literal["table"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteSchemaObjectResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def delete_schema_object(
        self,
        connector_id: str,
        *,
        id: str,
        type: Literal["schema"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteSchemaObjectResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def delete_schema_object(
        self,
        connector_id: str,
        *,
        id: str,
        type: Literal["database"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteSchemaObjectResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["id", "type"])
    def delete_schema_object(
        self,
        connector_id: str,
        *,
        id: str,
        type: Literal["column"] | Literal["table"] | Literal["schema"] | Literal["database"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteSchemaObjectResponse:
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._delete(
            f"/connectors/{connector_id}/schema_object",
            body=maybe_transform(
                {
                    "id": id,
                    "type": type,
                },
                connector_delete_schema_object_params.ConnectorDeleteSchemaObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteSchemaObjectResponse,
        )

    def delete_secret(
        self,
        secret_name: str,
        *,
        connector_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/connectors/{connector_id}/secrets/{secret_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def explore(
        self,
        connector_id: str,
        *,
        database_id: Optional[str] | Omit = omit,
        schema_id: Optional[str] | Omit = omit,
        stage: Optional[Literal["both", "ingestion", "annotation"]] | Omit = omit,
        table_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          stage: Which exploration stage to run

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/connectors/{connector_id}/explore",
            body=maybe_transform(
                {
                    "database_id": database_id,
                    "schema_id": schema_id,
                    "stage": stage,
                    "table_id": table_id,
                },
                connector_explore_params.ConnectorExploreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorGetResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorGetResponse,
        )

    def get_clarification_requests(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorGetClarificationRequestsResponse:
        """
        Get all clarification requests for a connector

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/connectors/{connector_id}/clarification-requests",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorGetClarificationRequestsResponse,
        )

    def get_exploration_runs(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExplorationRunsResponse:
        """
        Get all exploration runs for a connector (requires debug permission)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/connectors/{connector_id}/explore/runs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExplorationRunsResponse,
        )

    def get_exploration_status(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExploreStatusResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/connectors/{connector_id}/explore/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExploreStatusResponse,
        )

    def get_explorer_chat(
        self,
        connector_id: str,
        *,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExplorerChatResponse:
        """
        Returns chats for all phases (table discovery, column discovery for each table,
        etc.)

        Args:
          run_id: Exploration run ID (required)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/connectors/{connector_id}/explore/chat",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"run_id": run_id}, connector_get_explorer_chat_params.ConnectorGetExplorerChatParams
                ),
            ),
            cast_to=ExplorerChatResponse,
        )

    def get_store(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorStoreResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/connectors/{connector_id}/store",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorStoreResponse,
        )

    def list_tables(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListTablesResponse:
        """
        Returns all tables across all databases and schemas for the given connector.
        Useful for finding table IDs to pass to the explore endpoint for single-table
        exploration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/connectors/{connector_id}/tables",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListTablesResponse,
        )

    def list_with_snippets(
        self,
        *,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListWithSnippetsResponse:
        """
        Args:
          team_id: Team ID to list connectors for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/connectors/with-snippets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"team_id": team_id}, connector_list_with_snippets_params.ConnectorListWithSnippetsParams
                ),
            ),
            cast_to=ConnectorListWithSnippetsResponse,
        )

    def resolve_clarification(
        self,
        clarification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Mark a clarification request as resolved

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clarification_id:
            raise ValueError(f"Expected a non-empty value for `clarification_id` but received {clarification_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/connectors/clarification-requests/{clarification_id}/resolve",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def search_tables(
        self,
        *,
        query: str,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorSearchTablesResponse:
        """
        Args:
          query: Search query string

          team_id: Team ID to search tables for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/connectors/search-tables",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "team_id": team_id,
                    },
                    connector_search_tables_params.ConnectorSearchTablesParams,
                ),
            ),
            cast_to=ConnectorSearchTablesResponse,
        )

    def update_column(
        self,
        column_id: str,
        *,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update column metadata (notes)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not column_id:
            raise ValueError(f"Expected a non-empty value for `column_id` but received {column_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/connectors/columns/{column_id}",
            body=maybe_transform({"notes": notes}, connector_update_column_params.ConnectorUpdateColumnParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_table(
        self,
        table_id: str,
        *,
        description: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateTableResponse:
        """
        Update table metadata (description or notes)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        return self._patch(
            f"/connectors/tables/{table_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "notes": notes,
                },
                connector_update_table_params.ConnectorUpdateTableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateTableResponse,
        )


class AsyncConnectorsResource(AsyncAPIResource):
    @cached_property
    def type_snippets(self) -> AsyncTypeSnippetsResource:
        return AsyncTypeSnippetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncConnectorsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        known_connector_type: str,
        name: str,
        team_id: str,
        description: Optional[str] | Omit = omit,
        nango_connection_id: Optional[str] | Omit = omit,
        nango_integration_id: Optional[str] | Omit = omit,
        pipedream_account_id: Optional[str] | Omit = omit,
        pipedream_external_id: Optional[str] | Omit = omit,
        pipedream_project_id: Optional[str] | Omit = omit,
        refresh_script: Optional[str] | Omit = omit,
        secrets: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connector:
        """
        Args:
          nango_connection_id: Nango connection ID for OAuth token management

          nango_integration_id: Nango integration ID (e.g., "linear", "slack")

          pipedream_external_id: Unique external ID for Pipedream routing (required for Pipedream connectors)

          secrets: Optional secrets/environment variables for the connector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/connectors",
            body=await async_maybe_transform(
                {
                    "known_connector_type": known_connector_type,
                    "name": name,
                    "team_id": team_id,
                    "description": description,
                    "nango_connection_id": nango_connection_id,
                    "nango_integration_id": nango_integration_id,
                    "pipedream_account_id": pipedream_account_id,
                    "pipedream_external_id": pipedream_external_id,
                    "pipedream_project_id": pipedream_project_id,
                    "refresh_script": refresh_script,
                    "secrets": secrets,
                },
                connector_create_params.ConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connector,
        )

    async def update(
        self,
        connector_id: str,
        *,
        description: Optional[str] | Omit = omit,
        known_connector_type: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        refresh_script: Optional[str] | Omit = omit,
        usage_snippet_override: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/connectors/{connector_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "known_connector_type": known_connector_type,
                    "name": name,
                    "refresh_script": refresh_script,
                    "usage_snippet_override": usage_snippet_override,
                },
                connector_update_params.ConnectorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        team_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ConnectorWithSecrets, AsyncJobsList[ConnectorWithSecrets]]:
        """
        Args:
          team_id: Team ID to list connectors for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/connectors",
            page=AsyncJobsList[ConnectorWithSecrets],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "team_id": team_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    connector_list_params.ConnectorListParams,
                ),
            ),
            model=ConnectorWithSecrets,
        )

    async def delete(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_secret(
        self,
        connector_id: str,
        *,
        secret_name: str,
        secret_value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/connectors/{connector_id}/secrets",
            body=await async_maybe_transform(
                {
                    "secret_name": secret_name,
                    "secret_value": secret_value,
                },
                connector_create_secret_params.ConnectorCreateSecretParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    async def delete_schema_object(
        self,
        connector_id: str,
        *,
        id: str,
        type: Literal["column"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteSchemaObjectResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def delete_schema_object(
        self,
        connector_id: str,
        *,
        id: str,
        type: Literal["table"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteSchemaObjectResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def delete_schema_object(
        self,
        connector_id: str,
        *,
        id: str,
        type: Literal["schema"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteSchemaObjectResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def delete_schema_object(
        self,
        connector_id: str,
        *,
        id: str,
        type: Literal["database"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteSchemaObjectResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["id", "type"])
    async def delete_schema_object(
        self,
        connector_id: str,
        *,
        id: str,
        type: Literal["column"] | Literal["table"] | Literal["schema"] | Literal["database"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteSchemaObjectResponse:
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._delete(
            f"/connectors/{connector_id}/schema_object",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "type": type,
                },
                connector_delete_schema_object_params.ConnectorDeleteSchemaObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteSchemaObjectResponse,
        )

    async def delete_secret(
        self,
        secret_name: str,
        *,
        connector_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/connectors/{connector_id}/secrets/{secret_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def explore(
        self,
        connector_id: str,
        *,
        database_id: Optional[str] | Omit = omit,
        schema_id: Optional[str] | Omit = omit,
        stage: Optional[Literal["both", "ingestion", "annotation"]] | Omit = omit,
        table_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          stage: Which exploration stage to run

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/connectors/{connector_id}/explore",
            body=await async_maybe_transform(
                {
                    "database_id": database_id,
                    "schema_id": schema_id,
                    "stage": stage,
                    "table_id": table_id,
                },
                connector_explore_params.ConnectorExploreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorGetResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorGetResponse,
        )

    async def get_clarification_requests(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorGetClarificationRequestsResponse:
        """
        Get all clarification requests for a connector

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/connectors/{connector_id}/clarification-requests",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorGetClarificationRequestsResponse,
        )

    async def get_exploration_runs(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExplorationRunsResponse:
        """
        Get all exploration runs for a connector (requires debug permission)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/connectors/{connector_id}/explore/runs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExplorationRunsResponse,
        )

    async def get_exploration_status(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExploreStatusResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/connectors/{connector_id}/explore/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExploreStatusResponse,
        )

    async def get_explorer_chat(
        self,
        connector_id: str,
        *,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExplorerChatResponse:
        """
        Returns chats for all phases (table discovery, column discovery for each table,
        etc.)

        Args:
          run_id: Exploration run ID (required)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/connectors/{connector_id}/explore/chat",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"run_id": run_id}, connector_get_explorer_chat_params.ConnectorGetExplorerChatParams
                ),
            ),
            cast_to=ExplorerChatResponse,
        )

    async def get_store(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorStoreResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/connectors/{connector_id}/store",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorStoreResponse,
        )

    async def list_tables(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListTablesResponse:
        """
        Returns all tables across all databases and schemas for the given connector.
        Useful for finding table IDs to pass to the explore endpoint for single-table
        exploration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/connectors/{connector_id}/tables",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListTablesResponse,
        )

    async def list_with_snippets(
        self,
        *,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListWithSnippetsResponse:
        """
        Args:
          team_id: Team ID to list connectors for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/connectors/with-snippets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"team_id": team_id}, connector_list_with_snippets_params.ConnectorListWithSnippetsParams
                ),
            ),
            cast_to=ConnectorListWithSnippetsResponse,
        )

    async def resolve_clarification(
        self,
        clarification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Mark a clarification request as resolved

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clarification_id:
            raise ValueError(f"Expected a non-empty value for `clarification_id` but received {clarification_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/connectors/clarification-requests/{clarification_id}/resolve",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def search_tables(
        self,
        *,
        query: str,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorSearchTablesResponse:
        """
        Args:
          query: Search query string

          team_id: Team ID to search tables for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/connectors/search-tables",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "team_id": team_id,
                    },
                    connector_search_tables_params.ConnectorSearchTablesParams,
                ),
            ),
            cast_to=ConnectorSearchTablesResponse,
        )

    async def update_column(
        self,
        column_id: str,
        *,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update column metadata (notes)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not column_id:
            raise ValueError(f"Expected a non-empty value for `column_id` but received {column_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/connectors/columns/{column_id}",
            body=await async_maybe_transform(
                {"notes": notes}, connector_update_column_params.ConnectorUpdateColumnParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_table(
        self,
        table_id: str,
        *,
        description: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateTableResponse:
        """
        Update table metadata (description or notes)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        return await self._patch(
            f"/connectors/tables/{table_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "notes": notes,
                },
                connector_update_table_params.ConnectorUpdateTableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateTableResponse,
        )


class ConnectorsResourceWithRawResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.create = to_raw_response_wrapper(
            connectors.create,
        )
        self.update = to_raw_response_wrapper(
            connectors.update,
        )
        self.list = to_raw_response_wrapper(
            connectors.list,
        )
        self.delete = to_raw_response_wrapper(
            connectors.delete,
        )
        self.create_secret = to_raw_response_wrapper(
            connectors.create_secret,
        )
        self.delete_schema_object = to_raw_response_wrapper(
            connectors.delete_schema_object,
        )
        self.delete_secret = to_raw_response_wrapper(
            connectors.delete_secret,
        )
        self.explore = to_raw_response_wrapper(
            connectors.explore,
        )
        self.get = to_raw_response_wrapper(
            connectors.get,
        )
        self.get_clarification_requests = to_raw_response_wrapper(
            connectors.get_clarification_requests,
        )
        self.get_exploration_runs = to_raw_response_wrapper(
            connectors.get_exploration_runs,
        )
        self.get_exploration_status = to_raw_response_wrapper(
            connectors.get_exploration_status,
        )
        self.get_explorer_chat = to_raw_response_wrapper(
            connectors.get_explorer_chat,
        )
        self.get_store = to_raw_response_wrapper(
            connectors.get_store,
        )
        self.list_tables = to_raw_response_wrapper(
            connectors.list_tables,
        )
        self.list_with_snippets = to_raw_response_wrapper(
            connectors.list_with_snippets,
        )
        self.resolve_clarification = to_raw_response_wrapper(
            connectors.resolve_clarification,
        )
        self.search_tables = to_raw_response_wrapper(
            connectors.search_tables,
        )
        self.update_column = to_raw_response_wrapper(
            connectors.update_column,
        )
        self.update_table = to_raw_response_wrapper(
            connectors.update_table,
        )

    @cached_property
    def type_snippets(self) -> TypeSnippetsResourceWithRawResponse:
        return TypeSnippetsResourceWithRawResponse(self._connectors.type_snippets)


class AsyncConnectorsResourceWithRawResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.create = async_to_raw_response_wrapper(
            connectors.create,
        )
        self.update = async_to_raw_response_wrapper(
            connectors.update,
        )
        self.list = async_to_raw_response_wrapper(
            connectors.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connectors.delete,
        )
        self.create_secret = async_to_raw_response_wrapper(
            connectors.create_secret,
        )
        self.delete_schema_object = async_to_raw_response_wrapper(
            connectors.delete_schema_object,
        )
        self.delete_secret = async_to_raw_response_wrapper(
            connectors.delete_secret,
        )
        self.explore = async_to_raw_response_wrapper(
            connectors.explore,
        )
        self.get = async_to_raw_response_wrapper(
            connectors.get,
        )
        self.get_clarification_requests = async_to_raw_response_wrapper(
            connectors.get_clarification_requests,
        )
        self.get_exploration_runs = async_to_raw_response_wrapper(
            connectors.get_exploration_runs,
        )
        self.get_exploration_status = async_to_raw_response_wrapper(
            connectors.get_exploration_status,
        )
        self.get_explorer_chat = async_to_raw_response_wrapper(
            connectors.get_explorer_chat,
        )
        self.get_store = async_to_raw_response_wrapper(
            connectors.get_store,
        )
        self.list_tables = async_to_raw_response_wrapper(
            connectors.list_tables,
        )
        self.list_with_snippets = async_to_raw_response_wrapper(
            connectors.list_with_snippets,
        )
        self.resolve_clarification = async_to_raw_response_wrapper(
            connectors.resolve_clarification,
        )
        self.search_tables = async_to_raw_response_wrapper(
            connectors.search_tables,
        )
        self.update_column = async_to_raw_response_wrapper(
            connectors.update_column,
        )
        self.update_table = async_to_raw_response_wrapper(
            connectors.update_table,
        )

    @cached_property
    def type_snippets(self) -> AsyncTypeSnippetsResourceWithRawResponse:
        return AsyncTypeSnippetsResourceWithRawResponse(self._connectors.type_snippets)


class ConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.create = to_streamed_response_wrapper(
            connectors.create,
        )
        self.update = to_streamed_response_wrapper(
            connectors.update,
        )
        self.list = to_streamed_response_wrapper(
            connectors.list,
        )
        self.delete = to_streamed_response_wrapper(
            connectors.delete,
        )
        self.create_secret = to_streamed_response_wrapper(
            connectors.create_secret,
        )
        self.delete_schema_object = to_streamed_response_wrapper(
            connectors.delete_schema_object,
        )
        self.delete_secret = to_streamed_response_wrapper(
            connectors.delete_secret,
        )
        self.explore = to_streamed_response_wrapper(
            connectors.explore,
        )
        self.get = to_streamed_response_wrapper(
            connectors.get,
        )
        self.get_clarification_requests = to_streamed_response_wrapper(
            connectors.get_clarification_requests,
        )
        self.get_exploration_runs = to_streamed_response_wrapper(
            connectors.get_exploration_runs,
        )
        self.get_exploration_status = to_streamed_response_wrapper(
            connectors.get_exploration_status,
        )
        self.get_explorer_chat = to_streamed_response_wrapper(
            connectors.get_explorer_chat,
        )
        self.get_store = to_streamed_response_wrapper(
            connectors.get_store,
        )
        self.list_tables = to_streamed_response_wrapper(
            connectors.list_tables,
        )
        self.list_with_snippets = to_streamed_response_wrapper(
            connectors.list_with_snippets,
        )
        self.resolve_clarification = to_streamed_response_wrapper(
            connectors.resolve_clarification,
        )
        self.search_tables = to_streamed_response_wrapper(
            connectors.search_tables,
        )
        self.update_column = to_streamed_response_wrapper(
            connectors.update_column,
        )
        self.update_table = to_streamed_response_wrapper(
            connectors.update_table,
        )

    @cached_property
    def type_snippets(self) -> TypeSnippetsResourceWithStreamingResponse:
        return TypeSnippetsResourceWithStreamingResponse(self._connectors.type_snippets)


class AsyncConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.create = async_to_streamed_response_wrapper(
            connectors.create,
        )
        self.update = async_to_streamed_response_wrapper(
            connectors.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connectors.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connectors.delete,
        )
        self.create_secret = async_to_streamed_response_wrapper(
            connectors.create_secret,
        )
        self.delete_schema_object = async_to_streamed_response_wrapper(
            connectors.delete_schema_object,
        )
        self.delete_secret = async_to_streamed_response_wrapper(
            connectors.delete_secret,
        )
        self.explore = async_to_streamed_response_wrapper(
            connectors.explore,
        )
        self.get = async_to_streamed_response_wrapper(
            connectors.get,
        )
        self.get_clarification_requests = async_to_streamed_response_wrapper(
            connectors.get_clarification_requests,
        )
        self.get_exploration_runs = async_to_streamed_response_wrapper(
            connectors.get_exploration_runs,
        )
        self.get_exploration_status = async_to_streamed_response_wrapper(
            connectors.get_exploration_status,
        )
        self.get_explorer_chat = async_to_streamed_response_wrapper(
            connectors.get_explorer_chat,
        )
        self.get_store = async_to_streamed_response_wrapper(
            connectors.get_store,
        )
        self.list_tables = async_to_streamed_response_wrapper(
            connectors.list_tables,
        )
        self.list_with_snippets = async_to_streamed_response_wrapper(
            connectors.list_with_snippets,
        )
        self.resolve_clarification = async_to_streamed_response_wrapper(
            connectors.resolve_clarification,
        )
        self.search_tables = async_to_streamed_response_wrapper(
            connectors.search_tables,
        )
        self.update_column = async_to_streamed_response_wrapper(
            connectors.update_column,
        )
        self.update_table = async_to_streamed_response_wrapper(
            connectors.update_table,
        )

    @cached_property
    def type_snippets(self) -> AsyncTypeSnippetsResourceWithStreamingResponse:
        return AsyncTypeSnippetsResourceWithStreamingResponse(self._connectors.type_snippets)
