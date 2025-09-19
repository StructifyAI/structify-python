# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    structure_run_async_params,
    structure_job_status_params,
    structure_enhance_property_params,
    structure_find_relationship_params,
    structure_enhance_relationship_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.knowledge_graph_param import KnowledgeGraphParam
from ..types.save_requirement_param import SaveRequirementParam
from ..types.structure_job_status_response import StructureJobStatusResponse

__all__ = ["StructureResource", "AsyncStructureResource"]


class StructureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StructureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return StructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StructureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return StructureResourceWithStreamingResponse(self)

    def enhance_property(
        self,
        *,
        entity_id: str,
        property_name: str,
        allow_extra_entities: bool | Omit = omit,
        banned_domains: SequenceNotStr[str] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        special_job_type: Optional[Literal["HumanLLM"]] | Omit = omit,
        starting_searches: SequenceNotStr[str] | Omit = omit,
        starting_urls: SequenceNotStr[str] | Omit = omit,
        stop_config: Optional[structure_enhance_property_params.StopConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Returns a job id that can be waited on until the request is finished.

        Args:
          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            "/structure/enhance_property",
            body=maybe_transform(
                {
                    "entity_id": entity_id,
                    "property_name": property_name,
                    "allow_extra_entities": allow_extra_entities,
                    "banned_domains": banned_domains,
                    "node_id": node_id,
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
                    "stop_config": stop_config,
                },
                structure_enhance_property_params.StructureEnhancePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def enhance_relationship(
        self,
        *,
        entity_id: str,
        relationship_name: str,
        allow_extra_entities: bool | Omit = omit,
        banned_domains: SequenceNotStr[str] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        special_job_type: Optional[Literal["HumanLLM"]] | Omit = omit,
        starting_searches: SequenceNotStr[str] | Omit = omit,
        starting_urls: SequenceNotStr[str] | Omit = omit,
        stop_config: Optional[structure_enhance_relationship_params.StopConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Returns a job id that can be waited on until the request is finished.

        Args:
          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            "/structure/enhance_relationship",
            body=maybe_transform(
                {
                    "entity_id": entity_id,
                    "relationship_name": relationship_name,
                    "allow_extra_entities": allow_extra_entities,
                    "banned_domains": banned_domains,
                    "node_id": node_id,
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
                    "stop_config": stop_config,
                },
                structure_enhance_relationship_params.StructureEnhanceRelationshipParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def find_relationship(
        self,
        *,
        from_id: str,
        relationship_name: str,
        to_id: str,
        allow_extra_entities: bool | Omit = omit,
        banned_domains: SequenceNotStr[str] | Omit = omit,
        special_job_type: Optional[Literal["HumanLLM"]] | Omit = omit,
        starting_searches: SequenceNotStr[str] | Omit = omit,
        starting_urls: SequenceNotStr[str] | Omit = omit,
        stop_config: Optional[structure_find_relationship_params.StopConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Attempt to find the given relation between two entities.

        Args:
          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            "/structure/find_relationship",
            body=maybe_transform(
                {
                    "from_id": from_id,
                    "relationship_name": relationship_name,
                    "to_id": to_id,
                    "allow_extra_entities": allow_extra_entities,
                    "banned_domains": banned_domains,
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
                    "stop_config": stop_config,
                },
                structure_find_relationship_params.StructureFindRelationshipParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def is_complete(
        self,
        *,
        job: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            body=maybe_transform(job, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def job_status(
        self,
        *,
        job: structure_job_status_params.Job,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StructureJobStatusResponse:
        """
        If only dataset_name is provided, up to 1000 of the most recent jobs for that
        dataset will be returned.

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
        dataset: str,
        source: structure_run_async_params.Source,
        node_id: Optional[str] | Omit = omit,
        save_requirement: Iterable[SaveRequirementParam] | Omit = omit,
        seeded_entity: KnowledgeGraphParam | Omit = omit,
        special_job_type: Optional[Literal["HumanLLM"]] | Omit = omit,
        stop_config: Optional[structure_run_async_params.StopConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          source: These are all the types that can be converted into a BasicInputType

          seeded_entity: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a DB

          stop_config: Configuration parameters for the StopChecker

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
                    "dataset": dataset,
                    "source": source,
                    "node_id": node_id,
                    "save_requirement": save_requirement,
                    "seeded_entity": seeded_entity,
                    "special_job_type": special_job_type,
                    "stop_config": stop_config,
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStructureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncStructureResourceWithStreamingResponse(self)

    async def enhance_property(
        self,
        *,
        entity_id: str,
        property_name: str,
        allow_extra_entities: bool | Omit = omit,
        banned_domains: SequenceNotStr[str] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        special_job_type: Optional[Literal["HumanLLM"]] | Omit = omit,
        starting_searches: SequenceNotStr[str] | Omit = omit,
        starting_urls: SequenceNotStr[str] | Omit = omit,
        stop_config: Optional[structure_enhance_property_params.StopConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Returns a job id that can be waited on until the request is finished.

        Args:
          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            "/structure/enhance_property",
            body=await async_maybe_transform(
                {
                    "entity_id": entity_id,
                    "property_name": property_name,
                    "allow_extra_entities": allow_extra_entities,
                    "banned_domains": banned_domains,
                    "node_id": node_id,
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
                    "stop_config": stop_config,
                },
                structure_enhance_property_params.StructureEnhancePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def enhance_relationship(
        self,
        *,
        entity_id: str,
        relationship_name: str,
        allow_extra_entities: bool | Omit = omit,
        banned_domains: SequenceNotStr[str] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        special_job_type: Optional[Literal["HumanLLM"]] | Omit = omit,
        starting_searches: SequenceNotStr[str] | Omit = omit,
        starting_urls: SequenceNotStr[str] | Omit = omit,
        stop_config: Optional[structure_enhance_relationship_params.StopConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Returns a job id that can be waited on until the request is finished.

        Args:
          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            "/structure/enhance_relationship",
            body=await async_maybe_transform(
                {
                    "entity_id": entity_id,
                    "relationship_name": relationship_name,
                    "allow_extra_entities": allow_extra_entities,
                    "banned_domains": banned_domains,
                    "node_id": node_id,
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
                    "stop_config": stop_config,
                },
                structure_enhance_relationship_params.StructureEnhanceRelationshipParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def find_relationship(
        self,
        *,
        from_id: str,
        relationship_name: str,
        to_id: str,
        allow_extra_entities: bool | Omit = omit,
        banned_domains: SequenceNotStr[str] | Omit = omit,
        special_job_type: Optional[Literal["HumanLLM"]] | Omit = omit,
        starting_searches: SequenceNotStr[str] | Omit = omit,
        starting_urls: SequenceNotStr[str] | Omit = omit,
        stop_config: Optional[structure_find_relationship_params.StopConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Attempt to find the given relation between two entities.

        Args:
          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            "/structure/find_relationship",
            body=await async_maybe_transform(
                {
                    "from_id": from_id,
                    "relationship_name": relationship_name,
                    "to_id": to_id,
                    "allow_extra_entities": allow_extra_entities,
                    "banned_domains": banned_domains,
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
                    "stop_config": stop_config,
                },
                structure_find_relationship_params.StructureFindRelationshipParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def is_complete(
        self,
        *,
        job: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            body=await async_maybe_transform(job, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def job_status(
        self,
        *,
        job: structure_job_status_params.Job,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StructureJobStatusResponse:
        """
        If only dataset_name is provided, up to 1000 of the most recent jobs for that
        dataset will be returned.

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
        dataset: str,
        source: structure_run_async_params.Source,
        node_id: Optional[str] | Omit = omit,
        save_requirement: Iterable[SaveRequirementParam] | Omit = omit,
        seeded_entity: KnowledgeGraphParam | Omit = omit,
        special_job_type: Optional[Literal["HumanLLM"]] | Omit = omit,
        stop_config: Optional[structure_run_async_params.StopConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          source: These are all the types that can be converted into a BasicInputType

          seeded_entity: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a DB

          stop_config: Configuration parameters for the StopChecker

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
                    "dataset": dataset,
                    "source": source,
                    "node_id": node_id,
                    "save_requirement": save_requirement,
                    "seeded_entity": seeded_entity,
                    "special_job_type": special_job_type,
                    "stop_config": stop_config,
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

        self.enhance_property = to_raw_response_wrapper(
            structure.enhance_property,
        )
        self.enhance_relationship = to_raw_response_wrapper(
            structure.enhance_relationship,
        )
        self.find_relationship = to_raw_response_wrapper(
            structure.find_relationship,
        )
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

        self.enhance_property = async_to_raw_response_wrapper(
            structure.enhance_property,
        )
        self.enhance_relationship = async_to_raw_response_wrapper(
            structure.enhance_relationship,
        )
        self.find_relationship = async_to_raw_response_wrapper(
            structure.find_relationship,
        )
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

        self.enhance_property = to_streamed_response_wrapper(
            structure.enhance_property,
        )
        self.enhance_relationship = to_streamed_response_wrapper(
            structure.enhance_relationship,
        )
        self.find_relationship = to_streamed_response_wrapper(
            structure.find_relationship,
        )
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

        self.enhance_property = async_to_streamed_response_wrapper(
            structure.enhance_property,
        )
        self.enhance_relationship = async_to_streamed_response_wrapper(
            structure.enhance_relationship,
        )
        self.find_relationship = async_to_streamed_response_wrapper(
            structure.find_relationship,
        )
        self.is_complete = async_to_streamed_response_wrapper(
            structure.is_complete,
        )
        self.job_status = async_to_streamed_response_wrapper(
            structure.job_status,
        )
        self.run_async = async_to_streamed_response_wrapper(
            structure.run_async,
        )
