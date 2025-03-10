Additional Functionality
========================

We currently support a few additional features for our premium users that will help you get the most out of your datasets.

#. :ref:`Searching through Datasets <searching>`
#. :ref:`Summarizing Entity Properties <summarizing>`
#. :ref:`Creating Entity Subgraphs <subgraphs>`


.. _searching:

Searching through Datasets
--------------------------
For our premium users, we automatically embed all of their entities, which means that premium users can access search endpoint that allows you to search through your datasets using natural language. This is useful for when you don't know exactly what you are looking for, but you know some keywords that you want to search for.

In this example, we will search for all companies in our company dataset that are related to "healthcare".

.. code-block:: python

    results = client.entities.search(
        dataset="startups",
        table_name="company",
        query="healthcare"
    )

This will return a list of entities that match the query.

.. _summarizing:

Summarizing Entity Properties
----------------------------
Since we grab information from various sources (especially on the Internet), we often want to collapse all that various information into a single property. Our premium users can use the ``client.entities.summarize`` endpoint to collapse all that various information into a single property.
This is useful for when the exact text of the property is not as important as the general and comprehensive information that we can provide. For example, business descriptions are a great use case for this endpoint.

.. code-block:: python

    summarized_entity = client.entities.summarize(
        dataset="startups",
        entity_id="Entity-ea121d6f-6261-460d-a899-686fb067524c",
        properties=["description"],
        extra_instructions="Please summarize the key value proposition, excluding any extraneous information." # Optional
    )

This will return back an object of the entity with the summarized property.


.. _subgraphs:

Creating Entity Subgraphs
-------------------------

Every now and then, you might want to see the relationships between a group of entities. In these instances, it is helpful to be able to access a subgraph of the entities you are interested in.

For premium users, we support the ability to create entity subgraphs. This will return back a subgraph of the entities you are interested in, which you can then use to answer questions or analyze the data.

.. code-block:: python

    subgraph = client.entities.get_local_subgraph(
        id="Entity-ea121d6f-6261-460d-a899-686fb067524c",
        radius=2
    )

This will return back an object with the neighbors of the entity (including itself) and the relationships between them, as such:

.. code-block:: python

    from collections import defaultdict

    from_relationships = defaultdict(list)
    to_relationships = defaultdict(list)
    neighbors = {n.id: n for n in subgraph.neighbors}

    for r in subgraph.relationships:
        from_relationships[r.from_id].append(r)
        to_relationships[r.to_id].append(r)

    # Assume we have a dataset of just companies and the people that work at them, along with the customers of the companies
    for neighbor in subgraph.neighbors:
        for r in from_relationships[neighbor.id]:
            print(f"{neighbor.properties['name']} works at {neighbors[r.to_id].properties['name']}")
        for r in to_relationships[neighbor.id]:
            print(f"{neighbor.properties['name']} is a customer of {neighbors[r.from_id].properties['name']}")
