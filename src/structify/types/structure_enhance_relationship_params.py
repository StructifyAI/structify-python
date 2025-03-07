# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .enhance_relationship_param import EnhanceRelationshipParam

__all__ = ["StructureEnhanceRelationshipParams", "Body"]


class StructureEnhanceRelationshipParams(TypedDict, total=False):
    body: Required[Body]


class Body(EnhanceRelationshipParam):
    special_job_type: Optional[Literal["HumanLLM"]]
