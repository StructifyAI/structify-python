# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolMetadataParam"]


class ToolMetadataParam(TypedDict, total=False):
    description: Required[str]

    name: Required[
        Literal["Exit", "Save", "Wait", "Type", "Scroll", "ScrollToBottom", "Click", "Hover", "Error", "Google"]
    ]

    regex_validator: Required[str]
