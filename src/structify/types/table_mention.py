# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TableMention"]


class TableMention(BaseModel):
    id: str

    column_names: List[str]

    database_name: str

    name: str

    schema_name: str

    description: Optional[str] = None
