# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StructureEnhanceParams"]


class StructureEnhanceParams(TypedDict, total=False):
    entity_id: Required[str]

    allow_new_entities: bool

    property_name: Optional[str]

    relationship_name: Optional[str]

    special_job_type: Optional[Literal["HumanLLM"]]
