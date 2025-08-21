# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .subscription_plan import SubscriptionPlan

__all__ = ["StripeCreateSubscriptionParams"]


class StripeCreateSubscriptionParams(TypedDict, total=False):
    origin: Required[str]

    plan: Required[SubscriptionPlan]

    team_id: Required[str]
