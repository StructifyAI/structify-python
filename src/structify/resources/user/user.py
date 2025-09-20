# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .stripe import (
    StripeResource,
    AsyncStripeResource,
    StripeResourceWithRawResponse,
    AsyncStripeResourceWithRawResponse,
    StripeResourceWithStreamingResponse,
    AsyncStripeResourceWithStreamingResponse,
)
from ...types import user_usage_params, user_update_params, user_survey_submit_params
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
from ..._base_client import make_request_options
from ...types.user_info import UserInfo
from ...types.admin.user import User
from ...types.user_usage_response import UserUsageResponse
from ...types.survey_submission_response import SurveySubmissionResponse
from ...types.user_transactions_response import UserTransactionsResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def stripe(self) -> StripeResource:
        return StripeResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    def update(
        self,
        *,
        updates: user_update_params.Updates,
        current_email: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            "/user/update",
            body=maybe_transform(
                {
                    "updates": updates,
                    "current_email": current_email,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserInfo:
        """Enable a source"""
        return self._get(
            "/user/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserInfo,
        )

    def survey_submit(
        self,
        *,
        survey_response: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SurveySubmissionResponse:
        """
        Submit user onboarding survey

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/survey/submit",
            body=maybe_transform(
                {"survey_response": survey_response}, user_survey_submit_params.UserSurveySubmitParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SurveySubmissionResponse,
        )

    def transactions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserTransactionsResponse:
        return self._get(
            "/user/transactions/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserTransactionsResponse,
        )

    def usage(
        self,
        *,
        dataset: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUsageResponse:
        """
        Returns usage statistics for the user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset": dataset}, user_usage_params.UserUsageParams),
            ),
            cast_to=UserUsageResponse,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def stripe(self) -> AsyncStripeResource:
        return AsyncStripeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    async def update(
        self,
        *,
        updates: user_update_params.Updates,
        current_email: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            "/user/update",
            body=await async_maybe_transform(
                {
                    "updates": updates,
                    "current_email": current_email,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserInfo:
        """Enable a source"""
        return await self._get(
            "/user/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserInfo,
        )

    async def survey_submit(
        self,
        *,
        survey_response: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SurveySubmissionResponse:
        """
        Submit user onboarding survey

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/survey/submit",
            body=await async_maybe_transform(
                {"survey_response": survey_response}, user_survey_submit_params.UserSurveySubmitParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SurveySubmissionResponse,
        )

    async def transactions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserTransactionsResponse:
        return await self._get(
            "/user/transactions/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserTransactionsResponse,
        )

    async def usage(
        self,
        *,
        dataset: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUsageResponse:
        """
        Returns usage statistics for the user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dataset": dataset}, user_usage_params.UserUsageParams),
            ),
            cast_to=UserUsageResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.update = to_raw_response_wrapper(
            user.update,
        )
        self.info = to_raw_response_wrapper(
            user.info,
        )
        self.survey_submit = to_raw_response_wrapper(
            user.survey_submit,
        )
        self.transactions = to_raw_response_wrapper(
            user.transactions,
        )
        self.usage = to_raw_response_wrapper(
            user.usage,
        )

    @cached_property
    def stripe(self) -> StripeResourceWithRawResponse:
        return StripeResourceWithRawResponse(self._user.stripe)


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.update = async_to_raw_response_wrapper(
            user.update,
        )
        self.info = async_to_raw_response_wrapper(
            user.info,
        )
        self.survey_submit = async_to_raw_response_wrapper(
            user.survey_submit,
        )
        self.transactions = async_to_raw_response_wrapper(
            user.transactions,
        )
        self.usage = async_to_raw_response_wrapper(
            user.usage,
        )

    @cached_property
    def stripe(self) -> AsyncStripeResourceWithRawResponse:
        return AsyncStripeResourceWithRawResponse(self._user.stripe)


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.update = to_streamed_response_wrapper(
            user.update,
        )
        self.info = to_streamed_response_wrapper(
            user.info,
        )
        self.survey_submit = to_streamed_response_wrapper(
            user.survey_submit,
        )
        self.transactions = to_streamed_response_wrapper(
            user.transactions,
        )
        self.usage = to_streamed_response_wrapper(
            user.usage,
        )

    @cached_property
    def stripe(self) -> StripeResourceWithStreamingResponse:
        return StripeResourceWithStreamingResponse(self._user.stripe)


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.update = async_to_streamed_response_wrapper(
            user.update,
        )
        self.info = async_to_streamed_response_wrapper(
            user.info,
        )
        self.survey_submit = async_to_streamed_response_wrapper(
            user.survey_submit,
        )
        self.transactions = async_to_streamed_response_wrapper(
            user.transactions,
        )
        self.usage = async_to_streamed_response_wrapper(
            user.usage,
        )

    @cached_property
    def stripe(self) -> AsyncStripeResourceWithStreamingResponse:
        return AsyncStripeResourceWithStreamingResponse(self._user.stripe)
