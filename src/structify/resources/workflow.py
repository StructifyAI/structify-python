# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    ID,
    workflow_get_params,
    workflow_jobs_params,
    workflow_list_params,
    workflow_create_params,
    workflow_delete_params,
    workflow_update_params,
    workflow_trigger_params,
    workflow_job_progress_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from ..types.id import ID
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.workflow_param import WorkflowParam
from ..types.existing_workflow import ExistingWorkflow
from ..types.workflow_jobs_response import WorkflowJobsResponse
from ..types.workflow_list_response import WorkflowListResponse
from ..types.workflow_job_progress_response import WorkflowJobProgressResponse

__all__ = ["WorkflowResource", "AsyncWorkflowResource"]


class WorkflowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return WorkflowResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        dataset_name: str,
        workflow: WorkflowParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Create a new workflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/workflow/create",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "workflow": workflow,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def update(
        self,
        *,
        dataset_name: str,
        workflow: WorkflowParam,
        workflow_id: ID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Update an existing workflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/workflow/update",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "workflow": workflow,
                    "workflow_id": workflow_id,
                },
                workflow_update_params.WorkflowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def list(
        self,
        *,
        dataset_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowListResponse:
        """
        list a new workflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/workflow/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset_name": dataset_name}, workflow_list_params.WorkflowListParams),
            ),
            cast_to=WorkflowListResponse,
        )

    def delete(
        self,
        *,
        workflow_id: ID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing workflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/workflow/delete",
            body=maybe_transform({"workflow_id": workflow_id}, workflow_delete_params.WorkflowDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        *,
        workflow_id: ID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExistingWorkflow:
        """
        Get a workflow by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/workflow/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workflow_id": workflow_id}, workflow_get_params.WorkflowGetParams),
            ),
            cast_to=ExistingWorkflow,
        )

    def job_progress(
        self,
        *,
        workflow_id: ID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowJobProgressResponse:
        """
        Get the job status breakdown of a workflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/workflow/job_progress",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"workflow_id": workflow_id}, workflow_job_progress_params.WorkflowJobProgressParams
                ),
            ),
            cast_to=WorkflowJobProgressResponse,
        )

    def jobs(
        self,
        *,
        workflow_id: ID,
        group_id: Optional[str] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | NotGiven = NOT_GIVEN,
        step_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowJobsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/workflow/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "workflow_id": workflow_id,
                        "group_id": group_id,
                        "status": status,
                        "step_id": step_id,
                    },
                    workflow_jobs_params.WorkflowJobsParams,
                ),
            ),
            cast_to=WorkflowJobsResponse,
        )

    def trigger(
        self,
        *,
        entity_ids: List[str],
        workflow_id: ID,
        banned_domains: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stop_config: Optional[workflow_trigger_params.StopConfig] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Trigger a workflow on a set of entities

        Args:
          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/workflow/trigger",
            body=maybe_transform(
                {
                    "entity_ids": entity_ids,
                    "workflow_id": workflow_id,
                    "banned_domains": banned_domains,
                    "stop_config": stop_config,
                },
                workflow_trigger_params.WorkflowTriggerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncWorkflowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncWorkflowResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        dataset_name: str,
        workflow: WorkflowParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Create a new workflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/workflow/create",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "workflow": workflow,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def update(
        self,
        *,
        dataset_name: str,
        workflow: WorkflowParam,
        workflow_id: ID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Update an existing workflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/workflow/update",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "workflow": workflow,
                    "workflow_id": workflow_id,
                },
                workflow_update_params.WorkflowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def list(
        self,
        *,
        dataset_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowListResponse:
        """
        list a new workflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/workflow/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_name": dataset_name}, workflow_list_params.WorkflowListParams
                ),
            ),
            cast_to=WorkflowListResponse,
        )

    async def delete(
        self,
        *,
        workflow_id: ID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing workflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/workflow/delete",
            body=await async_maybe_transform({"workflow_id": workflow_id}, workflow_delete_params.WorkflowDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        *,
        workflow_id: ID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExistingWorkflow:
        """
        Get a workflow by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/workflow/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"workflow_id": workflow_id}, workflow_get_params.WorkflowGetParams),
            ),
            cast_to=ExistingWorkflow,
        )

    async def job_progress(
        self,
        *,
        workflow_id: ID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowJobProgressResponse:
        """
        Get the job status breakdown of a workflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/workflow/job_progress",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workflow_id": workflow_id}, workflow_job_progress_params.WorkflowJobProgressParams
                ),
            ),
            cast_to=WorkflowJobProgressResponse,
        )

    async def jobs(
        self,
        *,
        workflow_id: ID,
        group_id: Optional[str] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] | NotGiven = NOT_GIVEN,
        step_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowJobsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/workflow/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "workflow_id": workflow_id,
                        "group_id": group_id,
                        "status": status,
                        "step_id": step_id,
                    },
                    workflow_jobs_params.WorkflowJobsParams,
                ),
            ),
            cast_to=WorkflowJobsResponse,
        )

    async def trigger(
        self,
        *,
        entity_ids: List[str],
        workflow_id: ID,
        banned_domains: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stop_config: Optional[workflow_trigger_params.StopConfig] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Trigger a workflow on a set of entities

        Args:
          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/workflow/trigger",
            body=await async_maybe_transform(
                {
                    "entity_ids": entity_ids,
                    "workflow_id": workflow_id,
                    "banned_domains": banned_domains,
                    "stop_config": stop_config,
                },
                workflow_trigger_params.WorkflowTriggerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class WorkflowResourceWithRawResponse:
    def __init__(self, workflow: WorkflowResource) -> None:
        self._workflow = workflow

        self.create = to_raw_response_wrapper(
            workflow.create,
        )
        self.update = to_raw_response_wrapper(
            workflow.update,
        )
        self.list = to_raw_response_wrapper(
            workflow.list,
        )
        self.delete = to_raw_response_wrapper(
            workflow.delete,
        )
        self.get = to_raw_response_wrapper(
            workflow.get,
        )
        self.job_progress = to_raw_response_wrapper(
            workflow.job_progress,
        )
        self.jobs = to_raw_response_wrapper(
            workflow.jobs,
        )
        self.trigger = to_raw_response_wrapper(
            workflow.trigger,
        )


class AsyncWorkflowResourceWithRawResponse:
    def __init__(self, workflow: AsyncWorkflowResource) -> None:
        self._workflow = workflow

        self.create = async_to_raw_response_wrapper(
            workflow.create,
        )
        self.update = async_to_raw_response_wrapper(
            workflow.update,
        )
        self.list = async_to_raw_response_wrapper(
            workflow.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workflow.delete,
        )
        self.get = async_to_raw_response_wrapper(
            workflow.get,
        )
        self.job_progress = async_to_raw_response_wrapper(
            workflow.job_progress,
        )
        self.jobs = async_to_raw_response_wrapper(
            workflow.jobs,
        )
        self.trigger = async_to_raw_response_wrapper(
            workflow.trigger,
        )


class WorkflowResourceWithStreamingResponse:
    def __init__(self, workflow: WorkflowResource) -> None:
        self._workflow = workflow

        self.create = to_streamed_response_wrapper(
            workflow.create,
        )
        self.update = to_streamed_response_wrapper(
            workflow.update,
        )
        self.list = to_streamed_response_wrapper(
            workflow.list,
        )
        self.delete = to_streamed_response_wrapper(
            workflow.delete,
        )
        self.get = to_streamed_response_wrapper(
            workflow.get,
        )
        self.job_progress = to_streamed_response_wrapper(
            workflow.job_progress,
        )
        self.jobs = to_streamed_response_wrapper(
            workflow.jobs,
        )
        self.trigger = to_streamed_response_wrapper(
            workflow.trigger,
        )


class AsyncWorkflowResourceWithStreamingResponse:
    def __init__(self, workflow: AsyncWorkflowResource) -> None:
        self._workflow = workflow

        self.create = async_to_streamed_response_wrapper(
            workflow.create,
        )
        self.update = async_to_streamed_response_wrapper(
            workflow.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workflow.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workflow.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            workflow.get,
        )
        self.job_progress = async_to_streamed_response_wrapper(
            workflow.job_progress,
        )
        self.jobs = async_to_streamed_response_wrapper(
            workflow.jobs,
        )
        self.trigger = async_to_streamed_response_wrapper(
            workflow.trigger,
        )
