# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["Source", "URL", "Name", "SecFilingLink"]


class URL(BaseModel):
    url: str


class Name(BaseModel):
    name: str


class SecFilingLink(BaseModel):
    accession_number: str

    cik_number: str


Source: TypeAlias = Union[URL, Name, SecFilingLink, Optional[object]]
