# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncJobsList, AsyncJobsList
from ...types.admin import job_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.admin.admin_list_jobs_response import AdminListJobsResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter_test_users: bool,
        limit: int,
        offset: int,
        dataset_id: Optional[str] | Omit = omit,
        seeded_kg_search_term: Optional[str] | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncJobsList[AdminListJobsResponse]:
        """
        This endpoint allows admins to list jobs from all users without user ownership
        restrictions. Optionally filter out test users (users with functional_test
        feature flag or debug permission).

        Args:
          filter_test_users: Filter out jobs from test users (users with functional_test feature flag or
              debug permission)

          limit: Number of results to return

          offset: Pagination offset

          dataset_id: Dataset ID to optionally filter jobs by

          seeded_kg_search_term: Seeded kg search term

          since: List since a specific timestamp

          status: Status to optionally filter jobs by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/admin/jobs/list",
            page=SyncJobsList[AdminListJobsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_test_users": filter_test_users,
                        "limit": limit,
                        "offset": offset,
                        "dataset_id": dataset_id,
                        "seeded_kg_search_term": seeded_kg_search_term,
                        "since": since,
                        "status": status,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=AdminListJobsResponse,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter_test_users: bool,
        limit: int,
        offset: int,
        dataset_id: Optional[str] | Omit = omit,
        seeded_kg_search_term: Optional[str] | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AdminListJobsResponse, AsyncJobsList[AdminListJobsResponse]]:
        """
        This endpoint allows admins to list jobs from all users without user ownership
        restrictions. Optionally filter out test users (users with functional_test
        feature flag or debug permission).

        Args:
          filter_test_users: Filter out jobs from test users (users with functional_test feature flag or
              debug permission)

          limit: Number of results to return

          offset: Pagination offset

          dataset_id: Dataset ID to optionally filter jobs by

          seeded_kg_search_term: Seeded kg search term

          since: List since a specific timestamp

          status: Status to optionally filter jobs by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/admin/jobs/list",
            page=AsyncJobsList[AdminListJobsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_test_users": filter_test_users,
                        "limit": limit,
                        "offset": offset,
                        "dataset_id": dataset_id,
                        "seeded_kg_search_term": seeded_kg_search_term,
                        "since": since,
                        "status": status,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=AdminListJobsResponse,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.list = to_raw_response_wrapper(
            jobs.list,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.list = to_streamed_response_wrapper(
            jobs.list,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
