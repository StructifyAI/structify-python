# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    WorkflowSession,
    WorkflowSessionNode,
    GetSessionEventsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_node(self, client: Structify) -> None:
        session = client.sessions.create_node(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    def test_raw_response_create_node(self, client: Structify) -> None:
        response = client.sessions.with_raw_response.create_node(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    def test_streaming_response_create_node(self, client: Structify) -> None:
        with client.sessions.with_streaming_response.create_node(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(WorkflowSessionNode, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_node(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.create_node(
                "",
            )

    @parametrize
    def test_method_create_session(self, client: Structify) -> None:
        session = client.sessions.create_session(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowSession, session, path=["response"])

    @parametrize
    def test_raw_response_create_session(self, client: Structify) -> None:
        response = client.sessions.with_raw_response.create_session(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(WorkflowSession, session, path=["response"])

    @parametrize
    def test_streaming_response_create_session(self, client: Structify) -> None:
        with client.sessions.with_streaming_response.create_session(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(WorkflowSession, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_events(self, client: Structify) -> None:
        session = client.sessions.get_events(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetSessionEventsResponse, session, path=["response"])

    @parametrize
    def test_method_get_events_with_all_params(self, client: Structify) -> None:
        session = client.sessions.get_events(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
        )
        assert_matches_type(GetSessionEventsResponse, session, path=["response"])

    @parametrize
    def test_raw_response_get_events(self, client: Structify) -> None:
        response = client.sessions.with_raw_response.get_events(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(GetSessionEventsResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_get_events(self, client: Structify) -> None:
        with client.sessions.with_streaming_response.get_events(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(GetSessionEventsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_events(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.get_events(
                session_id="",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_node(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.create_node(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    async def test_raw_response_create_node(self, async_client: AsyncStructify) -> None:
        response = await async_client.sessions.with_raw_response.create_node(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    async def test_streaming_response_create_node(self, async_client: AsyncStructify) -> None:
        async with async_client.sessions.with_streaming_response.create_node(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(WorkflowSessionNode, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_node(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.create_node(
                "",
            )

    @parametrize
    async def test_method_create_session(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.create_session(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowSession, session, path=["response"])

    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncStructify) -> None:
        response = await async_client.sessions.with_raw_response.create_session(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(WorkflowSession, session, path=["response"])

    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncStructify) -> None:
        async with async_client.sessions.with_streaming_response.create_session(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(WorkflowSession, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_events(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.get_events(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetSessionEventsResponse, session, path=["response"])

    @parametrize
    async def test_method_get_events_with_all_params(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.get_events(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
        )
        assert_matches_type(GetSessionEventsResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_get_events(self, async_client: AsyncStructify) -> None:
        response = await async_client.sessions.with_raw_response.get_events(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(GetSessionEventsResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_get_events(self, async_client: AsyncStructify) -> None:
        async with async_client.sessions.with_streaming_response.get_events(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(GetSessionEventsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_events(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.get_events(
                session_id="",
            )
