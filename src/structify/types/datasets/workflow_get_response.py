# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .id import ID
from .workflow import Workflow

__all__ = ["WorkflowGetResponse"]


class WorkflowGetResponse(Workflow):
    id: ID
