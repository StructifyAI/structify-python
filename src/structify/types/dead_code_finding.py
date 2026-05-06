# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DeadCodeFinding"]


class DeadCodeFinding(BaseModel):
    """A symbol vulture flagged as unreached from `workflow()` during a review pass."""

    kind: str
    """
    Vulture category: `function`, `class`, `method`, `variable`, `import`,
    `attribute`.
    """

    line: int
    """1-indexed source line where the symbol is defined."""

    name: str
    """The unused symbol name."""

    path: str
    """Workflow-relative file path, e.g. `src/extractors/foo.py`."""
