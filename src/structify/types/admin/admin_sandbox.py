# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .sandbox_type import SandboxType

__all__ = ["AdminSandbox"]


class AdminSandbox(BaseModel):
    id: str

    active_count: int

    created_at: datetime

    sandbox_type: SandboxType

    status: Literal["alive", "terminated"]

    updated_at: datetime

    chat_session_id: Optional[str] = None

    exploration_run_id: Optional[str] = None

    latest_node: Optional[str] = None

    modal_id: Optional[str] = None

    modal_url: Optional[str] = None
