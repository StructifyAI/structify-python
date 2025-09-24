# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .user_team import UserTeam

__all__ = ["AddMemberResponse"]


class AddMemberResponse(BaseModel):
    invitation_sent: bool

    membership: UserTeam
