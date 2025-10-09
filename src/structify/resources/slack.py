# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..types import slack_events_params, slack_user_mapping_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.slack_api_response import SlackAPIResponse
from ..types.slack_connection_status import SlackConnectionStatus
from ..types.slack_user_mapping_response import SlackUserMappingResponse

__all__ = ["SlackResource", "AsyncSlackResource"]


class SlackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SlackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return SlackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SlackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return SlackResourceWithStreamingResponse(self)

    @overload
    def events(
        self,
        *,
        challenge: str,
        type: Literal["url_verification"],
        token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackAPIResponse:
        """This endpoint receives events from Slack when users mention @structify.

        It
        handles URL verification challenges and app mention events. Requires proper
        authentication via StructifyUser - no fake users created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def events(
        self,
        *,
        event: slack_events_params.Variant1Event,
        team_id: str,
        type: Literal["event_callback"],
        api_app_id: Optional[str] | Omit = omit,
        authed_users: Optional[SequenceNotStr[str]] | Omit = omit,
        event_context: Optional[str] | Omit = omit,
        event_id: Optional[str] | Omit = omit,
        event_time: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackAPIResponse:
        """This endpoint receives events from Slack when users mention @structify.

        It
        handles URL verification challenges and app mention events. Requires proper
        authentication via StructifyUser - no fake users created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["challenge", "type"], ["event", "team_id", "type"])
    def events(
        self,
        *,
        challenge: str | Omit = omit,
        type: Literal["url_verification"] | Literal["event_callback"],
        token: Optional[str] | Omit = omit,
        event: slack_events_params.Variant1Event | Omit = omit,
        team_id: str | Omit = omit,
        api_app_id: Optional[str] | Omit = omit,
        authed_users: Optional[SequenceNotStr[str]] | Omit = omit,
        event_context: Optional[str] | Omit = omit,
        event_id: Optional[str] | Omit = omit,
        event_time: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackAPIResponse:
        return cast(
            SlackAPIResponse,
            self._post(
                "/slack/events",
                body=maybe_transform(
                    {
                        "challenge": challenge,
                        "type": type,
                        "token": token,
                        "event": event,
                        "team_id": team_id,
                        "api_app_id": api_app_id,
                        "authed_users": authed_users,
                        "event_context": event_context,
                        "event_id": event_id,
                        "event_time": event_time,
                    },
                    slack_events_params.SlackEventsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, SlackAPIResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackConnectionStatus:
        """Get current user's Slack connection status"""
        return self._get(
            "/slack/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlackConnectionStatus,
        )

    def user_mapping(
        self,
        *,
        slack_bot_token: str,
        slack_team_id: str,
        slack_user_id: str,
        slack_username: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackUserMappingResponse:
        """
        Create Slack user mapping directly from token data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/slack/user-mapping",
            body=maybe_transform(
                {
                    "slack_bot_token": slack_bot_token,
                    "slack_team_id": slack_team_id,
                    "slack_user_id": slack_user_id,
                    "slack_username": slack_username,
                },
                slack_user_mapping_params.SlackUserMappingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlackUserMappingResponse,
        )


class AsyncSlackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSlackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSlackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSlackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncSlackResourceWithStreamingResponse(self)

    @overload
    async def events(
        self,
        *,
        challenge: str,
        type: Literal["url_verification"],
        token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackAPIResponse:
        """This endpoint receives events from Slack when users mention @structify.

        It
        handles URL verification challenges and app mention events. Requires proper
        authentication via StructifyUser - no fake users created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def events(
        self,
        *,
        event: slack_events_params.Variant1Event,
        team_id: str,
        type: Literal["event_callback"],
        api_app_id: Optional[str] | Omit = omit,
        authed_users: Optional[SequenceNotStr[str]] | Omit = omit,
        event_context: Optional[str] | Omit = omit,
        event_id: Optional[str] | Omit = omit,
        event_time: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackAPIResponse:
        """This endpoint receives events from Slack when users mention @structify.

        It
        handles URL verification challenges and app mention events. Requires proper
        authentication via StructifyUser - no fake users created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["challenge", "type"], ["event", "team_id", "type"])
    async def events(
        self,
        *,
        challenge: str | Omit = omit,
        type: Literal["url_verification"] | Literal["event_callback"],
        token: Optional[str] | Omit = omit,
        event: slack_events_params.Variant1Event | Omit = omit,
        team_id: str | Omit = omit,
        api_app_id: Optional[str] | Omit = omit,
        authed_users: Optional[SequenceNotStr[str]] | Omit = omit,
        event_context: Optional[str] | Omit = omit,
        event_id: Optional[str] | Omit = omit,
        event_time: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackAPIResponse:
        return cast(
            SlackAPIResponse,
            await self._post(
                "/slack/events",
                body=await async_maybe_transform(
                    {
                        "challenge": challenge,
                        "type": type,
                        "token": token,
                        "event": event,
                        "team_id": team_id,
                        "api_app_id": api_app_id,
                        "authed_users": authed_users,
                        "event_context": event_context,
                        "event_id": event_id,
                        "event_time": event_time,
                    },
                    slack_events_params.SlackEventsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, SlackAPIResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackConnectionStatus:
        """Get current user's Slack connection status"""
        return await self._get(
            "/slack/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlackConnectionStatus,
        )

    async def user_mapping(
        self,
        *,
        slack_bot_token: str,
        slack_team_id: str,
        slack_user_id: str,
        slack_username: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackUserMappingResponse:
        """
        Create Slack user mapping directly from token data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/slack/user-mapping",
            body=await async_maybe_transform(
                {
                    "slack_bot_token": slack_bot_token,
                    "slack_team_id": slack_team_id,
                    "slack_user_id": slack_user_id,
                    "slack_username": slack_username,
                },
                slack_user_mapping_params.SlackUserMappingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlackUserMappingResponse,
        )


class SlackResourceWithRawResponse:
    def __init__(self, slack: SlackResource) -> None:
        self._slack = slack

        self.events = to_raw_response_wrapper(
            slack.events,
        )
        self.status = to_raw_response_wrapper(
            slack.status,
        )
        self.user_mapping = to_raw_response_wrapper(
            slack.user_mapping,
        )


class AsyncSlackResourceWithRawResponse:
    def __init__(self, slack: AsyncSlackResource) -> None:
        self._slack = slack

        self.events = async_to_raw_response_wrapper(
            slack.events,
        )
        self.status = async_to_raw_response_wrapper(
            slack.status,
        )
        self.user_mapping = async_to_raw_response_wrapper(
            slack.user_mapping,
        )


class SlackResourceWithStreamingResponse:
    def __init__(self, slack: SlackResource) -> None:
        self._slack = slack

        self.events = to_streamed_response_wrapper(
            slack.events,
        )
        self.status = to_streamed_response_wrapper(
            slack.status,
        )
        self.user_mapping = to_streamed_response_wrapper(
            slack.user_mapping,
        )


class AsyncSlackResourceWithStreamingResponse:
    def __init__(self, slack: AsyncSlackResource) -> None:
        self._slack = slack

        self.events = async_to_streamed_response_wrapper(
            slack.events,
        )
        self.status = async_to_streamed_response_wrapper(
            slack.status,
        )
        self.user_mapping = async_to_streamed_response_wrapper(
            slack.user_mapping,
        )
