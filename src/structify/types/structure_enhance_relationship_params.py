# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StructureEnhanceRelationshipParams"]


class StructureEnhanceRelationshipParams(TypedDict, total=False):
    relationship_name: Required[str]

    allow_new_entities: bool

    source_id: Optional[str]

    special_job_type: Optional[Literal["HumanLLM"]]

    starting_searches: List[str]

    starting_urls: List[str]

    target_id: Optional[str]
