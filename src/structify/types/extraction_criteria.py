# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

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


class RequiredRelationship(BaseModel):
    relationship_name: str

    required_relationship: dict = FieldInfo(alias="RequiredRelationship")


class RequiredEntity(BaseModel):
    entity_id: int

    required_entity: dict = FieldInfo(alias="RequiredEntity")


class RequiredProperty(BaseModel):
    property_names: List[str]

    table_name: str
    """Vec<ExtractionCriteria> = it has to meet every one."""

    required_property: dict = FieldInfo(alias="RequiredProperty")


ExtractionCriteria = Union[RequiredProperty, RequiredEntity, RequiredProperty]
