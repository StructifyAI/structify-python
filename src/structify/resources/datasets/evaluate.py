# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..._base_client import make_request_options
from ...types.datasets import (
    evaluate_get_params,
    evaluate_run_params,
    evaluate_list_params,
    evaluate_delete_params,
    evaluate_status_params,
)
from ...types.datasets.evaluate_get_response import EvaluateGetResponse
from ...types.datasets.evaluate_run_response import EvaluateRunResponse
from ...types.datasets.evaluate_list_response import EvaluateListResponse
from ...types.datasets.evaluate_status_response import EvaluateStatusResponse

__all__ = ["EvaluateResource", "AsyncEvaluateResource"]


class EvaluateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return EvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return EvaluateResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        skip: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateListResponse:
        """
        List all dataset evaluation results with pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dataset/evaluate/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    evaluate_list_params.EvaluateListParams,
                ),
            ),
            cast_to=EvaluateListResponse,
        )

    def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a dataset evaluation result by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/dataset/evaluate/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, evaluate_delete_params.EvaluateDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateGetResponse:
        """
        Get a dataset evaluation result by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dataset/evaluate/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, evaluate_get_params.EvaluateGetParams),
            ),
            cast_to=EvaluateGetResponse,
        )

    def run(
        self,
        *,
        dataset_1: str,
        dataset_2: str,
        email_1: str,
        email_2: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateRunResponse:
        """
        Evaluate two datasets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataset/evaluate/run",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_1": dataset_1,
                        "dataset_2": dataset_2,
                        "email_1": email_1,
                        "email_2": email_2,
                    },
                    evaluate_run_params.EvaluateRunParams,
                ),
            ),
            cast_to=EvaluateRunResponse,
        )

    def status(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateStatusResponse:
        """
        Get the status of a dataset evaluation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dataset/evaluate/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, evaluate_status_params.EvaluateStatusParams),
            ),
            cast_to=EvaluateStatusResponse,
        )


class AsyncEvaluateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncEvaluateResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        skip: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateListResponse:
        """
        List all dataset evaluation results with pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dataset/evaluate/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    evaluate_list_params.EvaluateListParams,
                ),
            ),
            cast_to=EvaluateListResponse,
        )

    async def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a dataset evaluation result by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/dataset/evaluate/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, evaluate_delete_params.EvaluateDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateGetResponse:
        """
        Get a dataset evaluation result by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dataset/evaluate/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, evaluate_get_params.EvaluateGetParams),
            ),
            cast_to=EvaluateGetResponse,
        )

    async def run(
        self,
        *,
        dataset_1: str,
        dataset_2: str,
        email_1: str,
        email_2: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateRunResponse:
        """
        Evaluate two datasets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataset/evaluate/run",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset_1": dataset_1,
                        "dataset_2": dataset_2,
                        "email_1": email_1,
                        "email_2": email_2,
                    },
                    evaluate_run_params.EvaluateRunParams,
                ),
            ),
            cast_to=EvaluateRunResponse,
        )

    async def status(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateStatusResponse:
        """
        Get the status of a dataset evaluation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dataset/evaluate/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, evaluate_status_params.EvaluateStatusParams),
            ),
            cast_to=EvaluateStatusResponse,
        )


class EvaluateResourceWithRawResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.list = to_raw_response_wrapper(
            evaluate.list,
        )
        self.delete = to_raw_response_wrapper(
            evaluate.delete,
        )
        self.get = to_raw_response_wrapper(
            evaluate.get,
        )
        self.run = to_raw_response_wrapper(
            evaluate.run,
        )
        self.status = to_raw_response_wrapper(
            evaluate.status,
        )


class AsyncEvaluateResourceWithRawResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.list = async_to_raw_response_wrapper(
            evaluate.list,
        )
        self.delete = async_to_raw_response_wrapper(
            evaluate.delete,
        )
        self.get = async_to_raw_response_wrapper(
            evaluate.get,
        )
        self.run = async_to_raw_response_wrapper(
            evaluate.run,
        )
        self.status = async_to_raw_response_wrapper(
            evaluate.status,
        )


class EvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.list = to_streamed_response_wrapper(
            evaluate.list,
        )
        self.delete = to_streamed_response_wrapper(
            evaluate.delete,
        )
        self.get = to_streamed_response_wrapper(
            evaluate.get,
        )
        self.run = to_streamed_response_wrapper(
            evaluate.run,
        )
        self.status = to_streamed_response_wrapper(
            evaluate.status,
        )


class AsyncEvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.list = async_to_streamed_response_wrapper(
            evaluate.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            evaluate.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            evaluate.get,
        )
        self.run = async_to_streamed_response_wrapper(
            evaluate.run,
        )
        self.status = async_to_streamed_response_wrapper(
            evaluate.status,
        )
