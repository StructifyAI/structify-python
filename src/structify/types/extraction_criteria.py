# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["ExtractionCriteria", "RelationshipExtraction", "RelationshipExtractionRelationshipExtraction", "EntityExtraction", "EntityExtractionEntityExtraction", "GenericProperty", "GenericPropertyGenericProperty"]

class RelationshipExtractionRelationshipExtraction(BaseModel):
    relationship_name: str

class RelationshipExtraction(BaseModel):
    relationship_extraction: RelationshipExtractionRelationshipExtraction = FieldInfo(alias = "RelationshipExtraction")

class EntityExtractionEntityExtraction(BaseModel):
    entity_id: int

class EntityExtraction(BaseModel):
    entity_extraction: EntityExtractionEntityExtraction = FieldInfo(alias = "EntityExtraction")

class GenericPropertyGenericProperty(BaseModel):
    property_names: List[str]

    table_name: str
    """Vec<ExtractionCriteria> = it has to meet every one."""

class GenericProperty(BaseModel):
    generic_property: GenericPropertyGenericProperty = FieldInfo(alias = "GenericProperty")

ExtractionCriteria: TypeAlias = Union[RelationshipExtraction, EntityExtraction, GenericProperty]