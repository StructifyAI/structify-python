# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    EntityAddResponse,
    EntityGetResponse,
    EntityMergeResponse,
    EntityGetLocalSubgraphResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add(self, client: Structify) -> None:
        entity = client.entities.add(
            dataset_name="dataset_name",
            kg={},
        )
        assert_matches_type(EntityAddResponse, entity, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Structify) -> None:
        entity = client.entities.add(
            dataset_name="dataset_name",
            kg={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    },
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    },
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    },
                ],
                "relationships": [
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                        "properties": {"foo": "string"},
                    },
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                        "properties": {"foo": "string"},
                    },
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                        "properties": {"foo": "string"},
                    },
                ],
            },
            source_website="source_website",
        )
        assert_matches_type(EntityAddResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Structify) -> None:
        response = client.entities.with_raw_response.add(
            dataset_name="dataset_name",
            kg={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityAddResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Structify) -> None:
        with client.entities.with_streaming_response.add(
            dataset_name="dataset_name",
            kg={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityAddResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        entity = client.entities.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.entities.with_raw_response.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.entities.with_streaming_response.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityGetResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_local_subgraph(self, client: Structify) -> None:
        entity = client.entities.get_local_subgraph(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityGetLocalSubgraphResponse, entity, path=["response"])

    @parametrize
    def test_method_get_local_subgraph_with_all_params(self, client: Structify) -> None:
        entity = client.entities.get_local_subgraph(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            radius=0,
        )
        assert_matches_type(EntityGetLocalSubgraphResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_get_local_subgraph(self, client: Structify) -> None:
        response = client.entities.with_raw_response.get_local_subgraph(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityGetLocalSubgraphResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_get_local_subgraph(self, client: Structify) -> None:
        with client.entities.with_streaming_response.get_local_subgraph(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityGetLocalSubgraphResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_merge(self, client: Structify) -> None:
        entity = client.entities.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityMergeResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_merge(self, client: Structify) -> None:
        response = client.entities.with_raw_response.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityMergeResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_merge(self, client: Structify) -> None:
        with client.entities.with_streaming_response.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityMergeResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_add(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.add(
            dataset_name="dataset_name",
            kg={},
        )
        assert_matches_type(EntityAddResponse, entity, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.add(
            dataset_name="dataset_name",
            kg={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    },
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    },
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    },
                ],
                "relationships": [
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                        "properties": {"foo": "string"},
                    },
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                        "properties": {"foo": "string"},
                    },
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                        "properties": {"foo": "string"},
                    },
                ],
            },
            source_website="source_website",
        )
        assert_matches_type(EntityAddResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.add(
            dataset_name="dataset_name",
            kg={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityAddResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.add(
            dataset_name="dataset_name",
            kg={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityAddResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityGetResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_local_subgraph(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.get_local_subgraph(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityGetLocalSubgraphResponse, entity, path=["response"])

    @parametrize
    async def test_method_get_local_subgraph_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.get_local_subgraph(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            radius=0,
        )
        assert_matches_type(EntityGetLocalSubgraphResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_get_local_subgraph(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.get_local_subgraph(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityGetLocalSubgraphResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_get_local_subgraph(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.get_local_subgraph(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityGetLocalSubgraphResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_merge(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityMergeResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityMergeResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityMergeResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True
