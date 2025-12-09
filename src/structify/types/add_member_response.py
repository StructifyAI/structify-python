# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .team_role import TeamRole

__all__ = ["AddMemberResponse", "Membership"]


class Membership(BaseModel):
    """Contains membership information and API token value"""

    id: str

    created_at: datetime

    pending: bool

    role: TeamRole

    team_id: str

    value: object

    invitation_expires_at: Optional[datetime] = None

    invitation_token: Optional[str] = None

    invited_at: Optional[datetime] = None

    invited_by_user_id: Optional[str] = None

    invitee_email: Optional[str] = None

    user_id: Optional[str] = None


class AddMemberResponse(BaseModel):
    invitation_sent: bool

    membership: Membership
    """Contains membership information and API token value"""
