# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DatasetReorderPropertiesParams"]


class DatasetReorderPropertiesParams(TypedDict, total=False):
    dataset_name: Required[str]

    property_names: Required[SequenceNotStr[str]]

    table_name: Required[str]
