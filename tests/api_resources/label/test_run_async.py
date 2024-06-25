# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRunAsync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        run_async = client.label.run_async.create(
            dataset_name="string",
            structure_input={
                "sec_ingestor": {
                    "extraction_criteria": [
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                    ]
                }
            },
        )
        assert_matches_type(str, run_async, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.label.run_async.with_raw_response.create(
            dataset_name="string",
            structure_input={
                "sec_ingestor": {
                    "extraction_criteria": [
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                    ]
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run_async = response.parse()
        assert_matches_type(str, run_async, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.label.run_async.with_streaming_response.create(
            dataset_name="string",
            structure_input={
                "sec_ingestor": {
                    "extraction_criteria": [
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                    ]
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run_async = response.parse()
            assert_matches_type(str, run_async, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRunAsync:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        run_async = await async_client.label.run_async.create(
            dataset_name="string",
            structure_input={
                "sec_ingestor": {
                    "extraction_criteria": [
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                    ]
                }
            },
        )
        assert_matches_type(str, run_async, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.run_async.with_raw_response.create(
            dataset_name="string",
            structure_input={
                "sec_ingestor": {
                    "extraction_criteria": [
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                    ]
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run_async = await response.parse()
        assert_matches_type(str, run_async, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.label.run_async.with_streaming_response.create(
            dataset_name="string",
            structure_input={
                "sec_ingestor": {
                    "extraction_criteria": [
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                        {
                            "property_names": ["string", "string", "string"],
                            "table_name": "string",
                        },
                    ]
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run_async = await response.parse()
            assert_matches_type(str, run_async, path=["response"])

        assert cast(Any, response.is_closed) is True
