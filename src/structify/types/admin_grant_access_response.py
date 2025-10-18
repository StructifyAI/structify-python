# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .chat_session_role import ChatSessionRole

__all__ = ["AdminGrantAccessResponse"]


class AdminGrantAccessResponse(BaseModel):
    expires_at: datetime

    role: ChatSessionRole
