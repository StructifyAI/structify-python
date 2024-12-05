# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["DatasetViewRelationshipsResponse", "Properties", "PropertiesImage"]


class PropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


Properties: TypeAlias = Union[str, bool, float, PropertiesImage]


class DatasetViewRelationshipsResponse(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, Properties]

    to_id: str
