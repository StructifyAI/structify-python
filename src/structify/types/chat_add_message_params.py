# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChatAddMessageParams"]


class ChatAddMessageParams(TypedDict, total=False):
    content: Required[str]

    role: Required[str]
