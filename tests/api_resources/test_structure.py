# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import io
import os
from typing import Any, cast

import polars as pl
import pytest

from structify import Structify, AsyncStructify
from structify.types import DatasetDescriptorParam, StructureJobStatusResponse
from structify.types.structure_params import StructureParams
from structify.types.structure_response import StructureResponse
from structify.types.table_param import Property, TableParam
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


def make_structure_request() -> tuple[StructureParams, bytes]:
    buffer = io.BytesIO()
    pl.DataFrame({"name": ["Structify"]}).write_parquet(buffer)

    properties: list[Property] = [
        {"name": "name", "description": "Company name", "prop_type": "String"},
    ]
    tables: list[TableParam] = [
        {
            "name": "Company",
            "description": "Company table",
            "properties": properties,
        }
    ]
    dataset_descriptor: DatasetDescriptorParam = {
        "name": "test_dataset",
        "description": "Test dataset",
        "tables": tables,
        "relationships": [],
    }
    new_columns: list[Property] = [
        {"name": "description", "description": "Company description", "prop_type": "String"},
    ]
    params: StructureParams = {
        "dataset_descriptor": dataset_descriptor,
        "table_name": "Company",
        "new_columns": new_columns,
    }

    return params, buffer.getvalue()


class TestStructure:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_structure(self, client: Structify) -> None:
        params, file_data = make_structure_request()
        structure = client.structure.structure(
            params=params,
            file=file_data,
        )
        assert_matches_type(StructureResponse, structure, path=["response"])

    @parametrize
    def test_method_structure_with_all_params(self, client: Structify) -> None:
        params, file_data = make_structure_request()
        params["allow_expand_rows"] = True
        params["instruction"] = "Use the company name to find details."
        params["browser"] = {"starting_urls": ["https://www.example.com"], "proxy": True}
        params["sandbox"] = {}
        params["nsteps"] = 5
        params["model"] = "gpt-4o-mini"
        params["node_id"] = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
        structure = client.structure.structure(
            params=params,
            file=file_data,
        )
        assert_matches_type(StructureResponse, structure, path=["response"])

    @parametrize
    def test_raw_response_structure(self, client: Structify) -> None:
        params, file_data = make_structure_request()
        response = client.structure.with_raw_response.structure(
            params=params,
            file=file_data,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = response.parse()
        assert_matches_type(StructureResponse, structure, path=["response"])

    @parametrize
    def test_streaming_response_structure(self, client: Structify) -> None:
        params, file_data = make_structure_request()
        with client.structure.with_streaming_response.structure(
            params=params,
            file=file_data,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = response.parse()
            assert_matches_type(StructureResponse, structure, path=["response"])

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


class TestAsyncStructure:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_structure(self, async_client: AsyncStructify) -> None:
        params, file_data = make_structure_request()
        structure = await async_client.structure.structure(
            params=params,
            file=file_data,
        )
        assert_matches_type(StructureResponse, structure, path=["response"])

    @parametrize
    async def test_method_structure_with_all_params(self, async_client: AsyncStructify) -> None:
        params, file_data = make_structure_request()
        params["allow_expand_rows"] = True
        params["instruction"] = "Use the company name to find details."
        params["browser"] = {"starting_urls": ["https://www.example.com"], "proxy": True}
        params["sandbox"] = {}
        params["nsteps"] = 5
        params["model"] = "gpt-4o-mini"
        params["node_id"] = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
        structure = await async_client.structure.structure(
            params=params,
            file=file_data,
        )
        assert_matches_type(StructureResponse, structure, path=["response"])

    @parametrize
    async def test_raw_response_structure(self, async_client: AsyncStructify) -> None:
        params, file_data = make_structure_request()
        response = await async_client.structure.with_raw_response.structure(
            params=params,
            file=file_data,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        structure = await response.parse()
        assert_matches_type(StructureResponse, structure, path=["response"])

    @parametrize
    async def test_streaming_response_structure(self, async_client: AsyncStructify) -> None:
        params, file_data = make_structure_request()
        async with async_client.structure.with_streaming_response.structure(
            params=params,
            file=file_data,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            structure = await response.parse()
            assert_matches_type(StructureResponse, structure, path=["response"])

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
