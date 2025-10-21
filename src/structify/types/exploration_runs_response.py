# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .exploration_run import ExplorationRun

__all__ = ["ExplorationRunsResponse"]


class ExplorationRunsResponse(BaseModel):
    runs: List[ExplorationRun]
