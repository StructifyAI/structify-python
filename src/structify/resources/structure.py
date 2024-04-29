# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional, overload

import httpx

from ..types import (
    structure_execute_params,
    structure_execute_async_params,
    structure_mark_complete_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.is_complete import IsComplete

__all__ = ["StructureResource", "AsyncStructureResource"]


class StructureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StructureResourceWithRawResponse:
        return StructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StructureResourceWithStreamingResponse:
        return StructureResourceWithStreamingResponse(self)

    @overload
    def execute(
        self,
        *,
        dataset_name: str,
        text: structure_execute_params.Variant0Text,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    def execute(
        self,
        *,
        dataset_name: str,
        document: structure_execute_params.Variant1Document,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    def execute(
        self,
        *,
        dataset_name: str,
        web: structure_execute_params.Variant2Web,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    def execute(
        self,
        *,
        dataset_name: str,
        sec_filing: structure_execute_params.Variant3SecFiling,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    def execute(
        self,
        *,
        dataset_name: str,
        text: structure_execute_params.Variant0Text | NotGiven = NOT_GIVEN,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        document: structure_execute_params.Variant1Document | NotGiven = NOT_GIVEN,
        web: structure_execute_params.Variant2Web | NotGiven = NOT_GIVEN,
        sec_filing: structure_execute_params.Variant3SecFiling | NotGiven = NOT_GIVEN,
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
                structure_execute_params.StructureExecuteParams,
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
                    },
                    structure_execute_params.StructureExecuteParams,
                ),
            ),
            cast_to=object,
        )

    @overload
    def execute_async(
        self,
        *,
        dataset_name: str,
        text: structure_execute_async_params.Variant0Text,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    def execute_async(
        self,
        *,
        dataset_name: str,
        document: structure_execute_async_params.Variant1Document,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    def execute_async(
        self,
        *,
        dataset_name: str,
        web: structure_execute_async_params.Variant2Web,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    def execute_async(
        self,
        *,
        dataset_name: str,
        sec_filing: structure_execute_async_params.Variant3SecFiling,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    def execute_async(
        self,
        *,
        dataset_name: str,
        text: structure_execute_async_params.Variant0Text | NotGiven = NOT_GIVEN,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        document: structure_execute_async_params.Variant1Document | NotGiven = NOT_GIVEN,
        web: structure_execute_async_params.Variant2Web | NotGiven = NOT_GIVEN,
        sec_filing: structure_execute_async_params.Variant3SecFiling | NotGiven = NOT_GIVEN,
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
                structure_execute_async_params.StructureExecuteAsyncParams,
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
                    },
                    structure_execute_async_params.StructureExecuteAsyncParams,
                ),
            ),
            cast_to=object,
        )

    def mark_complete(
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
            body=maybe_transform(body, structure_mark_complete_params.StructureMarkCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IsComplete,
        )


class AsyncStructureResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStructureResourceWithRawResponse:
        return AsyncStructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStructureResourceWithStreamingResponse:
        return AsyncStructureResourceWithStreamingResponse(self)

    @overload
    async def execute(
        self,
        *,
        dataset_name: str,
        text: structure_execute_params.Variant0Text,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    async def execute(
        self,
        *,
        dataset_name: str,
        document: structure_execute_params.Variant1Document,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    async def execute(
        self,
        *,
        dataset_name: str,
        web: structure_execute_params.Variant2Web,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    async def execute(
        self,
        *,
        dataset_name: str,
        sec_filing: structure_execute_params.Variant3SecFiling,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    async def execute(
        self,
        *,
        dataset_name: str,
        text: structure_execute_params.Variant0Text | NotGiven = NOT_GIVEN,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        document: structure_execute_params.Variant1Document | NotGiven = NOT_GIVEN,
        web: structure_execute_params.Variant2Web | NotGiven = NOT_GIVEN,
        sec_filing: structure_execute_params.Variant3SecFiling | NotGiven = NOT_GIVEN,
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
                structure_execute_params.StructureExecuteParams,
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
                    },
                    structure_execute_params.StructureExecuteParams,
                ),
            ),
            cast_to=object,
        )

    @overload
    async def execute_async(
        self,
        *,
        dataset_name: str,
        text: structure_execute_async_params.Variant0Text,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    async def execute_async(
        self,
        *,
        dataset_name: str,
        document: structure_execute_async_params.Variant1Document,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    async def execute_async(
        self,
        *,
        dataset_name: str,
        web: structure_execute_async_params.Variant2Web,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    async def execute_async(
        self,
        *,
        dataset_name: str,
        sec_filing: structure_execute_async_params.Variant3SecFiling,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
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
    async def execute_async(
        self,
        *,
        dataset_name: str,
        text: structure_execute_async_params.Variant0Text | NotGiven = NOT_GIVEN,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        document: structure_execute_async_params.Variant1Document | NotGiven = NOT_GIVEN,
        web: structure_execute_async_params.Variant2Web | NotGiven = NOT_GIVEN,
        sec_filing: structure_execute_async_params.Variant3SecFiling | NotGiven = NOT_GIVEN,
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
                structure_execute_async_params.StructureExecuteAsyncParams,
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
                    },
                    structure_execute_async_params.StructureExecuteAsyncParams,
                ),
            ),
            cast_to=object,
        )

    async def mark_complete(
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
            body=await async_maybe_transform(body, structure_mark_complete_params.StructureMarkCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IsComplete,
        )


class StructureResourceWithRawResponse:
    def __init__(self, structure: StructureResource) -> None:
        self._structure = structure

        self.execute = to_raw_response_wrapper(
            structure.execute,
        )
        self.execute_async = to_raw_response_wrapper(
            structure.execute_async,
        )
        self.mark_complete = to_raw_response_wrapper(
            structure.mark_complete,
        )


class AsyncStructureResourceWithRawResponse:
    def __init__(self, structure: AsyncStructureResource) -> None:
        self._structure = structure

        self.execute = async_to_raw_response_wrapper(
            structure.execute,
        )
        self.execute_async = async_to_raw_response_wrapper(
            structure.execute_async,
        )
        self.mark_complete = async_to_raw_response_wrapper(
            structure.mark_complete,
        )


class StructureResourceWithStreamingResponse:
    def __init__(self, structure: StructureResource) -> None:
        self._structure = structure

        self.execute = to_streamed_response_wrapper(
            structure.execute,
        )
        self.execute_async = to_streamed_response_wrapper(
            structure.execute_async,
        )
        self.mark_complete = to_streamed_response_wrapper(
            structure.mark_complete,
        )


class AsyncStructureResourceWithStreamingResponse:
    def __init__(self, structure: AsyncStructureResource) -> None:
        self._structure = structure

        self.execute = async_to_streamed_response_wrapper(
            structure.execute,
        )
        self.execute_async = async_to_streamed_response_wrapper(
            structure.execute_async,
        )
        self.mark_complete = async_to_streamed_response_wrapper(
            structure.mark_complete,
        )
