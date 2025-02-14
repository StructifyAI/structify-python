# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetEvaluateParams"]


class DatasetEvaluateParams(TypedDict, total=False):
    dataset_1: Required[str]

    dataset_2: Required[str]

    email_1: Required[str]

    email_2: Required[str]
