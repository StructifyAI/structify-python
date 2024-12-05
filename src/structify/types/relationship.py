# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["Relationship", "Properties", "PropertiesImage"]


class PropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


Properties: TypeAlias = Union[str, bool, float, PropertiesImage]


class Relationship(BaseModel):
    source: int

    target: int

    type: str

    properties: Optional[Dict[str, Properties]] = None
