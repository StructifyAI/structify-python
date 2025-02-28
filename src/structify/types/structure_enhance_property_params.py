# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["StructureEnhancePropertyParams"]


class StructureEnhancePropertyParams(TypedDict, total=False):
    entity_id: Required[str]

    property_name: Required[str]

    allow_extra_entities: bool

    special_job_type: Optional[object]

    starting_searches: List[str]

    starting_urls: List[str]
