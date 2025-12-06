# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["APIKeyInfo"]


class APIKeyInfo(BaseModel):
    id: str

    created_at: datetime

    membership_id: str

    expires_at: Optional[datetime] = None

    last_used_at: Optional[datetime] = None

    name: Optional[str] = None

    revoked_at: Optional[datetime] = None
