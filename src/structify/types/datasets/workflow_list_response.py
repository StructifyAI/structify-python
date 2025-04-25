# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .id import ID
from .workflow import Workflow

__all__ = ["WorkflowListResponse", "WorkflowListResponseItem"]


class WorkflowListResponseItem(Workflow):
    id: ID


WorkflowListResponse: TypeAlias = List[WorkflowListResponseItem]
