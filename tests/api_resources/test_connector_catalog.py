# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import ConnectorCatalogWithMethods, ConnectorCatalogListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectorCatalog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        connector_catalog = client.connector_catalog.list()
        assert_matches_type(ConnectorCatalogListResponse, connector_catalog, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.connector_catalog.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector_catalog = response.parse()
        assert_matches_type(ConnectorCatalogListResponse, connector_catalog, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.connector_catalog.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector_catalog = response.parse()
            assert_matches_type(ConnectorCatalogListResponse, connector_catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        connector_catalog = client.connector_catalog.get(
            "slug",
        )
        assert_matches_type(ConnectorCatalogWithMethods, connector_catalog, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.connector_catalog.with_raw_response.get(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector_catalog = response.parse()
        assert_matches_type(ConnectorCatalogWithMethods, connector_catalog, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.connector_catalog.with_streaming_response.get(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector_catalog = response.parse()
            assert_matches_type(ConnectorCatalogWithMethods, connector_catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.connector_catalog.with_raw_response.get(
                "",
            )


class TestAsyncConnectorCatalog:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        connector_catalog = await async_client.connector_catalog.list()
        assert_matches_type(ConnectorCatalogListResponse, connector_catalog, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector_catalog = await response.parse()
        assert_matches_type(ConnectorCatalogListResponse, connector_catalog, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector_catalog = await response.parse()
            assert_matches_type(ConnectorCatalogListResponse, connector_catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        connector_catalog = await async_client.connector_catalog.get(
            "slug",
        )
        assert_matches_type(ConnectorCatalogWithMethods, connector_catalog, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.with_raw_response.get(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector_catalog = await response.parse()
        assert_matches_type(ConnectorCatalogWithMethods, connector_catalog, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.with_streaming_response.get(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector_catalog = await response.parse()
            assert_matches_type(ConnectorCatalogWithMethods, connector_catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.connector_catalog.with_raw_response.get(
                "",
            )
