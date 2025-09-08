# External services namespace for Structify Python client

from __future__ import annotations

from typing import List, Optional, Dict, Any
import polars as pl
from concurrent.futures import ThreadPoolExecutor, as_completed

from .whitelabel import WhitelabelResource
from .._base_client import make_request_options

__all__ = ["ExternalResource"]

MAX_PARALLEL_REQUESTS = 20


class ExternalResource(WhitelabelResource):
    """
    Container for all external/whitelabel services.
    
    This provides a namespace for external services that are
    separate from the core Structify functionality.
    """
    
    def search(
        self,
        *,
        df: pl.DataFrame,
        query_column: str = "query",
        num_results: int = 10,
        banned_domains: Optional[List[str]] = None
    ) -> pl.DataFrame:
        """
        Search for information using external search service.
        
        Args:
            df: DataFrame containing search queries
            query_column: Name of the column containing search queries (default: "query")
            num_results: Number of results per query (default: 10)
            banned_domains: Optional list of domains to exclude from results
            
        Returns:
            DataFrame with search results, including a 'query' column to track which search produced each result
        """
        # Extract unique queries from the DataFrame
        queries = df[query_column].unique().to_list()
        
        # Execute searches in parallel
        results = []
        with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
            # Submit all search requests
            future_to_query = {}
            for query in queries:
                if query:  # Skip empty queries
                    future = executor.submit(self._execute_single_search, query, num_results, banned_domains)
                    future_to_query[future] = query
            
            # Collect results as they complete
            for future in as_completed(future_to_query):
                query = future_to_query[future]
                search_results = future.result()
                
                # Add query column to each result
                for result in search_results:
                    result['query'] = query
                    results.append(result)
        
        # Convert to DataFrame
        if results:
            # Define schema for consistent output
            return pl.DataFrame(results, schema={
                "query": pl.Utf8,
                "url": pl.Utf8,
                "title": pl.Utf8,
                "description": pl.Utf8
            })
        else:
            # Return empty DataFrame with correct schema
            return pl.DataFrame(schema={
                "query": pl.Utf8,
                "url": pl.Utf8,
                "title": pl.Utf8,
                "description": pl.Utf8
            })
    
    def _execute_single_search(
        self,
        query: str,
        num_results: int = 10,
        banned_domains: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Execute a single search query and return results."""
        # Make the API call
        response = self._post(
            "/external/search",
            body={"query": query},
            cast_to=object,
            options=make_request_options()
        )
        
        # Response should be a list of search results
        if isinstance(response, list):
            return response
        return []