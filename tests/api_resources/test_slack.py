# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    SlackAPIResponse,
    SlackConnectionStatus,
    SlackUserMappingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSlack:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

    @parametrize
    def test_method_user_mapping(self, client: Structify) -> None:
        slack = client.slack.user_mapping(
            slack_bot_token="slack_bot_token",
            slack_team_id="slack_team_id",
            slack_user_id="slack_user_id",
        )
        assert_matches_type(SlackUserMappingResponse, slack, path=["response"])

    @parametrize
    def test_method_user_mapping_with_all_params(self, client: Structify) -> None:
        slack = client.slack.user_mapping(
            slack_bot_token="slack_bot_token",
            slack_team_id="slack_team_id",
            slack_user_id="slack_user_id",
            slack_username="slack_username",
        )
        assert_matches_type(SlackUserMappingResponse, slack, path=["response"])

    @parametrize
    def test_raw_response_user_mapping(self, client: Structify) -> None:
        response = client.slack.with_raw_response.user_mapping(
            slack_bot_token="slack_bot_token",
            slack_team_id="slack_team_id",
            slack_user_id="slack_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = response.parse()
        assert_matches_type(SlackUserMappingResponse, slack, path=["response"])

    @parametrize
    def test_streaming_response_user_mapping(self, client: Structify) -> None:
        with client.slack.with_streaming_response.user_mapping(
            slack_bot_token="slack_bot_token",
            slack_team_id="slack_team_id",
            slack_user_id="slack_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = response.parse()
            assert_matches_type(SlackUserMappingResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSlack:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

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

    @parametrize
    async def test_method_user_mapping(self, async_client: AsyncStructify) -> None:
        slack = await async_client.slack.user_mapping(
            slack_bot_token="slack_bot_token",
            slack_team_id="slack_team_id",
            slack_user_id="slack_user_id",
        )
        assert_matches_type(SlackUserMappingResponse, slack, path=["response"])

    @parametrize
    async def test_method_user_mapping_with_all_params(self, async_client: AsyncStructify) -> None:
        slack = await async_client.slack.user_mapping(
            slack_bot_token="slack_bot_token",
            slack_team_id="slack_team_id",
            slack_user_id="slack_user_id",
            slack_username="slack_username",
        )
        assert_matches_type(SlackUserMappingResponse, slack, path=["response"])

    @parametrize
    async def test_raw_response_user_mapping(self, async_client: AsyncStructify) -> None:
        response = await async_client.slack.with_raw_response.user_mapping(
            slack_bot_token="slack_bot_token",
            slack_team_id="slack_team_id",
            slack_user_id="slack_user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = await response.parse()
        assert_matches_type(SlackUserMappingResponse, slack, path=["response"])

    @parametrize
    async def test_streaming_response_user_mapping(self, async_client: AsyncStructify) -> None:
        async with async_client.slack.with_streaming_response.user_mapping(
            slack_bot_token="slack_bot_token",
            slack_team_id="slack_team_id",
            slack_user_id="slack_user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = await response.parse()
            assert_matches_type(SlackUserMappingResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True
