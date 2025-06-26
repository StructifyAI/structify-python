# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["UserSurveySubmitParams"]


class UserSurveySubmitParams(TypedDict, total=False):
    survey_response: Required[Dict[str, object]]
