# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.pagination import SyncJobsList, AsyncJobsList
from structify.types.admin import AdminSandbox

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSandbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        sandbox = client.admin.sandbox.list()
        assert_matches_type(SyncJobsList[AdminSandbox], sandbox, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        sandbox = client.admin.sandbox.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncJobsList[AdminSandbox], sandbox, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.admin.sandbox.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SyncJobsList[AdminSandbox], sandbox, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.admin.sandbox.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SyncJobsList[AdminSandbox], sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSandbox:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        sandbox = await async_client.admin.sandbox.list()
        assert_matches_type(AsyncJobsList[AdminSandbox], sandbox, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        sandbox = await async_client.admin.sandbox.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncJobsList[AdminSandbox], sandbox, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.sandbox.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(AsyncJobsList[AdminSandbox], sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.sandbox.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(AsyncJobsList[AdminSandbox], sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True
