# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import sys
import time
from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import job_list_params, job_status_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncJobsList, AsyncJobsList
from .._base_client import AsyncPaginator, make_request_options
from ..types.job_get_response import JobGetResponse
from ..types.job_list_response import JobListResponse
from ..types.job_cancel_response import JobCancelResponse
from ..types.job_status_response import JobStatusResponse
from ..types.job_get_step_response import JobGetStepResponse
from ..types.job_get_steps_response import JobGetStepsResponse
from ..types.job_get_scrapers_response import JobGetScrapersResponse
from ..types.job_get_step_graph_response import JobGetStepGraphResponse
from ..types.job_get_source_entities_response import JobGetSourceEntitiesResponse

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
        dataset: Optional[str] | Omit = omit,
        job_type: Optional[Literal["Web", "Pdf", "Derive", "Scrape"]] | Omit = omit,
        limit: int | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        seeded_kg_search_term: Optional[str] | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncJobsList[JobListResponse]:
        """
        List all the executions

        Args:
          dataset: Dataset name to optionally filter jobs by

          job_type: Type of job to optionally filter jobs by

          node_id: Node ID to optionally filter jobs by

          seeded_kg_search_term: seeded kg search term

          since: List since a specific timestamp

          status: Status to optionally filter jobs by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/jobs/list",
            page=SyncJobsList[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "job_type": job_type,
                        "limit": limit,
                        "node_id": node_id,
                        "offset": offset,
                        "seeded_kg_search_term": seeded_kg_search_term,
                        "since": since,
                        "status": status,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    def delete(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Delete a job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            f"/jobs/delete/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def cancel(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCancelResponse:
        """
        You successfully cancelled a job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._post(
            f"/jobs/cancel/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCancelResponse,
        )

    def get(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetResponse:
        """
        Retrieve a job from structify using a job_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/jobs/get/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetResponse,
        )

    def get_scrapers(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetScrapersResponse:
        """
        Retrieve scrapers associated with a job from structify.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/jobs/get_scrapers/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetScrapersResponse,
        )

    def get_source_entities(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetSourceEntitiesResponse:
        """
        Get all source entities and their associated sources for a specific job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/jobs/get_source_entities/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetSourceEntitiesResponse,
        )

    def get_step(
        self,
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetStepResponse:
        """
        Retrieve a step from structify.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._get(
            f"/jobs/get_step/{step_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetStepResponse,
        )

    def get_step_graph(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetStepGraphResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/jobs/get_step_graph/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetStepGraphResponse,
        )

    def get_steps(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetStepsResponse:
        """
        Retrieve a job from structify.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/jobs/get_steps/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetStepsResponse,
        )

    def schedule(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        One example use case is every single day check the news websites and pull them
        into my dataset.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/jobs/schedule",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def status(
        self,
        *,
        dataset_name: Optional[str] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobStatusResponse:
        """Returns counts of jobs by status (completed, running, failed, queued).

        Exactly
        one of job_ids or dataset_name must be provided. This endpoint can handle large
        numbers of job IDs since it returns aggregated data instead of individual job
        details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/jobs/status_aggregated",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "job_ids": job_ids,
                    "node_id": node_id,
                },
                job_status_params.JobStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobStatusResponse,
        )

    def wait_for_jobs(
        self,
        job_ids: Optional[SequenceNotStr[str]] = None,
        dataset_name: Optional[str] = None,
        stream: bool = False,
        title: Optional[str] = None,
        node_id: Optional[str] = None,
    ) -> None:
        """
        Wait for jobs to complete synchronously.

        Args:
          job_ids: List of job IDs to wait for
          stream: Whether to fail the function if any jobs fail. If False, the function will return a summary of the jobs and their statuses.
        """

        spinner = ["|", "/", "-", "\\"]
        spin_idx = 0
        start_time = time.monotonic()

        while True:
            statuses = self.status(job_ids=job_ids, dataset_name=dataset_name)

            # If we're inside a structify node of a workflow and want to stream progress, show the progress for that node
            display_title = "Waiting for jobs... "
            if title:
                display_title = title + "... "
                if node_id:
                    self._client.sessions.update_node_progress(
                        node_id=node_id,
                        current=statuses.completed + statuses.failed,
                        total=statuses.total,
                        title=title,
                        elapsed_seconds=time.monotonic() - start_time,
                    )
                    display_title = title + f"(node {node_id})... "
                else:
                    display_title = title + "... "

            status_line = (
                f"{spinner[spin_idx % len(spinner)]} "
                f"{display_title} "
                f"Queued: {statuses.queued}  "
                f"Running: {statuses.running}  "
                f"Completed: {statuses.completed}  "
                f"Failed: {statuses.failed}"
            )
            # If we're in a node, we delegate progress bars to our node progress tracker
            if node_id is None:
                sys.stdout.write("\r" + status_line)
                sys.stdout.flush()
            spin_idx += 1

            if statuses.running == 0 and statuses.queued == 0:
                break
            else:
                time.sleep(1)
        # Final status print
        sys.stdout.write("\n")
        sys.stdout.flush()

        if statuses.failed > 0:
            if stream:
                raise Exception(f"{statuses.failed} job(s) failed.")
            else:
                print(f"\nWARNING: {statuses.failed} jobs failed")  # noqa: T201


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
        dataset: Optional[str] | Omit = omit,
        job_type: Optional[Literal["Web", "Pdf", "Derive", "Scrape"]] | Omit = omit,
        limit: int | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        seeded_kg_search_term: Optional[str] | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JobListResponse, AsyncJobsList[JobListResponse]]:
        """
        List all the executions

        Args:
          dataset: Dataset name to optionally filter jobs by

          job_type: Type of job to optionally filter jobs by

          node_id: Node ID to optionally filter jobs by

          seeded_kg_search_term: seeded kg search term

          since: List since a specific timestamp

          status: Status to optionally filter jobs by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/jobs/list",
            page=AsyncJobsList[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "job_type": job_type,
                        "limit": limit,
                        "node_id": node_id,
                        "offset": offset,
                        "seeded_kg_search_term": seeded_kg_search_term,
                        "since": since,
                        "status": status,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    async def delete(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Delete a job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            f"/jobs/delete/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def cancel(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCancelResponse:
        """
        You successfully cancelled a job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._post(
            f"/jobs/cancel/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCancelResponse,
        )

    async def get(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetResponse:
        """
        Retrieve a job from structify using a job_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/jobs/get/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetResponse,
        )

    async def get_scrapers(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetScrapersResponse:
        """
        Retrieve scrapers associated with a job from structify.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/jobs/get_scrapers/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetScrapersResponse,
        )

    async def get_source_entities(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetSourceEntitiesResponse:
        """
        Get all source entities and their associated sources for a specific job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/jobs/get_source_entities/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetSourceEntitiesResponse,
        )

    async def get_step(
        self,
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetStepResponse:
        """
        Retrieve a step from structify.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._get(
            f"/jobs/get_step/{step_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetStepResponse,
        )

    async def get_step_graph(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetStepGraphResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/jobs/get_step_graph/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetStepGraphResponse,
        )

    async def get_steps(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetStepsResponse:
        """
        Retrieve a job from structify.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/jobs/get_steps/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobGetStepsResponse,
        )

    async def schedule(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        One example use case is every single day check the news websites and pull them
        into my dataset.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/jobs/schedule",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def status(
        self,
        *,
        dataset_name: Optional[str] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobStatusResponse:
        """Returns counts of jobs by status (completed, running, failed, queued).

        Exactly
        one of job_ids or dataset_name must be provided. This endpoint can handle large
        numbers of job IDs since it returns aggregated data instead of individual job
        details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/jobs/status_aggregated",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "job_ids": job_ids,
                    "node_id": node_id,
                },
                job_status_params.JobStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobStatusResponse,
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
        self.cancel = to_raw_response_wrapper(
            jobs.cancel,
        )
        self.get = to_raw_response_wrapper(
            jobs.get,
        )
        self.get_scrapers = to_raw_response_wrapper(
            jobs.get_scrapers,
        )
        self.get_source_entities = to_raw_response_wrapper(
            jobs.get_source_entities,
        )
        self.get_step = to_raw_response_wrapper(
            jobs.get_step,
        )
        self.get_step_graph = to_raw_response_wrapper(
            jobs.get_step_graph,
        )
        self.get_steps = to_raw_response_wrapper(
            jobs.get_steps,
        )
        self.schedule = to_raw_response_wrapper(
            jobs.schedule,
        )
        self.status = to_raw_response_wrapper(
            jobs.status,
        )
        self.wait_for_jobs = to_raw_response_wrapper(
            jobs.wait_for_jobs,
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
        self.cancel = async_to_raw_response_wrapper(
            jobs.cancel,
        )
        self.get = async_to_raw_response_wrapper(
            jobs.get,
        )
        self.get_scrapers = async_to_raw_response_wrapper(
            jobs.get_scrapers,
        )
        self.get_source_entities = async_to_raw_response_wrapper(
            jobs.get_source_entities,
        )
        self.get_step = async_to_raw_response_wrapper(
            jobs.get_step,
        )
        self.get_step_graph = async_to_raw_response_wrapper(
            jobs.get_step_graph,
        )
        self.get_steps = async_to_raw_response_wrapper(
            jobs.get_steps,
        )
        self.schedule = async_to_raw_response_wrapper(
            jobs.schedule,
        )
        self.status = async_to_raw_response_wrapper(
            jobs.status,
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
        self.cancel = to_streamed_response_wrapper(
            jobs.cancel,
        )
        self.get = to_streamed_response_wrapper(
            jobs.get,
        )
        self.get_scrapers = to_streamed_response_wrapper(
            jobs.get_scrapers,
        )
        self.get_source_entities = to_streamed_response_wrapper(
            jobs.get_source_entities,
        )
        self.get_step = to_streamed_response_wrapper(
            jobs.get_step,
        )
        self.get_step_graph = to_streamed_response_wrapper(
            jobs.get_step_graph,
        )
        self.get_steps = to_streamed_response_wrapper(
            jobs.get_steps,
        )
        self.schedule = to_streamed_response_wrapper(
            jobs.schedule,
        )
        self.status = to_streamed_response_wrapper(
            jobs.status,
        )
        self.wait_for_jobs = to_streamed_response_wrapper(
            jobs.wait_for_jobs,
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
        self.cancel = async_to_streamed_response_wrapper(
            jobs.cancel,
        )
        self.get = async_to_streamed_response_wrapper(
            jobs.get,
        )
        self.get_scrapers = async_to_streamed_response_wrapper(
            jobs.get_scrapers,
        )
        self.get_source_entities = async_to_streamed_response_wrapper(
            jobs.get_source_entities,
        )
        self.get_step = async_to_streamed_response_wrapper(
            jobs.get_step,
        )
        self.get_step_graph = async_to_streamed_response_wrapper(
            jobs.get_step_graph,
        )
        self.get_steps = async_to_streamed_response_wrapper(
            jobs.get_steps,
        )
        self.schedule = async_to_streamed_response_wrapper(
            jobs.schedule,
        )
        self.status = async_to_streamed_response_wrapper(
            jobs.status,
        )
