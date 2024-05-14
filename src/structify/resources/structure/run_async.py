# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ...types.structure import run_async_create_params

__all__ = ["RunAsyncResource", "AsyncRunAsyncResource"]


class RunAsyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunAsyncResourceWithRawResponse:
        return RunAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunAsyncResourceWithStreamingResponse:
        return RunAsyncResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        dataset_name: str,
        text: run_async_create_params.Variant0Text,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[object] | NotGiven = NOT_GIVEN,
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
        ...

    @overload
    def create(
        self,
        *,
        dataset_name: str,
        document: run_async_create_params.Variant1Document,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[object] | NotGiven = NOT_GIVEN,
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
        ...

    @overload
    def create(
        self,
        *,
        dataset_name: str,
        web: run_async_create_params.Variant2Web,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[object] | NotGiven = NOT_GIVEN,
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
        ...

    @overload
    def create(
        self,
        *,
        dataset_name: str,
        sec_filing: run_async_create_params.Variant3SecFiling,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[object] | NotGiven = NOT_GIVEN,
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
        ...

    @required_args(
        ["dataset_name", "text"], ["dataset_name", "document"], ["dataset_name", "web"], ["dataset_name", "sec_filing"]
    )
    def create(
        self,
        *,
        dataset_name: str,
        text: run_async_create_params.Variant0Text | NotGiven = NOT_GIVEN,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[object] | NotGiven = NOT_GIVEN,
        document: run_async_create_params.Variant1Document | NotGiven = NOT_GIVEN,
        web: run_async_create_params.Variant2Web | NotGiven = NOT_GIVEN,
        sec_filing: run_async_create_params.Variant3SecFiling | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        return self._post(
            "/structure/run_async",
            body=maybe_transform(
                {
                    "text": text,
                    "document": document,
                    "web": web,
                    "sec_filing": sec_filing,
                },
                run_async_create_params.RunAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_name": dataset_name,
                        "custom_instruction": custom_instruction,
                        "llm": llm,
                    },
                    run_async_create_params.RunAsyncCreateParams,
                ),
            ),
            cast_to=object,
        )


class AsyncRunAsyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunAsyncResourceWithRawResponse:
        return AsyncRunAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunAsyncResourceWithStreamingResponse:
        return AsyncRunAsyncResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        dataset_name: str,
        text: run_async_create_params.Variant0Text,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[object] | NotGiven = NOT_GIVEN,
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
        ...

    @overload
    async def create(
        self,
        *,
        dataset_name: str,
        document: run_async_create_params.Variant1Document,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[object] | NotGiven = NOT_GIVEN,
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
        ...

    @overload
    async def create(
        self,
        *,
        dataset_name: str,
        web: run_async_create_params.Variant2Web,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[object] | NotGiven = NOT_GIVEN,
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
        ...

    @overload
    async def create(
        self,
        *,
        dataset_name: str,
        sec_filing: run_async_create_params.Variant3SecFiling,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[object] | NotGiven = NOT_GIVEN,
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
        ...

    @required_args(
        ["dataset_name", "text"], ["dataset_name", "document"], ["dataset_name", "web"], ["dataset_name", "sec_filing"]
    )
    async def create(
        self,
        *,
        dataset_name: str,
        text: run_async_create_params.Variant0Text | NotGiven = NOT_GIVEN,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[object] | NotGiven = NOT_GIVEN,
        document: run_async_create_params.Variant1Document | NotGiven = NOT_GIVEN,
        web: run_async_create_params.Variant2Web | NotGiven = NOT_GIVEN,
        sec_filing: run_async_create_params.Variant3SecFiling | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        return await self._post(
            "/structure/run_async",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "document": document,
                    "web": web,
                    "sec_filing": sec_filing,
                },
                run_async_create_params.RunAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset_name": dataset_name,
                        "custom_instruction": custom_instruction,
                        "llm": llm,
                    },
                    run_async_create_params.RunAsyncCreateParams,
                ),
            ),
            cast_to=object,
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
