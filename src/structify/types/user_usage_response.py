# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["UserUsageResponse"]

class UserUsageResponse(BaseModel):
    num_entities: int

    num_relationships: int

    num_runs: int