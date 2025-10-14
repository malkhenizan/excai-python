# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebSearchActionFind"]


class WebSearchActionFind(BaseModel):
    pattern: str
    """The pattern or text to search for within the page."""

    type: Literal["find"]
    """The action type."""

    url: str
    """The URL of the page searched for the pattern."""
