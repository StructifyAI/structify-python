# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["EnhanceRelationshipParam"]


class EnhanceRelationshipParam(TypedDict, total=False):
    entity_id: Required[str]

    relationship_name: Required[str]

    allow_extra_entities: bool

    starting_searches: List[str]

    starting_urls: List[str]
