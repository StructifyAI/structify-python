# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    WorkflowSession,
    WorkflowSessionEdge,
    WorkflowSessionNode,
    GetWorkflowDagResponse,
    GetSessionEventsResponse,
)
from structify._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_edge(self, client: Structify) -> None:
        session = client.sessions.create_edge(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowSessionEdge, session, path=["response"])

    @parametrize
    def test_raw_response_create_edge(self, client: Structify) -> None:
        response = client.sessions.with_raw_response.create_edge(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(WorkflowSessionEdge, session, path=["response"])

    @parametrize
    def test_streaming_response_create_edge(self, client: Structify) -> None:
        with client.sessions.with_streaming_response.create_edge(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(WorkflowSessionEdge, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_edge(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.create_edge(
                session_id="",
                source_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                target_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_create_node(self, client: Structify) -> None:
        session = client.sessions.create_node(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            docstring="docstring",
            function_name="function_name",
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    def test_method_create_node_with_all_params(self, client: Structify) -> None:
        session = client.sessions.create_node(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            docstring="docstring",
            function_name="function_name",
            output_schema={},
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    def test_raw_response_create_node(self, client: Structify) -> None:
        response = client.sessions.with_raw_response.create_node(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            docstring="docstring",
            function_name="function_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    def test_streaming_response_create_node(self, client: Structify) -> None:
        with client.sessions.with_streaming_response.create_node(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            docstring="docstring",
            function_name="function_name",
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
                session_id="",
                docstring="docstring",
                function_name="function_name",
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
    def test_method_get_dag(self, client: Structify) -> None:
        session = client.sessions.get_dag(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetWorkflowDagResponse, session, path=["response"])

    @parametrize
    def test_raw_response_get_dag(self, client: Structify) -> None:
        response = client.sessions.with_raw_response.get_dag(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(GetWorkflowDagResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_get_dag(self, client: Structify) -> None:
        with client.sessions.with_streaming_response.get_dag(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(GetWorkflowDagResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_dag(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.get_dag(
                "",
            )

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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_node_output_data(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/sessions/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        session = client.sessions.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert session.is_closed
        assert session.json() == {"foo": "bar"}
        assert cast(Any, session.is_closed) is True
        assert isinstance(session, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_node_output_data(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/sessions/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        session = client.sessions.with_raw_response.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert session.is_closed is True
        assert session.http_request.headers.get("X-Stainless-Lang") == "python"
        assert session.json() == {"foo": "bar"}
        assert isinstance(session, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_node_output_data(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/sessions/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.sessions.with_streaming_response.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as session:
            assert not session.is_closed
            assert session.http_request.headers.get("X-Stainless-Lang") == "python"

            assert session.json() == {"foo": "bar"}
            assert cast(Any, session.is_closed) is True
            assert isinstance(session, StreamedBinaryAPIResponse)

        assert cast(Any, session.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_node_output_data(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            client.sessions.with_raw_response.get_node_output_data(
                "",
            )

    @parametrize
    def test_method_mark_errored(self, client: Structify) -> None:
        session = client.sessions.mark_errored(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error_message="error_message",
        )
        assert_matches_type(WorkflowSession, session, path=["response"])

    @parametrize
    def test_method_mark_errored_with_all_params(self, client: Structify) -> None:
        session = client.sessions.mark_errored(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error_message="error_message",
            error_traceback="error_traceback",
        )
        assert_matches_type(WorkflowSession, session, path=["response"])

    @parametrize
    def test_raw_response_mark_errored(self, client: Structify) -> None:
        response = client.sessions.with_raw_response.mark_errored(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error_message="error_message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(WorkflowSession, session, path=["response"])

    @parametrize
    def test_streaming_response_mark_errored(self, client: Structify) -> None:
        with client.sessions.with_streaming_response.mark_errored(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error_message="error_message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(WorkflowSession, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_mark_errored(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.mark_errored(
                session_id="",
                error_message="error_message",
            )

    @parametrize
    def test_method_update_node(self, client: Structify) -> None:
        session = client.sessions.update_node(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            execution_status="Unexecuted",
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    def test_method_update_node_with_all_params(self, client: Structify) -> None:
        session = client.sessions.update_node(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            execution_status="Unexecuted",
            error_message="error_message",
            error_traceback="error_traceback",
            execution_time_ms=0,
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    def test_raw_response_update_node(self, client: Structify) -> None:
        response = client.sessions.with_raw_response.update_node(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            execution_status="Unexecuted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    def test_streaming_response_update_node(self, client: Structify) -> None:
        with client.sessions.with_streaming_response.update_node(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            execution_status="Unexecuted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(WorkflowSessionNode, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_node(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            client.sessions.with_raw_response.update_node(
                node_id="",
                execution_status="Unexecuted",
            )

    @parametrize
    def test_method_upload_node_output_data(self, client: Structify) -> None:
        session = client.sessions.upload_node_output_data(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    def test_raw_response_upload_node_output_data(self, client: Structify) -> None:
        response = client.sessions.with_raw_response.upload_node_output_data(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    def test_streaming_response_upload_node_output_data(self, client: Structify) -> None:
        with client.sessions.with_streaming_response.upload_node_output_data(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(WorkflowSessionNode, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upload_node_output_data(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            client.sessions.with_raw_response.upload_node_output_data(
                node_id="",
                content=b"raw file contents",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_edge(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.create_edge(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WorkflowSessionEdge, session, path=["response"])

    @parametrize
    async def test_raw_response_create_edge(self, async_client: AsyncStructify) -> None:
        response = await async_client.sessions.with_raw_response.create_edge(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(WorkflowSessionEdge, session, path=["response"])

    @parametrize
    async def test_streaming_response_create_edge(self, async_client: AsyncStructify) -> None:
        async with async_client.sessions.with_streaming_response.create_edge(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(WorkflowSessionEdge, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_edge(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.create_edge(
                session_id="",
                source_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                target_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_create_node(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.create_node(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            docstring="docstring",
            function_name="function_name",
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    async def test_method_create_node_with_all_params(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.create_node(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            docstring="docstring",
            function_name="function_name",
            output_schema={},
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    async def test_raw_response_create_node(self, async_client: AsyncStructify) -> None:
        response = await async_client.sessions.with_raw_response.create_node(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            docstring="docstring",
            function_name="function_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    async def test_streaming_response_create_node(self, async_client: AsyncStructify) -> None:
        async with async_client.sessions.with_streaming_response.create_node(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            docstring="docstring",
            function_name="function_name",
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
                session_id="",
                docstring="docstring",
                function_name="function_name",
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
    async def test_method_get_dag(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.get_dag(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetWorkflowDagResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_get_dag(self, async_client: AsyncStructify) -> None:
        response = await async_client.sessions.with_raw_response.get_dag(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(GetWorkflowDagResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_get_dag(self, async_client: AsyncStructify) -> None:
        async with async_client.sessions.with_streaming_response.get_dag(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(GetWorkflowDagResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_dag(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.get_dag(
                "",
            )

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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_node_output_data(self, async_client: AsyncStructify, respx_mock: MockRouter) -> None:
        respx_mock.get("/sessions/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        session = await async_client.sessions.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert session.is_closed
        assert await session.json() == {"foo": "bar"}
        assert cast(Any, session.is_closed) is True
        assert isinstance(session, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_node_output_data(
        self, async_client: AsyncStructify, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/sessions/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        session = await async_client.sessions.with_raw_response.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert session.is_closed is True
        assert session.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await session.json() == {"foo": "bar"}
        assert isinstance(session, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_node_output_data(
        self, async_client: AsyncStructify, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/sessions/nodes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/output_data").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.sessions.with_streaming_response.get_node_output_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as session:
            assert not session.is_closed
            assert session.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await session.json() == {"foo": "bar"}
            assert cast(Any, session.is_closed) is True
            assert isinstance(session, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, session.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_node_output_data(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            await async_client.sessions.with_raw_response.get_node_output_data(
                "",
            )

    @parametrize
    async def test_method_mark_errored(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.mark_errored(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error_message="error_message",
        )
        assert_matches_type(WorkflowSession, session, path=["response"])

    @parametrize
    async def test_method_mark_errored_with_all_params(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.mark_errored(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error_message="error_message",
            error_traceback="error_traceback",
        )
        assert_matches_type(WorkflowSession, session, path=["response"])

    @parametrize
    async def test_raw_response_mark_errored(self, async_client: AsyncStructify) -> None:
        response = await async_client.sessions.with_raw_response.mark_errored(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error_message="error_message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(WorkflowSession, session, path=["response"])

    @parametrize
    async def test_streaming_response_mark_errored(self, async_client: AsyncStructify) -> None:
        async with async_client.sessions.with_streaming_response.mark_errored(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error_message="error_message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(WorkflowSession, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_mark_errored(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.mark_errored(
                session_id="",
                error_message="error_message",
            )

    @parametrize
    async def test_method_update_node(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.update_node(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            execution_status="Unexecuted",
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    async def test_method_update_node_with_all_params(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.update_node(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            execution_status="Unexecuted",
            error_message="error_message",
            error_traceback="error_traceback",
            execution_time_ms=0,
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    async def test_raw_response_update_node(self, async_client: AsyncStructify) -> None:
        response = await async_client.sessions.with_raw_response.update_node(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            execution_status="Unexecuted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    async def test_streaming_response_update_node(self, async_client: AsyncStructify) -> None:
        async with async_client.sessions.with_streaming_response.update_node(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            execution_status="Unexecuted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(WorkflowSessionNode, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_node(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            await async_client.sessions.with_raw_response.update_node(
                node_id="",
                execution_status="Unexecuted",
            )

    @parametrize
    async def test_method_upload_node_output_data(self, async_client: AsyncStructify) -> None:
        session = await async_client.sessions.upload_node_output_data(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        )
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    async def test_raw_response_upload_node_output_data(self, async_client: AsyncStructify) -> None:
        response = await async_client.sessions.with_raw_response.upload_node_output_data(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(WorkflowSessionNode, session, path=["response"])

    @parametrize
    async def test_streaming_response_upload_node_output_data(self, async_client: AsyncStructify) -> None:
        async with async_client.sessions.with_streaming_response.upload_node_output_data(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(WorkflowSessionNode, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upload_node_output_data(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            await async_client.sessions.with_raw_response.upload_node_output_data(
                node_id="",
                content=b"raw file contents",
            )
