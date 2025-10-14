# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .compound_filter import CompoundFilter
from .ranking_options import RankingOptions
from .comparison_filter import ComparisonFilter

__all__ = ["FileSearchTool", "Filters"]

Filters: TypeAlias = Union[ComparisonFilter, CompoundFilter]


class FileSearchTool(TypedDict, total=False):
    type: Required[Literal["file_search"]]
    """The type of the file search tool. Always `file_search`."""

    vector_store_ids: Required[SequenceNotStr[str]]
    """The IDs of the vector stores to search."""

    filters: Optional[Filters]
    """A filter to apply."""

    max_num_results: int
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: RankingOptions
    """Ranking options for search."""
