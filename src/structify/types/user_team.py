# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .team_role import TeamRole

__all__ = ["UserTeam"]


class UserTeam(BaseModel):
    id: str

    created_at: datetime

    role: TeamRole

    team_id: str

    user_id: str
