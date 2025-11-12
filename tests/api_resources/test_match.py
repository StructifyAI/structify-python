# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import MatchResult, CreateMatchJobsResponse
from structify.pagination import SyncJobsList, AsyncJobsList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_jobs(self, client: Structify) -> None:
        match = client.match.create_jobs(
            conditioning="conditioning",
            dataset="dataset",
            source_table="source_table",
            target_table="target_table",
        )
        assert_matches_type(CreateMatchJobsResponse, match, path=["response"])

    @parametrize
    def test_method_create_jobs_with_all_params(self, client: Structify) -> None:
        match = client.match.create_jobs(
            conditioning="conditioning",
            dataset="dataset",
            source_table="source_table",
            target_table="target_table",
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreateMatchJobsResponse, match, path=["response"])

    @parametrize
    def test_raw_response_create_jobs(self, client: Structify) -> None:
        response = client.match.with_raw_response.create_jobs(
            conditioning="conditioning",
            dataset="dataset",
            source_table="source_table",
            target_table="target_table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert_matches_type(CreateMatchJobsResponse, match, path=["response"])

    @parametrize
    def test_streaming_response_create_jobs(self, client: Structify) -> None:
        with client.match.with_streaming_response.create_jobs(
            conditioning="conditioning",
            dataset="dataset",
            source_table="source_table",
            target_table="target_table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert_matches_type(CreateMatchJobsResponse, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_results(self, client: Structify) -> None:
        match = client.match.list_results(
            dataset="dataset",
            source_table="source_table",
        )
        assert_matches_type(SyncJobsList[MatchResult], match, path=["response"])

    @parametrize
    def test_method_list_results_with_all_params(self, client: Structify) -> None:
        match = client.match.list_results(
            dataset="dataset",
            source_table="source_table",
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncJobsList[MatchResult], match, path=["response"])

    @parametrize
    def test_raw_response_list_results(self, client: Structify) -> None:
        response = client.match.with_raw_response.list_results(
            dataset="dataset",
            source_table="source_table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert_matches_type(SyncJobsList[MatchResult], match, path=["response"])

    @parametrize
    def test_streaming_response_list_results(self, client: Structify) -> None:
        with client.match.with_streaming_response.list_results(
            dataset="dataset",
            source_table="source_table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert_matches_type(SyncJobsList[MatchResult], match, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_jobs(self, async_client: AsyncStructify) -> None:
        match = await async_client.match.create_jobs(
            conditioning="conditioning",
            dataset="dataset",
            source_table="source_table",
            target_table="target_table",
        )
        assert_matches_type(CreateMatchJobsResponse, match, path=["response"])

    @parametrize
    async def test_method_create_jobs_with_all_params(self, async_client: AsyncStructify) -> None:
        match = await async_client.match.create_jobs(
            conditioning="conditioning",
            dataset="dataset",
            source_table="source_table",
            target_table="target_table",
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreateMatchJobsResponse, match, path=["response"])

    @parametrize
    async def test_raw_response_create_jobs(self, async_client: AsyncStructify) -> None:
        response = await async_client.match.with_raw_response.create_jobs(
            conditioning="conditioning",
            dataset="dataset",
            source_table="source_table",
            target_table="target_table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert_matches_type(CreateMatchJobsResponse, match, path=["response"])

    @parametrize
    async def test_streaming_response_create_jobs(self, async_client: AsyncStructify) -> None:
        async with async_client.match.with_streaming_response.create_jobs(
            conditioning="conditioning",
            dataset="dataset",
            source_table="source_table",
            target_table="target_table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert_matches_type(CreateMatchJobsResponse, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_results(self, async_client: AsyncStructify) -> None:
        match = await async_client.match.list_results(
            dataset="dataset",
            source_table="source_table",
        )
        assert_matches_type(AsyncJobsList[MatchResult], match, path=["response"])

    @parametrize
    async def test_method_list_results_with_all_params(self, async_client: AsyncStructify) -> None:
        match = await async_client.match.list_results(
            dataset="dataset",
            source_table="source_table",
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncJobsList[MatchResult], match, path=["response"])

    @parametrize
    async def test_raw_response_list_results(self, async_client: AsyncStructify) -> None:
        response = await async_client.match.with_raw_response.list_results(
            dataset="dataset",
            source_table="source_table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert_matches_type(AsyncJobsList[MatchResult], match, path=["response"])

    @parametrize
    async def test_streaming_response_list_results(self, async_client: AsyncStructify) -> None:
        async with async_client.match.with_streaming_response.list_results(
            dataset="dataset",
            source_table="source_table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert_matches_type(AsyncJobsList[MatchResult], match, path=["response"])

        assert cast(Any, response.is_closed) is True
