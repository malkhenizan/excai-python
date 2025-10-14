# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .output_message_param import OutputMessageParam
from .function_tool_call_param import FunctionToolCallParam
from .shared_params.input_audio import InputAudio
from .shared_params.mcp_tool_call import McpToolCall
from .shared_params.mcp_list_tools import McpListTools
from .shared_params.reasoning_item import ReasoningItem
from .evals.easy_input_message_param import EasyInputMessageParam
from .shared_params.custom_tool_call import CustomToolCall
from .shared_params.computer_tool_call import ComputerToolCall
from .shared_params.input_file_content import InputFileContent
from .shared_params.input_text_content import InputTextContent
from .shared_params.image_gen_tool_call import ImageGenToolCall
from .shared_params.input_image_content import InputImageContent
from .shared_params.mcp_approval_request import McpApprovalRequest
from .shared_params.web_search_tool_call import WebSearchToolCall
from .shared_params.file_search_tool_call import FileSearchToolCall
from .shared_params.local_shell_tool_call import LocalShellToolCall
from .shared_params.computer_screenshot_image import ComputerScreenshotImage
from .shared_params.code_interpreter_tool_call import CodeInterpreterToolCall
from .shared_params.local_shell_tool_call_output import LocalShellToolCallOutput
from .conversations.custom_tool_call_output_param import CustomToolCallOutputParam

__all__ = [
    "ConversationCreateParams",
    "Item",
    "ItemMessage",
    "ItemMessageContent",
    "ItemComputerCallOutput",
    "ItemComputerCallOutputAcknowledgedSafetyCheck",
    "ItemFunctionCallOutput",
    "ItemFunctionCallOutputOutputUnionMember1",
    "ItemFunctionCallOutputOutputUnionMember1InputText",
    "ItemFunctionCallOutputOutputUnionMember1InputImage",
    "ItemFunctionCallOutputOutputUnionMember1InputFile",
    "ItemMcpApprovalResponse",
    "ItemItemReference",
]


class ConversationCreateParams(TypedDict, total=False):
    items: Optional[Iterable[Item]]
    """Initial items to include in the conversation context.

    You may add up to 20 items at a time.
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """


ItemMessageContent: TypeAlias = Union[InputTextContent, InputImageContent, InputFileContent, InputAudio]


class ItemMessage(TypedDict, total=False):
    content: Required[Iterable[ItemMessageContent]]
    """
    A list of one or many input items to the model, containing different content
    types.
    """

    role: Required[Literal["user", "system", "developer"]]
    """The role of the message input. One of `user`, `system`, or `developer`."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Literal["message"]
    """The type of the message input. Always set to `message`."""


class ItemComputerCallOutputAcknowledgedSafetyCheck(TypedDict, total=False):
    id: Required[str]
    """The ID of the pending safety check."""

    code: Optional[str]
    """The type of the pending safety check."""

    message: Optional[str]
    """Details about the pending safety check."""


class ItemComputerCallOutput(TypedDict, total=False):
    call_id: Required[str]
    """The ID of the computer tool call that produced the output."""

    output: Required[ComputerScreenshotImage]
    """A computer screenshot image used with the computer use tool."""

    type: Required[Literal["computer_call_output"]]
    """The type of the computer tool call output. Always `computer_call_output`."""

    id: Optional[str]
    """The ID of the computer tool call output."""

    acknowledged_safety_checks: Optional[Iterable[ItemComputerCallOutputAcknowledgedSafetyCheck]]
    """
    The safety checks reported by the API that have been acknowledged by the
    developer.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """


class ItemFunctionCallOutputOutputUnionMember1InputText(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class ItemFunctionCallOutputOutputUnionMember1InputImage(TypedDict, total=False):
    type: Required[Literal["input_image"]]
    """The type of the input item. Always `input_image`."""

    detail: Optional[Literal["low", "high", "auto"]]
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    image_url: Optional[str]
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """


class ItemFunctionCallOutputOutputUnionMember1InputFile(TypedDict, total=False):
    type: Required[Literal["input_file"]]
    """The type of the input item. Always `input_file`."""

    file_data: Optional[str]
    """The base64-encoded data of the file to be sent to the model."""

    file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    file_url: Optional[str]
    """The URL of the file to be sent to the model."""

    filename: Optional[str]
    """The name of the file to be sent to the model."""


ItemFunctionCallOutputOutputUnionMember1: TypeAlias = Union[
    ItemFunctionCallOutputOutputUnionMember1InputText,
    ItemFunctionCallOutputOutputUnionMember1InputImage,
    ItemFunctionCallOutputOutputUnionMember1InputFile,
]


class ItemFunctionCallOutput(TypedDict, total=False):
    call_id: Required[str]
    """The unique ID of the function tool call generated by the model."""

    output: Required[Union[str, Iterable[ItemFunctionCallOutputOutputUnionMember1]]]
    """Text, image, or file output of the function tool call."""

    type: Required[Literal["function_call_output"]]
    """The type of the function tool call output. Always `function_call_output`."""

    id: Optional[str]
    """The unique ID of the function tool call output.

    Populated when this item is returned via API.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


class ItemMcpApprovalResponse(TypedDict, total=False):
    approval_request_id: Required[str]
    """The ID of the approval request being answered."""

    approve: Required[bool]
    """Whether the request was approved."""

    type: Required[Literal["mcp_approval_response"]]
    """The type of the item. Always `mcp_approval_response`."""

    id: Optional[str]
    """The unique ID of the approval response"""

    reason: Optional[str]
    """Optional reason for the decision."""


class ItemItemReference(TypedDict, total=False):
    id: Required[str]
    """The ID of the item to reference."""

    type: Optional[Literal["item_reference"]]
    """The type of item to reference. Always `item_reference`."""


Item: TypeAlias = Union[
    EasyInputMessageParam,
    ItemMessage,
    OutputMessageParam,
    FileSearchToolCall,
    ComputerToolCall,
    ItemComputerCallOutput,
    WebSearchToolCall,
    FunctionToolCallParam,
    ItemFunctionCallOutput,
    ReasoningItem,
    ImageGenToolCall,
    CodeInterpreterToolCall,
    LocalShellToolCall,
    LocalShellToolCallOutput,
    McpListTools,
    McpApprovalRequest,
    ItemMcpApprovalResponse,
    McpToolCall,
    CustomToolCallOutputParam,
    CustomToolCall,
    ItemItemReference,
]
