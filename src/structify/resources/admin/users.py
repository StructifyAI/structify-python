# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import user_create_params, user_get_stats_params, user_impersonate_params
from ..._base_client import make_request_options
from ...types.token_response import TokenResponse
from ...types.admin.user_list_response import UserListResponse
from ...types.admin.impersonate_response import ImpersonateResponse
from ...types.admin.user_get_stats_response import UserGetStatsResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        credit_count: Optional[int] | Omit = omit,
        email: Optional[str] | Omit = omit,
        feature_flags: List[
            Literal[
                "functional_test",
                "pdf_parsing",
                "boredm_construction_model",
                "generic_suspicious_queue",
                "new_use_case_preview",
                "bedrock_codegen",
                "cerebras_codegen",
                "gemini25pro",
                "claude_sonnet4",
                "none",
            ]
        ]
        | Omit = omit,
        full_name: Optional[str] | Omit = omit,
        is_admin: bool | Omit = omit,
        permissions: List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]] | Omit = omit,
        test: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Create a user, returning their session token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/users/create",
            body=maybe_transform(
                {
                    "credit_count": credit_count,
                    "email": email,
                    "feature_flags": feature_flags,
                    "full_name": full_name,
                    "is_admin": is_admin,
                    "permissions": permissions,
                    "test": test,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """Lists all users with their team memberships."""
        return self._get(
            "/admin/users/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListResponse,
        )

    def get_stats(
        self,
        *,
        bucket: Literal["Second", "Minute", "Hour", "Day", "Week", "Month", "Quarter", "Year", "Decade"] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        user_email: Optional[str] | Omit = omit,
        user_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetStatsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/users/get_stats",
            body=maybe_transform(
                {
                    "bucket": bucket,
                    "end_date": end_date,
                    "start_date": start_date,
                    "user_email": user_email,
                    "user_token": user_token,
                },
                user_get_stats_params.UserGetStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetStatsResponse,
        )

    def impersonate(
        self,
        *,
        membership_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImpersonateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/users/impersonate",
            body=maybe_transform({"membership_id": membership_id}, user_impersonate_params.UserImpersonateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImpersonateResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        credit_count: Optional[int] | Omit = omit,
        email: Optional[str] | Omit = omit,
        feature_flags: List[
            Literal[
                "functional_test",
                "pdf_parsing",
                "boredm_construction_model",
                "generic_suspicious_queue",
                "new_use_case_preview",
                "bedrock_codegen",
                "cerebras_codegen",
                "gemini25pro",
                "claude_sonnet4",
                "none",
            ]
        ]
        | Omit = omit,
        full_name: Optional[str] | Omit = omit,
        is_admin: bool | Omit = omit,
        permissions: List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]] | Omit = omit,
        test: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Create a user, returning their session token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/users/create",
            body=await async_maybe_transform(
                {
                    "credit_count": credit_count,
                    "email": email,
                    "feature_flags": feature_flags,
                    "full_name": full_name,
                    "is_admin": is_admin,
                    "permissions": permissions,
                    "test": test,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """Lists all users with their team memberships."""
        return await self._get(
            "/admin/users/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListResponse,
        )

    async def get_stats(
        self,
        *,
        bucket: Literal["Second", "Minute", "Hour", "Day", "Week", "Month", "Quarter", "Year", "Decade"] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        user_email: Optional[str] | Omit = omit,
        user_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetStatsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/users/get_stats",
            body=await async_maybe_transform(
                {
                    "bucket": bucket,
                    "end_date": end_date,
                    "start_date": start_date,
                    "user_email": user_email,
                    "user_token": user_token,
                },
                user_get_stats_params.UserGetStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetStatsResponse,
        )

    async def impersonate(
        self,
        *,
        membership_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImpersonateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/users/impersonate",
            body=await async_maybe_transform(
                {"membership_id": membership_id}, user_impersonate_params.UserImpersonateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImpersonateResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.get_stats = to_raw_response_wrapper(
            users.get_stats,
        )
        self.impersonate = to_raw_response_wrapper(
            users.impersonate,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.get_stats = async_to_raw_response_wrapper(
            users.get_stats,
        )
        self.impersonate = async_to_raw_response_wrapper(
            users.impersonate,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.get_stats = to_streamed_response_wrapper(
            users.get_stats,
        )
        self.impersonate = to_streamed_response_wrapper(
            users.impersonate,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.get_stats = async_to_streamed_response_wrapper(
            users.get_stats,
        )
        self.impersonate = async_to_streamed_response_wrapper(
            users.impersonate,
        )
