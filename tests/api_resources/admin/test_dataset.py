# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.admin import AdminDatasetReturn

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_by_id(self, client: Structify) -> None:
        dataset = client.admin.dataset.get_by_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AdminDatasetReturn, dataset, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Structify) -> None:
        response = client.admin.dataset.with_raw_response.get_by_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(AdminDatasetReturn, dataset, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Structify) -> None:
        with client.admin.dataset.with_streaming_response.get_by_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(AdminDatasetReturn, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataset:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.admin.dataset.get_by_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AdminDatasetReturn, dataset, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.dataset.with_raw_response.get_by_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(AdminDatasetReturn, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.dataset.with_streaming_response.get_by_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(AdminDatasetReturn, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True
