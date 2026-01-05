# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["ChatTemplate"]


class ChatTemplate(BaseModel):
    id: str

    chat_session_id: str

    created_at: datetime

    created_by: str

    description: str

    display_order: int

    image_url: str

    is_active: bool

    title: str

    updated_at: datetime

    updated_by: str
