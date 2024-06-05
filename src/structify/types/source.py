# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Source",
    "Text",
    "TextText",
    "Document",
    "DocumentDocument",
    "Web",
    "WebWeb",
    "SecFiling",
    "SecFilingSecFiling",
]


class TextText(BaseModel):
    text_content: str


class Text(BaseModel):
    text: TextText = FieldInfo(alias="Text")


class DocumentDocument(BaseModel):
    path: str


class Document(BaseModel):
    document: DocumentDocument = FieldInfo(alias="Document")


class WebWeb(BaseModel):
    phrase: str

    starting_website: Optional[str] = None


class Web(BaseModel):
    web: WebWeb = FieldInfo(alias="Web")


class SecFilingSecFiling(BaseModel):
    accession_number: Optional[str] = None

    quarter: Optional[int] = None

    year: Optional[int] = None


class SecFiling(BaseModel):
    sec_filing: SecFilingSecFiling = FieldInfo(alias="SECFiling")


Source = Union[Text, Document, Web, SecFiling]
