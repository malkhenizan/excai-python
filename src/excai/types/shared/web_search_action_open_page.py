# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebSearchActionOpenPage"]


class WebSearchActionOpenPage(BaseModel):
    type: Literal["open_page"]
    """The action type."""

    url: str
    """The URL opened by the model."""
