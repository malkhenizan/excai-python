# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .web_search_action_find import WebSearchActionFind
from .web_search_action_search import WebSearchActionSearch
from .web_search_action_open_page import WebSearchActionOpenPage

__all__ = ["WebSearchToolCall", "Action"]

Action: TypeAlias = Union[WebSearchActionSearch, WebSearchActionOpenPage, WebSearchActionFind]


class WebSearchToolCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the web search tool call."""

    action: Required[Action]
    """
    An object describing the specific action taken in this web search call. Includes
    details on how the model used the web (search, open_page, find).
    """

    status: Required[Literal["in_progress", "searching", "completed", "failed"]]
    """The status of the web search tool call."""

    type: Required[Literal["web_search_call"]]
    """The type of the web search tool call. Always `web_search_call`."""
