# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import match_create_jobs_params, match_list_results_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.match_result import MatchResult
from ..types.create_match_jobs_response import CreateMatchJobsResponse

__all__ = ["MatchResource", "AsyncMatchResource"]


class MatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return MatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return MatchResourceWithStreamingResponse(self)

    def create_jobs(
        self,
        *,
        conditioning: str,
        dataset: str,
        source_table: str,
        target_table: str,
        node_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateMatchJobsResponse:
        """This endpoint creates one job per entity in the source table.

        Each job will
        attempt to find a matching entity in the target table using LLM-based matching.

        Args:
          conditioning: Optional conditioning prompt for the LLM matcher

          dataset: Dataset name

          source_table: Source table name (entities to match from)

          target_table: Target table name (entities to match to)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/match/create_jobs",
            body=maybe_transform(
                {
                    "conditioning": conditioning,
                    "dataset": dataset,
                    "source_table": source_table,
                    "target_table": target_table,
                    "node_id": node_id,
                },
                match_create_jobs_params.MatchCreateJobsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateMatchJobsResponse,
        )

    def list_results(
        self,
        *,
        dataset: str,
        source_table: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncJobsList[MatchResult]:
        """
        Returns paginated match results showing which entities from the source table
        were matched to entities in target tables, along with the reasoning.

        Args:
          dataset: Dataset name

          source_table: Source table name to get matches for

          limit: Number of results to return (default: 1000, max: 1000)

          offset: Offset for pagination (default: 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/match/list_results",
            page=SyncJobsList[MatchResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "source_table": source_table,
                        "limit": limit,
                        "offset": offset,
                    },
                    match_list_results_params.MatchListResultsParams,
                ),
            ),
            model=MatchResult,
        )


class AsyncMatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncMatchResourceWithStreamingResponse(self)

    async def create_jobs(
        self,
        *,
        conditioning: str,
        dataset: str,
        source_table: str,
        target_table: str,
        node_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateMatchJobsResponse:
        """This endpoint creates one job per entity in the source table.

        Each job will
        attempt to find a matching entity in the target table using LLM-based matching.

        Args:
          conditioning: Optional conditioning prompt for the LLM matcher

          dataset: Dataset name

          source_table: Source table name (entities to match from)

          target_table: Target table name (entities to match to)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/match/create_jobs",
            body=await async_maybe_transform(
                {
                    "conditioning": conditioning,
                    "dataset": dataset,
                    "source_table": source_table,
                    "target_table": target_table,
                    "node_id": node_id,
                },
                match_create_jobs_params.MatchCreateJobsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateMatchJobsResponse,
        )

    def list_results(
        self,
        *,
        dataset: str,
        source_table: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MatchResult, AsyncJobsList[MatchResult]]:
        """
        Returns paginated match results showing which entities from the source table
        were matched to entities in target tables, along with the reasoning.

        Args:
          dataset: Dataset name

          source_table: Source table name to get matches for

          limit: Number of results to return (default: 1000, max: 1000)

          offset: Offset for pagination (default: 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/match/list_results",
            page=AsyncJobsList[MatchResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset": dataset,
                        "source_table": source_table,
                        "limit": limit,
                        "offset": offset,
                    },
                    match_list_results_params.MatchListResultsParams,
                ),
            ),
            model=MatchResult,
        )


class MatchResourceWithRawResponse:
    def __init__(self, match: MatchResource) -> None:
        self._match = match

        self.create_jobs = to_raw_response_wrapper(
            match.create_jobs,
        )
        self.list_results = to_raw_response_wrapper(
            match.list_results,
        )


class AsyncMatchResourceWithRawResponse:
    def __init__(self, match: AsyncMatchResource) -> None:
        self._match = match

        self.create_jobs = async_to_raw_response_wrapper(
            match.create_jobs,
        )
        self.list_results = async_to_raw_response_wrapper(
            match.list_results,
        )


class MatchResourceWithStreamingResponse:
    def __init__(self, match: MatchResource) -> None:
        self._match = match

        self.create_jobs = to_streamed_response_wrapper(
            match.create_jobs,
        )
        self.list_results = to_streamed_response_wrapper(
            match.list_results,
        )


class AsyncMatchResourceWithStreamingResponse:
    def __init__(self, match: AsyncMatchResource) -> None:
        self._match = match

        self.create_jobs = async_to_streamed_response_wrapper(
            match.create_jobs,
        )
        self.list_results = async_to_streamed_response_wrapper(
            match.list_results,
        )
