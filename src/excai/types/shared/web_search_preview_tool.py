# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .approximate_location import ApproximateLocation

__all__ = ["WebSearchPreviewTool"]


class WebSearchPreviewTool(BaseModel):
    type: Literal["web_search_preview", "web_search_preview_2025_03_11"]
    """The type of the web search tool.

    One of `web_search_preview` or `web_search_preview_2025_03_11`.
    """

    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[ApproximateLocation] = None
    """The user's location."""
