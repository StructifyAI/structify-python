# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChatCreateSessionParams"]


class ChatCreateSessionParams(TypedDict, total=False):
    git_branch: Required[str]

    git_commit_hash: Required[str]

    git_repo_id: Required[str]

    initial_message: Required[str]

    project_id: Required[str]
