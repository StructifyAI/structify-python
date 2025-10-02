# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkflowRunParams"]


class WorkflowRunParams(TypedDict, total=False):
    chat_session_id: Required[str]

    use_node_cache: Required[bool]
