Tracking Board Member Changes
======================================

In this tutorial, imagine you are intested in keeping tabs on who is on the board of various private companies.
Let's say furthermore, you are only interested in companies that are in the technology sector.
You want to know who is on the board of any given company, and you want to know when that information changes.

This information is not readily available, but you can determine it by periodically checking company websites, press releases, and SEC filings.
The goal being to regularly check if there have been any changes. Of course, since all the websites "Team" or "About Us" pages are all formatted differently, this is a near impossible task to execute with high accuracy.

Structify allows you to easily collect this information to track any changes.

Step 1: Create a Structify Dataset for Board Members
----------------------------------------------------
Next, we will need to create a dataset to store the board members information. We can do this by defining the schema in tables, properties, and relationships, making sure to include descriptions for each.

.. code-block:: python

    from structify import Structify
    from structify.types import DatasetDescriptor

    client = Structify()

    # We will define the schema we want to use for the dataset using the DatasetDescriptor object
    schema = DatasetDescriptor(
        name="private_tech_company_board_members",
        description="Dataset containing information about board members of private companies in the technology sector.",
        tables=[
            Table(
                name="board_member",
                description="information about board members of private companies in the technology sector",
                properties=[
                    Property(name="name", description="name of the board member"),
                    Property(name="title", description="title of the board member"),
                    Property(name="start_date", description="start date of the board member's tenure"),
                    Property(name="end_date", description="end date of the board member's tenure")
                ]
            ),
            Table(
                name="company",
                description="information about private companies in the technology sector",
                properties=[
                    Property(name="name", description="name of the company"),
                    Property(name="website", description="the url of the company's website")
                ]
            )
        ],
        relationships=[
            Relationship(
                name="sits_on_board",
                description="Company the board member is associated with",
                source_table="board_member",
                target_table="company"
            )
        ]
    )

    # Create the dataset
    client.datasets.create(**schema.to_dict())

.. tip::
    If you want Structify to handle entity resolution of your existing dataset, you will want to specify the merge strategy in the schema.


Step 2: Upload Your Existing Board Members Dataset
--------------------------------------------------
If we want to update the existing dataset that you may have, we will have to add it into Structify. We start that process by creating a helper function to convert a CSV file into a list of ``KnowledgeGraphParam`` objects.

.. code-block:: python

    import csv

    from pathlib import Path
    from typing import List

    from structify.types import DatasetDescriptor, EntityParam, KnowledgeGraphParam


    def kgs_from_csv(filename: str | Path, table_name: str, schema: DatasetDescriptor) -> List[KnowledgeGraphParam]:
        """Helper function to convert a CSV file into a list of KnowledgeGraphParam objects."""
        kgs = []
        with open(filename, "r") as f:
            reader = csv.reader(f)
            # Read header row to get property names
            header = next(reader)

            # Sanity check that the table exists and the property names are in the schema
            if table_name not in [t.name for t in schema.tables]:
                raise ValueError(f"Table {table_name} does not exist in the schema")

            valid_property_names = [p.name for p in next(t for t in schema.tables if t.name == table_name).properties]
            property_names = [prop for prop in header if prop in valid_property_names]
            print(f"Valid property names for table {table_name} in header: {property_names}")

            if len(property_names) != len(header):
                print(f"Property names {header} do not exactly match schema for table {table_name}")

            for row in reader:
                if len(row) != len(property_names):
                    if len(row) >= 1:
                        print(f"Row {row} does not have the correct number of properties, skipping...")
                        continue
                    else:
                        raise ValueError(f"Row {row} does not have any valid properties")

                kgs.append(
                    KnowledgeGraphParam(
                        entities=[
                            EntityParam(
                                id=0,
                                type=table_name,
                                properties={property_names[i]: row[i] for i in range(len(property_names))},
                            )
                        ],
                        relationships=[],
                    )
                )
        return kgs

Then, we'll want to use that helper function to upload the CSV using the ``entities.add`` endpoint.

.. code-block:: python

    for kg in kgs_from_csv("board_members.csv", "board_member", schema):
        client.entities.add(dataset=schema.name, entity_graph=kg)


Step 3: Add in Web Data
------------------------------------------------
Now that we have a dataset to store the board members information, we want to set up agent jobs to enhance the dataset with information from the web.

.. code-block:: python

    for person in client.dataset.view_table(dataset=schema.name, table="board_member"):
        client.structure.enhance_relationship(
            dataset=schema.name,
            entity_id=person.id,
            relationship_name="sits_on_board",
            allow_extra_entities=True
        )
    
    for company in client.dataset.view_table(dataset=schema.name, table="company"):
        client.structure.enhance_relationship(
            dataset=schema.name,
            entity_id=company.id,
            relationship_name="sits_on_board",
            allow_extra_entities=True
        )

By running the above code on a regular basis, you will be able to keep track of the board members of various private companies in the technology sector.
