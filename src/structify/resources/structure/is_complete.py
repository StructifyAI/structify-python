# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ...types.structure import is_complete_create_params
from ...types.structure.is_complete import IsComplete

__all__ = ["IsCompleteResource", "AsyncIsCompleteResource"]


class IsCompleteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IsCompleteResourceWithRawResponse:
        return IsCompleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IsCompleteResourceWithStreamingResponse:
        return IsCompleteResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IsComplete:
        """
        Wait for all specified async tasks to be completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/structure/is_complete",
            body=maybe_transform(body, is_complete_create_params.IsCompleteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IsComplete,
        )


class AsyncIsCompleteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIsCompleteResourceWithRawResponse:
        return AsyncIsCompleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIsCompleteResourceWithStreamingResponse:
        return AsyncIsCompleteResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IsComplete:
        """
        Wait for all specified async tasks to be completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/structure/is_complete",
            body=await async_maybe_transform(body, is_complete_create_params.IsCompleteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IsComplete,
        )


class IsCompleteResourceWithRawResponse:
    def __init__(self, is_complete: IsCompleteResource) -> None:
        self._is_complete = is_complete

        self.create = to_raw_response_wrapper(
            is_complete.create,
        )


class AsyncIsCompleteResourceWithRawResponse:
    def __init__(self, is_complete: AsyncIsCompleteResource) -> None:
        self._is_complete = is_complete

        self.create = async_to_raw_response_wrapper(
            is_complete.create,
        )


class IsCompleteResourceWithStreamingResponse:
    def __init__(self, is_complete: IsCompleteResource) -> None:
        self._is_complete = is_complete

        self.create = to_streamed_response_wrapper(
            is_complete.create,
        )


class AsyncIsCompleteResourceWithStreamingResponse:
    def __init__(self, is_complete: AsyncIsCompleteResource) -> None:
        self._is_complete = is_complete

        self.create = async_to_streamed_response_wrapper(
            is_complete.create,
        )
