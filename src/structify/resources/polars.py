# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from __future__ import annotations

import os
import uuid
from typing import Any, Dict, List, Tuple, Optional, TypedDict, cast
from concurrent.futures import Future, ThreadPoolExecutor, as_completed

import polars as pl
from tqdm import tqdm  # type: ignore
from polars import LazyFrame

from structify.types.entity_param import EntityParam
from structify.types.property_type_param import PropertyTypeParam
from structify.types.dataset_create_params import Relationship as CreateRelationshipParam
from structify.types.knowledge_graph_param import KnowledgeGraphParam

from ..types import TableParam
from .._compat import cached_property
from .._resource import SyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..types.table_param import Property
from .external_dataframe_proxy import ServicesProxy
from ..types.save_requirement_param import RequiredEntity, RequiredProperty
from ..types.dataset_descriptor_param import DatasetDescriptorParam
from ..types.structure_run_async_params import SourcePdf, StopConfig, SourceWebWeb

__all__ = ["PolarsResource"]

MAX_PARALLEL_REQUESTS = 20


class PolarsResource(SyncAPIResource):
    @cached_property
    def external(self) -> ServicesProxy:
        """Access external whitelabel services with DataFrame batch processing."""
        return ServicesProxy(self._client)

    @cached_property
    def with_raw_response(self) -> PolarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return PolarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return PolarsResourceWithStreamingResponse(self)

    def _add_single_entity(self, dataset_name: str, entity: EntityParam) -> tuple[str, EntityParam]:
        """Add a single entity to the given dataset and return (entity_id, entity).

        Always seeds with id=0 in the KnowledgeGraph to ensure consistent server-side ID assignment.
        """
        kg_param = KnowledgeGraphParam(
            entities=[EntityParam(type=entity["type"], id=0, properties=entity["properties"])],
            relationships=[],
        )
        entity_ids = self._client.entities.add_batch(
            dataset=dataset_name,
            entity_graphs=[kg_param],
        )
        return entity_ids[0], entity

    def enhance_columns(
        self,
        *,
        df: LazyFrame,
        new_columns: Dict[str, Dict[str, Any]],
        dataframe_name: str,
        dataframe_description: str,
        max_steps_override: int | None = None,
    ) -> LazyFrame:
        """
        Enhance one or more columns of a `LazyFrame` by letting Structify populate the
        values.

            • ``"type"`` (required):  a **Polars DataType *class*** (e.g. ``pl.Int64``)
            • ``"description"`` (optional): a human-readable string

        Example::

            new_cols = {
                "net_amount": {"type": pl.Float64, "description": "Net amount after tax"},
                "due_date": {"type": pl.Date},
            }

        Descriptions are optional but improve Structify's understanding of the
        data to infer.

        Args:
            df: The input `polars.LazyFrame` to enhance.
            new_columns: Schema describing the *new* columns. Accepts either a
                `polars.Schema` or a plain mapping from column name to dtype.
            dataframe_name: Logical name of the dataframe (e.g. "Company",
                "Invoice", …) – used as the Structify *entity type*.
            dataframe_description: Free-form description that provides the
                necessary context for Structify (e.g. "Companies that are in the
                food industry").
        """

        # Existing columns & their dtypes from the LazyFrame
        existing_schema_dict: Dict[str, pl.DataType] = df.collect_schema()

        # Normalise to Dict[str, Tuple[dtype, description]]
        new_columns_dict: Dict[str, tuple[pl.DataType, str]] = {}
        for col_name, val in new_columns.items():
            if "type" not in val:
                raise TypeError("Each new column must be a dict with a 'type' key containing a polars.DataType")
            dtype = val["type"]
            desc = val.get("description", "")
            new_columns_dict[col_name] = (dtype, desc)

        # ------------------------------------------------------------------
        # Build Structify `Property` objects for existing & new columns
        # ------------------------------------------------------------------
        pre_existing_properties = [
            Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype))
            for col_name, dtype in existing_schema_dict.items()
        ]

        new_column_properties = [
            Property(name=col_name, description=desc, prop_type=dtype_to_structify_type(dtype))
            for col_name, (dtype, desc) in new_columns_dict.items()
        ]

        all_properties = merge_column_properties(pre_existing_properties, new_column_properties)

        dataset_name = f"enhance_{dataframe_name}_{uuid.uuid4().hex}"
        self._client.datasets.create(
            name=dataset_name,
            description="",
            tables=[
                TableParam(
                    name=dataframe_name,
                    description=dataframe_description,
                    properties=all_properties,
                )
            ],
            relationships=[],
            ephemeral=True,
        )
        # For new columns, add a null value to the dataframe with proper types
        missing_new_columns = [col_name for col_name in new_columns_dict.keys() if col_name not in existing_schema_dict]
        if missing_new_columns:
            df = df.with_columns(
                [pl.lit(None, dtype=new_columns_dict[col_name][0]).alias(col_name) for col_name in missing_new_columns]
            )

        # Get the node ID when the function is called, not when the batch is processed
        node_id = get_node_id()

        # Create the expected output schema
        expected_schema = properties_to_schema(all_properties)

        # Apply Structify enrich on the dataframe
        def enhance_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            if batch_df.is_empty():
                return pl.DataFrame(schema=expected_schema)
            # 1. Add all the entities to the structify dataset
            column_schema = {col["name"]: col["name"] for col in all_properties}
            entities = dataframe_to_entities(batch_df, dataframe_name, column_schema)

            # We add individually instead of batched to maintain the mapping between entity and ID (Same as in enhance_relationships)
            entity_id_to_entity: Dict[str, EntityParam] = {}

            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                add_futures = [executor.submit(self._add_single_entity, dataset_name, entity) for entity in entities]
                for future in tqdm(
                    as_completed(add_futures), total=len(add_futures), desc=f"Adding {dataframe_name} entities"
                ):
                    entity_id, entity = future.result()
                    entity_id_to_entity[entity_id] = entity

            # 2. Enhance the entities
            def enhance_entity_property(
                structify_entity_id: str, entity_param: EntityParam, col_names: List[str]
            ) -> None:
                self._client.structure.run_async(
                    dataset=dataset_name,
                    source={
                        "web": SourceWebWeb(
                            banned_domains=[],
                            starting_searches=[],
                            starting_urls=[],
                        ),
                    },
                    node_id=node_id,
                    save_requirement=[
                        RequiredEntity(
                            seeded_entity_id=int(0),
                            entity_id=structify_entity_id,
                        ),
                        RequiredProperty(
                            property_names=col_names,
                            table_name=dataframe_name,
                        ),
                    ],
                    seeded_entity=KnowledgeGraphParam(
                        entities=[
                            EntityParam(
                                id=int(0),
                                properties=entity_param["properties"],
                                type=dataframe_name,
                            ),
                        ],
                        relationships=[],
                    ),
                    stop_config=StopConfig(max_steps_without_save=max_steps_override) if max_steps_override else None,
                )

            property_list = list(new_columns_dict.keys())
            if len(property_list) == 1:
                property_names = property_list[0]
            elif len(property_list) == 2:
                property_names = f"{property_list[0]} and {property_list[1]}"
            else:
                property_names = f"{', '.join(property_list[:-1])}, and {property_list[-1]}"
            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                futures: List[Future[None]] = []
                # Iterate through property name at the outer level for queueing so with large requests
                # we can skip later jobs if the earlier ones get extra properties.
                for property_name in property_list:
                    futures += [
                        executor.submit(enhance_entity_property, entity_id, entity_param, [property_name])
                        for entity_id, entity_param in entity_id_to_entity.items()
                    ]
                for future in tqdm(
                    as_completed(futures), total=len(futures), desc=f"Preparing enrichments for {property_names}"
                ):
                    future.result()  # Wait for completion
            # 3. Wait for all jobs to complete
            title = f"Enriching {property_names} for {dataframe_name}"
            self._client.jobs.wait_for_jobs(dataset_name=dataset_name, title=title, node_id=node_id)
            # 4. Collect the results
            results = [
                entity.properties
                for entity in self._client.datasets.view_table(dataset=dataset_name, name=dataframe_name)
            ]
            # 5. Return the results
            return pl.DataFrame(results, schema=expected_schema)

        return df.map_batches(enhance_batch, schema=expected_schema, no_optimizations=True)

    def enhance_relationships(
        self,
        *,
        lazy_df: LazyFrame,
        relationship_name: str,
        relationship_description: str,
        target_table_name: str,
        target_schema: Dict[str, Dict[str, Any]],
        target_schema_override: TableParam | None = None,
        source_table_name: str = "source_table",
        max_steps_override: int | None = None,
    ) -> LazyFrame:
        """
        Enhance a LazyFrame by finding related entities and creating a one-to-many relationship.

        Args:
            lazy_df: LazyFrame containing source entities
            relationship_name: Name of the relationship to create
            relationship_description: Description of the relationship to create
            target_table_name: Name of the target table for related entities
            target_schema: Schema definition for target entities, format: {"column_name": {"description": "...", "type": polars_dtype}}
            target_schema_override: Optional override for the target table schema (e.g. to add merge criteria)
            source_table_name: Name of the source table for related entities (e.g. "Company", "Person", etc.) (default: "source_table")

        Returns:
            LazyFrame with original columns plus new columns from related entities
        """
        input_schema = lazy_df.collect_schema()

        target_columns: dict[str, pl.DataType] = {}
        if target_schema_override:
            for prop in target_schema_override["properties"]:
                target_columns[prop["name"]] = structify_type_to_polars_dtype(prop.get("prop_type"))
        else:
            for col_name, col_info in target_schema.items():
                target_columns[col_name] = col_info.get("type", pl.String())

        output_schema = _merge_schema_with_suffix(input_schema, target_columns, suffix=target_table_name)

        target_properties: list[Property] = [
            Property(
                name=col_name,
                description=col_info.get("description", ""),
                prop_type=dtype_to_structify_type(col_info.get("type", pl.String())),
            )
            for col_name, col_info in target_schema.items()
        ]

        node_id = get_node_id()  # Wait until we update relationship endpoint to use node_id

        def enhance_relationship_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            if batch_df.is_empty():
                return pl.DataFrame(schema=output_schema)

            # Create dataset for this batch
            dataset_name = f"enhance_relationships_{relationship_name}_{uuid.uuid4().hex}"

            # Create source table properties from existing schema
            source_properties = [
                Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype))
                for col_name, dtype in input_schema.items()
            ]

            self._client.datasets.create(
                name=dataset_name,
                description="",
                tables=[
                    TableParam(
                        name=source_table_name,
                        description="Source entities for relationship enhancement",
                        properties=source_properties,
                    ),
                    TableParam(
                        name=target_table_name,
                        description=f"Target entities for {relationship_name} relationship",
                        properties=target_properties,
                    ),
                ],
                relationships=[
                    CreateRelationshipParam(
                        name=relationship_name,
                        description=relationship_description,
                        source_table=source_table_name,
                        target_table=target_table_name,
                        properties=[],
                    )
                ],
                ephemeral=True,
            )

            # Add source entities to dataset
            column_schema = {col_name: col_name for col_name in input_schema.names()}
            entities = dataframe_to_entities(batch_df, source_table_name, column_schema)

            # Add entities in batches to avoid JSON payload size issues
            entity_ids: List[str] = []
            entity_batches = chunk_entities_for_parallel_add(entities)

            def add_batch(batch: List[KnowledgeGraphParam]) -> List[str]:
                return self._client.entities.add_batch(
                    dataset=dataset_name,
                    entity_graphs=batch,
                )

            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                futures = [executor.submit(add_batch, batch) for batch in entity_batches]
                for future in tqdm(as_completed(futures), total=len(futures), desc=f"Preparing {source_table_name}"):
                    batch_entity_ids = future.result()
                    entity_ids.extend(batch_entity_ids)

            # Enhance relationships for each entity
            def enhance_relationship(entity_id: str) -> None:
                self._client.structure.enhance_relationship(
                    entity_id=entity_id,
                    relationship_name=relationship_name,
                    stop_config=StopConfig(max_steps_without_save=max_steps_override) if max_steps_override else None,
                    node_id=node_id,
                )

            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                futures = [executor.submit(enhance_relationship, entity_id) for entity_id in entity_ids]  # type: ignore
                for future in tqdm(
                    as_completed(futures), total=len(futures), desc=f"Preparing {relationship_name} enrichments"
                ):
                    future.result()  # Wait for completion

            # Wait for all relationship enhancement jobs to complete
            title = f"Finding {relationship_name} for {source_table_name}"
            self._client.jobs.wait_for_jobs(dataset_name=dataset_name, title=title, node_id=node_id)

            response = self._client.datasets.view_tables_with_relationships(
                dataset=dataset_name, name=source_table_name
            )

            result_rows: list[dict[str, Any]] = []

            # A little caching to avoid looking up the same entity multiple times
            source_entity_id_to_entity = {entity.id: entity for entity in response.entities}
            for relationship in response.relationships:
                target_entity = next(
                    (entity for entity in response.connected_entities if entity.id == relationship.to_id), None
                )
                source_entity = source_entity_id_to_entity.get(relationship.from_id)

                if target_entity and source_entity:
                    result_row: dict[str, Any] = cast(dict[str, Any], source_entity.properties.copy())
                    for prop_name in target_schema.keys():
                        eff = (
                            prop_name if prop_name not in input_schema else f"{prop_name}_{target_table_name}"
                        )  # If the column already exists in the input schema, we need to suffix it with the target table name
                        result_row[eff] = target_entity.properties.get(prop_name)
                    result_rows.append(result_row)

            # Handle source rows without relationships
            source_ids_with_relationships = {rel.from_id for rel in response.relationships}
            for source_id, source_entity in source_entity_id_to_entity.items():
                if source_id not in source_ids_with_relationships:
                    orphan_row: dict[str, Any] = cast(dict[str, Any], source_entity.properties.copy())
                    for prop_name in target_schema.keys():
                        eff = prop_name if prop_name not in input_schema else f"{prop_name}_{target_table_name}"
                        orphan_row[eff] = None
                    result_rows.append(orphan_row)

            if not result_rows:
                return pl.DataFrame(schema=output_schema)

            return pl.DataFrame(result_rows, schema=output_schema)

        return lazy_df.map_batches(enhance_relationship_batch, schema=output_schema, no_optimizations=True)

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
        """
        Enhance one or more columns of a `LazyFrame` directly from a URL.
        """

        # Existing columns & their dtypes from the LazyFrame
        existing_schema_dict: Dict[str, pl.DataType] = df.collect_schema()

        # Normalise to Dict[str, Tuple[dtype, description]]
        new_columns_dict: Dict[str, tuple[pl.DataType, str]] = {}
        for col_name, val in new_columns.items():
            if "type" not in val:
                raise TypeError("Each new column must be a dict with a 'type' key containing a polars.DataType")
            dtype = val["type"]
            desc = val.get("description", "")
            new_columns_dict[col_name] = (dtype, desc)

        # ------------------------------------------------------------------
        # Build Structify `Property` objects for existing & new columns
        # ------------------------------------------------------------------
        pre_existing_properties = [
            Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype))
            for col_name, dtype in existing_schema_dict.items()
        ]

        new_column_properties = [
            Property(name=col_name, description=desc, prop_type=dtype_to_structify_type(dtype))
            for col_name, (dtype, desc) in new_columns_dict.items()
        ]

        all_properties = merge_column_properties(pre_existing_properties, new_column_properties)

        dataset_name = f"enhance_{dataframe_name}_{uuid.uuid4().hex}"
        self._client.datasets.create(
            name=dataset_name,
            description="",
            tables=[
                TableParam(
                    name=dataframe_name,
                    description=dataframe_description,
                    properties=all_properties,
                )
            ],
            relationships=[],
            ephemeral=True,
        )

        # For new columns, add a null value to the dataframe with proper types
        missing_new_columns = [col_name for col_name in new_columns_dict.keys() if col_name not in existing_schema_dict]
        if missing_new_columns:
            df = df.with_columns(
                [pl.lit(None, dtype=new_columns_dict[col_name][0]).alias(col_name) for col_name in missing_new_columns]
            )

        # Get the node ID when the function is called, not when the batch is processed
        node_id = get_node_id()

        # Create the expected output schema
        expected_schema = properties_to_schema(all_properties)

        # Apply Structify scrape on the dataframe
        def scrape_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            if batch_df.is_empty():
                return pl.DataFrame(schema=expected_schema)

            # 1. Add all the entities to the structify dataset
            batch_df = batch_df.drop_nulls(subset=[url_column]).unique()
            column_schema = {col["name"]: col["name"] for col in all_properties}
            entities = dataframe_to_entities(batch_df, dataframe_name, column_schema, zero_ids=True)

            # We add individually instead of batched to maintain the mapping between entity and ID
            # This can be changed later if we make an endpoint for scrape single properties that
            # just takes in entity id and property names
            entity_id_to_entity: Dict[str, EntityParam] = {}

            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                add_futures = [executor.submit(self._add_single_entity, dataset_name, entity) for entity in entities]
                for future in tqdm(
                    as_completed(add_futures), total=len(add_futures), desc=f"Adding {dataframe_name} entities"
                ):
                    entity_id, entity = future.result()
                    entity_id_to_entity[entity_id] = entity

            # 2. Run scrape jobs for each entity
            def scrape_entity_property(entity_id: str) -> None:
                entity = entity_id_to_entity[entity_id]
                url = entity["properties"].get(url_column)
                if url is None:
                    return
                if not isinstance(url, str):
                    raise TypeError(
                        f"URL column {url_column} must be of string type, got {type(entity['properties'][url_column])}"
                    )

                self._client.scrape.scrape(
                    dataset_name=dataset_name,
                    extraction_criteria=[
                        RequiredProperty(
                            table_name=dataframe_name,
                            property_names=[p["name"] for p in new_column_properties],
                        ),
                        RequiredEntity(
                            seeded_entity_id=0,
                            entity_id=entity_id,
                        ),
                    ],
                    seeded_kg=KnowledgeGraphParam(entities=[entity], relationships=[]),
                    node_id=node_id,
                    stop_config=None,
                    use_proxy=use_proxy,
                    url=url,
                )

            property_list = list(new_columns_dict.keys())
            if len(property_list) == 1:
                property_names = property_list[0]
            elif len(property_list) == 2:
                property_names = f"{property_list[0]} and {property_list[1]}"
            else:
                property_names = f"{', '.join(property_list[:-1])}, and {property_list[-1]}"

            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                scrape_futures = [
                    executor.submit(scrape_entity_property, entity_id) for entity_id in entity_id_to_entity.keys()
                ]
                for future in tqdm(
                    as_completed(scrape_futures),
                    total=len(scrape_futures),
                    desc=f"Preparing scrapes for {property_names}",
                ):
                    future.result()  # Wait for completion

            # 3. Wait for all jobs to complete
            title = f"Scraping {property_names} for {dataframe_name}"
            self._client.jobs.wait_for_jobs(dataset_name=dataset_name, title=title, node_id=node_id)

            # 4. Collect the results
            results = [
                entity.properties
                for entity in self._client.datasets.view_table(dataset=dataset_name, name=dataframe_name)
            ]

            # 5. Return the results
            return pl.DataFrame(results, schema=expected_schema)

        return df.map_batches(scrape_batch, schema=expected_schema, no_optimizations=True)

    def scrape_relationships(
        self,
        *,
        lazy_df: LazyFrame,
        url_column: str,
        table_name: str,
        scrape_schema: Dict[str, Dict[str, Any]],
        scrape_schema_override: TableParam | None = None,
        original_column_map: Dict[str, str] = {},
        source_table_name: str = "source_table",
        relationship_name: str = "scraped",
        relationship_description: str = "",
        use_proxy: bool = False,
    ) -> LazyFrame:
        """
        Scrape data from URLs in a LazyFrame column and return structured results, with a column `source_url` that contains the original URL.

        Args:
          lazy_df: LazyFrame containing URLs to scrape
          url_column: Name of the column containing URLs (Must exist in the input LazyFrame)
          table_name: Name of the table to scrape. This will be the target table for the relationship.
          scrape_schema: Schema definition with descriptions, format: {"column_name": {"description": "...", "type": polars_dtype}}. If the column name is the same as the table name, it will be suffixed by the table name, e.g. "name_Person"
          original_column_map: Mapping of original column names to new names
        """
        relationship = CreateRelationshipParam(
            name=relationship_name,
            description=relationship_description,
            source_table=source_table_name,
            target_table=table_name,
            properties=[],
        )

        input_schema = lazy_df.collect_schema()

        if url_column not in input_schema:
            raise ValueError(f"Column '{url_column}' not found in LazyFrame")

        if scrape_schema_override:
            scraped_columns: dict[str, pl.DataType] = {}
            for prop in scrape_schema_override["properties"]:
                prop_name = original_column_map.get(prop["name"], prop["name"])
                scraped_columns[prop_name] = structify_type_to_polars_dtype(prop.get("prop_type"))
        else:
            scraped_columns = {
                col_name: col_info.get("type", pl.String()) for col_name, col_info in scrape_schema.items()
            }

        output_schema = _merge_schema_with_suffix(input_schema, scraped_columns, suffix=relationship["target_table"])

        properties: list[Property] = []
        for col_name, col_info in scrape_schema.items():
            polars_type = col_info.get("type", pl.String())
            structify_type = dtype_to_structify_type(polars_type)
            properties.append(
                Property(name=col_name, description=col_info.get("description", ""), prop_type=structify_type)
            )

        dataset_descriptor = DatasetDescriptorParam(
            name=f"scrape_{relationship['target_table']}_{uuid.uuid4().hex}",
            description="",
            tables=[
                TableParam(
                    name=relationship["target_table"],
                    description="",
                    properties=properties,
                ),
                TableParam(
                    name=relationship["source_table"],
                    description="Source entities for relationship enhancement",
                    properties=[
                        Property(
                            name=col_name,
                            description="",
                            prop_type=dtype_to_structify_type(input_schema[col_name]),
                        )
                        for col_name in input_schema.names()
                    ],
                ),
            ],
            relationships=[relationship],
        )

        node_id = get_node_id()

        def scrape_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            # 1. Get the unique URLs in the batch
            entities = batch_df.drop_nulls(subset=[url_column]).unique().to_dicts()

            # 2. Scrape the URLs
            def scrape_entity(entity: Dict[str, Any]) -> None:
                entity_clean = {k: v for k, v in entity.items() if v is not None}
                self._client.scrape.list(
                    table_name=relationship["target_table"],
                    dataset_name=dataset_descriptor["name"],
                    input={
                        "related": {
                            "relationship_name": relationship["name"],
                            "source_entity": {
                                "id": 1,
                                "properties": entity_clean,
                                "type": relationship["source_table"],
                            },
                            "source_url_column": url_column,
                        }
                    },
                    dataset_descriptor=dataset_descriptor,
                    node_id=node_id,
                    use_proxy=use_proxy,
                )

            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                futures = [executor.submit(scrape_entity, entity) for entity in entities]
                for future in tqdm(
                    as_completed(futures),
                    total=len(futures),
                    desc=f"Preparing to scrape websites for {relationship['target_table']}",
                ):
                    future.result()  # Wait for completion

            # Wait for all scraping jobs to complete
            title = f"Scraping websites for {relationship['target_table']}"
            self._client.jobs.wait_for_jobs(dataset_name=dataset_descriptor["name"], title=title, node_id=node_id)

            offset = 0
            LIMIT = 999
            result_rows: list[dict[str, Any]] = []
            while True:
                try:
                    response = self._client.datasets.view_tables_with_relationships(
                        dataset=dataset_descriptor["name"],
                        name=relationship["target_table"],
                        limit=LIMIT,
                        offset=offset,
                    )
                    for scraped_entity in response.entities:
                        rel = next((rel for rel in response.relationships if rel.to_id == scraped_entity.id), None)
                        if rel:
                            related_entity = next(
                                (e for e in response.connected_entities if e.id == rel.from_id),
                                None,
                            )
                            if related_entity:
                                result_row: dict[str, Any] = {
                                    **scraped_entity.properties,
                                    url_column: related_entity.properties[url_column],
                                }
                                result_rows.append(result_row)
                    offset += LIMIT
                    if len(response.entities) < LIMIT:
                        break
                except Exception:
                    break
            # Build scraped schema (pre-join, original names) incl. join column
            scraped_schema = scraped_columns | {url_column: input_schema[url_column]}

            # Fill missing columns in scraped results
            for result_row in result_rows:
                for col_name in scraped_schema.keys():
                    if col_name not in result_row:
                        result_row[col_name] = None
            scraped_df = pl.DataFrame(result_rows, schema=scraped_schema)

            joined_df = batch_df.join(scraped_df, on=url_column, how="left", suffix=f"_{relationship['target_table']}")
            return joined_df

        return lazy_df.map_batches(scrape_batch, schema=output_schema, no_optimizations=True)

    def scrape_urls(
        self,
        *,
        lazy_df: LazyFrame,
        url_column: str,
        table_name: str,
        scrape_schema: Dict[str, Dict[str, Any]],
        scrape_schema_override: TableParam | None = None,
        original_column_map: Dict[str, str] = {},
        use_proxy: bool = False,
    ) -> LazyFrame:
        """
        DEPRECATED: Use `scrape_relationships` instead.
        """
        return self.scrape_relationships(
            lazy_df=lazy_df,
            url_column=url_column,
            table_name=table_name,
            scrape_schema=scrape_schema,
            scrape_schema_override=scrape_schema_override,
            original_column_map=original_column_map,
            use_proxy=use_proxy,
        )

    def structure_pdfs(
        self,
        *,
        document_paths: LazyFrame,
        path_column: str,
        table_name: str,
        schema: Dict[str, Dict[str, Any]],
    ) -> LazyFrame:
        """
        Extract structured data from PDF documents and return as a LazyFrame.

        Args:
        document_paths: LazyFrame containing a column with paths to the PDF documents to process
        path_column: Name of the column containing PDF file paths
        table_name: Name of the table for the structured data
        schema: Schema definition with descriptions, format: {"column_name": {"description": "...", "type": polars_dtype}}

        Returns:
        LazyFrame: Structured data extracted from the PDFs
        """
        polars_schema = pl.Schema(
            [(path_column, pl.String())]
            + [(col_name, col_info.get("type", pl.String())) for col_name, col_info in schema.items()]
        )

        assert path_column in document_paths.collect_schema(), (
            f"Path column {path_column} must be in the input dataframe, got {document_paths.collect_schema()}"
        )

        table_param = as_table_param(table_name, polars_schema)

        node_id = get_node_id()

        def structure_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            # Get unique PDF paths in the batch
            batch_paths = batch_df.select(path_column).drop_nulls(subset=[path_column]).unique().to_series().to_list()

            # Process each PDF document
            path_to_dataset: dict[str, str] = {}
            job_ids: list[str] = []

            def process_pdf(pdf_path: str) -> Tuple[str, str, str]:
                dataset_name = f"structure_pdfs_{table_name}_{uuid.uuid4().hex}"

                # Create dataset for this PDF
                self._client.datasets.create(
                    name=dataset_name,
                    description="",
                    tables=[table_param],
                    relationships=[],
                    ephemeral=True,
                )

                # Upload the PDF document
                with open(pdf_path, "rb") as pdf_file:
                    self._client.documents.upload(
                        content=pdf_file,
                        file_type="PDF",
                        dataset=dataset_name,
                        path=f"{dataset_name}.pdf".encode(),
                    )

                job_id = self._client.structure.run_async(
                    dataset=dataset_name,
                    source=SourcePdf(pdf={"path": f"{dataset_name}.pdf"}),
                    node_id=node_id,
                )
                return job_id, str(pdf_path), dataset_name

            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                futures = [executor.submit(process_pdf, pdf_path) for pdf_path in batch_paths]
                for future in tqdm(as_completed(futures), total=len(futures), desc="Preparing PDFs"):
                    job_id, pdf_path, dataset_name = future.result()
                    job_ids.append(job_id)
                    path_to_dataset[pdf_path] = dataset_name

            # Wait for all PDF processing jobs to complete
            self._client.jobs.wait_for_jobs(job_ids=job_ids, title=f"Parsing {table_name} from PDFs", node_id=node_id)

            # Collect results from all processed PDFs
            structured_results: list[dict[str, Any]] = []

            def collect_pdf_results(pdf_path: str, dataset_name: str) -> List[Dict[str, Any]]:
                entities_result = self._client.datasets.view_table(dataset=dataset_name, name=table_name)
                return [{**entity.properties, path_column: pdf_path} for entity in entities_result]

            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                futures = [
                    executor.submit(collect_pdf_results, pdf_path, dataset_name)  # type: ignore
                    for pdf_path, dataset_name in path_to_dataset.items()
                ]
                for future in tqdm(as_completed(futures), total=len(futures), desc="Collecting PDF extractions"):
                    results = future.result()
                    structured_results.extend(results)

            # Ensure all columns are present with None for missing values
            for result_row in structured_results:
                for col_name in polars_schema.names():
                    if col_name not in result_row:
                        result_row[col_name] = None

            # Create DataFrame with structured results
            if not structured_results:
                structured_df = pl.DataFrame(
                    {col: pl.Series([], dtype=polars_schema[col]) for col in polars_schema.names()}
                )
            else:
                structured_df = pl.DataFrame(structured_results, schema=polars_schema)

            # Join with original batch to preserve any additional columns
            joined_df = batch_df.join(structured_df, on=path_column, how="left")
            return joined_df

        return document_paths.map_batches(structure_batch, schema=polars_schema, no_optimizations=True)

    def tag(
        self,
        *,
        df: LazyFrame,
        new_property_name: str,
        dtype: pl.DataType,
        instructions: str,
        dataframe_name: str,
        dataframe_description: str,
    ) -> LazyFrame:
        """
        Tag entities in a LazyFrame by deriving a new property value based on all existing properties.

        This function uses the derive endpoint to generate new property values based on all existing
        properties in each row, using the provided instructions.

        Args:
            df: The input `polars.LazyFrame` to tag.
            new_property_name: Name of the new property to derive.
            dtype: Polars DataType for the new property (e.g. pl.String(), pl.Int64()).
            instructions: Instructions for how to derive the new property value.
            dataframe_name: Logical name of the dataframe (e.g. "Company", "Invoice").
            dataframe_description: Description providing context for the dataframe.

        Returns:
            LazyFrame with the original columns plus the new derived property column.
        """
        # Existing columns & their dtypes from the LazyFrame
        existing_schema_dict: Dict[str, pl.DataType] = df.collect_schema()

        # Build Structify `Property` objects for existing columns
        existing_properties = [
            Property(name=col_name, description="", prop_type=dtype_to_structify_type(col_dtype))
            for col_name, col_dtype in existing_schema_dict.items()
        ]

        # Add the new property to derive
        new_property = Property(
            name=new_property_name, description=instructions, prop_type=dtype_to_structify_type(dtype)
        )

        all_properties = existing_properties + [new_property]

        dataset_name = f"tag_{dataframe_name}_{uuid.uuid4().hex}"
        self._client.datasets.create(
            name=dataset_name,
            description="",
            tables=[
                TableParam(
                    name=dataframe_name,
                    description=dataframe_description,
                    properties=all_properties,
                )
            ],
            relationships=[],
            ephemeral=True,
        )

        # Add the new column with null values and proper type
        df = df.with_columns([pl.lit(None, dtype=dtype).alias(new_property_name)])

        node_id = get_node_id()

        # Create the expected output schema
        expected_schema = properties_to_schema(all_properties)

        # Apply Structify derive on the dataframe
        def tag_batch(batch_df: pl.DataFrame) -> pl.DataFrame:
            if batch_df.is_empty():
                return pl.DataFrame(schema=expected_schema)

            # 1. Add all the entities to the structify dataset
            column_schema = {col["name"]: col["name"] for col in all_properties}
            entities = dataframe_to_entities(batch_df, dataframe_name, column_schema)

            # Add entities in batches to avoid JSON payload size issues
            entity_ids: List[str] = []
            entity_batches = chunk_entities_for_parallel_add(entities)

            def add_batch(batch: List[KnowledgeGraphParam]) -> List[str]:
                return self._client.entities.add_batch(
                    dataset=dataset_name,
                    entity_graphs=batch,
                )

            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                add_futures = [executor.submit(add_batch, batch) for batch in entity_batches]
                for future in tqdm(
                    as_completed(add_futures), total=len(add_futures), desc=f"Preparing {dataframe_name}"
                ):
                    batch_entity_ids = future.result()
                    entity_ids.extend(batch_entity_ids)

            # 2. Derive the new property for each entity
            def derive_entity_property(entity_id: str) -> None:
                self._client.entities.derive(
                    dataset=dataset_name,
                    entity_id=entity_id,
                    derived_property=new_property_name,
                    instructions=instructions,
                    node_id=node_id,
                )

            with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
                futures = [executor.submit(derive_entity_property, entity_id) for entity_id in entity_ids]
                for future in tqdm(
                    as_completed(futures), total=len(futures), desc=f"Preparing {new_property_name} tags"
                ):
                    future.result()  # Wait for completion

            # 3. Collect the results
            title = f"Tagging {new_property_name} for {dataframe_name}"
            self._client.jobs.wait_for_jobs(dataset_name=dataset_name, title=title, node_id=node_id)
            results = [
                entity.properties
                for entity in self._client.datasets.view_table(dataset=dataset_name, name=dataframe_name)
            ]

            # 4. Return the results
            return pl.DataFrame(results, schema=expected_schema)

        return df.map_batches(tag_batch, schema=expected_schema, no_optimizations=True)


