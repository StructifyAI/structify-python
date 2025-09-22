# External services namespace for Structify Python client

from __future__ import annotations

from typing import List

import polars as pl

from ..._resource import AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..whitelabel import WhitelabelResource, whitelabel_method

__all__ = [
    "ExternalResource",
    "AsyncExternalResource", 
    "ExternalResourceWithRawResponse",
    "AsyncExternalResourceWithRawResponse",
    "ExternalResourceWithStreamingResponse",
    "AsyncExternalResourceWithStreamingResponse",
]


class ExternalResource(WhitelabelResource):
    """
    Container for all external/whitelabel services.

    This provides a namespace for external services that are
    separate from the core Structify functionality.
    """

    @whitelabel_method("/external/search", dataframe_mode=True)
    def search(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Search for information using external search service.

        Args:
            df: DataFrame where each row contains search parameters:
                - query: The search query (required)
                - num_results: Number of results (optional, defaults to 10)
                - banned_domains: List of domains to exclude (optional)

        Returns:
            DataFrame with search results from all queries
        """
        # DataFrame mode automatically processes each row as a parallel API call
        return df

    @whitelabel_method("/external/validate", dataframe_mode=True)
    def validate_emails(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Validate email addresses using external validation service.

        Args:
            df: DataFrame where each row contains validation parameters:
                - email: Email address to validate (required)
                - check_mx: Whether to check MX records (optional, defaults to True)
                - timeout: Request timeout in seconds (optional)

        Returns:
            DataFrame with email validation results
        """
        return df

    @whitelabel_method("/external/enrich", dataframe_mode=True)
    def enrich_companies(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Enrich company information using external enrichment service.

        Args:
            df: DataFrame where each row contains enrichment parameters:
                - company: Company name to enrich (required)
                - data_points: List of data points to retrieve (optional)
                - include_subsidiaries: Include subsidiary data (optional, defaults to False)

        Returns:
            DataFrame with company enrichment results
        """
        return df

    @whitelabel_method("/external/geocode", dataframe_mode=True)
    def geocode_addresses(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Geocode addresses using external geocoding service.

        Args:
            df: DataFrame where each row contains geocoding parameters:
                - address: Address to geocode (required)
                - country: Country code for better accuracy (optional)
                - include_timezone: Include timezone data (optional, defaults to False)

        Returns:
            DataFrame with coordinates and location data
        """
        return df



class AsyncExternalResource(AsyncAPIResource):
    """Async version of ExternalResource."""

    async def search(
        self,
        *,
        df: pl.DataFrame,  # noqa: ARG002
        query_column: str = "query",  # noqa: ARG002
        num_results: int = 10,  # noqa: ARG002
        banned_domains: List[str] | None = None,  # noqa: ARG002
    ) -> pl.DataFrame:
        """
        Search for information using external search service.

        Args:
            df: DataFrame containing search queries
            query_column: Name of the column containing search queries (default: "query")
            num_results: Number of results to return per query (default: 10)
            banned_domains: List of domains to exclude from results (optional)

        Returns:
            DataFrame with search results, including a 'query' column to track which search produced each result
        """
        # For now, return empty results - this would need actual async implementation
        return pl.DataFrame(schema={"query": pl.Utf8, "url": pl.Utf8, "title": pl.Utf8, "description": pl.Utf8})


class ExternalResourceWithRawResponse:
    def __init__(self, external: ExternalResource) -> None:
        self._external = external

        self.search = to_raw_response_wrapper(
            external.search,
        )


class AsyncExternalResourceWithRawResponse:
    def __init__(self, external: AsyncExternalResource) -> None:
        self._external = external

        self.search = async_to_raw_response_wrapper(
            external.search,
        )


class ExternalResourceWithStreamingResponse:
    def __init__(self, external: ExternalResource) -> None:
        self._external = external

        self.search = to_streamed_response_wrapper(
            external.search,
        )


class AsyncExternalResourceWithStreamingResponse:
    def __init__(self, external: AsyncExternalResource) -> None:
        self._external = external

        self.search = async_to_streamed_response_wrapper(
            external.search,
        )
