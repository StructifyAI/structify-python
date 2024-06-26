# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Tuple
from typing_extensions import Literal
from ..types.logger import Log
__all__ = ["StructureJobStatusResponse"]

StructureJobStatusResponse = Tuple[List[Literal["Running", "Completed", "Failed"]], Log]
