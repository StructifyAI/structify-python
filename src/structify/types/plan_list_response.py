# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .plan import Plan
from .._models import BaseModel

__all__ = ["PlanListResponse", "PlanListResponseItem"]


class PlanListResponseItem(BaseModel):
    plan: Plan

    plan_id: str

    status: Literal["Running", "StartingNextStep", "Completed", "Failed", "Paused"]

    step: int


PlanListResponse: TypeAlias = List[PlanListResponseItem]
