# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from ..team_role import TeamRole

__all__ = ["AdminListMembersResponse", "Member"]


class Member(BaseModel):
    created_at: datetime

    email: str

    role: TeamRole

    team_id: str

    user_id: str


class AdminListMembersResponse(BaseModel):
    members: List[Member]
