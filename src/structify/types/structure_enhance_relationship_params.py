# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["StructureEnhanceRelationshipParams"]


class StructureEnhanceRelationshipParams(TypedDict, total=False):
    relationship_name: Required[str]

    allow_new_entities: bool

    source_id: Optional[str]

    target_id: Optional[str]
