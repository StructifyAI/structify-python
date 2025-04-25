# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.datasets import (
    WorkflowGetResponse,
    WorkflowListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        workflow = client.datasets.workflow.create(
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
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.datasets.workflow.with_raw_response.create(
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
        with client.datasets.workflow.with_streaming_response.create(
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
        workflow = client.datasets.workflow.update(
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
    def test_raw_response_update(self, client: Structify) -> None:
        response = client.datasets.workflow.with_raw_response.update(
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
        with client.datasets.workflow.with_streaming_response.update(
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
        workflow = client.datasets.workflow.list()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        workflow = client.datasets.workflow.list(
            dataset_name="dataset_name",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.datasets.workflow.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.datasets.workflow.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowListResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        workflow = client.datasets.workflow.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert workflow is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.datasets.workflow.with_raw_response.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.datasets.workflow.with_streaming_response.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        workflow = client.datasets.workflow.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.datasets.workflow.with_raw_response.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.datasets.workflow.with_streaming_response.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_trigger(self, client: Structify) -> None:
        workflow = client.datasets.workflow.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, workflow, path=["response"])

    @parametrize
    def test_raw_response_trigger(self, client: Structify) -> None:
        response = client.datasets.workflow.with_raw_response.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(object, workflow, path=["response"])

    @parametrize
    def test_streaming_response_trigger(self, client: Structify) -> None:
        with client.datasets.workflow.with_streaming_response.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(object, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkflow:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.datasets.workflow.create(
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
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.workflow.with_raw_response.create(
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
        async with async_client.datasets.workflow.with_streaming_response.create(
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
        workflow = await async_client.datasets.workflow.update(
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
    async def test_raw_response_update(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.workflow.with_raw_response.update(
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
        async with async_client.datasets.workflow.with_streaming_response.update(
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
        workflow = await async_client.datasets.workflow.list()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.datasets.workflow.list(
            dataset_name="dataset_name",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.workflow.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.workflow.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowListResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.datasets.workflow.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert workflow is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.workflow.with_raw_response.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.workflow.with_streaming_response.delete(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.datasets.workflow.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.workflow.with_raw_response.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.workflow.with_streaming_response.get(
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_trigger(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.datasets.workflow.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, workflow, path=["response"])

    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.workflow.with_raw_response.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(object, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.workflow.with_streaming_response.trigger(
            entity_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            workflow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(object, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True
