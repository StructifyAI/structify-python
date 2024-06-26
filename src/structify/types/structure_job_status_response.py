# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from typing import List, Union, Optional
from typing_extensions import Literal

from ..types.logger import Log

__all__ = ["StructureJobStatusResponse"]

StructureJobStatusResponse = List[Union[Literal["Running", "Completed", "Failed"], Optional[Log]]]
