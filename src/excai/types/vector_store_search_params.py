# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "VectorStoreSearchParams",
    "Filters",
    "FiltersComparisonFilter",
    "FiltersCompoundFilter",
    "FiltersCompoundFilterFilter",
    "FiltersCompoundFilterFilterComparisonFilter",
    "RankingOptions",
]


class VectorStoreSearchParams(TypedDict, total=False):
    query: Required[Union[str, SequenceNotStr[str]]]
    """A query string for a search"""

    filters: Filters
    """A filter to apply based on file attributes."""

    max_num_results: int
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: RankingOptions
    """Ranking options for search."""

    rewrite_query: bool
    """Whether to rewrite the natural language query for vector search."""


class FiltersComparisonFilter(TypedDict, total=False):
    key: Required[str]
    """The key to compare against the value."""

    type: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte"]]
    """Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    """

    value: Required[Union[str, float, bool]]
    """
    The value to compare against the attribute key; supports string, number, or
    boolean types.
    """


class FiltersCompoundFilterFilterComparisonFilter(TypedDict, total=False):
    key: Required[str]
    """The key to compare against the value."""

    type: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte"]]
    """Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    """

    value: Required[Union[str, float, bool]]
    """
    The value to compare against the attribute key; supports string, number, or
    boolean types.
    """


FiltersCompoundFilterFilter: TypeAlias = Union[FiltersCompoundFilterFilterComparisonFilter, object]


class FiltersCompoundFilter(TypedDict, total=False):
    filters: Required[Iterable[FiltersCompoundFilterFilter]]
    """Array of filters to combine.

    Items can be `ComparisonFilter` or `CompoundFilter`.
    """

    type: Required[Literal["and", "or"]]
    """Type of operation: `and` or `or`."""


Filters: TypeAlias = Union[FiltersComparisonFilter, FiltersCompoundFilter]


class RankingOptions(TypedDict, total=False):
    ranker: Literal["auto", "default-2024-11-15"]

    score_threshold: float
