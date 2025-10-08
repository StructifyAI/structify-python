# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TeamCreateSubscriptionParams"]


class TeamCreateSubscriptionParams(TypedDict, total=False):
    billing_interval: Required[str]

    is_active: Required[bool]

    subscription_tier: Required[Literal["free", "free_trial", "pro", "team", "enterprise"]]
    """Represents the different subscription tiers available"""

    team_id: Required[str]

    external_customer_id: Optional[str]

    external_price_id: Optional[str]

    external_subscription_id: Optional[str]