class PolarsResourceWithRawResponse:
    def __init__(self, dataframe: PolarsResource) -> None:
        self._dataframe = dataframe

        self.enhance_columns = to_raw_response_wrapper(
            dataframe.enhance_columns,
        )
        self.tag = to_raw_response_wrapper(
            dataframe.tag,
        )


class PolarsResourceWithStreamingResponse:
    def __init__(self, dataframe: PolarsResource) -> None:
        self._dataframe = dataframe

        self.enhance_columns = to_streamed_response_wrapper(
            dataframe.enhance_columns,
        )
        self.tag = to_streamed_response_wrapper(
            dataframe.tag,
        )


def get_node_id() -> Optional[str]:
    """
    Helper function to get node_id from STRUCTIFY_NODE_ID environment variable.

    Returns:
      The node ID from environment variable if available, otherwise None.
    """
    return os.environ.get("STRUCTIFY_NODE_ID")


def merge_column_properties(
    existing_properties: List[Property],
    new_properties: List[Property],
) -> List[Property]:
    """
    Merge existing and new column properties, taking the union of columns.

    If a column exists in both existing and new properties with different types,
    raises a helpful error message indicating the type mismatch.

    Args:
        existing_properties: Properties from existing DataFrame columns
        new_properties: Properties for new columns to add

    Returns:
        List of merged properties with new properties taking precedence for existing columns

    Raises:
        ValueError: If a column exists in both with different types
    """
    # Start with a copy of existing properties (so we add new properties on the right)
    all_properties = existing_properties.copy()

    # Add new properties that aren't in existing properties
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
                break
        else:
            # Add new property since it's not in properties yet
            all_properties.append(new_prop)

    return all_properties


