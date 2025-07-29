# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Sandbox"]


class Sandbox(BaseModel):
    id: str

    chat_session_id: str

    created_at: datetime

    modal_id: str

    modal_url: str

    status: Literal["alive", "terminated"]

    updated_at: datetime

    latest_node: Optional[str] = None
