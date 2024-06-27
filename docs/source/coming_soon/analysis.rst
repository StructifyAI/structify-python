.. _Analyzing Datasets:

Analyzing Your Datasets
=======================

Overview
--------

Part of the advantages to using Structify as your data infrastructure is the automatic powering of advanced analytics on top of your custom datasets. In our pipeline, Structify is developing the ability to power the following:

#. :ref:`Creating Custom Tags for Data <tagging>`
#. :ref:`Sorting Data along Any Axis <sorting>`
#. :ref:`Getting Confidence Scores <confidence>`


.. _tagging:

Tagging
-------
We will allow you to tag data either via LLM generated tags or custom tags. This lets you to easily filter your data based on the tags you have created.

A common practice is to sort datasets by industry. For example, if you are hiring a GTM specialist, you would want them to have deep knowledge and contacts within your vertical, so tagging your network by industry would allow you to easily filter for the right candidates. You can see a great example of this in `our tutorial <example/example3>`.

.. code-block:: python

    industry_tags = ['healthcare', 'retail', 'finance', 'technology', 'education', 'government', 'non-profit', 'other']
    structify.analysis.filter(
        dataset=candidates, 
        tags=industry_tags, 
        tag_description="a list of possible industries that the candidate has experience in"
    )


.. _sorting:

Sorting
-------
We allow for you to sort your data along any axis (subjective or objective). For example, you can sort news about clients along the sentiment to see how sentiment has changed over time, or you could cluster based on topic and sentiment to determine why audiences are reacting the way they are.

.. code-block:: python

    structify.analysis.sort(
        dataset=news, 
        axis=['sentiment', 'topic'], 
        sort_description="sorts the news by sentiment in order of positive association with our client George Washington University"
    )

.. _confidence:

Confidence Scores
-----------------
We allow for you to get confidence scores for any given datapoint. This is useful for understanding the quality of the data, and for understanding how strongly our agents feel about the certainty of a given datapoint.

If we wanted to get the confidence score for a datapoint, we would call the following:

.. code-block:: python

    structify.source.get_confidence(id = [123456])


Note that you first have to use the ``structufy.dataset.view`` endpoint to retrieve the id(s) of the relevant entities.

Now, you have the tools to be able to more deeply understand your datasets and derive insights from them.