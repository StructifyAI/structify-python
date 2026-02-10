# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..team_role import TeamRole

__all__ = ["AdminListMembersResponse", "Member"]


class Member(BaseModel):
    created_at: datetime

    email: str

    pending: bool

    role: TeamRole

    team_id: str

    user_id: Optional[str] = None


class AdminListMembersResponse(BaseModel):
    members: List[Member]
