# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

from .required_entity_param import RequiredEntityParam
from .required_property_param import RequiredPropertyParam
from .required_relationship_param import RequiredRelationshipParam

__all__ = ["ExtractionCriteriaParam"]

ExtractionCriteriaParam = Union[RequiredRelationshipParam, RequiredEntityParam, RequiredPropertyParam]
