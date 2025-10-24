# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify._utils import parse_datetime
from structify.pagination import SyncJobsList, AsyncJobsList
from structify.types.admin import (
    ExtendTrialResponse,
    GrantCreditsResponse,
    AdminTeamsListResponse,
    CancelSubscriptionResponse,
    CreateSubscriptionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        team = client.admin.teams.list()
        assert_matches_type(SyncJobsList[AdminTeamsListResponse], team, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        team = client.admin.teams.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncJobsList[AdminTeamsListResponse], team, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.admin.teams.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(SyncJobsList[AdminTeamsListResponse], team, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.admin.teams.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(SyncJobsList[AdminTeamsListResponse], team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel_subscription(self, client: Structify) -> None:
        team = client.admin.teams.cancel_subscription(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CancelSubscriptionResponse, team, path=["response"])

    @parametrize
    def test_raw_response_cancel_subscription(self, client: Structify) -> None:
        response = client.admin.teams.with_raw_response.cancel_subscription(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(CancelSubscriptionResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_cancel_subscription(self, client: Structify) -> None:
        with client.admin.teams.with_streaming_response.cancel_subscription(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(CancelSubscriptionResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_subscription(self, client: Structify) -> None:
        team = client.admin.teams.create_subscription(
            billing_interval="billing_interval",
            is_active=True,
            subscription_tier="free",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreateSubscriptionResponse, team, path=["response"])

    @parametrize
    def test_method_create_subscription_with_all_params(self, client: Structify) -> None:
        team = client.admin.teams.create_subscription(
            billing_interval="billing_interval",
            is_active=True,
            subscription_tier="free",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_customer_id="external_customer_id",
            external_price_id="external_price_id",
            external_subscription_id="external_subscription_id",
        )
        assert_matches_type(CreateSubscriptionResponse, team, path=["response"])

    @parametrize
    def test_raw_response_create_subscription(self, client: Structify) -> None:
        response = client.admin.teams.with_raw_response.create_subscription(
            billing_interval="billing_interval",
            is_active=True,
            subscription_tier="free",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(CreateSubscriptionResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_create_subscription(self, client: Structify) -> None:
        with client.admin.teams.with_streaming_response.create_subscription(
            billing_interval="billing_interval",
            is_active=True,
            subscription_tier="free",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(CreateSubscriptionResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_extend_trial(self, client: Structify) -> None:
        team = client.admin.teams.extend_trial(
            new_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtendTrialResponse, team, path=["response"])

    @parametrize
    def test_raw_response_extend_trial(self, client: Structify) -> None:
        response = client.admin.teams.with_raw_response.extend_trial(
            new_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(ExtendTrialResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_extend_trial(self, client: Structify) -> None:
        with client.admin.teams.with_streaming_response.extend_trial(
            new_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(ExtendTrialResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_grant_credits(self, client: Structify) -> None:
        team = client.admin.teams.grant_credits(
            amount=0,
            source_type="source_type",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GrantCreditsResponse, team, path=["response"])

    @parametrize
    def test_method_grant_credits_with_all_params(self, client: Structify) -> None:
        team = client.admin.teams.grant_credits(
            amount=0,
            source_type="source_type",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            source_ref="source_ref",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GrantCreditsResponse, team, path=["response"])

    @parametrize
    def test_raw_response_grant_credits(self, client: Structify) -> None:
        response = client.admin.teams.with_raw_response.grant_credits(
            amount=0,
            source_type="source_type",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(GrantCreditsResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_grant_credits(self, client: Structify) -> None:
        with client.admin.teams.with_streaming_response.grant_credits(
            amount=0,
            source_type="source_type",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(GrantCreditsResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTeams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        team = await async_client.admin.teams.list()
        assert_matches_type(AsyncJobsList[AdminTeamsListResponse], team, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        team = await async_client.admin.teams.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncJobsList[AdminTeamsListResponse], team, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.teams.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(AsyncJobsList[AdminTeamsListResponse], team, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.teams.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(AsyncJobsList[AdminTeamsListResponse], team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel_subscription(self, async_client: AsyncStructify) -> None:
        team = await async_client.admin.teams.cancel_subscription(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CancelSubscriptionResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_cancel_subscription(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.teams.with_raw_response.cancel_subscription(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(CancelSubscriptionResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_cancel_subscription(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.teams.with_streaming_response.cancel_subscription(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(CancelSubscriptionResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_subscription(self, async_client: AsyncStructify) -> None:
        team = await async_client.admin.teams.create_subscription(
            billing_interval="billing_interval",
            is_active=True,
            subscription_tier="free",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreateSubscriptionResponse, team, path=["response"])

    @parametrize
    async def test_method_create_subscription_with_all_params(self, async_client: AsyncStructify) -> None:
        team = await async_client.admin.teams.create_subscription(
            billing_interval="billing_interval",
            is_active=True,
            subscription_tier="free",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_customer_id="external_customer_id",
            external_price_id="external_price_id",
            external_subscription_id="external_subscription_id",
        )
        assert_matches_type(CreateSubscriptionResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_create_subscription(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.teams.with_raw_response.create_subscription(
            billing_interval="billing_interval",
            is_active=True,
            subscription_tier="free",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(CreateSubscriptionResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_create_subscription(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.teams.with_streaming_response.create_subscription(
            billing_interval="billing_interval",
            is_active=True,
            subscription_tier="free",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(CreateSubscriptionResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_extend_trial(self, async_client: AsyncStructify) -> None:
        team = await async_client.admin.teams.extend_trial(
            new_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtendTrialResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_extend_trial(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.teams.with_raw_response.extend_trial(
            new_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(ExtendTrialResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_extend_trial(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.teams.with_streaming_response.extend_trial(
            new_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(ExtendTrialResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_grant_credits(self, async_client: AsyncStructify) -> None:
        team = await async_client.admin.teams.grant_credits(
            amount=0,
            source_type="source_type",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GrantCreditsResponse, team, path=["response"])

    @parametrize
    async def test_method_grant_credits_with_all_params(self, async_client: AsyncStructify) -> None:
        team = await async_client.admin.teams.grant_credits(
            amount=0,
            source_type="source_type",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            source_ref="source_ref",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GrantCreditsResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_grant_credits(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.teams.with_raw_response.grant_credits(
            amount=0,
            source_type="source_type",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(GrantCreditsResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_grant_credits(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.teams.with_streaming_response.grant_credits(
            amount=0,
            source_type="source_type",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(GrantCreditsResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True
