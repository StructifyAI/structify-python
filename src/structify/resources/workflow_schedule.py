# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    workflow_schedule_create_params,
    workflow_schedule_update_params,
    workflow_schedule_get_sessions_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.workflow_schedule_info import WorkflowScheduleInfo
from ..types.workflow_schedule_get_response import WorkflowScheduleGetResponse
from ..types.workflow_schedule_get_all_response import WorkflowScheduleGetAllResponse
from ..types.get_workflow_schedule_sessions_response import GetWorkflowScheduleSessionsResponse

__all__ = ["WorkflowScheduleResource", "AsyncWorkflowScheduleResource"]


class WorkflowScheduleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkflowScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return WorkflowScheduleResourceWithStreamingResponse(self)

    def create(
        self,
        chat_session_id: str,
        *,
        git_commit_hash: str,
        name: str,
        cron_schedule: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowScheduleInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_session_id:
            raise ValueError(f"Expected a non-empty value for `chat_session_id` but received {chat_session_id!r}")
        return self._post(
            f"/workflow-schedule/{chat_session_id}",
            body=maybe_transform(
                {
                    "git_commit_hash": git_commit_hash,
                    "name": name,
                    "cron_schedule": cron_schedule,
                },
                workflow_schedule_create_params.WorkflowScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowScheduleInfo,
        )

    def update(
        self,
        schedule_id: str,
        *,
        cron_schedule: Optional[str] | Omit = omit,
        git_commit_hash: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowScheduleInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._put(
            f"/workflow-schedule/{schedule_id}",
            body=maybe_transform(
                {
                    "cron_schedule": cron_schedule,
                    "git_commit_hash": git_commit_hash,
                    "name": name,
                },
                workflow_schedule_update_params.WorkflowScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowScheduleInfo,
        )

    def delete(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/workflow-schedule/{schedule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        chat_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowScheduleGetResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_session_id:
            raise ValueError(f"Expected a non-empty value for `chat_session_id` but received {chat_session_id!r}")
        return self._get(
            f"/workflow-schedule/{chat_session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowScheduleGetResponse,
        )

    def get_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowScheduleGetAllResponse:
        return self._get(
            "/workflow-schedule",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowScheduleGetAllResponse,
        )

    def get_sessions(
        self,
        schedule_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetWorkflowScheduleSessionsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._post(
            f"/workflow-schedule/{schedule_id}/sessions",
            body=maybe_transform(
                {
                    "limit": limit,
                    "offset": offset,
                },
                workflow_schedule_get_sessions_params.WorkflowScheduleGetSessionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetWorkflowScheduleSessionsResponse,
        )


class AsyncWorkflowScheduleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkflowScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncWorkflowScheduleResourceWithStreamingResponse(self)

    async def create(
        self,
        chat_session_id: str,
        *,
        git_commit_hash: str,
        name: str,
        cron_schedule: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowScheduleInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_session_id:
            raise ValueError(f"Expected a non-empty value for `chat_session_id` but received {chat_session_id!r}")
        return await self._post(
            f"/workflow-schedule/{chat_session_id}",
            body=await async_maybe_transform(
                {
                    "git_commit_hash": git_commit_hash,
                    "name": name,
                    "cron_schedule": cron_schedule,
                },
                workflow_schedule_create_params.WorkflowScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowScheduleInfo,
        )

    async def update(
        self,
        schedule_id: str,
        *,
        cron_schedule: Optional[str] | Omit = omit,
        git_commit_hash: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowScheduleInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._put(
            f"/workflow-schedule/{schedule_id}",
            body=await async_maybe_transform(
                {
                    "cron_schedule": cron_schedule,
                    "git_commit_hash": git_commit_hash,
                    "name": name,
                },
                workflow_schedule_update_params.WorkflowScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowScheduleInfo,
        )

    async def delete(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/workflow-schedule/{schedule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        chat_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowScheduleGetResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_session_id:
            raise ValueError(f"Expected a non-empty value for `chat_session_id` but received {chat_session_id!r}")
        return await self._get(
            f"/workflow-schedule/{chat_session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowScheduleGetResponse,
        )

    async def get_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowScheduleGetAllResponse:
        return await self._get(
            "/workflow-schedule",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowScheduleGetAllResponse,
        )

    async def get_sessions(
        self,
        schedule_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetWorkflowScheduleSessionsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._post(
            f"/workflow-schedule/{schedule_id}/sessions",
            body=await async_maybe_transform(
                {
                    "limit": limit,
                    "offset": offset,
                },
                workflow_schedule_get_sessions_params.WorkflowScheduleGetSessionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetWorkflowScheduleSessionsResponse,
        )


class WorkflowScheduleResourceWithRawResponse:
    def __init__(self, workflow_schedule: WorkflowScheduleResource) -> None:
        self._workflow_schedule = workflow_schedule

        self.create = to_raw_response_wrapper(
            workflow_schedule.create,
        )
        self.update = to_raw_response_wrapper(
            workflow_schedule.update,
        )
        self.delete = to_raw_response_wrapper(
            workflow_schedule.delete,
        )
        self.get = to_raw_response_wrapper(
            workflow_schedule.get,
        )
        self.get_all = to_raw_response_wrapper(
            workflow_schedule.get_all,
        )
        self.get_sessions = to_raw_response_wrapper(
            workflow_schedule.get_sessions,
        )


class AsyncWorkflowScheduleResourceWithRawResponse:
    def __init__(self, workflow_schedule: AsyncWorkflowScheduleResource) -> None:
        self._workflow_schedule = workflow_schedule

        self.create = async_to_raw_response_wrapper(
            workflow_schedule.create,
        )
        self.update = async_to_raw_response_wrapper(
            workflow_schedule.update,
        )
        self.delete = async_to_raw_response_wrapper(
            workflow_schedule.delete,
        )
        self.get = async_to_raw_response_wrapper(
            workflow_schedule.get,
        )
        self.get_all = async_to_raw_response_wrapper(
            workflow_schedule.get_all,
        )
        self.get_sessions = async_to_raw_response_wrapper(
            workflow_schedule.get_sessions,
        )


class WorkflowScheduleResourceWithStreamingResponse:
    def __init__(self, workflow_schedule: WorkflowScheduleResource) -> None:
        self._workflow_schedule = workflow_schedule

        self.create = to_streamed_response_wrapper(
            workflow_schedule.create,
        )
        self.update = to_streamed_response_wrapper(
            workflow_schedule.update,
        )
        self.delete = to_streamed_response_wrapper(
            workflow_schedule.delete,
        )
        self.get = to_streamed_response_wrapper(
            workflow_schedule.get,
        )
        self.get_all = to_streamed_response_wrapper(
            workflow_schedule.get_all,
        )
        self.get_sessions = to_streamed_response_wrapper(
            workflow_schedule.get_sessions,
        )


class AsyncWorkflowScheduleResourceWithStreamingResponse:
    def __init__(self, workflow_schedule: AsyncWorkflowScheduleResource) -> None:
        self._workflow_schedule = workflow_schedule

        self.create = async_to_streamed_response_wrapper(
            workflow_schedule.create,
        )
        self.update = async_to_streamed_response_wrapper(
            workflow_schedule.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            workflow_schedule.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            workflow_schedule.get,
        )
        self.get_all = async_to_streamed_response_wrapper(
            workflow_schedule.get_all,
        )
        self.get_sessions = async_to_streamed_response_wrapper(
            workflow_schedule.get_sessions,
        )
