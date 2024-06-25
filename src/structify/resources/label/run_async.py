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
from ...types.label import run_async_create_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["RunAsyncResource", "AsyncRunAsyncResource"]


class RunAsyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunAsyncResourceWithRawResponse:
        return RunAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunAsyncResourceWithStreamingResponse:
        return RunAsyncResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        dataset_name: str,
        structure_input: run_async_create_params.StructureInput,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          structure_input: These are all the types that can be converted into a BasicInputType

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            "/label/run_async",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "structure_input": structure_input,
                },
                run_async_create_params.RunAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncRunAsyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunAsyncResourceWithRawResponse:
        return AsyncRunAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunAsyncResourceWithStreamingResponse:
        return AsyncRunAsyncResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        dataset_name: str,
        structure_input: run_async_create_params.StructureInput,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          structure_input: These are all the types that can be converted into a BasicInputType

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            "/label/run_async",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "structure_input": structure_input,
                },
                run_async_create_params.RunAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class RunAsyncResourceWithRawResponse:
    def __init__(self, run_async: RunAsyncResource) -> None:
        self._run_async = run_async

        self.create = to_raw_response_wrapper(
            run_async.create,
        )


class AsyncRunAsyncResourceWithRawResponse:
    def __init__(self, run_async: AsyncRunAsyncResource) -> None:
        self._run_async = run_async

        self.create = async_to_raw_response_wrapper(
            run_async.create,
        )


class RunAsyncResourceWithStreamingResponse:
    def __init__(self, run_async: RunAsyncResource) -> None:
        self._run_async = run_async

        self.create = to_streamed_response_wrapper(
            run_async.create,
        )


class AsyncRunAsyncResourceWithStreamingResponse:
    def __init__(self, run_async: AsyncRunAsyncResource) -> None:
        self._run_async = run_async

        self.create = async_to_streamed_response_wrapper(
            run_async.create,
        )
