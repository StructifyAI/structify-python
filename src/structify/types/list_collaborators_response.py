# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .chat_session_role import ChatSessionRole

__all__ = ["ListCollaboratorsResponse", "Collaborator"]


class Collaborator(BaseModel):
    """DTO for chat collaborator.

    Identity is keyed on membership_id — clients
    resolve email/name via their team-members lookup.
    """

    created_at: datetime

    membership_id: str

    role: ChatSessionRole

    updated_at: datetime


class ListCollaboratorsResponse(BaseModel):
    """Response for listing collaborators"""

    collaborators: List[Collaborator]
