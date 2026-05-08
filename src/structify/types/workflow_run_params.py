# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WorkflowRunParams"]


class WorkflowRunParams(TypedDict, total=False):
    chat_session_id: Required[str]

    use_node_cache: Required[bool]

    edited_node_name: Optional[str]

    rerun_from: SequenceNotStr[str]
    """Function names of nodes to force-rerun.

    Those nodes are excluded from cache resolution so they re-execute fresh; their
    ancestors cache-resolve.
    """

    skip_children: bool
    """
    When true, descendants of the `rerun_from` nodes are marked Skipped instead of
    executing. Use this to run a subset of the DAG.
    """
