# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebSearchActionSearch", "Source"]


class Source(TypedDict, total=False):
    type: Required[Literal["url"]]
    """The type of source. Always `url`."""

    url: Required[str]
    """The URL of the source."""


class WebSearchActionSearch(TypedDict, total=False):
    query: Required[str]
    """The search query."""

    type: Required[Literal["search"]]
    """The action type."""

    sources: Iterable[Source]
    """The sources used in the search."""
