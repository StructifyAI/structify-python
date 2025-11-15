# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCode:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate_code(self, client: Structify) -> None:
        code = client.code.generate_code(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        )
        assert code is None

    @parametrize
    def test_method_generate_code_with_all_params(self, client: Structify) -> None:
        code = client.code.generate_code(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
            assistant_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={
                "llm_key": "vllm.gpt-5-mini-2025-08-07",
                "reminder_message": "reminder_message",
                "system_prompt": "system_prompt",
            },
            trigger_workflow_execution=True,
            user_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert code is None

    @parametrize
    def test_raw_response_generate_code(self, client: Structify) -> None:
        response = client.code.with_raw_response.generate_code(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        code = response.parse()
        assert code is None

    @parametrize
    def test_streaming_response_generate_code(self, client: Structify) -> None:
        with client.code.with_streaming_response.generate_code(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            code = response.parse()
            assert code is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_interrupt_generation(self, client: Structify) -> None:
        code = client.code.interrupt_generation(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert code is None

    @parametrize
    def test_raw_response_interrupt_generation(self, client: Structify) -> None:
        response = client.code.with_raw_response.interrupt_generation(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        code = response.parse()
        assert code is None

    @parametrize
    def test_streaming_response_interrupt_generation(self, client: Structify) -> None:
        with client.code.with_streaming_response.interrupt_generation(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            code = response.parse()
            assert code is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCode:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_generate_code(self, async_client: AsyncStructify) -> None:
        code = await async_client.code.generate_code(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        )
        assert code is None

    @parametrize
    async def test_method_generate_code_with_all_params(self, async_client: AsyncStructify) -> None:
        code = await async_client.code.generate_code(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
            assistant_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={
                "llm_key": "vllm.gpt-5-mini-2025-08-07",
                "reminder_message": "reminder_message",
                "system_prompt": "system_prompt",
            },
            trigger_workflow_execution=True,
            user_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert code is None

    @parametrize
    async def test_raw_response_generate_code(self, async_client: AsyncStructify) -> None:
        response = await async_client.code.with_raw_response.generate_code(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        code = await response.parse()
        assert code is None

    @parametrize
    async def test_streaming_response_generate_code(self, async_client: AsyncStructify) -> None:
        async with async_client.code.with_streaming_response.generate_code(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            code = await response.parse()
            assert code is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_interrupt_generation(self, async_client: AsyncStructify) -> None:
        code = await async_client.code.interrupt_generation(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert code is None

    @parametrize
    async def test_raw_response_interrupt_generation(self, async_client: AsyncStructify) -> None:
        response = await async_client.code.with_raw_response.interrupt_generation(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        code = await response.parse()
        assert code is None

    @parametrize
    async def test_streaming_response_interrupt_generation(self, async_client: AsyncStructify) -> None:
        async with async_client.code.with_streaming_response.interrupt_generation(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            code = await response.parse()
            assert code is None

        assert cast(Any, response.is_closed) is True
