# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.user import (
    CreateSessionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStripe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_session(self, client: Structify) -> None:
        stripe = client.user.stripe.create_session(
            credits=0,
            origin="origin",
        )
        assert_matches_type(CreateSessionResponse, stripe, path=["response"])

    @parametrize
    def test_raw_response_create_session(self, client: Structify) -> None:
        response = client.user.stripe.with_raw_response.create_session(
            credits=0,
            origin="origin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = response.parse()
        assert_matches_type(CreateSessionResponse, stripe, path=["response"])

    @parametrize
    def test_streaming_response_create_session(self, client: Structify) -> None:
        with client.user.stripe.with_streaming_response.create_session(
            credits=0,
            origin="origin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = response.parse()
            assert_matches_type(CreateSessionResponse, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_subscription(self, client: Structify) -> None:
        stripe = client.user.stripe.create_subscription(
            origin="origin",
            plan="Pro",
        )
        assert_matches_type(CreateSessionResponse, stripe, path=["response"])

    @parametrize
    def test_raw_response_create_subscription(self, client: Structify) -> None:
        response = client.user.stripe.with_raw_response.create_subscription(
            origin="origin",
            plan="Pro",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = response.parse()
        assert_matches_type(CreateSessionResponse, stripe, path=["response"])

    @parametrize
    def test_streaming_response_create_subscription(self, client: Structify) -> None:
        with client.user.stripe.with_streaming_response.create_subscription(
            origin="origin",
            plan="Pro",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = response.parse()
            assert_matches_type(CreateSessionResponse, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStripe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_session(self, async_client: AsyncStructify) -> None:
        stripe = await async_client.user.stripe.create_session(
            credits=0,
            origin="origin",
        )
        assert_matches_type(CreateSessionResponse, stripe, path=["response"])

    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncStructify) -> None:
        response = await async_client.user.stripe.with_raw_response.create_session(
            credits=0,
            origin="origin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = await response.parse()
        assert_matches_type(CreateSessionResponse, stripe, path=["response"])

    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncStructify) -> None:
        async with async_client.user.stripe.with_streaming_response.create_session(
            credits=0,
            origin="origin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = await response.parse()
            assert_matches_type(CreateSessionResponse, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_subscription(self, async_client: AsyncStructify) -> None:
        stripe = await async_client.user.stripe.create_subscription(
            origin="origin",
            plan="Pro",
        )
        assert_matches_type(CreateSessionResponse, stripe, path=["response"])

    @parametrize
    async def test_raw_response_create_subscription(self, async_client: AsyncStructify) -> None:
        response = await async_client.user.stripe.with_raw_response.create_subscription(
            origin="origin",
            plan="Pro",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = await response.parse()
        assert_matches_type(CreateSessionResponse, stripe, path=["response"])

    @parametrize
    async def test_streaming_response_create_subscription(self, async_client: AsyncStructify) -> None:
        async with async_client.user.stripe.with_streaming_response.create_subscription(
            origin="origin",
            plan="Pro",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = await response.parse()
            assert_matches_type(CreateSessionResponse, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True
