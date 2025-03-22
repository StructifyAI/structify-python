# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .plan import Plan
from .._models import BaseModel

__all__ = ["PlanListResponse"]


class PlanListResponse(BaseModel):
    plan: Plan

    plan_id: str

    status: Literal["Queued", "Running", "Completed", "Failed", "Paused"]

    step: int
