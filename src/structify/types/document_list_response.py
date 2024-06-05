# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DocumentListResponse",
    "DocumentListResponseItem",
    "DocumentListResponseItemContent",
    "DocumentListResponseItemContentRemote",
    "DocumentListResponseItemContentLocal",
]


class DocumentListResponseItemContentRemote(BaseModel):
    remote: str = FieldInfo(alias="Remote")


class DocumentListResponseItemContentLocal(BaseModel):
    local: object = FieldInfo(alias="Local")


DocumentListResponseItemContent = Union[DocumentListResponseItemContentRemote, DocumentListResponseItemContentLocal]


class DocumentListResponseItem(BaseModel):
    content: DocumentListResponseItemContent

    document_type: Literal["Text", "Pdf", "SEC", "ExecutionHistory"]

    name: str


DocumentListResponse = List[DocumentListResponseItem]
