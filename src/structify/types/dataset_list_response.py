# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["DatasetListResponse", "DatasetListResponseItem"]

class DatasetListResponseItem(BaseModel):
    description: str

    name: str

DatasetListResponse: TypeAlias = List[DatasetListResponseItem]