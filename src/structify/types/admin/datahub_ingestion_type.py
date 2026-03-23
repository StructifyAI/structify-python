# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["DatahubIngestionType"]

DatahubIngestionType: TypeAlias = Literal["postgres", "snowflake", "salesforce", "hubspot", "bigquery"]
