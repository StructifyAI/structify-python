# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    DatasetGetResponse,
    DatasetListResponse,
    DatasetMatchResponse,
    DatasetViewTableResponse,
    DatasetViewRelationshipsResponse,
    DatasetViewTablesWithRelationshipsResponse,
)
from structify._utils import parse_datetime
from structify.pagination import SyncJobsList, AsyncJobsList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        dataset = client.datasets.create(
            description="description",
            name="name",
            relationships=[
                {
                    "description": "description",
                    "name": "name",
                    "source_table": "source_table",
                    "target_table": "target_table",
                }
            ],
            tables=[
                {
                    "description": "description",
                    "name": "name",
                    "properties": [
                        {
                            "description": "description",
                            "name": "name",
                        }
                    ],
                }
            ],
        )
        assert dataset is None

    @parametrize
    def test_method_create_with_all_params(self, client: Structify) -> None:
        dataset = client.datasets.create(
            description="description",
            name="name",
            relationships=[
                {
                    "description": "description",
                    "name": "name",
                    "source_table": "source_table",
                    "target_table": "target_table",
                    "merge_strategy": {
                        "probabilistic": {
                            "source_cardinality_given_target_match": 0,
                            "target_cardinality_given_source_match": 0,
                        }
                    },
                    "properties": [
                        {
                            "description": "description",
                            "name": "name",
                            "merge_strategy": "Unique",
                            "prop_type": "String",
                        }
                    ],
                }
            ],
            tables=[
                {
                    "description": "description",
                    "name": "name",
                    "properties": [
                        {
                            "description": "description",
                            "name": "name",
                            "merge_strategy": "Unique",
                            "prop_type": "String",
                        }
                    ],
                    "expected_cardinality": 0,
                }
            ],
            model_override="model_override",
        )
        assert dataset is None

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.create(
            description="description",
            name="name",
            relationships=[
                {
                    "description": "description",
                    "name": "name",
                    "source_table": "source_table",
                    "target_table": "target_table",
                }
            ],
            tables=[
                {
                    "description": "description",
                    "name": "name",
                    "properties": [
                        {
                            "description": "description",
                            "name": "name",
                        }
                    ],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.create(
            description="description",
            name="name",
            relationships=[
                {
                    "description": "description",
                    "name": "name",
                    "source_table": "source_table",
                    "target_table": "target_table",
                }
            ],
            tables=[
                {
                    "description": "description",
                    "name": "name",
                    "properties": [
                        {
                            "description": "description",
                            "name": "name",
                        }
                    ],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        dataset = client.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        dataset = client.datasets.delete(
            name="name",
        )
        assert dataset is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.delete(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.delete(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        dataset = client.datasets.get(
            name="name",
        )
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.get(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.get(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetGetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_match(self, client: Structify) -> None:
        dataset = client.datasets.match(
            dataset="dataset",
            query_kg={},
        )
        assert_matches_type(DatasetMatchResponse, dataset, path=["response"])

    @parametrize
    def test_method_match_with_all_params(self, client: Structify) -> None:
        dataset = client.datasets.match(
            dataset="dataset",
            query_kg={
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
            match_threshold=0,
        )
        assert_matches_type(DatasetMatchResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_match(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.match(
            dataset="dataset",
            query_kg={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetMatchResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_match(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.match(
            dataset="dataset",
            query_kg={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetMatchResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_view_relationships(self, client: Structify) -> None:
        dataset = client.datasets.view_relationships(
            dataset="dataset",
            name="name",
        )
        assert_matches_type(SyncJobsList[DatasetViewRelationshipsResponse], dataset, path=["response"])

    @parametrize
    def test_method_view_relationships_with_all_params(self, client: Structify) -> None:
        dataset = client.datasets.view_relationships(
            dataset="dataset",
            name="name",
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            last_updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            sort_by={
                "col_id": "creation_time",
                "sort": "asc",
            },
        )
        assert_matches_type(SyncJobsList[DatasetViewRelationshipsResponse], dataset, path=["response"])

    @parametrize
    def test_raw_response_view_relationships(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.view_relationships(
            dataset="dataset",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(SyncJobsList[DatasetViewRelationshipsResponse], dataset, path=["response"])

    @parametrize
    def test_streaming_response_view_relationships(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.view_relationships(
            dataset="dataset",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(SyncJobsList[DatasetViewRelationshipsResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_view_table(self, client: Structify) -> None:
        dataset = client.datasets.view_table(
            dataset="dataset",
            name="name",
        )
        assert_matches_type(SyncJobsList[DatasetViewTableResponse], dataset, path=["response"])

    @parametrize
    def test_method_view_table_with_all_params(self, client: Structify) -> None:
        dataset = client.datasets.view_table(
            dataset="dataset",
            name="name",
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            last_updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            sort_by={
                "col_id": "creation_time",
                "sort": "asc",
            },
        )
        assert_matches_type(SyncJobsList[DatasetViewTableResponse], dataset, path=["response"])

    @parametrize
    def test_raw_response_view_table(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.view_table(
            dataset="dataset",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(SyncJobsList[DatasetViewTableResponse], dataset, path=["response"])

    @parametrize
    def test_streaming_response_view_table(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.view_table(
            dataset="dataset",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(SyncJobsList[DatasetViewTableResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_view_tables_with_relationships(self, client: Structify) -> None:
        dataset = client.datasets.view_tables_with_relationships(
            dataset="dataset",
            name="name",
        )
        assert_matches_type(DatasetViewTablesWithRelationshipsResponse, dataset, path=["response"])

    @parametrize
    def test_method_view_tables_with_relationships_with_all_params(self, client: Structify) -> None:
        dataset = client.datasets.view_tables_with_relationships(
            dataset="dataset",
            name="name",
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            last_updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            sort_by={
                "col_id": "creation_time",
                "sort": "asc",
            },
        )
        assert_matches_type(DatasetViewTablesWithRelationshipsResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_view_tables_with_relationships(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.view_tables_with_relationships(
            dataset="dataset",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetViewTablesWithRelationshipsResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_view_tables_with_relationships(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.view_tables_with_relationships(
            dataset="dataset",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetViewTablesWithRelationshipsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.create(
            description="description",
            name="name",
            relationships=[
                {
                    "description": "description",
                    "name": "name",
                    "source_table": "source_table",
                    "target_table": "target_table",
                }
            ],
            tables=[
                {
                    "description": "description",
                    "name": "name",
                    "properties": [
                        {
                            "description": "description",
                            "name": "name",
                        }
                    ],
                }
            ],
        )
        assert dataset is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.create(
            description="description",
            name="name",
            relationships=[
                {
                    "description": "description",
                    "name": "name",
                    "source_table": "source_table",
                    "target_table": "target_table",
                    "merge_strategy": {
                        "probabilistic": {
                            "source_cardinality_given_target_match": 0,
                            "target_cardinality_given_source_match": 0,
                        }
                    },
                    "properties": [
                        {
                            "description": "description",
                            "name": "name",
                            "merge_strategy": "Unique",
                            "prop_type": "String",
                        }
                    ],
                }
            ],
            tables=[
                {
                    "description": "description",
                    "name": "name",
                    "properties": [
                        {
                            "description": "description",
                            "name": "name",
                            "merge_strategy": "Unique",
                            "prop_type": "String",
                        }
                    ],
                    "expected_cardinality": 0,
                }
            ],
            model_override="model_override",
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.create(
            description="description",
            name="name",
            relationships=[
                {
                    "description": "description",
                    "name": "name",
                    "source_table": "source_table",
                    "target_table": "target_table",
                }
            ],
            tables=[
                {
                    "description": "description",
                    "name": "name",
                    "properties": [
                        {
                            "description": "description",
                            "name": "name",
                        }
                    ],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.create(
            description="description",
            name="name",
            relationships=[
                {
                    "description": "description",
                    "name": "name",
                    "source_table": "source_table",
                    "target_table": "target_table",
                }
            ],
            tables=[
                {
                    "description": "description",
                    "name": "name",
                    "properties": [
                        {
                            "description": "description",
                            "name": "name",
                        }
                    ],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.delete(
            name="name",
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.delete(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.delete(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.get(
            name="name",
        )
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.get(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetGetResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.get(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetGetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_match(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.match(
            dataset="dataset",
            query_kg={},
        )
        assert_matches_type(DatasetMatchResponse, dataset, path=["response"])

    @parametrize
    async def test_method_match_with_all_params(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.match(
            dataset="dataset",
            query_kg={
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
            match_threshold=0,
        )
        assert_matches_type(DatasetMatchResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_match(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.match(
            dataset="dataset",
            query_kg={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetMatchResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_match(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.match(
            dataset="dataset",
            query_kg={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetMatchResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_view_relationships(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.view_relationships(
            dataset="dataset",
            name="name",
        )
        assert_matches_type(AsyncJobsList[DatasetViewRelationshipsResponse], dataset, path=["response"])

    @parametrize
    async def test_method_view_relationships_with_all_params(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.view_relationships(
            dataset="dataset",
            name="name",
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            last_updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            sort_by={
                "col_id": "creation_time",
                "sort": "asc",
            },
        )
        assert_matches_type(AsyncJobsList[DatasetViewRelationshipsResponse], dataset, path=["response"])

    @parametrize
    async def test_raw_response_view_relationships(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.view_relationships(
            dataset="dataset",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(AsyncJobsList[DatasetViewRelationshipsResponse], dataset, path=["response"])

    @parametrize
    async def test_streaming_response_view_relationships(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.view_relationships(
            dataset="dataset",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(AsyncJobsList[DatasetViewRelationshipsResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_view_table(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.view_table(
            dataset="dataset",
            name="name",
        )
        assert_matches_type(AsyncJobsList[DatasetViewTableResponse], dataset, path=["response"])

    @parametrize
    async def test_method_view_table_with_all_params(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.view_table(
            dataset="dataset",
            name="name",
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            last_updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            sort_by={
                "col_id": "creation_time",
                "sort": "asc",
            },
        )
        assert_matches_type(AsyncJobsList[DatasetViewTableResponse], dataset, path=["response"])

    @parametrize
    async def test_raw_response_view_table(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.view_table(
            dataset="dataset",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(AsyncJobsList[DatasetViewTableResponse], dataset, path=["response"])

    @parametrize
    async def test_streaming_response_view_table(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.view_table(
            dataset="dataset",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(AsyncJobsList[DatasetViewTableResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_view_tables_with_relationships(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.view_tables_with_relationships(
            dataset="dataset",
            name="name",
        )
        assert_matches_type(DatasetViewTablesWithRelationshipsResponse, dataset, path=["response"])

    @parametrize
    async def test_method_view_tables_with_relationships_with_all_params(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.view_tables_with_relationships(
            dataset="dataset",
            name="name",
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            last_updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            sort_by={
                "col_id": "creation_time",
                "sort": "asc",
            },
        )
        assert_matches_type(DatasetViewTablesWithRelationshipsResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_view_tables_with_relationships(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.view_tables_with_relationships(
            dataset="dataset",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetViewTablesWithRelationshipsResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_view_tables_with_relationships(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.view_tables_with_relationships(
            dataset="dataset",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetViewTablesWithRelationshipsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True
