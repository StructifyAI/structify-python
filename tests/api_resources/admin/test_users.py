# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import TokenResponse
from structify._utils import parse_datetime
from structify.types.admin import (
    User,
    UserListResponse,
    UserGetStatsResponse,
    UserGetCreditsResponse,
    UserSetCreditsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        user = client.admin.users.create()
        assert_matches_type(TokenResponse, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Structify) -> None:
        user = client.admin.users.create(
            credit_count=0,
            email="email",
            feature_flags=["functional_test"],
            is_admin=True,
            permissions=["labeler"],
            test=True,
        )
        assert_matches_type(TokenResponse, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.admin.users.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(TokenResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.admin.users.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(TokenResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Structify) -> None:
        user = client.admin.users.update(
            current_email="current_email",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Structify) -> None:
        user = client.admin.users.update(
            current_email="current_email",
            new_email="new_email",
            new_feature_flags=["functional_test"],
            new_permissions=["labeler"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Structify) -> None:
        response = client.admin.users.with_raw_response.update(
            current_email="current_email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Structify) -> None:
        with client.admin.users.with_streaming_response.update(
            current_email="current_email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        user = client.admin.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.admin.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.admin.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_credits(self, client: Structify) -> None:
        user = client.admin.users.get_credits()
        assert_matches_type(UserGetCreditsResponse, user, path=["response"])

    @parametrize
    def test_method_get_credits_with_all_params(self, client: Structify) -> None:
        user = client.admin.users.get_credits(
            user_email="user_email",
            user_token="user_token",
        )
        assert_matches_type(UserGetCreditsResponse, user, path=["response"])

    @parametrize
    def test_raw_response_get_credits(self, client: Structify) -> None:
        response = client.admin.users.with_raw_response.get_credits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetCreditsResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_get_credits(self, client: Structify) -> None:
        with client.admin.users.with_streaming_response.get_credits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserGetCreditsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_stats(self, client: Structify) -> None:
        user = client.admin.users.get_stats()
        assert_matches_type(UserGetStatsResponse, user, path=["response"])

    @parametrize
    def test_method_get_stats_with_all_params(self, client: Structify) -> None:
        user = client.admin.users.get_stats(
            bucket="Second",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            user_email="user_email",
            user_token="user_token",
        )
        assert_matches_type(UserGetStatsResponse, user, path=["response"])

    @parametrize
    def test_raw_response_get_stats(self, client: Structify) -> None:
        response = client.admin.users.with_raw_response.get_stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetStatsResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_get_stats(self, client: Structify) -> None:
        with client.admin.users.with_streaming_response.get_stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserGetStatsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_credits(self, client: Structify) -> None:
        user = client.admin.users.set_credits(
            credit_count=0,
            user_email="user_email",
        )
        assert_matches_type(UserSetCreditsResponse, user, path=["response"])

    @parametrize
    def test_raw_response_set_credits(self, client: Structify) -> None:
        response = client.admin.users.with_raw_response.set_credits(
            credit_count=0,
            user_email="user_email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserSetCreditsResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_set_credits(self, client: Structify) -> None:
        with client.admin.users.with_streaming_response.set_credits(
            credit_count=0,
            user_email="user_email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserSetCreditsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        user = await async_client.admin.users.create()
        assert_matches_type(TokenResponse, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStructify) -> None:
        user = await async_client.admin.users.create(
            credit_count=0,
            email="email",
            feature_flags=["functional_test"],
            is_admin=True,
            permissions=["labeler"],
            test=True,
        )
        assert_matches_type(TokenResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.users.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(TokenResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.users.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(TokenResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncStructify) -> None:
        user = await async_client.admin.users.update(
            current_email="current_email",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStructify) -> None:
        user = await async_client.admin.users.update(
            current_email="current_email",
            new_email="new_email",
            new_feature_flags=["functional_test"],
            new_permissions=["labeler"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.users.with_raw_response.update(
            current_email="current_email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.users.with_streaming_response.update(
            current_email="current_email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        user = await async_client.admin.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_credits(self, async_client: AsyncStructify) -> None:
        user = await async_client.admin.users.get_credits()
        assert_matches_type(UserGetCreditsResponse, user, path=["response"])

    @parametrize
    async def test_method_get_credits_with_all_params(self, async_client: AsyncStructify) -> None:
        user = await async_client.admin.users.get_credits(
            user_email="user_email",
            user_token="user_token",
        )
        assert_matches_type(UserGetCreditsResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_get_credits(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.users.with_raw_response.get_credits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetCreditsResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_get_credits(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.users.with_streaming_response.get_credits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserGetCreditsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_stats(self, async_client: AsyncStructify) -> None:
        user = await async_client.admin.users.get_stats()
        assert_matches_type(UserGetStatsResponse, user, path=["response"])

    @parametrize
    async def test_method_get_stats_with_all_params(self, async_client: AsyncStructify) -> None:
        user = await async_client.admin.users.get_stats(
            bucket="Second",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            user_email="user_email",
            user_token="user_token",
        )
        assert_matches_type(UserGetStatsResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_get_stats(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.users.with_raw_response.get_stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetStatsResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_get_stats(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.users.with_streaming_response.get_stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserGetStatsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_credits(self, async_client: AsyncStructify) -> None:
        user = await async_client.admin.users.set_credits(
            credit_count=0,
            user_email="user_email",
        )
        assert_matches_type(UserSetCreditsResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_set_credits(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.users.with_raw_response.set_credits(
            credit_count=0,
            user_email="user_email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserSetCreditsResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_set_credits(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.users.with_streaming_response.set_credits(
            credit_count=0,
            user_email="user_email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserSetCreditsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
