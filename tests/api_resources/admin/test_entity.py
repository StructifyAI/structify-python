# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import KnowledgeGraph

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_verify(self, client: Structify) -> None:
        entity = client.admin.entity.verify(
            dataset_name="dataset_name",
            kg={},
        )
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    def test_method_verify_with_all_params(self, client: Structify) -> None:
        entity = client.admin.entity.verify(
            dataset_name="dataset_name",
            kg={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ],
                "relationships": [
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                        "properties": {"foo": "string"},
                    }
                ],
            },
            fix=True,
        )
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    def test_raw_response_verify(self, client: Structify) -> None:
        response = client.admin.entity.with_raw_response.verify(
            dataset_name="dataset_name",
            kg={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    def test_streaming_response_verify(self, client: Structify) -> None:
        with client.admin.entity.with_streaming_response.verify(
            dataset_name="dataset_name",
            kg={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(KnowledgeGraph, entity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntity:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_verify(self, async_client: AsyncStructify) -> None:
        entity = await async_client.admin.entity.verify(
            dataset_name="dataset_name",
            kg={},
        )
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    async def test_method_verify_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.admin.entity.verify(
            dataset_name="dataset_name",
            kg={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ],
                "relationships": [
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                        "properties": {"foo": "string"},
                    }
                ],
            },
            fix=True,
        )
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.entity.with_raw_response.verify(
            dataset_name="dataset_name",
            kg={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.entity.with_streaming_response.verify(
            dataset_name="dataset_name",
            kg={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(KnowledgeGraph, entity, path=["response"])

        assert cast(Any, response.is_closed) is True
