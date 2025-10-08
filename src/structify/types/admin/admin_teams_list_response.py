# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..team import Team
from ..._models import BaseModel

__all__ = ["AdminTeamsListResponse", "AdminTeamsListResponseGrant", "AdminTeamsListResponseSubscription"]


class AdminTeamsListResponseGrant(BaseModel):
    id: str

    amount: int

    amount_remaining: int

    created_at: datetime

    source_type: str

    team_id: str

    updated_at: datetime

    expires_at: Optional[datetime] = None

    source_ref: Optional[str] = None

    starts_at: Optional[datetime] = None


class AdminTeamsListResponseSubscription(BaseModel):
    has_active_subscription: bool

    is_trial: bool

    remaining_credits: int

    subscription_tier: Literal["free", "free_trial", "pro", "team", "enterprise"]
    """Represents the different subscription tiers available"""

    trial_expires_at: Optional[datetime] = None


class AdminTeamsListResponse(Team):
    grants: List[AdminTeamsListResponseGrant]

    member_count: int

    subscription: AdminTeamsListResponseSubscription
