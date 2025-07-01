# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import ScrapeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScrape:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        scrape = client.scrape.list(
            dataset_descriptor={
                "description": "description",
                "name": "name",
                "relationships": [
                    {
                        "description": "description",
                        "name": "name",
                        "source_table": "source_table",
                        "target_table": "target_table",
                    }
                ],
                "tables": [
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
            },
            table_name="table_name",
            url="url",
        )
        assert_matches_type(ScrapeListResponse, scrape, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        scrape = client.scrape.list(
            dataset_descriptor={
                "description": "description",
                "name": "name",
                "relationships": [
                    {
                        "description": "description",
                        "name": "name",
                        "source_table": "source_table",
                        "target_table": "target_table",
                        "merge_strategy": {
                            "source_cardinality_given_target_match": 0,
                            "target_cardinality_given_source_match": 0,
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
                "tables": [
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
                        "primary_column": "primary_column",
                    }
                ],
                "llm_override_field": "llm_override_field",
            },
            table_name="table_name",
            url="url",
            run_metadata={
                "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "session_id": "session_id",
            },
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(ScrapeListResponse, scrape, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.scrape.with_raw_response.list(
            dataset_descriptor={
                "description": "description",
                "name": "name",
                "relationships": [
                    {
                        "description": "description",
                        "name": "name",
                        "source_table": "source_table",
                        "target_table": "target_table",
                    }
                ],
                "tables": [
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
            },
            table_name="table_name",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scrape = response.parse()
        assert_matches_type(ScrapeListResponse, scrape, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.scrape.with_streaming_response.list(
            dataset_descriptor={
                "description": "description",
                "name": "name",
                "relationships": [
                    {
                        "description": "description",
                        "name": "name",
                        "source_table": "source_table",
                        "target_table": "target_table",
                    }
                ],
                "tables": [
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
            },
            table_name="table_name",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scrape = response.parse()
            assert_matches_type(ScrapeListResponse, scrape, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScrape:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        scrape = await async_client.scrape.list(
            dataset_descriptor={
                "description": "description",
                "name": "name",
                "relationships": [
                    {
                        "description": "description",
                        "name": "name",
                        "source_table": "source_table",
                        "target_table": "target_table",
                    }
                ],
                "tables": [
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
            },
            table_name="table_name",
            url="url",
        )
        assert_matches_type(ScrapeListResponse, scrape, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        scrape = await async_client.scrape.list(
            dataset_descriptor={
                "description": "description",
                "name": "name",
                "relationships": [
                    {
                        "description": "description",
                        "name": "name",
                        "source_table": "source_table",
                        "target_table": "target_table",
                        "merge_strategy": {
                            "source_cardinality_given_target_match": 0,
                            "target_cardinality_given_source_match": 0,
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
                "tables": [
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
                        "primary_column": "primary_column",
                    }
                ],
                "llm_override_field": "llm_override_field",
            },
            table_name="table_name",
            url="url",
            run_metadata={
                "node_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "session_id": "session_id",
            },
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(ScrapeListResponse, scrape, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.scrape.with_raw_response.list(
            dataset_descriptor={
                "description": "description",
                "name": "name",
                "relationships": [
                    {
                        "description": "description",
                        "name": "name",
                        "source_table": "source_table",
                        "target_table": "target_table",
                    }
                ],
                "tables": [
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
            },
            table_name="table_name",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scrape = await response.parse()
        assert_matches_type(ScrapeListResponse, scrape, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.scrape.with_streaming_response.list(
            dataset_descriptor={
                "description": "description",
                "name": "name",
                "relationships": [
                    {
                        "description": "description",
                        "name": "name",
                        "source_table": "source_table",
                        "target_table": "target_table",
                    }
                ],
                "tables": [
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
            },
            table_name="table_name",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scrape = await response.parse()
            assert_matches_type(ScrapeListResponse, scrape, path=["response"])

        assert cast(Any, response.is_closed) is True
