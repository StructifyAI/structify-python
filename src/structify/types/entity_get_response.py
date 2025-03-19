# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = ["EntityGetResponse", "Properties"]

Properties: TypeAlias = Union[str, bool, float, Image]


class EntityGetResponse(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, Properties]

    updated_at: datetime
