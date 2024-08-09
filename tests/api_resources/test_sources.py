# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import SourceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        source = client.sources.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        source = client.sources.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property="property",
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.sources.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.sources.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSources:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        source = await async_client.sources.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        source = await async_client.sources.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property="property",
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.sources.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.sources.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True
