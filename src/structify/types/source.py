# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Source", "Web", "Document"]



class Web(BaseModel):
    url: str

    web: dict = FieldInfo(alias="Web") 


class Document(BaseModel):
    name: str
    document: dict = FieldInfo(alias="Document")


Source = Union[Web, Document, Literal["None"]]
