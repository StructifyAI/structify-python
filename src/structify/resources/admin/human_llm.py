# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
    human_llm_get_jobs_params,
    human_llm_finish_job_params,
    human_llm_update_step_params,
    human_llm_get_next_step_params,
    human_llm_add_to_dataset_params,
    human_llm_start_next_job_params,
    human_llm_add_search_for_job_params,
)
from ..._base_client import make_request_options
from ...types.execution_step import ExecutionStep
from ...types.admin.step_choices import StepChoices
from ...types.admin.human_llm_get_jobs_response import HumanLlmGetJobsResponse
from ...types.admin.human_llm_prelabel_step_response import HumanLlmPrelabelStepResponse

__all__ = ["HumanLlmResource", "AsyncHumanLlmResource"]


class HumanLlmResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HumanLlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return HumanLlmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HumanLlmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return HumanLlmResourceWithStreamingResponse(self)

    def add_search_for_job(
        self,
        *,
        job_id: str,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StepChoices:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/human_llm/add_search_for_job",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "job_id": job_id,
                        "url": url,
                    },
                    human_llm_add_search_for_job_params.HumanLlmAddSearchForJobParams,
                ),
            ),
            cast_to=StepChoices,
        )

    def add_to_dataset(
        self,
        *,
        extraction_criteria_met: bool,
        job_id: str,
        step_id: str,
        tool_calls: Iterable[human_llm_add_to_dataset_params.ToolCall],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Adds the given step to the HumanLLM dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/human_llm/add_to_dataset",
            body=maybe_transform(
                {
                    "extraction_criteria_met": extraction_criteria_met,
                    "job_id": job_id,
                    "step_id": step_id,
                    "tool_calls": tool_calls,
                },
                human_llm_add_to_dataset_params.HumanLlmAddToDatasetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def finish_job(
        self,
        *,
        id: str,
        status: Literal["Queued", "Running", "Completed", "Failed"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/human_llm/finish_job",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "status": status,
                    },
                    human_llm_finish_job_params.HumanLlmFinishJobParams,
                ),
            ),
            cast_to=object,
        )

    def get_jobs(
        self,
        *,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HumanLlmGetJobsResponse:
        """
        Start the next human llm job in the queue

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/human_llm/get_jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, human_llm_get_jobs_params.HumanLlmGetJobsParams),
            ),
            cast_to=HumanLlmGetJobsResponse,
        )

    def get_next_step(
        self,
        *,
        job_id: str,
        step_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionStep:
        """
        Given a step id, get the next formatted step to label.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/human_llm/get_next_step",
            body=maybe_transform(
                {
                    "job_id": job_id,
                    "step_id": step_id,
                },
                human_llm_get_next_step_params.HumanLlmGetNextStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionStep,
        )

    def prelabel_step(
        self,
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HumanLlmPrelabelStepResponse:
        """
        Update a step by setting and preparing the given tool calls, then return
        possible next steps with descriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._post(
            f"/admin/human_llm/prelabel_step/{step_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HumanLlmPrelabelStepResponse,
        )

    def start_next_job(
        self,
        *,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StepChoices:
        """
        Start the next human llm job in the queue

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/human_llm/start_next_job",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"job_id": job_id}, human_llm_start_next_job_params.HumanLlmStartNextJobParams),
            ),
            cast_to=StepChoices,
        )

    def update_step(
        self,
        *,
        extraction_criteria_met: bool,
        job_id: str,
        step_id: str,
        tool_calls: Iterable[human_llm_update_step_params.ToolCall],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StepChoices:
        """
        Update a step by setting and preparing the given tool calls, then return
        possible next steps with descriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/human_llm/update_step",
            body=maybe_transform(
                {
                    "extraction_criteria_met": extraction_criteria_met,
                    "job_id": job_id,
                    "step_id": step_id,
                    "tool_calls": tool_calls,
                },
                human_llm_update_step_params.HumanLlmUpdateStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StepChoices,
        )


class AsyncHumanLlmResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHumanLlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHumanLlmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHumanLlmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncHumanLlmResourceWithStreamingResponse(self)

    async def add_search_for_job(
        self,
        *,
        job_id: str,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StepChoices:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/human_llm/add_search_for_job",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "job_id": job_id,
                        "url": url,
                    },
                    human_llm_add_search_for_job_params.HumanLlmAddSearchForJobParams,
                ),
            ),
            cast_to=StepChoices,
        )

    async def add_to_dataset(
        self,
        *,
        extraction_criteria_met: bool,
        job_id: str,
        step_id: str,
        tool_calls: Iterable[human_llm_add_to_dataset_params.ToolCall],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Adds the given step to the HumanLLM dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/human_llm/add_to_dataset",
            body=await async_maybe_transform(
                {
                    "extraction_criteria_met": extraction_criteria_met,
                    "job_id": job_id,
                    "step_id": step_id,
                    "tool_calls": tool_calls,
                },
                human_llm_add_to_dataset_params.HumanLlmAddToDatasetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def finish_job(
        self,
        *,
        id: str,
        status: Literal["Queued", "Running", "Completed", "Failed"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/human_llm/finish_job",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "status": status,
                    },
                    human_llm_finish_job_params.HumanLlmFinishJobParams,
                ),
            ),
            cast_to=object,
        )

    async def get_jobs(
        self,
        *,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HumanLlmGetJobsResponse:
        """
        Start the next human llm job in the queue

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/human_llm/get_jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, human_llm_get_jobs_params.HumanLlmGetJobsParams),
            ),
            cast_to=HumanLlmGetJobsResponse,
        )

    async def get_next_step(
        self,
        *,
        job_id: str,
        step_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionStep:
        """
        Given a step id, get the next formatted step to label.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/human_llm/get_next_step",
            body=await async_maybe_transform(
                {
                    "job_id": job_id,
                    "step_id": step_id,
                },
                human_llm_get_next_step_params.HumanLlmGetNextStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionStep,
        )

    async def prelabel_step(
        self,
        step_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HumanLlmPrelabelStepResponse:
        """
        Update a step by setting and preparing the given tool calls, then return
        possible next steps with descriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._post(
            f"/admin/human_llm/prelabel_step/{step_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HumanLlmPrelabelStepResponse,
        )

    async def start_next_job(
        self,
        *,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StepChoices:
        """
        Start the next human llm job in the queue

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/human_llm/start_next_job",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"job_id": job_id}, human_llm_start_next_job_params.HumanLlmStartNextJobParams
                ),
            ),
            cast_to=StepChoices,
        )

    async def update_step(
        self,
        *,
        extraction_criteria_met: bool,
        job_id: str,
        step_id: str,
        tool_calls: Iterable[human_llm_update_step_params.ToolCall],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StepChoices:
        """
        Update a step by setting and preparing the given tool calls, then return
        possible next steps with descriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/human_llm/update_step",
            body=await async_maybe_transform(
                {
                    "extraction_criteria_met": extraction_criteria_met,
                    "job_id": job_id,
                    "step_id": step_id,
                    "tool_calls": tool_calls,
                },
                human_llm_update_step_params.HumanLlmUpdateStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StepChoices,
        )


class HumanLlmResourceWithRawResponse:
    def __init__(self, human_llm: HumanLlmResource) -> None:
        self._human_llm = human_llm

        self.add_search_for_job = to_raw_response_wrapper(
            human_llm.add_search_for_job,
        )
        self.add_to_dataset = to_raw_response_wrapper(
            human_llm.add_to_dataset,
        )
        self.finish_job = to_raw_response_wrapper(
            human_llm.finish_job,
        )
        self.get_jobs = to_raw_response_wrapper(
            human_llm.get_jobs,
        )
        self.get_next_step = to_raw_response_wrapper(
            human_llm.get_next_step,
        )
        self.prelabel_step = to_raw_response_wrapper(
            human_llm.prelabel_step,
        )
        self.start_next_job = to_raw_response_wrapper(
            human_llm.start_next_job,
        )
        self.update_step = to_raw_response_wrapper(
            human_llm.update_step,
        )


class AsyncHumanLlmResourceWithRawResponse:
    def __init__(self, human_llm: AsyncHumanLlmResource) -> None:
        self._human_llm = human_llm

        self.add_search_for_job = async_to_raw_response_wrapper(
            human_llm.add_search_for_job,
        )
        self.add_to_dataset = async_to_raw_response_wrapper(
            human_llm.add_to_dataset,
        )
        self.finish_job = async_to_raw_response_wrapper(
            human_llm.finish_job,
        )
        self.get_jobs = async_to_raw_response_wrapper(
            human_llm.get_jobs,
        )
        self.get_next_step = async_to_raw_response_wrapper(
            human_llm.get_next_step,
        )
        self.prelabel_step = async_to_raw_response_wrapper(
            human_llm.prelabel_step,
        )
        self.start_next_job = async_to_raw_response_wrapper(
            human_llm.start_next_job,
        )
        self.update_step = async_to_raw_response_wrapper(
            human_llm.update_step,
        )


class HumanLlmResourceWithStreamingResponse:
    def __init__(self, human_llm: HumanLlmResource) -> None:
        self._human_llm = human_llm

        self.add_search_for_job = to_streamed_response_wrapper(
            human_llm.add_search_for_job,
        )
        self.add_to_dataset = to_streamed_response_wrapper(
            human_llm.add_to_dataset,
        )
        self.finish_job = to_streamed_response_wrapper(
            human_llm.finish_job,
        )
        self.get_jobs = to_streamed_response_wrapper(
            human_llm.get_jobs,
        )
        self.get_next_step = to_streamed_response_wrapper(
            human_llm.get_next_step,
        )
        self.prelabel_step = to_streamed_response_wrapper(
            human_llm.prelabel_step,
        )
        self.start_next_job = to_streamed_response_wrapper(
            human_llm.start_next_job,
        )
        self.update_step = to_streamed_response_wrapper(
            human_llm.update_step,
        )


class AsyncHumanLlmResourceWithStreamingResponse:
    def __init__(self, human_llm: AsyncHumanLlmResource) -> None:
        self._human_llm = human_llm

        self.add_search_for_job = async_to_streamed_response_wrapper(
            human_llm.add_search_for_job,
        )
        self.add_to_dataset = async_to_streamed_response_wrapper(
            human_llm.add_to_dataset,
        )
        self.finish_job = async_to_streamed_response_wrapper(
            human_llm.finish_job,
        )
        self.get_jobs = async_to_streamed_response_wrapper(
            human_llm.get_jobs,
        )
        self.get_next_step = async_to_streamed_response_wrapper(
            human_llm.get_next_step,
        )
        self.prelabel_step = async_to_streamed_response_wrapper(
            human_llm.prelabel_step,
        )
        self.start_next_job = async_to_streamed_response_wrapper(
            human_llm.start_next_job,
        )
        self.update_step = async_to_streamed_response_wrapper(
            human_llm.update_step,
        )
