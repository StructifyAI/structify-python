# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .required_entity import RequiredEntity
from .required_property import RequiredProperty
from .required_relationship import RequiredRelationship

__all__ = ["ExtractionCriteria"]

ExtractionCriteria = Union[RequiredRelationship, RequiredEntity, RequiredProperty]
