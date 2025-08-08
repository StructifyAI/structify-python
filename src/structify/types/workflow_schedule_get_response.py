# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .workflow_schedule_info import WorkflowScheduleInfo

__all__ = ["WorkflowScheduleGetResponse"]

WorkflowScheduleGetResponse: TypeAlias = List[WorkflowScheduleInfo]
