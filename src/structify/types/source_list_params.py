# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["SourceListParams"]

class SourceListParams(TypedDict, total=False):
    id: Required[str]
    """Entity ID to get sources for"""

    property: Optional[str]
    """Optional property name to filter sources by"""