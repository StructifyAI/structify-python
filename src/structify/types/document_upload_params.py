# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from .._types import FileTypes

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["DocumentUploadParams"]

class DocumentUploadParams(TypedDict, total=False):
    content: Required[FileTypes]

    file_type: Required[Literal["Text", "PDF", "SEC", "ExecutionHistory"]]

    path: Required[FileTypes]