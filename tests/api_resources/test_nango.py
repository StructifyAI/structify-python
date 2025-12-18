# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import NangoCreateSessionResponse, NangoListIntegrationsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNango:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_session(self, client: Structify) -> None:
        nango = client.nango.create_session()
        assert_matches_type(NangoCreateSessionResponse, nango, path=["response"])

    @parametrize
    def test_raw_response_create_session(self, client: Structify) -> None:
        response = client.nango.with_raw_response.create_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nango = response.parse()
        assert_matches_type(NangoCreateSessionResponse, nango, path=["response"])

    @parametrize
    def test_streaming_response_create_session(self, client: Structify) -> None:
        with client.nango.with_streaming_response.create_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nango = response.parse()
            assert_matches_type(NangoCreateSessionResponse, nango, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_integrations(self, client: Structify) -> None:
        nango = client.nango.list_integrations()
        assert_matches_type(NangoListIntegrationsResponse, nango, path=["response"])

    @parametrize
    def test_raw_response_list_integrations(self, client: Structify) -> None:
        response = client.nango.with_raw_response.list_integrations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nango = response.parse()
        assert_matches_type(NangoListIntegrationsResponse, nango, path=["response"])

    @parametrize
    def test_streaming_response_list_integrations(self, client: Structify) -> None:
        with client.nango.with_streaming_response.list_integrations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nango = response.parse()
            assert_matches_type(NangoListIntegrationsResponse, nango, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNango:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_session(self, async_client: AsyncStructify) -> None:
        nango = await async_client.nango.create_session()
        assert_matches_type(NangoCreateSessionResponse, nango, path=["response"])

    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncStructify) -> None:
        response = await async_client.nango.with_raw_response.create_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nango = await response.parse()
        assert_matches_type(NangoCreateSessionResponse, nango, path=["response"])

    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncStructify) -> None:
        async with async_client.nango.with_streaming_response.create_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nango = await response.parse()
            assert_matches_type(NangoCreateSessionResponse, nango, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_integrations(self, async_client: AsyncStructify) -> None:
        nango = await async_client.nango.list_integrations()
        assert_matches_type(NangoListIntegrationsResponse, nango, path=["response"])

    @parametrize
    async def test_raw_response_list_integrations(self, async_client: AsyncStructify) -> None:
        response = await async_client.nango.with_raw_response.list_integrations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nango = await response.parse()
        assert_matches_type(NangoListIntegrationsResponse, nango, path=["response"])

    @parametrize
    async def test_streaming_response_list_integrations(self, async_client: AsyncStructify) -> None:
        async with async_client.nango.with_streaming_response.list_integrations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nango = await response.parse()
            assert_matches_type(NangoListIntegrationsResponse, nango, path=["response"])

        assert cast(Any, response.is_closed) is True
