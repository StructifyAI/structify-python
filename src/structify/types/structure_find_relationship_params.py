# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .find_relationship_param import FindRelationshipParam

__all__ = ["StructureFindRelationshipParams", "Body"]


class StructureFindRelationshipParams(TypedDict, total=False):
    body: Required[Body]


class Body(FindRelationshipParam):
    special_job_type: Optional[Literal["HumanLLM"]]
