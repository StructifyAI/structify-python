# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SandboxCreateParams"]


class SandboxCreateParams(TypedDict, total=False):
    chat_session_id: Required[str]

    modal_id: Required[str]

    modal_url: Required[str]

    status: Required[Literal["alive", "terminated"]]

    latest_node: Optional[str]
