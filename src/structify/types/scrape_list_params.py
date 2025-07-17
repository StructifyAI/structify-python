# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .dataset_descriptor_param import DatasetDescriptorParam

__all__ = ["ScrapeListParams", "StopConfig"]


class ScrapeListParams(TypedDict, total=False):
    dataset_descriptor: Required[DatasetDescriptorParam]
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    table_name: Required[str]

    url: Required[str]

    node_id: Optional[str]

    stop_config: Optional[StopConfig]
    """Configuration parameters for the StopChecker"""


class StopConfig(TypedDict, total=False):
    max_steps_without_save: Required[int]

    max_errors: Optional[int]

    max_execution_time_secs: Optional[int]

    max_total_steps: Optional[int]
