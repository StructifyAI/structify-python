# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Optional, cast
from datetime import datetime

import httpx

from ..types import (
    ChatVisibility,
    ChatSessionRole,
    chat_copy_params,
    chat_load_files_params,
    chat_list_sessions_params,
    chat_add_git_commit_params,
    chat_create_session_params,
    chat_update_session_params,
    chat_simulate_prompt_params,
    chat_add_collaborator_params,
    chat_load_input_files_params,
    chat_revert_to_commit_params,
    chat_admin_issue_found_params,
    chat_delete_input_file_params,
    chat_update_visibility_params,
    chat_upload_input_file_params,
    chat_grant_admin_override_params,
    chat_update_session_favorite_params,
    chat_copy_node_output_by_code_hash_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.chat_session import ChatSession
from ..types.chat_visibility import ChatVisibility
from ..types.chat_prompt_param import ChatPromptParam
from ..types.chat_session_role import ChatSessionRole
from ..types.chat_load_files_response import ChatLoadFilesResponse
from ..types.simulate_prompt_response import SimulatePromptResponse
from ..types.get_chat_session_response import GetChatSessionResponse
from ..types.get_dependencies_response import GetDependenciesResponse
from ..types.admin_issue_found_response import AdminIssueFoundResponse
from ..types.chat_session_with_messages import ChatSessionWithMessages
from ..types.update_visibility_response import UpdateVisibilityResponse
from ..types.admin_grant_access_response import AdminGrantAccessResponse
from ..types.list_chat_sessions_response import ListChatSessionsResponse
from ..types.list_collaborators_response import ListCollaboratorsResponse
from ..types.chat_add_git_commit_response import ChatAddGitCommitResponse
from ..types.chat_get_git_commit_response import ChatGetGitCommitResponse
from ..types.chat_list_templates_response import ChatListTemplatesResponse
from ..types.create_chat_session_response import CreateChatSessionResponse
from ..types.delete_chat_session_response import DeleteChatSessionResponse
from ..types.chat_list_input_files_response import ChatListInputFilesResponse
from ..types.chat_load_input_files_response import ChatLoadInputFilesResponse
from ..types.chat_revert_to_commit_response import ChatRevertToCommitResponse
from ..types.chat_delete_input_file_response import ChatDeleteInputFileResponse
from ..types.chat_get_partial_chats_response import ChatGetPartialChatsResponse
from ..types.chat_upload_input_file_response import ChatUploadInputFileResponse
from ..types.chat_get_session_timeline_response import ChatGetSessionTimelineResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def add_collaborator(
        self,
        chat_id: str,
        *,
        email: str,
        role: ChatSessionRole,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/chat/sessions/{chat_id}/collaborators",
            body=maybe_transform(
                {
                    "email": email,
                    "role": role,
                },
                chat_add_collaborator_params.ChatAddCollaboratorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_git_commit(
        self,
        session_id: str,
        *,
        commit_hash: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAddGitCommitResponse:
        """
        Add a git commit to a chat session

        Args:
          commit_hash: The git commit hash (must be 40 characters)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/chat/sessions/{session_id}/commits",
            body=maybe_transform({"commit_hash": commit_hash}, chat_add_git_commit_params.ChatAddGitCommitParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatAddGitCommitResponse,
        )

    def admin_issue_found(
        self,
        chat_id: str,
        *,
        message: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminIssueFoundResponse:
        """
        Add an IssueFound tool call as an admin-only auto-review message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            f"/chat/sessions/{chat_id}/admin/issue_found",
            body=maybe_transform(
                {
                    "message": message,
                    "title": title,
                },
                chat_admin_issue_found_params.ChatAdminIssueFoundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminIssueFoundResponse,
        )

    def copy(
        self,
        *,
        copy_name: str,
        source_chat_id: str,
        team_id: str,
        copy_inputs: bool | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSessionWithMessages:
        """
        Copy a chat session with its workflows and git files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat/copy",
            body=maybe_transform(
                {
                    "copy_name": copy_name,
                    "source_chat_id": source_chat_id,
                    "team_id": team_id,
                    "copy_inputs": copy_inputs,
                    "project_id": project_id,
                },
                chat_copy_params.ChatCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSessionWithMessages,
        )

    def copy_node_output_by_code_hash(
        self,
        session_id: str,
        *,
        code_md5_hash: str,
        new_node_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/chat/sessions/{session_id}/nodes/by_code_hash",
            body=maybe_transform(
                {
                    "code_md5_hash": code_md5_hash,
                    "new_node_id": new_node_id,
                },
                chat_copy_node_output_by_code_hash_params.ChatCopyNodeOutputByCodeHashParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def create_session(
        self,
        *,
        team_id: str,
        config: Optional[chat_create_session_params.Config] | Omit = omit,
        ephemeral: Optional[bool] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateChatSessionResponse:
        """
        Create a new chat session with an initial message

        Args:
          config: Configuration for chat session with system prompt and LLM key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat/sessions",
            body=maybe_transform(
                {
                    "team_id": team_id,
                    "config": config,
                    "ephemeral": ephemeral,
                    "project_id": project_id,
                },
                chat_create_session_params.ChatCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateChatSessionResponse,
        )

    def delete_input_file(
        self,
        chat_id: str,
        *,
        filenames: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatDeleteInputFileResponse:
        """
        Delete input files from a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            f"/chat/input-files/delete/{chat_id}",
            body=maybe_transform({"filenames": filenames}, chat_delete_input_file_params.ChatDeleteInputFileParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeleteInputFileResponse,
        )

    def delete_session(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteChatSessionResponse:
        """
        Delete a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._delete(
            f"/chat/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteChatSessionResponse,
        )

    def get_dependencies(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetDependenciesResponse:
        """
        Get all dependencies for a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/chat/sessions/{session_id}/dependencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetDependenciesResponse,
        )

    def get_git_commit(
        self,
        commit_hash: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatGetGitCommitResponse:
        """
        Get a specific git commit by its hash for a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not commit_hash:
            raise ValueError(f"Expected a non-empty value for `commit_hash` but received {commit_hash!r}")
        return self._get(
            f"/chat/sessions/{chat_id}/commits/{commit_hash}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatGetGitCommitResponse,
        )

    def get_partial_chats(
        self,
        chat_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatGetPartialChatsResponse:
        """
        Get all partial chats for a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_session_id:
            raise ValueError(f"Expected a non-empty value for `chat_session_id` but received {chat_session_id!r}")
        return self._get(
            f"/chat/{chat_session_id}/partial-chats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatGetPartialChatsResponse,
        )

    def get_session(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetChatSessionResponse:
        """
        Get a chat session with all its messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/chat/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetChatSessionResponse,
        )

    def get_session_timeline(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatGetSessionTimelineResponse:
        """
        Get chronological timeline of messages and commits for a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/chat/sessions/{session_id}/timeline",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatGetSessionTimelineResponse,
        )

    def grant_admin_override(
        self,
        chat_id: str,
        *,
        duration_hours: int,
        role: ChatSessionRole,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGrantAccessResponse:
        """
        Grant temporary admin override access for the calling admin to a chat session

        Args:
          duration_hours: Duration in hours for the temporary access

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            f"/chat/sessions/{chat_id}/admin_override",
            body=maybe_transform(
                {
                    "duration_hours": duration_hours,
                    "role": role,
                },
                chat_grant_admin_override_params.ChatGrantAdminOverrideParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGrantAccessResponse,
        )

    def list_collaborators(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListCollaboratorsResponse:
        """
        List all users who have access to a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            f"/chat/sessions/{chat_id}/collaborators",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListCollaboratorsResponse,
        )

    def list_input_files(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatListInputFilesResponse:
        """
        List input files for a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            f"/chat/input-files/list/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatListInputFilesResponse,
        )

    def list_sessions(
        self,
        *,
        team_id: str,
        limit: Optional[int] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListChatSessionsResponse:
        """
        List all chat sessions for the authenticated user within a specific team and
        project.

        Args:
          team_id: Team ID to filter chat sessions

          limit: Maximum number of sessions to return (default: 50)

          project_id: Project ID to filter chat sessions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/chat/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "team_id": team_id,
                        "limit": limit,
                        "project_id": project_id,
                    },
                    chat_list_sessions_params.ChatListSessionsParams,
                ),
            ),
            cast_to=ListChatSessionsResponse,
        )

    def list_templates(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatListTemplatesResponse:
        """List active chat templates for the /chat page"""
        return self._get(
            "/chat/templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatListTemplatesResponse,
        )

    def load_files(
        self,
        *,
        chat_id: str,
        commit_hash: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatLoadFilesResponse:
        """
        Load files from a chat session's git repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat/files/load",
            body=maybe_transform(
                {
                    "chat_id": chat_id,
                    "commit_hash": commit_hash,
                },
                chat_load_files_params.ChatLoadFilesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatLoadFilesResponse,
        )

    def load_input_file(
        self,
        filename: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download a single input file by chat ID and filename

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/chat/input-files/download/{chat_id}/{filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def load_input_files(
        self,
        chat_id: str,
        *,
        since: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatLoadInputFilesResponse:
        """
        Pass `since` query param (RFC 3339 timestamp) to only get files created/updated
        after that time. The response includes `latest_timestamp` which can be passed as
        `since` on the next call.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            f"/chat/input-files/download-all/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"since": since}, chat_load_input_files_params.ChatLoadInputFilesParams),
            ),
            cast_to=ChatLoadInputFilesResponse,
        )

    def make_permanent(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Make an ephemeral chat session permanent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/chat/sessions/{session_id}/make-permanent",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove_collaborator(
        self,
        user_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/chat/sessions/{chat_id}/collaborators/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def revert_to_commit(
        self,
        session_id: str,
        *,
        commit_hash: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatRevertToCommitResponse:
        """
        Revert a chat session to a specific commit

        Args:
          commit_hash: The git commit hash to revert to (must be 40 characters)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/chat/sessions/{session_id}/revert",
            body=maybe_transform({"commit_hash": commit_hash}, chat_revert_to_commit_params.ChatRevertToCommitParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatRevertToCommitResponse,
        )

    def simulate_prompt(
        self,
        chat_session_id: str,
        *,
        chat_prompt: ChatPromptParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulatePromptResponse:
        """
        any messages to the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_session_id:
            raise ValueError(f"Expected a non-empty value for `chat_session_id` but received {chat_session_id!r}")
        return self._post(
            f"/chat/{chat_session_id}/simulate-prompt",
            body=maybe_transform({"chat_prompt": chat_prompt}, chat_simulate_prompt_params.ChatSimulatePromptParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulatePromptResponse,
        )

    def update_session(
        self,
        session_id: str,
        *,
        message_head: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        skip_confirmations: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSession:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._patch(
            f"/chat/sessions/{session_id}",
            body=maybe_transform(
                {
                    "message_head": message_head,
                    "name": name,
                    "project_id": project_id,
                    "skip_confirmations": skip_confirmations,
                },
                chat_update_session_params.ChatUpdateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSession,
        )

    def update_session_favorite(
        self,
        session_id: str,
        *,
        is_favorite: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSession:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._patch(
            f"/chat/sessions/{session_id}/favorite",
            body=maybe_transform(
                {"is_favorite": is_favorite}, chat_update_session_favorite_params.ChatUpdateSessionFavoriteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSession,
        )

    def update_visibility(
        self,
        session_id: str,
        *,
        visibility: ChatVisibility,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateVisibilityResponse:
        """
        Update visibility of a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._put(
            f"/chat/sessions/{session_id}/visibility",
            body=maybe_transform({"visibility": visibility}, chat_update_visibility_params.ChatUpdateVisibilityParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateVisibilityResponse,
        )

    def upload_input_file(
        self,
        chat_id: str,
        *,
        content: FileTypes,
        content_type: str,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatUploadInputFileResponse:
        """
        Upload an input file to a chat session's bucket storage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        body = deepcopy_minimal(
            {
                "content": content,
                "content_type": content_type,
                "file_name": file_name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["content"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/chat/input-files/upload/{chat_id}",
            body=maybe_transform(body, chat_upload_input_file_params.ChatUploadInputFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatUploadInputFileResponse,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def add_collaborator(
        self,
        chat_id: str,
        *,
        email: str,
        role: ChatSessionRole,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/chat/sessions/{chat_id}/collaborators",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "role": role,
                },
                chat_add_collaborator_params.ChatAddCollaboratorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_git_commit(
        self,
        session_id: str,
        *,
        commit_hash: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAddGitCommitResponse:
        """
        Add a git commit to a chat session

        Args:
          commit_hash: The git commit hash (must be 40 characters)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/chat/sessions/{session_id}/commits",
            body=await async_maybe_transform(
                {"commit_hash": commit_hash}, chat_add_git_commit_params.ChatAddGitCommitParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatAddGitCommitResponse,
        )

    async def admin_issue_found(
        self,
        chat_id: str,
        *,
        message: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminIssueFoundResponse:
        """
        Add an IssueFound tool call as an admin-only auto-review message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            f"/chat/sessions/{chat_id}/admin/issue_found",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "title": title,
                },
                chat_admin_issue_found_params.ChatAdminIssueFoundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminIssueFoundResponse,
        )

    async def copy(
        self,
        *,
        copy_name: str,
        source_chat_id: str,
        team_id: str,
        copy_inputs: bool | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSessionWithMessages:
        """
        Copy a chat session with its workflows and git files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat/copy",
            body=await async_maybe_transform(
                {
                    "copy_name": copy_name,
                    "source_chat_id": source_chat_id,
                    "team_id": team_id,
                    "copy_inputs": copy_inputs,
                    "project_id": project_id,
                },
                chat_copy_params.ChatCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSessionWithMessages,
        )

    async def copy_node_output_by_code_hash(
        self,
        session_id: str,
        *,
        code_md5_hash: str,
        new_node_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/chat/sessions/{session_id}/nodes/by_code_hash",
            body=await async_maybe_transform(
                {
                    "code_md5_hash": code_md5_hash,
                    "new_node_id": new_node_id,
                },
                chat_copy_node_output_by_code_hash_params.ChatCopyNodeOutputByCodeHashParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def create_session(
        self,
        *,
        team_id: str,
        config: Optional[chat_create_session_params.Config] | Omit = omit,
        ephemeral: Optional[bool] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateChatSessionResponse:
        """
        Create a new chat session with an initial message

        Args:
          config: Configuration for chat session with system prompt and LLM key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat/sessions",
            body=await async_maybe_transform(
                {
                    "team_id": team_id,
                    "config": config,
                    "ephemeral": ephemeral,
                    "project_id": project_id,
                },
                chat_create_session_params.ChatCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateChatSessionResponse,
        )

    async def delete_input_file(
        self,
        chat_id: str,
        *,
        filenames: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatDeleteInputFileResponse:
        """
        Delete input files from a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            f"/chat/input-files/delete/{chat_id}",
            body=await async_maybe_transform(
                {"filenames": filenames}, chat_delete_input_file_params.ChatDeleteInputFileParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeleteInputFileResponse,
        )

    async def delete_session(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteChatSessionResponse:
        """
        Delete a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._delete(
            f"/chat/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteChatSessionResponse,
        )

    async def get_dependencies(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetDependenciesResponse:
        """
        Get all dependencies for a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/chat/sessions/{session_id}/dependencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetDependenciesResponse,
        )

    async def get_git_commit(
        self,
        commit_hash: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatGetGitCommitResponse:
        """
        Get a specific git commit by its hash for a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not commit_hash:
            raise ValueError(f"Expected a non-empty value for `commit_hash` but received {commit_hash!r}")
        return await self._get(
            f"/chat/sessions/{chat_id}/commits/{commit_hash}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatGetGitCommitResponse,
        )

    async def get_partial_chats(
        self,
        chat_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatGetPartialChatsResponse:
        """
        Get all partial chats for a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_session_id:
            raise ValueError(f"Expected a non-empty value for `chat_session_id` but received {chat_session_id!r}")
        return await self._get(
            f"/chat/{chat_session_id}/partial-chats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatGetPartialChatsResponse,
        )

    async def get_session(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetChatSessionResponse:
        """
        Get a chat session with all its messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/chat/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetChatSessionResponse,
        )

    async def get_session_timeline(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatGetSessionTimelineResponse:
        """
        Get chronological timeline of messages and commits for a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/chat/sessions/{session_id}/timeline",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatGetSessionTimelineResponse,
        )

    async def grant_admin_override(
        self,
        chat_id: str,
        *,
        duration_hours: int,
        role: ChatSessionRole,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminGrantAccessResponse:
        """
        Grant temporary admin override access for the calling admin to a chat session

        Args:
          duration_hours: Duration in hours for the temporary access

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            f"/chat/sessions/{chat_id}/admin_override",
            body=await async_maybe_transform(
                {
                    "duration_hours": duration_hours,
                    "role": role,
                },
                chat_grant_admin_override_params.ChatGrantAdminOverrideParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminGrantAccessResponse,
        )

    async def list_collaborators(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListCollaboratorsResponse:
        """
        List all users who have access to a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            f"/chat/sessions/{chat_id}/collaborators",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListCollaboratorsResponse,
        )

    async def list_input_files(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatListInputFilesResponse:
        """
        List input files for a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            f"/chat/input-files/list/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatListInputFilesResponse,
        )

    async def list_sessions(
        self,
        *,
        team_id: str,
        limit: Optional[int] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListChatSessionsResponse:
        """
        List all chat sessions for the authenticated user within a specific team and
        project.

        Args:
          team_id: Team ID to filter chat sessions

          limit: Maximum number of sessions to return (default: 50)

          project_id: Project ID to filter chat sessions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/chat/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "team_id": team_id,
                        "limit": limit,
                        "project_id": project_id,
                    },
                    chat_list_sessions_params.ChatListSessionsParams,
                ),
            ),
            cast_to=ListChatSessionsResponse,
        )

    async def list_templates(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatListTemplatesResponse:
        """List active chat templates for the /chat page"""
        return await self._get(
            "/chat/templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatListTemplatesResponse,
        )

    async def load_files(
        self,
        *,
        chat_id: str,
        commit_hash: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatLoadFilesResponse:
        """
        Load files from a chat session's git repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat/files/load",
            body=await async_maybe_transform(
                {
                    "chat_id": chat_id,
                    "commit_hash": commit_hash,
                },
                chat_load_files_params.ChatLoadFilesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatLoadFilesResponse,
        )

    async def load_input_file(
        self,
        filename: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download a single input file by chat ID and filename

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/chat/input-files/download/{chat_id}/{filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def load_input_files(
        self,
        chat_id: str,
        *,
        since: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatLoadInputFilesResponse:
        """
        Pass `since` query param (RFC 3339 timestamp) to only get files created/updated
        after that time. The response includes `latest_timestamp` which can be passed as
        `since` on the next call.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            f"/chat/input-files/download-all/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"since": since}, chat_load_input_files_params.ChatLoadInputFilesParams
                ),
            ),
            cast_to=ChatLoadInputFilesResponse,
        )

    async def make_permanent(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Make an ephemeral chat session permanent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/chat/sessions/{session_id}/make-permanent",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove_collaborator(
        self,
        user_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/chat/sessions/{chat_id}/collaborators/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def revert_to_commit(
        self,
        session_id: str,
        *,
        commit_hash: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatRevertToCommitResponse:
        """
        Revert a chat session to a specific commit

        Args:
          commit_hash: The git commit hash to revert to (must be 40 characters)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/chat/sessions/{session_id}/revert",
            body=await async_maybe_transform(
                {"commit_hash": commit_hash}, chat_revert_to_commit_params.ChatRevertToCommitParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatRevertToCommitResponse,
        )

    async def simulate_prompt(
        self,
        chat_session_id: str,
        *,
        chat_prompt: ChatPromptParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulatePromptResponse:
        """
        any messages to the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_session_id:
            raise ValueError(f"Expected a non-empty value for `chat_session_id` but received {chat_session_id!r}")
        return await self._post(
            f"/chat/{chat_session_id}/simulate-prompt",
            body=await async_maybe_transform(
                {"chat_prompt": chat_prompt}, chat_simulate_prompt_params.ChatSimulatePromptParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulatePromptResponse,
        )

    async def update_session(
        self,
        session_id: str,
        *,
        message_head: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        skip_confirmations: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSession:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._patch(
            f"/chat/sessions/{session_id}",
            body=await async_maybe_transform(
                {
                    "message_head": message_head,
                    "name": name,
                    "project_id": project_id,
                    "skip_confirmations": skip_confirmations,
                },
                chat_update_session_params.ChatUpdateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSession,
        )

    async def update_session_favorite(
        self,
        session_id: str,
        *,
        is_favorite: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSession:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._patch(
            f"/chat/sessions/{session_id}/favorite",
            body=await async_maybe_transform(
                {"is_favorite": is_favorite}, chat_update_session_favorite_params.ChatUpdateSessionFavoriteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSession,
        )

    async def update_visibility(
        self,
        session_id: str,
        *,
        visibility: ChatVisibility,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateVisibilityResponse:
        """
        Update visibility of a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._put(
            f"/chat/sessions/{session_id}/visibility",
            body=await async_maybe_transform(
                {"visibility": visibility}, chat_update_visibility_params.ChatUpdateVisibilityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateVisibilityResponse,
        )

    async def upload_input_file(
        self,
        chat_id: str,
        *,
        content: FileTypes,
        content_type: str,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatUploadInputFileResponse:
        """
        Upload an input file to a chat session's bucket storage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        body = deepcopy_minimal(
            {
                "content": content,
                "content_type": content_type,
                "file_name": file_name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["content"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/chat/input-files/upload/{chat_id}",
            body=await async_maybe_transform(body, chat_upload_input_file_params.ChatUploadInputFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatUploadInputFileResponse,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.add_collaborator = to_raw_response_wrapper(
            chat.add_collaborator,
        )
        self.add_git_commit = to_raw_response_wrapper(
            chat.add_git_commit,
        )
        self.admin_issue_found = to_raw_response_wrapper(
            chat.admin_issue_found,
        )
        self.copy = to_raw_response_wrapper(
            chat.copy,
        )
        self.copy_node_output_by_code_hash = to_raw_response_wrapper(
            chat.copy_node_output_by_code_hash,
        )
        self.create_session = to_raw_response_wrapper(
            chat.create_session,
        )
        self.delete_input_file = to_raw_response_wrapper(
            chat.delete_input_file,
        )
        self.delete_session = to_raw_response_wrapper(
            chat.delete_session,
        )
        self.get_dependencies = to_raw_response_wrapper(
            chat.get_dependencies,
        )
        self.get_git_commit = to_raw_response_wrapper(
            chat.get_git_commit,
        )
        self.get_partial_chats = to_raw_response_wrapper(
            chat.get_partial_chats,
        )
        self.get_session = to_raw_response_wrapper(
            chat.get_session,
        )
        self.get_session_timeline = to_raw_response_wrapper(
            chat.get_session_timeline,
        )
        self.grant_admin_override = to_raw_response_wrapper(
            chat.grant_admin_override,
        )
        self.list_collaborators = to_raw_response_wrapper(
            chat.list_collaborators,
        )
        self.list_input_files = to_raw_response_wrapper(
            chat.list_input_files,
        )
        self.list_sessions = to_raw_response_wrapper(
            chat.list_sessions,
        )
        self.list_templates = to_raw_response_wrapper(
            chat.list_templates,
        )
        self.load_files = to_raw_response_wrapper(
            chat.load_files,
        )
        self.load_input_file = to_custom_raw_response_wrapper(
            chat.load_input_file,
            BinaryAPIResponse,
        )
        self.load_input_files = to_raw_response_wrapper(
            chat.load_input_files,
        )
        self.make_permanent = to_raw_response_wrapper(
            chat.make_permanent,
        )
        self.remove_collaborator = to_raw_response_wrapper(
            chat.remove_collaborator,
        )
        self.revert_to_commit = to_raw_response_wrapper(
            chat.revert_to_commit,
        )
        self.simulate_prompt = to_raw_response_wrapper(
            chat.simulate_prompt,
        )
        self.update_session = to_raw_response_wrapper(
            chat.update_session,
        )
        self.update_session_favorite = to_raw_response_wrapper(
            chat.update_session_favorite,
        )
        self.update_visibility = to_raw_response_wrapper(
            chat.update_visibility,
        )
        self.upload_input_file = to_raw_response_wrapper(
            chat.upload_input_file,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.add_collaborator = async_to_raw_response_wrapper(
            chat.add_collaborator,
        )
        self.add_git_commit = async_to_raw_response_wrapper(
            chat.add_git_commit,
        )
        self.admin_issue_found = async_to_raw_response_wrapper(
            chat.admin_issue_found,
        )
        self.copy = async_to_raw_response_wrapper(
            chat.copy,
        )
        self.copy_node_output_by_code_hash = async_to_raw_response_wrapper(
            chat.copy_node_output_by_code_hash,
        )
        self.create_session = async_to_raw_response_wrapper(
            chat.create_session,
        )
        self.delete_input_file = async_to_raw_response_wrapper(
            chat.delete_input_file,
        )
        self.delete_session = async_to_raw_response_wrapper(
            chat.delete_session,
        )
        self.get_dependencies = async_to_raw_response_wrapper(
            chat.get_dependencies,
        )
        self.get_git_commit = async_to_raw_response_wrapper(
            chat.get_git_commit,
        )
        self.get_partial_chats = async_to_raw_response_wrapper(
            chat.get_partial_chats,
        )
        self.get_session = async_to_raw_response_wrapper(
            chat.get_session,
        )
        self.get_session_timeline = async_to_raw_response_wrapper(
            chat.get_session_timeline,
        )
        self.grant_admin_override = async_to_raw_response_wrapper(
            chat.grant_admin_override,
        )
        self.list_collaborators = async_to_raw_response_wrapper(
            chat.list_collaborators,
        )
        self.list_input_files = async_to_raw_response_wrapper(
            chat.list_input_files,
        )
        self.list_sessions = async_to_raw_response_wrapper(
            chat.list_sessions,
        )
        self.list_templates = async_to_raw_response_wrapper(
            chat.list_templates,
        )
        self.load_files = async_to_raw_response_wrapper(
            chat.load_files,
        )
        self.load_input_file = async_to_custom_raw_response_wrapper(
            chat.load_input_file,
            AsyncBinaryAPIResponse,
        )
        self.load_input_files = async_to_raw_response_wrapper(
            chat.load_input_files,
        )
        self.make_permanent = async_to_raw_response_wrapper(
            chat.make_permanent,
        )
        self.remove_collaborator = async_to_raw_response_wrapper(
            chat.remove_collaborator,
        )
        self.revert_to_commit = async_to_raw_response_wrapper(
            chat.revert_to_commit,
        )
        self.simulate_prompt = async_to_raw_response_wrapper(
            chat.simulate_prompt,
        )
        self.update_session = async_to_raw_response_wrapper(
            chat.update_session,
        )
        self.update_session_favorite = async_to_raw_response_wrapper(
            chat.update_session_favorite,
        )
        self.update_visibility = async_to_raw_response_wrapper(
            chat.update_visibility,
        )
        self.upload_input_file = async_to_raw_response_wrapper(
            chat.upload_input_file,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.add_collaborator = to_streamed_response_wrapper(
            chat.add_collaborator,
        )
        self.add_git_commit = to_streamed_response_wrapper(
            chat.add_git_commit,
        )
        self.admin_issue_found = to_streamed_response_wrapper(
            chat.admin_issue_found,
        )
        self.copy = to_streamed_response_wrapper(
            chat.copy,
        )
        self.copy_node_output_by_code_hash = to_streamed_response_wrapper(
            chat.copy_node_output_by_code_hash,
        )
        self.create_session = to_streamed_response_wrapper(
            chat.create_session,
        )
        self.delete_input_file = to_streamed_response_wrapper(
            chat.delete_input_file,
        )
        self.delete_session = to_streamed_response_wrapper(
            chat.delete_session,
        )
        self.get_dependencies = to_streamed_response_wrapper(
            chat.get_dependencies,
        )
        self.get_git_commit = to_streamed_response_wrapper(
            chat.get_git_commit,
        )
        self.get_partial_chats = to_streamed_response_wrapper(
            chat.get_partial_chats,
        )
        self.get_session = to_streamed_response_wrapper(
            chat.get_session,
        )
        self.get_session_timeline = to_streamed_response_wrapper(
            chat.get_session_timeline,
        )
        self.grant_admin_override = to_streamed_response_wrapper(
            chat.grant_admin_override,
        )
        self.list_collaborators = to_streamed_response_wrapper(
            chat.list_collaborators,
        )
        self.list_input_files = to_streamed_response_wrapper(
            chat.list_input_files,
        )
        self.list_sessions = to_streamed_response_wrapper(
            chat.list_sessions,
        )
        self.list_templates = to_streamed_response_wrapper(
            chat.list_templates,
        )
        self.load_files = to_streamed_response_wrapper(
            chat.load_files,
        )
        self.load_input_file = to_custom_streamed_response_wrapper(
            chat.load_input_file,
            StreamedBinaryAPIResponse,
        )
        self.load_input_files = to_streamed_response_wrapper(
            chat.load_input_files,
        )
        self.make_permanent = to_streamed_response_wrapper(
            chat.make_permanent,
        )
        self.remove_collaborator = to_streamed_response_wrapper(
            chat.remove_collaborator,
        )
        self.revert_to_commit = to_streamed_response_wrapper(
            chat.revert_to_commit,
        )
        self.simulate_prompt = to_streamed_response_wrapper(
            chat.simulate_prompt,
        )
        self.update_session = to_streamed_response_wrapper(
            chat.update_session,
        )
        self.update_session_favorite = to_streamed_response_wrapper(
            chat.update_session_favorite,
        )
        self.update_visibility = to_streamed_response_wrapper(
            chat.update_visibility,
        )
        self.upload_input_file = to_streamed_response_wrapper(
            chat.upload_input_file,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.add_collaborator = async_to_streamed_response_wrapper(
            chat.add_collaborator,
        )
        self.add_git_commit = async_to_streamed_response_wrapper(
            chat.add_git_commit,
        )
        self.admin_issue_found = async_to_streamed_response_wrapper(
            chat.admin_issue_found,
        )
        self.copy = async_to_streamed_response_wrapper(
            chat.copy,
        )
        self.copy_node_output_by_code_hash = async_to_streamed_response_wrapper(
            chat.copy_node_output_by_code_hash,
        )
        self.create_session = async_to_streamed_response_wrapper(
            chat.create_session,
        )
        self.delete_input_file = async_to_streamed_response_wrapper(
            chat.delete_input_file,
        )
        self.delete_session = async_to_streamed_response_wrapper(
            chat.delete_session,
        )
        self.get_dependencies = async_to_streamed_response_wrapper(
            chat.get_dependencies,
        )
        self.get_git_commit = async_to_streamed_response_wrapper(
            chat.get_git_commit,
        )
        self.get_partial_chats = async_to_streamed_response_wrapper(
            chat.get_partial_chats,
        )
        self.get_session = async_to_streamed_response_wrapper(
            chat.get_session,
        )
        self.get_session_timeline = async_to_streamed_response_wrapper(
            chat.get_session_timeline,
        )
        self.grant_admin_override = async_to_streamed_response_wrapper(
            chat.grant_admin_override,
        )
        self.list_collaborators = async_to_streamed_response_wrapper(
            chat.list_collaborators,
        )
        self.list_input_files = async_to_streamed_response_wrapper(
            chat.list_input_files,
        )
        self.list_sessions = async_to_streamed_response_wrapper(
            chat.list_sessions,
        )
        self.list_templates = async_to_streamed_response_wrapper(
            chat.list_templates,
        )
        self.load_files = async_to_streamed_response_wrapper(
            chat.load_files,
        )
        self.load_input_file = async_to_custom_streamed_response_wrapper(
            chat.load_input_file,
            AsyncStreamedBinaryAPIResponse,
        )
        self.load_input_files = async_to_streamed_response_wrapper(
            chat.load_input_files,
        )
        self.make_permanent = async_to_streamed_response_wrapper(
            chat.make_permanent,
        )
        self.remove_collaborator = async_to_streamed_response_wrapper(
            chat.remove_collaborator,
        )
        self.revert_to_commit = async_to_streamed_response_wrapper(
            chat.revert_to_commit,
        )
        self.simulate_prompt = async_to_streamed_response_wrapper(
            chat.simulate_prompt,
        )
        self.update_session = async_to_streamed_response_wrapper(
            chat.update_session,
        )
        self.update_session_favorite = async_to_streamed_response_wrapper(
            chat.update_session_favorite,
        )
        self.update_visibility = async_to_streamed_response_wrapper(
            chat.update_visibility,
        )
        self.upload_input_file = async_to_streamed_response_wrapper(
            chat.upload_input_file,
        )
