# Dynamic proxy for adding DataFrame batch processing to all external endpoints

from __future__ import annotations

import re
from typing import Any, Dict, List, Callable, Optional
from dataclasses import field, dataclass
from concurrent.futures import Future, ThreadPoolExecutor

import polars as pl
from pydantic import BaseModel

from .external import ExternalResource

__all__ = ["ServicesProxy"]


@dataclass
class EndpointConfig:
    """Configuration for how to process API responses into DataFrames"""
    expand_path: Optional[str] = None  # Path to list to expand (e.g., 'organic_results')
    properties: List[str] = field(default_factory=lambda: [])  # Properties to extract (relative to expanded items)


# Configuration for each endpoint - how to transform responses into clean DataFrames
ENDPOINT_CONFIGS = {
    # News endpoints
    'news.top_headlines': EndpointConfig(
        expand_path='articles',
        properties=['title', 'url', 'content', 'publishedAt', 'source.name', 'author']
    ),
    'news.everything': EndpointConfig(
        expand_path='articles',
        properties=['title', 'url', 'content', 'publishedAt', 'source.name', 'author']
    ),
    'news.sources': EndpointConfig(
        expand_path='sources',
        properties=['id', 'name', 'description', 'url', 'category', 'country', 'language']
    ),
    
    # Search API endpoints
    'search_api.google_search': EndpointConfig(
        expand_path='organic_results',
        properties=['link', 'title', 'snippet', 'display_link']
    ),
    'search_api.google_maps_search': EndpointConfig(
        # Direct list response - no expand_path needed
        properties=['name', 'address', 'rating', 'place_id', 'types']
    ),
    'search_api.google_maps_place_details': EndpointConfig(
        properties=['name', 'formatted_address', 'rating', 'user_ratings_total', 'price_level', 'website']
    ),
    'search_api.google_maps_place_reviews': EndpointConfig(
        expand_path='reviews',
        properties=['author_name', 'rating', 'text', 'time', 'relative_time_description']
    ),
    'search_api.google_maps_place_photos': EndpointConfig(
        expand_path='photos',
        properties=['photo_reference', 'height', 'width', 'html_attributions']
    ),
    'search_api.google_flights_search': EndpointConfig(
        expand_path='flights',
        properties=['price', 'departure_time', 'arrival_time', 'airline', 'flight_number', 'duration']
    ),
    'search_api.google_flights_calendar': EndpointConfig(
        expand_path='calendar_results',
        properties=['date', 'price', 'departure_time', 'arrival_time']
    ),
    'search_api.google_flights_location_search': EndpointConfig(
        expand_path='locations',
        properties=['name', 'code', 'city', 'country']
    ),
    'search_api.google_scholar_search': EndpointConfig(
        expand_path='organic_results',
        properties=['title', 'link', 'snippet', 'publication_info', 'citation_count']
    ),
    'search_api.google_scholar_author_search': EndpointConfig(
        expand_path='authors',
        properties=['name', 'affiliation', 'citations', 'h_index', 'i10_index']
    ),
    'search_api.google_scholar_citations': EndpointConfig(
        expand_path='citations',
        properties=['title', 'authors', 'publication', 'year', 'citation_count']
    ),
    'search_api.location_search': EndpointConfig(
        expand_path='locations',
        properties=['name', 'display_name', 'lat', 'lon', 'country', 'state']
    ),
    
    # People endpoints
    'people.people_search': EndpointConfig(
        expand_path='people',
        properties=['name', 'title', 'company', 'location', 'linkedin_url']
    ),
    'people.people_match': EndpointConfig(
        expand_path='matches',
        properties=['name', 'confidence_score', 'linkedin_url', 'company', 'title']
    ),
    'people.companies_search': EndpointConfig(
        expand_path='companies',
        properties=['name', 'domain', 'industry', 'size', 'linkedin_url', 'description']
    ),
    'people.organizations_enrich': EndpointConfig(
        properties=['name', 'domain', 'industry', 'employee_count', 'description', 'linkedin_url']
    ),
    'people.organization_detail': EndpointConfig(
        properties=['name', 'domain', 'industry', 'employee_count', 'description', 'founded']
    ),
    'people.organization_job_postings': EndpointConfig(
        expand_path='job_postings',
        properties=['title', 'company', 'location', 'description', 'posted_date', 'url']
    ),
}