def chunk_entities_for_parallel_add(
    entities: list[EntityParam], batch_size: int = 100
) -> list[list[KnowledgeGraphParam]]:
    """
    Chunk entities into batches to avoid JSON payload size issues.
    Each entity gets its own KnowledgeGraph, but we group them into batches for API calls.

    Args:
        entities: List of entities to chunk
        batch_size: Maximum number of KnowledgeGraphs per batch (default: 100)

    Returns:
        List of batches, where each batch is a list of KnowledgeGraphParam objects
    """
    # Handle empty input
    if not entities:
        return []

    # Convert each entity to its own KnowledgeGraph
    knowledge_graphs: list[KnowledgeGraphParam] = [
        {"entities": [EntityParam(type=entity["type"], id=0, properties=entity["properties"])], "relationships": []}
        for entity in entities
    ]

    # Chunk the KnowledgeGraphs into batches
    batches: list[list[KnowledgeGraphParam]] = []
    for i in range(0, len(knowledge_graphs), batch_size):
        batch = knowledge_graphs[i : i + batch_size]
        batches.append(batch)

    return batches


def dataframe_to_entities(
    batch_df: pl.DataFrame, entity_type: str, column_schema: Dict[str, str], zero_ids: bool = False
) -> list[EntityParam]:
    """Convert DataFrame rows to EntityParam objects, filtering out null values."""
    return [
        EntityParam(
            type=entity_type,
            id=i if not zero_ids else 0,
            properties={
                prop_name: str(row[col_name])
                for col_name, prop_name in column_schema.items()
                if row[col_name] is not None
            },
        )
        for i, row in enumerate(batch_df.to_dicts())
    ]


