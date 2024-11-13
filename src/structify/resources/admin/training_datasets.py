# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
    training_dataset_list_datums_params,
    training_dataset_remove_datum_params,
    training_dataset_update_datum_params,
    training_dataset_upload_datum_params,
    training_dataset_reset_pending_params,
    training_dataset_get_step_by_id_params,
    training_dataset_get_labeller_stats_params,
    training_dataset_get_next_unverified_params,
    training_dataset_mark_suspicious_datum_params,
)
from ..._base_client import make_request_options
from ...types.admin.training_datum_response import TrainingDatumResponse
from ...types.admin.training_dataset_list_response import TrainingDatasetListResponse
from ...types.admin.training_dataset_size_response import TrainingDatasetSizeResponse
from ...types.admin.training_dataset_list_datums_response import TrainingDatasetListDatumsResponse
from ...types.admin.training_dataset_get_labeller_stats_response import TrainingDatasetGetLabellerStatsResponse

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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatasetListResponse:
        """Lists all training datasets."""
        return self._get(
            "/admin/training_datasets/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingDatasetListResponse,
        )

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
        step_id: str,
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
                    "step_id": step_id,
                },
                training_dataset_add_datum_params.TrainingDatasetAddDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_labeller_stats(
        self,
        *,
        status: Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"],
        dataset_name: Optional[str] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatasetGetLabellerStatsResponse:
        """
        Gets statistics about labellers' work on a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/training_datasets/labeller_stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "status": status,
                        "dataset_name": dataset_name,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    training_dataset_get_labeller_stats_params.TrainingDatasetGetLabellerStatsParams,
                ),
            ),
            cast_to=TrainingDatasetGetLabellerStatsResponse,
        )

    def get_next_unverified(
        self,
        *,
        dataset_name: str,
        status: Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"],
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
                    {
                        "dataset_name": dataset_name,
                        "status": status,
                    },
                    training_dataset_get_next_unverified_params.TrainingDatasetGetNextUnverifiedParams,
                ),
            ),
            cast_to=TrainingDatumResponse,
        )

    def get_step_by_id(
        self,
        *,
        step_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatumResponse:
        """
        Lists all training datums for a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/training_datasets/get_step_by_id",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"step_id": step_id}, training_dataset_get_step_by_id_params.TrainingDatasetGetStepByIDParams
                ),
            ),
            cast_to=TrainingDatumResponse,
        )

    def list_datums(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatasetListDatumsResponse:
        """
        Lists all training datums for a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/training_datasets/list_datums",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"dataset_name": dataset_name}, training_dataset_list_datums_params.TrainingDatasetListDatumsParams
                ),
            ),
            cast_to=TrainingDatasetListDatumsResponse,
        )

    def mark_suspicious_datum(
        self,
        *,
        reason: str,
        step_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/admin/training_datasets/mark_suspicious_datum",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "reason": reason,
                        "step_id": step_id,
                    },
                    training_dataset_mark_suspicious_datum_params.TrainingDatasetMarkSuspiciousDatumParams,
                ),
            ),
            cast_to=NoneType,
        )

    def remove_datum(
        self,
        *,
        step_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes a training datum from the specified dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/admin/training_datasets/remove_datum",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"step_id": step_id}, training_dataset_remove_datum_params.TrainingDatasetRemoveDatumParams
                ),
            ),
            cast_to=NoneType,
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
        end_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"]]
        | NotGiven = NOT_GIVEN,
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
                    "end_date": end_date,
                    "start_date": start_date,
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
        status: Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"],
        updated_tool_calls: Iterable[training_dataset_update_datum_params.UpdatedToolCall],
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
            "/admin/training_datasets/update_datum",
            body=maybe_transform(
                {
                    "id": id,
                    "status": status,
                    "updated_tool_calls": updated_tool_calls,
                },
                training_dataset_update_datum_params.TrainingDatasetUpdateDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upload_datum(
        self,
        *,
        dataset_name: FileTypes,
        step_bytes: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Uploads a new training datum to the specified dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "dataset_name": dataset_name,
                "step_bytes": step_bytes,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["dataset_name"], ["step_bytes"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            "/admin/training_datasets/upload_datum",
            body=maybe_transform(body, training_dataset_upload_datum_params.TrainingDatasetUploadDatumParams),
            files=files,
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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatasetListResponse:
        """Lists all training datasets."""
        return await self._get(
            "/admin/training_datasets/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingDatasetListResponse,
        )

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
        step_id: str,
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
                    "step_id": step_id,
                },
                training_dataset_add_datum_params.TrainingDatasetAddDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_labeller_stats(
        self,
        *,
        status: Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"],
        dataset_name: Optional[str] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatasetGetLabellerStatsResponse:
        """
        Gets statistics about labellers' work on a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/training_datasets/labeller_stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "status": status,
                        "dataset_name": dataset_name,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    training_dataset_get_labeller_stats_params.TrainingDatasetGetLabellerStatsParams,
                ),
            ),
            cast_to=TrainingDatasetGetLabellerStatsResponse,
        )

    async def get_next_unverified(
        self,
        *,
        dataset_name: str,
        status: Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"],
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
                    {
                        "dataset_name": dataset_name,
                        "status": status,
                    },
                    training_dataset_get_next_unverified_params.TrainingDatasetGetNextUnverifiedParams,
                ),
            ),
            cast_to=TrainingDatumResponse,
        )

    async def get_step_by_id(
        self,
        *,
        step_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatumResponse:
        """
        Lists all training datums for a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/training_datasets/get_step_by_id",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"step_id": step_id}, training_dataset_get_step_by_id_params.TrainingDatasetGetStepByIDParams
                ),
            ),
            cast_to=TrainingDatumResponse,
        )

    async def list_datums(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatasetListDatumsResponse:
        """
        Lists all training datums for a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/training_datasets/list_datums",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_name": dataset_name}, training_dataset_list_datums_params.TrainingDatasetListDatumsParams
                ),
            ),
            cast_to=TrainingDatasetListDatumsResponse,
        )

    async def mark_suspicious_datum(
        self,
        *,
        reason: str,
        step_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/admin/training_datasets/mark_suspicious_datum",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "reason": reason,
                        "step_id": step_id,
                    },
                    training_dataset_mark_suspicious_datum_params.TrainingDatasetMarkSuspiciousDatumParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def remove_datum(
        self,
        *,
        step_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes a training datum from the specified dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/admin/training_datasets/remove_datum",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"step_id": step_id}, training_dataset_remove_datum_params.TrainingDatasetRemoveDatumParams
                ),
            ),
            cast_to=NoneType,
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
        end_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"]]
        | NotGiven = NOT_GIVEN,
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
                    "end_date": end_date,
                    "start_date": start_date,
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
        status: Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"],
        updated_tool_calls: Iterable[training_dataset_update_datum_params.UpdatedToolCall],
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
            "/admin/training_datasets/update_datum",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "status": status,
                    "updated_tool_calls": updated_tool_calls,
                },
                training_dataset_update_datum_params.TrainingDatasetUpdateDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upload_datum(
        self,
        *,
        dataset_name: FileTypes,
        step_bytes: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Uploads a new training datum to the specified dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "dataset_name": dataset_name,
                "step_bytes": step_bytes,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["dataset_name"], ["step_bytes"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            "/admin/training_datasets/upload_datum",
            body=await async_maybe_transform(
                body, training_dataset_upload_datum_params.TrainingDatasetUploadDatumParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TrainingDatasetsResourceWithRawResponse:
    def __init__(self, training_datasets: TrainingDatasetsResource) -> None:
        self._training_datasets = training_datasets

        self.list = to_raw_response_wrapper(
            training_datasets.list,
        )
        self.add = to_raw_response_wrapper(
            training_datasets.add,
        )
        self.add_datum = to_raw_response_wrapper(
            training_datasets.add_datum,
        )
        self.get_labeller_stats = to_raw_response_wrapper(
            training_datasets.get_labeller_stats,
        )
        self.get_next_unverified = to_raw_response_wrapper(
            training_datasets.get_next_unverified,
        )
        self.get_step_by_id = to_raw_response_wrapper(
            training_datasets.get_step_by_id,
        )
        self.list_datums = to_raw_response_wrapper(
            training_datasets.list_datums,
        )
        self.mark_suspicious_datum = to_raw_response_wrapper(
            training_datasets.mark_suspicious_datum,
        )
        self.remove_datum = to_raw_response_wrapper(
            training_datasets.remove_datum,
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
        self.upload_datum = to_raw_response_wrapper(
            training_datasets.upload_datum,
        )


class AsyncTrainingDatasetsResourceWithRawResponse:
    def __init__(self, training_datasets: AsyncTrainingDatasetsResource) -> None:
        self._training_datasets = training_datasets

        self.list = async_to_raw_response_wrapper(
            training_datasets.list,
        )
        self.add = async_to_raw_response_wrapper(
            training_datasets.add,
        )
        self.add_datum = async_to_raw_response_wrapper(
            training_datasets.add_datum,
        )
        self.get_labeller_stats = async_to_raw_response_wrapper(
            training_datasets.get_labeller_stats,
        )
        self.get_next_unverified = async_to_raw_response_wrapper(
            training_datasets.get_next_unverified,
        )
        self.get_step_by_id = async_to_raw_response_wrapper(
            training_datasets.get_step_by_id,
        )
        self.list_datums = async_to_raw_response_wrapper(
            training_datasets.list_datums,
        )
        self.mark_suspicious_datum = async_to_raw_response_wrapper(
            training_datasets.mark_suspicious_datum,
        )
        self.remove_datum = async_to_raw_response_wrapper(
            training_datasets.remove_datum,
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
        self.upload_datum = async_to_raw_response_wrapper(
            training_datasets.upload_datum,
        )


class TrainingDatasetsResourceWithStreamingResponse:
    def __init__(self, training_datasets: TrainingDatasetsResource) -> None:
        self._training_datasets = training_datasets

        self.list = to_streamed_response_wrapper(
            training_datasets.list,
        )
        self.add = to_streamed_response_wrapper(
            training_datasets.add,
        )
        self.add_datum = to_streamed_response_wrapper(
            training_datasets.add_datum,
        )
        self.get_labeller_stats = to_streamed_response_wrapper(
            training_datasets.get_labeller_stats,
        )
        self.get_next_unverified = to_streamed_response_wrapper(
            training_datasets.get_next_unverified,
        )
        self.get_step_by_id = to_streamed_response_wrapper(
            training_datasets.get_step_by_id,
        )
        self.list_datums = to_streamed_response_wrapper(
            training_datasets.list_datums,
        )
        self.mark_suspicious_datum = to_streamed_response_wrapper(
            training_datasets.mark_suspicious_datum,
        )
        self.remove_datum = to_streamed_response_wrapper(
            training_datasets.remove_datum,
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
        self.upload_datum = to_streamed_response_wrapper(
            training_datasets.upload_datum,
        )


class AsyncTrainingDatasetsResourceWithStreamingResponse:
    def __init__(self, training_datasets: AsyncTrainingDatasetsResource) -> None:
        self._training_datasets = training_datasets

        self.list = async_to_streamed_response_wrapper(
            training_datasets.list,
        )
        self.add = async_to_streamed_response_wrapper(
            training_datasets.add,
        )
        self.add_datum = async_to_streamed_response_wrapper(
            training_datasets.add_datum,
        )
        self.get_labeller_stats = async_to_streamed_response_wrapper(
            training_datasets.get_labeller_stats,
        )
        self.get_next_unverified = async_to_streamed_response_wrapper(
            training_datasets.get_next_unverified,
        )
        self.get_step_by_id = async_to_streamed_response_wrapper(
            training_datasets.get_step_by_id,
        )
        self.list_datums = async_to_streamed_response_wrapper(
            training_datasets.list_datums,
        )
        self.mark_suspicious_datum = async_to_streamed_response_wrapper(
            training_datasets.mark_suspicious_datum,
        )
        self.remove_datum = async_to_streamed_response_wrapper(
            training_datasets.remove_datum,
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
        self.upload_datum = async_to_streamed_response_wrapper(
            training_datasets.upload_datum,
        )
