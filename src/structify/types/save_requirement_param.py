# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["SaveRequirementParam", "RequiredRelationship", "RequiredEntity", "RequiredProperty"]


class RequiredRelationship(TypedDict, total=False):
    relationship_name: Required[str]


class RequiredEntity(TypedDict, total=False):
    seeded_entity_id: Required[int]
    """
    The integer id corresponding to an entity in the seeded entity graph (different
    from the global dataset entity id)
    """

    entity_id: Optional[str]


class RequiredProperty(TypedDict, total=False):
    property_names: Required[List[str]]
    """If there are multiple properties, it can match just one of them"""

    table_name: Required[str]
    """The table name of the entity to update"""


SaveRequirementParam: TypeAlias = Union[RequiredRelationship, RequiredEntity, RequiredProperty]
