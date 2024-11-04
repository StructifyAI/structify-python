# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.admin import human_llm_update_step_params
from ..._base_client import make_request_options
from ...types.execution_step import ExecutionStep
from ...types.admin.human_llm_update_step_response import HumanLlmUpdateStepResponse

__all__ = ["HumanLlmResource", "AsyncHumanLlmResource"]


class HumanLlmResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HumanLlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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

    def get_next_step(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionStep:
        """Given a step id, get the next formatted step to label."""
        return self._get(
            "/admin/human_llm/get_next_step",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionStep,
        )

    def update_step(
        self,
        *,
        job_id: str,
        step_id: str,
        tool_calls: Iterable[human_llm_update_step_params.ToolCall],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HumanLlmUpdateStepResponse:
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
                    "job_id": job_id,
                    "step_id": step_id,
                    "tool_calls": tool_calls,
                },
                human_llm_update_step_params.HumanLlmUpdateStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HumanLlmUpdateStepResponse,
        )


class AsyncHumanLlmResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHumanLlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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

    async def get_next_step(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionStep:
        """Given a step id, get the next formatted step to label."""
        return await self._get(
            "/admin/human_llm/get_next_step",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionStep,
        )

    async def update_step(
        self,
        *,
        job_id: str,
        step_id: str,
        tool_calls: Iterable[human_llm_update_step_params.ToolCall],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HumanLlmUpdateStepResponse:
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
                    "job_id": job_id,
                    "step_id": step_id,
                    "tool_calls": tool_calls,
                },
                human_llm_update_step_params.HumanLlmUpdateStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HumanLlmUpdateStepResponse,
        )


class HumanLlmResourceWithRawResponse:
    def __init__(self, human_llm: HumanLlmResource) -> None:
        self._human_llm = human_llm

        self.get_next_step = to_raw_response_wrapper(
            human_llm.get_next_step,
        )
        self.update_step = to_raw_response_wrapper(
            human_llm.update_step,
        )


class AsyncHumanLlmResourceWithRawResponse:
    def __init__(self, human_llm: AsyncHumanLlmResource) -> None:
        self._human_llm = human_llm

        self.get_next_step = async_to_raw_response_wrapper(
            human_llm.get_next_step,
        )
        self.update_step = async_to_raw_response_wrapper(
            human_llm.update_step,
        )


class HumanLlmResourceWithStreamingResponse:
    def __init__(self, human_llm: HumanLlmResource) -> None:
        self._human_llm = human_llm

        self.get_next_step = to_streamed_response_wrapper(
            human_llm.get_next_step,
        )
        self.update_step = to_streamed_response_wrapper(
            human_llm.update_step,
        )


class AsyncHumanLlmResourceWithStreamingResponse:
    def __init__(self, human_llm: AsyncHumanLlmResource) -> None:
        self._human_llm = human_llm

        self.get_next_step = async_to_streamed_response_wrapper(
            human_llm.get_next_step,
        )
        self.update_step = async_to_streamed_response_wrapper(
            human_llm.update_step,
        )
