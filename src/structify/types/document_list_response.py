# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing_extensions import Literal, TypeAlias

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["DocumentListResponse", "DocumentListResponseItem"]

class DocumentListResponseItem(BaseModel):
    document_type: Literal["Text", "PDF", "SEC", "ExecutionHistory"]

    name: str

    content: Optional[object] = None

DocumentListResponse: TypeAlias = List[DocumentListResponseItem]