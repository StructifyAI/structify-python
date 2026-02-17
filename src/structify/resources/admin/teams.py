# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import TeamRole
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
from ...types.admin import (
    team_list_params,
    team_add_member_params,
    team_extend_trial_params,
    team_expire_grants_params,
    team_grant_credits_params,
    team_remove_member_params,
    team_cancel_subscription_params,
    team_create_subscription_params,
    team_update_seats_override_params,
)
from ..._base_client import make_request_options
from ...types.team_role import TeamRole
from ...types.admin.team_list_response import TeamListResponse
from ...types.admin.extend_trial_response import ExtendTrialResponse
from ...types.admin.expire_grants_response import ExpireGrantsResponse
from ...types.admin.grant_credits_response import GrantCreditsResponse
from ...types.admin.admin_add_member_response import AdminAddMemberResponse
from ...types.admin.admin_list_members_response import AdminListMembersResponse
from ...types.admin.admin_remove_member_response import AdminRemoveMemberResponse
from ...types.admin.cancel_subscription_response import CancelSubscriptionResponse
from ...types.admin.create_subscription_response import CreateSubscriptionResponse
from ...types.admin.update_seats_override_response import UpdateSeatsOverrideResponse

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
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamListResponse:
        """
        Lists teams in the system along with their subscription information, credit
        grants, and member counts. Supports optional pagination via limit, offset, and
        search query parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/team/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                    },
                    team_list_params.TeamListParams,
                ),
            ),
            cast_to=TeamListResponse,
        )

    def add_member(
        self,
        *,
        email: str,
        role: TeamRole,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminAddMemberResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/team/add_member",
            body=maybe_transform(
                {
                    "email": email,
                    "role": role,
                    "team_id": team_id,
                },
                team_add_member_params.TeamAddMemberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminAddMemberResponse,
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

    def expire_grants(
        self,
        *,
        source_type: str,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpireGrantsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/team/expire_grants",
            body=maybe_transform(
                {
                    "source_type": source_type,
                    "team_id": team_id,
                },
                team_expire_grants_params.TeamExpireGrantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpireGrantsResponse,
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

    def list_members(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminListMembersResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._get(
            f"/admin/team/{team_id}/members",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminListMembersResponse,
        )

    def remove_member(
        self,
        *,
        team_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminRemoveMemberResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/team/remove_member",
            body=maybe_transform(
                {
                    "team_id": team_id,
                    "user_id": user_id,
                },
                team_remove_member_params.TeamRemoveMemberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminRemoveMemberResponse,
        )

    def update_seats_override(
        self,
        *,
        team_id: str,
        seats_override: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateSeatsOverrideResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/team/update_seats_override",
            body=maybe_transform(
                {
                    "team_id": team_id,
                    "seats_override": seats_override,
                },
                team_update_seats_override_params.TeamUpdateSeatsOverrideParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateSeatsOverrideResponse,
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

    async def list(
        self,
        *,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TeamListResponse:
        """
        Lists teams in the system along with their subscription information, credit
        grants, and member counts. Supports optional pagination via limit, offset, and
        search query parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/team/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                    },
                    team_list_params.TeamListParams,
                ),
            ),
            cast_to=TeamListResponse,
        )

    async def add_member(
        self,
        *,
        email: str,
        role: TeamRole,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminAddMemberResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/team/add_member",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "role": role,
                    "team_id": team_id,
                },
                team_add_member_params.TeamAddMemberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminAddMemberResponse,
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

    async def expire_grants(
        self,
        *,
        source_type: str,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpireGrantsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/team/expire_grants",
            body=await async_maybe_transform(
                {
                    "source_type": source_type,
                    "team_id": team_id,
                },
                team_expire_grants_params.TeamExpireGrantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpireGrantsResponse,
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

    async def list_members(
        self,
        team_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminListMembersResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._get(
            f"/admin/team/{team_id}/members",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminListMembersResponse,
        )

    async def remove_member(
        self,
        *,
        team_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminRemoveMemberResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/team/remove_member",
            body=await async_maybe_transform(
                {
                    "team_id": team_id,
                    "user_id": user_id,
                },
                team_remove_member_params.TeamRemoveMemberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminRemoveMemberResponse,
        )

    async def update_seats_override(
        self,
        *,
        team_id: str,
        seats_override: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateSeatsOverrideResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/team/update_seats_override",
            body=await async_maybe_transform(
                {
                    "team_id": team_id,
                    "seats_override": seats_override,
                },
                team_update_seats_override_params.TeamUpdateSeatsOverrideParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateSeatsOverrideResponse,
        )


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.list = to_raw_response_wrapper(
            teams.list,
        )
        self.add_member = to_raw_response_wrapper(
            teams.add_member,
        )
        self.cancel_subscription = to_raw_response_wrapper(
            teams.cancel_subscription,
        )
        self.create_subscription = to_raw_response_wrapper(
            teams.create_subscription,
        )
        self.expire_grants = to_raw_response_wrapper(
            teams.expire_grants,
        )
        self.extend_trial = to_raw_response_wrapper(
            teams.extend_trial,
        )
        self.grant_credits = to_raw_response_wrapper(
            teams.grant_credits,
        )
        self.list_members = to_raw_response_wrapper(
            teams.list_members,
        )
        self.remove_member = to_raw_response_wrapper(
            teams.remove_member,
        )
        self.update_seats_override = to_raw_response_wrapper(
            teams.update_seats_override,
        )


class AsyncTeamsResourceWithRawResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.list = async_to_raw_response_wrapper(
            teams.list,
        )
        self.add_member = async_to_raw_response_wrapper(
            teams.add_member,
        )
        self.cancel_subscription = async_to_raw_response_wrapper(
            teams.cancel_subscription,
        )
        self.create_subscription = async_to_raw_response_wrapper(
            teams.create_subscription,
        )
        self.expire_grants = async_to_raw_response_wrapper(
            teams.expire_grants,
        )
        self.extend_trial = async_to_raw_response_wrapper(
            teams.extend_trial,
        )
        self.grant_credits = async_to_raw_response_wrapper(
            teams.grant_credits,
        )
        self.list_members = async_to_raw_response_wrapper(
            teams.list_members,
        )
        self.remove_member = async_to_raw_response_wrapper(
            teams.remove_member,
        )
        self.update_seats_override = async_to_raw_response_wrapper(
            teams.update_seats_override,
        )


class TeamsResourceWithStreamingResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.list = to_streamed_response_wrapper(
            teams.list,
        )
        self.add_member = to_streamed_response_wrapper(
            teams.add_member,
        )
        self.cancel_subscription = to_streamed_response_wrapper(
            teams.cancel_subscription,
        )
        self.create_subscription = to_streamed_response_wrapper(
            teams.create_subscription,
        )
        self.expire_grants = to_streamed_response_wrapper(
            teams.expire_grants,
        )
        self.extend_trial = to_streamed_response_wrapper(
            teams.extend_trial,
        )
        self.grant_credits = to_streamed_response_wrapper(
            teams.grant_credits,
        )
        self.list_members = to_streamed_response_wrapper(
            teams.list_members,
        )
        self.remove_member = to_streamed_response_wrapper(
            teams.remove_member,
        )
        self.update_seats_override = to_streamed_response_wrapper(
            teams.update_seats_override,
        )


class AsyncTeamsResourceWithStreamingResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.list = async_to_streamed_response_wrapper(
            teams.list,
        )
        self.add_member = async_to_streamed_response_wrapper(
            teams.add_member,
        )
        self.cancel_subscription = async_to_streamed_response_wrapper(
            teams.cancel_subscription,
        )
        self.create_subscription = async_to_streamed_response_wrapper(
            teams.create_subscription,
        )
        self.expire_grants = async_to_streamed_response_wrapper(
            teams.expire_grants,
        )
        self.extend_trial = async_to_streamed_response_wrapper(
            teams.extend_trial,
        )
        self.grant_credits = async_to_streamed_response_wrapper(
            teams.grant_credits,
        )
        self.list_members = async_to_streamed_response_wrapper(
            teams.list_members,
        )
        self.remove_member = async_to_streamed_response_wrapper(
            teams.remove_member,
        )
        self.update_seats_override = async_to_streamed_response_wrapper(
            teams.update_seats_override,
        )
