# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["WikiCreateParams"]


class WikiCreateParams(TypedDict, total=False):
    content: Required[Dict[str, object]]

    slug: Required[str]

    title: Required[str]
