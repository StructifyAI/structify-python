# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.connectors import Snippet

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTypeSnippets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_upsert(self, client: Structify) -> None:
        type_snippet = client.connectors.type_snippets.upsert(
            connector_type="connector_type",
        )
        assert_matches_type(Snippet, type_snippet, path=["response"])

    @parametrize
    def test_method_upsert_with_all_params(self, client: Structify) -> None:
        type_snippet = client.connectors.type_snippets.upsert(
            connector_type="connector_type",
            usage_snippet="usage_snippet",
        )
        assert_matches_type(Snippet, type_snippet, path=["response"])

    @parametrize
    def test_raw_response_upsert(self, client: Structify) -> None:
        response = client.connectors.type_snippets.with_raw_response.upsert(
            connector_type="connector_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type_snippet = response.parse()
        assert_matches_type(Snippet, type_snippet, path=["response"])

    @parametrize
    def test_streaming_response_upsert(self, client: Structify) -> None:
        with client.connectors.type_snippets.with_streaming_response.upsert(
            connector_type="connector_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type_snippet = response.parse()
            assert_matches_type(Snippet, type_snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upsert(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_type` but received ''"):
            client.connectors.type_snippets.with_raw_response.upsert(
                connector_type="",
            )


class TestAsyncTypeSnippets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_upsert(self, async_client: AsyncStructify) -> None:
        type_snippet = await async_client.connectors.type_snippets.upsert(
            connector_type="connector_type",
        )
        assert_matches_type(Snippet, type_snippet, path=["response"])

    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncStructify) -> None:
        type_snippet = await async_client.connectors.type_snippets.upsert(
            connector_type="connector_type",
            usage_snippet="usage_snippet",
        )
        assert_matches_type(Snippet, type_snippet, path=["response"])

    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncStructify) -> None:
        response = await async_client.connectors.type_snippets.with_raw_response.upsert(
            connector_type="connector_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        type_snippet = await response.parse()
        assert_matches_type(Snippet, type_snippet, path=["response"])

    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncStructify) -> None:
        async with async_client.connectors.type_snippets.with_streaming_response.upsert(
            connector_type="connector_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            type_snippet = await response.parse()
            assert_matches_type(Snippet, type_snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_type` but received ''"):
            await async_client.connectors.type_snippets.with_raw_response.upsert(
                connector_type="",
            )
