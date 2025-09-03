# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EntitySummarizeParams"]


class EntitySummarizeParams(TypedDict, total=False):
    dataset: Required[str]

    entity_id: Required[str]

    properties: Required[SequenceNotStr[str]]

    extra_instructions: Optional[SequenceNotStr[str]]
    """A list of instructions for each property to guide the summarization process"""
