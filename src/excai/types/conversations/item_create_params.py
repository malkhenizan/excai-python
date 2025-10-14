# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "ItemCreateParams",
    "Item",
    "ItemMessage",
    "ItemMessageContentInputMessageContentList",
    "ItemMessageContentInputMessageContentListInputText",
    "ItemMessageContentInputMessageContentListInputImage",
    "ItemMessageContentInputMessageContentListInputFile",
    "ItemMessageContentInputMessageContentListInputAudio",
    "ItemMessageContentInputMessageContentListInputAudioInputAudio",
    "ItemFileSearchCall",
    "ItemFileSearchCallResult",
    "ItemComputerCall",
    "ItemComputerCallAction",
    "ItemComputerCallActionClick",
    "ItemComputerCallActionDoubleClick",
    "ItemComputerCallActionDrag",
    "ItemComputerCallActionDragPath",
    "ItemComputerCallActionKeypress",
    "ItemComputerCallActionMove",
    "ItemComputerCallActionScreenshot",
    "ItemComputerCallActionScroll",
    "ItemComputerCallActionType",
    "ItemComputerCallActionWait",
    "ItemComputerCallPendingSafetyCheck",
    "ItemComputerCallOutput",
    "ItemComputerCallOutputOutput",
    "ItemComputerCallOutputAcknowledgedSafetyCheck",
    "ItemWebSearchCall",
    "ItemWebSearchCallAction",
    "ItemWebSearchCallActionSearch",
    "ItemWebSearchCallActionSearchSource",
    "ItemWebSearchCallActionOpenPage",
    "ItemWebSearchCallActionFind",
    "ItemFunctionCall",
    "ItemFunctionCallOutput",
    "ItemFunctionCallOutputOutputUnionMember1",
    "ItemFunctionCallOutputOutputUnionMember1InputText",
    "ItemFunctionCallOutputOutputUnionMember1InputImage",
    "ItemFunctionCallOutputOutputUnionMember1InputFile",
    "ItemReasoning",
    "ItemReasoningSummary",
    "ItemReasoningContent",
    "ItemImageGenerationCall",
    "ItemCodeInterpreterCall",
    "ItemCodeInterpreterCallOutput",
    "ItemCodeInterpreterCallOutputLogs",
    "ItemCodeInterpreterCallOutputImage",
    "ItemLocalShellCall",
    "ItemLocalShellCallAction",
    "ItemLocalShellCallOutput",
    "ItemMcpListTools",
    "ItemMcpListToolsTool",
    "ItemMcpApprovalRequest",
    "ItemMcpApprovalResponse",
    "ItemMcpCall",
    "ItemCustomToolCallOutput",
    "ItemCustomToolCallOutputOutputOutputContentList",
    "ItemCustomToolCallOutputOutputOutputContentListInputText",
    "ItemCustomToolCallOutputOutputOutputContentListInputImage",
    "ItemCustomToolCallOutputOutputOutputContentListInputFile",
    "ItemCustomToolCall",
    "ItemItemReference",
]


class ItemCreateParams(TypedDict, total=False):
    items: Required[Iterable[Item]]
    """The items to add to the conversation. You may add up to 20 items at a time."""

    include: List[
        Literal[
            "code_interpreter_call.outputs",
            "computer_call_output.output.image_url",
            "file_search_call.results",
            "message.input_image.image_url",
            "message.output_text.logprobs",
            "reasoning.encrypted_content",
        ]
    ]
    """Additional fields to include in the response.

    See the `include` parameter for
    [listing Conversation items above](https://platform.excai.com/docs/api-reference/conversations/list-items#conversations_list_items-include)
    for more information.
    """


