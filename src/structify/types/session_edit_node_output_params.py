# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .cell_edit_param import CellEditParam

__all__ = ["SessionEditNodeOutputParams"]


class SessionEditNodeOutputParams(TypedDict, total=False):
    edits: Required[Iterable[CellEditParam]]
