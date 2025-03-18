.. _backsourcing:

Backsourcing
============
For all our users, knowing that you have accurate data is of paramount importance, so we allow you to see the sources that were used to validate and create any given datapoint. This is useful for understanding where our agent found the information for a given datapoint.

To use this endpoint, you need to know the ids of a given datapoint. In order to find that information, you would need to call the ``structify.datasets.view_table`` endpoint. 

After calling that endpoint, you will receive a Python object containing information about the entity like the below:
``DatasetViewTableResponse(id='Entity-ea121d6f-6261-460d-a899-686fb067524c', label='company', properties={'name': 'Structify'}, creation_time=datetime.datetime(2025, 3, 1, 3, 17, 43, 219881, tzinfo=datetime.timezone.utc))``

To then find the sources that were used to create this entity, you would call the ``structify.sources.list`` endpoint as so:

.. code-block:: python

    print(structify.sources.list(id='Entity-ea121d6f-6261-460d-a899-686fb067524c'))

This call would result in a Python object including the id, as follows:

.. code-block:: python
    
    [
        Source(
            id='Source-1aafc4a0-fd36-44e1-af5c-4ac63300a891',
            link=Web(url='https://www.structify.ai/'),
            location=Visual(Position(x=0, y=500)),
            creation_time=datetime.datetime(2025, 1, 1, 12, 34, 56, 789101, tzinfo=datetime.timezone.utc),
            is_summary=False,
            user_specified=False,
        ),
        Source(
            id='Source-92472065-1881-449a-875a-41aab8351bf7',
            link=Web(url='https://github.com/StructifyAI/'), 
            location=Visual(Position(x=0, y=0)),
            creation_time=datetime.datetime(2025, 1, 1, 22, 47, 7, 398915, tzinfo=datetime.timezone.utc),
            is_summary=False,
            user_specified=False,
        )
    ]

The location field in the source object is a visual representation of where the data was found on the source. This is useful for understanding the context in which the data was found.
