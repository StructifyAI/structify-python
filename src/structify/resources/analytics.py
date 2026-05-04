# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import analytics_list_events_params, analytics_list_trackers_params, analytics_create_tracker_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.list_events_response import ListEventsResponse
from ..types.list_trackers_response import ListTrackersResponse
from ..types.create_tracker_response import CreateTrackerResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)

    def create_tracker(
        self,
        *,
        name: str,
        team_id: str,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateTrackerResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/analytics/tracker",
            body=maybe_transform(
                {
                    "name": name,
                    "team_id": team_id,
                    "allowed_origins": allowed_origins,
                },
                analytics_create_tracker_params.AnalyticsCreateTrackerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateTrackerResponse,
        )

    def list_events(
        self,
        tracker_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListEventsResponse:
        """Args:
          cursor: Opaque cursor returned as `next_cursor` on the previous page.

        Omit on the first
              request.

          limit: Maximum number of events to return. Defaults to 100, capped at 1000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tracker_id:
            raise ValueError(f"Expected a non-empty value for `tracker_id` but received {tracker_id!r}")
        return self._get(
            path_template("/analytics/{tracker_id}/events", tracker_id=tracker_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    analytics_list_events_params.AnalyticsListEventsParams,
                ),
            ),
            cast_to=ListEventsResponse,
        )

    def list_trackers(
        self,
        *,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListTrackersResponse:
        """
        Args:
          team_id: Team to list trackers for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/analytics/tracker",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"team_id": team_id}, analytics_list_trackers_params.AnalyticsListTrackersParams),
            ),
            cast_to=ListTrackersResponse,
        )

    def revoke_tracker(
        self,
        tracker_id: str,
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
        if not tracker_id:
            raise ValueError(f"Expected a non-empty value for `tracker_id` but received {tracker_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/analytics/tracker/{tracker_id}", tracker_id=tracker_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)

    async def create_tracker(
        self,
        *,
        name: str,
        team_id: str,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateTrackerResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/analytics/tracker",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "team_id": team_id,
                    "allowed_origins": allowed_origins,
                },
                analytics_create_tracker_params.AnalyticsCreateTrackerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateTrackerResponse,
        )

    async def list_events(
        self,
        tracker_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListEventsResponse:
        """Args:
          cursor: Opaque cursor returned as `next_cursor` on the previous page.

        Omit on the first
              request.

          limit: Maximum number of events to return. Defaults to 100, capped at 1000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tracker_id:
            raise ValueError(f"Expected a non-empty value for `tracker_id` but received {tracker_id!r}")
        return await self._get(
            path_template("/analytics/{tracker_id}/events", tracker_id=tracker_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    analytics_list_events_params.AnalyticsListEventsParams,
                ),
            ),
            cast_to=ListEventsResponse,
        )

    async def list_trackers(
        self,
        *,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListTrackersResponse:
        """
        Args:
          team_id: Team to list trackers for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/analytics/tracker",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"team_id": team_id}, analytics_list_trackers_params.AnalyticsListTrackersParams
                ),
            ),
            cast_to=ListTrackersResponse,
        )

    async def revoke_tracker(
        self,
        tracker_id: str,
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
        if not tracker_id:
            raise ValueError(f"Expected a non-empty value for `tracker_id` but received {tracker_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/analytics/tracker/{tracker_id}", tracker_id=tracker_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.create_tracker = to_raw_response_wrapper(
            analytics.create_tracker,
        )
        self.list_events = to_raw_response_wrapper(
            analytics.list_events,
        )
        self.list_trackers = to_raw_response_wrapper(
            analytics.list_trackers,
        )
        self.revoke_tracker = to_raw_response_wrapper(
            analytics.revoke_tracker,
        )


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.create_tracker = async_to_raw_response_wrapper(
            analytics.create_tracker,
        )
        self.list_events = async_to_raw_response_wrapper(
            analytics.list_events,
        )
        self.list_trackers = async_to_raw_response_wrapper(
            analytics.list_trackers,
        )
        self.revoke_tracker = async_to_raw_response_wrapper(
            analytics.revoke_tracker,
        )


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.create_tracker = to_streamed_response_wrapper(
            analytics.create_tracker,
        )
        self.list_events = to_streamed_response_wrapper(
            analytics.list_events,
        )
        self.list_trackers = to_streamed_response_wrapper(
            analytics.list_trackers,
        )
        self.revoke_tracker = to_streamed_response_wrapper(
            analytics.revoke_tracker,
        )


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.create_tracker = async_to_streamed_response_wrapper(
            analytics.create_tracker,
        )
        self.list_events = async_to_streamed_response_wrapper(
            analytics.list_events,
        )
        self.list_trackers = async_to_streamed_response_wrapper(
            analytics.list_trackers,
        )
        self.revoke_tracker = async_to_streamed_response_wrapper(
            analytics.revoke_tracker,
        )
