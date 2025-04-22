# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetSetPrimaryColumnParams"]


class DatasetSetPrimaryColumnParams(TypedDict, total=False):
    dataset_name: Required[str]

    property_name: Required[str]

    table_name: Required[str]
