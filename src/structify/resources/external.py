# External services namespace for Structify Python client

from __future__ import annotations

from typing import Any, Dict, List, cast

import polars as pl

from .whitelabel import WhitelabelResource, whitelabel_method
from .._compat import cached_property
from .._resource import AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)

__all__ = [
    "ExternalResource",
    "AsyncExternalResource", 
    "ExternalResourceWithRawResponse",
    "AsyncExternalResourceWithRawResponse",
    "ExternalResourceWithStreamingResponse", 
    "AsyncExternalResourceWithStreamingResponse"
]


class ExternalResource(WhitelabelResource):
    """
    Container for all external/whitelabel services.

    This provides a namespace for external services that are
    separate from the core Structify functionality.
    """

    @whitelabel_method("/external/search")
    def search(
        self,
        *,
        df: pl.DataFrame,
        query_column: str = "query",
        num_results: int = 10,
        banned_domains: List[str] | None = None,
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
        # Extract unique queries from the DataFrame
        queries = df[query_column].unique().to_list()

        # Return the parameters for the whitelabel decorator to process
        return {"queries": queries, "num_results": num_results, "banned_domains": banned_domains or []}  # type: ignore[return-value]

    def _post_process_search(self, response: Any, queries: List[str]) -> pl.DataFrame:  # noqa: ARG002
        """Post-process search results into DataFrame format."""
        results: List[Dict[str, Any]] = []

        if isinstance(response, list):
            # If response is already a list, it's the processed results
            results = cast(List[Dict[str, Any]], response)
        elif isinstance(response, dict) and "results" in response:
            # If response is wrapped in a results key
            results = cast(List[Dict[str, Any]], response["results"])

        # Convert to DataFrame with proper schema
        if results:
            return pl.DataFrame(
                results, schema={"query": pl.Utf8, "url": pl.Utf8, "title": pl.Utf8, "description": pl.Utf8}
            )
        else:
            return pl.DataFrame(schema={"query": pl.Utf8, "url": pl.Utf8, "title": pl.Utf8, "description": pl.Utf8})


class AsyncExternalResource(AsyncAPIResource):
    """
    Async container for all external/whitelabel services.
    
    This provides a namespace for external services that are
    separate from the core Structify functionality.
    """

    @cached_property
    def with_raw_response(self) -> AsyncExternalResourceWithRawResponse:
        return AsyncExternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalResourceWithStreamingResponse:
        return AsyncExternalResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        df: pl.DataFrame,
        query_column: str = "query",
        num_results: int = 10,
        banned_domains: List[str] | None = None,
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
        # Extract unique queries from the DataFrame
        queries = df[query_column].unique().to_list()

        # Prepare payload
        payload = {"queries": queries, "num_results": num_results, "banned_domains": banned_domains or []}
        
        # Make the API call
        response = await self._post(
            "/external/search",
            body=payload,
            cast_to=object,
        )

        # Post-process the response
        return self._post_process_search(response, queries)

    def _post_process_search(self, response: Any, queries: List[str]) -> pl.DataFrame:  # noqa: ARG002
        """Post-process search results into DataFrame format."""
        results: List[Dict[str, Any]] = []

        if isinstance(response, list):
            # If response is already a list, it's the processed results
            results = cast(List[Dict[str, Any]], response)
        elif isinstance(response, dict) and "results" in response:
            # If response is wrapped in a results key
            results = cast(List[Dict[str, Any]], response["results"])

        # Convert to DataFrame with proper schema
        if results:
            return pl.DataFrame(
                results, schema={"query": pl.Utf8, "url": pl.Utf8, "title": pl.Utf8, "description": pl.Utf8}
            )
        else:
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
