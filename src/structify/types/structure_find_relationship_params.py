# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StructureFindRelationshipParams"]


class StructureFindRelationshipParams(TypedDict, total=False):
    from_id: Required[str]

    relationship_name: Required[str]

    to_id: Required[str]

    allow_extra_entities: bool

    special_job_type: Optional[Literal["HumanLLM"]]

    starting_searches: List[str]

    starting_urls: List[str]
