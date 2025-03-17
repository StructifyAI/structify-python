# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SourceListResponse", "SourceListResponseItem"]


class SourceListResponseItem(BaseModel):
    id: int

    created_at: datetime

    is_summary: bool

    link: object

    location: object

    user_specified: bool

    step_id: Optional[int] = None


SourceListResponse: TypeAlias = List[SourceListResponseItem]
