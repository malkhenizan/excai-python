# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .web_search_action_find import WebSearchActionFind
from .web_search_action_search import WebSearchActionSearch
from .web_search_action_open_page import WebSearchActionOpenPage

__all__ = ["WebSearchToolCall", "Action"]

Action: TypeAlias = Annotated[
    Union[WebSearchActionSearch, WebSearchActionOpenPage, WebSearchActionFind], PropertyInfo(discriminator="type")
]


class WebSearchToolCall(BaseModel):
    id: str
    """The unique ID of the web search tool call."""

    action: Action
    """
    An object describing the specific action taken in this web search call. Includes
    details on how the model used the web (search, open_page, find).
    """

    status: Literal["in_progress", "searching", "completed", "failed"]
    """The status of the web search tool call."""

    type: Literal["web_search_call"]
    """The type of the web search tool call. Always `web_search_call`."""
