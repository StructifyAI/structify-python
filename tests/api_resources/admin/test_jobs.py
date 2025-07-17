# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify._utils import parse_datetime
from structify.pagination import SyncJobsList, AsyncJobsList
from structify.types.admin import AdminListJobsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        job = client.admin.jobs.list(
            filter_test_users=True,
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncJobsList[AdminListJobsResponse], job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        job = client.admin.jobs.list(
            filter_test_users=True,
            limit=0,
            offset=0,
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            seeded_kg_search_term="seeded_kg_search_term",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="Queued",
        )
        assert_matches_type(SyncJobsList[AdminListJobsResponse], job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.admin.jobs.with_raw_response.list(
            filter_test_users=True,
            limit=0,
            offset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SyncJobsList[AdminListJobsResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.admin.jobs.with_streaming_response.list(
            filter_test_users=True,
            limit=0,
            offset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(SyncJobsList[AdminListJobsResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        job = await async_client.admin.jobs.list(
            filter_test_users=True,
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncJobsList[AdminListJobsResponse], job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        job = await async_client.admin.jobs.list(
            filter_test_users=True,
            limit=0,
            offset=0,
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            seeded_kg_search_term="seeded_kg_search_term",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="Queued",
        )
        assert_matches_type(AsyncJobsList[AdminListJobsResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.jobs.with_raw_response.list(
            filter_test_users=True,
            limit=0,
            offset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(AsyncJobsList[AdminListJobsResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.jobs.with_streaming_response.list(
            filter_test_users=True,
            limit=0,
            offset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(AsyncJobsList[AdminListJobsResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True
