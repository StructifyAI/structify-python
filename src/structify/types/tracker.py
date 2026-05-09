# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Tracker"]


class Tracker(BaseModel):
    id: str

    allowed_origins: List[str]

    created_at: datetime

    name: str

    team_id: str

    revoked_at: Optional[datetime] = None
