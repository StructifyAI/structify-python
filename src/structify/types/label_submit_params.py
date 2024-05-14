# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LabelSubmitParams"]


class LabelSubmitParams(TypedDict, total=False):
    _text: Required[str]

    uuid: Required[str]
