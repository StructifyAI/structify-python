# Generic whitelabel service infrastructure for Structify Python client

from __future__ import annotations

from typing import Any, Dict, List, TypeVar, Callable, Optional, cast
from functools import wraps
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import polars as pl
except ImportError:
    pl = None  # type: ignore[assignment]

from .._compat import cached_property
from .._resource import SyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["WhitelabelResource", "whitelabel_method"]

T = TypeVar("T")


def whitelabel_method(
    endpoint: str,
    method: str = "POST",
    response_key: Optional[str] = None,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator for creating whitelabel service methods that proxy to API endpoints.
    
    Automatically processes DataFrame inputs as parallel API calls - each row becomes
    one API call, and results are returned as a DataFrame.

    Args:
        endpoint: The API endpoint to call (e.g., "/external/search")
        method: HTTP method to use (GET, POST, etc.)
        response_key: If set, extract this key from the response object

    Example:
        @whitelabel_method("/external/search")
        def search(self, df: pl.DataFrame) -> pl.DataFrame:
            return df  # Each row becomes a parallel API call automatically
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(self: WhitelabelResource, *args: Any, **kwargs: Any) -> Any:
            # Always process DataFrame inputs as parallel API calls
            if pl is None:
                raise ImportError("polars is required for whitelabel methods but is not installed")
            
            # Find the DataFrame in the arguments
            df = None
            for arg in args:
                if hasattr(arg, "__class__") and arg.__class__.__name__ == "DataFrame":
                    df = arg
                    break
            
            if df is None:
                for value in kwargs.values():
                    if hasattr(value, "__class__") and value.__class__.__name__ == "DataFrame":
                        df = value
                        break
            
            if df is None:
                raise ValueError("DataFrame not found in arguments - whitelabel methods require DataFrame input")
            
            # Convert DataFrame rows to parallel API calls
            rows = df.to_dicts()
            if not rows:
                # Return empty DataFrame with same schema
                return df.clear()
            
            # Execute parallel requests
            with ThreadPoolExecutor(max_workers=20) as executor:
                futures = [
                    executor.submit(self._execute_single_request, endpoint, row, method)
                    for row in rows
                ]
                results = [future.result() for future in futures]
            
            # Convert results back to DataFrame
            return pl.DataFrame(results) if results else pl.DataFrame()

        # Store metadata for documentation generation
        setattr(wrapper, "_whitelabel_metadata", {"endpoint": endpoint, "method": method, "response_key": response_key})  # noqa: B010

        return cast(Callable[..., T], wrapper)

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
        headers: Dict[str, str] = {}
        if extra_headers:
            headers.update(extra_headers)
        return headers

    def _execute_parallel_requests(
        self, endpoint: str, queries: List[str], payload: Dict[str, Any], method: str, max_workers: int = 20
    ) -> List[Dict[str, Any]]:
        """Execute parallel requests for multiple queries."""
        results: List[Dict[str, Any]] = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all requests
            future_to_query: Dict[Any, str] = {}
            for query in queries:
                if query:  # Skip empty queries
                    # Create individual payload for this query
                    single_payload = payload.copy()
                    single_payload["query"] = query
                    single_payload.pop("queries", None)  # Remove queries list

                    future = executor.submit(self._execute_single_request, endpoint, single_payload, method)
                    future_to_query[future] = query

            # Collect results as they complete
            for future in as_completed(future_to_query):
                current_query: str = future_to_query[future]
                single_result = future.result()

                # Add query column to each result if it's a list
                if isinstance(single_result, list):
                    for result in cast(List[Any], single_result):
                        if isinstance(result, dict):
                            result_dict = cast(Dict[str, Any], result)
                            result_dict["query"] = current_query
                            results.append(result_dict)
                elif isinstance(single_result, dict):
                    single_result_dict = cast(Dict[str, Any], single_result)
                    single_result_dict["query"] = current_query
                    results.append(single_result_dict)

        return results

    def _execute_single_request(self, endpoint: str, payload: Dict[str, Any], method: str) -> Any:
        """Execute a single request to the API."""
        if method.upper() == "GET":
            return self._get(
                endpoint, cast_to=object, options=make_request_options(extra_query=cast(Dict[str, object], payload))
            )
        elif method.upper() == "POST":
            return self._post(endpoint, body=payload, cast_to=object, options=make_request_options())
        elif method.upper() == "PUT":
            return self._put(endpoint, body=payload, cast_to=object, options=make_request_options())
        elif method.upper() == "DELETE":
            return self._delete(endpoint, cast_to=object, options=make_request_options())
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")


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
