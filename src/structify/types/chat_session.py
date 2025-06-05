# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["ChatSession"]


class ChatSession(BaseModel):
    id: str

    created_at: datetime

    updated_at: datetime

    user_id: str
