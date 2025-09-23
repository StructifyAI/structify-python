# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChatRevertToCommitParams"]


class ChatRevertToCommitParams(TypedDict, total=False):
    commit_hash: Required[str]
    """The git commit hash to revert to (must be 40 characters)"""
