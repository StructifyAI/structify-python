import uuid
from unittest.mock import MagicMock

import pytest

from structify.types.table_param import TableParam
from structify.resources.spark_dataframe import SparkDataFrameResource


@pytest.fixture()
def mock_client() -> MagicMock:  # type: ignore[return-value]
    """Return a Structify client stub with common endpoints mocked."""
    client = MagicMock()

    # jobs helper should always succeed
    client.jobs.wait_for_jobs.return_value = None

    # nested resources that are referenced by the helper
    client.scrape.list.return_value = "scrape-job-id"
    client.structure.run_async.return_value = "structure-job-id"

    # return predictable IDs for add_batch
    client.entities.add_batch.return_value = ["e1", "e2"]

    # datasets.view_table will be overwritten in individual tests as needed
    return client


@pytest.fixture()
def mock_spark() -> MagicMock:  # type: ignore[return-value]
    """Return a minimal SparkSession stub."""
    spark = MagicMock()
    sentinel_df = object()
    spark.createDataFrame.return_value = sentinel_df  # any call should return this sentinel
    return spark


def _sample_schema() -> TableParam:  # type: ignore[return-value]
    """Return a simple schema for use in the tests."""
    return {
        "name": "my_table",
        "description": "Test table",
        "properties": [
            {"name": "field1", "description": "First field"},
            {"name": "field2", "description": "Second field"},
        ],
    }


def test_scrape_url(mock_client: MagicMock, mock_spark: MagicMock) -> None:
    """scrape_url should request scraping and convert the results to a DataFrame."""
    # Fake entities returned by datasets.view_table
    entity1 = MagicMock(id="1", properties={"field1": "a", "field2": "b"})
    entity2 = MagicMock(id="2", properties={"field1": "c", "field2": "d"})
    mock_client.datasets.view_table.return_value = [entity1, entity2]

    helper = SparkDataFrameResource(mock_client)

    result = helper.scrape_url(
        url="http://example.com",
        table_name="my_table",
        schema=_sample_schema(),
        spark=mock_spark,
    )

    # The helper should return whatever the Spark stub produced
    assert result is mock_spark.createDataFrame.return_value

    mock_client.scrape.list.assert_called_once()
    mock_client.jobs.wait_for_jobs.assert_called_once_with(
        [
            mock_client.scrape.list.return_value,
        ]
    )
    mock_client.datasets.view_table.assert_called_once()


def test_structure_pdf(mock_client: MagicMock, mock_spark: MagicMock, monkeypatch: pytest.MonkeyPatch) -> None:
    """structure_pdf should upload a document, wait for structuring, and return a DataFrame."""
    # Ensure deterministic dataset name by patching uuid.uuid4
    monkeypatch.setattr(uuid, "uuid4", lambda: uuid.UUID(int=0))

    # Fake entities returned by datasets.view_table
    entity = MagicMock(id="1", properties={"field1": "x", "field2": "y"})
    mock_client.datasets.view_table.return_value = [entity]

    helper = SparkDataFrameResource(mock_client)

    result = helper.structure_pdf(
        document=b"%PDF-1.4\n%...\n",
        table_name="my_table",
        schema=_sample_schema(),
        spark=mock_spark,
    )

    assert result is mock_spark.createDataFrame.return_value

    # Validate that the main calls were executed exactly once
    mock_client.datasets.create.assert_called_once()
    mock_client.documents.upload.assert_called_once()
    mock_client.structure.run_async.assert_called_once()
    mock_client.jobs.wait_for_jobs.assert_called_once_with(
        [
            mock_client.structure.run_async.return_value,
        ]
    )
    mock_client.datasets.view_table.assert_called_once()
