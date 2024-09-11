# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["StructureEnhanceParams"]


class StructureEnhanceParams(TypedDict, total=False):
    entity_id: Required[str]

    property_name: Optional[str]

    relationship_name: Optional[str]
