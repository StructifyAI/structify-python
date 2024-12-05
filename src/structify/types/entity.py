# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = ["Entity", "Properties"]

Properties: TypeAlias = Union[str, bool, float, Image]


class Entity(BaseModel):
    id: int

    properties: Dict[str, Properties]

    type: str
