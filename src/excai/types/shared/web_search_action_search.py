# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebSearchActionSearch", "Source"]


class Source(BaseModel):
    type: Literal["url"]
    """The type of source. Always `url`."""

    url: str
    """The URL of the source."""


class WebSearchActionSearch(BaseModel):
    query: str
    """The search query."""

    type: Literal["search"]
    """The action type."""

    sources: Optional[List[Source]] = None
    """The sources used in the search."""
