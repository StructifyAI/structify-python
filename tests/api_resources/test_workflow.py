# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_run(self, client: Structify) -> None:
        workflow = client.workflow.run(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            use_node_cache=True,
        )
        assert workflow is None

    @parametrize
    def test_raw_response_run(self, client: Structify) -> None:
        response = client.workflow.with_raw_response.run(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            use_node_cache=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @parametrize
    def test_streaming_response_run(self, client: Structify) -> None:
        with client.workflow.with_streaming_response.run(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            use_node_cache=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stop(self, client: Structify) -> None:
        workflow = client.workflow.stop(
            workflow_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert workflow is None

    @parametrize
    def test_raw_response_stop(self, client: Structify) -> None:
        response = client.workflow.with_raw_response.stop(
            workflow_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @parametrize
    def test_streaming_response_stop(self, client: Structify) -> None:
        with client.workflow.with_streaming_response.stop(
            workflow_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkflow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_run(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.run(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            use_node_cache=True,
        )
        assert workflow is None

    @parametrize
    async def test_raw_response_run(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow.with_raw_response.run(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            use_node_cache=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow.with_streaming_response.run(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            use_node_cache=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stop(self, async_client: AsyncStructify) -> None:
        workflow = await async_client.workflow.stop(
            workflow_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert workflow is None

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncStructify) -> None:
        response = await async_client.workflow.with_raw_response.stop(
            workflow_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncStructify) -> None:
        async with async_client.workflow.with_streaming_response.stop(
            workflow_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True
