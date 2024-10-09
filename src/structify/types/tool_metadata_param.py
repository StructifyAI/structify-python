# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolMetadataParam"]


class ToolMetadataParam(TypedDict, total=False):
    description: Required[str]

    name: Required[Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]]

    regex_validator: Required[str]

    tool_validator: Required[Dict[str, object]]
