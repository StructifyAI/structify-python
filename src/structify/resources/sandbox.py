# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import sandbox_update_status_params
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
from ..types.sandbox import Sandbox
from ..types.sandbox_list_chat_response import SandboxListChatResponse

__all__ = ["SandboxResource", "AsyncSandboxResource"]


class SandboxResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SandboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return SandboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return SandboxResourceWithStreamingResponse(self)

    def create_chat(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sandbox:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            f"/sandbox/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sandbox,
        )

    def get_live_chat(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sandbox:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            f"/sandbox/live/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sandbox,
        )

    def list_chat(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SandboxListChatResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            f"/sandbox/list/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxListChatResponse,
        )

    def update_status(
        self,
        sandbox_id: str,
        *,
        status: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sandbox:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._patch(
            f"/sandbox/{sandbox_id}/status",
            body=maybe_transform({"status": status}, sandbox_update_status_params.SandboxUpdateStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sandbox,
        )


class AsyncSandboxResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSandboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSandboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncSandboxResourceWithStreamingResponse(self)

    async def create_chat(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sandbox:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            f"/sandbox/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sandbox,
        )

    async def get_live_chat(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sandbox:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            f"/sandbox/live/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sandbox,
        )

    async def list_chat(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SandboxListChatResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            f"/sandbox/list/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxListChatResponse,
        )

    async def update_status(
        self,
        sandbox_id: str,
        *,
        status: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sandbox:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._patch(
            f"/sandbox/{sandbox_id}/status",
            body=await async_maybe_transform(
                {"status": status}, sandbox_update_status_params.SandboxUpdateStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sandbox,
        )


class SandboxResourceWithRawResponse:
    def __init__(self, sandbox: SandboxResource) -> None:
        self._sandbox = sandbox

        self.create_chat = to_raw_response_wrapper(
            sandbox.create_chat,
        )
        self.get_live_chat = to_raw_response_wrapper(
            sandbox.get_live_chat,
        )
        self.list_chat = to_raw_response_wrapper(
            sandbox.list_chat,
        )
        self.update_status = to_raw_response_wrapper(
            sandbox.update_status,
        )


class AsyncSandboxResourceWithRawResponse:
    def __init__(self, sandbox: AsyncSandboxResource) -> None:
        self._sandbox = sandbox

        self.create_chat = async_to_raw_response_wrapper(
            sandbox.create_chat,
        )
        self.get_live_chat = async_to_raw_response_wrapper(
            sandbox.get_live_chat,
        )
        self.list_chat = async_to_raw_response_wrapper(
            sandbox.list_chat,
        )
        self.update_status = async_to_raw_response_wrapper(
            sandbox.update_status,
        )


class SandboxResourceWithStreamingResponse:
    def __init__(self, sandbox: SandboxResource) -> None:
        self._sandbox = sandbox

        self.create_chat = to_streamed_response_wrapper(
            sandbox.create_chat,
        )
        self.get_live_chat = to_streamed_response_wrapper(
            sandbox.get_live_chat,
        )
        self.list_chat = to_streamed_response_wrapper(
            sandbox.list_chat,
        )
        self.update_status = to_streamed_response_wrapper(
            sandbox.update_status,
        )


class AsyncSandboxResourceWithStreamingResponse:
    def __init__(self, sandbox: AsyncSandboxResource) -> None:
        self._sandbox = sandbox

        self.create_chat = async_to_streamed_response_wrapper(
            sandbox.create_chat,
        )
        self.get_live_chat = async_to_streamed_response_wrapper(
            sandbox.get_live_chat,
        )
        self.list_chat = async_to_streamed_response_wrapper(
            sandbox.list_chat,
        )
        self.update_status = async_to_streamed_response_wrapper(
            sandbox.update_status,
        )
