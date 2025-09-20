# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TeamSubscriptionStatus"]


class TeamSubscriptionStatus(BaseModel):
    has_active_subscription: bool

    is_trial: bool

    remaining_credits: int

    subscription_tier: Literal["free", "free_trial", "pro", "team", "enterprise"]
    """Represents the different subscription tiers available"""

    trial_expires_at: Optional[datetime] = None
