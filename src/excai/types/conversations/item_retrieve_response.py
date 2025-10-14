# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .message import Message
from ..._utils import PropertyInfo
from ..shared.mcp_tool_call import McpToolCall
from ..shared.mcp_list_tools import McpListTools
from ..shared.reasoning_item import ReasoningItem
from .custom_tool_call_output import CustomToolCallOutput
from ..shared.custom_tool_call import CustomToolCall
from ..shared.computer_tool_call import ComputerToolCall
from ..shared.image_gen_tool_call import ImageGenToolCall
from ..shared.mcp_approval_request import McpApprovalRequest
from ..shared.web_search_tool_call import WebSearchToolCall
from ..shared.file_search_tool_call import FileSearchToolCall
from ..shared.local_shell_tool_call import LocalShellToolCall
from ..shared.code_interpreter_tool_call import CodeInterpreterToolCall
from ..shared.function_tool_call_resource import FunctionToolCallResource
from ..shared.local_shell_tool_call_output import LocalShellToolCallOutput
from ..shared.mcp_approval_response_resource import McpApprovalResponseResource
from ..shared.computer_tool_call_output_resource import ComputerToolCallOutputResource
from ..shared.function_tool_call_output_resource import FunctionToolCallOutputResource

__all__ = ["ItemRetrieveResponse"]

ItemRetrieveResponse: TypeAlias = Annotated[
    Union[
        Message,
        FunctionToolCallResource,
        FunctionToolCallOutputResource,
        FileSearchToolCall,
        WebSearchToolCall,
        ImageGenToolCall,
        ComputerToolCall,
        ComputerToolCallOutputResource,
        ReasoningItem,
        CodeInterpreterToolCall,
        LocalShellToolCall,
        LocalShellToolCallOutput,
        McpListTools,
        McpApprovalRequest,
        McpApprovalResponseResource,
        McpToolCall,
        CustomToolCall,
        CustomToolCallOutput,
    ],
    PropertyInfo(discriminator="type"),
]
