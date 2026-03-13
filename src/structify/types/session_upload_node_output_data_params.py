# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["SessionUploadNodeOutputDataParams"]


class SessionUploadNodeOutputDataParams(TypedDict, total=False):
    content: Required[FileTypes]

    cache_final_rows: Optional[int]

    cache_final_size_bytes: Optional[int]

    cache_max_bytes: Optional[int]

    cache_original_rows: Optional[int]

    cache_original_size_bytes: Optional[int]

    cache_truncated: Optional[bool]

    output_schema: Optional[str]
