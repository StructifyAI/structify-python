# Dynamic proxy for adding DataFrame batch processing to all external endpoints

from __future__ import annotations

from typing import Any, Dict
from concurrent.futures import ThreadPoolExecutor

try:
    import polars as pl
except ImportError:
    pl = None  # type: ignore[assignment]

from .._base_client import make_request_options
from .external import ExternalResource

__all__ = ["ExternalResourceProxy"]


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
            
            results = []
            for future in futures:
                try:
                    result = future.result()
                    if isinstance(result, dict):
                        results.append(result)
                    elif isinstance(result, list) and len(result) > 0:
                        # If API returns a list, extend results
                        if isinstance(result[0], dict):
                            results.extend(result)
                        else:
                            results.append({"result": result})
                    else:
                        results.append({"result": result})
                except Exception as e:
                    results.append({"error": str(e)})
        
        return pl.DataFrame(results) if results else pl.DataFrame()
    
    def _execute_single_request(self, original_method, payload: Dict[str, Any]) -> Any:
        """Execute a single API request."""
        # Call the original method with the payload as keyword arguments
        return original_method(**payload)
    


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