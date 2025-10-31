# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .project_visibility import ProjectVisibility

__all__ = ["Project"]


class Project(BaseModel):
    id: str

    created_at: datetime

    name: str

    team_id: str

    updated_at: datetime

    visibility: ProjectVisibility

    description: Optional[str] = None
