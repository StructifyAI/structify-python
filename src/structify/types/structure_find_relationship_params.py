# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StructureFindRelationshipParams"]


class StructureFindRelationshipParams(TypedDict, total=False):
    relationship_name: Required[str]

    source_entity_id: Required[str]

    target_entity_id: Required[str]

    allow_extra_entities: bool

    special_job_type: Optional[Literal["HumanLLM"]]

    starting_searches: List[str]

    starting_urls: List[str]
