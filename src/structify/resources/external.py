# External services namespace for Structify Python client

from __future__ import annotations

from typing import List, Optional, Dict, Any
from .whitelabel import WhitelabelResource, whitelabel_method

__all__ = ["ExternalResource"]


class ExternalResource(WhitelabelResource):
    """
    Container for all external/whitelabel services.
    
    This provides a namespace for external services that are
    separate from the core Structify functionality.
    """
    
    @whitelabel_method("/external/search", method="POST")
    def search(
        self,
        *,
        queries: List[str],
        num_results: int = 10,
        banned_domains: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Search for information using external search service.
        
        Args:
            queries: List of search queries to execute
            num_results: Number of results per query (default: 10)
            banned_domains: Optional list of domains to exclude from results
            
        Returns:
            Dictionary with deduplicated search results
        """
        # Send only the first query to the endpoint (which expects a single query)
        # In the future, this could be enhanced to batch multiple queries
        return {"query": queries[0] if queries else ""}
    
    def _post_process_search(self, response: Any, queries: List[str]) -> Dict[str, Any]:
        """Post-process search response."""
        if isinstance(response, list):
            # Deduplicate by URL
            seen_urls = set()
            unique_results = []
            for result in response:
                url = result.get('url', '')
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    unique_results.append(result)
            
            return {
                "queries": queries,
                "results": unique_results,
                "count": len(unique_results)
            }
        return response