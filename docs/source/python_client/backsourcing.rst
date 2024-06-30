.. _backsourcing:

Backsourcing
============
For all our users, knowing that you have accurate data is of paramount importance, so we allow you to see the sources that were used to validate and create any given datapoint. This is useful for understanding the provenance of a given datapoint and for understanding the context in which it was created.

To use this endpoint, you need to know the ids of a given datapoint. In order to find that information, you would need to call the ``structify.dataset.view`` endpoint. 

.. code-block:: python

    from pprint import pprint

    pprint(structify.dataset.view(name = "startups", table = "company"))

This call would result a JSON object including the id, as follows:

.. code-block:: python
    
    [{
        'id': 232997,
        'label': 'company',
        'properties': {
            'description': 'Dropbox is building the world’s first smart '
                                'workspace. Back in 2007, making work better '
                                'for people meant designing a simpler way to '
                                'keep files in sync. Today, it means designing '
                                'products that reduce busywork so you can '
                                'focus on the work that matters.',
            'name': 'Dropbox',
            'website': 'http://dropbox.com'
            }
        }
    ]

Once you have the ids, you can call the ``structify.source.get_sources`` endpoint.

.. code-block:: python

    structify.source.get_sources(id = 232997)

The output will then be a JSON object containing information about the source and where on the source the relevant information lies. Here is an example output:

.. code-block:: python

    [{'location': {'Visual': {'x': 0, 'y': 0}},
    'link': {'Web': {'url': 'https://www.ycombinator.com/companies/dropbox'}},
    'extra_properties': {}}]


