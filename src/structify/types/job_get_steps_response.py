# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .execution_step import ExecutionStep

__all__ = ["JobGetStepsResponse"]

JobGetStepsResponse: TypeAlias = List[ExecutionStep]
