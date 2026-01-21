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

    provider: Literal["modal", "daytona"]

    provider_id: str

    status: Literal["alive", "terminated"]

    tunnel_url: str

    updated_at: datetime

    api_url: Optional[str] = None

    latest_node: Optional[str] = None

    session_id: Optional[str] = None
