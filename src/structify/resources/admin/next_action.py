# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import (
    next_action_get_training_data_params,
    next_action_add_training_datum_params,
    next_action_get_training_datum_params,
    next_action_delete_training_data_params,
    next_action_label_training_datum_params,
    next_action_get_batched_training_data_params,
)
from ..._base_client import make_request_options
from ...types.admin.action_training_data_entry import ActionTrainingDataEntry
from ...types.admin.action_training_data_response import ActionTrainingDataResponse
from ...types.admin.delete_action_training_data_response import DeleteActionTrainingDataResponse

__all__ = ["NextActionResource", "AsyncNextActionResource"]


class NextActionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NextActionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return NextActionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NextActionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return NextActionResourceWithStreamingResponse(self)

    def add_training_datum(
        self,
        *,
        input: next_action_add_training_datum_params.Input,
        label: str,
        output: next_action_add_training_datum_params.Output,
        job_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add a new action training datum

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/admin/next_action/add_action_training_datum",
            body=maybe_transform(
                {
                    "input": input,
                    "label": label,
                    "output": output,
                    "job_id": job_id,
                },
                next_action_add_training_datum_params.NextActionAddTrainingDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_training_data(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteActionTrainingDataResponse:
        """
        Args:
          id: ID of the training datum to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/admin/next_action/delete_action_training_data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"id": id}, next_action_delete_training_data_params.NextActionDeleteTrainingDataParams
                ),
            ),
            cast_to=DeleteActionTrainingDataResponse,
        )

    def get_batched_training_data(
        self,
        *,
        job_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionTrainingDataResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/next_action/get_batched_action_training_data",
            body=maybe_transform(
                {"job_ids": job_ids},
                next_action_get_batched_training_data_params.NextActionGetBatchedTrainingDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionTrainingDataResponse,
        )

    def get_training_data(
        self,
        *,
        from_date: Union[str, datetime, None] | Omit = omit,
        job_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Optional[Literal["HumanLLMLabel", "LLMOutput", "Pending", "Reviewed", "Verified", "Others"]]
        | Omit = omit,
        to_date: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionTrainingDataResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/next_action/get_action_training_data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_date": from_date,
                        "job_id": job_id,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                        "to_date": to_date,
                    },
                    next_action_get_training_data_params.NextActionGetTrainingDataParams,
                ),
            ),
            cast_to=ActionTrainingDataResponse,
        )

    def get_training_datum(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionTrainingDataEntry:
        """
        Args:
          id: ID of the training datum to get

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/next_action/get_action_training_datum",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"id": id}, next_action_get_training_datum_params.NextActionGetTrainingDatumParams
                ),
            ),
            cast_to=ActionTrainingDataEntry,
        )

    def label_training_datum(
        self,
        *,
        id: str,
        label: str,
        output: next_action_label_training_datum_params.Output,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Label an existing action training datum

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/admin/next_action/label_action_training_datum",
            body=maybe_transform(
                {
                    "id": id,
                    "label": label,
                    "output": output,
                },
                next_action_label_training_datum_params.NextActionLabelTrainingDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncNextActionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNextActionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNextActionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNextActionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncNextActionResourceWithStreamingResponse(self)

    async def add_training_datum(
        self,
        *,
        input: next_action_add_training_datum_params.Input,
        label: str,
        output: next_action_add_training_datum_params.Output,
        job_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add a new action training datum

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/admin/next_action/add_action_training_datum",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "label": label,
                    "output": output,
                    "job_id": job_id,
                },
                next_action_add_training_datum_params.NextActionAddTrainingDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_training_data(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteActionTrainingDataResponse:
        """
        Args:
          id: ID of the training datum to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/admin/next_action/delete_action_training_data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id": id}, next_action_delete_training_data_params.NextActionDeleteTrainingDataParams
                ),
            ),
            cast_to=DeleteActionTrainingDataResponse,
        )

    async def get_batched_training_data(
        self,
        *,
        job_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionTrainingDataResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/next_action/get_batched_action_training_data",
            body=await async_maybe_transform(
                {"job_ids": job_ids},
                next_action_get_batched_training_data_params.NextActionGetBatchedTrainingDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionTrainingDataResponse,
        )

    async def get_training_data(
        self,
        *,
        from_date: Union[str, datetime, None] | Omit = omit,
        job_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Optional[Literal["HumanLLMLabel", "LLMOutput", "Pending", "Reviewed", "Verified", "Others"]]
        | Omit = omit,
        to_date: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionTrainingDataResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/next_action/get_action_training_data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_date": from_date,
                        "job_id": job_id,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                        "to_date": to_date,
                    },
                    next_action_get_training_data_params.NextActionGetTrainingDataParams,
                ),
            ),
            cast_to=ActionTrainingDataResponse,
        )

    async def get_training_datum(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionTrainingDataEntry:
        """
        Args:
          id: ID of the training datum to get

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/next_action/get_action_training_datum",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id": id}, next_action_get_training_datum_params.NextActionGetTrainingDatumParams
                ),
            ),
            cast_to=ActionTrainingDataEntry,
        )

    async def label_training_datum(
        self,
        *,
        id: str,
        label: str,
        output: next_action_label_training_datum_params.Output,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Label an existing action training datum

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/admin/next_action/label_action_training_datum",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "label": label,
                    "output": output,
                },
                next_action_label_training_datum_params.NextActionLabelTrainingDatumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class NextActionResourceWithRawResponse:
    def __init__(self, next_action: NextActionResource) -> None:
        self._next_action = next_action

        self.add_training_datum = to_raw_response_wrapper(
            next_action.add_training_datum,
        )
        self.delete_training_data = to_raw_response_wrapper(
            next_action.delete_training_data,
        )
        self.get_batched_training_data = to_raw_response_wrapper(
            next_action.get_batched_training_data,
        )
        self.get_training_data = to_raw_response_wrapper(
            next_action.get_training_data,
        )
        self.get_training_datum = to_raw_response_wrapper(
            next_action.get_training_datum,
        )
        self.label_training_datum = to_raw_response_wrapper(
            next_action.label_training_datum,
        )


