# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.usage_get_job_info_response import UsageGetJobInfoResponse

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        return UsageResourceWithStreamingResponse(self)

    def get_job_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageGetJobInfoResponse:
        """Returns a token that can be waited on until the request is finished."""
        return self._post(
            "/usage/get_job_info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetJobInfoResponse,
        )


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self)

    async def get_job_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageGetJobInfoResponse:
        """Returns a token that can be waited on until the request is finished."""
        return await self._post(
            "/usage/get_job_info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetJobInfoResponse,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.get_job_info = to_raw_response_wrapper(
            usage.get_job_info,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.get_job_info = async_to_raw_response_wrapper(
            usage.get_job_info,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.get_job_info = to_streamed_response_wrapper(
            usage.get_job_info,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.get_job_info = async_to_streamed_response_wrapper(
            usage.get_job_info,
        )
