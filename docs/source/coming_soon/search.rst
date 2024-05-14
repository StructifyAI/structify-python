Searching through Datasets
==========================

Overview
--------
When you have a large dataset, it can be difficult to find the specific piece of data you are looking for. And often, you will create the datasets as a reference backend for users or AI tools to reference in answering certain questions, which means you won't know immediately what to search for. In those cases, it will be crucial to set up a method to search through the datasets. This can be done via a couple different methods depending on how much specificity you want to allow in the search:

#. :ref:`If you know the keywords to search <string-search>`
#. :ref:`If you just have a question <natural-language-search>`


.. _string-search:

Searching for Specific Strings within Datasets
-----------------------------------------------
Another simple method is to allow users to search for a specific string within the dataset. This can be done by creating a function that takes in a string and returns all the rows that contain that string. This endpoint works best if the you've used enums in your dataset.

If we wanted to power a search for employees who attended a certain school, we could create the following function:

.. code-block:: python

    def search_schools(dataset_name, school_name):

        # We need to specify the table and columns the keyword search applies to
        search_target = {
            "table": [
                "name": "education",
                "columns": ["name"]
            ]
        }
        return client.dataset.query(name = dataset_name, search = search_target, keyword = school_name.lower())

This will return to us a subset of the dataset that contains just the entities whose education table contains the school name we are looking for.

.. tip::
    You can bulk search for multiple keywords by passing a list of keywords to the "keyword" parameter. You can also conduct a search across multiple tables by passing a list of search targets to the "search" parameter.

.. _natural-language-search:

Natural Language Search
-----------------------
The most powerful method is to allow users to ask questions in natural language and have the system return the relevant data. This endpoint is powered by Structify's LLM agents. While the most complex method, it is allows for the most flexible and user-friendly experience.

If we wanted to power users to search for employees by describing the type of school they attended (e.g. "Ivy League tier schools" or "liberal arts colleges in California"), we could create the following function:

.. code-block:: python

    def plaintext_school_search(dataset_name, query):
        return client.analysis.query(dataset = dataset_name, query = query)

Using the ``client.analysis.query`` endpoint powers a more conversational experience for users, and typically, we see this endpoint powering chatbots or other conversational interfaces.
