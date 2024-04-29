# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceListSourcesParams"]


class SourceListSourcesParams(TypedDict, total=False):
    id: Required[int]
    """Id of the entity to get sources for"""
