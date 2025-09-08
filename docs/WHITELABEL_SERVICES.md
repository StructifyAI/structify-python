# Whitelabel Services in Structify Python Client

## Overview

The whitelabel service pattern allows us to easily add new API services to the Structify Python client without duplicating boilerplate code. This pattern is based on a decorator-based approach that automatically handles HTTP requests, response parsing, and error handling.

## Architecture

### Core Components

1. **`WhitelabelResource`** - Base class that extends `SyncAPIResource` and provides common functionality
2. **`@whitelabel_method`** - Decorator that transforms methods into API calls
3. **Service-specific resources** - Classes that inherit from `WhitelabelResource` and define service methods

## Creating a New Whitelabel Service

### Step 1: Create the Service Resource

Create a new file in `src/structify/resources/your_service.py`:

```python
from typing import Dict, List, Any, Optional
from .whitelabel import WhitelabelResource, whitelabel_method

class YourServiceResource(WhitelabelResource):
    """Resource for your service functionality."""
    
    @whitelabel_method("/external/your-endpoint", method="POST")
    def your_method(
        self,
        param1: str,
        param2: int = 10
    ) -> Dict[str, Any]:
        """Your method description."""
        return {
            "param1": param1,
            "param2": param2
        }
```

### Step 2: Define Types (Optional)

Create type definitions in `src/structify/types/your_service_types.py`:

```python
from typing import TypedDict, List

class YourRequest(TypedDict):
    param1: str
    param2: int

class YourResponse(TypedDict):
    result: str
    data: List[Dict[str, Any]]
```

### Step 3: Register the Service

1. Add to `src/structify/resources/__init__.py`:
```python
from .your_service import YourServiceResource
# Add to __all__ list
```

2. Add to `src/structify/_client.py`:
```python
# In imports
from .resources import your_service

# In class definition
your_service: your_service.YourServiceResource

# In __init__ method
self.your_service = your_service.YourServiceResource(self)
```

## Decorator Options

The `@whitelabel_method` decorator supports several options:

### Basic Usage
```python
@whitelabel_method("/api/endpoint", method="POST")
```

### Extract Response Key
```python
@whitelabel_method("/api/endpoint", method="POST", response_key="results")
def get_results(self, query: str) -> List[Dict]:
    # This will return response["results"] instead of the full response
    return {"query": query}
```

### Pass-through Parameters
```python
@whitelabel_method("/api/endpoint", method="POST", pass_through_params=True)
def flexible_method(self, **kwargs) -> Dict:
    # All kwargs will be passed directly as the request body
    pass
```

## Features

### Automatic Response Wrappers

Every whitelabel service automatically gets:

1. **Raw Response Access**
```python
with client.your_service.with_raw_response.your_method(...) as response:
    print(response.status_code)
    data = response.parse()
```

2. **Streaming Response Access**
```python
with client.your_service.with_streaming_response.your_method(...) as response:
    for chunk in response:
        process(chunk)
```

### Method Types

You can create different types of methods:

1. **Simple API Call**
```python
@whitelabel_method("/api/search", method="POST")
def search(self, query: str) -> Dict:
    return {"query": query}
```

2. **Convenience Method with Response Processing**
```python
@whitelabel_method("/api/search", method="POST", response_key="results")
def search_results_only(self, query: str) -> List:
    return {"query": query}
```

3. **Complex Client-side Logic**
```python
def search_multiple(self, queries: List[str]) -> List[Dict]:
    """Make multiple API calls and aggregate results."""
    all_results = []
    for query in queries:
        response = self.search(query)
        all_results.extend(response["results"])
    return all_results
```

## Real Example: Search Service

Here's the complete search service implementation:

```python
from typing import List, Optional, Dict, Any
from .whitelabel import WhitelabelResource, whitelabel_method

class SearchResource(WhitelabelResource):
    """Resource for web search functionality."""
    
    @whitelabel_method("/external/search", method="POST")
    def search(
        self, 
        query: str, 
        num_results: int = 10,
        banned_domains: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Perform a web search."""
        request_data = {
            "query": query,
            "num_results": num_results,
        }
        if banned_domains:
            request_data["banned_domains"] = banned_domains
        return request_data
    
    @whitelabel_method("/external/search", method="POST", response_key="results")
    def search_results_only(
        self,
        query: str,
        num_results: int = 10
    ) -> List[Dict[str, Any]]:
        """Get just the results array."""
        return {"query": query, "num_results": num_results}
```

## Usage

```python
from structify import Structify

client = Structify(api_key="...")

# Use the search service
results = client.search.search("AI companies", num_results=5)
print(f"Found {results['count']} results")

# Get just the results array
results_only = client.search.search_results_only("machine learning")
for result in results_only:
    print(result["url"])

# Access raw response
with client.search.with_raw_response.search("quantum computing") as response:
    print(f"Status: {response.status_code}")
    data = response.parse()
```

## Benefits

1. **Code Reuse**: No need to duplicate HTTP client code
2. **Consistency**: All services follow the same pattern
3. **Automatic Features**: Raw/streaming responses work automatically
4. **Type Safety**: Full type hints support
5. **Easy Testing**: Services can be easily mocked
6. **Documentation**: Docstrings are preserved and accessible

## Best Practices

1. **Keep methods focused**: Each method should do one thing well
2. **Use type hints**: Always specify parameter and return types
3. **Document thoroughly**: Write clear docstrings with examples
4. **Handle errors gracefully**: The decorator handles HTTP errors automatically
5. **Create convenience methods**: Provide both full responses and extracted data
6. **Group related functionality**: One resource class per service domain

## Testing

When testing whitelabel services, you can mock the underlying HTTP calls:

```python
def test_search_service(mocker):
    client = Structify(api_key="test")
    
    # Mock the _post method
    mock_response = {"results": [...], "count": 5}
    mocker.patch.object(
        client.search, 
        '_post',
        return_value=mock_response
    )
    
    result = client.search.search("test query")
    assert result["count"] == 5
```

## Migration Guide

To migrate an existing service to use the whitelabel pattern:

1. Identify the API endpoints and methods
2. Create a new resource class extending `WhitelabelResource`
3. Add `@whitelabel_method` decorators to methods
4. Remove manual HTTP client code
5. Update client initialization
6. Test thoroughly

## Future Enhancements

Potential improvements to the whitelabel pattern:

1. **Async support**: Add `AsyncWhitelabelResource` for async operations
2. **Retry logic**: Configurable retry strategies per method
3. **Caching**: Built-in response caching with TTL
4. **Metrics**: Automatic performance metrics collection
5. **Validation**: Request/response schema validation