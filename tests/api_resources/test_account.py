# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import NewToken, UserInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_test_token(self, client: Structify) -> None:
        account = client.account.create_test_token()
        assert_matches_type(NewToken, account, path=["response"])

    @parametrize
    def test_raw_response_create_test_token(self, client: Structify) -> None:
        response = client.account.with_raw_response.create_test_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(NewToken, account, path=["response"])

    @parametrize
    def test_streaming_response_create_test_token(self, client: Structify) -> None:
        with client.account.with_streaming_response.create_test_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(NewToken, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_info(self, client: Structify) -> None:
        account = client.account.info()
        assert_matches_type(UserInfoResponse, account, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Structify) -> None:
        response = client.account.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(UserInfoResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Structify) -> None:
        with client.account.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(UserInfoResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccount:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_test_token(self, async_client: AsyncStructify) -> None:
        account = await async_client.account.create_test_token()
        assert_matches_type(NewToken, account, path=["response"])

    @parametrize
    async def test_raw_response_create_test_token(self, async_client: AsyncStructify) -> None:
        response = await async_client.account.with_raw_response.create_test_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(NewToken, account, path=["response"])

    @parametrize
    async def test_streaming_response_create_test_token(self, async_client: AsyncStructify) -> None:
        async with async_client.account.with_streaming_response.create_test_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(NewToken, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_info(self, async_client: AsyncStructify) -> None:
        account = await async_client.account.info()
        assert_matches_type(UserInfoResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncStructify) -> None:
        response = await async_client.account.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(UserInfoResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncStructify) -> None:
        async with async_client.account.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(UserInfoResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
