# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ChatSession"]


class ChatSession(BaseModel):
    id: str

    created_at: datetime

    ephemeral: bool

    git_application_token: str

    is_public: bool

    project_id: str

    updated_at: datetime

    name: Optional[str] = None
