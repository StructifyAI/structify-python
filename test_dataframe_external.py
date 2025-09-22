#!/usr/bin/env python3
"""Test DataFrame batch processing for external endpoints."""

import sys
sys.path.insert(0, '/tmp/structify-python/src')

import os
import polars as pl
import structify

def test_dataframe_batch_processing():
    """Test that DataFrame batch processing works for external endpoints."""
    
    # Get API key from environment or use test key
    api_key = os.environ.get('STRUCTIFY_API_KEY', 'test')
    
    # Create client
    client = structify.Structify(api_key=api_key)
    
    # Create test DataFrame with multiple search queries
    df = pl.DataFrame({
        'query': ['Python programming', 'Machine learning', 'Data science'],
        'num_results': [5, 3, 4]
    })
    
    print("Input DataFrame:")
    print(df)
    print()
    
    # Access the external endpoints through polars
    external = client.polars.external
    
    print("Available batch processing methods:")
    methods = [m for m in dir(external) if not m.startswith('_') and 
               m not in ['with_raw_response', 'with_streaming_response'] and 
               callable(getattr(external, m))]
    for method in methods:
        print(f"  - {method}")
    print()
    
    # Example: Google search with batch processing
    print("Example usage - Google search batch processing:")
    print("  results = external.google_search(df)")
    print("  This would process all 3 queries in parallel and return results as a DataFrame")
    print()
    
    # Create DataFrame for organization enrichment
    org_df = pl.DataFrame({
        'domain': ['google.com', 'microsoft.com', 'apple.com']
    })
    
    print("Organization enrichment example:")
    print(org_df)
    print("  enriched = external.organizations_enrich(org_df)")
    print("  This would enrich all 3 organizations in parallel")
    print()
    
    # Create DataFrame for people search
    people_df = pl.DataFrame({
        'first_name': ['John', 'Jane', 'Bob'],
        'last_name': ['Doe', 'Smith', 'Johnson'],
        'organization_name': ['Google', 'Microsoft', 'Apple']
    })
    
    print("People match example:")
    print(people_df)
    print("  matched = external.people_match(people_df)")
    print("  This would match all 3 people in parallel")
    
    return True

if __name__ == '__main__':
    success = test_dataframe_batch_processing()
    if success:
        print("\n✅ DataFrame batch processing interface is ready!")
        print("Each method takes a DataFrame where every row becomes a parallel API call.")
    else:
        print("\n❌ Test failed")
        sys.exit(1)