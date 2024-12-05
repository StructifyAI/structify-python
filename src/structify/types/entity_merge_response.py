# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EntityMergeResponse", "Properties", "PropertiesImage"]


class PropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


Properties: TypeAlias = Union[str, bool, float, PropertiesImage]


class EntityMergeResponse(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Properties]
