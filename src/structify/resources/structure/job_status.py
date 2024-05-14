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
from ...types.structure import job_status_create_params

__all__ = ["JobStatusResource", "AsyncJobStatusResource"]


class JobStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobStatusResourceWithRawResponse:
        return JobStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobStatusResourceWithStreamingResponse:
        return JobStatusResourceWithStreamingResponse(self)

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
    ) -> object:
        """
        Wait for all specified async tasks to be completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/structure/job_status",
            body=maybe_transform(body, job_status_create_params.JobStatusCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncJobStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobStatusResourceWithRawResponse:
        return AsyncJobStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobStatusResourceWithStreamingResponse:
        return AsyncJobStatusResourceWithStreamingResponse(self)

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
    ) -> object:
        """
        Wait for all specified async tasks to be completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/structure/job_status",
            body=await async_maybe_transform(body, job_status_create_params.JobStatusCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class JobStatusResourceWithRawResponse:
    def __init__(self, job_status: JobStatusResource) -> None:
        self._job_status = job_status

        self.create = to_raw_response_wrapper(
            job_status.create,
        )


class AsyncJobStatusResourceWithRawResponse:
    def __init__(self, job_status: AsyncJobStatusResource) -> None:
        self._job_status = job_status

        self.create = async_to_raw_response_wrapper(
            job_status.create,
        )


class JobStatusResourceWithStreamingResponse:
    def __init__(self, job_status: JobStatusResource) -> None:
        self._job_status = job_status

        self.create = to_streamed_response_wrapper(
            job_status.create,
        )


class AsyncJobStatusResourceWithStreamingResponse:
    def __init__(self, job_status: AsyncJobStatusResource) -> None:
        self._job_status = job_status

        self.create = async_to_streamed_response_wrapper(
            job_status.create,
        )
