# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["DocumentListResponse", "DocumentListResponseItem"]


class DocumentListResponseItem(BaseModel):
    created_time: datetime

    document_type: Literal["Text", "PDF", "SEC"]

    name: str

    content: Optional[object] = None


DocumentListResponse: TypeAlias = List[DocumentListResponseItem]
