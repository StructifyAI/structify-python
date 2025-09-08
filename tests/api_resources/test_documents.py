# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    DocumentListResponse,
    DocumentDownloadResponse,
    DocumentStructureResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        document = client.documents.list()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        document = client.documents.list(
            dataset="dataset",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        document = client.documents.delete(
            file_path="file_path",
        )
        assert document is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.documents.with_raw_response.delete(
            file_path="file_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.documents.with_streaming_response.delete(
            file_path="file_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_download(self, client: Structify) -> None:
        document = client.documents.download(
            file_path="file_path",
        )
        assert_matches_type(DocumentDownloadResponse, document, path=["response"])

    @parametrize
    def test_raw_response_download(self, client: Structify) -> None:
        response = client.documents.with_raw_response.download(
            file_path="file_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentDownloadResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_download(self, client: Structify) -> None:
        with client.documents.with_streaming_response.download(
            file_path="file_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentDownloadResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_structure(self, client: Structify) -> None:
        document = client.documents.structure(
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
            content=b"raw file contents",
        )
        assert_matches_type(DocumentStructureResponse, document, path=["response"])

    @parametrize
    def test_method_structure_with_all_params(self, client: Structify) -> None:
        document = client.documents.structure(
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
            content=b"raw file contents",
        )
        assert_matches_type(DocumentStructureResponse, document, path=["response"])

    @parametrize
    def test_raw_response_structure(self, client: Structify) -> None:
        response = client.documents.with_raw_response.structure(
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
            content=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentStructureResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_structure(self, client: Structify) -> None:
        with client.documents.with_streaming_response.structure(
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
            content=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentStructureResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload(self, client: Structify) -> None:
        document = client.documents.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        )
        assert document is None

    @parametrize
    def test_method_upload_with_all_params(self, client: Structify) -> None:
        document = client.documents.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
            dataset="dataset",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert document is None

    @parametrize
    def test_raw_response_upload(self, client: Structify) -> None:
        response = client.documents.with_raw_response.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_upload(self, client: Structify) -> None:
        with client.documents.with_streaming_response.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.list()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.list(
            dataset="dataset",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.delete(
            file_path="file_path",
        )
        assert document is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.delete(
            file_path="file_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.delete(
            file_path="file_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_download(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.download(
            file_path="file_path",
        )
        assert_matches_type(DocumentDownloadResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_download(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.download(
            file_path="file_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentDownloadResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.download(
            file_path="file_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentDownloadResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_structure(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.structure(
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
            content=b"raw file contents",
        )
        assert_matches_type(DocumentStructureResponse, document, path=["response"])

    @parametrize
    async def test_method_structure_with_all_params(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.structure(
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
            content=b"raw file contents",
        )
        assert_matches_type(DocumentStructureResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_structure(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.structure(
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
            content=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentStructureResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_structure(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.structure(
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
            content=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentStructureResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        )
        assert document is None

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
            dataset="dataset",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert document is None

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True
