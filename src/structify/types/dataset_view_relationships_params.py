# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["DatasetViewRelationshipsParams"]

class DatasetViewRelationshipsParams(TypedDict, total=False):
    dataset: Required[str]

    name: Required[str]

    limit: int

    offset: int