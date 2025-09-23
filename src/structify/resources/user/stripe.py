# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.user import (
    SubscriptionPlan,
    stripe_create_session_params,
    stripe_create_subscription_params,
    stripe_create_portal_session_params,
)
from ..._base_client import make_request_options
from ...types.user.subscription_plan import SubscriptionPlan
from ...types.user.create_session_response import CreateSessionResponse

__all__ = ["StripeResource", "AsyncStripeResource"]


class StripeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StripeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return StripeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StripeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return StripeResourceWithStreamingResponse(self)

    def create_portal_session(
        self,
        *,
        return_url: str,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateSessionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/transactions/stripe/create_portal_session",
            body=maybe_transform(
                {
                    "return_url": return_url,
                    "team_id": team_id,
                },
                stripe_create_portal_session_params.StripeCreatePortalSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSessionResponse,
        )

    def create_session(
        self,
        *,
        credits: int,
        origin: str,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateSessionResponse:
        """
        Args:
          credits: Amount in cents (i64)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/transactions/stripe/create_session",
            body=maybe_transform(
                {
                    "credits": credits,
                    "origin": origin,
                    "team_id": team_id,
                },
                stripe_create_session_params.StripeCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSessionResponse,
        )

    def create_subscription(
        self,
        *,
        origin: str,
        plan: SubscriptionPlan,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateSessionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/transactions/stripe/create_subscription",
            body=maybe_transform(
                {
                    "origin": origin,
                    "plan": plan,
                    "team_id": team_id,
                },
                stripe_create_subscription_params.StripeCreateSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSessionResponse,
        )


class AsyncStripeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStripeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStripeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStripeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncStripeResourceWithStreamingResponse(self)

    async def create_portal_session(
        self,
        *,
        return_url: str,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateSessionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/transactions/stripe/create_portal_session",
            body=await async_maybe_transform(
                {
                    "return_url": return_url,
                    "team_id": team_id,
                },
                stripe_create_portal_session_params.StripeCreatePortalSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSessionResponse,
        )

    async def create_session(
        self,
        *,
        credits: int,
        origin: str,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateSessionResponse:
        """
        Args:
          credits: Amount in cents (i64)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/transactions/stripe/create_session",
            body=await async_maybe_transform(
                {
                    "credits": credits,
                    "origin": origin,
                    "team_id": team_id,
                },
                stripe_create_session_params.StripeCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSessionResponse,
        )

    async def create_subscription(
        self,
        *,
        origin: str,
        plan: SubscriptionPlan,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateSessionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/transactions/stripe/create_subscription",
            body=await async_maybe_transform(
                {
                    "origin": origin,
                    "plan": plan,
                    "team_id": team_id,
                },
                stripe_create_subscription_params.StripeCreateSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSessionResponse,
        )


class StripeResourceWithRawResponse:
    def __init__(self, stripe: StripeResource) -> None:
        self._stripe = stripe

        self.create_portal_session = to_raw_response_wrapper(
            stripe.create_portal_session,
        )
        self.create_session = to_raw_response_wrapper(
            stripe.create_session,
        )
        self.create_subscription = to_raw_response_wrapper(
            stripe.create_subscription,
        )


class AsyncStripeResourceWithRawResponse:
    def __init__(self, stripe: AsyncStripeResource) -> None:
        self._stripe = stripe

        self.create_portal_session = async_to_raw_response_wrapper(
            stripe.create_portal_session,
        )
        self.create_session = async_to_raw_response_wrapper(
            stripe.create_session,
        )
        self.create_subscription = async_to_raw_response_wrapper(
            stripe.create_subscription,
        )


class StripeResourceWithStreamingResponse:
    def __init__(self, stripe: StripeResource) -> None:
        self._stripe = stripe

        self.create_portal_session = to_streamed_response_wrapper(
            stripe.create_portal_session,
        )
        self.create_session = to_streamed_response_wrapper(
            stripe.create_session,
        )
        self.create_subscription = to_streamed_response_wrapper(
            stripe.create_subscription,
        )


class AsyncStripeResourceWithStreamingResponse:
    def __init__(self, stripe: AsyncStripeResource) -> None:
        self._stripe = stripe

        self.create_portal_session = async_to_streamed_response_wrapper(
            stripe.create_portal_session,
        )
        self.create_session = async_to_streamed_response_wrapper(
            stripe.create_session,
        )
        self.create_subscription = async_to_streamed_response_wrapper(
            stripe.create_subscription,
        )
