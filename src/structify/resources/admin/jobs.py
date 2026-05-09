# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncJobsList, AsyncJobsList
from ...types.admin import job_list_params, job_delete_params, job_kill_by_user_params, job_update_concurrency_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.admin.job_list_response import JobListResponse
from ...types.admin.job_concurrency_response import JobConcurrencyResponse
from ...types.admin.job_kill_by_user_response import JobKillByUserResponse
from ...types.admin.admin_delete_jobs_response import AdminDeleteJobsResponse
from ...types.admin.job_running_stats_response import JobRunningStatsResponse
from ...types.admin.job_update_concurrency_response import JobUpdateConcurrencyResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    """Admin endpoints"""

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
        job_type: Optional[Literal["Web", "Pdf", "Derive", "Scrape", "Match", "ConnectorExplore", "DatahubIngestion"]]
        | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncJobsList[JobListResponse]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/admin/jobs/list",
            page=SyncJobsList[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "job_type": job_type,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                        "user_id": user_id,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    def delete(
        self,
        *,
        job_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminDeleteJobsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/jobs/delete",
            body=maybe_transform({"job_ids": job_ids}, job_delete_params.JobDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminDeleteJobsResponse,
        )

    def concurrency(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobConcurrencyResponse:
        return self._get(
            "/admin/jobs/concurrency_limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobConcurrencyResponse,
        )

    def kill_by_user(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobKillByUserResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/jobs/kill_by_user",
            body=maybe_transform({"user_id": user_id}, job_kill_by_user_params.JobKillByUserParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobKillByUserResponse,
        )

    def running_stats(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobRunningStatsResponse:
        return self._get(
            "/admin/jobs/running_stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobRunningStatsResponse,
        )

    def update_concurrency(
        self,
        *,
        max_connector_explore_jobs: Optional[int] | Omit = omit,
        max_derive_jobs: Optional[int] | Omit = omit,
        max_match_jobs: Optional[int] | Omit = omit,
        max_pdf_jobs: Optional[int] | Omit = omit,
        max_scrape_jobs: Optional[int] | Omit = omit,
        max_total_jobs: Optional[int] | Omit = omit,
        max_web_jobs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobUpdateConcurrencyResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/admin/jobs/concurrency_limits",
            body=maybe_transform(
                {
                    "max_connector_explore_jobs": max_connector_explore_jobs,
                    "max_derive_jobs": max_derive_jobs,
                    "max_match_jobs": max_match_jobs,
                    "max_pdf_jobs": max_pdf_jobs,
                    "max_scrape_jobs": max_scrape_jobs,
                    "max_total_jobs": max_total_jobs,
                    "max_web_jobs": max_web_jobs,
                },
                job_update_concurrency_params.JobUpdateConcurrencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobUpdateConcurrencyResponse,
        )


class AsyncJobsResource(AsyncAPIResource):
    """Admin endpoints"""

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
        job_type: Optional[Literal["Web", "Pdf", "Derive", "Scrape", "Match", "ConnectorExplore", "DatahubIngestion"]]
        | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JobListResponse, AsyncJobsList[JobListResponse]]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/admin/jobs/list",
            page=AsyncJobsList[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "job_type": job_type,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                        "user_id": user_id,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    async def delete(
        self,
        *,
        job_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminDeleteJobsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/jobs/delete",
            body=await async_maybe_transform({"job_ids": job_ids}, job_delete_params.JobDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminDeleteJobsResponse,
        )

    async def concurrency(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobConcurrencyResponse:
        return await self._get(
            "/admin/jobs/concurrency_limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobConcurrencyResponse,
        )

    async def kill_by_user(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobKillByUserResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/jobs/kill_by_user",
            body=await async_maybe_transform({"user_id": user_id}, job_kill_by_user_params.JobKillByUserParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobKillByUserResponse,
        )

    async def running_stats(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobRunningStatsResponse:
        return await self._get(
            "/admin/jobs/running_stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobRunningStatsResponse,
        )

    async def update_concurrency(
        self,
        *,
        max_connector_explore_jobs: Optional[int] | Omit = omit,
        max_derive_jobs: Optional[int] | Omit = omit,
        max_match_jobs: Optional[int] | Omit = omit,
        max_pdf_jobs: Optional[int] | Omit = omit,
        max_scrape_jobs: Optional[int] | Omit = omit,
        max_total_jobs: Optional[int] | Omit = omit,
        max_web_jobs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobUpdateConcurrencyResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/admin/jobs/concurrency_limits",
            body=await async_maybe_transform(
                {
                    "max_connector_explore_jobs": max_connector_explore_jobs,
                    "max_derive_jobs": max_derive_jobs,
                    "max_match_jobs": max_match_jobs,
                    "max_pdf_jobs": max_pdf_jobs,
                    "max_scrape_jobs": max_scrape_jobs,
                    "max_total_jobs": max_total_jobs,
                    "max_web_jobs": max_web_jobs,
                },
                job_update_concurrency_params.JobUpdateConcurrencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobUpdateConcurrencyResponse,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.delete = to_raw_response_wrapper(
            jobs.delete,
        )
        self.concurrency = to_raw_response_wrapper(
            jobs.concurrency,
        )
        self.kill_by_user = to_raw_response_wrapper(
            jobs.kill_by_user,
        )
        self.running_stats = to_raw_response_wrapper(
            jobs.running_stats,
        )
        self.update_concurrency = to_raw_response_wrapper(
            jobs.update_concurrency,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            jobs.delete,
        )
        self.concurrency = async_to_raw_response_wrapper(
            jobs.concurrency,
        )
        self.kill_by_user = async_to_raw_response_wrapper(
            jobs.kill_by_user,
        )
        self.running_stats = async_to_raw_response_wrapper(
            jobs.running_stats,
        )
        self.update_concurrency = async_to_raw_response_wrapper(
            jobs.update_concurrency,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.delete = to_streamed_response_wrapper(
            jobs.delete,
        )
        self.concurrency = to_streamed_response_wrapper(
            jobs.concurrency,
        )
        self.kill_by_user = to_streamed_response_wrapper(
            jobs.kill_by_user,
        )
        self.running_stats = to_streamed_response_wrapper(
            jobs.running_stats,
        )
        self.update_concurrency = to_streamed_response_wrapper(
            jobs.update_concurrency,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            jobs.delete,
        )
        self.concurrency = async_to_streamed_response_wrapper(
            jobs.concurrency,
        )
        self.kill_by_user = async_to_streamed_response_wrapper(
            jobs.kill_by_user,
        )
        self.running_stats = async_to_streamed_response_wrapper(
            jobs.running_stats,
        )
        self.update_concurrency = async_to_streamed_response_wrapper(
            jobs.update_concurrency,
        )
