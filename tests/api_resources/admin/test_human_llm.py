# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.admin import HumanLlmUpdateStepResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHumanLlm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update_step(self, client: Structify) -> None:
        human_llm = client.admin.human_llm.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )
        assert_matches_type(HumanLlmUpdateStepResponse, human_llm, path=["response"])

    @parametrize
    def test_raw_response_update_step(self, client: Structify) -> None:
        response = client.admin.human_llm.with_raw_response.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = response.parse()
        assert_matches_type(HumanLlmUpdateStepResponse, human_llm, path=["response"])

    @parametrize
    def test_streaming_response_update_step(self, client: Structify) -> None:
        with client.admin.human_llm.with_streaming_response.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = response.parse()
            assert_matches_type(HumanLlmUpdateStepResponse, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHumanLlm:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update_step(self, async_client: AsyncStructify) -> None:
        human_llm = await async_client.admin.human_llm.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )
        assert_matches_type(HumanLlmUpdateStepResponse, human_llm, path=["response"])

    @parametrize
    async def test_raw_response_update_step(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.human_llm.with_raw_response.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = await response.parse()
        assert_matches_type(HumanLlmUpdateStepResponse, human_llm, path=["response"])

    @parametrize
    async def test_streaming_response_update_step(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.human_llm.with_streaming_response.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = await response.parse()
            assert_matches_type(HumanLlmUpdateStepResponse, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True