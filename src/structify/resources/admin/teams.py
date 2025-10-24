# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
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
from ...pagination import SyncJobsList, AsyncJobsList
from ...types.admin import (
    team_list_params,
    team_extend_trial_params,
    team_grant_credits_params,
    team_cancel_subscription_params,
    team_create_subscription_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.admin.extend_trial_response import ExtendTrialResponse
from ...types.admin.grant_credits_response import GrantCreditsResponse
from ...types.admin.admin_teams_list_response import AdminTeamsListResponse
from ...types.admin.cancel_subscription_response import CancelSubscriptionResponse
from ...types.admin.create_subscription_response import CreateSubscriptionResponse

__all__ = ["TeamsResource", "AsyncTeamsResource"]


class TeamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return TeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return TeamsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncJobsList[AdminTeamsListResponse]:
        """
        Lists teams in the system along with their subscription information, credit
        grants, and member counts. Supports optional pagination via limit and offset
        query parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/admin/team/list",
            page=SyncJobsList[AdminTeamsListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    team_list_params.TeamListParams,
                ),
            ),
            model=AdminTeamsListResponse,
        )

    def cancel_subscription(
        self,
        *,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelSubscriptionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/team/cancel_subscription",
            body=maybe_transform({"team_id": team_id}, team_cancel_subscription_params.TeamCancelSubscriptionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CancelSubscriptionResponse,
        )

    def create_subscription(
        self,
        *,
        billing_interval: str,
        is_active: bool,
        subscription_tier: Literal["free", "free_trial", "pro", "team", "enterprise"],
        team_id: str,
        external_customer_id: Optional[str] | Omit = omit,
        external_price_id: Optional[str] | Omit = omit,
        external_subscription_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateSubscriptionResponse:
        """
        Args:
          subscription_tier: Represents the different subscription tiers available

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/team/create_subscription",
            body=maybe_transform(
                {
                    "billing_interval": billing_interval,
                    "is_active": is_active,
                    "subscription_tier": subscription_tier,
                    "team_id": team_id,
                    "external_customer_id": external_customer_id,
                    "external_price_id": external_price_id,
                    "external_subscription_id": external_subscription_id,
                },
                team_create_subscription_params.TeamCreateSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSubscriptionResponse,
        )

    def extend_trial(
        self,
        *,
        new_expires_at: Union[str, datetime],
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtendTrialResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/team/extend_trial",
            body=maybe_transform(
                {
                    "new_expires_at": new_expires_at,
                    "team_id": team_id,
                },
                team_extend_trial_params.TeamExtendTrialParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtendTrialResponse,
        )

    def grant_credits(
        self,
        *,
        amount: int,
        source_type: str,
        team_id: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        source_ref: Optional[str] | Omit = omit,
        starts_at: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GrantCreditsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/team/grant_credits",
            body=maybe_transform(
                {
                    "amount": amount,
                    "source_type": source_type,
                    "team_id": team_id,
                    "expires_at": expires_at,
                    "source_ref": source_ref,
                    "starts_at": starts_at,
                },
                team_grant_credits_params.TeamGrantCreditsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantCreditsResponse,
        )


class AsyncTeamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncTeamsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AdminTeamsListResponse, AsyncJobsList[AdminTeamsListResponse]]:
        """
        Lists teams in the system along with their subscription information, credit
        grants, and member counts. Supports optional pagination via limit and offset
        query parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/admin/team/list",
            page=AsyncJobsList[AdminTeamsListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    team_list_params.TeamListParams,
                ),
            ),
            model=AdminTeamsListResponse,
        )

    async def cancel_subscription(
        self,
        *,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelSubscriptionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/team/cancel_subscription",
            body=await async_maybe_transform(
                {"team_id": team_id}, team_cancel_subscription_params.TeamCancelSubscriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CancelSubscriptionResponse,
        )

    async def create_subscription(
        self,
        *,
        billing_interval: str,
        is_active: bool,
        subscription_tier: Literal["free", "free_trial", "pro", "team", "enterprise"],
        team_id: str,
        external_customer_id: Optional[str] | Omit = omit,
        external_price_id: Optional[str] | Omit = omit,
        external_subscription_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateSubscriptionResponse:
        """
        Args:
          subscription_tier: Represents the different subscription tiers available

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/team/create_subscription",
            body=await async_maybe_transform(
                {
                    "billing_interval": billing_interval,
                    "is_active": is_active,
                    "subscription_tier": subscription_tier,
                    "team_id": team_id,
                    "external_customer_id": external_customer_id,
                    "external_price_id": external_price_id,
                    "external_subscription_id": external_subscription_id,
                },
                team_create_subscription_params.TeamCreateSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSubscriptionResponse,
        )

    async def extend_trial(
        self,
        *,
        new_expires_at: Union[str, datetime],
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtendTrialResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/team/extend_trial",
            body=await async_maybe_transform(
                {
                    "new_expires_at": new_expires_at,
                    "team_id": team_id,
                },
                team_extend_trial_params.TeamExtendTrialParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtendTrialResponse,
        )

    async def grant_credits(
        self,
        *,
        amount: int,
        source_type: str,
        team_id: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        source_ref: Optional[str] | Omit = omit,
        starts_at: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GrantCreditsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/team/grant_credits",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "source_type": source_type,
                    "team_id": team_id,
                    "expires_at": expires_at,
                    "source_ref": source_ref,
                    "starts_at": starts_at,
                },
                team_grant_credits_params.TeamGrantCreditsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantCreditsResponse,
        )


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.list = to_raw_response_wrapper(
            teams.list,
        )
        self.cancel_subscription = to_raw_response_wrapper(
            teams.cancel_subscription,
        )
        self.create_subscription = to_raw_response_wrapper(
            teams.create_subscription,
        )
        self.extend_trial = to_raw_response_wrapper(
            teams.extend_trial,
        )
        self.grant_credits = to_raw_response_wrapper(
            teams.grant_credits,
        )


class AsyncTeamsResourceWithRawResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.list = async_to_raw_response_wrapper(
            teams.list,
        )
        self.cancel_subscription = async_to_raw_response_wrapper(
            teams.cancel_subscription,
        )
        self.create_subscription = async_to_raw_response_wrapper(
            teams.create_subscription,
        )
        self.extend_trial = async_to_raw_response_wrapper(
            teams.extend_trial,
        )
        self.grant_credits = async_to_raw_response_wrapper(
            teams.grant_credits,
        )


class TeamsResourceWithStreamingResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.list = to_streamed_response_wrapper(
            teams.list,
        )
        self.cancel_subscription = to_streamed_response_wrapper(
            teams.cancel_subscription,
        )
        self.create_subscription = to_streamed_response_wrapper(
            teams.create_subscription,
        )
        self.extend_trial = to_streamed_response_wrapper(
            teams.extend_trial,
        )
        self.grant_credits = to_streamed_response_wrapper(
            teams.grant_credits,
        )


class AsyncTeamsResourceWithStreamingResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.list = async_to_streamed_response_wrapper(
            teams.list,
        )
        self.cancel_subscription = async_to_streamed_response_wrapper(
            teams.cancel_subscription,
        )
        self.create_subscription = async_to_streamed_response_wrapper(
            teams.create_subscription,
        )
        self.extend_trial = async_to_streamed_response_wrapper(
            teams.extend_trial,
        )
        self.grant_credits = async_to_streamed_response_wrapper(
            teams.grant_credits,
        )
