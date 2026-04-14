# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .signed_upload_target import SignedUploadTarget

__all__ = ["UploadCompleteParams"]


class UploadCompleteParams(TypedDict, total=False):
    blob_name: Required[str]

    content_type: Required[str]

    target: Required[SignedUploadTarget]

    cache_final_rows: Optional[int]

    cache_final_size_bytes: Optional[int]

    cache_max_bytes: Optional[int]

    cache_original_rows: Optional[int]

    cache_original_size_bytes: Optional[int]

    cache_truncated: Optional[bool]

    chat_id: Optional[str]

    file_name: Optional[str]

    node_id: Optional[str]

    output_schema: object
