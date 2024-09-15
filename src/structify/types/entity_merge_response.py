# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from datetime import datetime

from .._models import BaseModel

__all__ = ["EntityMergeResponse"]


class EntityMergeResponse(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[str, int, bool]]
