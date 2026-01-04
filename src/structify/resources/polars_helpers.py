# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from __future__ import annotations

import os
from typing import Any, Dict, List, Optional

import polars as pl

from ..types.table_param import Property, TableParam
from ..types.property_type_param import PropertyTypeParam


def get_node_id() -> Optional[str]:
    return os.environ.get("STRUCTIFY_NODE_ID")


def merge_column_properties(
    existing_properties: List[Property],
    new_properties: List[Property],
) -> List[Property]:
    all_properties = existing_properties.copy()

    for new_prop in new_properties:
        for prop in all_properties:
            if prop["name"] == new_prop["name"]:
                existing_type = prop.get("prop_type")
                new_type = new_prop.get("prop_type")
                if existing_type != new_type:
                    raise ValueError(
                        f"Column '{prop['name']}' type mismatch: existing column has type '{existing_type}' "
                        f"but new column specifies type '{new_type}'. "
                        f"Please ensure the new column type matches the existing column type, "
                        f"or use a different column name."
                    )
                prop["description"] = new_prop["description"]
                if "merge_strategy" in new_prop:
                    prop["merge_strategy"] = new_prop["merge_strategy"]
                break
        else:
            all_properties.append(new_prop)

    return all_properties


def dtype_to_structify_type(dtype: pl.DataType) -> PropertyTypeParam:
    if dtype == pl.Int64:
        return "Integer"
    elif dtype == pl.Float64:
        return "Float"
    elif dtype == pl.Boolean:
        return "Boolean"
    elif dtype == pl.String:
        return "String"
    elif dtype == pl.Date:
        return "Date"
    elif isinstance(dtype, pl.Enum):
        return {"enum": list(dtype.categories)}
    else:
        return "String"


def structify_type_to_polars_dtype(structify_type: PropertyTypeParam | None) -> pl.DataType:
    if structify_type == "Integer":
        return pl.Int64()
    elif structify_type == "Float":
        return pl.Float64()
    elif structify_type == "Boolean":
        return pl.Boolean()
    elif structify_type == "String":
        return pl.String()
    elif structify_type == "Date":
        return pl.Date()
    elif isinstance(structify_type, dict) and "enum" in structify_type:
        return pl.Enum(categories=structify_type["enum"])
    else:
        return pl.String()


def properties_to_schema(properties: list[Property]) -> pl.Schema:
    return pl.Schema({prop["name"]: structify_type_to_polars_dtype(prop.get("prop_type")) for prop in properties})


def schema_to_properties(schema: pl.Schema) -> list[Property]:
    return [
        Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype))
        for col_name, dtype in schema.items()
    ]


def _merge_schema_with_suffix(
    input_schema: pl.Schema,
    new_columns: dict[str, pl.DataType],
    *,
    suffix: str,
) -> pl.Schema:
    merged: dict[str, pl.DataType] = dict(input_schema)
    for col, dtype in new_columns.items():
        effective = col if (col not in input_schema) else f"{col}_{suffix}"
        merged[effective] = dtype

    return pl.Schema(merged)


def as_table_param(table_name: str, schema: Dict[str, Dict[str, Any]]) -> TableParam:
    return TableParam(
        name=table_name,
        description="",
        properties=[
            Property(
                name=col_name,
                description=type_and_desc.get("description", ""),
                prop_type=dtype_to_structify_type(type_and_desc["type"]),
            )
            for col_name, type_and_desc in schema.items()
        ],
    )
