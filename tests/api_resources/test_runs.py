# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    ExecutionStep,
    RunGetResponse,
    RunListResponse,
    RunCancelResponse,
    RunGetStepsResponse,
)
from structify.pagination import SyncRunsList, AsyncRunsList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        run = client.runs.list()
        assert_matches_type(SyncRunsList[RunListResponse], run, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        run = client.runs.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncRunsList[RunListResponse], run, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncRunsList[RunListResponse], run, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncRunsList[RunListResponse], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        run = client.runs.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, run, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.runs.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(str, run, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.runs.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(str, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.runs.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: Structify) -> None:
        run = client.runs.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunCancelResponse, run, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Structify) -> None:
        response = client.runs.with_raw_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCancelResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Structify) -> None:
        with client.runs.with_streaming_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCancelResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.runs.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        run = client.runs.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunGetResponse, run, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.runs.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.runs.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.runs.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_get_step(self, client: Structify) -> None:
        run = client.runs.get_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExecutionStep, run, path=["response"])

    @parametrize
    def test_raw_response_get_step(self, client: Structify) -> None:
        response = client.runs.with_raw_response.get_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(ExecutionStep, run, path=["response"])

    @parametrize
    def test_streaming_response_get_step(self, client: Structify) -> None:
        with client.runs.with_streaming_response.get_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(ExecutionStep, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_step(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.runs.with_raw_response.get_step(
                "",
            )

    @parametrize
    def test_method_get_steps(self, client: Structify) -> None:
        run = client.runs.get_steps(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunGetStepsResponse, run, path=["response"])

    @parametrize
    def test_raw_response_get_steps(self, client: Structify) -> None:
        response = client.runs.with_raw_response.get_steps(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetStepsResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_get_steps(self, client: Structify) -> None:
        with client.runs.with_streaming_response.get_steps(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetStepsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_steps(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.runs.with_raw_response.get_steps(
                "",
            )

    @parametrize
    def test_method_schedule(self, client: Structify) -> None:
        run = client.runs.schedule()
        assert run is None

    @parametrize
    def test_raw_response_schedule(self, client: Structify) -> None:
        response = client.runs.with_raw_response.schedule()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert run is None

    @parametrize
    def test_streaming_response_schedule(self, client: Structify) -> None:
        with client.runs.with_streaming_response.schedule() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert run is None

        assert cast(Any, response.is_closed) is True


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        run = await async_client.runs.list()
        assert_matches_type(AsyncRunsList[RunListResponse], run, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        run = await async_client.runs.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncRunsList[RunListResponse], run, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AsyncRunsList[RunListResponse], run, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncRunsList[RunListResponse], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        run = await async_client.runs.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, run, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.runs.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(str, run, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.runs.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(str, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.runs.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncStructify) -> None:
        run = await async_client.runs.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunCancelResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncStructify) -> None:
        response = await async_client.runs.with_raw_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCancelResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncStructify) -> None:
        async with async_client.runs.with_streaming_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCancelResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.runs.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        run = await async_client.runs.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunGetResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.runs.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.runs.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.runs.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_get_step(self, async_client: AsyncStructify) -> None:
        run = await async_client.runs.get_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExecutionStep, run, path=["response"])

    @parametrize
    async def test_raw_response_get_step(self, async_client: AsyncStructify) -> None:
        response = await async_client.runs.with_raw_response.get_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(ExecutionStep, run, path=["response"])

    @parametrize
    async def test_streaming_response_get_step(self, async_client: AsyncStructify) -> None:
        async with async_client.runs.with_streaming_response.get_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(ExecutionStep, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_step(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.runs.with_raw_response.get_step(
                "",
            )

    @parametrize
    async def test_method_get_steps(self, async_client: AsyncStructify) -> None:
        run = await async_client.runs.get_steps(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunGetStepsResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_get_steps(self, async_client: AsyncStructify) -> None:
        response = await async_client.runs.with_raw_response.get_steps(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetStepsResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_get_steps(self, async_client: AsyncStructify) -> None:
        async with async_client.runs.with_streaming_response.get_steps(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetStepsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_steps(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.runs.with_raw_response.get_steps(
                "",
            )

    @parametrize
    async def test_method_schedule(self, async_client: AsyncStructify) -> None:
        run = await async_client.runs.schedule()
        assert run is None

    @parametrize
    async def test_raw_response_schedule(self, async_client: AsyncStructify) -> None:
        response = await async_client.runs.with_raw_response.schedule()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert run is None

    @parametrize
    async def test_streaming_response_schedule(self, async_client: AsyncStructify) -> None:
        async with async_client.runs.with_streaming_response.schedule() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert run is None

        assert cast(Any, response.is_closed) is True
