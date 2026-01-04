# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from __future__ import annotations

from typing import Any, Dict

import polars as pl
from polars import LazyFrame

from .polars_helpers import (
    dtype_to_structify_type,
    _merge_schema_with_suffix,
    structify_type_to_polars_dtype,
)
from ..types.table_param import Property, TableParam


class DeprecatedPolarsMixin:
    def enhance_columns(
        self,
        *,
        df: LazyFrame,
        new_columns: Dict[str, Dict[str, Any]],
        dataframe_name: str,
        dataframe_description: str,
    ) -> LazyFrame:
        structured = self.structure(
            df=df,
            new_columns=new_columns,
            table_name=dataframe_name,
            table_description=dataframe_description,
        )
        return structured.drop(["_original_index", "_job_id", "_explanation"])

    def scrape_columns(
        self,
        *,
        df: LazyFrame,
        url_column: str,
        new_columns: Dict[str, Dict[str, Any]],
        dataframe_name: str,
        dataframe_description: str,
        use_proxy: bool = False,
    ) -> LazyFrame:
        input_schema = df.collect_schema()
        if url_column not in input_schema:
            raise ValueError(f"Column '{url_column}' not found in LazyFrame")

        instruction = f"Use the URL in column '{url_column}' as the source for scraping."
        browser = {"proxy": use_proxy} if use_proxy else None

        structured = self.structure(
            df=df,
            new_columns=new_columns,
            table_name=dataframe_name,
            table_description=dataframe_description,
            instruction=instruction,
            browser=browser,
        )
        return structured.drop(["_original_index", "_job_id", "_explanation"])

    def scrape_relationships(
        self,
        *,
        lazy_df: LazyFrame,
        url_column: str,
        table_name: str,
        scrape_schema: Dict[str, Dict[str, Any]],
        scrape_schema_override: TableParam | None = None,
        original_column_map: Dict[str, str] | None = None,
        source_table_name: str = "source_table",
        relationship_name: str = "scraped",
        relationship_description: str = "",
        use_proxy: bool = False,
    ) -> LazyFrame:
        input_schema = lazy_df.collect_schema()
        if url_column not in input_schema:
            raise ValueError(f"Column '{url_column}' not found in LazyFrame")
        if original_column_map is None:
            original_column_map = {}

        scraped_columns: dict[str, pl.DataType] = {}
        column_details: dict[str, dict[str, Any]] = {}
        if scrape_schema_override:
            for prop in scrape_schema_override["properties"]:
                prop_name = original_column_map.get(prop["name"], prop["name"])
                prop_type = prop.get("prop_type")
                if prop_type is None:
                    raise ValueError("scrape_schema_override properties must include 'prop_type'.")
                scraped_columns[prop_name] = structify_type_to_polars_dtype(prop_type)
                column_details[prop_name] = {
                    "description": prop.get("description", ""),
                    "prop_type": prop_type,
                    "merge_strategy": prop.get("merge_strategy"),
                }
        else:
            for col_name, col_info in scrape_schema.items():
                dtype = col_info.get("type", pl.String())
                scraped_columns[col_name] = dtype
                column_details[col_name] = {
                    "description": col_info.get("description", ""),
                    "prop_type": dtype_to_structify_type(dtype),
                }

        output_schema = _merge_schema_with_suffix(input_schema, scraped_columns, suffix=table_name)

        new_columns: list[Property] = []
        for col_name in scraped_columns:
            effective_name = col_name if col_name not in input_schema else f"{col_name}_{table_name}"
            details = column_details[col_name]
            prop: Property = {
                "name": effective_name,
                "description": details.get("description", ""),
                "prop_type": details.get("prop_type"),
            }
            if details.get("merge_strategy") is not None:
                prop["merge_strategy"] = details.get("merge_strategy")
            new_columns.append(prop)

        instruction_parts = [
            f"Use the URL in column '{url_column}' as the source for scraping.",
            f"Source table: {source_table_name}.",
            f"Find {relationship_name} for each row and return one row per related entity.",
            relationship_description,
        ]
        instruction = " ".join([part for part in instruction_parts if part])
        browser = {"proxy": use_proxy} if use_proxy else None

        structured = self.structure(
            df=lazy_df,
            new_columns=new_columns,
            table_name=table_name,
            table_description=relationship_description,
            instruction=instruction,
            allow_expand_rows=True,
            browser=browser,
        )
        structured = structured.drop(["_original_index", "_job_id", "_explanation"])
        structured_columns = structured.collect_schema().names()
        if scrape_schema_override and original_column_map:
            structured = structured.rename(
                {
                    col_name: original_column_map.get(col_name, col_name)
                    for col_name in original_column_map.values()
                    if col_name in structured_columns
                }
            )
        return structured.select(output_schema.names())

    def structure_pdfs(
        self,
        *,
        document_paths: LazyFrame,
        path_column: str,
        table_name: str,
        schema: Dict[str, Dict[str, Any]],
        conditioning: str = "",
    ) -> LazyFrame:
        for key, value in schema.items():
            if "type" not in value:
                raise ValueError(f"Missing 'type' for column '{key}' in schema")

        output_schema = pl.Schema(
            {
                path_column: pl.String(),
                **{col_name: col_info.get("type", pl.String()) for col_name, col_info in schema.items()},
            }
        )

        if path_column not in document_paths.collect_schema():
            raise ValueError(f"Column '{path_column}' not found in document_paths")

        collected = document_paths.collect()
        if collected.is_empty():
            return pl.DataFrame(schema=output_schema).lazy()

        non_null = collected.drop_nulls(subset=[path_column])
        if non_null.is_empty():
            with_nulls = collected.with_columns(
                [
                    pl.lit(None, dtype=output_schema[col_name]).alias(col_name)
                    for col_name in output_schema.names()
                    if col_name != path_column
                ]
            )
            return with_nulls.select(output_schema.names()).lazy()

        upload_df = self.upload_files(paths=non_null.select(path_column).unique().to_series().to_list())
        enriched = non_null.join(upload_df, left_on=path_column, right_on="local_path", how="left")

        new_columns: list[dict[str, Any]] = [
            {
                "name": col_name,
                "description": col_info.get("description", ""),
                "type": col_info.get("type", pl.String()),
            }
            for col_name, col_info in schema.items()
        ]

        structured = self.structure(
            df=enriched.lazy(),
            new_columns=new_columns,
            table_name=table_name,
            table_description=conditioning,
        )

        drop_candidates = [
            "_original_index",
            "_job_id",
            "_explanation",
            "file_path",
            "file_name",
            "file_extension",
            "file_size_bytes",
            "local_path",
        ]
        structured_columns = structured.collect_schema().names()
        columns_to_drop = [col for col in drop_candidates if col in structured_columns]
        structured = structured.drop(columns_to_drop)
        structured = structured.select([path_column] + list(schema.keys()))

        result = collected.lazy().join(structured, on=path_column, how="left")
        return result.select(output_schema.names())
