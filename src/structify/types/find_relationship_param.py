# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["FindRelationshipParam"]


class FindRelationshipParam(TypedDict, total=False):
    relationship_name: Required[str]

    source_entity_id: Required[str]

    target_entity_id: Required[str]

    allow_extra_entities: bool

    starting_searches: List[str]

    starting_urls: List[str]
