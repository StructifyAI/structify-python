# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import report_step_params, report_entity_params
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

__all__ = ["ReportResource", "AsyncReportResource"]


class ReportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportResourceWithRawResponse:
        return ReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportResourceWithStreamingResponse:
        return ReportResourceWithStreamingResponse(self)

    def entity(
        self,
        *,
        id: str,
        property: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get all sources for a given entity

        Args:
          property: A short message about why the entity is being reported

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            "/report/entity",
            body=maybe_transform(
                {
                    "id": id,
                    "property": property,
                },
                report_entity_params.ReportEntityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def step(
        self,
        *,
        step_id: str,
        message: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get all sources for a given entity

        Args:
          message: A short message about why the step is being reported

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            "/report/step",
            body=maybe_transform(
                {
                    "step_id": step_id,
                    "message": message,
                },
                report_step_params.ReportStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncReportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportResourceWithRawResponse:
        return AsyncReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportResourceWithStreamingResponse:
        return AsyncReportResourceWithStreamingResponse(self)

    async def entity(
        self,
        *,
        id: str,
        property: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get all sources for a given entity

        Args:
          property: A short message about why the entity is being reported

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            "/report/entity",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "property": property,
                },
                report_entity_params.ReportEntityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def step(
        self,
        *,
        step_id: str,
        message: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get all sources for a given entity

        Args:
          message: A short message about why the step is being reported

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            "/report/step",
            body=await async_maybe_transform(
                {
                    "step_id": step_id,
                    "message": message,
                },
                report_step_params.ReportStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ReportResourceWithRawResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

        self.entity = to_raw_response_wrapper(
            report.entity,
        )
        self.step = to_raw_response_wrapper(
            report.step,
        )


class AsyncReportResourceWithRawResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

        self.entity = async_to_raw_response_wrapper(
            report.entity,
        )
        self.step = async_to_raw_response_wrapper(
            report.step,
        )


class ReportResourceWithStreamingResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

        self.entity = to_streamed_response_wrapper(
            report.entity,
        )
        self.step = to_streamed_response_wrapper(
            report.step,
        )


class AsyncReportResourceWithStreamingResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

        self.entity = async_to_streamed_response_wrapper(
            report.entity,
        )
        self.step = async_to_streamed_response_wrapper(
            report.step,
        )
