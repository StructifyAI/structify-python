# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    StructureJobStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStructure:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_enhance_property(self, client: Structify) -> None:
        structure = client.structure.enhance_property(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property_name="property_name",
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_method_enhance_property_with_all_params(self, client: Structify) -> None:
        structure = client.structure.enhance_property(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property_name="property_name",
            allow_extra_entities=True,
            banned_domains=["string"],
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            special_job_type="HumanLLM",
            starting_searches=["string"],
            starting_urls=["string"],
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_raw_response_enhance_property(self, client: Structify) -> None:
        response = client.structure.with_raw_response.enhance_property(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property_name="property_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_streaming_response_enhance_property(self, client: Structify) -> None:
        with client.structure.with_streaming_response.enhance_property(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property_name="property_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_enhance_relationship(self, client: Structify) -> None:
        structure = client.structure.enhance_relationship(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_method_enhance_relationship_with_all_params(self, client: Structify) -> None:
        structure = client.structure.enhance_relationship(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
            allow_extra_entities=True,
            banned_domains=["string"],
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            special_job_type="HumanLLM",
            starting_searches=["string"],
            starting_urls=["string"],
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_raw_response_enhance_relationship(self, client: Structify) -> None:
        response = client.structure.with_raw_response.enhance_relationship(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_streaming_response_enhance_relationship(self, client: Structify) -> None:
        with client.structure.with_streaming_response.enhance_relationship(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_find_relationship(self, client: Structify) -> None:
        structure = client.structure.find_relationship(
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_method_find_relationship_with_all_params(self, client: Structify) -> None:
        structure = client.structure.find_relationship(
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allow_extra_entities=True,
            banned_domains=["string"],
            special_job_type="HumanLLM",
            starting_searches=["string"],
            starting_urls=["string"],
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_raw_response_find_relationship(self, client: Structify) -> None:
        response = client.structure.with_raw_response.find_relationship(
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_streaming_response_find_relationship(self, client: Structify) -> None:
        with client.structure.with_streaming_response.find_relationship(
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_is_complete(self, client: Structify) -> None:
        structure = client.structure.is_complete(
            job=["string"],
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_raw_response_is_complete(self, client: Structify) -> None:
        response = client.structure.with_raw_response.is_complete(
            job=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_streaming_response_is_complete(self, client: Structify) -> None:
        with client.structure.with_streaming_response.is_complete(
            job=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_job_status(self, client: Structify) -> None:
        structure = client.structure.job_status(
            job={},
        )
        assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

    @parametrize
    def test_method_job_status_with_all_params(self, client: Structify) -> None:
        structure = client.structure.job_status(
            job={
                "dataset_name": "dataset_name",
                "job_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
        )
        assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

    @parametrize
    def test_raw_response_job_status(self, client: Structify) -> None:
        response = client.structure.with_raw_response.job_status(
            job={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = response.parse()
        assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

    @parametrize
    def test_streaming_response_job_status(self, client: Structify) -> None:
        with client.structure.with_streaming_response.job_status(
            job={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = response.parse()
            assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_async(self, client: Structify) -> None:
        structure = client.structure.run_async(
            dataset="dataset",
            source={"pdf": {"path": "path"}},
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_method_run_async_with_all_params(self, client: Structify) -> None:
        structure = client.structure.run_async(
            dataset="dataset",
            source={"pdf": {"path": "path"}},
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            save_requirement=[{"relationship_name": "relationship_name"}],
            seeded_entity={
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
            special_job_type="HumanLLM",
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_raw_response_run_async(self, client: Structify) -> None:
        response = client.structure.with_raw_response.run_async(
            dataset="dataset",
            source={"pdf": {"path": "path"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_streaming_response_run_async(self, client: Structify) -> None:
        with client.structure.with_streaming_response.run_async(
            dataset="dataset",
            source={"pdf": {"path": "path"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStructure:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_enhance_property(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.enhance_property(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property_name="property_name",
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_method_enhance_property_with_all_params(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.enhance_property(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property_name="property_name",
            allow_extra_entities=True,
            banned_domains=["string"],
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            special_job_type="HumanLLM",
            starting_searches=["string"],
            starting_urls=["string"],
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_raw_response_enhance_property(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.with_raw_response.enhance_property(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property_name="property_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = await response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_streaming_response_enhance_property(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.with_streaming_response.enhance_property(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property_name="property_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = await response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_enhance_relationship(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.enhance_relationship(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_method_enhance_relationship_with_all_params(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.enhance_relationship(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
            allow_extra_entities=True,
            banned_domains=["string"],
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            special_job_type="HumanLLM",
            starting_searches=["string"],
            starting_urls=["string"],
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_raw_response_enhance_relationship(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.with_raw_response.enhance_relationship(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = await response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_streaming_response_enhance_relationship(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.with_streaming_response.enhance_relationship(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = await response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_find_relationship(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.find_relationship(
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_method_find_relationship_with_all_params(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.find_relationship(
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allow_extra_entities=True,
            banned_domains=["string"],
            special_job_type="HumanLLM",
            starting_searches=["string"],
            starting_urls=["string"],
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_raw_response_find_relationship(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.with_raw_response.find_relationship(
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = await response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_streaming_response_find_relationship(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.with_streaming_response.find_relationship(
            from_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            relationship_name="relationship_name",
            to_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = await response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_is_complete(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.is_complete(
            job=["string"],
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_raw_response_is_complete(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.with_raw_response.is_complete(
            job=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = await response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_streaming_response_is_complete(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.with_streaming_response.is_complete(
            job=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = await response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_job_status(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.job_status(
            job={},
        )
        assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

    @parametrize
    async def test_method_job_status_with_all_params(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.job_status(
            job={
                "dataset_name": "dataset_name",
                "job_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
        )
        assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

    @parametrize
    async def test_raw_response_job_status(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.with_raw_response.job_status(
            job={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = await response.parse()
        assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

    @parametrize
    async def test_streaming_response_job_status(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.with_streaming_response.job_status(
            job={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = await response.parse()
            assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_async(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.run_async(
            dataset="dataset",
            source={"pdf": {"path": "path"}},
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_method_run_async_with_all_params(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.run_async(
            dataset="dataset",
            source={"pdf": {"path": "path"}},
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            save_requirement=[{"relationship_name": "relationship_name"}],
            seeded_entity={
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
            special_job_type="HumanLLM",
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_raw_response_run_async(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.with_raw_response.run_async(
            dataset="dataset",
            source={"pdf": {"path": "path"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = await response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_streaming_response_run_async(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.with_streaming_response.run_async(
            dataset="dataset",
            source={"pdf": {"path": "path"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = await response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True
