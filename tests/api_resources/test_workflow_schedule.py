# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    WorkflowScheduleInfo,
    WorkflowScheduleGetResponse,
    WorkflowScheduleGetAllResponse,
    GetWorkflowScheduleSessionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflowSchedule:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        workflow_schedule = client.workflow_schedule.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            git_commit_hash="git_commit_hash",
            name="name",
        )
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Structify) -> None:
        workflow_schedule = client.workflow_schedule.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            git_commit_hash="git_commit_hash",
            name="name",
            cron_schedule="cron_schedule",
        )
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.workflow_schedule.with_raw_response.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            git_commit_hash="git_commit_hash",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = response.parse()
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.workflow_schedule.with_streaming_response.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            git_commit_hash="git_commit_hash",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = response.parse()
            assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_session_id` but received ''"):
            client.workflow_schedule.with_raw_response.create(
                chat_session_id="",
                git_commit_hash="git_commit_hash",
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Structify) -> None:
        workflow_schedule = client.workflow_schedule.update(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Structify) -> None:
        workflow_schedule = client.workflow_schedule.update(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cron_schedule="cron_schedule",
            git_commit_hash="git_commit_hash",
            name="name",
        )
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Structify) -> None:
        response = client.workflow_schedule.with_raw_response.update(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = response.parse()
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Structify) -> None:
        with client.workflow_schedule.with_streaming_response.update(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = response.parse()
            assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.workflow_schedule.with_raw_response.update(
                schedule_id="",
            )

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        workflow_schedule = client.workflow_schedule.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert workflow_schedule is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.workflow_schedule.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = response.parse()
        assert workflow_schedule is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.workflow_schedule.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = response.parse()
            assert workflow_schedule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.workflow_schedule.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        workflow_schedule = client.workflow_schedule.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowScheduleGetResponse, workflow_schedule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.workflow_schedule.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = response.parse()
        assert_matches_type(WorkflowScheduleGetResponse, workflow_schedule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.workflow_schedule.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = response.parse()
            assert_matches_type(WorkflowScheduleGetResponse, workflow_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_session_id` but received ''"):
            client.workflow_schedule.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_get_all(self, client: Structify) -> None:
        workflow_schedule = client.workflow_schedule.get_all()
        assert_matches_type(WorkflowScheduleGetAllResponse, workflow_schedule, path=["response"])

    @parametrize
    def test_raw_response_get_all(self, client: Structify) -> None:
        response = client.workflow_schedule.with_raw_response.get_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = response.parse()
        assert_matches_type(WorkflowScheduleGetAllResponse, workflow_schedule, path=["response"])

    @parametrize
    def test_streaming_response_get_all(self, client: Structify) -> None:
        with client.workflow_schedule.with_streaming_response.get_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = response.parse()
            assert_matches_type(WorkflowScheduleGetAllResponse, workflow_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_sessions(self, client: Structify) -> None:
        workflow_schedule = client.workflow_schedule.get_sessions(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetWorkflowScheduleSessionsResponse, workflow_schedule, path=["response"])

    @parametrize
    def test_method_get_sessions_with_all_params(self, client: Structify) -> None:
        workflow_schedule = client.workflow_schedule.get_sessions(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
        )
        assert_matches_type(GetWorkflowScheduleSessionsResponse, workflow_schedule, path=["response"])

    @parametrize
    def test_raw_response_get_sessions(self, client: Structify) -> None:
        response = client.workflow_schedule.with_raw_response.get_sessions(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = response.parse()
        assert_matches_type(GetWorkflowScheduleSessionsResponse, workflow_schedule, path=["response"])

    @parametrize
    def test_streaming_response_get_sessions(self, client: Structify) -> None:
        with client.workflow_schedule.with_streaming_response.get_sessions(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = response.parse()
            assert_matches_type(GetWorkflowScheduleSessionsResponse, workflow_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_sessions(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.workflow_schedule.with_raw_response.get_sessions(
                schedule_id="",
            )


class TestAsyncWorkflowSchedule:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        workflow_schedule = await async_client.workflow_schedule.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            git_commit_hash="git_commit_hash",
            name="name",
        )
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStructify) -> None:
        workflow_schedule = await async_client.workflow_schedule.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            git_commit_hash="git_commit_hash",
            name="name",
            cron_schedule="cron_schedule",
        )
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow_schedule.with_raw_response.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            git_commit_hash="git_commit_hash",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = await response.parse()
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow_schedule.with_streaming_response.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            git_commit_hash="git_commit_hash",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = await response.parse()
            assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_session_id` but received ''"):
            await async_client.workflow_schedule.with_raw_response.create(
                chat_session_id="",
                git_commit_hash="git_commit_hash",
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncStructify) -> None:
        workflow_schedule = await async_client.workflow_schedule.update(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStructify) -> None:
        workflow_schedule = await async_client.workflow_schedule.update(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cron_schedule="cron_schedule",
            git_commit_hash="git_commit_hash",
            name="name",
        )
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow_schedule.with_raw_response.update(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = await response.parse()
        assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow_schedule.with_streaming_response.update(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = await response.parse()
            assert_matches_type(WorkflowScheduleInfo, workflow_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.workflow_schedule.with_raw_response.update(
                schedule_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        workflow_schedule = await async_client.workflow_schedule.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert workflow_schedule is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow_schedule.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = await response.parse()
        assert workflow_schedule is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow_schedule.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = await response.parse()
            assert workflow_schedule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.workflow_schedule.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        workflow_schedule = await async_client.workflow_schedule.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowScheduleGetResponse, workflow_schedule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow_schedule.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = await response.parse()
        assert_matches_type(WorkflowScheduleGetResponse, workflow_schedule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow_schedule.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = await response.parse()
            assert_matches_type(WorkflowScheduleGetResponse, workflow_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_session_id` but received ''"):
            await async_client.workflow_schedule.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_get_all(self, async_client: AsyncStructify) -> None:
        workflow_schedule = await async_client.workflow_schedule.get_all()
        assert_matches_type(WorkflowScheduleGetAllResponse, workflow_schedule, path=["response"])

    @parametrize
    async def test_raw_response_get_all(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow_schedule.with_raw_response.get_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = await response.parse()
        assert_matches_type(WorkflowScheduleGetAllResponse, workflow_schedule, path=["response"])

    @parametrize
    async def test_streaming_response_get_all(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow_schedule.with_streaming_response.get_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = await response.parse()
            assert_matches_type(WorkflowScheduleGetAllResponse, workflow_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_sessions(self, async_client: AsyncStructify) -> None:
        workflow_schedule = await async_client.workflow_schedule.get_sessions(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetWorkflowScheduleSessionsResponse, workflow_schedule, path=["response"])

    @parametrize
    async def test_method_get_sessions_with_all_params(self, async_client: AsyncStructify) -> None:
        workflow_schedule = await async_client.workflow_schedule.get_sessions(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
        )
        assert_matches_type(GetWorkflowScheduleSessionsResponse, workflow_schedule, path=["response"])

    @parametrize
    async def test_raw_response_get_sessions(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow_schedule.with_raw_response.get_sessions(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_schedule = await response.parse()
        assert_matches_type(GetWorkflowScheduleSessionsResponse, workflow_schedule, path=["response"])

    @parametrize
    async def test_streaming_response_get_sessions(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow_schedule.with_streaming_response.get_sessions(
            schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_schedule = await response.parse()
            assert_matches_type(GetWorkflowScheduleSessionsResponse, workflow_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_sessions(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.workflow_schedule.with_raw_response.get_sessions(
                schedule_id="",
            )
