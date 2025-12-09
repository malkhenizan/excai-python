# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .comparison_filter_param import ComparisonFilterParam

__all__ = ["CompoundFilterParam", "Filter"]

Filter: TypeAlias = Union[ComparisonFilterParam, object]


class CompoundFilterParam(TypedDict, total=False):
    """Combine multiple filters using `and` or `or`."""

    filters: Required[Iterable[Filter]]
    """Array of filters to combine.

    Items can be `ComparisonFilter` or `CompoundFilter`.
    """

    type: Required[Literal["and", "or"]]
    """Type of operation: `and` or `or`."""
