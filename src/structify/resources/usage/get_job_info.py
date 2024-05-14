# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.usage import get_job_info_create_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["GetJobInfoResource", "AsyncGetJobInfoResource"]


class GetJobInfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GetJobInfoResourceWithRawResponse:
        return GetJobInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GetJobInfoResourceWithStreamingResponse:
        return GetJobInfoResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        job_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Structure an unstructured data source into the given dataset in an async
        fashion.

        Returns a token that can be waited on until the request is finished.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/usage/get_job_info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"job_id": job_id}, get_job_info_create_params.GetJobInfoCreateParams),
            ),
            cast_to=object,
        )


class AsyncGetJobInfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGetJobInfoResourceWithRawResponse:
        return AsyncGetJobInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGetJobInfoResourceWithStreamingResponse:
        return AsyncGetJobInfoResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        job_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Structure an unstructured data source into the given dataset in an async
        fashion.

        Returns a token that can be waited on until the request is finished.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/usage/get_job_info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"job_id": job_id}, get_job_info_create_params.GetJobInfoCreateParams
                ),
            ),
            cast_to=object,
        )


class GetJobInfoResourceWithRawResponse:
    def __init__(self, get_job_info: GetJobInfoResource) -> None:
        self._get_job_info = get_job_info

        self.create = to_raw_response_wrapper(
            get_job_info.create,
        )


class AsyncGetJobInfoResourceWithRawResponse:
    def __init__(self, get_job_info: AsyncGetJobInfoResource) -> None:
        self._get_job_info = get_job_info

        self.create = async_to_raw_response_wrapper(
            get_job_info.create,
        )


class GetJobInfoResourceWithStreamingResponse:
    def __init__(self, get_job_info: GetJobInfoResource) -> None:
        self._get_job_info = get_job_info

        self.create = to_streamed_response_wrapper(
            get_job_info.create,
        )


class AsyncGetJobInfoResourceWithStreamingResponse:
    def __init__(self, get_job_info: AsyncGetJobInfoResource) -> None:
        self._get_job_info = get_job_info

        self.create = async_to_streamed_response_wrapper(
            get_job_info.create,
        )
