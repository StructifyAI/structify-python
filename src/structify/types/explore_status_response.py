# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .exploration_status import ExplorationStatus

__all__ = ["ExploreStatusResponse"]


class ExploreStatusResponse(BaseModel):
    status: ExplorationStatus

    error: Optional[str] = None

    started_at: Optional[datetime] = None
