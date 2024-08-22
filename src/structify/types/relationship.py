# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["Relationship"]

class Relationship(BaseModel):
    source: int

    target: int

    type: str

    properties: Optional[Dict[str, str]] = None