# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .plan_param import PlanParam

__all__ = ["PlanCreateParams"]


class PlanCreateParams(TypedDict, total=False):
    dataset: Required[str]

    plan: Required[PlanParam]
