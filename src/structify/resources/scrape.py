# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import scrape_list_params, scrape_scrape_params
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
from .._base_client import make_request_options
from ..types.scrape_list_response import ScrapeListResponse
from ..types.knowledge_graph_param import KnowledgeGraphParam
from ..types.save_requirement_param import SaveRequirementParam
from ..types.scrape_scrape_response import ScrapeScrapeResponse
from ..types.dataset_descriptor_param import DatasetDescriptorParam

__all__ = ["ScrapeResource", "AsyncScrapeResource"]


class ScrapeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScrapeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return ScrapeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScrapeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return ScrapeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        dataset_descriptor: DatasetDescriptorParam,
        input: scrape_list_params.Input,
        table_name: str,
        dataset_name: Optional[str] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        stop_config: Optional[scrape_list_params.StopConfig] | Omit = omit,
        use_proxy: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScrapeListResponse:
        """
        Args:
          dataset_descriptor: A dataset is where you put multiple referential schemas.

              A dataset is a complete namespace where all references between schemas are held
              within the dataset.

          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scrape/list",
            body=maybe_transform(
                {
                    "dataset_descriptor": dataset_descriptor,
                    "input": input,
                    "table_name": table_name,
                    "dataset_name": dataset_name,
                    "node_id": node_id,
                    "stop_config": stop_config,
                    "use_proxy": use_proxy,
                },
                scrape_list_params.ScrapeListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScrapeListResponse,
        )

    def scrape(
        self,
        *,
        dataset_name: str,
        extraction_criteria: Iterable[SaveRequirementParam],
        url: str,
        node_id: Optional[str] | Omit = omit,
        seeded_kg: Optional[KnowledgeGraphParam] | Omit = omit,
        stop_config: Optional[scrape_scrape_params.StopConfig] | Omit = omit,
        use_proxy: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScrapeScrapeResponse:
        """
        Args:
          seeded_kg: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a DB

          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scrape",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "extraction_criteria": extraction_criteria,
                    "url": url,
                    "node_id": node_id,
                    "seeded_kg": seeded_kg,
                    "stop_config": stop_config,
                    "use_proxy": use_proxy,
                },
                scrape_scrape_params.ScrapeScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScrapeScrapeResponse,
        )


class AsyncScrapeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScrapeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScrapeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScrapeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncScrapeResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        dataset_descriptor: DatasetDescriptorParam,
        input: scrape_list_params.Input,
        table_name: str,
        dataset_name: Optional[str] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        stop_config: Optional[scrape_list_params.StopConfig] | Omit = omit,
        use_proxy: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScrapeListResponse:
        """
        Args:
          dataset_descriptor: A dataset is where you put multiple referential schemas.

              A dataset is a complete namespace where all references between schemas are held
              within the dataset.

          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scrape/list",
            body=await async_maybe_transform(
                {
                    "dataset_descriptor": dataset_descriptor,
                    "input": input,
                    "table_name": table_name,
                    "dataset_name": dataset_name,
                    "node_id": node_id,
                    "stop_config": stop_config,
                    "use_proxy": use_proxy,
                },
                scrape_list_params.ScrapeListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScrapeListResponse,
        )

    async def scrape(
        self,
        *,
        dataset_name: str,
        extraction_criteria: Iterable[SaveRequirementParam],
        url: str,
        node_id: Optional[str] | Omit = omit,
        seeded_kg: Optional[KnowledgeGraphParam] | Omit = omit,
        stop_config: Optional[scrape_scrape_params.StopConfig] | Omit = omit,
        use_proxy: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScrapeScrapeResponse:
        """
        Args:
          seeded_kg: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a DB

          stop_config: Configuration parameters for the StopChecker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scrape",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "extraction_criteria": extraction_criteria,
                    "url": url,
                    "node_id": node_id,
                    "seeded_kg": seeded_kg,
                    "stop_config": stop_config,
                    "use_proxy": use_proxy,
                },
                scrape_scrape_params.ScrapeScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScrapeScrapeResponse,
        )


class ScrapeResourceWithRawResponse:
    def __init__(self, scrape: ScrapeResource) -> None:
        self._scrape = scrape

        self.list = to_raw_response_wrapper(
            scrape.list,
        )
        self.scrape = to_raw_response_wrapper(
            scrape.scrape,
        )


class AsyncScrapeResourceWithRawResponse:
    def __init__(self, scrape: AsyncScrapeResource) -> None:
        self._scrape = scrape

        self.list = async_to_raw_response_wrapper(
            scrape.list,
        )
        self.scrape = async_to_raw_response_wrapper(
            scrape.scrape,
        )


class ScrapeResourceWithStreamingResponse:
    def __init__(self, scrape: ScrapeResource) -> None:
        self._scrape = scrape

        self.list = to_streamed_response_wrapper(
            scrape.list,
        )
        self.scrape = to_streamed_response_wrapper(
            scrape.scrape,
        )


class AsyncScrapeResourceWithStreamingResponse:
    def __init__(self, scrape: AsyncScrapeResource) -> None:
        self._scrape = scrape

        self.list = async_to_streamed_response_wrapper(
            scrape.list,
        )
        self.scrape = async_to_streamed_response_wrapper(
            scrape.scrape,
        )
