# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from unittest.mock import Mock, patch

import polars as pl
import pytest

from structify import Structify

# Shared schema & helpers used across multiple tests
SCRAPE_SCHEMA = {
    "company_name": {"description": "Name of the company", "type": pl.Utf8},
    "employee_count": {"description": "Number of employees", "type": pl.Int64},
}

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
            new_columns={
                "occupation": {"description": "Person's job title", "type": pl.Utf8},
            },
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
            new_columns={
                "occupation": {"description": "Person's job title", "type": pl.Utf8},
                "salary": {"description": "Person's annual salary", "type": pl.Float64},
            },
            dataframe_name="people",
            dataframe_description="People data including employment information",
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_scrape_urls(self, client: Structify) -> None:
        # Create test LazyFrame with URLs
        url_data = {"url": ["https://example.com", "https://test.com"], "id": [1, 2]}
        lazy_df = pl.DataFrame(url_data).lazy()

        dataframe = client.polars.scrape_urls(
            lazy_df=lazy_df,
            url_column="url",
            table_name="companies",
            scrape_schema=SCRAPE_SCHEMA,
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_scrape_urls_with_all_params(self, client: Structify) -> None:
        # Create test LazyFrame with URLs
        url_data = {"url": ["https://example.com", "https://test.com"], "id": [1, 2]}
        lazy_df = pl.DataFrame(url_data).lazy()

        dataframe = client.polars.scrape_urls(
            lazy_df=lazy_df,
            url_column="url",
            table_name="companies",
            scrape_schema=SCRAPE_SCHEMA,
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

        # Mock all the API calls that structure_pdf makes
        with patch.object(client.datasets, "create") as mock_create, patch.object(
            client.documents, "upload"
        ) as mock_upload, patch.object(client.structure, "run_async") as mock_run_async, patch.object(
            client.jobs, "wait_for_jobs"
        ) as mock_wait_for_jobs, patch.object(client.datasets, "view_table") as mock_view_table:
            # Configure mock return values
            mock_run_async.return_value = "test-job-id"
            mock_wait_for_jobs.return_value = None  # No error message

            # Mock entity with sample data
            mock_entity = Mock()
            mock_entity.properties = {"invoice_number": "INV-001", "amount": 1234.56}
            mock_view_table.return_value = [mock_entity]

            dataframe = client.polars.structure_pdf(
                document=pdf_content,
                table_name="invoices",
                schema=schema,
            )

            assert isinstance(dataframe, pl.LazyFrame)

            # Verify the API calls were made with correct parameters
            mock_create.assert_called_once()
            mock_upload.assert_called_once()
            mock_run_async.assert_called_once()
            mock_wait_for_jobs.assert_called_once_with(["test-job-id"])
            mock_view_table.assert_called_once()

            # Test that we can collect the LazyFrame and get the expected data
            result_df = dataframe.collect()
            assert len(result_df) == 1
            assert result_df["invoice_number"][0] == "INV-001"
            assert result_df["amount"][0] == 1234.56
