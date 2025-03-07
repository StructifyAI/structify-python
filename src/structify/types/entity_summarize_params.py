# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EntitySummarizeParams"]


class EntitySummarizeParams(TypedDict, total=False):
    dataset_name: Required[str]

    entity_id: Required[str]

    properties: Required[List[str]]

    extra_instructions: Optional[List[str]]
    """A list of instructions for each property to guide the summarization process"""
