# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ExplorationRun"]


class ExplorationRun(BaseModel):
    id: str

    connector_id: str

    created_at: datetime

    checkpoint_blob_name: Optional[str] = None

    latest_snapshot_blob_name: Optional[str] = None

    triggered_by: Optional[str] = None
