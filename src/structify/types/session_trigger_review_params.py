# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .dead_code_finding_param import DeadCodeFindingParam

__all__ = ["SessionTriggerReviewParams"]


class SessionTriggerReviewParams(TypedDict, total=False):
    dead_code_findings: Iterable[DeadCodeFindingParam]
    """Symbols vulture flagged as unreached from `workflow()`.

    Empty when the workflow is clean.
    """
