.. _schema-guidance:

Schema Recipes for Success
===========================

Art versus Science in Schema Design
------------------------------------
The way we at Structify approach schema design is to think of it as both an art **and** a science. The proper recipe for a robust and powerful schema will include both creativity in how you build and connect tables, as well as precision in how you define the parameters (properties and relationships) that you're looking to structure.

- **Creativity**
    One of the coolest (and most powerful) things about **structifying** data is that you're fully in control of how the data transforms from unstructured to structured. A lot of thought work can (and should, in complex use cases) go into how you go about building the set of tables and how they connect (the schema for short).
    - Example: We recently built a schema for a use case that wanted to structure pharmaceutical clinical trial results, from graphs and charts present in the write-up. These outcomes can be incredibly convoluted, as they span multiple trial groups, including a control group, as well as results at different dosages. A naive approach (and our first one) was to try and cram all these as properties into one table. After some discussion and whiteboarding, we transformed the schema to look a little different, leveraging creativity in tables and their relationships to build something that more properly encapsulated the data we were looking at. Check out the finished product below.
- **Advice**
    Our biggest recommendation when trying to think about how to map your data is to take a step back and think about the problem. Consider what you're trying to structure as a whole, and break it into pieces. What are you interested in seeing atomically? Those are your entities (or **rows**) in a table. Consider what elements describe these things (making them different from each other). Get a list of those, and those are your properties (or **columns**). Now you've got a table for a specific type of entity! Create a table for each **kind** of entity that makes up your data. Finally, consider the things that connect different kinds of entities. These are your relationships! Now you've got a schema! See below for a word on relationship properties.

The Science: Precision in Descriptions
---------------------------------------

Accuracy and clarity in descriptions are fundamental. When defining entities, tables, and properties, make sure to:

- Provide clear and concise definitions.
- Use precise language to avoid ambiguity.
- Avoid overloading properties with too many different kinds of information.
- Consider edge cases, and delineate exact behavior you want for best results.

Example: the Name property. You'll come up with this one a lot, whether it's a person's name, a fictional character's name, or a company's name. Let's take a Person Table and the Name property; you might be tempted to write a description like this: "The name of the person". Here's why that might lead to unexpected results:
    1. People generally have first and last names. What happens if the model comes back with 10 different Alex's, and didn't grab a last name?
        a. Consider this description instead: "A person's full name, including when possible first, middle, and last name, but always AT LEAST a last name" See the difference?
    2. What about titles? Mr. , Mrs. , Dr. Hon. (Honorable, if you didn't know), M.D. , Ph.D. Maybe you want these, maybe you don't. Either way, you should make it clear in the schema!

Enums: When to use Them
-----------------------

The obvious usefulness of enums is that they allow us to restrict values to a pre-determined set (say goodbye to painful data cleaning) and in doing so enable use cases for properties that are naturally limited. For instance, if we had a dataset about professional athletes, and we were interested in looking at their college level as a property we might write an enum that takes in D3, D2, D1 etc.
The hidden power of enums lies in their ability to let dora INFER. For instance, let's say that we're interested in a company's market type (B2B - Business to Businesss vs. B2C -- business to consumer). This is something you'll rarely see written somewhere on a company's website*, so it might be useful to you as an enum. Intuition here is that if we see the company's website, that talks about a product that handles all browser needs for AI companies, we can safely conclude that they're B2B.

.. note::
    It is of course possible that a separate blog has directly written about a company being B2B SaaS -- in which case, we'll find it. So if you want to find it spelled out, we can do that too, no ENUM necessary. That's the beauty of Structify.

Below are a few more bonuses to enums:
- Maintain integrity by restricting property values to a predefined set.
- Ensure clarity when representing data that has specific categories, such as "status" or "type."

Relationship Properties -- When to Use Them
--------------------------------------------
Relationships can also have **properties** attached to them, which is where the design gets interesting. For example, a "supplies" relationship between a manufacturer and a product could have a property like "supply rate."

This is a good example of a relationship property because it applies to THAT SPECIFIC relationship between entities. This is because a different manufacturer, that might also supply that product, could have a different supply rate. This means it can't be a property in the product table. Since a manufacturer likely supplies multiple different products, with different supply rates, it can't be in the manufacturer table either. Thus, it's a relationship property. Pretty cool right?

Schema Cookbook
----------------
Check out the schema cookbook section to find schemas you might find useful in putting these design principles into practice. Give them a try, and let us know what you think!

* :doc:`financials_schema`
* :doc:`clinical_trials_schema`
* :doc:`ecommerce_schema`
* :doc:`semiconductor_schema`