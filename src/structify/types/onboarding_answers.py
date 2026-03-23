# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OnboardingAnswers"]


class OnboardingAnswers(BaseModel):
    company_name: Optional[str] = None

    connected_connector_ids: Optional[List[str]] = None

    full_name: Optional[str] = None

    primary_goal: Optional[str] = None

    recommended_template_id: Optional[str] = None

    role: Optional[str] = None

    systems_to_connect: Optional[List[str]] = None
