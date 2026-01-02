"""Cost confirmation utilities for workflow execution.

This module provides helpers to request user confirmation before executing
costly operations (web scraping, PDF extraction, etc.) when running within
a workflow context.
"""

from __future__ import annotations

import os
import time
from typing import Any

CONFIRMATION_TIMEOUT_SECONDS = 3600
CONFIRMATION_POLL_INTERVAL_SECONDS = 0.5


def request_cost_confirmation_if_needed(client: Any, row_count: int) -> bool:
    """Request cost confirmation if running in workflow context with confirmation enabled.

    When STRUCTIFY_REQUIRES_CONFIRMATION=true and STRUCTIFY_NODE_ID is set,
    this function requests user confirmation before proceeding with costly
    operations like web scraping or PDF extraction.

    Args:
        client: The Structify client instance
        row_count: Number of rows to be processed (used for cost estimation)

    Returns:
        True if confirmed, confirmation not required, or not in workflow context.
        False if user rejected the operation.

    Raises:
        TimeoutError: If confirmation times out after CONFIRMATION_TIMEOUT_SECONDS
    """
    if os.environ.get("STRUCTIFY_REQUIRES_CONFIRMATION", "").lower() != "true":
        return True

    node_id = os.environ.get("STRUCTIFY_NODE_ID")
    if not node_id:
        return True

    if row_count <= 0:
        return True

    client.sessions.request_confirmation(node_id=node_id, row_count=row_count)

    start_time = time.time()
    while time.time() - start_time < CONFIRMATION_TIMEOUT_SECONDS:
        time.sleep(CONFIRMATION_POLL_INTERVAL_SECONDS)
        node = client.sessions.get_node(node_id=node_id).node

        if node.confirmation_status == "confirmed":
            return True
        if node.confirmation_status == "rejected":
            return False

    raise TimeoutError(f"Timeout waiting for cost confirmation for node {node_id}")
