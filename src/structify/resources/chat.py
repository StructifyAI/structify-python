# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    chat_add_message_params,
    chat_list_sessions_params,
    chat_add_git_commit_params,
    chat_create_session_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.add_chat_message_response import AddChatMessageResponse
from ..types.get_chat_session_response import GetChatSessionResponse
from ..types.list_chat_sessions_response import ListChatSessionsResponse
from ..types.chat_add_git_commit_response import ChatAddGitCommitResponse
from ..types.chat_get_git_commit_response import ChatGetGitCommitResponse
from ..types.create_chat_session_response import CreateChatSessionResponse
from ..types.delete_chat_session_response import DeleteChatSessionResponse
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def create_session(
        self,
        *,
        git_application_token: str,
        initial_message: str,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                    "git_application_token": git_application_token,
                    "initial_message": initial_message,
                    "project_id": project_id,
                },
                chat_create_session_params.ChatCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateChatSessionResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def list_sessions(
        self,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def create_session(
        self,
        *,
        git_application_token: str,
        initial_message: str,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                    "git_application_token": git_application_token,
                    "initial_message": initial_message,
                    "project_id": project_id,
                },
                chat_create_session_params.ChatCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateChatSessionResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def list_sessions(
        self,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.add_git_commit = to_raw_response_wrapper(
            chat.add_git_commit,
        )
        self.add_message = to_raw_response_wrapper(
            chat.add_message,
        )
        self.create_session = to_raw_response_wrapper(
            chat.create_session,
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
        self.list_sessions = to_raw_response_wrapper(
            chat.list_sessions,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.add_git_commit = async_to_raw_response_wrapper(
            chat.add_git_commit,
        )
        self.add_message = async_to_raw_response_wrapper(
            chat.add_message,
        )
        self.create_session = async_to_raw_response_wrapper(
            chat.create_session,
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
        self.list_sessions = async_to_raw_response_wrapper(
            chat.list_sessions,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.add_git_commit = to_streamed_response_wrapper(
            chat.add_git_commit,
        )
        self.add_message = to_streamed_response_wrapper(
            chat.add_message,
        )
        self.create_session = to_streamed_response_wrapper(
            chat.create_session,
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
        self.list_sessions = to_streamed_response_wrapper(
            chat.list_sessions,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.add_git_commit = async_to_streamed_response_wrapper(
            chat.add_git_commit,
        )
        self.add_message = async_to_streamed_response_wrapper(
            chat.add_message,
        )
        self.create_session = async_to_streamed_response_wrapper(
            chat.create_session,
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
        self.list_sessions = async_to_streamed_response_wrapper(
            chat.list_sessions,
        )
