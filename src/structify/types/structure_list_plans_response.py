# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .plan import Plan
from .._models import BaseModel

__all__ = ["StructureListPlansResponse", "StructureListPlansResponseItem"]


class StructureListPlansResponseItem(BaseModel):
    plan: Plan

    plan_id: str

    status: Literal["Running", "StartingNextStep", "Completed", "Failed"]

    step: int


StructureListPlansResponse: TypeAlias = List[StructureListPlansResponseItem]
