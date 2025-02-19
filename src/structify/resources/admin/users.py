# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import (
    user_create_params,
    user_update_params,
    user_get_stats_params,
    user_get_credits_params,
    user_set_credits_params,
)
from ..._base_client import make_request_options
from ...types.admin.user import User
from ...types.token_response import TokenResponse
from ...types.admin.user_list_response import UserListResponse
from ...types.admin.user_get_stats_response import UserGetStatsResponse
from ...types.admin.user_get_credits_response import UserGetCreditsResponse
from ...types.admin.user_set_credits_response import UserSetCreditsResponse

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
        credit_count: Optional[int] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        feature_flags: List[
            Literal["functional_test", "pdf_parsing", "boredm_construction_hack", "boredm_construction_model", "none"]
        ]
        | NotGiven = NOT_GIVEN,
        is_admin: bool | NotGiven = NOT_GIVEN,
        permissions: List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]] | NotGiven = NOT_GIVEN,
        test: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenResponse:
        """
        Create a user, returing their API token.

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

    def update(
        self,
        *,
        current_email: str,
        new_email: Optional[str] | NotGiven = NOT_GIVEN,
        new_feature_flags: Optional[
            List[
                Literal[
                    "functional_test", "pdf_parsing", "boredm_construction_hack", "boredm_construction_model", "none"
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        new_permissions: Optional[List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Update a user's permissions and type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/admin/users/update",
            body=maybe_transform(
                {
                    "current_email": current_email,
                    "new_email": new_email,
                    "new_feature_flags": new_feature_flags,
                    "new_permissions": new_permissions,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """Lists all the users in the system along with their associated API tokens."""
        return self._get(
            "/admin/users/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListResponse,
        )

    def get_credits(
        self,
        *,
        user_email: Optional[str] | NotGiven = NOT_GIVEN,
        user_token: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserGetCreditsResponse:
        """
        get the credit balance of a user by email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/users/get_credits",
            body=maybe_transform(
                {
                    "user_email": user_email,
                    "user_token": user_token,
                },
                user_get_credits_params.UserGetCreditsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetCreditsResponse,
        )

    def get_stats(
        self,
        *,
        bucket: Literal["Second", "Minute", "Hour", "Day", "Week", "Month", "Quarter", "Year", "Decade"]
        | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        user_email: Optional[str] | NotGiven = NOT_GIVEN,
        user_token: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def set_credits(
        self,
        *,
        credit_count: int,
        user_email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSetCreditsResponse:
        """
        set the credit balance of a user, returing that new credit balance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/users/set_credits",
            body=maybe_transform(
                {
                    "credit_count": credit_count,
                    "user_email": user_email,
                },
                user_set_credits_params.UserSetCreditsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSetCreditsResponse,
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
        credit_count: Optional[int] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        feature_flags: List[
            Literal["functional_test", "pdf_parsing", "boredm_construction_hack", "boredm_construction_model", "none"]
        ]
        | NotGiven = NOT_GIVEN,
        is_admin: bool | NotGiven = NOT_GIVEN,
        permissions: List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]] | NotGiven = NOT_GIVEN,
        test: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenResponse:
        """
        Create a user, returing their API token.

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

    async def update(
        self,
        *,
        current_email: str,
        new_email: Optional[str] | NotGiven = NOT_GIVEN,
        new_feature_flags: Optional[
            List[
                Literal[
                    "functional_test", "pdf_parsing", "boredm_construction_hack", "boredm_construction_model", "none"
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        new_permissions: Optional[List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Update a user's permissions and type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/admin/users/update",
            body=await async_maybe_transform(
                {
                    "current_email": current_email,
                    "new_email": new_email,
                    "new_feature_flags": new_feature_flags,
                    "new_permissions": new_permissions,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """Lists all the users in the system along with their associated API tokens."""
        return await self._get(
            "/admin/users/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListResponse,
        )

    async def get_credits(
        self,
        *,
        user_email: Optional[str] | NotGiven = NOT_GIVEN,
        user_token: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserGetCreditsResponse:
        """
        get the credit balance of a user by email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/users/get_credits",
            body=await async_maybe_transform(
                {
                    "user_email": user_email,
                    "user_token": user_token,
                },
                user_get_credits_params.UserGetCreditsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetCreditsResponse,
        )

    async def get_stats(
        self,
        *,
        bucket: Literal["Second", "Minute", "Hour", "Day", "Week", "Month", "Quarter", "Year", "Decade"]
        | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        user_email: Optional[str] | NotGiven = NOT_GIVEN,
        user_token: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def set_credits(
        self,
        *,
        credit_count: int,
        user_email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSetCreditsResponse:
        """
        set the credit balance of a user, returing that new credit balance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/users/set_credits",
            body=await async_maybe_transform(
                {
                    "credit_count": credit_count,
                    "user_email": user_email,
                },
                user_set_credits_params.UserSetCreditsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSetCreditsResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.get_credits = to_raw_response_wrapper(
            users.get_credits,
        )
        self.get_stats = to_raw_response_wrapper(
            users.get_stats,
        )
        self.set_credits = to_raw_response_wrapper(
            users.set_credits,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.get_credits = async_to_raw_response_wrapper(
            users.get_credits,
        )
        self.get_stats = async_to_raw_response_wrapper(
            users.get_stats,
        )
        self.set_credits = async_to_raw_response_wrapper(
            users.set_credits,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.get_credits = to_streamed_response_wrapper(
            users.get_credits,
        )
        self.get_stats = to_streamed_response_wrapper(
            users.get_stats,
        )
        self.set_credits = to_streamed_response_wrapper(
            users.set_credits,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.get_credits = async_to_streamed_response_wrapper(
            users.get_credits,
        )
        self.get_stats = async_to_streamed_response_wrapper(
            users.get_stats,
        )
        self.set_credits = async_to_streamed_response_wrapper(
            users.set_credits,
        )