class EndpointProxy:
    """
    Proxy for individual service endpoints (e.g., news, people, search_api).
    
    Intercepts method calls and automatically detects DataFrame inputs,
    processing each row as a parallel API call.
    """
    
    def __init__(self, service: Any):
        self._service = service
        self._client = getattr(service, '_client', None)
    
    def __getattr__(self, name: str) -> Any:
        # Get the original method/attribute
        original_attr = getattr(self._service, name)
        
        # If it's not callable, return as-is
        if not callable(original_attr):
            return original_attr
        
        # If it's a special method, return as-is
        if name.startswith('_') or name in ['with_raw_response', 'with_streaming_response']:
            return original_attr
        
        # Return a wrapped version that supports DataFrame batch processing
        def wrapped_method(*args: Any, **kwargs: Any) -> Any:
            # Check if first argument is a DataFrame
            if args and isinstance(args[0], pl.DataFrame):
                df = args[0]
                return self._batch_process_dataframe(name, df)
            else:
                # Regular method call - delegate to original
                return original_attr(*args, **kwargs)
        
        return wrapped_method
    
    def _batch_process_dataframe(self, method_name: str, df: pl.DataFrame) -> pl.DataFrame:
        """Process DataFrame rows as parallel API calls."""
        THREAD_POOL_SIZE = 20

        if df.is_empty():
            return df.clear()
        
        rows = df.to_dicts()
        
        # Get the original method once
        original_method = getattr(self._service, method_name)
        
        # Execute parallel requests
        with ThreadPoolExecutor(max_workers=THREAD_POOL_SIZE) as executor:
            futures: List[Future[Any]] = []
            for row in rows:
                future = executor.submit(self._execute_single_request, original_method, row)
                futures.append(future)
            
            # Process results using endpoint configuration
            all_results: List[Dict[str, Any]] = []
            for i, future in enumerate(futures):
                try:
                    result = future.result()
                    processed_rows = self._process_response(method_name, result, rows[i])
                    all_results.extend(processed_rows)
                except Exception as e:
                    # Add error row with query context
                    error_row: Dict[str, Any] = {"error": str(e)}
                    error_row.update({f"query_{k}": v for k, v in rows[i].items()})
                    all_results.append(error_row)
        
        return pl.DataFrame(all_results) if all_results else pl.DataFrame()
    
    def _execute_single_request(self, original_method: Callable[..., Any], payload: Dict[str, Any]) -> Any:
        """Execute a single API request."""
        # Call the original method with the payload as keyword arguments
        return original_method(**payload)
    
    def _process_response(self, method_name: str, result: BaseModel, original_query_row: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Process API response using endpoint configuration to create clean DataFrame rows."""
        
        # Build endpoint key (e.g., 'search_api.google_search')
        # Convert class name to resource name by removing 'Resource' suffix and converting to snake_case
        class_name = self._service.__class__.__name__
        resource_name = class_name.replace('Resource', '')
        # Convert from PascalCase to snake_case
        resource_name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', resource_name)
        resource_name = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', resource_name)
        resource_name = resource_name.lower()
        endpoint_key = f"{resource_name}.{method_name}"
        
        # Get configuration for this endpoint
        config = ENDPOINT_CONFIGS.get(endpoint_key, EndpointConfig())
        
        # Convert Pydantic model to dict
        data: Any = result.model_dump()
        
        # Determine what to iterate over
        items: List[Dict[str, Any]]
        if config.expand_path:
            # Extract list from the specified path
            extracted = self._get_by_path(data, config.expand_path)
            if not isinstance(extracted, list):
                raise ValueError(f"Expected list at path '{config.expand_path}', got {type(extracted).__name__}")
            items = extracted  # type: ignore[assignment]
        elif isinstance(data, list):
            # Direct list response
            items = data  # type: ignore[assignment]
        else:
            # Single dict response
            items = [data]
        
        # Extract properties from each item
        processed_rows: List[Dict[str, Any]] = []
        for item in items:
            if config.properties:
                # Extract only specified properties
                row: Dict[str, Any] = {}
                for prop_path in config.properties:
                    value = self._get_by_path(item, prop_path)
                    # Use last part of path as column name (e.g., 'source.name' -> 'name')
                    col_name = prop_path.split('.')[-1]
                    row[col_name] = value
            else:
                # No properties specified - use whole item
                row = item  # type: ignore[assignment]
            
            # Add original query data with 'query_' prefix
            row.update({f"query_{k}": v for k, v in original_query_row.items()})
            processed_rows.append(row)
        
        return processed_rows
    
    def _get_by_path(self, data: Any, path: str) -> Any:
        """Get value from nested dict using dot notation (e.g., 'source.name')."""
        if not path:
            return data
        
        current = data
        for key in path.split('.'):
            if isinstance(current, dict):
                current = current.get(key)  # type: ignore[union-attr]
            else:
                return None
            if current is None:
                return None
        return current  # type: ignore[return-value]
    


class ServicesProxy:
    """
    Proxy for the main ExternalResource that wraps all service endpoints
    with DataFrame batch processing capability.
    """
    
    def __init__(self, client: Any) -> None:
        self._client = client
        self._external_resource = ExternalResource(client)
    
    @property
    def news(self) -> EndpointProxy:
        """News API with DataFrame batch processing."""
        return EndpointProxy(self._external_resource.news)
    
    @property  
    def people(self) -> EndpointProxy:
        """People/Apollo API with DataFrame batch processing."""
        return EndpointProxy(self._external_resource.people)
    
    @property
    def search_api(self) -> EndpointProxy:
        """Search API with DataFrame batch processing.""" 
        return EndpointProxy(self._external_resource.search_api)
    
    def __getattr__(self, name: str) -> Any:
        """Delegate any other attributes to the original external resource."""
        return getattr(self._external_resource, name)