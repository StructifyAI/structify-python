# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["OnboardingAnswersParam"]


class OnboardingAnswersParam(TypedDict, total=False):
    company_name: Optional[str]

    connected_connector_ids: Optional[SequenceNotStr[str]]

    full_name: Optional[str]

    primary_goal: Optional[str]

    recommended_template_id: Optional[str]

    role: Optional[str]

    systems_to_connect: Optional[SequenceNotStr[str]]
