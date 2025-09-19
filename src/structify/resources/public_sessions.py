# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
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

__all__ = ["PublicSessionsResource", "AsyncPublicSessionsResource"]


class PublicSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublicSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return PublicSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return PublicSessionsResourceWithStreamingResponse(self)

    def get_latest_workflow(
        self,
        chat_session_id: str,
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
        if not chat_session_id:
            raise ValueError(f"Expected a non-empty value for `chat_session_id` but received {chat_session_id!r}")
        return self._get(
            f"/public/chat/{chat_session_id}/latest-workflow",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowDag,
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
            f"/public/nodes/{node_id}/output_data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncPublicSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublicSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublicSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncPublicSessionsResourceWithStreamingResponse(self)

    async def get_latest_workflow(
        self,
        chat_session_id: str,
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
        if not chat_session_id:
            raise ValueError(f"Expected a non-empty value for `chat_session_id` but received {chat_session_id!r}")
        return await self._get(
            f"/public/chat/{chat_session_id}/latest-workflow",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowDag,
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
            f"/public/nodes/{node_id}/output_data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class PublicSessionsResourceWithRawResponse:
    def __init__(self, public_sessions: PublicSessionsResource) -> None:
        self._public_sessions = public_sessions

        self.get_latest_workflow = to_raw_response_wrapper(
            public_sessions.get_latest_workflow,
        )
        self.get_node_output_data = to_custom_raw_response_wrapper(
            public_sessions.get_node_output_data,
            BinaryAPIResponse,
        )


class AsyncPublicSessionsResourceWithRawResponse:
    def __init__(self, public_sessions: AsyncPublicSessionsResource) -> None:
        self._public_sessions = public_sessions

        self.get_latest_workflow = async_to_raw_response_wrapper(
            public_sessions.get_latest_workflow,
        )
        self.get_node_output_data = async_to_custom_raw_response_wrapper(
            public_sessions.get_node_output_data,
            AsyncBinaryAPIResponse,
        )


class PublicSessionsResourceWithStreamingResponse:
    def __init__(self, public_sessions: PublicSessionsResource) -> None:
        self._public_sessions = public_sessions

        self.get_latest_workflow = to_streamed_response_wrapper(
            public_sessions.get_latest_workflow,
        )
        self.get_node_output_data = to_custom_streamed_response_wrapper(
            public_sessions.get_node_output_data,
            StreamedBinaryAPIResponse,
        )


class AsyncPublicSessionsResourceWithStreamingResponse:
    def __init__(self, public_sessions: AsyncPublicSessionsResource) -> None:
        self._public_sessions = public_sessions

        self.get_latest_workflow = async_to_streamed_response_wrapper(
            public_sessions.get_latest_workflow,
        )
        self.get_node_output_data = async_to_custom_streamed_response_wrapper(
            public_sessions.get_node_output_data,
            AsyncStreamedBinaryAPIResponse,
        )
