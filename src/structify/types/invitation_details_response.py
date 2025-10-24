# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["InvitationDetailsResponse"]


class InvitationDetailsResponse(BaseModel):
    invitee_email: str

    team_name: str

    user_exists: bool
