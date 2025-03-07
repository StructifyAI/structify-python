# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required

from .web_param import WebParam

__all__ = ["EnhancePropertyParam"]


class EnhancePropertyParam(WebParam):
    entity_id: Required[str]

    property_name: Required[str]

    allow_extra_entities: bool
