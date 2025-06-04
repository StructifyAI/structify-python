import asyncio
from typing import Optional

import pandas as pd

from structify import AsyncStructify
from structify.types import Table, Entity, Property, KnowledgeGraph


async def enhance_column(
    client: AsyncStructify,
    df: pd.DataFrame,
    column_name: str,
    column_description: str,
    table_name: Optional[str] = None,
    table_description: Optional[str] = None,
) -> pd.DataFrame:
    if df.index.name is None:
        raise ValueError("DataFrame must have an index name")
    column_names = df.columns.values.tolist()
    if column_name not in column_names:
        column_names.append(column_name)
    dataset_name = f"enhance_{column_name}"
    await client.datasets.create(
        name=dataset_name,
        description=f"Enhanced {column_name} column",
        tables=[
            Table(
                name=table_name,
                description=table_description,
                properties=[Property(name=name, description=f"Enhanced {name} column") for name in column_names],
            )
        ],
    )
    entity_ids = await client.entities.add_batch(
        dataset=dataset_name,
        entity_graph=KnowledgeGraph(
            entities=[
                Entity(
                    id=str(index),
                    properties={column_name: str(value)},
                )
                for index, value in df[column_name].items()
            ]
        ),
    )

    async def enhance_and_wait(entity_id):
        job_id = await client.structure.enhance_property(
            entity_id=entity_id,
            property_name=column_name,
            allow_extra_entities=True,
            special_job_type="HumanLLM",
            starting_searches=[column_description],
        )
        await client.jobs.wait(job_id)
        return job_id

    await asyncio.gather(*(enhance_and_wait(entity_id) for entity_id in entity_ids))

    entities = await client.datasets.view_table(dataset=dataset_name, name=table_name)
    data = [ {col: entity.properties.get(col) for col in column_names} for entity in entities ]
    return pd.DataFrame(data, columns=column_names)
