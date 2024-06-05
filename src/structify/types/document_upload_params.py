# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["DocumentUploadParams"]


class DocumentUploadParams(TypedDict, total=False):
    file_type: Required[Literal["Text", "Pdf", "SEC", "ExecutionHistory"]]
    """\"The type of file to store" """

    path: Required[str]
    """The path to store the document"""

    contents: Required[FileTypes]
