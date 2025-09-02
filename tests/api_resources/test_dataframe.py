# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from unittest.mock import Mock, patch, mock_open

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

        with patch.object(client.datasets, "create") as mock_create, patch.object(
            client.documents, "upload"
        ) as mock_upload, patch.object(client.structure, "run_async") as mock_run_async, patch.object(
            client.jobs, "wait_for_jobs"
        ) as mock_wait_for_jobs, patch.object(client.datasets, "view_table") as mock_view_table, patch(
            "builtins.open", mock_open(read_data=pdf_content)
        ):
            # Configure mock return values
            mock_run_async.return_value = "test-job-id"
            mock_wait_for_jobs.return_value = None  # No error message

            # Mock entity with sample data
            mock_entity = Mock()
            mock_entity.properties = {"invoice_number": "INV-001", "amount": 1234.56}
            mock_view_table.return_value = [mock_entity]

            dataframe = client.polars.structure_pdfs(
                document_paths=pl.DataFrame({"pdf_path": ["/tmp/fake.pdf"]}).lazy(),
                path_column="pdf_path",
                table_name="invoices",
                schema=schema,
            )

            assert isinstance(dataframe, pl.LazyFrame)

            # Trigger execution so that the mocked API methods are called
            result_df = dataframe.collect()

            # Verify the API calls were made with correct parameters AFTER execution
            mock_create.assert_called_once()
            mock_upload.assert_called_once()
            mock_run_async.assert_called_once()
            mock_wait_for_jobs.assert_called_once_with(
                job_ids=["test-job-id"], title="Parsing invoices from PDFs", node_id=None
            )
            mock_view_table.assert_called_once()

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
        with patch.object(client.datasets, "create") as mock_create, patch.object(
            client.entities, "add_batch"
        ) as mock_add_batch, patch.object(
            client.structure, "enhance_relationship"
        ) as mock_enhance_relationship, patch.object(client.jobs, "wait_for_jobs") as mock_wait_for_jobs, patch.object(
            client.datasets, "view_tables_with_relationships"
        ) as mock_view_tables_with_relationships:
            # Configure mock return values
            mock_add_batch.return_value = ["entity-1", "entity-2", "entity-3"]
            mock_enhance_relationship.return_value = "test-job-id"
            mock_wait_for_jobs.return_value = None

            # Build mock response mimicking DatasetViewTablesWithRelationshipsResponse
            # Source entities
            mock_source_1 = Mock(id="entity-1", properties={"company_name": "Structify"})
            mock_source_2 = Mock(id="entity-2", properties={"company_name": "Google"})
            mock_source_3 = Mock(id="entity-3", properties={"company_name": "Microsoft"})

            # Target/connected entities
            mock_target_1 = Mock(id="target-1", properties={"employee_name": "Alex", "position": "CEO"})
            mock_target_2 = Mock(id="target-2", properties={"employee_name": "Alex", "position": "SWE"})
            mock_target_3 = Mock(id="target-3", properties={"employee_name": "Alex", "position": "PM"})

            # Relationships connecting sources to targets
            rel1 = Mock(from_id="entity-1", to_id="target-1")
            rel2 = Mock(from_id="entity-2", to_id="target-2")
            rel3 = Mock(from_id="entity-3", to_id="target-3")

            mock_response = Mock()
            mock_response.entities = [mock_source_1, mock_source_2, mock_source_3]
            mock_response.connected_entities = [mock_target_1, mock_target_2, mock_target_3]
            mock_response.relationships = [rel1, rel2, rel3]

            mock_view_tables_with_relationships.return_value = mock_response

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
            mock_create.assert_called_once()
            mock_add_batch.assert_called_once()
            assert mock_enhance_relationship.call_count == 3  # One for each entity
            mock_wait_for_jobs.assert_called_once()

            assert len(result_df) == 3
            assert "company_name" in result_df.columns
            assert "employee_name" in result_df.columns
            assert "position" in result_df.columns

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
