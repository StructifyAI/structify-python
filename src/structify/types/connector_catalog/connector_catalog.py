# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ConnectorCatalog"]


class ConnectorCatalog(BaseModel):
    id: str

    categories: List[Optional[str]]

    created_at: datetime

    name: str

    slug: str

    updated_at: datetime

    description: Optional[str] = None

    logo_path: Optional[str] = None

    priority: Optional[int] = None
