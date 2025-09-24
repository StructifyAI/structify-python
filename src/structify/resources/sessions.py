# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    WorkflowNodeExecutionStatus,
    session_kill_jobs_params,
    session_get_events_params,
    session_create_edge_params,
    session_create_node_params,
    session_update_node_params,
    session_mark_errored_params,
    session_create_session_params,
    session_update_node_progress_params,
    session_upload_node_output_data_params,
    session_upload_node_visualization_output_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.workflow_dag import WorkflowDag
from ..types.workflow_session import WorkflowSession
from ..types.workflow_session_edge import WorkflowSessionEdge
from ..types.workflow_session_node import WorkflowSessionNode
from ..types.get_node_logs_response import GetNodeLogsResponse
from ..types.session_kill_jobs_response import SessionKillJobsResponse
from ..types.session_get_events_response import SessionGetEventsResponse
from ..types.workflow_node_execution_status import WorkflowNodeExecutionStatus
from ..types.session_get_node_progress_response import SessionGetNodeProgressResponse

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        code_md5_hash: str,
        docstring: str,
        function_name: str,
        output_schema: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    "code_md5_hash": code_md5_hash,
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
        workflow_schedule_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                {
                    "chat_session_id": chat_session_id,
                    "workflow_schedule_id": workflow_schedule_id,
                },
                session_create_session_params.SessionCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSession,
        )

    def finalize_dag(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Finalize a workflow session DAG by validating and marking it as ready

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/sessions/{session_id}/dag_ready",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowDag:
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
            cast_to=WorkflowDag,
        )

    def get_events(
        self,
        node_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_term: Optional[str] | Omit = omit,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetEventsResponse:
        """
        Get events from all jobs for a specific workflow node.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return self._get(
            f"/sessions/nodes/{node_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search_term": search_term,
                        "status": status,
                    },
                    session_get_events_params.SessionGetEventsParams,
                ),
            ),
            cast_to=SessionGetEventsResponse,
        )

    def get_node_logs(
        self,
        node_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetNodeLogsResponse:
        """
        Get terminal logs for a workflow node

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return self._get(
            f"/sessions/node/{node_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetNodeLogsResponse,
        )

    def get_node_output_data(
        self,
        node_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/sessions/nodes/{node_id}/output_data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_node_progress(
        self,
        node_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetNodeProgressResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return self._get(
            f"/sessions/nodes/{node_id}/progress",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGetNodeProgressResponse,
        )

    def kill_jobs(
        self,
        session_id: str,
        *,
        message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionKillJobsResponse:
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
            f"/sessions/{session_id}/kill_jobs",
            body=maybe_transform({"message": message}, session_kill_jobs_params.SessionKillJobsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionKillJobsResponse,
        )

    def mark_errored(
        self,
        session_id: str,
        *,
        error_message: str,
        error_traceback: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        error_message: Optional[str] | Omit = omit,
        error_traceback: Optional[str] | Omit = omit,
        execution_time_ms: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                },
                session_update_node_params.SessionUpdateNodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionNode,
        )

    def update_node_progress(
        self,
        node_id: str,
        *,
        current: int,
        elapsed_seconds: float,
        title: str,
        total: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/sessions/nodes/{node_id}/progress",
            body=maybe_transform(
                {
                    "current": current,
                    "elapsed_seconds": elapsed_seconds,
                    "title": title,
                    "total": total,
                },
                session_update_node_progress_params.SessionUpdateNodeProgressParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionNode,
        )

    def upload_node_output_data(
        self,
        node_id: str,
        *,
        content: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        body = deepcopy_minimal({"content": content})
        files = extract_files(cast(Mapping[str, object], body), paths=[["content"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/sessions/nodes/{node_id}/output_data",
            body=maybe_transform(body, session_upload_node_output_data_params.SessionUploadNodeOutputDataParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionNode,
        )

    def upload_node_visualization_output(
        self,
        node_id: str,
        *,
        visualization_output: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        return self._post(
            f"/sessions/nodes/{node_id}/visualization_output",
            body=maybe_transform(
                {"visualization_output": visualization_output},
                session_upload_node_visualization_output_params.SessionUploadNodeVisualizationOutputParams,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        code_md5_hash: str,
        docstring: str,
        function_name: str,
        output_schema: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    "code_md5_hash": code_md5_hash,
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
        workflow_schedule_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                {
                    "chat_session_id": chat_session_id,
                    "workflow_schedule_id": workflow_schedule_id,
                },
                session_create_session_params.SessionCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSession,
        )

    async def finalize_dag(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Finalize a workflow session DAG by validating and marking it as ready

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/sessions/{session_id}/dag_ready",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowDag:
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
            cast_to=WorkflowDag,
        )

    async def get_events(
        self,
        node_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_term: Optional[str] | Omit = omit,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetEventsResponse:
        """
        Get events from all jobs for a specific workflow node.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return await self._get(
            f"/sessions/nodes/{node_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search_term": search_term,
                        "status": status,
                    },
                    session_get_events_params.SessionGetEventsParams,
                ),
            ),
            cast_to=SessionGetEventsResponse,
        )

    async def get_node_logs(
        self,
        node_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetNodeLogsResponse:
        """
        Get terminal logs for a workflow node

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return await self._get(
            f"/sessions/node/{node_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetNodeLogsResponse,
        )

    async def get_node_output_data(
        self,
        node_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/sessions/nodes/{node_id}/output_data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_node_progress(
        self,
        node_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetNodeProgressResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_id:
            raise ValueError(f"Expected a non-empty value for `node_id` but received {node_id!r}")
        return await self._get(
            f"/sessions/nodes/{node_id}/progress",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGetNodeProgressResponse,
        )

    async def kill_jobs(
        self,
        session_id: str,
        *,
        message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionKillJobsResponse:
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
            f"/sessions/{session_id}/kill_jobs",
            body=await async_maybe_transform({"message": message}, session_kill_jobs_params.SessionKillJobsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionKillJobsResponse,
        )

    async def mark_errored(
        self,
        session_id: str,
        *,
        error_message: str,
        error_traceback: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        error_message: Optional[str] | Omit = omit,
        error_traceback: Optional[str] | Omit = omit,
        execution_time_ms: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                },
                session_update_node_params.SessionUpdateNodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionNode,
        )

    async def update_node_progress(
        self,
        node_id: str,
        *,
        current: int,
        elapsed_seconds: float,
        title: str,
        total: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/sessions/nodes/{node_id}/progress",
            body=await async_maybe_transform(
                {
                    "current": current,
                    "elapsed_seconds": elapsed_seconds,
                    "title": title,
                    "total": total,
                },
                session_update_node_progress_params.SessionUpdateNodeProgressParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionNode,
        )

    async def upload_node_output_data(
        self,
        node_id: str,
        *,
        content: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        body = deepcopy_minimal({"content": content})
        files = extract_files(cast(Mapping[str, object], body), paths=[["content"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/sessions/nodes/{node_id}/output_data",
            body=await async_maybe_transform(
                body, session_upload_node_output_data_params.SessionUploadNodeOutputDataParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowSessionNode,
        )

    async def upload_node_visualization_output(
        self,
        node_id: str,
        *,
        visualization_output: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        return await self._post(
            f"/sessions/nodes/{node_id}/visualization_output",
            body=await async_maybe_transform(
                {"visualization_output": visualization_output},
                session_upload_node_visualization_output_params.SessionUploadNodeVisualizationOutputParams,
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
        self.finalize_dag = to_raw_response_wrapper(
            sessions.finalize_dag,
        )
        self.get_dag = to_raw_response_wrapper(
            sessions.get_dag,
        )
        self.get_events = to_raw_response_wrapper(
            sessions.get_events,
        )
        self.get_node_logs = to_raw_response_wrapper(
            sessions.get_node_logs,
        )
        self.get_node_output_data = to_custom_raw_response_wrapper(
            sessions.get_node_output_data,
            BinaryAPIResponse,
        )
        self.get_node_progress = to_raw_response_wrapper(
            sessions.get_node_progress,
        )
        self.kill_jobs = to_raw_response_wrapper(
            sessions.kill_jobs,
        )
        self.mark_errored = to_raw_response_wrapper(
            sessions.mark_errored,
        )
        self.update_node = to_raw_response_wrapper(
            sessions.update_node,
        )
        self.update_node_progress = to_raw_response_wrapper(
            sessions.update_node_progress,
        )
        self.upload_node_output_data = to_raw_response_wrapper(
            sessions.upload_node_output_data,
        )
        self.upload_node_visualization_output = to_raw_response_wrapper(
            sessions.upload_node_visualization_output,
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
        self.finalize_dag = async_to_raw_response_wrapper(
            sessions.finalize_dag,
        )
        self.get_dag = async_to_raw_response_wrapper(
            sessions.get_dag,
        )
        self.get_events = async_to_raw_response_wrapper(
            sessions.get_events,
        )
        self.get_node_logs = async_to_raw_response_wrapper(
            sessions.get_node_logs,
        )
        self.get_node_output_data = async_to_custom_raw_response_wrapper(
            sessions.get_node_output_data,
            AsyncBinaryAPIResponse,
        )
        self.get_node_progress = async_to_raw_response_wrapper(
            sessions.get_node_progress,
        )
        self.kill_jobs = async_to_raw_response_wrapper(
            sessions.kill_jobs,
        )
        self.mark_errored = async_to_raw_response_wrapper(
            sessions.mark_errored,
        )
        self.update_node = async_to_raw_response_wrapper(
            sessions.update_node,
        )
        self.update_node_progress = async_to_raw_response_wrapper(
            sessions.update_node_progress,
        )
        self.upload_node_output_data = async_to_raw_response_wrapper(
            sessions.upload_node_output_data,
        )
        self.upload_node_visualization_output = async_to_raw_response_wrapper(
            sessions.upload_node_visualization_output,
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
        self.finalize_dag = to_streamed_response_wrapper(
            sessions.finalize_dag,
        )
        self.get_dag = to_streamed_response_wrapper(
            sessions.get_dag,
        )
        self.get_events = to_streamed_response_wrapper(
            sessions.get_events,
        )
        self.get_node_logs = to_streamed_response_wrapper(
            sessions.get_node_logs,
        )
        self.get_node_output_data = to_custom_streamed_response_wrapper(
            sessions.get_node_output_data,
            StreamedBinaryAPIResponse,
        )
        self.get_node_progress = to_streamed_response_wrapper(
            sessions.get_node_progress,
        )
        self.kill_jobs = to_streamed_response_wrapper(
            sessions.kill_jobs,
        )
        self.mark_errored = to_streamed_response_wrapper(
            sessions.mark_errored,
        )
        self.update_node = to_streamed_response_wrapper(
            sessions.update_node,
        )
        self.update_node_progress = to_streamed_response_wrapper(
            sessions.update_node_progress,
        )
        self.upload_node_output_data = to_streamed_response_wrapper(
            sessions.upload_node_output_data,
        )
        self.upload_node_visualization_output = to_streamed_response_wrapper(
            sessions.upload_node_visualization_output,
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
        self.finalize_dag = async_to_streamed_response_wrapper(
            sessions.finalize_dag,
        )
        self.get_dag = async_to_streamed_response_wrapper(
            sessions.get_dag,
        )
        self.get_events = async_to_streamed_response_wrapper(
            sessions.get_events,
        )
        self.get_node_logs = async_to_streamed_response_wrapper(
            sessions.get_node_logs,
        )
        self.get_node_output_data = async_to_custom_streamed_response_wrapper(
            sessions.get_node_output_data,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_node_progress = async_to_streamed_response_wrapper(
            sessions.get_node_progress,
        )
        self.kill_jobs = async_to_streamed_response_wrapper(
            sessions.kill_jobs,
        )
        self.mark_errored = async_to_streamed_response_wrapper(
            sessions.mark_errored,
        )
        self.update_node = async_to_streamed_response_wrapper(
            sessions.update_node,
        )
        self.update_node_progress = async_to_streamed_response_wrapper(
            sessions.update_node_progress,
        )
        self.upload_node_output_data = async_to_streamed_response_wrapper(
            sessions.upload_node_output_data,
        )
        self.upload_node_visualization_output = async_to_streamed_response_wrapper(
            sessions.upload_node_visualization_output,
        )
