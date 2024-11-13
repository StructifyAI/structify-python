# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TrainingDatasetGetLabellerStatsParams"]


class TrainingDatasetGetLabellerStatsParams(TypedDict, total=False):
    dataset_name: Required[str]

    status: Required[Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"]]

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]