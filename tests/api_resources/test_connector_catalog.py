# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import ConnectorCatalogWithMethods, ConnectorCatalogListResponse
from structify._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectorCatalog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        connector_catalog = client.connector_catalog.list()
        assert_matches_type(ConnectorCatalogListResponse, connector_catalog, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        connector_catalog = client.connector_catalog.list(
            limit=0,
            offset=0,
            search="search",
        )
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_logo(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/connector-catalog/slug/logo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        connector_catalog = client.connector_catalog.get_logo(
            "slug",
        )
        assert connector_catalog.is_closed
        assert connector_catalog.json() == {"foo": "bar"}
        assert cast(Any, connector_catalog.is_closed) is True
        assert isinstance(connector_catalog, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_logo(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/connector-catalog/slug/logo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        connector_catalog = client.connector_catalog.with_raw_response.get_logo(
            "slug",
        )

        assert connector_catalog.is_closed is True
        assert connector_catalog.http_request.headers.get("X-Stainless-Lang") == "python"
        assert connector_catalog.json() == {"foo": "bar"}
        assert isinstance(connector_catalog, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_logo(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/connector-catalog/slug/logo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.connector_catalog.with_streaming_response.get_logo(
            "slug",
        ) as connector_catalog:
            assert not connector_catalog.is_closed
            assert connector_catalog.http_request.headers.get("X-Stainless-Lang") == "python"

            assert connector_catalog.json() == {"foo": "bar"}
            assert cast(Any, connector_catalog.is_closed) is True
            assert isinstance(connector_catalog, StreamedBinaryAPIResponse)

        assert cast(Any, connector_catalog.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_logo(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.connector_catalog.with_raw_response.get_logo(
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
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        connector_catalog = await async_client.connector_catalog.list(
            limit=0,
            offset=0,
            search="search",
        )
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_logo(self, async_client: AsyncStructify, respx_mock: MockRouter) -> None:
        respx_mock.get("/connector-catalog/slug/logo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        connector_catalog = await async_client.connector_catalog.get_logo(
            "slug",
        )
        assert connector_catalog.is_closed
        assert await connector_catalog.json() == {"foo": "bar"}
        assert cast(Any, connector_catalog.is_closed) is True
        assert isinstance(connector_catalog, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_logo(self, async_client: AsyncStructify, respx_mock: MockRouter) -> None:
        respx_mock.get("/connector-catalog/slug/logo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        connector_catalog = await async_client.connector_catalog.with_raw_response.get_logo(
            "slug",
        )

        assert connector_catalog.is_closed is True
        assert connector_catalog.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await connector_catalog.json() == {"foo": "bar"}
        assert isinstance(connector_catalog, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_logo(self, async_client: AsyncStructify, respx_mock: MockRouter) -> None:
        respx_mock.get("/connector-catalog/slug/logo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.connector_catalog.with_streaming_response.get_logo(
            "slug",
        ) as connector_catalog:
            assert not connector_catalog.is_closed
            assert connector_catalog.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await connector_catalog.json() == {"foo": "bar"}
            assert cast(Any, connector_catalog.is_closed) is True
            assert isinstance(connector_catalog, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, connector_catalog.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_logo(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.connector_catalog.with_raw_response.get_logo(
                "",
            )
