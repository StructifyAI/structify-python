# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    PlanListResponse,
    PlanPauseAllResponse,
    PlanResumeAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlan:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        plan = client.plan.create(
            dataset="dataset",
            plan={
                "steps": [
                    {
                        "entity_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "property_name": "property_name",
                    }
                ]
            },
        )
        assert_matches_type(str, plan, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.plan.with_raw_response.create(
            dataset="dataset",
            plan={
                "steps": [
                    {
                        "entity_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "property_name": "property_name",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(str, plan, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.plan.with_streaming_response.create(
            dataset="dataset",
            plan={
                "steps": [
                    {
                        "entity_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "property_name": "property_name",
                    }
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(str, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        plan = client.plan.list()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.plan.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.plan.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanListResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_pause_all(self, client: Structify) -> None:
        plan = client.plan.pause_all(
            dataset_name="dataset_name",
        )
        assert_matches_type(PlanPauseAllResponse, plan, path=["response"])

    @parametrize
    def test_raw_response_pause_all(self, client: Structify) -> None:
        response = client.plan.with_raw_response.pause_all(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanPauseAllResponse, plan, path=["response"])

    @parametrize
    def test_streaming_response_pause_all(self, client: Structify) -> None:
        with client.plan.with_streaming_response.pause_all(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanPauseAllResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_resume_all(self, client: Structify) -> None:
        plan = client.plan.resume_all(
            dataset_name="dataset_name",
        )
        assert_matches_type(PlanResumeAllResponse, plan, path=["response"])

    @parametrize
    def test_raw_response_resume_all(self, client: Structify) -> None:
        response = client.plan.with_raw_response.resume_all(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanResumeAllResponse, plan, path=["response"])

    @parametrize
    def test_streaming_response_resume_all(self, client: Structify) -> None:
        with client.plan.with_streaming_response.resume_all(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanResumeAllResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPlan:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        plan = await async_client.plan.create(
            dataset="dataset",
            plan={
                "steps": [
                    {
                        "entity_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "property_name": "property_name",
                    }
                ]
            },
        )
        assert_matches_type(str, plan, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.plan.with_raw_response.create(
            dataset="dataset",
            plan={
                "steps": [
                    {
                        "entity_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "property_name": "property_name",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(str, plan, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.plan.with_streaming_response.create(
            dataset="dataset",
            plan={
                "steps": [
                    {
                        "entity_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "property_name": "property_name",
                    }
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(str, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        plan = await async_client.plan.list()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.plan.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.plan.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanListResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_pause_all(self, async_client: AsyncStructify) -> None:
        plan = await async_client.plan.pause_all(
            dataset_name="dataset_name",
        )
        assert_matches_type(PlanPauseAllResponse, plan, path=["response"])

    @parametrize
    async def test_raw_response_pause_all(self, async_client: AsyncStructify) -> None:
        response = await async_client.plan.with_raw_response.pause_all(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanPauseAllResponse, plan, path=["response"])

    @parametrize
    async def test_streaming_response_pause_all(self, async_client: AsyncStructify) -> None:
        async with async_client.plan.with_streaming_response.pause_all(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanPauseAllResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_resume_all(self, async_client: AsyncStructify) -> None:
        plan = await async_client.plan.resume_all(
            dataset_name="dataset_name",
        )
        assert_matches_type(PlanResumeAllResponse, plan, path=["response"])

    @parametrize
    async def test_raw_response_resume_all(self, async_client: AsyncStructify) -> None:
        response = await async_client.plan.with_raw_response.resume_all(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanResumeAllResponse, plan, path=["response"])

    @parametrize
    async def test_streaming_response_resume_all(self, async_client: AsyncStructify) -> None:
        async with async_client.plan.with_streaming_response.resume_all(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanResumeAllResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True
