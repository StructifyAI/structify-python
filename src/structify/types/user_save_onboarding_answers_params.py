# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .onboarding_answers_param import OnboardingAnswersParam

__all__ = ["UserSaveOnboardingAnswersParams"]


class UserSaveOnboardingAnswersParams(TypedDict, total=False):
    answers: Required[OnboardingAnswersParam]
