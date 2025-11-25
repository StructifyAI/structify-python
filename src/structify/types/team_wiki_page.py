# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TeamWikiPage"]


class TeamWikiPage(BaseModel):
    id: str

    content: Dict[str, object]

    created_at: datetime

    created_by: str

    slug: str

    team_id: str

    title: str

    updated_at: datetime

    deleted_at: Optional[datetime] = None
