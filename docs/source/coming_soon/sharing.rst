Sharing Datasets
================
Oftentimes, you will want to share your dataset with others. You can use the ``structify.datasets.share`` API call to share your dataset with others. This API call requires the following:

* **name:** The name of the dataset you want to share
* **share_method:** The method of sharing the dataset. This can be "public" or "private". 
* **restrictions**: (optional) A list of restrictions that you want to place on the dataset. This can be "view-only", "refresh-only", "edit", "no-delete", or "admin". Each successive option has more priviledges. The default is "view".
* **users:** (optional) A list of user ids that you want to share the dataset with.
* **emails:** (optional) A list of emails that you want to share the dataset with.

.. note::
    If you want to share the dataset with specific users, you can use the "private" method and pass a list of either ``user_ids`` to the "users" parameter. If the target recipients are not users, you can pass a list of emails to the "emails" parameter, which will send them an email link to create an account and view the dataset.

Here's an example that walks through sharing the employees dataset with various co-workers who do not have Structify accounts:

.. code-block:: python

    structify.datasets.share(
        name="employees", 
        share_method="private", 
        restrictions="no-delete",
        emails=["ellie@structify.ai", "sami@structify.ai", "maya@structify.ai"]
    )
