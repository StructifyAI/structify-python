# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["DocumentUploadParams"]


class DocumentUploadParams(TypedDict, total=False):
    content: Required[FileTypes]

    file_type: Required[Literal["Text", "Pdf", "SEC", "ExecutionHistory"]]

    path: Required[FileTypes]
