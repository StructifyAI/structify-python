# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import (
    structure_run_async_params,
    structure_job_status_params,
    structure_is_complete_params,
)
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
from ..types.knowledge_graph_param import KnowledgeGraphParam
from ..types.structure_job_status_response import StructureJobStatusResponse

__all__ = ["StructureResource", "AsyncStructureResource"]


class StructureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StructureResourceWithRawResponse:
        return StructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StructureResourceWithStreamingResponse:
        return StructureResourceWithStreamingResponse(self)

    def is_complete(
        self,
        *,
        job: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Wait for all specified async tasks to be completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            "/structure/is_complete",
            body=maybe_transform(job, structure_is_complete_params.StructureIsCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def job_status(
        self,
        *,
        job: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StructureJobStatusResponse:
        """
        and any associated LogNodes that have been added to them

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/structure/job_status",
            body=maybe_transform(job, structure_job_status_params.StructureJobStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StructureJobStatusResponse,
        )

    def run_async(
        self,
        *,
        dataset_name: str,
        structure_input: structure_run_async_params.StructureInput,
        seeded_entity: KnowledgeGraphParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          structure_input: These are all the types that can be converted into a BasicInputType

          seeded_entity: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a Neo4j DB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            "/structure/run_async",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "structure_input": structure_input,
                    "seeded_entity": seeded_entity,
                },
                structure_run_async_params.StructureRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncStructureResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStructureResourceWithRawResponse:
        return AsyncStructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStructureResourceWithStreamingResponse:
        return AsyncStructureResourceWithStreamingResponse(self)

    async def is_complete(
        self,
        *,
        job: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Wait for all specified async tasks to be completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            "/structure/is_complete",
            body=await async_maybe_transform(job, structure_is_complete_params.StructureIsCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def job_status(
        self,
        *,
        job: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StructureJobStatusResponse:
        """
        and any associated LogNodes that have been added to them

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/structure/job_status",
            body=await async_maybe_transform(job, structure_job_status_params.StructureJobStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StructureJobStatusResponse,
        )

    async def run_async(
        self,
        *,
        dataset_name: str,
        structure_input: structure_run_async_params.StructureInput,
        seeded_entity: KnowledgeGraphParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          structure_input: These are all the types that can be converted into a BasicInputType

          seeded_entity: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a Neo4j DB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            "/structure/run_async",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "structure_input": structure_input,
                    "seeded_entity": seeded_entity,
                },
                structure_run_async_params.StructureRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class StructureResourceWithRawResponse:
    def __init__(self, structure: StructureResource) -> None:
        self._structure = structure

        self.is_complete = to_raw_response_wrapper(
            structure.is_complete,
        )
        self.job_status = to_raw_response_wrapper(
            structure.job_status,
        )
        self.run_async = to_raw_response_wrapper(
            structure.run_async,
        )


class AsyncStructureResourceWithRawResponse:
    def __init__(self, structure: AsyncStructureResource) -> None:
        self._structure = structure

        self.is_complete = async_to_raw_response_wrapper(
            structure.is_complete,
        )
        self.job_status = async_to_raw_response_wrapper(
            structure.job_status,
        )
        self.run_async = async_to_raw_response_wrapper(
            structure.run_async,
        )


class StructureResourceWithStreamingResponse:
    def __init__(self, structure: StructureResource) -> None:
        self._structure = structure

        self.is_complete = to_streamed_response_wrapper(
            structure.is_complete,
        )
        self.job_status = to_streamed_response_wrapper(
            structure.job_status,
        )
        self.run_async = to_streamed_response_wrapper(
            structure.run_async,
        )


class AsyncStructureResourceWithStreamingResponse:
    def __init__(self, structure: AsyncStructureResource) -> None:
        self._structure = structure

        self.is_complete = async_to_streamed_response_wrapper(
            structure.is_complete,
        )
        self.job_status = async_to_streamed_response_wrapper(
            structure.job_status,
        )
        self.run_async = async_to_streamed_response_wrapper(
            structure.run_async,
        )
