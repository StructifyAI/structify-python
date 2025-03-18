# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SourceListResponse", "SourceListResponseItem"]


class SourceListResponseItem(BaseModel):
    id: str

    created_at: datetime

    is_summary: bool

    user_specified: bool

    link: Optional[object] = None

    location: Optional[object] = None

    step_id: Optional[str] = None


SourceListResponse: TypeAlias = List[SourceListResponseItem]
