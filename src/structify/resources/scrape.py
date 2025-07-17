# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import scrape_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
        table_name: str,
        url: str,
        node_id: Optional[str] | NotGiven = NOT_GIVEN,
        stop_config: Optional[scrape_list_params.StopConfig] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScrapeListResponse:
        """
        Scrape a list from a URL and return a knowledge graph

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
                    "table_name": table_name,
                    "url": url,
                    "node_id": node_id,
                    "stop_config": stop_config,
                },
                scrape_list_params.ScrapeListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScrapeListResponse,
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
        table_name: str,
        url: str,
        node_id: Optional[str] | NotGiven = NOT_GIVEN,
        stop_config: Optional[scrape_list_params.StopConfig] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScrapeListResponse:
        """
        Scrape a list from a URL and return a knowledge graph

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
                    "table_name": table_name,
                    "url": url,
                    "node_id": node_id,
                    "stop_config": stop_config,
                },
                scrape_list_params.ScrapeListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScrapeListResponse,
        )


class ScrapeResourceWithRawResponse:
    def __init__(self, scrape: ScrapeResource) -> None:
        self._scrape = scrape

        self.list = to_raw_response_wrapper(
            scrape.list,
        )


class AsyncScrapeResourceWithRawResponse:
    def __init__(self, scrape: AsyncScrapeResource) -> None:
        self._scrape = scrape

        self.list = async_to_raw_response_wrapper(
            scrape.list,
        )


class ScrapeResourceWithStreamingResponse:
    def __init__(self, scrape: ScrapeResource) -> None:
        self._scrape = scrape

        self.list = to_streamed_response_wrapper(
            scrape.list,
        )


class AsyncScrapeResourceWithStreamingResponse:
    def __init__(self, scrape: AsyncScrapeResource) -> None:
        self._scrape = scrape

        self.list = async_to_streamed_response_wrapper(
            scrape.list,
        )
