# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .phase_activity import PhaseActivity
from .datahub_progress import DatahubProgress

__all__ = ["ExplorationProgress"]


class ExplorationProgress(BaseModel):
    phases: List[PhaseActivity]

    datahub: Optional[DatahubProgress] = None
