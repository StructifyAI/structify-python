# Generic whitelabel service infrastructure for Structify Python client

from __future__ import annotations

from typing import Any, Dict, Optional, TypeVar, Callable
from functools import wraps

from .._resource import SyncAPIResource
from .._compat import cached_property
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)

__all__ = ["WhitelabelResource", "whitelabel_method"]

T = TypeVar("T")


def whitelabel_method(
    endpoint: str,
    method: str = "POST",
    response_key: Optional[str] = None,
    pass_through_params: bool = False,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator for creating whitelabel service methods that proxy to API endpoints.
    
    Args:
        endpoint: The API endpoint to call (e.g., "/external/search")
        method: HTTP method to use (GET, POST, etc.)
        response_key: If set, extract this key from the response object
        pass_through_params: If True, pass all kwargs directly to the API call
    
    Example:
        @whitelabel_method("/external/search", response_key="results")
        def search(self, query: str, num_results: int = 10) -> list:
            return {"query": query, "num_results": num_results}
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(self: WhitelabelResource, *args, **kwargs) -> Any:
            # Call the original function to get the request payload
            payload = func(self, *args, **kwargs)
            
            # If pass_through_params is True, use kwargs directly as payload
            if pass_through_params:
                payload = kwargs
            
            # Make the API call
            if method.upper() == "GET":
                response = self._get(endpoint, params=payload)
            elif method.upper() == "POST":
                response = self._post(endpoint, body=payload)
            elif method.upper() == "PUT":
                response = self._put(endpoint, body=payload)
            elif method.upper() == "DELETE":
                response = self._delete(endpoint)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            # Extract response key if specified
            if response_key and isinstance(response, dict):
                return response.get(response_key, response)
            
            return response
        
        # Store metadata for documentation generation
        wrapper._whitelabel_metadata = {
            "endpoint": endpoint,
            "method": method,
            "response_key": response_key,
        }
        
        return wrapper
    
    return decorator


class WhitelabelResource(SyncAPIResource):
    """
    Base class for whitelabel service resources.
    
    This provides a foundation for creating service-specific resources
    that proxy to backend APIs while maintaining a clean client interface.
    """
    
    @cached_property
    def with_raw_response(self) -> WhitelabelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.
        """
        return WhitelabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhitelabelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.
        """
        return WhitelabelResourceWithStreamingResponse(self)
    
    def _build_headers(self, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Build headers for API requests, allowing service-specific customization."""
        headers = {}
        if extra_headers:
            headers.update(extra_headers)
        return headers


class WhitelabelResourceWithRawResponse:
    def __init__(self, resource: WhitelabelResource) -> None:
        self._resource = resource
        
        # Dynamically wrap all whitelabel methods
        for attr_name in dir(resource):
            if not attr_name.startswith("_"):
                attr = getattr(resource, attr_name)
                if callable(attr) and hasattr(attr, "_whitelabel_metadata"):
                    setattr(self, attr_name, to_raw_response_wrapper(attr))


class WhitelabelResourceWithStreamingResponse:
    def __init__(self, resource: WhitelabelResource) -> None:
        self._resource = resource
        
        # Dynamically wrap all whitelabel methods
        for attr_name in dir(resource):
            if not attr_name.startswith("_"):
                attr = getattr(resource, attr_name)
                if callable(attr) and hasattr(attr, "_whitelabel_metadata"):
                    setattr(self, attr_name, to_streamed_response_wrapper(attr))