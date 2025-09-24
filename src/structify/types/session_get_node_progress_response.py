# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SessionGetNodeProgressResponse", "SessionGetNodeProgressResponseItem"]


class SessionGetNodeProgressResponseItem(BaseModel):
    current: int

    elapsed_seconds: float

    started_at: datetime

    total: int


SessionGetNodeProgressResponse: TypeAlias = Dict[str, SessionGetNodeProgressResponseItem]
