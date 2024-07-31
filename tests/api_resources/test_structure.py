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
    def test_method_is_complete(self, client: Structify) -> None:
        structure = client.structure.is_complete(
            job=["string", "string", "string"],
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_raw_response_is_complete(self, client: Structify) -> None:
        response = client.structure.with_raw_response.is_complete(
            job=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_streaming_response_is_complete(self, client: Structify) -> None:
        with client.structure.with_streaming_response.is_complete(
            job=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_job_status(self, client: Structify) -> None:
        structure = client.structure.job_status(
            job=["string", "string", "string"],
        )
        assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

    @parametrize
    def test_raw_response_job_status(self, client: Structify) -> None:
        response = client.structure.with_raw_response.job_status(
            job=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = response.parse()
        assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

    @parametrize
    def test_streaming_response_job_status(self, client: Structify) -> None:
        with client.structure.with_streaming_response.job_status(
            job=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = response.parse()
            assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_async(self, client: Structify) -> None:
        structure = client.structure.run_async(
            name="name",
            structure_input={"sec_ingestor": {}},
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_method_run_async_with_all_params(self, client: Structify) -> None:
        structure = client.structure.run_async(
            name="name",
            structure_input={
                "sec_ingestor": {
                    "accession_number": "accession_number",
                    "quarter": 0,
                    "year": 0,
                }
            },
            extraction_criteria=[
                {"relationship_extraction": {"relationship_name": "relationship_name"}},
                {"relationship_extraction": {"relationship_name": "relationship_name"}},
                {"relationship_extraction": {"relationship_name": "relationship_name"}},
            ],
            seeded_entity={
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
                    },
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                    },
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                    },
                ],
            },
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_raw_response_run_async(self, client: Structify) -> None:
        response = client.structure.with_raw_response.run_async(
            name="name",
            structure_input={"sec_ingestor": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    def test_streaming_response_run_async(self, client: Structify) -> None:
        with client.structure.with_streaming_response.run_async(
            name="name",
            structure_input={"sec_ingestor": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStructure:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_is_complete(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.is_complete(
            job=["string", "string", "string"],
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_raw_response_is_complete(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.with_raw_response.is_complete(
            job=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = await response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_streaming_response_is_complete(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.with_streaming_response.is_complete(
            job=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = await response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_job_status(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.job_status(
            job=["string", "string", "string"],
        )
        assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

    @parametrize
    async def test_raw_response_job_status(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.with_raw_response.job_status(
            job=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = await response.parse()
        assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

    @parametrize
    async def test_streaming_response_job_status(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.with_streaming_response.job_status(
            job=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = await response.parse()
            assert_matches_type(StructureJobStatusResponse, structure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_async(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.run_async(
            name="name",
            structure_input={"sec_ingestor": {}},
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_method_run_async_with_all_params(self, async_client: AsyncStructify) -> None:
        structure = await async_client.structure.run_async(
            name="name",
            structure_input={
                "sec_ingestor": {
                    "accession_number": "accession_number",
                    "quarter": 0,
                    "year": 0,
                }
            },
            extraction_criteria=[
                {"relationship_extraction": {"relationship_name": "relationship_name"}},
                {"relationship_extraction": {"relationship_name": "relationship_name"}},
                {"relationship_extraction": {"relationship_name": "relationship_name"}},
            ],
            seeded_entity={
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
                    },
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                    },
                    {
                        "source": 0,
                        "target": 0,
                        "type": "type",
                    },
                ],
            },
        )
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_raw_response_run_async(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.with_raw_response.run_async(
            name="name",
            structure_input={"sec_ingestor": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = await response.parse()
        assert_matches_type(str, structure, path=["response"])

    @parametrize
    async def test_streaming_response_run_async(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.with_streaming_response.run_async(
            name="name",
            structure_input={"sec_ingestor": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = await response.parse()
            assert_matches_type(str, structure, path=["response"])

        assert cast(Any, response.is_closed) is True
