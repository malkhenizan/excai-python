# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .mcp_list_tools_tool import McpListToolsTool

__all__ = ["McpListTools"]


class McpListTools(BaseModel):
    id: str
    """The unique ID of the list."""

    server_label: str
    """The label of the MCP server."""

    tools: List[McpListToolsTool]
    """The tools available on the server."""

    type: Literal["mcp_list_tools"]
    """The type of the item. Always `mcp_list_tools`."""

    error: Optional[str] = None
    """Error message if the server could not list tools."""
