# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import ExternalSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_search(self, client: Structify) -> None:
        external = client.external.search(
            query="query",
        )
        assert_matches_type(ExternalSearchResponse, external, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Structify) -> None:
        response = client.external.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = response.parse()
        assert_matches_type(ExternalSearchResponse, external, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Structify) -> None:
        with client.external.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = response.parse()
            assert_matches_type(ExternalSearchResponse, external, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExternal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_search(self, async_client: AsyncStructify) -> None:
        external = await async_client.external.search(
            query="query",
        )
        assert_matches_type(ExternalSearchResponse, external, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = await response.parse()
        assert_matches_type(ExternalSearchResponse, external, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncStructify) -> None:
        async with async_client.external.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = await response.parse()
            assert_matches_type(ExternalSearchResponse, external, path=["response"])

        assert cast(Any, response.is_closed) is True
