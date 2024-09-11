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
from .._base_client import make_request_options
from ..types.user_info import UserInfo
from ..types.token_response import TokenResponse
from ..types.user_usage_response import UserUsageResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def create_test_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenResponse:
        """Creates a test token."""
        return self._post(
            "/user/create_test_token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    def info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserInfo:
        """Enable a source"""
        return self._get(
            "/user/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserInfo,
        )

    def jwt_to_api_token(
        self,
        jwt: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenResponse:
        """JWTs are commonly used for authentication in web applications.

        They contain
        encoded information about the user and are typically short-lived for security
        reasons.

        This endpoint exists to allow clients who have authenticated via JWT (e.g.,
        through Supabase) to obtain a long-lived API token. The API token can then be
        used for subsequent requests to the API without requiring frequent
        re-authentication.

        This conversion process enhances security by separating the authentication
        mechanism (JWT) from the API access mechanism (API token), while providing a
        seamless experience for users transitioning from web-based authentication to API
        usage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not jwt:
            raise ValueError(f"Expected a non-empty value for `jwt` but received {jwt!r}")
        return self._post(
            f"/user/jwt_to_api_token/{jwt}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    def usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUsageResponse:
        """Creates a test token."""
        return self._get(
            "/user/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUsageResponse,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def create_test_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenResponse:
        """Creates a test token."""
        return await self._post(
            "/user/create_test_token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    async def info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserInfo:
        """Enable a source"""
        return await self._get(
            "/user/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserInfo,
        )

    async def jwt_to_api_token(
        self,
        jwt: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenResponse:
        """JWTs are commonly used for authentication in web applications.

        They contain
        encoded information about the user and are typically short-lived for security
        reasons.

        This endpoint exists to allow clients who have authenticated via JWT (e.g.,
        through Supabase) to obtain a long-lived API token. The API token can then be
        used for subsequent requests to the API without requiring frequent
        re-authentication.

        This conversion process enhances security by separating the authentication
        mechanism (JWT) from the API access mechanism (API token), while providing a
        seamless experience for users transitioning from web-based authentication to API
        usage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not jwt:
            raise ValueError(f"Expected a non-empty value for `jwt` but received {jwt!r}")
        return await self._post(
            f"/user/jwt_to_api_token/{jwt}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    async def usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUsageResponse:
        """Creates a test token."""
        return await self._get(
            "/user/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUsageResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create_test_token = to_raw_response_wrapper(
            user.create_test_token,
        )
        self.info = to_raw_response_wrapper(
            user.info,
        )
        self.jwt_to_api_token = to_raw_response_wrapper(
            user.jwt_to_api_token,
        )
        self.usage = to_raw_response_wrapper(
            user.usage,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create_test_token = async_to_raw_response_wrapper(
            user.create_test_token,
        )
        self.info = async_to_raw_response_wrapper(
            user.info,
        )
        self.jwt_to_api_token = async_to_raw_response_wrapper(
            user.jwt_to_api_token,
        )
        self.usage = async_to_raw_response_wrapper(
            user.usage,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create_test_token = to_streamed_response_wrapper(
            user.create_test_token,
        )
        self.info = to_streamed_response_wrapper(
            user.info,
        )
        self.jwt_to_api_token = to_streamed_response_wrapper(
            user.jwt_to_api_token,
        )
        self.usage = to_streamed_response_wrapper(
            user.usage,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create_test_token = async_to_streamed_response_wrapper(
            user.create_test_token,
        )
        self.info = async_to_streamed_response_wrapper(
            user.info,
        )
        self.jwt_to_api_token = async_to_streamed_response_wrapper(
            user.jwt_to_api_token,
        )
        self.usage = async_to_streamed_response_wrapper(
            user.usage,
        )
