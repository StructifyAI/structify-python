# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["FindRelationshipParam"]


class FindRelationshipParam(TypedDict, total=False):
    from_id: Required[str]

    relationship_name: Required[str]

    to_id: Required[str]

    allow_extra_entities: bool

    starting_searches: List[str]

    starting_urls: List[str]
