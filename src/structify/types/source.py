# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["Source", "Web", "WebWeb", "Document", "DocumentDocument"]

class WebWeb(BaseModel):
    url: str

class Web(BaseModel):
    web: WebWeb = FieldInfo(alias = "Web")

class DocumentDocument(BaseModel):
    name: str

class Document(BaseModel):
    document: DocumentDocument = FieldInfo(alias = "Document")

Source: TypeAlias = Union[Web, Document, Literal["UserCreated"]]