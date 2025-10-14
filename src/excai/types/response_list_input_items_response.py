# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .output_message import OutputMessage
from .shared.input_audio import InputAudio
from .shared.mcp_tool_call import McpToolCall
from .shared.mcp_list_tools import McpListTools
from .shared.computer_tool_call import ComputerToolCall
from .shared.input_file_content import InputFileContent
from .shared.input_text_content import InputTextContent
from .shared.image_gen_tool_call import ImageGenToolCall
from .shared.input_image_content import InputImageContent
from .shared.mcp_approval_request import McpApprovalRequest
from .shared.web_search_tool_call import WebSearchToolCall
from .shared.file_search_tool_call import FileSearchToolCall
from .shared.local_shell_tool_call import LocalShellToolCall
from .shared.code_interpreter_tool_call import CodeInterpreterToolCall
from .shared.function_tool_call_resource import FunctionToolCallResource
from .shared.local_shell_tool_call_output import LocalShellToolCallOutput
from .shared.mcp_approval_response_resource import McpApprovalResponseResource
from .shared.computer_tool_call_output_resource import ComputerToolCallOutputResource
from .shared.function_tool_call_output_resource import FunctionToolCallOutputResource

__all__ = ["ResponseListInputItemsResponse", "Data", "DataMessage", "DataMessageContent"]

DataMessageContent: TypeAlias = Annotated[
    Union[InputTextContent, InputImageContent, InputFileContent, InputAudio], PropertyInfo(discriminator="type")
]


class DataMessage(BaseModel):
    id: str
    """The unique ID of the message input."""

    content: List[DataMessageContent]
    """
    A list of one or many input items to the model, containing different content
    types.
    """

    role: Literal["user", "system", "developer"]
    """The role of the message input. One of `user`, `system`, or `developer`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always set to `message`."""


Data: TypeAlias = Annotated[
    Union[
        DataMessage,
        OutputMessage,
        FileSearchToolCall,
        ComputerToolCall,
        ComputerToolCallOutputResource,
        WebSearchToolCall,
        FunctionToolCallResource,
        FunctionToolCallOutputResource,
        ImageGenToolCall,
        CodeInterpreterToolCall,
        LocalShellToolCall,
        LocalShellToolCallOutput,
        McpListTools,
        McpApprovalRequest,
        McpApprovalResponseResource,
        McpToolCall,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseListInputItemsResponse(BaseModel):
    data: List[Data]
    """A list of items used to generate this response."""

    first_id: str
    """The ID of the first item in the list."""

    has_more: bool
    """Whether there are more items available."""

    last_id: str
    """The ID of the last item in the list."""

    object: Literal["list"]
    """The type of object returned, must be `list`."""
