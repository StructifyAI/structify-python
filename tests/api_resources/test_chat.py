# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    AddChatMessageResponse,
    GetChatSessionResponse,
    ChatAddGitCommitResponse,
    ChatGetGitCommitResponse,
    ListChatSessionsResponse,
    CreateChatSessionResponse,
    DeleteChatSessionResponse,
    ChatGetSessionTimelineResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_git_commit(self, client: Structify) -> None:
        chat = client.chat.add_git_commit(
            session_id="session_id",
            commit_hash="commit_hash",
        )
        assert_matches_type(ChatAddGitCommitResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_add_git_commit(self, client: Structify) -> None:
        response = client.chat.with_raw_response.add_git_commit(
            session_id="session_id",
            commit_hash="commit_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatAddGitCommitResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_add_git_commit(self, client: Structify) -> None:
        with client.chat.with_streaming_response.add_git_commit(
            session_id="session_id",
            commit_hash="commit_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatAddGitCommitResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_git_commit(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.chat.with_raw_response.add_git_commit(
                session_id="",
                commit_hash="commit_hash",
            )

    @parametrize
    def test_method_add_message(self, client: Structify) -> None:
        chat = client.chat.add_message(
            session_id="session_id",
            content="content",
            role="role",
        )
        assert_matches_type(AddChatMessageResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_add_message(self, client: Structify) -> None:
        response = client.chat.with_raw_response.add_message(
            session_id="session_id",
            content="content",
            role="role",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(AddChatMessageResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_add_message(self, client: Structify) -> None:
        with client.chat.with_streaming_response.add_message(
            session_id="session_id",
            content="content",
            role="role",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(AddChatMessageResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_message(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.chat.with_raw_response.add_message(
                session_id="",
                content="content",
                role="role",
            )

    @parametrize
    def test_method_create_session(self, client: Structify) -> None:
        chat = client.chat.create_session(
            git_repo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            initial_message="initial_message",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create_session(self, client: Structify) -> None:
        response = client.chat.with_raw_response.create_session(
            git_repo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            initial_message="initial_message",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create_session(self, client: Structify) -> None:
        with client.chat.with_streaming_response.create_session(
            git_repo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            initial_message="initial_message",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_session(self, client: Structify) -> None:
        chat = client.chat.delete_session(
            "session_id",
        )
        assert_matches_type(DeleteChatSessionResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_delete_session(self, client: Structify) -> None:
        response = client.chat.with_raw_response.delete_session(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(DeleteChatSessionResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_delete_session(self, client: Structify) -> None:
        with client.chat.with_streaming_response.delete_session(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(DeleteChatSessionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_session(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.chat.with_raw_response.delete_session(
                "",
            )

    @parametrize
    def test_method_get_git_commit(self, client: Structify) -> None:
        chat = client.chat.get_git_commit(
            commit_hash="commit_hash",
            chat_id="chat_id",
        )
        assert_matches_type(ChatGetGitCommitResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_get_git_commit(self, client: Structify) -> None:
        response = client.chat.with_raw_response.get_git_commit(
            commit_hash="commit_hash",
            chat_id="chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatGetGitCommitResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_get_git_commit(self, client: Structify) -> None:
        with client.chat.with_streaming_response.get_git_commit(
            commit_hash="commit_hash",
            chat_id="chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatGetGitCommitResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_git_commit(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chat.with_raw_response.get_git_commit(
                commit_hash="commit_hash",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commit_hash` but received ''"):
            client.chat.with_raw_response.get_git_commit(
                commit_hash="",
                chat_id="chat_id",
            )

    @parametrize
    def test_method_get_session(self, client: Structify) -> None:
        chat = client.chat.get_session(
            "session_id",
        )
        assert_matches_type(GetChatSessionResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_get_session(self, client: Structify) -> None:
        response = client.chat.with_raw_response.get_session(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(GetChatSessionResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_get_session(self, client: Structify) -> None:
        with client.chat.with_streaming_response.get_session(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(GetChatSessionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_session(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.chat.with_raw_response.get_session(
                "",
            )

    @parametrize
    def test_method_get_session_timeline(self, client: Structify) -> None:
        chat = client.chat.get_session_timeline(
            "session_id",
        )
        assert_matches_type(ChatGetSessionTimelineResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_get_session_timeline(self, client: Structify) -> None:
        response = client.chat.with_raw_response.get_session_timeline(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatGetSessionTimelineResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_get_session_timeline(self, client: Structify) -> None:
        with client.chat.with_streaming_response.get_session_timeline(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatGetSessionTimelineResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_session_timeline(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.chat.with_raw_response.get_session_timeline(
                "",
            )

    @parametrize
    def test_method_list_sessions(self, client: Structify) -> None:
        chat = client.chat.list_sessions()
        assert_matches_type(ListChatSessionsResponse, chat, path=["response"])

    @parametrize
    def test_method_list_sessions_with_all_params(self, client: Structify) -> None:
        chat = client.chat.list_sessions(
            limit=0,
        )
        assert_matches_type(ListChatSessionsResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_list_sessions(self, client: Structify) -> None:
        response = client.chat.with_raw_response.list_sessions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ListChatSessionsResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_list_sessions(self, client: Structify) -> None:
        with client.chat.with_streaming_response.list_sessions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ListChatSessionsResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_add_git_commit(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.add_git_commit(
            session_id="session_id",
            commit_hash="commit_hash",
        )
        assert_matches_type(ChatAddGitCommitResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_add_git_commit(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.add_git_commit(
            session_id="session_id",
            commit_hash="commit_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatAddGitCommitResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_add_git_commit(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.add_git_commit(
            session_id="session_id",
            commit_hash="commit_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatAddGitCommitResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_git_commit(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.chat.with_raw_response.add_git_commit(
                session_id="",
                commit_hash="commit_hash",
            )

    @parametrize
    async def test_method_add_message(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.add_message(
            session_id="session_id",
            content="content",
            role="role",
        )
        assert_matches_type(AddChatMessageResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_add_message(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.add_message(
            session_id="session_id",
            content="content",
            role="role",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(AddChatMessageResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_add_message(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.add_message(
            session_id="session_id",
            content="content",
            role="role",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(AddChatMessageResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_message(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.chat.with_raw_response.add_message(
                session_id="",
                content="content",
                role="role",
            )

    @parametrize
    async def test_method_create_session(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.create_session(
            git_repo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            initial_message="initial_message",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.create_session(
            git_repo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            initial_message="initial_message",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.create_session(
            git_repo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            initial_message="initial_message",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_session(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.delete_session(
            "session_id",
        )
        assert_matches_type(DeleteChatSessionResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_delete_session(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.delete_session(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(DeleteChatSessionResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_delete_session(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.delete_session(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(DeleteChatSessionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_session(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.chat.with_raw_response.delete_session(
                "",
            )

    @parametrize
    async def test_method_get_git_commit(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.get_git_commit(
            commit_hash="commit_hash",
            chat_id="chat_id",
        )
        assert_matches_type(ChatGetGitCommitResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_get_git_commit(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.get_git_commit(
            commit_hash="commit_hash",
            chat_id="chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatGetGitCommitResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_get_git_commit(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.get_git_commit(
            commit_hash="commit_hash",
            chat_id="chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatGetGitCommitResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_git_commit(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chat.with_raw_response.get_git_commit(
                commit_hash="commit_hash",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commit_hash` but received ''"):
            await async_client.chat.with_raw_response.get_git_commit(
                commit_hash="",
                chat_id="chat_id",
            )

    @parametrize
    async def test_method_get_session(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.get_session(
            "session_id",
        )
        assert_matches_type(GetChatSessionResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_get_session(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.get_session(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(GetChatSessionResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_get_session(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.get_session(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(GetChatSessionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_session(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.chat.with_raw_response.get_session(
                "",
            )

    @parametrize
    async def test_method_get_session_timeline(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.get_session_timeline(
            "session_id",
        )
        assert_matches_type(ChatGetSessionTimelineResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_get_session_timeline(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.get_session_timeline(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatGetSessionTimelineResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_get_session_timeline(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.get_session_timeline(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatGetSessionTimelineResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_session_timeline(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.chat.with_raw_response.get_session_timeline(
                "",
            )

    @parametrize
    async def test_method_list_sessions(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.list_sessions()
        assert_matches_type(ListChatSessionsResponse, chat, path=["response"])

    @parametrize
    async def test_method_list_sessions_with_all_params(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.list_sessions(
            limit=0,
        )
        assert_matches_type(ListChatSessionsResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_list_sessions(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.list_sessions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ListChatSessionsResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_list_sessions(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.list_sessions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ListChatSessionsResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
