# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .project_visibility import ProjectVisibility
from .project_collaborator_input_param import ProjectCollaboratorInputParam

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    team_id: Required[str]

    collaborators: Optional[Iterable[ProjectCollaboratorInputParam]]

    description: Optional[str]

    name: Optional[str]

    visibility: Optional[ProjectVisibility]
