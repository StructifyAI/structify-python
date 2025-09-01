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
    EntityGetMergesResponse,
    EntitySummarizeResponse,
    EntityAgentMergeResponse,
    EntityTriggerMergeResponse,
    EntityUpdatePropertyResponse,
    EntityAddRelationshipResponse,
    EntityGetLocalSubgraphResponse,
    EntityGetSourceEntitiesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        entity = client.entities.delete(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityDeleteResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.entities.with_raw_response.delete(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityDeleteResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.entities.with_streaming_response.delete(
            dataset="dataset",
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
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
        )
        assert_matches_type(EntityAddResponse, entity, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Structify) -> None:
        entity = client.entities.add(
            dataset="dataset",
            entity_graph={
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
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityAddResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Structify) -> None:
        with client.entities.with_streaming_response.add(
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityAddResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_batch(self, client: Structify) -> None:
        entity = client.entities.add_batch(
            dataset="dataset",
            entity_graphs=[
                {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                }
            ],
        )
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    def test_method_add_batch_with_all_params(self, client: Structify) -> None:
        entity = client.entities.add_batch(
            dataset="dataset",
            entity_graphs=[
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
            skip_malformed_entities=True,
            source="None",
        )
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_add_batch(self, client: Structify) -> None:
        response = client.entities.with_raw_response.add_batch(
            dataset="dataset",
            entity_graphs=[
                {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_add_batch(self, client: Structify) -> None:
        with client.entities.with_streaming_response.add_batch(
            dataset="dataset",
            entity_graphs=[
                {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_relationship(self, client: Structify) -> None:
        entity = client.entities.add_relationship(
            dataset="dataset",
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_type="relationship_type",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityAddRelationshipResponse, entity, path=["response"])

    @parametrize
    def test_method_add_relationship_with_all_params(self, client: Structify) -> None:
        entity = client.entities.add_relationship(
            dataset="dataset",
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_type="relationship_type",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "string"},
        )
        assert_matches_type(EntityAddRelationshipResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_add_relationship(self, client: Structify) -> None:
        response = client.entities.with_raw_response.add_relationship(
            dataset="dataset",
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_type="relationship_type",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityAddRelationshipResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_add_relationship(self, client: Structify) -> None:
        with client.entities.with_streaming_response.add_relationship(
            dataset="dataset",
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_type="relationship_type",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityAddRelationshipResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_agent_merge(self, client: Structify) -> None:
        entity = client.entities.agent_merge(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityAgentMergeResponse, entity, path=["response"])

    @parametrize
    def test_method_agent_merge_with_all_params(self, client: Structify) -> None:
        entity = client.entities.agent_merge(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            force_consider_entities=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            top_k=0,
        )
        assert_matches_type(EntityAgentMergeResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_agent_merge(self, client: Structify) -> None:
        response = client.entities.with_raw_response.agent_merge(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityAgentMergeResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_agent_merge(self, client: Structify) -> None:
        with client.entities.with_streaming_response.agent_merge(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityAgentMergeResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_relationship(self, client: Structify) -> None:
        entity = client.entities.delete_relationship(
            dataset="dataset",
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, entity, path=["response"])

    @parametrize
    def test_raw_response_delete_relationship(self, client: Structify) -> None:
        response = client.entities.with_raw_response.delete_relationship(
            dataset="dataset",
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(object, entity, path=["response"])

    @parametrize
    def test_streaming_response_delete_relationship(self, client: Structify) -> None:
        with client.entities.with_streaming_response.delete_relationship(
            dataset="dataset",
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(object, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_derive(self, client: Structify) -> None:
        entity = client.entities.derive(
            dataset="dataset",
            derived_property="derived_property",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            instructions="instructions",
        )
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    def test_method_derive_with_all_params(self, client: Structify) -> None:
        entity = client.entities.derive(
            dataset="dataset",
            derived_property="derived_property",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            instructions="instructions",
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    def test_raw_response_derive(self, client: Structify) -> None:
        response = client.entities.with_raw_response.derive(
            dataset="dataset",
            derived_property="derived_property",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            instructions="instructions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    def test_streaming_response_derive(self, client: Structify) -> None:
        with client.entities.with_streaming_response.derive(
            dataset="dataset",
            derived_property="derived_property",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            instructions="instructions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(str, entity, path=["response"])

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

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
    @parametrize
    def test_method_get_merges(self, client: Structify) -> None:
        entity = client.entities.get_merges(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityGetMergesResponse, entity, path=["response"])

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
    @parametrize
    def test_raw_response_get_merges(self, client: Structify) -> None:
        response = client.entities.with_raw_response.get_merges(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityGetMergesResponse, entity, path=["response"])

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
    @parametrize
    def test_streaming_response_get_merges(self, client: Structify) -> None:
        with client.entities.with_streaming_response.get_merges(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityGetMergesResponse, entity, path=["response"])

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

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
    @parametrize
    def test_method_merge(self, client: Structify) -> None:
        entity = client.entities.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityMergeResponse, entity, path=["response"])

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
    @parametrize
    def test_method_merge_with_all_params(self, client: Structify) -> None:
        entity = client.entities.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            debug=True,
        )
        assert_matches_type(EntityMergeResponse, entity, path=["response"])

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
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

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
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
            dataset="dataset",
            query="query",
            table_name="table_name",
        )
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Structify) -> None:
        response = client.entities.with_raw_response.search(
            dataset="dataset",
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
            dataset="dataset",
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
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
        )
        assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

    @parametrize
    def test_method_summarize_with_all_params(self, client: Structify) -> None:
        entity = client.entities.summarize(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
            extra_instructions=["string"],
        )
        assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_summarize(self, client: Structify) -> None:
        response = client.entities.with_raw_response.summarize(
            dataset="dataset",
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
            dataset="dataset",
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
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "string"},
        )
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    def test_method_update_property_with_all_params(self, client: Structify) -> None:
        entity = client.entities.update_property(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "string"},
            source="None",
        )
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_update_property(self, client: Structify) -> None:
        response = client.entities.with_raw_response.update_property(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_update_property(self, client: Structify) -> None:
        with client.entities.with_streaming_response.update_property(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_verify(self, client: Structify) -> None:
        entity = client.entities.verify(
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
        )
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    def test_method_verify_with_all_params(self, client: Structify) -> None:
        entity = client.entities.verify(
            dataset="dataset",
            entity_graph={
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
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    def test_streaming_response_verify(self, client: Structify) -> None:
        with client.entities.with_streaming_response.verify(
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
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
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.delete(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityDeleteResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.delete(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityDeleteResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.delete(
            dataset="dataset",
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
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
        )
        assert_matches_type(EntityAddResponse, entity, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.add(
            dataset="dataset",
            entity_graph={
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
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityAddResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.add(
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityAddResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_batch(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.add_batch(
            dataset="dataset",
            entity_graphs=[
                {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                }
            ],
        )
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    async def test_method_add_batch_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.add_batch(
            dataset="dataset",
            entity_graphs=[
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
            skip_malformed_entities=True,
            source="None",
        )
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_add_batch(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.add_batch(
            dataset="dataset",
            entity_graphs=[
                {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_add_batch(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.add_batch(
            dataset="dataset",
            entity_graphs=[
                {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityAddBatchResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_relationship(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.add_relationship(
            dataset="dataset",
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_type="relationship_type",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityAddRelationshipResponse, entity, path=["response"])

    @parametrize
    async def test_method_add_relationship_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.add_relationship(
            dataset="dataset",
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_type="relationship_type",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "string"},
        )
        assert_matches_type(EntityAddRelationshipResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_add_relationship(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.add_relationship(
            dataset="dataset",
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_type="relationship_type",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityAddRelationshipResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_add_relationship(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.add_relationship(
            dataset="dataset",
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_type="relationship_type",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityAddRelationshipResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_agent_merge(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.agent_merge(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityAgentMergeResponse, entity, path=["response"])

    @parametrize
    async def test_method_agent_merge_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.agent_merge(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            force_consider_entities=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            top_k=0,
        )
        assert_matches_type(EntityAgentMergeResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_agent_merge(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.agent_merge(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityAgentMergeResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_agent_merge(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.agent_merge(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityAgentMergeResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_relationship(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.delete_relationship(
            dataset="dataset",
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, entity, path=["response"])

    @parametrize
    async def test_raw_response_delete_relationship(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.delete_relationship(
            dataset="dataset",
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(object, entity, path=["response"])

    @parametrize
    async def test_streaming_response_delete_relationship(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.delete_relationship(
            dataset="dataset",
            relationship_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(object, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_derive(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.derive(
            dataset="dataset",
            derived_property="derived_property",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            instructions="instructions",
        )
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    async def test_method_derive_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.derive(
            dataset="dataset",
            derived_property="derived_property",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            instructions="instructions",
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    async def test_raw_response_derive(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.derive(
            dataset="dataset",
            derived_property="derived_property",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            instructions="instructions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    async def test_streaming_response_derive(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.derive(
            dataset="dataset",
            derived_property="derived_property",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            instructions="instructions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(str, entity, path=["response"])

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

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
    @parametrize
    async def test_method_get_merges(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.get_merges(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityGetMergesResponse, entity, path=["response"])

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
    @parametrize
    async def test_raw_response_get_merges(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.get_merges(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityGetMergesResponse, entity, path=["response"])

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
    @parametrize
    async def test_streaming_response_get_merges(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.get_merges(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityGetMergesResponse, entity, path=["response"])

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

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
    @parametrize
    async def test_method_merge(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EntityMergeResponse, entity, path=["response"])

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
    @parametrize
    async def test_method_merge_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.merge(
            entity_1_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_2_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            debug=True,
        )
        assert_matches_type(EntityMergeResponse, entity, path=["response"])

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
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

    @pytest.mark.skip(reason="This test is failing because the of the recursive data structure")
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
            dataset="dataset",
            query="query",
            table_name="table_name",
        )
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.search(
            dataset="dataset",
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
            dataset="dataset",
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
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
        )
        assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.summarize(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties=["string"],
            extra_instructions=["string"],
        )
        assert_matches_type(EntitySummarizeResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.summarize(
            dataset="dataset",
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
            dataset="dataset",
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
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "string"},
        )
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    async def test_method_update_property_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.update_property(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "string"},
            source="None",
        )
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_update_property(self, async_client: AsyncStructify) -> None:
        response = await async_client.entities.with_raw_response.update_property(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_update_property(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.update_property(
            dataset="dataset",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityUpdatePropertyResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_verify(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.verify(
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
        )
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    async def test_method_verify_with_all_params(self, async_client: AsyncStructify) -> None:
        entity = await async_client.entities.verify(
            dataset="dataset",
            entity_graph={
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
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(KnowledgeGraph, entity, path=["response"])

    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncStructify) -> None:
        async with async_client.entities.with_streaming_response.verify(
            dataset="dataset",
            entity_graph={
                "entities": [
                    {
                        "id": 0,
                        "properties": {"foo": "string"},
                        "type": "type",
                    }
                ]
            },
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
