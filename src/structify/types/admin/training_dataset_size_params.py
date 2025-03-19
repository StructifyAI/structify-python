# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TrainingDatasetSizeParams"]


class TrainingDatasetSizeParams(TypedDict, total=False):
    dataset_name: Optional[str]

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
