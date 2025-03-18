# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = ["DatasetViewRelationshipsResponse", "Properties"]

Properties: TypeAlias = Union[str, bool, float, Image]


class DatasetViewRelationshipsResponse(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, Properties]

    to_id: str
