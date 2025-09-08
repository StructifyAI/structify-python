#!/usr/bin/env python3
"""
Example usage of the Structify search service.

This demonstrates how to use the whitelabel search API through the
Structify Python client.
"""

import os

from structify import Structify


def main():
    # Initialize the client
    client = Structify(
        api_key=os.environ.get("STRUCTIFY_API_TOKEN"),
        environment="production"
    )
    
    print("=" * 60)
    print("Structify Search Service Example")
    print("=" * 60)
    
    # Example 1: Basic search
    print("\n1. Basic Search for 'artificial intelligence startups':")
    print("-" * 40)
    
    response = client.external.search.search(
        query="artificial intelligence startups",
        num_results=5
    )
    
    print(f"Found {response['count']} results for '{response['query']}':")
    for i, result in enumerate(response['results'], 1):
        print(f"\n{i}. {result['title']}")
        print(f"   URL: {result['url']}")
        print(f"   Description: {result['description'][:100]}...")
    
    # Example 2: Search with banned domains
    print("\n\n2. Search excluding certain domains:")
    print("-" * 40)
    
    response = client.external.search.search(
        query="machine learning frameworks",
        num_results=5,
        banned_domains=["medium.com", "towardsdatascience.com"]
    )
    
    print(f"Found {response['count']} results (excluding Medium):")
    for result in response['results']:
        print(f"  - {result['title']} ({result['url']})")
    
    # Example 3: Get results only (convenience method)
    print("\n\n3. Get results array directly:")
    print("-" * 40)
    
    results = client.external.search.search_results_only(
        query="deep learning research papers",
        num_results=3
    )
    
    print(f"Direct results (showing URLs only):")
    for result in results:
        print(f"  - {result['url']}")
    
    # Example 4: Multiple searches with deduplication
    print("\n\n4. Multiple searches with automatic deduplication:")
    print("-" * 40)
    
    queries = [
        "transformer models NLP",
        "BERT GPT language models",
        "attention mechanism deep learning"
    ]
    
    all_results = client.external.search.search_multiple(
        queries=queries,
        num_results_per_query=3
    )
    
    print(f"Combined results from {len(queries)} queries ({len(all_results)} unique URLs):")
    for result in all_results:
        print(f"  - {result['title'][:50]}... ({result['url'][:40]}...)")
    
    # Example 5: Using raw response
    print("\n\n5. Access raw HTTP response:")
    print("-" * 40)
    
    with client.external.search.with_raw_response.search(
        query="quantum computing",
        num_results=2
    ) as response:
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)[:100]}...")
        data = response.parse()
        print(f"First result: {data['results'][0]['title']}")


if __name__ == "__main__":
    main()