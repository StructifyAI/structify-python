# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["StructureEnhanceRelationshipParams"]


class StructureEnhanceRelationshipParams(TypedDict, total=False):
    entity_id: Required[str]

    relationship_name: Required[str]

    allow_extra_entities: bool

    banned_domains: SequenceNotStr[str]

    node_id: Optional[str]

    starting_searches: SequenceNotStr[str]

    starting_urls: SequenceNotStr[str]
