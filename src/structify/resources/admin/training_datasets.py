# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Mapping, Iterable, Optional, cast
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
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.admin import (
    training_dataset_add_params,
    training_dataset_size_params,
    training_dataset_add_datum_params,
    training_dataset_label_datum_params,
    training_dataset_list_datums_params,
    training_dataset_remove_datum_params,
    training_dataset_verify_datum_params,
    training_dataset_download_datum_params,
    training_dataset_get_datum_info_params,
    training_dataset_get_next_datum_params,
    training_dataset_switch_dataset_params,
    training_dataset_get_labeller_stats_params,
    training_dataset_update_datum_status_params,
    training_dataset_upload_labeled_step_params,
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
        This property can be used as a prefix for any HTTP method call to return
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

    def download_datum(
        self,
        *,
        step_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Lists all training datums for a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            "/admin/training_datasets/download_datum_step",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"step_id": step_id}, training_dataset_download_datum_params.TrainingDatasetDownloadDatumParams
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_datum_info(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatumResponse:
        """This includes the status, step, last updated time, and all updates.

        If the datum
        does not exist, a 204 status is returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/training_datasets/get_datum_info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"id": id}, training_dataset_get_datum_info_params.TrainingDatasetGetDatumInfoParams
                ),
            ),
            cast_to=TrainingDatumResponse,
        )

    def get_labeller_stats(
        self,
        *,
        status: Literal[
            "Unlabeled",
            "NavLabeled",
            "SaveLabeled",
            "Verified",
            "Pending",
            "Skipped",
            "SuspiciousNav",
            "SuspiciousSave",
        ],
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

    def get_next_datum(
        self,
        *,
        dataset_name: str,
        status: Literal[
            "Unlabeled",
            "NavLabeled",
            "SaveLabeled",
            "Verified",
            "Pending",
            "Skipped",
            "SuspiciousNav",
            "SuspiciousSave",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TrainingDatumResponse]:
        """
        Returns None if no datum is available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/training_datasets/get_next_datum",
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
                    training_dataset_get_next_datum_params.TrainingDatasetGetNextDatumParams,
                ),
            ),
            cast_to=TrainingDatumResponse,
        )

    def label_datum(
        self,
        *,
        id: str,
        status: Literal[
            "Unlabeled",
            "NavLabeled",
            "SaveLabeled",
            "Verified",
            "Pending",
            "Skipped",
            "SuspiciousNav",
            "SuspiciousSave",
        ],
        updated_tool_calls: Iterable[training_dataset_label_datum_params.UpdatedToolCall],
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
            "/admin/training_datasets/label_datum",
            body=maybe_transform(
                {
                    "id": id,
                    "status": status,
                    "updated_tool_calls": updated_tool_calls,
                },
                training_dataset_label_datum_params.TrainingDatasetLabelDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_datums(
        self,
        *,
        dataset_name: str,
        last_updated: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
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
                    {
                        "dataset_name": dataset_name,
                        "last_updated": last_updated,
                    },
                    training_dataset_list_datums_params.TrainingDatasetListDatumsParams,
                ),
            ),
            cast_to=TrainingDatasetListDatumsResponse,
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
            "/admin/training_datasets/remove_from_dataset",
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

    def size(
        self,
        *,
        dataset_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        status: Optional[
            Literal[
                "Unlabeled",
                "NavLabeled",
                "SaveLabeled",
                "Verified",
                "Pending",
                "Skipped",
                "SuspiciousNav",
                "SuspiciousSave",
            ]
        ]
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
                    "dataset_names": dataset_names,
                    "end_date": end_date,
                    "start_date": start_date,
                    "status": status,
                },
                training_dataset_size_params.TrainingDatasetSizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingDatasetSizeResponse,
        )

    def switch_dataset(
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
        Switches a training datum to a new dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/admin/training_datasets/switch_dataset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_name": dataset_name,
                        "step_id": step_id,
                    },
                    training_dataset_switch_dataset_params.TrainingDatasetSwitchDatasetParams,
                ),
            ),
            cast_to=NoneType,
        )

    def update_datum_status(
        self,
        *,
        id: str,
        status: Literal[
            "Unlabeled",
            "NavLabeled",
            "SaveLabeled",
            "Verified",
            "Pending",
            "Skipped",
            "SuspiciousNav",
            "SuspiciousSave",
        ],
        review_message: Optional[str] | NotGiven = NOT_GIVEN,
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
            "/admin/training_datasets/update_datum_status",
            body=maybe_transform(
                {
                    "id": id,
                    "status": status,
                    "review_message": review_message,
                },
                training_dataset_update_datum_status_params.TrainingDatasetUpdateDatumStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upload_labeled_step(
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
            "/admin/training_datasets/upload_labeled_step",
            body=maybe_transform(
                body, training_dataset_upload_labeled_step_params.TrainingDatasetUploadLabeledStepParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def verify_datum(
        self,
        *,
        id: str,
        verified_nav_id: str,
        verified_save_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Verifies a training datum update.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/admin/training_datasets/verify_datum",
            body=maybe_transform(
                {
                    "id": id,
                    "verified_nav_id": verified_nav_id,
                    "verified_save_id": verified_save_id,
                },
                training_dataset_verify_datum_params.TrainingDatasetVerifyDatumParams,
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
        This property can be used as a prefix for any HTTP method call to return
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

    async def download_datum(
        self,
        *,
        step_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Lists all training datums for a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            "/admin/training_datasets/download_datum_step",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"step_id": step_id}, training_dataset_download_datum_params.TrainingDatasetDownloadDatumParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_datum_info(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingDatumResponse:
        """This includes the status, step, last updated time, and all updates.

        If the datum
        does not exist, a 204 status is returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/training_datasets/get_datum_info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id": id}, training_dataset_get_datum_info_params.TrainingDatasetGetDatumInfoParams
                ),
            ),
            cast_to=TrainingDatumResponse,
        )

    async def get_labeller_stats(
        self,
        *,
        status: Literal[
            "Unlabeled",
            "NavLabeled",
            "SaveLabeled",
            "Verified",
            "Pending",
            "Skipped",
            "SuspiciousNav",
            "SuspiciousSave",
        ],
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

    async def get_next_datum(
        self,
        *,
        dataset_name: str,
        status: Literal[
            "Unlabeled",
            "NavLabeled",
            "SaveLabeled",
            "Verified",
            "Pending",
            "Skipped",
            "SuspiciousNav",
            "SuspiciousSave",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TrainingDatumResponse]:
        """
        Returns None if no datum is available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/training_datasets/get_next_datum",
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
                    training_dataset_get_next_datum_params.TrainingDatasetGetNextDatumParams,
                ),
            ),
            cast_to=TrainingDatumResponse,
        )

    async def label_datum(
        self,
        *,
        id: str,
        status: Literal[
            "Unlabeled",
            "NavLabeled",
            "SaveLabeled",
            "Verified",
            "Pending",
            "Skipped",
            "SuspiciousNav",
            "SuspiciousSave",
        ],
        updated_tool_calls: Iterable[training_dataset_label_datum_params.UpdatedToolCall],
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
            "/admin/training_datasets/label_datum",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "status": status,
                    "updated_tool_calls": updated_tool_calls,
                },
                training_dataset_label_datum_params.TrainingDatasetLabelDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_datums(
        self,
        *,
        dataset_name: str,
        last_updated: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
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
                    {
                        "dataset_name": dataset_name,
                        "last_updated": last_updated,
                    },
                    training_dataset_list_datums_params.TrainingDatasetListDatumsParams,
                ),
            ),
            cast_to=TrainingDatasetListDatumsResponse,
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
            "/admin/training_datasets/remove_from_dataset",
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

    async def size(
        self,
        *,
        dataset_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        status: Optional[
            Literal[
                "Unlabeled",
                "NavLabeled",
                "SaveLabeled",
                "Verified",
                "Pending",
                "Skipped",
                "SuspiciousNav",
                "SuspiciousSave",
            ]
        ]
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
                    "dataset_names": dataset_names,
                    "end_date": end_date,
                    "start_date": start_date,
                    "status": status,
                },
                training_dataset_size_params.TrainingDatasetSizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingDatasetSizeResponse,
        )

    async def switch_dataset(
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
        Switches a training datum to a new dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/admin/training_datasets/switch_dataset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset_name": dataset_name,
                        "step_id": step_id,
                    },
                    training_dataset_switch_dataset_params.TrainingDatasetSwitchDatasetParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def update_datum_status(
        self,
        *,
        id: str,
        status: Literal[
            "Unlabeled",
            "NavLabeled",
            "SaveLabeled",
            "Verified",
            "Pending",
            "Skipped",
            "SuspiciousNav",
            "SuspiciousSave",
        ],
        review_message: Optional[str] | NotGiven = NOT_GIVEN,
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
            "/admin/training_datasets/update_datum_status",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "status": status,
                    "review_message": review_message,
                },
                training_dataset_update_datum_status_params.TrainingDatasetUpdateDatumStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upload_labeled_step(
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
            "/admin/training_datasets/upload_labeled_step",
            body=await async_maybe_transform(
                body, training_dataset_upload_labeled_step_params.TrainingDatasetUploadLabeledStepParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def verify_datum(
        self,
        *,
        id: str,
        verified_nav_id: str,
        verified_save_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Verifies a training datum update.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/admin/training_datasets/verify_datum",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "verified_nav_id": verified_nav_id,
                    "verified_save_id": verified_save_id,
                },
                training_dataset_verify_datum_params.TrainingDatasetVerifyDatumParams,
            ),
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
        self.download_datum = to_custom_raw_response_wrapper(
            training_datasets.download_datum,
            BinaryAPIResponse,
        )
        self.get_datum_info = to_raw_response_wrapper(
            training_datasets.get_datum_info,
        )
        self.get_labeller_stats = to_raw_response_wrapper(
            training_datasets.get_labeller_stats,
        )
        self.get_next_datum = to_raw_response_wrapper(
            training_datasets.get_next_datum,
        )
        self.label_datum = to_raw_response_wrapper(
            training_datasets.label_datum,
        )
        self.list_datums = to_raw_response_wrapper(
            training_datasets.list_datums,
        )
        self.remove_datum = to_raw_response_wrapper(
            training_datasets.remove_datum,
        )
        self.size = to_raw_response_wrapper(
            training_datasets.size,
        )
        self.switch_dataset = to_raw_response_wrapper(
            training_datasets.switch_dataset,
        )
        self.update_datum_status = to_raw_response_wrapper(
            training_datasets.update_datum_status,
        )
        self.upload_labeled_step = to_raw_response_wrapper(
            training_datasets.upload_labeled_step,
        )
        self.verify_datum = to_raw_response_wrapper(
            training_datasets.verify_datum,
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
        self.download_datum = async_to_custom_raw_response_wrapper(
            training_datasets.download_datum,
            AsyncBinaryAPIResponse,
        )
        self.get_datum_info = async_to_raw_response_wrapper(
            training_datasets.get_datum_info,
        )
        self.get_labeller_stats = async_to_raw_response_wrapper(
            training_datasets.get_labeller_stats,
        )
        self.get_next_datum = async_to_raw_response_wrapper(
            training_datasets.get_next_datum,
        )
        self.label_datum = async_to_raw_response_wrapper(
            training_datasets.label_datum,
        )
        self.list_datums = async_to_raw_response_wrapper(
            training_datasets.list_datums,
        )
        self.remove_datum = async_to_raw_response_wrapper(
            training_datasets.remove_datum,
        )
        self.size = async_to_raw_response_wrapper(
            training_datasets.size,
        )
        self.switch_dataset = async_to_raw_response_wrapper(
            training_datasets.switch_dataset,
        )
        self.update_datum_status = async_to_raw_response_wrapper(
            training_datasets.update_datum_status,
        )
        self.upload_labeled_step = async_to_raw_response_wrapper(
            training_datasets.upload_labeled_step,
        )
        self.verify_datum = async_to_raw_response_wrapper(
            training_datasets.verify_datum,
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
        self.download_datum = to_custom_streamed_response_wrapper(
            training_datasets.download_datum,
            StreamedBinaryAPIResponse,
        )
        self.get_datum_info = to_streamed_response_wrapper(
            training_datasets.get_datum_info,
        )
        self.get_labeller_stats = to_streamed_response_wrapper(
            training_datasets.get_labeller_stats,
        )
        self.get_next_datum = to_streamed_response_wrapper(
            training_datasets.get_next_datum,
        )
        self.label_datum = to_streamed_response_wrapper(
            training_datasets.label_datum,
        )
        self.list_datums = to_streamed_response_wrapper(
            training_datasets.list_datums,
        )
        self.remove_datum = to_streamed_response_wrapper(
            training_datasets.remove_datum,
        )
        self.size = to_streamed_response_wrapper(
            training_datasets.size,
        )
        self.switch_dataset = to_streamed_response_wrapper(
            training_datasets.switch_dataset,
        )
        self.update_datum_status = to_streamed_response_wrapper(
            training_datasets.update_datum_status,
        )
        self.upload_labeled_step = to_streamed_response_wrapper(
            training_datasets.upload_labeled_step,
        )
        self.verify_datum = to_streamed_response_wrapper(
            training_datasets.verify_datum,
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
        self.download_datum = async_to_custom_streamed_response_wrapper(
            training_datasets.download_datum,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_datum_info = async_to_streamed_response_wrapper(
            training_datasets.get_datum_info,
        )
        self.get_labeller_stats = async_to_streamed_response_wrapper(
            training_datasets.get_labeller_stats,
        )
        self.get_next_datum = async_to_streamed_response_wrapper(
            training_datasets.get_next_datum,
        )
        self.label_datum = async_to_streamed_response_wrapper(
            training_datasets.label_datum,
        )
        self.list_datums = async_to_streamed_response_wrapper(
            training_datasets.list_datums,
        )
        self.remove_datum = async_to_streamed_response_wrapper(
            training_datasets.remove_datum,
        )
        self.size = async_to_streamed_response_wrapper(
            training_datasets.size,
        )
        self.switch_dataset = async_to_streamed_response_wrapper(
            training_datasets.switch_dataset,
        )
        self.update_datum_status = async_to_streamed_response_wrapper(
            training_datasets.update_datum_status,
        )
        self.upload_labeled_step = async_to_streamed_response_wrapper(
            training_datasets.upload_labeled_step,
        )
        self.verify_datum = async_to_streamed_response_wrapper(
            training_datasets.verify_datum,
        )
