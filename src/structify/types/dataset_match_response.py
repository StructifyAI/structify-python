# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["DatasetMatchResponse", "Entity", "EntityProperties", "EntityPropertiesImage"]


class EntityPropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


EntityProperties: TypeAlias = Union[str, bool, float, EntityPropertiesImage]


class Entity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, EntityProperties]


class DatasetMatchResponse(BaseModel):
    entity: Entity

    score: float
