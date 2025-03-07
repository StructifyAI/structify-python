# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MergeConfigParam"]


class MergeConfigParam(TypedDict, total=False):
    baseline_cardinality: Required[int]
    """
    The number of unique values that are expected to be present in the complete
    dataset

    This is used for merging to determine how significant a match is. (i.e. if there
    are only 2 possible values, a match gives less confidence than if there are 100)
    """

    match_transfer_probability: Required[float]
    """The estimated probability that, given an entity match, the properties also match

    For a person's full name, this would be quite high. For a person's job title, it
    would be lower because people can have multiple job titles over time or at
    different companies at the same time.
    """

    comparison_strategy: Literal["Default", "EnforceUniqueness"]
