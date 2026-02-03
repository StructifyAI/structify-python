# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .cell_edit_param import CellEditParam

__all__ = ["ParquetEditParam", "EditCell", "DeleteRow", "AddRow"]


class EditCell(CellEditParam, total=False):
    type: Required[Literal["edit_cell"]]


class DeleteRow(TypedDict, total=False):
    row_index: Required[int]

    type: Required[Literal["delete_row"]]


class AddRow(TypedDict, total=False):
    type: Required[Literal["add_row"]]

    values: Required[Dict[str, str]]


ParquetEditParam: TypeAlias = Union[EditCell, DeleteRow, AddRow]
