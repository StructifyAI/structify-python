# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.admin import (
    ActionTrainingDataResponse,
    DeleteActionTrainingDataResponse,
    ActionTrainingDataMetadataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNextAction:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_training_datum(self, client: Structify) -> None:
        next_action = client.admin.next_action.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_queries": ["string"],
                "seeded_kg": {},
            },
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )
        assert next_action is None

    @parametrize
    def test_method_add_training_datum_with_all_params(self, client: Structify) -> None:
        next_action = client.admin.next_action.add_training_datum(
            input={
                "all_steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "action_name": "action_name",
                        "metadata": {"foo": "string"},
                    }
                ],
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_queries": ["string"],
                "seeded_kg": {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ],
                    "relationships": [
                        {
                            "source": 0,
                            "target": 0,
                            "type": "type",
                            "properties": {"foo": "string"},
                        }
                    ],
                },
            },
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert next_action is None

    @parametrize
    def test_raw_response_add_training_datum(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_queries": ["string"],
                "seeded_kg": {},
            },
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert next_action is None

    @parametrize
    def test_streaming_response_add_training_datum(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_queries": ["string"],
                "seeded_kg": {},
            },
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert next_action is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_training_data(self, client: Structify) -> None:
        next_action = client.admin.next_action.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_raw_response_delete_training_data(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_streaming_response_delete_training_data(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_training_data(self, client: Structify) -> None:
        next_action = client.admin.next_action.get_training_data()
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_method_get_training_data_with_all_params(self, client: Structify) -> None:
        next_action = client.admin.next_action.get_training_data(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
            status="status",
        )
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_raw_response_get_training_data(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.get_training_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_streaming_response_get_training_data(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.get_training_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_training_data_metadata(self, client: Structify) -> None:
        next_action = client.admin.next_action.get_training_data_metadata()
        assert_matches_type(ActionTrainingDataMetadataResponse, next_action, path=["response"])

    @parametrize
    def test_method_get_training_data_metadata_with_all_params(self, client: Structify) -> None:
        next_action = client.admin.next_action.get_training_data_metadata(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
            status="status",
        )
        assert_matches_type(ActionTrainingDataMetadataResponse, next_action, path=["response"])

    @parametrize
    def test_raw_response_get_training_data_metadata(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.get_training_data_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert_matches_type(ActionTrainingDataMetadataResponse, next_action, path=["response"])

    @parametrize
    def test_streaming_response_get_training_data_metadata(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.get_training_data_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert_matches_type(ActionTrainingDataMetadataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_label_training_datum(self, client: Structify) -> None:
        next_action = client.admin.next_action.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )
        assert next_action is None

    @parametrize
    def test_raw_response_label_training_datum(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert next_action is None

    @parametrize
    def test_streaming_response_label_training_datum(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert next_action is None

        assert cast(Any, response.is_closed) is True


class TestAsyncNextAction:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_add_training_datum(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_queries": ["string"],
                "seeded_kg": {},
            },
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )
        assert next_action is None

    @parametrize
    async def test_method_add_training_datum_with_all_params(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.add_training_datum(
            input={
                "all_steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "action_name": "action_name",
                        "metadata": {"foo": "string"},
                    }
                ],
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_queries": ["string"],
                "seeded_kg": {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ],
                    "relationships": [
                        {
                            "source": 0,
                            "target": 0,
                            "type": "type",
                            "properties": {"foo": "string"},
                        }
                    ],
                },
            },
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert next_action is None

    @parametrize
    async def test_raw_response_add_training_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_queries": ["string"],
                "seeded_kg": {},
            },
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert next_action is None

    @parametrize
    async def test_streaming_response_add_training_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_queries": ["string"],
                "seeded_kg": {},
            },
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert next_action is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_training_data(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_raw_response_delete_training_data(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_streaming_response_delete_training_data(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_training_data(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.get_training_data()
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_method_get_training_data_with_all_params(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.get_training_data(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
            status="status",
        )
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_raw_response_get_training_data(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.get_training_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_streaming_response_get_training_data(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.get_training_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_training_data_metadata(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.get_training_data_metadata()
        assert_matches_type(ActionTrainingDataMetadataResponse, next_action, path=["response"])

    @parametrize
    async def test_method_get_training_data_metadata_with_all_params(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.get_training_data_metadata(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
            status="status",
        )
        assert_matches_type(ActionTrainingDataMetadataResponse, next_action, path=["response"])

    @parametrize
    async def test_raw_response_get_training_data_metadata(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.get_training_data_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert_matches_type(ActionTrainingDataMetadataResponse, next_action, path=["response"])

    @parametrize
    async def test_streaming_response_get_training_data_metadata(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.get_training_data_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert_matches_type(ActionTrainingDataMetadataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_label_training_datum(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )
        assert next_action is None

    @parametrize
    async def test_raw_response_label_training_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert next_action is None

    @parametrize
    async def test_streaming_response_label_training_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={"selected_step": {"step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert next_action is None

        assert cast(Any, response.is_closed) is True
