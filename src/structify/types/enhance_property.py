# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .web import Web

__all__ = ["EnhanceProperty"]


class EnhanceProperty(Web):
    entity_id: str

    property_name: str

    allow_extra_entities: Optional[bool] = None
