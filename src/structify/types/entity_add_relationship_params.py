# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

__all__ = ["EntityAddRelationshipParams"]


class EntityAddRelationshipParams(TypedDict, total=False):
    dataset: Required[str]

    from_id: Required[str]

    relationship_type: Required[str]

    to_id: Required[str]

    properties: Dict[str, Union[str, bool, float]]
