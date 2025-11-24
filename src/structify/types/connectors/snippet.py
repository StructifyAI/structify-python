# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Snippet"]


class Snippet(BaseModel):
    id: str

    connector_type: str

    created_at: datetime

    updated_at: datetime

    usage_snippet: Optional[str] = None
