# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HumanLlmAddSearchForJobParams"]


class HumanLlmAddSearchForJobParams(TypedDict, total=False):
    job_id: Required[str]

    search_term: Required[str]
