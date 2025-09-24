# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AcceptInvitationResponse"]


class AcceptInvitationResponse(BaseModel):
    requires_signup: bool

    success: bool

    team_id: str

    team_name: str

    user_email: str
