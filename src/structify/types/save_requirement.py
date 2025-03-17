# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SaveRequirement", "RequiredRelationship", "RequiredEntity", "RequiredProperty"]


class RequiredRelationship(BaseModel):
    relationship_name: str


class RequiredEntity(BaseModel):
    seeded_entity_id: int
    """
    The integer id corresponding to an entity in the seeded entity graph (different
    from the global dataset entity id)
    """

    entity_id: Optional[str] = None


class RequiredProperty(BaseModel):
    property_names: List[str]
    """If there are multiple properties, it can match just one of them"""

    table_name: str
    """The table name of the entity to update"""


SaveRequirement: TypeAlias = Union[RequiredRelationship, RequiredEntity, RequiredProperty]
