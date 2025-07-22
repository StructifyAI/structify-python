# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    WorkflowNodeExecutionStatus,
    session_get_events_params,
    session_create_edge_params,
    session_create_node_params,
    session_update_node_params,
    session_mark_errored_params,
    session_create_session_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.workflow_session import WorkflowSession
from ..types.workflow_session_edge import WorkflowSessionEdge
from ..types.workflow_session_node import WorkflowSessionNode
from ..types.get_workflow_dag_response import GetWorkflowDagResponse
from ..types.get_session_events_response import GetSessionEventsResponse
from ..types.workflow_node_execution_status import WorkflowNodeExecutionStatus

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create_edge(
        self,
        session_id: str,
        *,
        source_node_id: str,
        target_node_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowSessionEdge:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/sessions/{session_id}/edges",
            body=maybe_transform(
                {
                    "source_node_id": source_node_id,
                    "target_node_id": target_node_id,
                },
                session_create_edge_params.SessionCreateEdgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionEdge,
        )

    def create_node(
        self,
        session_id: str,
        *,
        docstring: str,
        function_name: str,
        output_schema: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowSessionNode:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/sessions/{session_id}/nodes",
            body=maybe_transform(
                {
                    "docstring": docstring,
                    "function_name": function_name,
                    "output_schema": output_schema,
                },
                session_create_node_params.SessionCreateNodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionNode,
        )

    def create_session(
        self,
        *,
        chat_session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowSession:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sessions",
            body=maybe_transform(
                {"chat_session_id": chat_session_id}, session_create_session_params.SessionCreateSessionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSession,
        )

    def get_dag(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetWorkflowDagResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/sessions/{session_id}/dag",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetWorkflowDagResponse,
        )

    def get_events(
        self,
        session_id: str,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetSessionEventsResponse:
        """
        Get events from all jobs in a session's event queue (without removing them).

        Args:
          limit: Maximum number of events to fetch (default: 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/sessions/{session_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, session_get_events_params.SessionGetEventsParams),
            ),
            cast_to=GetSessionEventsResponse,
        )

    def mark_errored(
        self,
        session_id: str,
        *,
        error_message: str,
        error_traceback: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowSession:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._patch(
            f"/sessions/{session_id}/error",
            body=maybe_transform(
                {
                    "error_message": error_message,
                    "error_traceback": error_traceback,
                },
                session_mark_errored_params.SessionMarkErroredParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSession,
        )

    def update_node(
        self,
        node_id: str,
        *,
        execution_status: WorkflowNodeExecutionStatus,
        error_message: Optional[str] | NotGiven = NOT_GIVEN,
        error_traceback: Optional[str] | NotGiven = NOT_GIVEN,
        execution_time_ms: Optional[int] | NotGiven = NOT_GIVEN,
        output_data: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowSessionNode:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return self._patch(
            f"/sessions/nodes/{node_id}",
            body=maybe_transform(
                {
                    "execution_status": execution_status,
                    "error_message": error_message,
                    "error_traceback": error_traceback,
                    "execution_time_ms": execution_time_ms,
                    "output_data": output_data,
                },
                session_update_node_params.SessionUpdateNodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionNode,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create_edge(
        self,
        session_id: str,
        *,
        source_node_id: str,
        target_node_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowSessionEdge:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/sessions/{session_id}/edges",
            body=await async_maybe_transform(
                {
                    "source_node_id": source_node_id,
                    "target_node_id": target_node_id,
                },
                session_create_edge_params.SessionCreateEdgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionEdge,
        )

    async def create_node(
        self,
        session_id: str,
        *,
        docstring: str,
        function_name: str,
        output_schema: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowSessionNode:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/sessions/{session_id}/nodes",
            body=await async_maybe_transform(
                {
                    "docstring": docstring,
                    "function_name": function_name,
                    "output_schema": output_schema,
                },
                session_create_node_params.SessionCreateNodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionNode,
        )

    async def create_session(
        self,
        *,
        chat_session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowSession:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sessions",
            body=await async_maybe_transform(
                {"chat_session_id": chat_session_id}, session_create_session_params.SessionCreateSessionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSession,
        )

    async def get_dag(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetWorkflowDagResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/sessions/{session_id}/dag",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetWorkflowDagResponse,
        )

    async def get_events(
        self,
        session_id: str,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetSessionEventsResponse:
        """
        Get events from all jobs in a session's event queue (without removing them).

        Args:
          limit: Maximum number of events to fetch (default: 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/sessions/{session_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, session_get_events_params.SessionGetEventsParams),
            ),
            cast_to=GetSessionEventsResponse,
        )

    async def mark_errored(
        self,
        session_id: str,
        *,
        error_message: str,
        error_traceback: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowSession:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._patch(
            f"/sessions/{session_id}/error",
            body=await async_maybe_transform(
                {
                    "error_message": error_message,
                    "error_traceback": error_traceback,
                },
                session_mark_errored_params.SessionMarkErroredParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSession,
        )

    async def update_node(
        self,
        node_id: str,
        *,
        execution_status: WorkflowNodeExecutionStatus,
        error_message: Optional[str] | NotGiven = NOT_GIVEN,
        error_traceback: Optional[str] | NotGiven = NOT_GIVEN,
        execution_time_ms: Optional[int] | NotGiven = NOT_GIVEN,
        output_data: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowSessionNode:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return await self._patch(
            f"/sessions/nodes/{node_id}",
            body=await async_maybe_transform(
                {
                    "execution_status": execution_status,
                    "error_message": error_message,
                    "error_traceback": error_traceback,
                    "execution_time_ms": execution_time_ms,
                    "output_data": output_data,
                },
                session_update_node_params.SessionUpdateNodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionNode,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create_edge = to_raw_response_wrapper(
            sessions.create_edge,
        )
        self.create_node = to_raw_response_wrapper(
            sessions.create_node,
        )
        self.create_session = to_raw_response_wrapper(
            sessions.create_session,
        )
        self.get_dag = to_raw_response_wrapper(
            sessions.get_dag,
        )
        self.get_events = to_raw_response_wrapper(
            sessions.get_events,
        )
        self.mark_errored = to_raw_response_wrapper(
            sessions.mark_errored,
        )
        self.update_node = to_raw_response_wrapper(
            sessions.update_node,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create_edge = async_to_raw_response_wrapper(
            sessions.create_edge,
        )
        self.create_node = async_to_raw_response_wrapper(
            sessions.create_node,
        )
        self.create_session = async_to_raw_response_wrapper(
            sessions.create_session,
        )
        self.get_dag = async_to_raw_response_wrapper(
            sessions.get_dag,
        )
        self.get_events = async_to_raw_response_wrapper(
            sessions.get_events,
        )
        self.mark_errored = async_to_raw_response_wrapper(
            sessions.mark_errored,
        )
        self.update_node = async_to_raw_response_wrapper(
            sessions.update_node,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create_edge = to_streamed_response_wrapper(
            sessions.create_edge,
        )
        self.create_node = to_streamed_response_wrapper(
            sessions.create_node,
        )
        self.create_session = to_streamed_response_wrapper(
            sessions.create_session,
        )
        self.get_dag = to_streamed_response_wrapper(
            sessions.get_dag,
        )
        self.get_events = to_streamed_response_wrapper(
            sessions.get_events,
        )
        self.mark_errored = to_streamed_response_wrapper(
            sessions.mark_errored,
        )
        self.update_node = to_streamed_response_wrapper(
            sessions.update_node,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create_edge = async_to_streamed_response_wrapper(
            sessions.create_edge,
        )
        self.create_node = async_to_streamed_response_wrapper(
            sessions.create_node,
        )
        self.create_session = async_to_streamed_response_wrapper(
            sessions.create_session,
        )
        self.get_dag = async_to_streamed_response_wrapper(
            sessions.get_dag,
        )
        self.get_events = async_to_streamed_response_wrapper(
            sessions.get_events,
        )
        self.mark_errored = async_to_streamed_response_wrapper(
            sessions.mark_errored,
        )
        self.update_node = async_to_streamed_response_wrapper(
            sessions.update_node,
        )
