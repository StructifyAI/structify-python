# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Source", "Web", "WebWeb", "Document", "DocumentDocument", "UserCreatedWeb", "UserCreatedWebUserCreatedWeb"]


class WebWeb(BaseModel):
    url: str


class Web(BaseModel):
    web: WebWeb = FieldInfo(alias="Web")


class DocumentDocument(BaseModel):
    name: str


class Document(BaseModel):
    document: DocumentDocument = FieldInfo(alias="Document")


class UserCreatedWebUserCreatedWeb(BaseModel):
    url: str


class UserCreatedWeb(BaseModel):
    user_created_web: UserCreatedWebUserCreatedWeb = FieldInfo(alias="UserCreatedWeb")


Source: TypeAlias = Union[Web, Document, Literal["UserCreated"], UserCreatedWeb]
