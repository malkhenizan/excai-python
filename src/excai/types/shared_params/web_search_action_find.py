# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebSearchActionFind"]


class WebSearchActionFind(TypedDict, total=False):
    pattern: Required[str]
    """The pattern or text to search for within the page."""

    type: Required[Literal["find"]]
    """The action type."""

    url: Required[str]
    """The URL of the page searched for the pattern."""
