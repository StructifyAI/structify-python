# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Source", "Web", "WebWeb", "Document", "DocumentDocument", "SecFiling", "SecFilingSecFiling"]


class WebWeb(BaseModel):
    url: str


class Web(BaseModel):
    web: WebWeb = FieldInfo(alias="Web")


class DocumentDocument(BaseModel):
    name: str


class Document(BaseModel):
    document: DocumentDocument = FieldInfo(alias="Document")


class SecFilingSecFiling(BaseModel):
    accession_number: str

    cik_number: str


class SecFiling(BaseModel):
    sec_filing: SecFilingSecFiling = FieldInfo(alias="SecFiling")


Source: TypeAlias = Union[Web, Document, SecFiling]
