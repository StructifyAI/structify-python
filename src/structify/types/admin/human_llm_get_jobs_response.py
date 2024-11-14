# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .human_llm_job import HumanLlmJob

__all__ = ["HumanLlmGetJobsResponse"]

HumanLlmGetJobsResponse: TypeAlias = List[HumanLlmJob]
