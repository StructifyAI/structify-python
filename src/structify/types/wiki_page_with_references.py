# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .wiki_page import WikiPage
from .wiki_connector_reference import WikiConnectorReference

__all__ = ["WikiPageWithReferences"]


class WikiPageWithReferences(WikiPage):
    references: List[WikiConnectorReference]
