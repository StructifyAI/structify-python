# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .set_access_action import SetAccessAction

__all__ = ["SetAccessResponse"]


class SetAccessResponse(BaseModel):
    action: SetAccessAction

    expires_at: Optional[datetime] = None

    membership_id: Optional[str] = None