def dtype_to_structify_type(dtype: pl.DataType) -> PropertyTypeParam:
    """
    Convert a Polars dtype to a Structify type.
    Map a Polars dtype to a Structify PropertyTypeParam.

    Args:
        dtype: The Polars data type to convert.

    Returns:
        The corresponding Structify PropertyTypeParam value.

    Notes:
        - Defaults to PropertyTypeParam.STRING for unknown types.
        - This mapping is intentionally explicit to avoid silent mismatches as Structify and Polars evolve.
    """
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
    """Convert a list of Structify properties to a Polars schema."""
    return pl.Schema({prop["name"]: structify_type_to_polars_dtype(prop.get("prop_type")) for prop in properties})


def _merge_schema_with_suffix(
    input_schema: pl.Schema,
    new_columns: dict[str, pl.DataType],
    *,
    suffix: str,
) -> pl.Schema:
    """Merge *new_columns* into *input_schema*.

    If a column already exists in *input_schema*, the column name gets
    `_<suffix>` appended to avoid collisions.

    Returns the merged Polars schema.
    """

    merged: dict[str, pl.DataType] = dict(input_schema)
    for col, dtype in new_columns.items():
        effective = col if (col not in input_schema) else f"{col}_{suffix}"
        merged[effective] = dtype

    return pl.Schema(merged)


def as_table_param(table_name: str, schema: pl.Schema) -> TableParam:
    return TableParam(
        name=table_name,
        description="",
        properties=[
            Property(name=col_name, description="", prop_type=dtype_to_structify_type(dtype))
            for col_name, dtype in schema.items()
        ],
    )


class Relationship(TypedDict):
    name: str
    description: Optional[str]
    source_table: str
    target_table: str
