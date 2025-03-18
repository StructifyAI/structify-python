Viewing Your Datasets
=====================

.. _view-dataset:

Viewing Tables & Relationships
-----------------------------
Structify provides several methods to view the contents of your datasets:

View a Single Table
~~~~~~~~~~~~~~~~~~
To view the contents of a specific table in your dataset:

.. code-block:: python
    
    table_data = structify.datasets.view_table(
        dataset="startups",
        name="founder"
    )

    for row in table_data:
        print(row)

For each row, you'll be able to view its ID, creation time, type, and properties.

View Relationships
~~~~~~~~~~~~~~~~
To view specific relationships in your dataset:

.. code-block:: python

    relationships = structify.datasets.view_relationships(
        dataset="startups",
        name="founded"
    )

    for relationship in relationships:
        print(relationship)

For each relationship, you'll be able to view its source ID, target ID, creation time, type, and properties.

View Tables with Their Relationships
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To view tables along with their associated relationships:

.. code-block:: python

    founder_details = structify.datasets.view_tables_with_relationships(
        dataset="startups",
        name="founder"
    )

    """
    The response will be an object with three keys, as such:
     first list contains the table data you'd expect from view_table
     the second contains the relationship data you'd expect from view_relationships
     the third contains the table data of the connected table for all the relationships
    """
    founders = founder_details.entities
    relationships = founder_details.relationships
    connected_entities = founder_details.connected_entities

.. tip::
    
    All viewing methods support optional parameters for pagination and sorting:
    
    - ``limit``: Maximum number of results to return
    - ``offset``: Number of results to skip
    - ``sort_by``: Field to sort results by
    - ``last_updated``: Filter by last update time
    - ``job_id``: Filter by specific job ID


Viewing Detailed Entity Information
--------------------------------
Structify provides two methods to get detailed information about specific entities:

Get Entity Details
~~~~~~~~~~~~~~~~
To retrieve basic information about a specific entity:

.. code-block:: python

    entity = structify.entities.get(
        id="entity_123",
        resolve_id=True  # Optional: Resolve any ID references for entities that were merged
    )

    print(entity)  # Shows entity details including ID, type, and properties

View Entity with Relationships
~~~~~~~~~~~~~~~~~~~~~~~~~~~
To get a comprehensive view of an entity including its relationships:

.. code-block:: python

    entity_view = structify.entities.view(
        id="entity_123",
        resolve_id=True  # Optional: Resolve any ID references
    )

    print(entity_view)  # Shows entity details with associated relationships

The difference between ``get`` and ``view``:
 - ``get`` returns basic entity information
 - ``view`` returns entity information along with its relationships and connected entities

.. tip::
    Both methods support the optional ``resolve_id`` parameter which, when set to ``True``, 
    will resolve any ID conflicts from merging entities to their full entity information.
