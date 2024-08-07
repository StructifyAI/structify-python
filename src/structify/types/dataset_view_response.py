# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["DatasetViewResponse", "UnionMember0", "UnionMember1"]


class UnionMember0(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[Optional[str], Optional[bool], Optional[int]]]


class UnionMember1(BaseModel):
    from_id: str

    label: str

    to_id: str


DatasetViewResponse: TypeAlias = Union[List[UnionMember0], List[UnionMember1]]