class ItemMessageContentInputMessageContentListInputText(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class ItemMessageContentInputMessageContentListInputImage(TypedDict, total=False):
    detail: Required[Literal["low", "high", "auto"]]
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    type: Required[Literal["input_image"]]
    """The type of the input item. Always `input_image`."""

    file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    image_url: Optional[str]
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """


class ItemMessageContentInputMessageContentListInputFile(TypedDict, total=False):
    type: Required[Literal["input_file"]]
    """The type of the input item. Always `input_file`."""

    file_data: str
    """The content of the file to be sent to the model."""

    file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    file_url: str
    """The URL of the file to be sent to the model."""

    filename: str
    """The name of the file to be sent to the model."""


class ItemMessageContentInputMessageContentListInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class ItemMessageContentInputMessageContentListInputAudio(TypedDict, total=False):
    input_audio: Required[ItemMessageContentInputMessageContentListInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


ItemMessageContentInputMessageContentList: TypeAlias = Union[
    ItemMessageContentInputMessageContentListInputText,
    ItemMessageContentInputMessageContentListInputImage,
    ItemMessageContentInputMessageContentListInputFile,
    ItemMessageContentInputMessageContentListInputAudio,
]


class ItemMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[ItemMessageContentInputMessageContentList]]]
    """
    Text, image, or audio input to the model, used to generate a response. Can also
    contain previous assistant responses.
    """

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class ItemFileSearchCallResult(TypedDict, total=False):
    attributes: Optional[Dict[str, Union[str, float, bool]]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard. Keys are
    strings with a maximum length of 64 characters. Values are strings with a
    maximum length of 512 characters, booleans, or numbers.
    """

    file_id: str
    """The unique ID of the file."""

    filename: str
    """The name of the file."""

    score: float
    """The relevance score of the file - a value between 0 and 1."""

    text: str
    """The text that was retrieved from the file."""


class ItemFileSearchCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the file search tool call."""

    queries: Required[SequenceNotStr[str]]
    """The queries used to search for files."""

    status: Required[Literal["in_progress", "searching", "completed", "incomplete", "failed"]]
    """The status of the file search tool call.

    One of `in_progress`, `searching`, `incomplete` or `failed`,
    """

    type: Required[Literal["file_search_call"]]
    """The type of the file search tool call. Always `file_search_call`."""

    results: Optional[Iterable[ItemFileSearchCallResult]]
    """The results of the file search tool call."""


class ItemComputerCallActionClick(TypedDict, total=False):
    button: Required[Literal["left", "right", "wheel", "back", "forward"]]
    """Indicates which mouse button was pressed during the click.

    One of `left`, `right`, `wheel`, `back`, or `forward`.
    """

    type: Required[Literal["click"]]
    """Specifies the event type.

    For a click action, this property is always set to `click`.
    """

    x: Required[int]
    """The x-coordinate where the click occurred."""

    y: Required[int]
    """The y-coordinate where the click occurred."""


class ItemComputerCallActionDoubleClick(TypedDict, total=False):
    type: Required[Literal["double_click"]]
    """Specifies the event type.

    For a double click action, this property is always set to `double_click`.
    """

    x: Required[int]
    """The x-coordinate where the double click occurred."""

    y: Required[int]
    """The y-coordinate where the double click occurred."""


class ItemComputerCallActionDragPath(TypedDict, total=False):
    x: Required[int]
    """The x-coordinate."""

    y: Required[int]
    """The y-coordinate."""


class ItemComputerCallActionDrag(TypedDict, total=False):
    path: Required[Iterable[ItemComputerCallActionDragPath]]
    """An array of coordinates representing the path of the drag action.

    Coordinates will appear as an array of objects, eg

    ```
    [
      { x: 100, y: 200 },
      { x: 200, y: 300 }
    ]
    ```
    """

    type: Required[Literal["drag"]]
    """Specifies the event type.

    For a drag action, this property is always set to `drag`.
    """


class ItemComputerCallActionKeypress(TypedDict, total=False):
    keys: Required[SequenceNotStr[str]]
    """The combination of keys the model is requesting to be pressed.

    This is an array of strings, each representing a key.
    """

    type: Required[Literal["keypress"]]
    """Specifies the event type.

    For a keypress action, this property is always set to `keypress`.
    """


class ItemComputerCallActionMove(TypedDict, total=False):
    type: Required[Literal["move"]]
    """Specifies the event type.

    For a move action, this property is always set to `move`.
    """

    x: Required[int]
    """The x-coordinate to move to."""

    y: Required[int]
    """The y-coordinate to move to."""


class ItemComputerCallActionScreenshot(TypedDict, total=False):
    type: Required[Literal["screenshot"]]
    """Specifies the event type.

    For a screenshot action, this property is always set to `screenshot`.
    """


class ItemComputerCallActionScroll(TypedDict, total=False):
    scroll_x: Required[int]
    """The horizontal scroll distance."""

    scroll_y: Required[int]
    """The vertical scroll distance."""

    type: Required[Literal["scroll"]]
    """Specifies the event type.

    For a scroll action, this property is always set to `scroll`.
    """

    x: Required[int]
    """The x-coordinate where the scroll occurred."""

    y: Required[int]
    """The y-coordinate where the scroll occurred."""


class ItemComputerCallActionType(TypedDict, total=False):
    text: Required[str]
    """The text to type."""

    type: Required[Literal["type"]]
    """Specifies the event type.

    For a type action, this property is always set to `type`.
    """


class ItemComputerCallActionWait(TypedDict, total=False):
    type: Required[Literal["wait"]]
    """Specifies the event type.

    For a wait action, this property is always set to `wait`.
    """


ItemComputerCallAction: TypeAlias = Union[
    ItemComputerCallActionClick,
    ItemComputerCallActionDoubleClick,
    ItemComputerCallActionDrag,
    ItemComputerCallActionKeypress,
    ItemComputerCallActionMove,
    ItemComputerCallActionScreenshot,
    ItemComputerCallActionScroll,
    ItemComputerCallActionType,
    ItemComputerCallActionWait,
]


class ItemComputerCallPendingSafetyCheck(TypedDict, total=False):
    id: Required[str]
    """The ID of the pending safety check."""

    code: Required[str]
    """The type of the pending safety check."""

    message: Required[str]
    """Details about the pending safety check."""


class ItemComputerCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the computer call."""

    action: Required[ItemComputerCallAction]
    """A click action."""

    call_id: Required[str]
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: Required[Iterable[ItemComputerCallPendingSafetyCheck]]
    """The pending safety checks for the computer call."""

    status: Required[Literal["in_progress", "completed", "incomplete"]]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Required[Literal["computer_call"]]
    """The type of the computer call. Always `computer_call`."""


class ItemComputerCallOutputOutput(TypedDict, total=False):
    type: Required[Literal["computer_screenshot"]]
    """Specifies the event type.

    For a computer screenshot, this property is always set to `computer_screenshot`.
    """

    file_id: str
    """The identifier of an uploaded file that contains the screenshot."""

    image_url: str
    """The URL of the screenshot image."""


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

    output: Required[ItemComputerCallOutputOutput]
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


class ItemWebSearchCallActionSearchSource(TypedDict, total=False):
    type: Required[Literal["url"]]
    """The type of source. Always `url`."""

    url: Required[str]
    """The URL of the source."""


class ItemWebSearchCallActionSearch(TypedDict, total=False):
    query: Required[str]
    """The search query."""

    type: Required[Literal["search"]]
    """The action type."""

    sources: Iterable[ItemWebSearchCallActionSearchSource]
    """The sources used in the search."""


class ItemWebSearchCallActionOpenPage(TypedDict, total=False):
    type: Required[Literal["open_page"]]
    """The action type."""

    url: Required[str]
    """The URL opened by the model."""


class ItemWebSearchCallActionFind(TypedDict, total=False):
    pattern: Required[str]
    """The pattern or text to search for within the page."""

    type: Required[Literal["find"]]
    """The action type."""

    url: Required[str]
    """The URL of the page searched for the pattern."""


ItemWebSearchCallAction: TypeAlias = Union[
    ItemWebSearchCallActionSearch, ItemWebSearchCallActionOpenPage, ItemWebSearchCallActionFind
]


class ItemWebSearchCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the web search tool call."""

    action: Required[ItemWebSearchCallAction]
    """
    An object describing the specific action taken in this web search call. Includes
    details on how the model used the web (search, open_page, find).
    """

    status: Required[Literal["in_progress", "searching", "completed", "failed"]]
    """The status of the web search tool call."""

    type: Required[Literal["web_search_call"]]
    """The type of the web search tool call. Always `web_search_call`."""


class ItemFunctionCall(TypedDict, total=False):
    arguments: Required[str]
    """A JSON string of the arguments to pass to the function."""

    call_id: Required[str]
    """The unique ID of the function tool call generated by the model."""

    name: Required[str]
    """The name of the function to run."""

    type: Required[Literal["function_call"]]
    """The type of the function tool call. Always `function_call`."""

    id: str
    """The unique ID of the function tool call."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
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


class ItemReasoningSummary(TypedDict, total=False):
    text: Required[str]
    """A summary of the reasoning output from the model so far."""

    type: Required[Literal["summary_text"]]
    """The type of the object. Always `summary_text`."""


class ItemReasoningContent(TypedDict, total=False):
    text: Required[str]
    """The reasoning text from the model."""

    type: Required[Literal["reasoning_text"]]
    """The type of the reasoning text. Always `reasoning_text`."""


class ItemReasoning(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the reasoning content."""

    summary: Required[Iterable[ItemReasoningSummary]]
    """Reasoning summary content."""

    type: Required[Literal["reasoning"]]
    """The type of the object. Always `reasoning`."""

    content: Iterable[ItemReasoningContent]
    """Reasoning text content."""

    encrypted_content: Optional[str]
    """
    The encrypted content of the reasoning item - populated when a response is
    generated with `reasoning.encrypted_content` in the `include` parameter.
    """

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


class ItemImageGenerationCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the image generation call."""

    result: Required[Optional[str]]
    """The generated image encoded in base64."""

    status: Required[Literal["in_progress", "completed", "generating", "failed"]]
    """The status of the image generation call."""

    type: Required[Literal["image_generation_call"]]
    """The type of the image generation call. Always `image_generation_call`."""


class ItemCodeInterpreterCallOutputLogs(TypedDict, total=False):
    logs: Required[str]
    """The logs output from the code interpreter."""

    type: Required[Literal["logs"]]
    """The type of the output. Always 'logs'."""


class ItemCodeInterpreterCallOutputImage(TypedDict, total=False):
    type: Required[Literal["image"]]
    """The type of the output. Always 'image'."""

    url: Required[str]
    """The URL of the image output from the code interpreter."""


ItemCodeInterpreterCallOutput: TypeAlias = Union[ItemCodeInterpreterCallOutputLogs, ItemCodeInterpreterCallOutputImage]


class ItemCodeInterpreterCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the code interpreter tool call."""

    code: Required[Optional[str]]
    """The code to run, or null if not available."""

    container_id: Required[str]
    """The ID of the container used to run the code."""

    outputs: Required[Optional[Iterable[ItemCodeInterpreterCallOutput]]]
    """
    The outputs generated by the code interpreter, such as logs or images. Can be
    null if no outputs are available.
    """

    status: Required[Literal["in_progress", "completed", "incomplete", "interpreting", "failed"]]
    """The status of the code interpreter tool call.

    Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and
    `failed`.
    """

    type: Required[Literal["code_interpreter_call"]]
    """The type of the code interpreter tool call. Always `code_interpreter_call`."""


class ItemLocalShellCallAction(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]
    """The command to run."""

    env: Required[Dict[str, str]]
    """Environment variables to set for the command."""

    type: Required[Literal["exec"]]
    """The type of the local shell action. Always `exec`."""

    timeout_ms: Optional[int]
    """Optional timeout in milliseconds for the command."""

    user: Optional[str]
    """Optional user to run the command as."""

    working_directory: Optional[str]
    """Optional working directory to run the command in."""


class ItemLocalShellCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the local shell call."""

    action: Required[ItemLocalShellCallAction]
    """Execute a shell command on the server."""

    call_id: Required[str]
    """The unique ID of the local shell tool call generated by the model."""

    status: Required[Literal["in_progress", "completed", "incomplete"]]
    """The status of the local shell call."""

    type: Required[Literal["local_shell_call"]]
    """The type of the local shell call. Always `local_shell_call`."""


class ItemLocalShellCallOutput(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the local shell tool call generated by the model."""

    output: Required[str]
    """A JSON string of the output of the local shell tool call."""

    type: Required[Literal["local_shell_call_output"]]
    """The type of the local shell tool call output. Always `local_shell_call_output`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """The status of the item. One of `in_progress`, `completed`, or `incomplete`."""


class ItemMcpListToolsTool(TypedDict, total=False):
    input_schema: Required[object]
    """The JSON schema describing the tool's input."""

    name: Required[str]
    """The name of the tool."""

    annotations: Optional[object]
    """Additional annotations about the tool."""

    description: Optional[str]
    """The description of the tool."""


class ItemMcpListTools(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the list."""

    server_label: Required[str]
    """The label of the MCP server."""

    tools: Required[Iterable[ItemMcpListToolsTool]]
    """The tools available on the server."""

    type: Required[Literal["mcp_list_tools"]]
    """The type of the item. Always `mcp_list_tools`."""

    error: Optional[str]
    """Error message if the server could not list tools."""


class ItemMcpApprovalRequest(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the approval request."""

    arguments: Required[str]
    """A JSON string of arguments for the tool."""

    name: Required[str]
    """The name of the tool to run."""

    server_label: Required[str]
    """The label of the MCP server making the request."""

    type: Required[Literal["mcp_approval_request"]]
    """The type of the item. Always `mcp_approval_request`."""


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


class ItemMcpCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the tool call."""

    arguments: Required[str]
    """A JSON string of the arguments passed to the tool."""

    name: Required[str]
    """The name of the tool that was run."""

    server_label: Required[str]
    """The label of the MCP server running the tool."""

    type: Required[Literal["mcp_call"]]
    """The type of the item. Always `mcp_call`."""

    approval_request_id: Optional[str]
    """
    Unique identifier for the MCP tool call approval request. Include this value in
    a subsequent `mcp_approval_response` input to approve or reject the
    corresponding tool call.
    """

    error: Optional[str]
    """The error from the tool call, if any."""

    output: Optional[str]
    """The output from the tool call."""

    status: Literal["in_progress", "completed", "incomplete", "calling", "failed"]
    """The status of the tool call.

    One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.
    """


class ItemCustomToolCallOutputOutputOutputContentListInputText(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class ItemCustomToolCallOutputOutputOutputContentListInputImage(TypedDict, total=False):
    detail: Required[Literal["low", "high", "auto"]]
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    type: Required[Literal["input_image"]]
    """The type of the input item. Always `input_image`."""

    file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    image_url: Optional[str]
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """


class ItemCustomToolCallOutputOutputOutputContentListInputFile(TypedDict, total=False):
    type: Required[Literal["input_file"]]
    """The type of the input item. Always `input_file`."""

    file_data: str
    """The content of the file to be sent to the model."""

    file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    file_url: str
    """The URL of the file to be sent to the model."""

    filename: str
    """The name of the file to be sent to the model."""


ItemCustomToolCallOutputOutputOutputContentList: TypeAlias = Union[
    ItemCustomToolCallOutputOutputOutputContentListInputText,
    ItemCustomToolCallOutputOutputOutputContentListInputImage,
    ItemCustomToolCallOutputOutputOutputContentListInputFile,
]


class ItemCustomToolCallOutput(TypedDict, total=False):
    call_id: Required[str]
    """The call ID, used to map this custom tool call output to a custom tool call."""

    output: Required[Union[str, Iterable[ItemCustomToolCallOutputOutputOutputContentList]]]
    """
    The output from the custom tool call generated by your code. Can be a string or
    an list of output content.
    """

    type: Required[Literal["custom_tool_call_output"]]
    """The type of the custom tool call output. Always `custom_tool_call_output`."""

    id: str
    """The unique ID of the custom tool call output in the EXCai platform."""


class ItemCustomToolCall(TypedDict, total=False):
    call_id: Required[str]
    """An identifier used to map this custom tool call to a tool call output."""

    input: Required[str]
    """The input for the custom tool call generated by the model."""

    name: Required[str]
    """The name of the custom tool being called."""

    type: Required[Literal["custom_tool_call"]]
    """The type of the custom tool call. Always `custom_tool_call`."""

    id: str
    """The unique ID of the custom tool call in the EXCai platform."""


class ItemItemReference(TypedDict, total=False):
    id: Required[str]
    """The ID of the item to reference."""

    type: Optional[Literal["item_reference"]]
    """The type of item to reference. Always `item_reference`."""


Item: TypeAlias = Union[
    ItemMessage,
    ItemMessage,
    ItemMessage,
    ItemFileSearchCall,
    ItemComputerCall,
    ItemComputerCallOutput,
    ItemWebSearchCall,
    ItemFunctionCall,
    ItemFunctionCallOutput,
    ItemReasoning,
    ItemImageGenerationCall,
    ItemCodeInterpreterCall,
    ItemLocalShellCall,
    ItemLocalShellCallOutput,
    ItemMcpListTools,
    ItemMcpApprovalRequest,
    ItemMcpApprovalResponse,
    ItemMcpCall,
    ItemCustomToolCallOutput,
    ItemCustomToolCall,
    ItemItemReference,
]
