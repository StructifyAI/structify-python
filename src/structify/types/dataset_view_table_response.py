# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["DatasetViewTableResponse"]


class DatasetViewTableResponse(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[Optional[str], Optional[bool], Optional[int]]]
