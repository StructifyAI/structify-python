# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .project import Project
from .project_member import ProjectMember

__all__ = ["ProjectGetResponse"]


class ProjectGetResponse(Project):
    members: List[ProjectMember]
