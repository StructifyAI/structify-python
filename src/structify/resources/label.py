# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional, overload

import httpx

from ..types import label_run_params, label_submit_params, label_get_messages_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.label_get_messages_response import LabelGetMessagesResponse

__all__ = ["LabelResource", "AsyncLabelResource"]


class LabelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelResourceWithRawResponse:
        return LabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelResourceWithStreamingResponse:
        return LabelResourceWithStreamingResponse(self)

    def get_messages(
        self,
        *,
        uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LabelGetMessagesResponse]:
        """
        web requests that would be cancelled by cloudflare in prod.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/label/refresh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"uuid": uuid}, label_get_messages_params.LabelGetMessagesParams),
            ),
            cast_to=LabelGetMessagesResponse,
        )

    @overload
    def run(
        self,
        *,
        dataset_name: str,
        text: label_run_params.Variant0Text,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        dataset_name: str,
        document: label_run_params.Variant1Document,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        dataset_name: str,
        web: label_run_params.Variant2Web,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        dataset_name: str,
        sec_filing: label_run_params.Variant3SecFiling,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
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
    def run(
        self,
        *,
        dataset_name: str,
        text: label_run_params.Variant0Text | NotGiven = NOT_GIVEN,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        document: label_run_params.Variant1Document | NotGiven = NOT_GIVEN,
        web: label_run_params.Variant2Web | NotGiven = NOT_GIVEN,
        sec_filing: label_run_params.Variant3SecFiling | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/label/run_async",
            body=maybe_transform(
                {
                    "text": text,
                    "document": document,
                    "web": web,
                    "sec_filing": sec_filing,
                },
                label_run_params.LabelRunParams,
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
                    label_run_params.LabelRunParams,
                ),
            ),
            cast_to=NoneType,
        )

    def submit(
        self,
        uuid: str,
        *,
        body: Iterable[label_submit_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit a label as part of the human LLM.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            f"/label/submit/{uuid}",
            body=maybe_transform(body, label_submit_params.LabelSubmitParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncLabelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelResourceWithRawResponse:
        return AsyncLabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelResourceWithStreamingResponse:
        return AsyncLabelResourceWithStreamingResponse(self)

    async def get_messages(
        self,
        *,
        uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LabelGetMessagesResponse]:
        """
        web requests that would be cancelled by cloudflare in prod.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/label/refresh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"uuid": uuid}, label_get_messages_params.LabelGetMessagesParams),
            ),
            cast_to=LabelGetMessagesResponse,
        )

    @overload
    async def run(
        self,
        *,
        dataset_name: str,
        text: label_run_params.Variant0Text,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        dataset_name: str,
        document: label_run_params.Variant1Document,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        dataset_name: str,
        web: label_run_params.Variant2Web,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        dataset_name: str,
        sec_filing: label_run_params.Variant3SecFiling,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
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
    async def run(
        self,
        *,
        dataset_name: str,
        text: label_run_params.Variant0Text | NotGiven = NOT_GIVEN,
        custom_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        document: label_run_params.Variant1Document | NotGiven = NOT_GIVEN,
        web: label_run_params.Variant2Web | NotGiven = NOT_GIVEN,
        sec_filing: label_run_params.Variant3SecFiling | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/label/run_async",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "document": document,
                    "web": web,
                    "sec_filing": sec_filing,
                },
                label_run_params.LabelRunParams,
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
                    label_run_params.LabelRunParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def submit(
        self,
        uuid: str,
        *,
        body: Iterable[label_submit_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit a label as part of the human LLM.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            f"/label/submit/{uuid}",
            body=await async_maybe_transform(body, label_submit_params.LabelSubmitParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class LabelResourceWithRawResponse:
    def __init__(self, label: LabelResource) -> None:
        self._label = label

        self.get_messages = to_raw_response_wrapper(
            label.get_messages,
        )
        self.run = to_raw_response_wrapper(
            label.run,
        )
        self.submit = to_raw_response_wrapper(
            label.submit,
        )


class AsyncLabelResourceWithRawResponse:
    def __init__(self, label: AsyncLabelResource) -> None:
        self._label = label

        self.get_messages = async_to_raw_response_wrapper(
            label.get_messages,
        )
        self.run = async_to_raw_response_wrapper(
            label.run,
        )
        self.submit = async_to_raw_response_wrapper(
            label.submit,
        )


class LabelResourceWithStreamingResponse:
    def __init__(self, label: LabelResource) -> None:
        self._label = label

        self.get_messages = to_streamed_response_wrapper(
            label.get_messages,
        )
        self.run = to_streamed_response_wrapper(
            label.run,
        )
        self.submit = to_streamed_response_wrapper(
            label.submit,
        )


class AsyncLabelResourceWithStreamingResponse:
    def __init__(self, label: AsyncLabelResource) -> None:
        self._label = label

        self.get_messages = async_to_streamed_response_wrapper(
            label.get_messages,
        )
        self.run = async_to_streamed_response_wrapper(
            label.run,
        )
        self.submit = async_to_streamed_response_wrapper(
            label.submit,
        )
