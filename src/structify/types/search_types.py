# Type definitions for search service

from typing import List, Optional, TypedDict


class SearchResult(TypedDict):
    """Individual search result from the search API."""

    query: str
    url: str
    title: str
    description: str


class SearchRequest(TypedDict):
    """Request payload for search API."""

    query: str
    num_results: int
    banned_domains: Optional[List[str]]


class SearchResponse(TypedDict):
    """Response from the search API."""

    results: List[SearchResult]
    query: str
    count: int
