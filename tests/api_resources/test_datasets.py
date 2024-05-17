# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    DatasetDescriptor,
    DatasetListResponse,
    DatasetViewResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        dataset = client.datasets.create(
            description="string",
            name="string",
            relationships=[
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
            ],
            tables=[
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
            ],
        )
        assert dataset is None

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.create(
            description="string",
            name="string",
            relationships=[
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
            ],
            tables=[
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.create(
            description="string",
            name="string",
            relationships=[
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
            ],
            tables=[
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
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
            name="string",
        )
        assert dataset is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.delete(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.delete(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        dataset = client.datasets.get(
            name="string",
        )
        assert_matches_type(Optional[DatasetDescriptor], dataset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.get(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[DatasetDescriptor], dataset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.get(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[DatasetDescriptor], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_view(self, client: Structify) -> None:
        dataset = client.datasets.view(
            dataset_name="string",
            table_name="string",
        )
        assert_matches_type(DatasetViewResponse, dataset, path=["response"])

    @parametrize
    def test_method_view_with_all_params(self, client: Structify) -> None:
        dataset = client.datasets.view(
            dataset_name="string",
            table_name="string",
            limit=0,
            skip=0,
        )
        assert_matches_type(DatasetViewResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_view(self, client: Structify) -> None:
        response = client.datasets.with_raw_response.view(
            dataset_name="string",
            table_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetViewResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_view(self, client: Structify) -> None:
        with client.datasets.with_streaming_response.view(
            dataset_name="string",
            table_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetViewResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.create(
            description="string",
            name="string",
            relationships=[
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
            ],
            tables=[
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
            ],
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.create(
            description="string",
            name="string",
            relationships=[
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
            ],
            tables=[
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.create(
            description="string",
            name="string",
            relationships=[
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
                {
                    "description": "string",
                    "name": "string",
                    "source_table": "string",
                    "target_table": "string",
                },
            ],
            tables=[
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
                {
                    "description": "string",
                    "name": "string",
                    "properties": [
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                        {
                            "description": "string",
                            "name": "string",
                        },
                    ],
                },
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
            name="string",
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.delete(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.delete(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.get(
            name="string",
        )
        assert_matches_type(Optional[DatasetDescriptor], dataset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.get(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[DatasetDescriptor], dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.get(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[DatasetDescriptor], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_view(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.view(
            dataset_name="string",
            table_name="string",
        )
        assert_matches_type(DatasetViewResponse, dataset, path=["response"])

    @parametrize
    async def test_method_view_with_all_params(self, async_client: AsyncStructify) -> None:
        dataset = await async_client.datasets.view(
            dataset_name="string",
            table_name="string",
            limit=0,
            skip=0,
        )
        assert_matches_type(DatasetViewResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_view(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.with_raw_response.view(
            dataset_name="string",
            table_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetViewResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_view(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.with_streaming_response.view(
            dataset_name="string",
            table_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetViewResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True
