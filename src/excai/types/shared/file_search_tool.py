# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .compound_filter import CompoundFilter
from .ranking_options import RankingOptions
from .comparison_filter import ComparisonFilter

__all__ = ["FileSearchTool", "Filters"]

Filters: TypeAlias = Union[ComparisonFilter, CompoundFilter, None]


class FileSearchTool(BaseModel):
    type: Literal["file_search"]
    """The type of the file search tool. Always `file_search`."""

    vector_store_ids: List[str]
    """The IDs of the vector stores to search."""

    filters: Optional[Filters] = None
    """A filter to apply."""

    max_num_results: Optional[int] = None
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: Optional[RankingOptions] = None
    """Ranking options for search."""
