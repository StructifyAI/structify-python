# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionCreateNodeParams"]


class SessionCreateNodeParams(TypedDict, total=False):
    code_md5_hash: Required[str]

    docstring: Required[str]

    function_name: Required[str]

    output_schema: object
