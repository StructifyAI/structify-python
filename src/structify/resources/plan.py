# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import plan_pause_params, plan_create_params, plan_resume_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .._base_client import make_request_options
from ..types.plan_param import PlanParam
from ..types.plan_list_response import PlanListResponse
from ..types.plan_pause_response import PlanPauseResponse
from ..types.plan_resume_response import PlanResumeResponse

__all__ = ["PlanResource", "AsyncPlanResource"]


class PlanResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return PlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return PlanResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        dataset: str,
        plan: PlanParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Create a plan to run consecutive jobs as each step finishes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            "/plan/create",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "plan": plan,
                },
                plan_create_params.PlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
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
    ) -> PlanListResponse:
        """List all plans for your user account in the database."""
        return self._get(
            "/plan/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanListResponse,
        )

    def pause(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlanPauseResponse:
        """
        Pause all running plans for your user account in the database.

        Args:
          dataset_name: Name of the dataset to pause plans for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/plan/pause",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset_name": dataset_name}, plan_pause_params.PlanPauseParams),
            ),
            cast_to=PlanPauseResponse,
        )

    def resume(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlanResumeResponse:
        """
        Resume all paused plans for your user account in the database.

        Args:
          dataset_name: Name of the dataset to resume plans for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/plan/resume",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset_name": dataset_name}, plan_resume_params.PlanResumeParams),
            ),
            cast_to=PlanResumeResponse,
        )


class AsyncPlanResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncPlanResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        dataset: str,
        plan: PlanParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Create a plan to run consecutive jobs as each step finishes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            "/plan/create",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "plan": plan,
                },
                plan_create_params.PlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
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
    ) -> PlanListResponse:
        """List all plans for your user account in the database."""
        return await self._get(
            "/plan/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanListResponse,
        )

    async def pause(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlanPauseResponse:
        """
        Pause all running plans for your user account in the database.

        Args:
          dataset_name: Name of the dataset to pause plans for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/plan/pause",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dataset_name": dataset_name}, plan_pause_params.PlanPauseParams),
            ),
            cast_to=PlanPauseResponse,
        )

    async def resume(
        self,
        *,
        dataset_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlanResumeResponse:
        """
        Resume all paused plans for your user account in the database.

        Args:
          dataset_name: Name of the dataset to resume plans for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/plan/resume",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dataset_name": dataset_name}, plan_resume_params.PlanResumeParams),
            ),
            cast_to=PlanResumeResponse,
        )


class PlanResourceWithRawResponse:
    def __init__(self, plan: PlanResource) -> None:
        self._plan = plan

        self.create = to_raw_response_wrapper(
            plan.create,
        )
        self.list = to_raw_response_wrapper(
            plan.list,
        )
        self.pause = to_raw_response_wrapper(
            plan.pause,
        )
        self.resume = to_raw_response_wrapper(
            plan.resume,
        )


class AsyncPlanResourceWithRawResponse:
    def __init__(self, plan: AsyncPlanResource) -> None:
        self._plan = plan

        self.create = async_to_raw_response_wrapper(
            plan.create,
        )
        self.list = async_to_raw_response_wrapper(
            plan.list,
        )
        self.pause = async_to_raw_response_wrapper(
            plan.pause,
        )
        self.resume = async_to_raw_response_wrapper(
            plan.resume,
        )


class PlanResourceWithStreamingResponse:
    def __init__(self, plan: PlanResource) -> None:
        self._plan = plan

        self.create = to_streamed_response_wrapper(
            plan.create,
        )
        self.list = to_streamed_response_wrapper(
            plan.list,
        )
        self.pause = to_streamed_response_wrapper(
            plan.pause,
        )
        self.resume = to_streamed_response_wrapper(
            plan.resume,
        )


class AsyncPlanResourceWithStreamingResponse:
    def __init__(self, plan: AsyncPlanResource) -> None:
        self._plan = plan

        self.create = async_to_streamed_response_wrapper(
            plan.create,
        )
        self.list = async_to_streamed_response_wrapper(
            plan.list,
        )
        self.pause = async_to_streamed_response_wrapper(
            plan.pause,
        )
        self.resume = async_to_streamed_response_wrapper(
            plan.resume,
        )
