# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    structure_run_async_params,
    structure_create_plan_params,
    structure_enhance_property_params,
    structure_find_relationship_params,
    structure_enhance_relationship_params,
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
from ..types.plan_param import PlanParam
from ..types.knowledge_graph_param import KnowledgeGraphParam
from ..types.extraction_criteria_param import ExtractionCriteriaParam
from ..types.structure_job_status_response import StructureJobStatusResponse
from ..types.structure_list_plans_response import StructureListPlansResponse

__all__ = ["StructureResource", "AsyncStructureResource"]
# ---------------- Stainless modification ----------------
import time
import logging
from typing import Optional

from ..pagination import SyncJobsList

log: logging.Logger = logging.getLogger(__name__)

from ..types.dataset_view_table_response import DatasetViewTableResponse

# --------------------------------------------------------


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

    def create_plan(
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
            "/structure/create_plan",
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "plan": plan,
                },
                structure_create_plan_params.StructureCreatePlanParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def enhance_property(
        self,
        *,
        entity_id: str,
        property_name: str,
        allow_extra_entities: bool | NotGiven = NOT_GIVEN,
        special_job_type: Optional[Literal["HumanLLM"]] | NotGiven = NOT_GIVEN,
        starting_searches: List[str] | NotGiven = NOT_GIVEN,
        starting_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Returns a job id that can be waited on until the request is finished.

        Args:
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
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
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
        allow_extra_entities: bool | NotGiven = NOT_GIVEN,
        special_job_type: Optional[Literal["HumanLLM"]] | NotGiven = NOT_GIVEN,
        starting_searches: List[str] | NotGiven = NOT_GIVEN,
        starting_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Returns a job id that can be waited on until the request is finished.

        Args:
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
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
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
        relationship_name: str,
        source_entity_id: str,
        target_entity_id: str,
        allow_extra_entities: bool | NotGiven = NOT_GIVEN,
        special_job_type: Optional[Literal["HumanLLM"]] | NotGiven = NOT_GIVEN,
        starting_searches: List[str] | NotGiven = NOT_GIVEN,
        starting_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Attempt to find the given relation between two entities.

        Args:
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
                    "relationship_name": relationship_name,
                    "source_entity_id": source_entity_id,
                    "target_entity_id": target_entity_id,
                    "allow_extra_entities": allow_extra_entities,
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
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
            body=maybe_transform(job, List[str]),
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
            body=maybe_transform(job, List[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StructureJobStatusResponse,
        )

    def list_plans(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StructureListPlansResponse:
        """List all plans for your user account in the database."""
        return self._get(
            "/structure/list_plans",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StructureListPlansResponse,
        )

    def run_async(
        self,
        *,
        name: str,
        structure_input: structure_run_async_params.StructureInput,
        extraction_criteria: Iterable[ExtractionCriteriaParam] | NotGiven = NOT_GIVEN,
        seeded_entity: KnowledgeGraphParam | NotGiven = NOT_GIVEN,
        special_job_type: Optional[Literal["HumanLLM"]] | NotGiven = NOT_GIVEN,
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
                    "name": name,
                    "structure_input": structure_input,
                    "extraction_criteria": extraction_criteria,
                    "seeded_entity": seeded_entity,
                    "special_job_type": special_job_type,
                },
                structure_run_async_params.StructureRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )
    

    # -------------------------------------------------------------------------
    # We put them down here to avoid messing with stainless imports and keep everything
    # centralized to one spot.

    def run(  # type: ignore
        self,
        name: str,
        table_name: str,
        structure_input: structure_run_async_params.StructureInput,
        extraction_criteria: Iterable[ExtractionCriteriaParam] | NotGiven = NOT_GIVEN,
        seeded_entity: KnowledgeGraphParam | NotGiven = NOT_GIVEN,
        timeout: Optional[int] = None,
    ) -> SyncJobsList[DatasetViewTableResponse]:
        """
        This function simulates a synchronous run of the async function by calling it and then waiting.
        If the timeout is reached, it attempts to cancel the job.
        """
        token: str = self.run_async(
            name=name,
            structure_input=structure_input,
            extraction_criteria=extraction_criteria,
            seeded_entity=seeded_entity,
        )
        start_time = time.time() if timeout is not None else None
        successfully_started_job = False
        last_idx = 0

        while True:
            if timeout is not None and start_time is not None:
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    if successfully_started_job:
                        raise TimeoutError(f"Job execution exceeded timeout of {timeout} seconds.")
                    else:
                        raise TimeoutError(f"Job creation exceeded timeout of {timeout} seconds.")

            resp = self.job_status(job=[token])
            status = resp.job_status[0]
            all_logs = resp.log_nodes

            new_logs = all_logs[last_idx:]
            for new_log in new_logs:
                log.info("{}".format(new_log))
            last_idx = len(all_logs)

            successfully_started_job = True
            if status not in ["Queued", "Running"]:
                return self._client.datasets.view_table(dataset=name, name=table_name)
            time.sleep(1)
    # -------------------------------------------------------------------------


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

    async def create_plan(
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
            "/structure/create_plan",
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "plan": plan,
                },
                structure_create_plan_params.StructureCreatePlanParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def enhance_property(
        self,
        *,
        entity_id: str,
        property_name: str,
        allow_extra_entities: bool | NotGiven = NOT_GIVEN,
        special_job_type: Optional[Literal["HumanLLM"]] | NotGiven = NOT_GIVEN,
        starting_searches: List[str] | NotGiven = NOT_GIVEN,
        starting_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Returns a job id that can be waited on until the request is finished.

        Args:
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
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
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
        allow_extra_entities: bool | NotGiven = NOT_GIVEN,
        special_job_type: Optional[Literal["HumanLLM"]] | NotGiven = NOT_GIVEN,
        starting_searches: List[str] | NotGiven = NOT_GIVEN,
        starting_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Returns a job id that can be waited on until the request is finished.

        Args:
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
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
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
        relationship_name: str,
        source_entity_id: str,
        target_entity_id: str,
        allow_extra_entities: bool | NotGiven = NOT_GIVEN,
        special_job_type: Optional[Literal["HumanLLM"]] | NotGiven = NOT_GIVEN,
        starting_searches: List[str] | NotGiven = NOT_GIVEN,
        starting_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Attempt to find the given relation between two entities.

        Args:
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
                    "relationship_name": relationship_name,
                    "source_entity_id": source_entity_id,
                    "target_entity_id": target_entity_id,
                    "allow_extra_entities": allow_extra_entities,
                    "special_job_type": special_job_type,
                    "starting_searches": starting_searches,
                    "starting_urls": starting_urls,
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
            body=await async_maybe_transform(job, List[str]),
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
            body=await async_maybe_transform(job, List[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StructureJobStatusResponse,
        )

    async def list_plans(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StructureListPlansResponse:
        """List all plans for your user account in the database."""
        return await self._get(
            "/structure/list_plans",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StructureListPlansResponse,
        )

    async def run_async(
        self,
        *,
        name: str,
        structure_input: structure_run_async_params.StructureInput,
        extraction_criteria: Iterable[ExtractionCriteriaParam] | NotGiven = NOT_GIVEN,
        seeded_entity: KnowledgeGraphParam | NotGiven = NOT_GIVEN,
        special_job_type: Optional[Literal["HumanLLM"]] | NotGiven = NOT_GIVEN,
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
                    "name": name,
                    "structure_input": structure_input,
                    "extraction_criteria": extraction_criteria,
                    "seeded_entity": seeded_entity,
                    "special_job_type": special_job_type,
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

        self.create_plan = to_raw_response_wrapper(
            structure.create_plan,
        )
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
        self.list_plans = to_raw_response_wrapper(
            structure.list_plans,
        )
        self.run_async = to_raw_response_wrapper(
            structure.run_async,
        )


class AsyncStructureResourceWithRawResponse:
    def __init__(self, structure: AsyncStructureResource) -> None:
        self._structure = structure

        self.create_plan = async_to_raw_response_wrapper(
            structure.create_plan,
        )
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
        self.list_plans = async_to_raw_response_wrapper(
            structure.list_plans,
        )
        self.run_async = async_to_raw_response_wrapper(
            structure.run_async,
        )


class StructureResourceWithStreamingResponse:
    def __init__(self, structure: StructureResource) -> None:
        self._structure = structure

        self.create_plan = to_streamed_response_wrapper(
            structure.create_plan,
        )
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
        self.list_plans = to_streamed_response_wrapper(
            structure.list_plans,
        )
        self.run_async = to_streamed_response_wrapper(
            structure.run_async,
        )


class AsyncStructureResourceWithStreamingResponse:
    def __init__(self, structure: AsyncStructureResource) -> None:
        self._structure = structure

        self.create_plan = async_to_streamed_response_wrapper(
            structure.create_plan,
        )
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
        self.list_plans = async_to_streamed_response_wrapper(
            structure.list_plans,
        )
        self.run_async = async_to_streamed_response_wrapper(
            structure.run_async,
        )
