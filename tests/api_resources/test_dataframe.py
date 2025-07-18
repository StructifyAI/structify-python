# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import polars as pl
import pytest

from structify import Structify

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolars:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_enhance_columns(self, client: Structify) -> None:
        # Create test LazyFrame
        data = {"name": ["Alex", "Bob", "Charlie"], "age": [25, 30, 35], "city": ["New York", "London", "Tokyo"]}
        lazy_df = pl.DataFrame(data).lazy()

        dataframe = client.polars.enhance_columns(
            df=lazy_df,
            new_columns=[{"name": "occupation", "description": "Person's job title"}],
            dataframe_name="people",
            dataframe_description="People data",
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_enhance_columns_with_all_params(self, client: Structify) -> None:
        # Create test LazyFrame
        data = {"name": ["Alex", "Bob", "Charlie"], "age": [25, 30, 35], "city": ["New York", "London", "Tokyo"]}
        lazy_df = pl.DataFrame(data).lazy()

        dataframe = client.polars.enhance_columns(
            df=lazy_df,
            new_columns=[
                {"name": "occupation", "description": "Person's job title"},
                {"name": "salary", "description": "Person's annual salary"},
            ],
            dataframe_name="people",
            dataframe_description="People data including employment information",
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_scrape_urls(self, client: Structify) -> None:
        # Create test LazyFrame with URLs
        url_data = {"url": ["https://example.com", "https://test.com"], "id": [1, 2]}
        lazy_df = pl.DataFrame(url_data).lazy()

        schema = {
            "company_name": {"description": "Name of the company", "type": pl.Utf8},
            "employee_count": {"description": "Number of employees", "type": pl.Int64},
        }

        column_map = {"company_name": "name", "employee_count": "employees"}

        dataframe = client.polars.scrape_urls(
            lazy_df=lazy_df,
            url_column="url",
            table_name="companies",
            scrape_schema=schema,
            original_column_map=column_map,
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_scrape_urls_with_all_params(self, client: Structify) -> None:
        # Create test LazyFrame with URLs
        url_data = {"url": ["https://example.com", "https://test.com"], "id": [1, 2]}
        lazy_df = pl.DataFrame(url_data).lazy()

        schema = {
            "company_name": {"description": "Name of the company", "type": pl.Utf8},
            "employee_count": {"description": "Number of employees", "type": pl.Int64},
        }

        column_map = {"company_name": "name", "employee_count": "employees"}

        dataframe = client.polars.scrape_urls(
            lazy_df=lazy_df,
            url_column="url",
            table_name="companies",
            scrape_schema=schema,
            original_column_map=column_map,
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_structure_pdf(self, client: Structify) -> None:
        # Mock PDF content
        pdf_content = b"PDF content here"

        schema = {
            "invoice_number": {"description": "The invoice number", "type": pl.Utf8},
            "amount": {"description": "Invoice amount", "type": pl.Float64},
        }

        dataframe = client.polars.structure_pdf(
            document=pdf_content,
            table_name="invoices",
            schema=schema,
        )
        assert isinstance(dataframe, pl.LazyFrame)
