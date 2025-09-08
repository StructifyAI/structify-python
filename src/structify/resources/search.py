# Search service resource for Structify Python client

from __future__ import annotations

from typing import List, Optional, Dict, Any

from .whitelabel import WhitelabelResource, whitelabel_method
from ..types.search_types import SearchResult, SearchRequest, SearchResponse

__all__ = ["SearchResource"]


class SearchResource(WhitelabelResource):
    """
    Resource for web search functionality.
    
    This provides access to the external search API endpoint that leverages
    existing search providers (Brave, SearchAPI, BrightData) configured on the backend.
    """
    
    @whitelabel_method("/external/search", method="POST")
    def search(
        self, 
        query: str, 
        num_results: int = 10,
        banned_domains: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Perform a web search using the configured search provider.
        
        Args:
            query: The search query string
            num_results: Maximum number of results to return (default: 10)
            banned_domains: Optional list of domains to exclude from results
            
        Returns:
            Dict with results, query, and count keys for compatibility
            
        Example:
            >>> client = Structify(api_key="...")
            >>> results = client.search.search("AI companies", num_results=5)
            >>> for result in results["results"]:
            ...     print(f"{result['title']}: {result['url']}")
        """
        request_data = {"query": query}
        
        # Note: The current API doesn't support num_results or banned_domains
        # but we keep the interface for future compatibility
        
        return request_data
    
    def _post_process_search(self, response, query: str):
        """Post-process the search response."""
        if isinstance(response, list):
            # API returned list directly, format it
            return {
                "results": response,
                "query": query,
                "count": len(response)
            }
        return response
        
    def _post_process_search_results_only(self, response, query: str):
        """Post-process for search_results_only - return list directly."""
        if isinstance(response, list):
            return response
        return response
    
    @whitelabel_method("/external/search", method="POST")
    def search_results_only(
        self,
        query: str,
        num_results: int = 10,
        banned_domains: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Perform a web search and return only the results list.
        
        This is a convenience method that extracts just the results array
        from the search response.
        
        Args:
            query: The search query string
            num_results: Maximum number of results to return (default: 10)
            banned_domains: Optional list of domains to exclude from results
            
        Returns:
            List of SearchResult objects
            
        Example:
            >>> client = Structify(api_key="...")
            >>> results = client.search.search_results_only("machine learning")
            >>> for result in results:
            ...     print(result["url"])
        """
        request_data = {"query": query}
        return request_data
    
    def search_multiple(
        self,
        queries: List[str],
        num_results_per_query: int = 10,
        banned_domains: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Perform multiple searches and aggregate the results.
        
        This method makes multiple API calls and combines the results,
        automatically deduplicating based on URL.
        
        Args:
            queries: List of search query strings
            num_results_per_query: Max results per individual query
            banned_domains: Optional list of domains to exclude
            
        Returns:
            List of unique SearchResult objects across all queries
            
        Example:
            >>> client = Structify(api_key="...")
            >>> results = client.search.search_multiple([
            ...     "AI startups",
            ...     "machine learning companies",
            ...     "deep learning research"
            ... ])
        """
        all_results = []
        seen_urls = set()
        
        for query in queries:
            # Use search_results_only to get the list directly
            results = self.search_results_only(query, num_results_per_query, banned_domains)
            
            for result in results:
                if result["url"] not in seen_urls:
                    seen_urls.add(result["url"])
                    all_results.append(result)
        
        return all_results