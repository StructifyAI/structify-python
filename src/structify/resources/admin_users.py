# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.admin_user_list_response import AdminUserListResponse

__all__ = ["AdminUsersResource", "AsyncAdminUsersResource"]


class AdminUsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdminUsersResourceWithRawResponse:
        return AdminUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminUsersResourceWithStreamingResponse:
        return AdminUsersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminUserListResponse:
        """Lists all the users in the system."""
        return self._get(
            "/admin/users/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminUserListResponse,
        )


class AsyncAdminUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdminUsersResourceWithRawResponse:
        return AsyncAdminUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminUsersResourceWithStreamingResponse:
        return AsyncAdminUsersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminUserListResponse:
        """Lists all the users in the system."""
        return await self._get(
            "/admin/users/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminUserListResponse,
        )


class AdminUsersResourceWithRawResponse:
    def __init__(self, admin_users: AdminUsersResource) -> None:
        self._admin_users = admin_users

        self.list = to_raw_response_wrapper(
            admin_users.list,
        )


class AsyncAdminUsersResourceWithRawResponse:
    def __init__(self, admin_users: AsyncAdminUsersResource) -> None:
        self._admin_users = admin_users

        self.list = async_to_raw_response_wrapper(
            admin_users.list,
        )


class AdminUsersResourceWithStreamingResponse:
    def __init__(self, admin_users: AdminUsersResource) -> None:
        self._admin_users = admin_users

        self.list = to_streamed_response_wrapper(
            admin_users.list,
        )


class AsyncAdminUsersResourceWithStreamingResponse:
    def __init__(self, admin_users: AsyncAdminUsersResource) -> None:
        self._admin_users = admin_users

        self.list = async_to_streamed_response_wrapper(
            admin_users.list,
        )
