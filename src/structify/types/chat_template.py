# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .template_question import TemplateQuestion

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

    questions: List[TemplateQuestion]

    title: str

    updated_at: datetime

    updated_by: str
