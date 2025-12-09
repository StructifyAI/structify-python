# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    JobListResponse,
    JobCancelResponse,
    JobStatusResponse,
    GetJobEventsResponse,
    JobGetScrapersResponse,
    JobGetSourceEntitiesResponse,
)
from structify._utils import parse_datetime
from structify.pagination import SyncJobsList, AsyncJobsList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        job = client.jobs.list()
        assert_matches_type(SyncJobsList[JobListResponse], job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        job = client.jobs.list(
            dataset="dataset",
            job_type="Web",
            limit=0,
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            offset=0,
            seeded_kg_search_term="seeded_kg_search_term",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="Queued",
        )
        assert_matches_type(SyncJobsList[JobListResponse], job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SyncJobsList[JobListResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(SyncJobsList[JobListResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Structify) -> None:
        job = client.jobs.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobCancelResponse, job, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Structify) -> None:
        response = client.jobs.with_raw_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCancelResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Structify) -> None:
        with client.jobs.with_streaming_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCancelResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.jobs.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_get_events(self, client: Structify) -> None:
        job = client.jobs.get_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetJobEventsResponse, job, path=["response"])

    @parametrize
    def test_raw_response_get_events(self, client: Structify) -> None:
        response = client.jobs.with_raw_response.get_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(GetJobEventsResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_get_events(self, client: Structify) -> None:
        with client.jobs.with_streaming_response.get_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(GetJobEventsResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_events(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.with_raw_response.get_events(
                "",
            )

    @parametrize
    def test_method_get_scrapers(self, client: Structify) -> None:
        job = client.jobs.get_scrapers(
            "job_id",
        )
        assert_matches_type(JobGetScrapersResponse, job, path=["response"])

    @parametrize
    def test_raw_response_get_scrapers(self, client: Structify) -> None:
        response = client.jobs.with_raw_response.get_scrapers(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobGetScrapersResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_get_scrapers(self, client: Structify) -> None:
        with client.jobs.with_streaming_response.get_scrapers(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobGetScrapersResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_scrapers(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.with_raw_response.get_scrapers(
                "",
            )

    @parametrize
    def test_method_get_source_entities(self, client: Structify) -> None:
        job = client.jobs.get_source_entities(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobGetSourceEntitiesResponse, job, path=["response"])

    @parametrize
    def test_raw_response_get_source_entities(self, client: Structify) -> None:
        response = client.jobs.with_raw_response.get_source_entities(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobGetSourceEntitiesResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_get_source_entities(self, client: Structify) -> None:
        with client.jobs.with_streaming_response.get_source_entities(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobGetSourceEntitiesResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_source_entities(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.with_raw_response.get_source_entities(
                "",
            )

    @parametrize
    def test_method_schedule(self, client: Structify) -> None:
        job = client.jobs.schedule()
        assert job is None

    @parametrize
    def test_raw_response_schedule(self, client: Structify) -> None:
        response = client.jobs.with_raw_response.schedule()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @parametrize
    def test_streaming_response_schedule(self, client: Structify) -> None:
        with client.jobs.with_streaming_response.schedule() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_status(self, client: Structify) -> None:
        job = client.jobs.status()
        assert_matches_type(JobStatusResponse, job, path=["response"])

    @parametrize
    def test_method_status_with_all_params(self, client: Structify) -> None:
        job = client.jobs.status(
            dataset_name="dataset_name",
            job_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobStatusResponse, job, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Structify) -> None:
        response = client.jobs.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobStatusResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Structify) -> None:
        with client.jobs.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobStatusResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        job = await async_client.jobs.list()
        assert_matches_type(AsyncJobsList[JobListResponse], job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        job = await async_client.jobs.list(
            dataset="dataset",
            job_type="Web",
            limit=0,
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            offset=0,
            seeded_kg_search_term="seeded_kg_search_term",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="Queued",
        )
        assert_matches_type(AsyncJobsList[JobListResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(AsyncJobsList[JobListResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(AsyncJobsList[JobListResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncStructify) -> None:
        job = await async_client.jobs.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobCancelResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncStructify) -> None:
        response = await async_client.jobs.with_raw_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCancelResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncStructify) -> None:
        async with async_client.jobs.with_streaming_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCancelResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.jobs.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_get_events(self, async_client: AsyncStructify) -> None:
        job = await async_client.jobs.get_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetJobEventsResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_get_events(self, async_client: AsyncStructify) -> None:
        response = await async_client.jobs.with_raw_response.get_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(GetJobEventsResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_get_events(self, async_client: AsyncStructify) -> None:
        async with async_client.jobs.with_streaming_response.get_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(GetJobEventsResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_events(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.with_raw_response.get_events(
                "",
            )

    @parametrize
    async def test_method_get_scrapers(self, async_client: AsyncStructify) -> None:
        job = await async_client.jobs.get_scrapers(
            "job_id",
        )
        assert_matches_type(JobGetScrapersResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_get_scrapers(self, async_client: AsyncStructify) -> None:
        response = await async_client.jobs.with_raw_response.get_scrapers(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobGetScrapersResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_get_scrapers(self, async_client: AsyncStructify) -> None:
        async with async_client.jobs.with_streaming_response.get_scrapers(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobGetScrapersResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_scrapers(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.with_raw_response.get_scrapers(
                "",
            )

    @parametrize
    async def test_method_get_source_entities(self, async_client: AsyncStructify) -> None:
        job = await async_client.jobs.get_source_entities(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobGetSourceEntitiesResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_get_source_entities(self, async_client: AsyncStructify) -> None:
        response = await async_client.jobs.with_raw_response.get_source_entities(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobGetSourceEntitiesResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_get_source_entities(self, async_client: AsyncStructify) -> None:
        async with async_client.jobs.with_streaming_response.get_source_entities(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobGetSourceEntitiesResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_source_entities(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.with_raw_response.get_source_entities(
                "",
            )

    @parametrize
    async def test_method_schedule(self, async_client: AsyncStructify) -> None:
        job = await async_client.jobs.schedule()
        assert job is None

    @parametrize
    async def test_raw_response_schedule(self, async_client: AsyncStructify) -> None:
        response = await async_client.jobs.with_raw_response.schedule()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @parametrize
    async def test_streaming_response_schedule(self, async_client: AsyncStructify) -> None:
        async with async_client.jobs.with_streaming_response.schedule() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_status(self, async_client: AsyncStructify) -> None:
        job = await async_client.jobs.status()
        assert_matches_type(JobStatusResponse, job, path=["response"])

    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncStructify) -> None:
        job = await async_client.jobs.status(
            dataset_name="dataset_name",
            job_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobStatusResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncStructify) -> None:
        response = await async_client.jobs.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobStatusResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncStructify) -> None:
        async with async_client.jobs.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobStatusResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True
