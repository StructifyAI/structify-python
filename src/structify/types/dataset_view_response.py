# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["DatasetViewResponse", "KgEntity", "Relationship"]


class KgEntity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[Optional[str], Optional[bool], Optional[int]]]


class Relationship(BaseModel):
    from_id: str

    label: str

    to_id: str


DatasetViewResponse: TypeAlias = Union[KgEntity, Relationship]
