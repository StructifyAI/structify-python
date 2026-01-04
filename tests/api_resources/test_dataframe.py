# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import tempfile
from unittest.mock import Mock, patch

import polars as pl
import pytest

from structify import Structify
from structify.resources.polars import dtype_to_structify_type, structify_type_to_polars_dtype

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
    def test_method_scrape_columns(self, client: Structify) -> None:
        # Create test LazyFrame with URLs
        url_data = {"url": ["https://example.com", "https://test.com"], "id": [1, 2]}
        lazy_df = pl.DataFrame(url_data).lazy()

        dataframe = client.polars.scrape_columns(
            df=lazy_df,
            url_column="url",
            new_columns=SCRAPE_SCHEMA,
            dataframe_name="companies",
            dataframe_description="Company data scraped from URLs",
        )
        assert isinstance(dataframe, pl.LazyFrame)

    @parametrize
    def test_method_scrape_columns_with_all_params(self, client: Structify) -> None:
        # Create test LazyFrame with URLs
        url_data = {"url": ["https://example.com", "https://test.com"], "id": [1, 2]}
        lazy_df = pl.DataFrame(url_data).lazy()

        dataframe = client.polars.scrape_columns(
            df=lazy_df,
            url_column="url",
            new_columns=SCRAPE_SCHEMA,
            dataframe_name="companies",
            dataframe_description="Company data scraped from URLs",
            use_proxy=True,
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

        with tempfile.NamedTemporaryFile(suffix=".pdf") as temp_file:
            temp_file.write(pdf_content)
            temp_file.flush()

            with patch.object(client.documents, "upload") as mock_upload, patch.object(
                client.polars, "_post"
            ) as mock_post, patch.object(client.jobs, "wait_for_jobs") as mock_wait_for_jobs, patch.object(
                client.datasets, "view_table"
            ) as mock_view_table:
                # Configure mock return values
                mock_post.return_value = {"dataset_name": "test_dataset", "table_name": "invoices", "job_ids": ["job-1"]}
                mock_wait_for_jobs.return_value = None

                # Mock entity with sample data
                mock_entity = Mock()
                mock_entity.properties = {
                    "pdf_path": temp_file.name,
                    "invoice_number": "INV-001",
                    "amount": 1234.56,
                }
                mock_view_table.return_value = [mock_entity]

                dataframe = client.polars.structure_pdfs(
                    document_paths=pl.DataFrame({"pdf_path": [temp_file.name]}).lazy(),
                    path_column="pdf_path",
                    table_name="invoices",
                    schema=schema,
                )

                assert isinstance(dataframe, pl.LazyFrame)

                # Trigger execution so that the mocked API methods are called
                result_df = dataframe.collect()

                # Verify the API calls were made with correct parameters AFTER execution
                mock_upload.assert_called_once()
                mock_post.assert_called_once()
                mock_wait_for_jobs.assert_called_once_with(
                    dataset_name="test_dataset",
                    title="Structuring invoices",
                    node_id=None,
                )
                mock_view_table.assert_called_once_with(dataset="test_dataset", name="invoices")

                # Validate returned data
                assert len(result_df) == 1
                assert result_df["invoice_number"][0] == "INV-001"
                assert result_df["amount"][0] == 1234.56

    @parametrize
    def test_method_enhance_relationships(self, client: Structify) -> None:
        # Create test LazyFrame with source data
        source_data = {"company_name": ["Structify", "Google", "Microsoft"]}
        lazy_df = pl.DataFrame(source_data).lazy()

        target_schema = {
            "employee_name": {"description": "Name of the employee", "type": pl.Utf8},
            "position": {"description": "Employee position", "type": pl.Utf8},
        }

        # Mock all the API calls that enhance_relationships makes
        with patch.object(client.polars, "_post") as mock_post, patch.object(
            client.jobs, "wait_for_jobs"
        ) as mock_wait_for_jobs, patch.object(client.datasets, "view_table") as mock_view_table:
            # Configure mock return values
            mock_post.return_value = {"dataset_name": "test_dataset", "table_name": "Company", "job_ids": ["job-1"]}
            mock_wait_for_jobs.return_value = None

            mock_entity = Mock()
            mock_entity.properties = {
                "company_name": "Structify",
                "employee_name": "Alex",
                "position": "CEO",
            }
            mock_view_table.return_value = [mock_entity]

            dataframe = client.polars.enhance_relationships(
                lazy_df=lazy_df,
                relationship_name="employees",
                relationship_description="Employees working at company",
                target_table_name="Employee",
                target_schema=target_schema,
                source_table_name="Company",
            )

            assert isinstance(dataframe, pl.LazyFrame)

            # Collect the LazyFrame – this triggers the side-effects in the lazy pipeline
            result_df = dataframe.collect()

            # Verify the API calls were made with correct parameters (after collect)
            mock_post.assert_called_once()
            mock_wait_for_jobs.assert_called_once_with(
                dataset_name="test_dataset",
                title="Structuring Company",
                node_id=None,
            )
            mock_view_table.assert_called_once_with(dataset="test_dataset", name="Company")

            assert len(result_df) == 1
            assert list(result_df.columns) == ["company_name", "employee_name", "position"]

    def test_enum_dtype(self) -> None:
        polars_int = pl.Int64()
        structify_int = dtype_to_structify_type(polars_int)
        assert structify_int == "Integer"
        assert structify_type_to_polars_dtype(structify_int) == polars_int

        polars_float = pl.Float64()
        structify_float = dtype_to_structify_type(polars_float)
        assert structify_float == "Float"
        assert structify_type_to_polars_dtype(structify_float) == polars_float

        polars_enum = pl.Enum(categories=["a", "b", "c"])
        structify_reversed_enum = dtype_to_structify_type(polars_enum)
        assert structify_reversed_enum == {"enum": ["a", "b", "c"]}
        assert structify_type_to_polars_dtype(structify_reversed_enum) == polars_enum
