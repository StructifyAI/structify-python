# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .onboarding_answers import OnboardingAnswers

__all__ = ["GetOnboardingAnswersResponse"]


class GetOnboardingAnswersResponse(BaseModel):
    answers: OnboardingAnswers
