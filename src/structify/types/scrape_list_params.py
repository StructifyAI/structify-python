# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .dataset_descriptor_param import DatasetDescriptorParam

__all__ = ["ScrapeListParams"]


class ScrapeListParams(TypedDict, total=False):
    dataset_descriptor: Required[DatasetDescriptorParam]
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    table_name: Required[str]

    url: Required[str]
