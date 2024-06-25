# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.label.llm_assist_retrieve_response import LlmAssistRetrieveResponse

__all__ = ["LlmAssistResource", "AsyncLlmAssistResource"]


class LlmAssistResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LlmAssistResourceWithRawResponse:
        return LlmAssistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmAssistResourceWithStreamingResponse:
        return LlmAssistResourceWithStreamingResponse(self)

    def retrieve(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmAssistRetrieveResponse:
        """
        web requests that would be cancelled by cloudflare in prod.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/label/llm_assist/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmAssistRetrieveResponse,
        )


class AsyncLlmAssistResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLlmAssistResourceWithRawResponse:
        return AsyncLlmAssistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmAssistResourceWithStreamingResponse:
        return AsyncLlmAssistResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmAssistRetrieveResponse:
        """
        web requests that would be cancelled by cloudflare in prod.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/label/llm_assist/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmAssistRetrieveResponse,
        )


class LlmAssistResourceWithRawResponse:
    def __init__(self, llm_assist: LlmAssistResource) -> None:
        self._llm_assist = llm_assist

        self.retrieve = to_raw_response_wrapper(
            llm_assist.retrieve,
        )


class AsyncLlmAssistResourceWithRawResponse:
    def __init__(self, llm_assist: AsyncLlmAssistResource) -> None:
        self._llm_assist = llm_assist

        self.retrieve = async_to_raw_response_wrapper(
            llm_assist.retrieve,
        )


class LlmAssistResourceWithStreamingResponse:
    def __init__(self, llm_assist: LlmAssistResource) -> None:
        self._llm_assist = llm_assist

        self.retrieve = to_streamed_response_wrapper(
            llm_assist.retrieve,
        )


class AsyncLlmAssistResourceWithStreamingResponse:
    def __init__(self, llm_assist: AsyncLlmAssistResource) -> None:
        self._llm_assist = llm_assist

        self.retrieve = async_to_streamed_response_wrapper(
            llm_assist.retrieve,
        )
