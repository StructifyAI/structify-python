# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReportStepParams"]


class ReportStepParams(TypedDict, total=False):
    step_id: Required[str]

    message: Optional[str]
    """A short message about why the step is being reported"""
