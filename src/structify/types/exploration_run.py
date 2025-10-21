# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["ExplorationRun"]


class ExplorationRun(BaseModel):
    created_at: datetime

    run_id: str
