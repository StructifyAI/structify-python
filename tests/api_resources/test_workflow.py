# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    ExistingWorkflow,
    WorkflowJobsResponse,
    WorkflowListResponse,
    WorkflowJobProgressResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        workflow = client.workflow.create(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
        )
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Structify) -> None:
        workflow = client.workflow.create(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
                "default_banned_domains": ["string"],
                "default_stop_conditions": {
                    "max_steps_without_save": 0,
                    "max_errors": 0,
                    "max_execution_time_secs": 0,
                    "max_total_steps": 0,
                },
            },
        )
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.workflow.with_raw_response.create(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.workflow.with_streaming_response.create(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(str, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Structify) -> None:
        workflow = client.workflow.update(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Structify) -> None:
        workflow = client.workflow.update(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
                "default_banned_domains": ["string"],
                "default_stop_conditions": {
                    "max_steps_without_save": 0,
                    "max_errors": 0,
                    "max_execution_time_secs": 0,
                    "max_total_steps": 0,
                },
            },
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Structify) -> None:
        response = client.workflow.with_raw_response.update(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Structify) -> None:
        with client.workflow.with_streaming_response.update(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(str, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        workflow = client.workflow.list()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        workflow = client.workflow.list(
            dataset_name="dataset_name",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.workflow.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.workflow.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowListResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        workflow = client.workflow.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert workflow is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.workflow.with_raw_response.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.workflow.with_streaming_response.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        workflow = client.workflow.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExistingWorkflow, workflow, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.workflow.with_raw_response.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(ExistingWorkflow, workflow, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.workflow.with_streaming_response.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(ExistingWorkflow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_job_progress(self, client: Structify) -> None:
        workflow = client.workflow.job_progress(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowJobProgressResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_job_progress(self, client: Structify) -> None:
        response = client.workflow.with_raw_response.job_progress(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowJobProgressResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_job_progress(self, client: Structify) -> None:
        with client.workflow.with_streaming_response.job_progress(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowJobProgressResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_jobs(self, client: Structify) -> None:
        workflow = client.workflow.jobs(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowJobsResponse, workflow, path=["response"])

    @parametrize
    def test_method_jobs_with_all_params(self, client: Structify) -> None:
        workflow = client.workflow.jobs(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="Queued",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowJobsResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_jobs(self, client: Structify) -> None:
        response = client.workflow.with_raw_response.jobs(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowJobsResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_jobs(self, client: Structify) -> None:
        with client.workflow.with_streaming_response.jobs(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowJobsResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_trigger(self, client: Structify) -> None:
        workflow = client.workflow.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, workflow, path=["response"])

    @parametrize
    def test_method_trigger_with_all_params(self, client: Structify) -> None:
        workflow = client.workflow.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            banned_domains=["string"],
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(object, workflow, path=["response"])

    @parametrize
    def test_raw_response_trigger(self, client: Structify) -> None:
        response = client.workflow.with_raw_response.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(object, workflow, path=["response"])

    @parametrize
    def test_streaming_response_trigger(self, client: Structify) -> None:
        with client.workflow.with_streaming_response.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(object, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkflow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.create(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
        )
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.create(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
                "default_banned_domains": ["string"],
                "default_stop_conditions": {
                    "max_steps_without_save": 0,
                    "max_errors": 0,
                    "max_execution_time_secs": 0,
                    "max_total_steps": 0,
                },
            },
        )
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow.with_raw_response.create(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow.with_streaming_response.create(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(str, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.update(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.update(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
                "default_banned_domains": ["string"],
                "default_stop_conditions": {
                    "max_steps_without_save": 0,
                    "max_errors": 0,
                    "max_execution_time_secs": 0,
                    "max_total_steps": 0,
                },
            },
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow.with_raw_response.update(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(str, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow.with_streaming_response.update(
            dataset_name="dataset_name",
            workflow={
                "name": "name",
                "starting_step": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "starting_table": "starting_table",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "children": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                        "operation": {"enhance_properties": ["string"]},
                        "table_name": "table_name",
                    }
                ],
            },
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(str, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.list()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.list(
            dataset_name="dataset_name",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowListResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert workflow is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow.with_raw_response.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow.with_streaming_response.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExistingWorkflow, workflow, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow.with_raw_response.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(ExistingWorkflow, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow.with_streaming_response.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(ExistingWorkflow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_job_progress(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.job_progress(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowJobProgressResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_job_progress(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow.with_raw_response.job_progress(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowJobProgressResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_job_progress(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow.with_streaming_response.job_progress(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowJobProgressResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_jobs(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.jobs(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowJobsResponse, workflow, path=["response"])

    @parametrize
    async def test_method_jobs_with_all_params(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.jobs(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="Queued",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowJobsResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_jobs(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow.with_raw_response.jobs(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowJobsResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_jobs(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow.with_streaming_response.jobs(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowJobsResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_trigger(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, workflow, path=["response"])

    @parametrize
    async def test_method_trigger_with_all_params(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            banned_domains=["string"],
            stop_config={
                "max_steps_without_save": 0,
                "max_errors": 0,
                "max_execution_time_secs": 0,
                "max_total_steps": 0,
            },
        )
        assert_matches_type(object, workflow, path=["response"])

    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow.with_raw_response.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(object, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow.with_streaming_response.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(object, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True
