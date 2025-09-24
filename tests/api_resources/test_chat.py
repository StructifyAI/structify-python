# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    ChatSession,
    TogglePublicResponse,
    ChatLoadFilesResponse,
    AddChatMessageResponse,
    GetChatSessionResponse,
    ChatDeleteFilesResponse,
    ChatSessionWithMessages,
    ChatAddGitCommitResponse,
    ChatGetGitCommitResponse,
    ListChatSessionsResponse,
    CreateChatSessionResponse,
    DeleteChatSessionResponse,
    ListCollaboratorsResponse,
    ChatRevertToCommitResponse,
    ChatGetSessionTimelineResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_collaborator(self, client: Structify) -> None:
        chat = client.chat.add_collaborator(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            role="owner",
        )
        assert chat is None

    @parametrize
    def test_raw_response_add_collaborator(self, client: Structify) -> None:
        response = client.chat.with_raw_response.add_collaborator(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert chat is None

    @parametrize
    def test_streaming_response_add_collaborator(self, client: Structify) -> None:
        with client.chat.with_streaming_response.add_collaborator(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            role="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_collaborator(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chat.with_raw_response.add_collaborator(
                chat_id="",
                email="email",
                role="owner",
            )

    @parametrize
    def test_method_add_git_commit(self, client: Structify) -> None:
        chat = client.chat.add_git_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        )
        assert_matches_type(ChatAddGitCommitResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_add_git_commit(self, client: Structify) -> None:
        response = client.chat.with_raw_response.add_git_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatAddGitCommitResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_add_git_commit(self, client: Structify) -> None:
        with client.chat.with_streaming_response.add_git_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
    def test_method_copy(self, client: Structify) -> None:
        chat = client.chat.copy(
            copy_name="copy_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatSessionWithMessages, chat, path=["response"])

    @parametrize
    def test_raw_response_copy(self, client: Structify) -> None:
        response = client.chat.with_raw_response.copy(
            copy_name="copy_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatSessionWithMessages, chat, path=["response"])

    @parametrize
    def test_streaming_response_copy(self, client: Structify) -> None:
        with client.chat.with_streaming_response.copy(
            copy_name="copy_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatSessionWithMessages, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_copy_node_output_by_code_hash(self, client: Structify) -> None:
        chat = client.chat.copy_node_output_by_code_hash(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code_md5_hash="code_md5_hash",
        )
        assert_matches_type(str, chat, path=["response"])

    @parametrize
    def test_method_copy_node_output_by_code_hash_with_all_params(self, client: Structify) -> None:
        chat = client.chat.copy_node_output_by_code_hash(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code_md5_hash="code_md5_hash",
            new_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, chat, path=["response"])

    @parametrize
    def test_raw_response_copy_node_output_by_code_hash(self, client: Structify) -> None:
        response = client.chat.with_raw_response.copy_node_output_by_code_hash(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code_md5_hash="code_md5_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(str, chat, path=["response"])

    @parametrize
    def test_streaming_response_copy_node_output_by_code_hash(self, client: Structify) -> None:
        with client.chat.with_streaming_response.copy_node_output_by_code_hash(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code_md5_hash="code_md5_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(str, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_copy_node_output_by_code_hash(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.chat.with_raw_response.copy_node_output_by_code_hash(
                session_id="",
                code_md5_hash="code_md5_hash",
            )

    @parametrize
    def test_method_create_session(self, client: Structify) -> None:
        chat = client.chat.create_session(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

    @parametrize
    def test_method_create_session_with_all_params(self, client: Structify) -> None:
        chat = client.chat.create_session(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ephemeral=True,
            initial_message="initial_message",
        )
        assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create_session(self, client: Structify) -> None:
        response = client.chat.with_raw_response.create_session(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create_session(self, client: Structify) -> None:
        with client.chat.with_streaming_response.create_session(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_files(self, client: Structify) -> None:
        chat = client.chat.delete_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paths=["string"],
        )
        assert_matches_type(ChatDeleteFilesResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_delete_files(self, client: Structify) -> None:
        response = client.chat.with_raw_response.delete_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paths=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatDeleteFilesResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_delete_files(self, client: Structify) -> None:
        with client.chat.with_streaming_response.delete_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paths=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatDeleteFilesResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_files(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chat.with_raw_response.delete_files(
                chat_id="",
                paths=["string"],
            )

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
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatGetSessionTimelineResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_get_session_timeline(self, client: Structify) -> None:
        response = client.chat.with_raw_response.get_session_timeline(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatGetSessionTimelineResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_get_session_timeline(self, client: Structify) -> None:
        with client.chat.with_streaming_response.get_session_timeline(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
    def test_method_list_collaborators(self, client: Structify) -> None:
        chat = client.chat.list_collaborators(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListCollaboratorsResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_list_collaborators(self, client: Structify) -> None:
        response = client.chat.with_raw_response.list_collaborators(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ListCollaboratorsResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_list_collaborators(self, client: Structify) -> None:
        with client.chat.with_streaming_response.list_collaborators(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ListCollaboratorsResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_collaborators(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chat.with_raw_response.list_collaborators(
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

    @parametrize
    def test_method_load_files(self, client: Structify) -> None:
        chat = client.chat.load_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatLoadFilesResponse, chat, path=["response"])

    @parametrize
    def test_method_load_files_with_all_params(self, client: Structify) -> None:
        chat = client.chat.load_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        )
        assert_matches_type(ChatLoadFilesResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_load_files(self, client: Structify) -> None:
        response = client.chat.with_raw_response.load_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatLoadFilesResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_load_files(self, client: Structify) -> None:
        with client.chat.with_streaming_response.load_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatLoadFilesResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_make_permanent(self, client: Structify) -> None:
        chat = client.chat.make_permanent(
            "session_id",
        )
        assert chat is None

    @parametrize
    def test_raw_response_make_permanent(self, client: Structify) -> None:
        response = client.chat.with_raw_response.make_permanent(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert chat is None

    @parametrize
    def test_streaming_response_make_permanent(self, client: Structify) -> None:
        with client.chat.with_streaming_response.make_permanent(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_make_permanent(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.chat.with_raw_response.make_permanent(
                "",
            )

    @parametrize
    def test_method_remove_collaborator(self, client: Structify) -> None:
        chat = client.chat.remove_collaborator(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert chat is None

    @parametrize
    def test_raw_response_remove_collaborator(self, client: Structify) -> None:
        response = client.chat.with_raw_response.remove_collaborator(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert chat is None

    @parametrize
    def test_streaming_response_remove_collaborator(self, client: Structify) -> None:
        with client.chat.with_streaming_response.remove_collaborator(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_collaborator(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chat.with_raw_response.remove_collaborator(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.chat.with_raw_response.remove_collaborator(
                user_id="",
                chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_revert_to_commit(self, client: Structify) -> None:
        chat = client.chat.revert_to_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        )
        assert_matches_type(ChatRevertToCommitResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_revert_to_commit(self, client: Structify) -> None:
        response = client.chat.with_raw_response.revert_to_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatRevertToCommitResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_revert_to_commit(self, client: Structify) -> None:
        with client.chat.with_streaming_response.revert_to_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatRevertToCommitResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revert_to_commit(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.chat.with_raw_response.revert_to_commit(
                session_id="",
                commit_hash="commit_hash",
            )

    @parametrize
    def test_method_toggle_public(self, client: Structify) -> None:
        chat = client.chat.toggle_public(
            session_id="session_id",
            is_public=True,
        )
        assert_matches_type(TogglePublicResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_toggle_public(self, client: Structify) -> None:
        response = client.chat.with_raw_response.toggle_public(
            session_id="session_id",
            is_public=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(TogglePublicResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_toggle_public(self, client: Structify) -> None:
        with client.chat.with_streaming_response.toggle_public(
            session_id="session_id",
            is_public=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(TogglePublicResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_toggle_public(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.chat.with_raw_response.toggle_public(
                session_id="",
                is_public=True,
            )

    @parametrize
    def test_method_update_session(self, client: Structify) -> None:
        chat = client.chat.update_session(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatSession, chat, path=["response"])

    @parametrize
    def test_method_update_session_with_all_params(self, client: Structify) -> None:
        chat = client.chat.update_session(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_favorite=True,
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatSession, chat, path=["response"])

    @parametrize
    def test_raw_response_update_session(self, client: Structify) -> None:
        response = client.chat.with_raw_response.update_session(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatSession, chat, path=["response"])

    @parametrize
    def test_streaming_response_update_session(self, client: Structify) -> None:
        with client.chat.with_streaming_response.update_session(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatSession, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_session(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.chat.with_raw_response.update_session(
                session_id="",
            )


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_add_collaborator(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.add_collaborator(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            role="owner",
        )
        assert chat is None

    @parametrize
    async def test_raw_response_add_collaborator(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.add_collaborator(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert chat is None

    @parametrize
    async def test_streaming_response_add_collaborator(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.add_collaborator(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            role="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_collaborator(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chat.with_raw_response.add_collaborator(
                chat_id="",
                email="email",
                role="owner",
            )

    @parametrize
    async def test_method_add_git_commit(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.add_git_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        )
        assert_matches_type(ChatAddGitCommitResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_add_git_commit(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.add_git_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatAddGitCommitResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_add_git_commit(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.add_git_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
    async def test_method_copy(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.copy(
            copy_name="copy_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatSessionWithMessages, chat, path=["response"])

    @parametrize
    async def test_raw_response_copy(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.copy(
            copy_name="copy_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatSessionWithMessages, chat, path=["response"])

    @parametrize
    async def test_streaming_response_copy(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.copy(
            copy_name="copy_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatSessionWithMessages, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_copy_node_output_by_code_hash(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.copy_node_output_by_code_hash(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code_md5_hash="code_md5_hash",
        )
        assert_matches_type(str, chat, path=["response"])

    @parametrize
    async def test_method_copy_node_output_by_code_hash_with_all_params(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.copy_node_output_by_code_hash(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code_md5_hash="code_md5_hash",
            new_node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, chat, path=["response"])

    @parametrize
    async def test_raw_response_copy_node_output_by_code_hash(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.copy_node_output_by_code_hash(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code_md5_hash="code_md5_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(str, chat, path=["response"])

    @parametrize
    async def test_streaming_response_copy_node_output_by_code_hash(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.copy_node_output_by_code_hash(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            code_md5_hash="code_md5_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(str, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_copy_node_output_by_code_hash(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.chat.with_raw_response.copy_node_output_by_code_hash(
                session_id="",
                code_md5_hash="code_md5_hash",
            )

    @parametrize
    async def test_method_create_session(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.create_session(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

    @parametrize
    async def test_method_create_session_with_all_params(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.create_session(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ephemeral=True,
            initial_message="initial_message",
        )
        assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.create_session(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.create_session(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(CreateChatSessionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_files(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.delete_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paths=["string"],
        )
        assert_matches_type(ChatDeleteFilesResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_delete_files(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.delete_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paths=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatDeleteFilesResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_delete_files(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.delete_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paths=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatDeleteFilesResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_files(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chat.with_raw_response.delete_files(
                chat_id="",
                paths=["string"],
            )

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
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatGetSessionTimelineResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_get_session_timeline(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.get_session_timeline(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatGetSessionTimelineResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_get_session_timeline(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.get_session_timeline(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
    async def test_method_list_collaborators(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.list_collaborators(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListCollaboratorsResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_list_collaborators(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.list_collaborators(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ListCollaboratorsResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_list_collaborators(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.list_collaborators(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ListCollaboratorsResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_collaborators(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chat.with_raw_response.list_collaborators(
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

    @parametrize
    async def test_method_load_files(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.load_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatLoadFilesResponse, chat, path=["response"])

    @parametrize
    async def test_method_load_files_with_all_params(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.load_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        )
        assert_matches_type(ChatLoadFilesResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_load_files(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.load_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatLoadFilesResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_load_files(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.load_files(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatLoadFilesResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_make_permanent(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.make_permanent(
            "session_id",
        )
        assert chat is None

    @parametrize
    async def test_raw_response_make_permanent(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.make_permanent(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert chat is None

    @parametrize
    async def test_streaming_response_make_permanent(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.make_permanent(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_make_permanent(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.chat.with_raw_response.make_permanent(
                "",
            )

    @parametrize
    async def test_method_remove_collaborator(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.remove_collaborator(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert chat is None

    @parametrize
    async def test_raw_response_remove_collaborator(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.remove_collaborator(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert chat is None

    @parametrize
    async def test_streaming_response_remove_collaborator(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.remove_collaborator(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_collaborator(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chat.with_raw_response.remove_collaborator(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.chat.with_raw_response.remove_collaborator(
                user_id="",
                chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_revert_to_commit(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.revert_to_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        )
        assert_matches_type(ChatRevertToCommitResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_revert_to_commit(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.revert_to_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatRevertToCommitResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_revert_to_commit(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.revert_to_commit(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            commit_hash="commit_hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatRevertToCommitResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revert_to_commit(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.chat.with_raw_response.revert_to_commit(
                session_id="",
                commit_hash="commit_hash",
            )

    @parametrize
    async def test_method_toggle_public(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.toggle_public(
            session_id="session_id",
            is_public=True,
        )
        assert_matches_type(TogglePublicResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_toggle_public(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.toggle_public(
            session_id="session_id",
            is_public=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(TogglePublicResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_toggle_public(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.toggle_public(
            session_id="session_id",
            is_public=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(TogglePublicResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_toggle_public(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.chat.with_raw_response.toggle_public(
                session_id="",
                is_public=True,
            )

    @parametrize
    async def test_method_update_session(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.update_session(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatSession, chat, path=["response"])

    @parametrize
    async def test_method_update_session_with_all_params(self, async_client: AsyncStructify) -> None:
        chat = await async_client.chat.update_session(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_favorite=True,
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatSession, chat, path=["response"])

    @parametrize
    async def test_raw_response_update_session(self, async_client: AsyncStructify) -> None:
        response = await async_client.chat.with_raw_response.update_session(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatSession, chat, path=["response"])

    @parametrize
    async def test_streaming_response_update_session(self, async_client: AsyncStructify) -> None:
        async with async_client.chat.with_streaming_response.update_session(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatSession, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_session(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.chat.with_raw_response.update_session(
                session_id="",
            )
