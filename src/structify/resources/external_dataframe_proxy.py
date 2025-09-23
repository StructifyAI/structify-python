# Dynamic proxy for adding DataFrame batch processing to all external endpoints

from __future__ import annotations

from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor

try:
    import polars as pl
except ImportError:
    pl = None  # type: ignore[assignment]

from .._base_client import make_request_options
from .external import ExternalResource

__all__ = ["ExternalResourceProxy"]


@dataclass
class EndpointConfig:
    """Configuration for how to process API responses into DataFrames"""
    expand_path: Optional[str] = None  # Path to list to expand (e.g., 'organic_results')
    properties: List[str] = field(default_factory=list)  # Properties to extract (relative to expanded items)


# Configuration for each endpoint - how to transform responses into clean DataFrames
ENDPOINT_CONFIGS = {
    'search_api.google_search': EndpointConfig(
        expand_path='organic_results',
        properties=['link', 'title', 'snippet', 'display_link']
    ),
    'search_api.google_maps_search': EndpointConfig(
        # Direct list response - no expand_path needed
        properties=['name', 'address', 'rating', 'place_id', 'types']
    ),
    'search_api.google_scholar_search': EndpointConfig(
        expand_path='organic_results',
        properties=['title', 'link', 'snippet', 'publication_info']
    ),
    'news.everything': EndpointConfig(
        expand_path='articles',
        properties=['title', 'url', 'content', 'publishedAt', 'source.name', 'author']
    ),
    'news.sources': EndpointConfig(
        expand_path='sources',
        properties=['id', 'name', 'description', 'url', 'category', 'country', 'language']
    ),
    'news.top_headlines': EndpointConfig(
        expand_path='articles',
        properties=['title', 'url', 'content', 'publishedAt', 'source.name', 'author']
    ),
    'people.search': EndpointConfig(
        expand_path='people',
        properties=['name', 'title', 'company', 'location', 'linkedin_url']
    ),
    'people.enrich': EndpointConfig(
        # Single person response - no expand_path
        properties=['name', 'title', 'company', 'emails', 'phone_numbers', 'linkedin_url']
    ),
}


class DataFrameBatchProxy:
    """
    Dynamic proxy that adds DataFrame batch processing to any resource object.
    
    Intercepts all method calls and automatically detects DataFrame inputs,
    processing each row as a parallel API call.
    """
    
    def __init__(self, resource: Any):
        self._resource = resource
        self._client = getattr(resource, '_client', None)
    
    def __getattr__(self, name: str) -> Any:
        # Get the original method/attribute
        original_attr = getattr(self._resource, name)
        
        # If it's not callable, return as-is
        if not callable(original_attr):
            return original_attr
        
        # If it's a special method, return as-is
        if name.startswith('_') or name in ['with_raw_response', 'with_streaming_response']:
            return original_attr
        
        # Return a wrapped version that supports DataFrame batch processing
        def wrapped_method(*args, **kwargs):
            # Check if first argument is a DataFrame
            if args and pl is not None and hasattr(args[0], '__class__') and args[0].__class__.__name__ == 'DataFrame':
                df = args[0]
                return self._batch_process_dataframe(name, df)
            else:
                # Regular method call - delegate to original
                return original_attr(*args, **kwargs)
        
        return wrapped_method
    
    def _batch_process_dataframe(self, method_name: str, df: pl.DataFrame) -> pl.DataFrame:
        """Process DataFrame rows as parallel API calls."""
        if df.is_empty():
            return df.clear()
        
        rows = df.to_dicts()
        
        # Get the original method once
        original_method = getattr(self._resource, method_name)
        
        # Execute parallel requests
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = []
            for row in rows:
                future = executor.submit(self._execute_single_request, original_method, row)
                futures.append(future)
            
            # Process results using endpoint configuration
            all_results = []
            for i, future in enumerate(futures):
                try:
                    result = future.result()
                    processed_rows = self._process_response(method_name, result, rows[i])
                    all_results.extend(processed_rows)
                except Exception as e:
                    # Add error row with query context
                    error_row = {"error": str(e)}
                    error_row.update({f"query_{k}": v for k, v in rows[i].items()})
                    all_results.append(error_row)
        
        return pl.DataFrame(all_results) if all_results else pl.DataFrame()
    
    def _execute_single_request(self, original_method, payload: Dict[str, Any]) -> Any:
        """Execute a single API request."""
        # Call the original method with the payload as keyword arguments
        return original_method(**payload)
    
    def _process_response(self, method_name: str, result: Any, original_query_row: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Process API response using endpoint configuration to create clean DataFrame rows."""
        
        # Build endpoint key (e.g., 'search_api.google_search')
        # Convert class name like 'SearchAPIResource' to 'search_api'
        class_name = self._resource.__class__.__name__
        # Handle special case of 'API' in the name
        if 'API' in class_name:
            resource_name = class_name.replace('APIResource', '_api').replace('API', '_api')
        else:
            resource_name = class_name.replace('Resource', '')
        
        # Convert to lowercase and clean up
        resource_name = resource_name.lower().replace('__', '_').strip('_')
        endpoint_key = f"{resource_name}.{method_name}"
        
        # Get configuration for this endpoint
        config = ENDPOINT_CONFIGS.get(endpoint_key, EndpointConfig())
        
        # Convert Pydantic model to dict if needed
        if hasattr(result, 'model_dump'):
            data = result.model_dump()
        else:
            data = result
        
        # Determine what to iterate over
        if config.expand_path:
            # Extract list from the specified path
            items = self._get_by_path(data, config.expand_path)
            if not isinstance(items, list):
                items = [items] if items else []
        elif isinstance(data, list):
            # Direct list response
            items = data
        else:
            # Single dict response
            items = [data]
        
        # Extract properties from each item
        processed_rows = []
        for item in items:
            if not isinstance(item, dict):
                # Handle non-dict items
                row = {"result": item}
            elif config.properties:
                # Extract only specified properties
                row = {}
                for prop_path in config.properties:
                    value = self._get_by_path(item, prop_path)
                    # Use last part of path as column name (e.g., 'source.name' -> 'name')
                    col_name = prop_path.split('.')[-1]
                    row[col_name] = value
            else:
                # No properties specified - use whole item
                row = item
            
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
                current = current.get(key)
            else:
                return None
            if current is None:
                return None
        return current
    


class ExternalResourceProxy:
    """
    Proxy for the main ExternalResource that wraps all sub-resources
    with DataFrame batch processing capability.
    """
    
    def __init__(self, client):
        self._client = client
        self._external_resource = ExternalResource(client)
    
    @property
    def news(self):
        """News API with DataFrame batch processing."""
        return DataFrameBatchProxy(self._external_resource.news)
    
    @property  
    def people(self):
        """People/Apollo API with DataFrame batch processing."""
        return DataFrameBatchProxy(self._external_resource.people)
    
    @property
    def search_api(self):
        """Search API with DataFrame batch processing.""" 
        return DataFrameBatchProxy(self._external_resource.search_api)
    
    def __getattr__(self, name: str):
        """Delegate any other attributes to the original external resource."""
        return getattr(self._external_resource, name)