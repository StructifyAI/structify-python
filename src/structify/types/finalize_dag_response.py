# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["FinalizeDagResponse", "UnchangedNode"]


class UnchangedNode(BaseModel):
    cached_from_node_id: str

    node_id: str


class FinalizeDagResponse(BaseModel):
    node_ids: List[str]

    skipped_nodes: List[str]
    """
    Nodes marked Skipped during finalize because they are descendants of a
    `rerun_from` node and the caller set `skip_children = true`.
    """

    unchanged_nodes: List[UnchangedNode]
    """
    Nodes that were cache-resolved during finalize and are already marked Success.
    The Python runtime skips execution for these instead of making per-node cache
    calls.
    """
