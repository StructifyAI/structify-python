# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    dataset_create_params,
    dataset_delete_params,
    dataset_view_entries_params,
    dataset_retrieve_info_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
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
from ..types.dataset_descriptor import DatasetDescriptor
from ..types.dataset_list_response import DatasetListResponse
from ..types.dataset_view_entries_response import DatasetViewEntriesResponse

__all__ = ["DatasetResource", "AsyncDatasetResource"]


class DatasetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetResourceWithRawResponse:
        return DatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetResourceWithStreamingResponse:
        return DatasetResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        name: str,
        tables: Iterable[dataset_create_params.Table],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create a Dataset

        Creates a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/dataset/create",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "tables": tables,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListResponse:
        """
        List datasets

        Gets all datasets owned by the current user
        """
        return self._get(
            "/dataset/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListResponse,
        )

    def delete(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Permanently delete a dataset and all its contents

        Args:
          name: The name of the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/dataset/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, dataset_delete_params.DatasetDeleteParams),
            ),
            cast_to=NoneType,
        )

    def retrieve_info(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DatasetDescriptor]:
        """
        Grab a dataset by its name.

        Args:
          name: Information about the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dataset/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, dataset_retrieve_info_params.DatasetRetrieveInfoParams),
            ),
            cast_to=DatasetDescriptor,
        )

    def view_entries(
        self,
        *,
        dataset_name: str,
        table_name: str,
        limit: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetViewEntriesResponse:
        """
        View entries from a table in a dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dataset/view",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_name": dataset_name,
                        "table_name": table_name,
                        "limit": limit,
                        "skip": skip,
                    },
                    dataset_view_entries_params.DatasetViewEntriesParams,
                ),
            ),
            cast_to=DatasetViewEntriesResponse,
        )


class AsyncDatasetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetResourceWithRawResponse:
        return AsyncDatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetResourceWithStreamingResponse:
        return AsyncDatasetResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        name: str,
        tables: Iterable[dataset_create_params.Table],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create a Dataset

        Creates a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/dataset/create",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "tables": tables,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListResponse:
        """
        List datasets

        Gets all datasets owned by the current user
        """
        return await self._get(
            "/dataset/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListResponse,
        )

    async def delete(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Permanently delete a dataset and all its contents

        Args:
          name: The name of the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/dataset/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"name": name}, dataset_delete_params.DatasetDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def retrieve_info(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DatasetDescriptor]:
        """
        Grab a dataset by its name.

        Args:
          name: Information about the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dataset/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"name": name}, dataset_retrieve_info_params.DatasetRetrieveInfoParams
                ),
            ),
            cast_to=DatasetDescriptor,
        )

    async def view_entries(
        self,
        *,
        dataset_name: str,
        table_name: str,
        limit: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetViewEntriesResponse:
        """
        View entries from a table in a dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dataset/view",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset_name": dataset_name,
                        "table_name": table_name,
                        "limit": limit,
                        "skip": skip,
                    },
                    dataset_view_entries_params.DatasetViewEntriesParams,
                ),
            ),
            cast_to=DatasetViewEntriesResponse,
        )


class DatasetResourceWithRawResponse:
    def __init__(self, dataset: DatasetResource) -> None:
        self._dataset = dataset

        self.create = to_raw_response_wrapper(
            dataset.create,
        )
        self.list = to_raw_response_wrapper(
            dataset.list,
        )
        self.delete = to_raw_response_wrapper(
            dataset.delete,
        )
        self.retrieve_info = to_raw_response_wrapper(
            dataset.retrieve_info,
        )
        self.view_entries = to_raw_response_wrapper(
            dataset.view_entries,
        )


class AsyncDatasetResourceWithRawResponse:
    def __init__(self, dataset: AsyncDatasetResource) -> None:
        self._dataset = dataset

        self.create = async_to_raw_response_wrapper(
            dataset.create,
        )
        self.list = async_to_raw_response_wrapper(
            dataset.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dataset.delete,
        )
        self.retrieve_info = async_to_raw_response_wrapper(
            dataset.retrieve_info,
        )
        self.view_entries = async_to_raw_response_wrapper(
            dataset.view_entries,
        )


class DatasetResourceWithStreamingResponse:
    def __init__(self, dataset: DatasetResource) -> None:
        self._dataset = dataset

        self.create = to_streamed_response_wrapper(
            dataset.create,
        )
        self.list = to_streamed_response_wrapper(
            dataset.list,
        )
        self.delete = to_streamed_response_wrapper(
            dataset.delete,
        )
        self.retrieve_info = to_streamed_response_wrapper(
            dataset.retrieve_info,
        )
        self.view_entries = to_streamed_response_wrapper(
            dataset.view_entries,
        )


class AsyncDatasetResourceWithStreamingResponse:
    def __init__(self, dataset: AsyncDatasetResource) -> None:
        self._dataset = dataset

        self.create = async_to_streamed_response_wrapper(
            dataset.create,
        )
        self.list = async_to_streamed_response_wrapper(
            dataset.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dataset.delete,
        )
        self.retrieve_info = async_to_streamed_response_wrapper(
            dataset.retrieve_info,
        )
        self.view_entries = async_to_streamed_response_wrapper(
            dataset.view_entries,
        )
