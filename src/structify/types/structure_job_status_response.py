# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

__all__ = ["StructureJobStatusResponse"]

StructureJobStatusResponse: TypeAlias = List[Literal["Queued", "Running", "Completed", "Failed"]]
