# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

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
from ...types.admin import (
    training_dataset_add_params,
    training_dataset_size_params,
    training_dataset_add_datum_params,
    training_dataset_update_datum_params,
    training_dataset_reset_pending_params,
    training_dataset_get_next_unverified_params,
)
from ..._base_client import make_request_options
from ...types.execution_step_param import ExecutionStepParam
from ...types.admin.training_datum_response import TrainingDatumResponse
from ...types.admin.training_dataset_size_response import TrainingDatasetSizeResponse

__all__ = ["TrainingDatasetsResource", "AsyncTrainingDatasetsResource"]


class TrainingDatasetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrainingDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return TrainingDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrainingDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return TrainingDatasetsResourceWithStreamingResponse(self)

    def add(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Creates a new training dataset with the given name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/admin/training_datasets/add_dataset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"dataset_name": dataset_name}, training_dataset_add_params.TrainingDatasetAddParams
                ),
            ),
            cast_to=NoneType,
        )

    def add_datum(
        self,
        *,
        dataset_name: str,
        step: ExecutionStepParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Adds a new training datum to the specified dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/admin/training_datasets/add_datum",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "step": step,
                },
                training_dataset_add_datum_params.TrainingDatasetAddDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_next_unverified(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatumResponse:
        """
        Retrieves the next unverified training datum from the specified dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/training_datasets/next_unverified",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"dataset_name": dataset_name},
                    training_dataset_get_next_unverified_params.TrainingDatasetGetNextUnverifiedParams,
                ),
            ),
            cast_to=TrainingDatumResponse,
        )

    def reset_pending(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Resets all pending training data in the specified dataset back to unverified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/admin/training_datasets/reset_pending",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"dataset_name": dataset_name},
                    training_dataset_reset_pending_params.TrainingDatasetResetPendingParams,
                ),
            ),
            cast_to=NoneType,
        )

    def size(
        self,
        *,
        dataset_name: str,
        status: Optional[Literal["Unverified", "Verified", "Pending", "Skipped"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatasetSizeResponse:
        """
        Returns the number of training data in the specified dataset, filtered by
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/training_datasets/size",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "status": status,
                },
                training_dataset_size_params.TrainingDatasetSizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    def update_datum(
        self,
        *,
        id: str,
        status: Literal["Unverified", "Verified", "Pending", "Skipped"],
        step: ExecutionStepParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates the status and content of an existing training datum.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/admin/training_data/update_datum",
            body=maybe_transform(
                {
                    "id": id,
                    "status": status,
                    "step": step,
                },
                training_dataset_update_datum_params.TrainingDatasetUpdateDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTrainingDatasetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrainingDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrainingDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrainingDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncTrainingDatasetsResourceWithStreamingResponse(self)

    async def add(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Creates a new training dataset with the given name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/admin/training_datasets/add_dataset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_name": dataset_name}, training_dataset_add_params.TrainingDatasetAddParams
                ),
            ),
            cast_to=NoneType,
        )

    async def add_datum(
        self,
        *,
        dataset_name: str,
        step: ExecutionStepParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Adds a new training datum to the specified dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/admin/training_datasets/add_datum",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "step": step,
                },
                training_dataset_add_datum_params.TrainingDatasetAddDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_next_unverified(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatumResponse:
        """
        Retrieves the next unverified training datum from the specified dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/training_datasets/next_unverified",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_name": dataset_name},
                    training_dataset_get_next_unverified_params.TrainingDatasetGetNextUnverifiedParams,
                ),
            ),
            cast_to=TrainingDatumResponse,
        )

    async def reset_pending(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Resets all pending training data in the specified dataset back to unverified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/admin/training_datasets/reset_pending",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_name": dataset_name},
                    training_dataset_reset_pending_params.TrainingDatasetResetPendingParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def size(
        self,
        *,
        dataset_name: str,
        status: Optional[Literal["Unverified", "Verified", "Pending", "Skipped"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatasetSizeResponse:
        """
        Returns the number of training data in the specified dataset, filtered by
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/training_datasets/size",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "status": status,
                },
                training_dataset_size_params.TrainingDatasetSizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=int,
        )

    async def update_datum(
        self,
        *,
        id: str,
        status: Literal["Unverified", "Verified", "Pending", "Skipped"],
        step: ExecutionStepParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates the status and content of an existing training datum.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/admin/training_data/update_datum",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "status": status,
                    "step": step,
                },
                training_dataset_update_datum_params.TrainingDatasetUpdateDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TrainingDatasetsResourceWithRawResponse:
    def __init__(self, training_datasets: TrainingDatasetsResource) -> None:
        self._training_datasets = training_datasets

        self.add = to_raw_response_wrapper(
            training_datasets.add,
        )
        self.add_datum = to_raw_response_wrapper(
            training_datasets.add_datum,
        )
        self.get_next_unverified = to_raw_response_wrapper(
            training_datasets.get_next_unverified,
        )
        self.reset_pending = to_raw_response_wrapper(
            training_datasets.reset_pending,
        )
        self.size = to_raw_response_wrapper(
            training_datasets.size,
        )
        self.update_datum = to_raw_response_wrapper(
            training_datasets.update_datum,
        )


class AsyncTrainingDatasetsResourceWithRawResponse:
    def __init__(self, training_datasets: AsyncTrainingDatasetsResource) -> None:
        self._training_datasets = training_datasets

        self.add = async_to_raw_response_wrapper(
            training_datasets.add,
        )
        self.add_datum = async_to_raw_response_wrapper(
            training_datasets.add_datum,
        )
        self.get_next_unverified = async_to_raw_response_wrapper(
            training_datasets.get_next_unverified,
        )
        self.reset_pending = async_to_raw_response_wrapper(
            training_datasets.reset_pending,
        )
        self.size = async_to_raw_response_wrapper(
            training_datasets.size,
        )
        self.update_datum = async_to_raw_response_wrapper(
            training_datasets.update_datum,
        )


class TrainingDatasetsResourceWithStreamingResponse:
    def __init__(self, training_datasets: TrainingDatasetsResource) -> None:
        self._training_datasets = training_datasets

        self.add = to_streamed_response_wrapper(
            training_datasets.add,
        )
        self.add_datum = to_streamed_response_wrapper(
            training_datasets.add_datum,
        )
        self.get_next_unverified = to_streamed_response_wrapper(
            training_datasets.get_next_unverified,
        )
        self.reset_pending = to_streamed_response_wrapper(
            training_datasets.reset_pending,
        )
        self.size = to_streamed_response_wrapper(
            training_datasets.size,
        )
        self.update_datum = to_streamed_response_wrapper(
            training_datasets.update_datum,
        )


class AsyncTrainingDatasetsResourceWithStreamingResponse:
    def __init__(self, training_datasets: AsyncTrainingDatasetsResource) -> None:
        self._training_datasets = training_datasets

        self.add = async_to_streamed_response_wrapper(
            training_datasets.add,
        )
        self.add_datum = async_to_streamed_response_wrapper(
            training_datasets.add_datum,
        )
        self.get_next_unverified = async_to_streamed_response_wrapper(
            training_datasets.get_next_unverified,
        )
        self.reset_pending = async_to_streamed_response_wrapper(
            training_datasets.reset_pending,
        )
        self.size = async_to_streamed_response_wrapper(
            training_datasets.size,
        )
        self.update_datum = async_to_streamed_response_wrapper(
            training_datasets.update_datum,
        )