class AsyncNextActionResourceWithRawResponse:
    def __init__(self, next_action: AsyncNextActionResource) -> None:
        self._next_action = next_action

        self.add_training_datum = async_to_raw_response_wrapper(
            next_action.add_training_datum,
        )
        self.delete_training_data = async_to_raw_response_wrapper(
            next_action.delete_training_data,
        )
        self.get_batched_training_data = async_to_raw_response_wrapper(
            next_action.get_batched_training_data,
        )
        self.get_training_data = async_to_raw_response_wrapper(
            next_action.get_training_data,
        )
        self.get_training_datum = async_to_raw_response_wrapper(
            next_action.get_training_datum,
        )
        self.label_training_datum = async_to_raw_response_wrapper(
            next_action.label_training_datum,
        )


class NextActionResourceWithStreamingResponse:
    def __init__(self, next_action: NextActionResource) -> None:
        self._next_action = next_action

        self.add_training_datum = to_streamed_response_wrapper(
            next_action.add_training_datum,
        )
        self.delete_training_data = to_streamed_response_wrapper(
            next_action.delete_training_data,
        )
        self.get_batched_training_data = to_streamed_response_wrapper(
            next_action.get_batched_training_data,
        )
        self.get_training_data = to_streamed_response_wrapper(
            next_action.get_training_data,
        )
        self.get_training_datum = to_streamed_response_wrapper(
            next_action.get_training_datum,
        )
        self.label_training_datum = to_streamed_response_wrapper(
            next_action.label_training_datum,
        )


class AsyncNextActionResourceWithStreamingResponse:
    def __init__(self, next_action: AsyncNextActionResource) -> None:
        self._next_action = next_action

        self.add_training_datum = async_to_streamed_response_wrapper(
            next_action.add_training_datum,
        )
        self.delete_training_data = async_to_streamed_response_wrapper(
            next_action.delete_training_data,
        )
        self.get_batched_training_data = async_to_streamed_response_wrapper(
            next_action.get_batched_training_data,
        )
        self.get_training_data = async_to_streamed_response_wrapper(
            next_action.get_training_data,
        )
        self.get_training_datum = async_to_streamed_response_wrapper(
            next_action.get_training_datum,
        )
        self.label_training_datum = async_to_streamed_response_wrapper(
            next_action.label_training_datum,
        )
