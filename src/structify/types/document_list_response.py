# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["DocumentListResponse", "DocumentListResponseItem"]


class DocumentListResponseItem(BaseModel):
    document_type: Literal["Text", "PDF", "SEC", "ExecutionHistory"]

    name: str

    content: Optional[object] = None


DocumentListResponse: TypeAlias = List[DocumentListResponseItem]
