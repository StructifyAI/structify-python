# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TrainingDatasetListDatumsParams"]


class TrainingDatasetListDatumsParams(TypedDict, total=False):
    dataset_name: Required[str]

    last_updated: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
