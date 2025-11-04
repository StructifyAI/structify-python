# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FunctionalTestCreateParams"]


class FunctionalTestCreateParams(TypedDict, total=False):
    team_id: Required[str]

    model_override: Optional[str]

    prompt_override: Optional[str]
