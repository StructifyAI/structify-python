# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .team_wiki_page import TeamWikiPage
from .wiki_connector_reference import WikiConnectorReference

__all__ = ["WikiPageWithReferences"]


class WikiPageWithReferences(TeamWikiPage):
    references: List[WikiConnectorReference]
