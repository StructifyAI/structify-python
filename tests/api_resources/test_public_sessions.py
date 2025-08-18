# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import WorkflowDag
from structify._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPublicSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_latest_workflow(self, client: Structify) -> None:
        public_session = client.public_sessions.get_latest_workflow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowDag, public_session, path=["response"])

    @parametrize
    def test_raw_response_get_latest_workflow(self, client: Structify) -> None:
        response = client.public_sessions.with_raw_response.get_latest_workflow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_session = response.parse()
        assert_matches_type(WorkflowDag, public_session, path=["response"])

    @parametrize
    def test_streaming_response_get_latest_workflow(self, client: Structify) -> None:
        with client.public_sessions.with_streaming_response.get_latest_workflow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_session = response.parse()
            assert_matches_type(WorkflowDag, public_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_latest_workflow(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_session_id` but received ''"):
            client.public_sessions.with_raw_response.get_latest_workflow(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_node_output_data(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/public/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        public_session = client.public_sessions.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert public_session.is_closed
        assert public_session.json() == {"foo": "bar"}
        assert cast(Any, public_session.is_closed) is True
        assert isinstance(public_session, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_node_output_data(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/public/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        public_session = client.public_sessions.with_raw_response.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert public_session.is_closed is True
        assert public_session.http_request.headers.get("X-Stainless-Lang") == "python"
        assert public_session.json() == {"foo": "bar"}
        assert isinstance(public_session, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_node_output_data(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/public/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.public_sessions.with_streaming_response.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as public_session:
            assert not public_session.is_closed
            assert public_session.http_request.headers.get("X-Stainless-Lang") == "python"

            assert public_session.json() == {"foo": "bar"}
            assert cast(Any, public_session.is_closed) is True
            assert isinstance(public_session, StreamedBinaryAPIResponse)

        assert cast(Any, public_session.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_node_output_data(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            client.public_sessions.with_raw_response.get_node_output_data(
                "",
            )


class TestAsyncPublicSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_latest_workflow(self, async_client: AsyncStructify) -> None:
        public_session = await async_client.public_sessions.get_latest_workflow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowDag, public_session, path=["response"])

    @parametrize
    async def test_raw_response_get_latest_workflow(self, async_client: AsyncStructify) -> None:
        response = await async_client.public_sessions.with_raw_response.get_latest_workflow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_session = await response.parse()
        assert_matches_type(WorkflowDag, public_session, path=["response"])

    @parametrize
    async def test_streaming_response_get_latest_workflow(self, async_client: AsyncStructify) -> None:
        async with async_client.public_sessions.with_streaming_response.get_latest_workflow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_session = await response.parse()
            assert_matches_type(WorkflowDag, public_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_latest_workflow(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_session_id` but received ''"):
            await async_client.public_sessions.with_raw_response.get_latest_workflow(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_node_output_data(self, async_client: AsyncStructify, respx_mock: MockRouter) -> None:
        respx_mock.get("/public/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        public_session = await async_client.public_sessions.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert public_session.is_closed
        assert await public_session.json() == {"foo": "bar"}
        assert cast(Any, public_session.is_closed) is True
        assert isinstance(public_session, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_node_output_data(
        self, async_client: AsyncStructify, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/public/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        public_session = await async_client.public_sessions.with_raw_response.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert public_session.is_closed is True
        assert public_session.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await public_session.json() == {"foo": "bar"}
        assert isinstance(public_session, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_node_output_data(
        self, async_client: AsyncStructify, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/public/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.public_sessions.with_streaming_response.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as public_session:
            assert not public_session.is_closed
            assert public_session.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await public_session.json() == {"foo": "bar"}
            assert cast(Any, public_session.is_closed) is True
            assert isinstance(public_session, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, public_session.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_node_output_data(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            await async_client.public_sessions.with_raw_response.get_node_output_data(
                "",
            )
