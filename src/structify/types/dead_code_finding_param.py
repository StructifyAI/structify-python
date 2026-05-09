# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeadCodeFindingParam"]


class DeadCodeFindingParam(TypedDict, total=False):
    """A symbol vulture flagged as unreached from `workflow()` during a review pass."""

    kind: Required[str]
    """
    Vulture category: `function`, `class`, `method`, `variable`, `import`,
    `attribute`.
    """

    line: Required[int]
    """1-indexed source line where the symbol is defined."""

    name: Required[str]
    """The unused symbol name."""

    path: Required[str]
    """Workflow-relative file path, e.g. `src/extractors/foo.py`."""
