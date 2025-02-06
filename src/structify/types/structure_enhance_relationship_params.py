# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StructureEnhanceRelationshipParams"]


class StructureEnhanceRelationshipParams(TypedDict, total=False):
    relationship_name: Required[str]

    allow_new_entities: bool

    source_id: Optional[str]

    special_job_type: Optional[Literal["HumanLLM"]]

    target_id: Optional[str]
