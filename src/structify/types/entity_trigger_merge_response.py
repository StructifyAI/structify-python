# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = ["EntityTriggerMergeResponse", "Properties"]

Properties: TypeAlias = Union[str, bool, float, Image]


class EntityTriggerMergeResponse(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Properties]
