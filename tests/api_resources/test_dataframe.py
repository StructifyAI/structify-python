# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest
import polars as pl

from structify import Structify
from structify.types import TableParam

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataframe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_enhance_column(self, client: Structify) -> None:
        # Create test LazyFrame
        data = {"name": ["Alex", "Bob", "Charlie"], "age": [25, 30, 35], "city": ["New York", "London", "Tokyo"]}
        lazy_df = pl.DataFrame(data).lazy()

        dataframe = client.dataframe.enhance_column(
            df=lazy_df,
            column_name="occupation",
            column_description="Person's job title",
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_enhance_column_with_all_params(self, client: Structify) -> None:
        # Create test LazyFrame
        data = {"name": ["Alex", "Bob", "Charlie"], "age": [25, 30, 35], "city": ["New York", "London", "Tokyo"]}
        lazy_df = pl.DataFrame(data).lazy()

        dataframe = client.dataframe.enhance_column(
            df=lazy_df,
            column_name="occupation",
            column_description="Person's job title",
            table_name="people",
            table_description="People data",
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_scrape_urls(self, client: Structify) -> None:
        # Create test LazyFrame with URLs
        url_data = {"url": ["https://example.com", "https://test.com"], "id": [1, 2]}
        lazy_df = pl.DataFrame(url_data).lazy()

        schema = {
            "name": "companies",
            "description": "Company data",
            "properties": [
                {"name": "company_name", "description": "Name of the company"},
                {"name": "employee_count", "description": "Number of employees"},
            ],
        }

        column_map = {"company_name": "name", "employee_count": "employees"}

        dataframe = client.dataframe.scrape_urls(
            lazy_df=lazy_df,
            url_column="url",
            table_name="companies",
            ScrapeSchema=schema,
            original_column_map=column_map,
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_scrape_urls_with_all_params(self, client: Structify) -> None:
        # Create test LazyFrame with URLs
        url_data = {"url": ["https://example.com", "https://test.com"], "id": [1, 2]}
        lazy_df = pl.DataFrame(url_data).lazy()

        schema: TableParam = {
            "name": "companies",
            "description": "Company data",
            "properties": [
                {"name": "company_name", "description": "Name of the company"},
                {"name": "employee_count", "description": "Number of employees"},
            ],
        }

        column_map = {"company_name": "name", "employee_count": "employees"}

        dataframe = client.dataframe.scrape_urls(
            lazy_df=lazy_df,
            url_column="url",
            table_name="companies",
            ScrapeSchema=schema,
            original_column_map=column_map,
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_structure_pdf(self, client: Structify) -> None:
        # Mock PDF content
        pdf_content = b"PDF content here"

        schema: TableParam = {
            "name": "invoices",
            "description": "Invoice data",
            "properties": [
                {"name": "invoice_number", "description": "Invoice number"},
                {"name": "amount", "description": "Invoice amount"},
            ],
        }

        dataframe = client.dataframe.structure_pdf(
            document=pdf_content,
            table_name="invoices",
            schema=schema,
        )
        assert isinstance(dataframe, pl.LazyFrame)
