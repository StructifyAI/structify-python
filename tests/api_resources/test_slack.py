# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    SlackAPIResponse,
    SlackOAuthResponse,
    SlackConnectionStatus,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSlack:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_disconnect(self, client: Structify) -> None:
        slack = client.slack.disconnect()
        assert_matches_type(SlackOAuthResponse, slack, path=["response"])

    @parametrize
    def test_raw_response_disconnect(self, client: Structify) -> None:
        response = client.slack.with_raw_response.disconnect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = response.parse()
        assert_matches_type(SlackOAuthResponse, slack, path=["response"])

    @parametrize
    def test_streaming_response_disconnect(self, client: Structify) -> None:
        with client.slack.with_streaming_response.disconnect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = response.parse()
            assert_matches_type(SlackOAuthResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_events_overload_1(self, client: Structify) -> None:
        slack = client.slack.events(
            challenge="challenge",
            type="url_verification",
        )
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    def test_method_events_with_all_params_overload_1(self, client: Structify) -> None:
        slack = client.slack.events(
            challenge="challenge",
            type="url_verification",
            token="token",
        )
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    def test_raw_response_events_overload_1(self, client: Structify) -> None:
        response = client.slack.with_raw_response.events(
            challenge="challenge",
            type="url_verification",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = response.parse()
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    def test_streaming_response_events_overload_1(self, client: Structify) -> None:
        with client.slack.with_streaming_response.events(
            challenge="challenge",
            type="url_verification",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = response.parse()
            assert_matches_type(SlackAPIResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_events_overload_2(self, client: Structify) -> None:
        slack = client.slack.events(
            event={
                "channel": "channel",
                "text": "text",
                "ts": "ts",
                "type": "app_mention",
                "user": "user",
            },
            team_id="team_id",
            type="event_callback",
        )
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    def test_method_events_with_all_params_overload_2(self, client: Structify) -> None:
        slack = client.slack.events(
            event={
                "channel": "channel",
                "text": "text",
                "ts": "ts",
                "type": "app_mention",
                "user": "user",
                "channel_type": "channel_type",
                "client_msg_id": "client_msg_id",
                "event_ts": "event_ts",
                "team": "team",
                "thread_ts": "thread_ts",
            },
            team_id="team_id",
            type="event_callback",
            api_app_id="api_app_id",
            authed_users=["string"],
            event_context="event_context",
            event_id="event_id",
            event_time=0,
        )
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    def test_raw_response_events_overload_2(self, client: Structify) -> None:
        response = client.slack.with_raw_response.events(
            event={
                "channel": "channel",
                "text": "text",
                "ts": "ts",
                "type": "app_mention",
                "user": "user",
            },
            team_id="team_id",
            type="event_callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = response.parse()
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    def test_streaming_response_events_overload_2(self, client: Structify) -> None:
        with client.slack.with_streaming_response.events(
            event={
                "channel": "channel",
                "text": "text",
                "ts": "ts",
                "type": "app_mention",
                "user": "user",
            },
            team_id="team_id",
            type="event_callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = response.parse()
            assert_matches_type(SlackAPIResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_oauth_callback(self, client: Structify) -> None:
        slack = client.slack.oauth_callback(
            code="code",
        )
        assert_matches_type(SlackOAuthResponse, slack, path=["response"])

    @parametrize
    def test_method_oauth_callback_with_all_params(self, client: Structify) -> None:
        slack = client.slack.oauth_callback(
            code="code",
            redirect_uri="redirect_uri",
        )
        assert_matches_type(SlackOAuthResponse, slack, path=["response"])

    @parametrize
    def test_raw_response_oauth_callback(self, client: Structify) -> None:
        response = client.slack.with_raw_response.oauth_callback(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = response.parse()
        assert_matches_type(SlackOAuthResponse, slack, path=["response"])

    @parametrize
    def test_streaming_response_oauth_callback(self, client: Structify) -> None:
        with client.slack.with_streaming_response.oauth_callback(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = response.parse()
            assert_matches_type(SlackOAuthResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_status(self, client: Structify) -> None:
        slack = client.slack.status()
        assert_matches_type(SlackConnectionStatus, slack, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Structify) -> None:
        response = client.slack.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = response.parse()
        assert_matches_type(SlackConnectionStatus, slack, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Structify) -> None:
        with client.slack.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = response.parse()
            assert_matches_type(SlackConnectionStatus, slack, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSlack:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_disconnect(self, async_client: AsyncStructify) -> None:
        slack = await async_client.slack.disconnect()
        assert_matches_type(SlackOAuthResponse, slack, path=["response"])

    @parametrize
    async def test_raw_response_disconnect(self, async_client: AsyncStructify) -> None:
        response = await async_client.slack.with_raw_response.disconnect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = await response.parse()
        assert_matches_type(SlackOAuthResponse, slack, path=["response"])

    @parametrize
    async def test_streaming_response_disconnect(self, async_client: AsyncStructify) -> None:
        async with async_client.slack.with_streaming_response.disconnect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = await response.parse()
            assert_matches_type(SlackOAuthResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_events_overload_1(self, async_client: AsyncStructify) -> None:
        slack = await async_client.slack.events(
            challenge="challenge",
            type="url_verification",
        )
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    async def test_method_events_with_all_params_overload_1(self, async_client: AsyncStructify) -> None:
        slack = await async_client.slack.events(
            challenge="challenge",
            type="url_verification",
            token="token",
        )
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    async def test_raw_response_events_overload_1(self, async_client: AsyncStructify) -> None:
        response = await async_client.slack.with_raw_response.events(
            challenge="challenge",
            type="url_verification",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = await response.parse()
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    async def test_streaming_response_events_overload_1(self, async_client: AsyncStructify) -> None:
        async with async_client.slack.with_streaming_response.events(
            challenge="challenge",
            type="url_verification",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = await response.parse()
            assert_matches_type(SlackAPIResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_events_overload_2(self, async_client: AsyncStructify) -> None:
        slack = await async_client.slack.events(
            event={
                "channel": "channel",
                "text": "text",
                "ts": "ts",
                "type": "app_mention",
                "user": "user",
            },
            team_id="team_id",
            type="event_callback",
        )
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    async def test_method_events_with_all_params_overload_2(self, async_client: AsyncStructify) -> None:
        slack = await async_client.slack.events(
            event={
                "channel": "channel",
                "text": "text",
                "ts": "ts",
                "type": "app_mention",
                "user": "user",
                "channel_type": "channel_type",
                "client_msg_id": "client_msg_id",
                "event_ts": "event_ts",
                "team": "team",
                "thread_ts": "thread_ts",
            },
            team_id="team_id",
            type="event_callback",
            api_app_id="api_app_id",
            authed_users=["string"],
            event_context="event_context",
            event_id="event_id",
            event_time=0,
        )
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    async def test_raw_response_events_overload_2(self, async_client: AsyncStructify) -> None:
        response = await async_client.slack.with_raw_response.events(
            event={
                "channel": "channel",
                "text": "text",
                "ts": "ts",
                "type": "app_mention",
                "user": "user",
            },
            team_id="team_id",
            type="event_callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = await response.parse()
        assert_matches_type(SlackAPIResponse, slack, path=["response"])

    @parametrize
    async def test_streaming_response_events_overload_2(self, async_client: AsyncStructify) -> None:
        async with async_client.slack.with_streaming_response.events(
            event={
                "channel": "channel",
                "text": "text",
                "ts": "ts",
                "type": "app_mention",
                "user": "user",
            },
            team_id="team_id",
            type="event_callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = await response.parse()
            assert_matches_type(SlackAPIResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_oauth_callback(self, async_client: AsyncStructify) -> None:
        slack = await async_client.slack.oauth_callback(
            code="code",
        )
        assert_matches_type(SlackOAuthResponse, slack, path=["response"])

    @parametrize
    async def test_method_oauth_callback_with_all_params(self, async_client: AsyncStructify) -> None:
        slack = await async_client.slack.oauth_callback(
            code="code",
            redirect_uri="redirect_uri",
        )
        assert_matches_type(SlackOAuthResponse, slack, path=["response"])

    @parametrize
    async def test_raw_response_oauth_callback(self, async_client: AsyncStructify) -> None:
        response = await async_client.slack.with_raw_response.oauth_callback(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = await response.parse()
        assert_matches_type(SlackOAuthResponse, slack, path=["response"])

    @parametrize
    async def test_streaming_response_oauth_callback(self, async_client: AsyncStructify) -> None:
        async with async_client.slack.with_streaming_response.oauth_callback(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = await response.parse()
            assert_matches_type(SlackOAuthResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_status(self, async_client: AsyncStructify) -> None:
        slack = await async_client.slack.status()
        assert_matches_type(SlackConnectionStatus, slack, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncStructify) -> None:
        response = await async_client.slack.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = await response.parse()
        assert_matches_type(SlackConnectionStatus, slack, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncStructify) -> None:
        async with async_client.slack.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = await response.parse()
            assert_matches_type(SlackConnectionStatus, slack, path=["response"])

        assert cast(Any, response.is_closed) is True
