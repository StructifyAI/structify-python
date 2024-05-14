# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional, overload
from typing_extensions import Literal

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
from ...types.structure import run_create_params

__all__ = ["RunResource", "AsyncRunResource"]


class RunResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunResourceWithRawResponse:
        return RunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunResourceWithStreamingResponse:
        return RunResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        dataset_name: str,
        text: run_create_params.Variant0Text,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[Literal["Gpt4V", "Structify", "Human"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Structure an unstructured data source into the given dataset.

        There's a couple of different types of sources. Right now, you can either add a
        file path or the internet as a whole. In the future, we'll allow you to pare
        down the internet to a specific domain or criterium.

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
        document: run_create_params.Variant1Document,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[Literal["Gpt4V", "Structify", "Human"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Structure an unstructured data source into the given dataset.

        There's a couple of different types of sources. Right now, you can either add a
        file path or the internet as a whole. In the future, we'll allow you to pare
        down the internet to a specific domain or criterium.

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
        web: run_create_params.Variant2Web,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[Literal["Gpt4V", "Structify", "Human"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Structure an unstructured data source into the given dataset.

        There's a couple of different types of sources. Right now, you can either add a
        file path or the internet as a whole. In the future, we'll allow you to pare
        down the internet to a specific domain or criterium.

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
        sec_filing: run_create_params.Variant3SecFiling,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[Literal["Gpt4V", "Structify", "Human"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Structure an unstructured data source into the given dataset.

        There's a couple of different types of sources. Right now, you can either add a
        file path or the internet as a whole. In the future, we'll allow you to pare
        down the internet to a specific domain or criterium.

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
        text: run_create_params.Variant0Text | NotGiven = NOT_GIVEN,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[Literal["Gpt4V", "Structify", "Human"]] | NotGiven = NOT_GIVEN,
        document: run_create_params.Variant1Document | NotGiven = NOT_GIVEN,
        web: run_create_params.Variant2Web | NotGiven = NOT_GIVEN,
        sec_filing: run_create_params.Variant3SecFiling | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        return self._post(
            "/structure/run",
            body=maybe_transform(
                {
                    "text": text,
                    "document": document,
                    "web": web,
                    "sec_filing": sec_filing,
                },
                run_create_params.RunCreateParams,
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
                    run_create_params.RunCreateParams,
                ),
            ),
            cast_to=object,
        )


class AsyncRunResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunResourceWithRawResponse:
        return AsyncRunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunResourceWithStreamingResponse:
        return AsyncRunResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        dataset_name: str,
        text: run_create_params.Variant0Text,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[Literal["Gpt4V", "Structify", "Human"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Structure an unstructured data source into the given dataset.

        There's a couple of different types of sources. Right now, you can either add a
        file path or the internet as a whole. In the future, we'll allow you to pare
        down the internet to a specific domain or criterium.

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
        document: run_create_params.Variant1Document,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[Literal["Gpt4V", "Structify", "Human"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Structure an unstructured data source into the given dataset.

        There's a couple of different types of sources. Right now, you can either add a
        file path or the internet as a whole. In the future, we'll allow you to pare
        down the internet to a specific domain or criterium.

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
        web: run_create_params.Variant2Web,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[Literal["Gpt4V", "Structify", "Human"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Structure an unstructured data source into the given dataset.

        There's a couple of different types of sources. Right now, you can either add a
        file path or the internet as a whole. In the future, we'll allow you to pare
        down the internet to a specific domain or criterium.

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
        sec_filing: run_create_params.Variant3SecFiling,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[Literal["Gpt4V", "Structify", "Human"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Structure an unstructured data source into the given dataset.

        There's a couple of different types of sources. Right now, you can either add a
        file path or the internet as a whole. In the future, we'll allow you to pare
        down the internet to a specific domain or criterium.

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
        text: run_create_params.Variant0Text | NotGiven = NOT_GIVEN,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        llm: Optional[Literal["Gpt4V", "Structify", "Human"]] | NotGiven = NOT_GIVEN,
        document: run_create_params.Variant1Document | NotGiven = NOT_GIVEN,
        web: run_create_params.Variant2Web | NotGiven = NOT_GIVEN,
        sec_filing: run_create_params.Variant3SecFiling | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        return await self._post(
            "/structure/run",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "document": document,
                    "web": web,
                    "sec_filing": sec_filing,
                },
                run_create_params.RunCreateParams,
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
                    run_create_params.RunCreateParams,
                ),
            ),
            cast_to=object,
        )


class RunResourceWithRawResponse:
    def __init__(self, run: RunResource) -> None:
        self._run = run

        self.create = to_raw_response_wrapper(
            run.create,
        )


class AsyncRunResourceWithRawResponse:
    def __init__(self, run: AsyncRunResource) -> None:
        self._run = run

        self.create = async_to_raw_response_wrapper(
            run.create,
        )


class RunResourceWithStreamingResponse:
    def __init__(self, run: RunResource) -> None:
        self._run = run

        self.create = to_streamed_response_wrapper(
            run.create,
        )


class AsyncRunResourceWithStreamingResponse:
    def __init__(self, run: AsyncRunResource) -> None:
        self._run = run

        self.create = async_to_streamed_response_wrapper(
            run.create,
        )
