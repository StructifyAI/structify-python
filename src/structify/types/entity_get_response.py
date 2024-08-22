# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import Dict, Union, Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["EntityGetResponse"]

class EntityGetResponse(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[Optional[str], Optional[bool], Optional[int]]]