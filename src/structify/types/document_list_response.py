# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["DocumentListResponse", "DocumentListResponseItem"]


class DocumentListResponseItem(BaseModel):
    id: str

    created_at: datetime

    file_bytes: object

    file_type: Literal["Text", "PDF", "SEC"]

    name: str

    user_id: str

    created_from_job: Optional[str] = None

    dataset_id: Optional[str] = None

    project_id: Optional[str] = None


DocumentListResponse: TypeAlias = List[DocumentListResponseItem]
