# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .entity import Entity

__all__ = ["DatasetViewResponse", "DatasetViewResponseItem"]


class DatasetViewResponseItem(Entity):
    from_id: int

    label: str

    to_id: int


DatasetViewResponse = List[List[DatasetViewResponseItem]]
