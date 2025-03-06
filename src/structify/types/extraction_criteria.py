# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ExtractionCriteria",
    "RelationshipExtraction",
    "RelationshipExtractionRelationshipExtraction",
    "EntityExtraction",
    "EntityExtractionEntityExtraction",
    "GenericProperty",
    "GenericPropertyGenericProperty",
]


class RelationshipExtractionRelationshipExtraction(BaseModel):
    relationship_name: str


class RelationshipExtraction(BaseModel):
    relationship_extraction: RelationshipExtractionRelationshipExtraction = FieldInfo(alias="RelationshipExtraction")


class EntityExtractionEntityExtraction(BaseModel):
    seeded_kg_id: int
    """The integer id corresponding to an entity in the seeded kg"""

    dataset_entity_id: Optional[str] = None


class EntityExtraction(BaseModel):
    entity_extraction: EntityExtractionEntityExtraction = FieldInfo(alias="EntityExtraction")


class GenericPropertyGenericProperty(BaseModel):
    property_names: List[str]

    table_name: str
    """Vec<ExtractionCriteria> = it has to meet every one."""


class GenericProperty(BaseModel):
    generic_property: GenericPropertyGenericProperty = FieldInfo(alias="GenericProperty")


ExtractionCriteria: TypeAlias = Union[RelationshipExtraction, EntityExtraction, GenericProperty]
