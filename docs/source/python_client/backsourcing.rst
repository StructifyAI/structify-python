.. _backsourcing:

Backsourcing
============
For all our users, knowing that you have accurate data is of paramount importance, so we allow you to see the sources that were used to validate and create any given datapoint. This is useful for understanding the provenance of a given datapoint and for understanding the context in which it was created.

To use this endpoint, you need to know the ids of a given datapoint. In order to find that information, you would need to call the ``structify.datasets.view`` endpoint. 

After calling that endpoint, you will receive a Python object containing information about the entity like the below:
``Entity(id='Entity-ea121d6f-6261-460d-a899-686fb067524c', label='company', properties={'name': 'Structify'})``

To then find the sources that were used to create this entity, you would call the ``structify.sources.list`` endpoint as so:

.. code-block:: python

    print(structify.sources.list(id='Entity-ea121d6f-6261-460d-a899-686fb067524c'))

This call would result a Python object including the id, as follows:

.. code-block:: python
    
    [
        Source(
            id='Source-1aafc4a0-fd36-44e1-af5c-4ac63300a891',
            link=Web(url='https://www.structify.ai/'), 
            location=Visual(Position(x=0, y=500))
        ),
        Source(
            id='Source-92472065-1881-449a-875a-41aab8351bf7',
            link=Web(url='https://github.com/StructifyAI//'), 
            location=Visual(Position(x=0, y=0))
        )
    ]

The location field in the source object is a visual representation of where the data was found on the source. This is useful for understanding the context in which the data was found.
