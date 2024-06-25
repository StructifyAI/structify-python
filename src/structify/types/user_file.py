# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserFile"]


class UserFile(BaseModel):
    document_type: Literal["Text", "Pdf", "SEC", "ExecutionHistory"]

    name: str

    content: Optional[object] = None
