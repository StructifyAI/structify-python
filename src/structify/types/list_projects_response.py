# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .project import Project
from .._models import BaseModel

__all__ = ["ListProjectsResponse"]


class ListProjectsResponse(BaseModel):
    projects: List[Project]
