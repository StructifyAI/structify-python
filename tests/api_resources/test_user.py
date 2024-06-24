# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import NewToken, UserInfo

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_test_token(self, client: Structify) -> None:
        user = client.user.create_test_token()
        assert_matches_type(NewToken, user, path=["response"])

    @parametrize
    def test_raw_response_create_test_token(self, client: Structify) -> None:
        response = client.user.with_raw_response.create_test_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(NewToken, user, path=["response"])

    @parametrize
    def test_streaming_response_create_test_token(self, client: Structify) -> None:
        with client.user.with_streaming_response.create_test_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(NewToken, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_info(self, client: Structify) -> None:
        user = client.user.info()
        assert_matches_type(UserInfo, user, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Structify) -> None:
        response = client.user.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserInfo, user, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Structify) -> None:
        with client.user.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserInfo, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_test_token(self, async_client: AsyncStructify) -> None:
        user = await async_client.user.create_test_token()
        assert_matches_type(NewToken, user, path=["response"])

    @parametrize
    async def test_raw_response_create_test_token(self, async_client: AsyncStructify) -> None:
        response = await async_client.user.with_raw_response.create_test_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(NewToken, user, path=["response"])

    @parametrize
    async def test_streaming_response_create_test_token(self, async_client: AsyncStructify) -> None:
        async with async_client.user.with_streaming_response.create_test_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(NewToken, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_info(self, async_client: AsyncStructify) -> None:
        user = await async_client.user.info()
        assert_matches_type(UserInfo, user, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncStructify) -> None:
        response = await async_client.user.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserInfo, user, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncStructify) -> None:
        async with async_client.user.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserInfo, user, path=["response"])

        assert cast(Any, response.is_closed) is True
