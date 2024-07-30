# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RequiredEntity", "EntityExtraction"]


class EntityExtraction(BaseModel):
    entity_id: int


class RequiredEntity(BaseModel):
    entity_extraction: EntityExtraction = FieldInfo(alias="EntityExtraction")
