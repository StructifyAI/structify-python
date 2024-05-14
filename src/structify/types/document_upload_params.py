# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DocumentUploadParams"]


class DocumentUploadParams(TypedDict, total=False):
    doctype: Required[Literal["Text", "Pdf", "SEC", "ExecutionHistory"]]

    path: Required[str]
    """The path you want to upload the file to."""

    body: Required[object]
