# DataFrame batch processing for external endpoints

from __future__ import annotations

from typing import Any, Dict, List, Optional, cast
from concurrent.futures import ThreadPoolExecutor

import polars as pl

from .._resource import SyncAPIResource
from .._compat import cached_property
from .._base_client import make_request_options

__all__ = ["PolarsExternalResource"]


class PolarsExternalResource(SyncAPIResource):
    """
    DataFrame-based batch processing for external API endpoints.
    
    Each method takes a Polars DataFrame where each row becomes a parallel API call.
    Results are returned as a DataFrame with responses from all calls.
    """
    
    def _batch_process(self, endpoint: str, df: pl.DataFrame, method: str = "POST") -> pl.DataFrame:
        """
        Process DataFrame rows as parallel API calls.
        
        Args:
            endpoint: API endpoint to call
            df: DataFrame where each row is a request
            method: HTTP method (GET or POST)
            
        Returns:
            DataFrame with results from all API calls
        """
        if df.is_empty():
            return df.clear()
            
        rows = df.to_dicts()
        
        # Execute parallel requests
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = []
            for row in rows:
                future = executor.submit(self._execute_single_request, endpoint, row, method)
                futures.append(future)
            
            results = []
            for future in futures:
                try:
                    result = future.result()
                    if isinstance(result, dict):
                        results.append(result)
                    elif isinstance(result, list) and len(result) > 0:
                        # If API returns a list, take first item or flatten as needed
                        results.extend(result if isinstance(result[0], dict) else [{"result": result}])
                    else:
                        results.append({"result": result})
                except Exception as e:
                    results.append({"error": str(e)})
        
        return pl.DataFrame(results) if results else pl.DataFrame()
    
    def _execute_single_request(self, endpoint: str, payload: Dict[str, Any], method: str) -> Any:
        """Execute a single API request."""
        if method.upper() == "GET":
            return self._get(
                endpoint, 
                cast_to=object, 
                options=make_request_options(extra_query=cast(Dict[str, object], payload))
            )
        elif method.upper() == "POST":
            return self._post(
                endpoint, 
                body=payload, 
                cast_to=object, 
                options=make_request_options()
            )
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
    
    # Google Search API endpoints
    def google_search(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Search Google with multiple queries in parallel.
        
        Expected DataFrame columns:
        - query: Search query (required)
        - num_results: Number of results (optional)
        - country: Country code (optional)
        - language: Language code (optional)
        
        Returns:
            DataFrame with search results
        """
        return self._batch_process("/external/search-api/google-search", df, "POST")
    
    def google_maps_search(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Search Google Maps with multiple queries in parallel.
        
        Expected DataFrame columns:
        - query: Search query (required)
        - location: Location to search around (optional)
        - radius: Search radius (optional)
        
        Returns:
            DataFrame with map search results
        """
        return self._batch_process("/external/search-api/google-maps/search", df, "POST")
    
    def google_maps_place_details(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Get Google Maps place details for multiple places in parallel.
        
        Expected DataFrame columns:
        - place_id: Google Maps place ID (required)
        
        Returns:
            DataFrame with place details
        """
        return self._batch_process("/external/search-api/google-maps/place-details", df, "GET")
    
    def google_scholar_search(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Search Google Scholar with multiple queries in parallel.
        
        Expected DataFrame columns:
        - query: Search query (required)
        - num_results: Number of results (optional)
        - year_from: Start year filter (optional)
        - year_to: End year filter (optional)
        
        Returns:
            DataFrame with scholar search results
        """
        return self._batch_process("/external/search-api/google-scholar/search", df, "POST")
    
    # News API endpoints  
    def news_everything(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Search news articles with multiple queries in parallel.
        
        Expected DataFrame columns:
        - q: Search query (required)
        - sources: News sources (optional)
        - domains: Domains to search (optional)
        - from_date: Start date (optional)
        - to_date: End date (optional)
        
        Returns:
            DataFrame with news articles
        """
        return self._batch_process("/external/news/everything", df, "POST")
    
    def news_top_headlines(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Get top headlines with multiple queries/categories in parallel.
        
        Expected DataFrame columns:
        - q: Search query (optional)
        - category: News category (optional)
        - country: Country code (optional)
        - sources: News sources (optional)
        
        Returns:
            DataFrame with top headlines
        """
        return self._batch_process("/external/news/top-headlines", df, "POST")
    
    # Apollo/People API endpoints
    def people_search(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Search for people with multiple queries in parallel.
        
        Expected DataFrame columns:
        - q: Search query (required)
        - person_titles: Job titles (optional)
        - person_locations: Locations (optional)
        - organization_names: Organization names (optional)
        
        Returns:
            DataFrame with people search results
        """
        return self._batch_process("/external/people/people-search", df, "POST")
    
    def companies_search(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Search for companies with multiple queries in parallel.
        
        Expected DataFrame columns:
        - q: Search query (required)
        - organization_locations: Company locations (optional)
        - organization_num_employees_ranges: Employee count ranges (optional)
        
        Returns:
            DataFrame with company search results
        """
        return self._batch_process("/external/people/companies-search", df, "POST")
    
    def organizations_enrich(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Enrich organization data for multiple organizations in parallel.
        
        Expected DataFrame columns:
        - domain: Organization domain (required)
        
        Returns:
            DataFrame with enriched organization data
        """
        return self._batch_process("/external/people/organizations-enrich", df, "GET")
    
    def people_match(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Match people data for multiple people in parallel.
        
        Expected DataFrame columns:
        - first_name: First name (required)
        - last_name: Last name (required)
        - organization_name: Organization name (optional)
        - email: Email address (optional)
        
        Returns:
            DataFrame with people match results
        """
        return self._batch_process("/external/people/people-match", df, "POST")