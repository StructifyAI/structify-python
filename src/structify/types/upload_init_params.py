# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .signed_upload_target import SignedUploadTarget

__all__ = ["UploadInitParams"]


class UploadInitParams(TypedDict, total=False):
    content_type: Required[str]

    file_size: Required[int]

    target: Required[SignedUploadTarget]

    chat_id: Optional[str]

    node_id: Optional[str]
