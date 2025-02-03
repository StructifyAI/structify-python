# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    KnowledgeGraph,
    EntityAddResponse,
    EntityGetResponse,
    EntityViewResponse,
    EntityMergeResponse,
    EntityDeleteResponse,
    EntitySearchResponse,
    EntityAddBatchResponse,
    EntityListJobsResponse,
    EntitySummarizeResponse,
    EntityTriggerMergeResponse,
    EntityUpdatePropertyResponse,
    EntityGetLocalSubgraphResponse,
    EntityGetSourceEntitiesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        entity = client.entities.delete(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityDeleteResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.entities.with_raw_response.delete(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityDeleteResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.entities.with_streaming_response.delete(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityDeleteResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            attempt_merge=True,
            source="None",
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
    def test_method_add_batch(self, client: Structify) -> None:
        entity = client.entities.add_batch(
            dataset_name="dataset_name",
            kgs=[{}],
        )
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    def test_method_add_batch_with_all_params(self, client: Structify) -> None:
        entity = client.entities.add_batch(
            dataset_name="dataset_name",
            kgs=[
                {
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
                }
            ],
            attempt_merge=True,
            source="None",
        )
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_add_batch(self, client: Structify) -> None:
        response = client.entities.with_raw_response.add_batch(
            dataset_name="dataset_name",
            kgs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_add_batch(self, client: Structify) -> None:
        with client.entities.with_streaming_response.add_batch(
            dataset_name="dataset_name",
            kgs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        entity = client.entities.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Structify) -> None:
        entity = client.entities.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolve_id=True,
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
    def test_method_get_source_entities(self, client: Structify) -> None:
        entity = client.entities.get_source_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityGetSourceEntitiesResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_get_source_entities(self, client: Structify) -> None:
        response = client.entities.with_raw_response.get_source_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityGetSourceEntitiesResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_get_source_entities(self, client: Structify) -> None:
        with client.entities.with_streaming_response.get_source_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityGetSourceEntitiesResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_jobs(self, client: Structify) -> None:
        entity = client.entities.list_jobs(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityListJobsResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_list_jobs(self, client: Structify) -> None:
        response = client.entities.with_raw_response.list_jobs(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityListJobsResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_list_jobs(self, client: Structify) -> None:
        with client.entities.with_streaming_response.list_jobs(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityListJobsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_merge(self, client: Structify) -> None:
        entity = client.entities.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityMergeResponse, entity, path=["response"])

    @parametrize
    def test_method_merge_with_all_params(self, client: Structify) -> None:
        entity = client.entities.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            debug=True,
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

    @parametrize
    def test_method_search(self, client: Structify) -> None:
        entity = client.entities.search(
            dataset_name="dataset_name",
            query="query",
            table_name="table_name",
        )
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Structify) -> None:
        response = client.entities.with_raw_response.search(
            dataset_name="dataset_name",
            query="query",
            table_name="table_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Structify) -> None:
        with client.entities.with_streaming_response.search(
            dataset_name="dataset_name",
            query="query",
            table_name="table_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntitySearchResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_summarize(self, client: Structify) -> None:
        entity = client.entities.summarize(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
        )
        assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

    @parametrize
    def test_method_summarize_with_all_params(self, client: Structify) -> None:
        entity = client.entities.summarize(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
            extra_instructions=["string"],
        )
        assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_summarize(self, client: Structify) -> None:
        response = client.entities.with_raw_response.summarize(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_summarize(self, client: Structify) -> None:
        with client.entities.with_streaming_response.summarize(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_trigger_merge(self, client: Structify) -> None:
        entity = client.entities.trigger_merge(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityTriggerMergeResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_trigger_merge(self, client: Structify) -> None:
        response = client.entities.with_raw_response.trigger_merge(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityTriggerMergeResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_trigger_merge(self, client: Structify) -> None:
        with client.entities.with_streaming_response.trigger_merge(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityTriggerMergeResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_property(self, client: Structify) -> None:
        entity = client.entities.update_property(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prop_name="prop_name",
            prop_value="string",
        )
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    def test_method_update_property_with_all_params(self, client: Structify) -> None:
        entity = client.entities.update_property(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prop_name="prop_name",
            prop_value="string",
            source="None",
        )
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_update_property(self, client: Structify) -> None:
        response = client.entities.with_raw_response.update_property(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prop_name="prop_name",
            prop_value="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_update_property(self, client: Structify) -> None:
        with client.entities.with_streaming_response.update_property(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prop_name="prop_name",
            prop_value="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_verify(self, client: Structify) -> None:
        entity = client.entities.verify(
            dataset_name="dataset_name",
            kg={},
        )
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    def test_method_verify_with_all_params(self, client: Structify) -> None:
        entity = client.entities.verify(
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
        response = client.entities.with_raw_response.verify(
            dataset_name="dataset_name",
            kg={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    def test_streaming_response_verify(self, client: Structify) -> None:
        with client.entities.with_streaming_response.verify(
            dataset_name="dataset_name",
            kg={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(KnowledgeGraph, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_view(self, client: Structify) -> None:
        entity = client.entities.view(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityViewResponse, entity, path=["response"])

    @parametrize
    def test_method_view_with_all_params(self, client: Structify) -> None:
        entity = client.entities.view(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolve_id=True,
        )
        assert_matches_type(EntityViewResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_view(self, client: Structify) -> None:
        response = client.entities.with_raw_response.view(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityViewResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_view(self, client: Structify) -> None:
        with client.entities.with_streaming_response.view(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityViewResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.delete(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityDeleteResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.delete(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityDeleteResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.delete(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityDeleteResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            attempt_merge=True,
            source="None",
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
    async def test_method_add_batch(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.add_batch(
            dataset_name="dataset_name",
            kgs=[{}],
        )
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    async def test_method_add_batch_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.add_batch(
            dataset_name="dataset_name",
            kgs=[
                {
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
                }
            ],
            attempt_merge=True,
            source="None",
        )
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_add_batch(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.add_batch(
            dataset_name="dataset_name",
            kgs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_add_batch(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.add_batch(
            dataset_name="dataset_name",
            kgs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolve_id=True,
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
    async def test_method_get_source_entities(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.get_source_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityGetSourceEntitiesResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_get_source_entities(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.get_source_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityGetSourceEntitiesResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_get_source_entities(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.get_source_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityGetSourceEntitiesResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_jobs(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.list_jobs(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityListJobsResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_list_jobs(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.list_jobs(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityListJobsResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_list_jobs(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.list_jobs(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityListJobsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_merge(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityMergeResponse, entity, path=["response"])

    @parametrize
    async def test_method_merge_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            debug=True,
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

    @parametrize
    async def test_method_search(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.search(
            dataset_name="dataset_name",
            query="query",
            table_name="table_name",
        )
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.search(
            dataset_name="dataset_name",
            query="query",
            table_name="table_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.search(
            dataset_name="dataset_name",
            query="query",
            table_name="table_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntitySearchResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_summarize(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.summarize(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
        )
        assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.summarize(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
            extra_instructions=["string"],
        )
        assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.summarize(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.summarize(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_trigger_merge(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.trigger_merge(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityTriggerMergeResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_trigger_merge(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.trigger_merge(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityTriggerMergeResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_trigger_merge(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.trigger_merge(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityTriggerMergeResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_property(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.update_property(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prop_name="prop_name",
            prop_value="string",
        )
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    async def test_method_update_property_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.update_property(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prop_name="prop_name",
            prop_value="string",
            source="None",
        )
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_update_property(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.update_property(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prop_name="prop_name",
            prop_value="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_update_property(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.update_property(
            dataset_name="dataset_name",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prop_name="prop_name",
            prop_value="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_verify(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.verify(
            dataset_name="dataset_name",
            kg={},
        )
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    async def test_method_verify_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.verify(
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
        response = await async_client.entities.with_raw_response.verify(
            dataset_name="dataset_name",
            kg={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.verify(
            dataset_name="dataset_name",
            kg={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(KnowledgeGraph, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_view(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.view(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityViewResponse, entity, path=["response"])

    @parametrize
    async def test_method_view_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.view(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolve_id=True,
        )
        assert_matches_type(EntityViewResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_view(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.view(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityViewResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_view(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.view(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityViewResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True
