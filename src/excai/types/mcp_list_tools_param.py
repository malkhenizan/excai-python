# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .mcp_list_tools_tool_param import McpListToolsToolParam

__all__ = ["McpListToolsParam"]


class McpListToolsParam(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the list."""

    server_label: Required[str]
    """The label of the MCP server."""

    tools: Required[Iterable[McpListToolsToolParam]]
    """The tools available on the server."""

    type: Required[Literal["mcp_list_tools"]]
    """The type of the item. Always `mcp_list_tools`."""

    error: Optional[str]
    """Error message if the server could not list tools."""
