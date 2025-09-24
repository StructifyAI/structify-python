# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    ChatSessionRole,
    chat_copy_params,
    chat_load_files_params,
    chat_add_message_params,
    chat_delete_files_params,
    chat_list_sessions_params,
    chat_toggle_public_params,
    chat_add_git_commit_params,
    chat_create_session_params,
    chat_update_session_params,
    chat_add_collaborator_params,
    chat_revert_to_commit_params,
    chat_copy_node_output_by_code_hash_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.chat_session import ChatSession
from ..types.chat_session_role import ChatSessionRole
from ..types.toggle_public_response import TogglePublicResponse
from ..types.chat_load_files_response import ChatLoadFilesResponse
from ..types.add_chat_message_response import AddChatMessageResponse
from ..types.get_chat_session_response import GetChatSessionResponse
from ..types.chat_delete_files_response import ChatDeleteFilesResponse
from ..types.chat_session_with_messages import ChatSessionWithMessages
from ..types.list_chat_sessions_response import ListChatSessionsResponse
from ..types.list_collaborators_response import ListCollaboratorsResponse
from ..types.chat_add_git_commit_response import ChatAddGitCommitResponse
from ..types.chat_get_git_commit_response import ChatGetGitCommitResponse
from ..types.create_chat_session_response import CreateChatSessionResponse
from ..types.delete_chat_session_response import DeleteChatSessionResponse
from ..types.chat_revert_to_commit_response import ChatRevertToCommitResponse
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

    def add_message(
        self,
        session_id: str,
        *,
        content: str,
        role: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddChatMessageResponse:
        """
        Add a message to a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/chat/sessions/{session_id}/messages",
            body=maybe_transform(
                {
                    "content": content,
                    "role": role,
                },
                chat_add_message_params.ChatAddMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddChatMessageResponse,
        )

    def copy(
        self,
        *,
        copy_name: str,
        project_id: str,
        source_chat_id: str,
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
                    "project_id": project_id,
                    "source_chat_id": source_chat_id,
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
        new_node_id: Optional[str] | Omit = omit,
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
        project_id: str,
        ephemeral: Optional[bool] | Omit = omit,
        initial_message: Optional[str] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat/sessions",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "ephemeral": ephemeral,
                    "initial_message": initial_message,
                },
                chat_create_session_params.ChatCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateChatSessionResponse,
        )

    def delete_files(
        self,
        chat_id: str,
        *,
        paths: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatDeleteFilesResponse:
        """
        Delete files from a chat session's git repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            f"/chat/files/delete/{chat_id}",
            body=maybe_transform({"paths": paths}, chat_delete_files_params.ChatDeleteFilesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeleteFilesResponse,
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

    def list_sessions(
        self,
        *,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListChatSessionsResponse:
        """
        List all chat sessions for the authenticated user.

        Args:
          limit: Maximum number of sessions to return (default: 50)

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
                query=maybe_transform({"limit": limit}, chat_list_sessions_params.ChatListSessionsParams),
            ),
            cast_to=ListChatSessionsResponse,
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

    def toggle_public(
        self,
        session_id: str,
        *,
        is_public: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TogglePublicResponse:
        """
        Toggle public visibility of a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._put(
            f"/chat/sessions/{session_id}/public",
            body=maybe_transform({"is_public": is_public}, chat_toggle_public_params.ChatTogglePublicParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TogglePublicResponse,
        )

    def update_session(
        self,
        session_id: str,
        *,
        is_favorite: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
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
                    "is_favorite": is_favorite,
                    "name": name,
                    "project_id": project_id,
                },
                chat_update_session_params.ChatUpdateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSession,
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

    async def add_message(
        self,
        session_id: str,
        *,
        content: str,
        role: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddChatMessageResponse:
        """
        Add a message to a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/chat/sessions/{session_id}/messages",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "role": role,
                },
                chat_add_message_params.ChatAddMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddChatMessageResponse,
        )

    async def copy(
        self,
        *,
        copy_name: str,
        project_id: str,
        source_chat_id: str,
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
                    "project_id": project_id,
                    "source_chat_id": source_chat_id,
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
        new_node_id: Optional[str] | Omit = omit,
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
        project_id: str,
        ephemeral: Optional[bool] | Omit = omit,
        initial_message: Optional[str] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat/sessions",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "ephemeral": ephemeral,
                    "initial_message": initial_message,
                },
                chat_create_session_params.ChatCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateChatSessionResponse,
        )

    async def delete_files(
        self,
        chat_id: str,
        *,
        paths: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatDeleteFilesResponse:
        """
        Delete files from a chat session's git repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            f"/chat/files/delete/{chat_id}",
            body=await async_maybe_transform({"paths": paths}, chat_delete_files_params.ChatDeleteFilesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeleteFilesResponse,
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

    async def list_sessions(
        self,
        *,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListChatSessionsResponse:
        """
        List all chat sessions for the authenticated user.

        Args:
          limit: Maximum number of sessions to return (default: 50)

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
                query=await async_maybe_transform({"limit": limit}, chat_list_sessions_params.ChatListSessionsParams),
            ),
            cast_to=ListChatSessionsResponse,
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

    async def toggle_public(
        self,
        session_id: str,
        *,
        is_public: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TogglePublicResponse:
        """
        Toggle public visibility of a chat session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._put(
            f"/chat/sessions/{session_id}/public",
            body=await async_maybe_transform(
                {"is_public": is_public}, chat_toggle_public_params.ChatTogglePublicParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TogglePublicResponse,
        )

    async def update_session(
        self,
        session_id: str,
        *,
        is_favorite: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
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
                    "is_favorite": is_favorite,
                    "name": name,
                    "project_id": project_id,
                },
                chat_update_session_params.ChatUpdateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSession,
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
        self.add_message = to_raw_response_wrapper(
            chat.add_message,
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
        self.delete_files = to_raw_response_wrapper(
            chat.delete_files,
        )
        self.delete_session = to_raw_response_wrapper(
            chat.delete_session,
        )
        self.get_git_commit = to_raw_response_wrapper(
            chat.get_git_commit,
        )
        self.get_session = to_raw_response_wrapper(
            chat.get_session,
        )
        self.get_session_timeline = to_raw_response_wrapper(
            chat.get_session_timeline,
        )
        self.list_collaborators = to_raw_response_wrapper(
            chat.list_collaborators,
        )
        self.list_sessions = to_raw_response_wrapper(
            chat.list_sessions,
        )
        self.load_files = to_raw_response_wrapper(
            chat.load_files,
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
        self.toggle_public = to_raw_response_wrapper(
            chat.toggle_public,
        )
        self.update_session = to_raw_response_wrapper(
            chat.update_session,
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
        self.add_message = async_to_raw_response_wrapper(
            chat.add_message,
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
        self.delete_files = async_to_raw_response_wrapper(
            chat.delete_files,
        )
        self.delete_session = async_to_raw_response_wrapper(
            chat.delete_session,
        )
        self.get_git_commit = async_to_raw_response_wrapper(
            chat.get_git_commit,
        )
        self.get_session = async_to_raw_response_wrapper(
            chat.get_session,
        )
        self.get_session_timeline = async_to_raw_response_wrapper(
            chat.get_session_timeline,
        )
        self.list_collaborators = async_to_raw_response_wrapper(
            chat.list_collaborators,
        )
        self.list_sessions = async_to_raw_response_wrapper(
            chat.list_sessions,
        )
        self.load_files = async_to_raw_response_wrapper(
            chat.load_files,
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
        self.toggle_public = async_to_raw_response_wrapper(
            chat.toggle_public,
        )
        self.update_session = async_to_raw_response_wrapper(
            chat.update_session,
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
        self.add_message = to_streamed_response_wrapper(
            chat.add_message,
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
        self.delete_files = to_streamed_response_wrapper(
            chat.delete_files,
        )
        self.delete_session = to_streamed_response_wrapper(
            chat.delete_session,
        )
        self.get_git_commit = to_streamed_response_wrapper(
            chat.get_git_commit,
        )
        self.get_session = to_streamed_response_wrapper(
            chat.get_session,
        )
        self.get_session_timeline = to_streamed_response_wrapper(
            chat.get_session_timeline,
        )
        self.list_collaborators = to_streamed_response_wrapper(
            chat.list_collaborators,
        )
        self.list_sessions = to_streamed_response_wrapper(
            chat.list_sessions,
        )
        self.load_files = to_streamed_response_wrapper(
            chat.load_files,
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
        self.toggle_public = to_streamed_response_wrapper(
            chat.toggle_public,
        )
        self.update_session = to_streamed_response_wrapper(
            chat.update_session,
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
        self.add_message = async_to_streamed_response_wrapper(
            chat.add_message,
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
        self.delete_files = async_to_streamed_response_wrapper(
            chat.delete_files,
        )
        self.delete_session = async_to_streamed_response_wrapper(
            chat.delete_session,
        )
        self.get_git_commit = async_to_streamed_response_wrapper(
            chat.get_git_commit,
        )
        self.get_session = async_to_streamed_response_wrapper(
            chat.get_session,
        )
        self.get_session_timeline = async_to_streamed_response_wrapper(
            chat.get_session_timeline,
        )
        self.list_collaborators = async_to_streamed_response_wrapper(
            chat.list_collaborators,
        )
        self.list_sessions = async_to_streamed_response_wrapper(
            chat.list_sessions,
        )
        self.load_files = async_to_streamed_response_wrapper(
            chat.load_files,
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
        self.toggle_public = async_to_streamed_response_wrapper(
            chat.toggle_public,
        )
        self.update_session = async_to_streamed_response_wrapper(
            chat.update_session,
        )
