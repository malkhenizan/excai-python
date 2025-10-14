# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ItemRetrieveResponse",
    "Message",
    "MessageContent",
    "MessageContentInputText",
    "MessageContentOutputText",
    "MessageContentOutputTextAnnotation",
    "MessageContentOutputTextAnnotationFileCitation",
    "MessageContentOutputTextAnnotationURLCitation",
    "MessageContentOutputTextAnnotationContainerFileCitation",
    "MessageContentOutputTextAnnotationFilePath",
    "MessageContentOutputTextLogprob",
    "MessageContentOutputTextLogprobTopLogprob",
    "MessageContentText",
    "MessageContentSummaryText",
    "MessageContentReasoningText",
    "MessageContentRefusal",
    "MessageContentInputImage",
    "MessageContentComputerScreenshot",
    "MessageContentInputFile",
    "FunctionCall",
    "FunctionCallOutput",
    "FunctionCallOutputOutputOutputContentList",
    "FunctionCallOutputOutputOutputContentListInputText",
    "FunctionCallOutputOutputOutputContentListInputImage",
    "FunctionCallOutputOutputOutputContentListInputFile",
    "FileSearchCall",
    "FileSearchCallResult",
    "WebSearchCall",
    "WebSearchCallAction",
    "WebSearchCallActionSearch",
    "WebSearchCallActionSearchSource",
    "WebSearchCallActionOpenPage",
    "WebSearchCallActionFind",
    "ImageGenerationCall",
    "ComputerCall",
    "ComputerCallAction",
    "ComputerCallActionClick",
    "ComputerCallActionDoubleClick",
    "ComputerCallActionDrag",
    "ComputerCallActionDragPath",
    "ComputerCallActionKeypress",
    "ComputerCallActionMove",
    "ComputerCallActionScreenshot",
    "ComputerCallActionScroll",
    "ComputerCallActionType",
    "ComputerCallActionWait",
    "ComputerCallPendingSafetyCheck",
    "ComputerCallOutput",
    "ComputerCallOutputOutput",
    "ComputerCallOutputAcknowledgedSafetyCheck",
    "Reasoning",
    "ReasoningSummary",
    "ReasoningContent",
    "CodeInterpreterCall",
    "CodeInterpreterCallOutput",
    "CodeInterpreterCallOutputLogs",
    "CodeInterpreterCallOutputImage",
    "LocalShellCall",
    "LocalShellCallAction",
    "LocalShellCallOutput",
    "McpListTools",
    "McpListToolsTool",
    "McpApprovalRequest",
    "McpApprovalResponse",
    "McpCall",
    "CustomToolCall",
    "CustomToolCallOutput",
    "CustomToolCallOutputOutputOutputContentList",
    "CustomToolCallOutputOutputOutputContentListInputText",
    "CustomToolCallOutputOutputOutputContentListInputImage",
    "CustomToolCallOutputOutputOutputContentListInputFile",
]


class MessageContentInputText(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class MessageContentOutputTextAnnotationFileCitation(BaseModel):
    file_id: str
    """The ID of the file."""

    filename: str
    """The filename of the file cited."""

    index: int
    """The index of the file in the list of files."""

    type: Literal["file_citation"]
    """The type of the file citation. Always `file_citation`."""


class MessageContentOutputTextAnnotationURLCitation(BaseModel):
    end_index: int
    """The index of the last character of the URL citation in the message."""

    start_index: int
    """The index of the first character of the URL citation in the message."""

    title: str
    """The title of the web resource."""

    type: Literal["url_citation"]
    """The type of the URL citation. Always `url_citation`."""

    url: str
    """The URL of the web resource."""


class MessageContentOutputTextAnnotationContainerFileCitation(BaseModel):
    container_id: str
    """The ID of the container file."""

    end_index: int
    """The index of the last character of the container file citation in the message."""

    file_id: str
    """The ID of the file."""

    filename: str
    """The filename of the container file cited."""

    start_index: int
    """The index of the first character of the container file citation in the message."""

    type: Literal["container_file_citation"]
    """The type of the container file citation. Always `container_file_citation`."""


class MessageContentOutputTextAnnotationFilePath(BaseModel):
    file_id: str
    """The ID of the file."""

    index: int
    """The index of the file in the list of files."""

    type: Literal["file_path"]
    """The type of the file path. Always `file_path`."""


MessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        MessageContentOutputTextAnnotationFileCitation,
        MessageContentOutputTextAnnotationURLCitation,
        MessageContentOutputTextAnnotationContainerFileCitation,
        MessageContentOutputTextAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class MessageContentOutputTextLogprobTopLogprob(BaseModel):
    token: str

    bytes: List[int]

    logprob: float


class MessageContentOutputTextLogprob(BaseModel):
    token: str

    bytes: List[int]

    logprob: float

    top_logprobs: List[MessageContentOutputTextLogprobTopLogprob]


class MessageContentOutputText(BaseModel):
    annotations: List[MessageContentOutputTextAnnotation]
    """The annotations of the text output."""

    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""

    logprobs: Optional[List[MessageContentOutputTextLogprob]] = None


class MessageContentText(BaseModel):
    text: str

    type: Literal["text"]


class MessageContentSummaryText(BaseModel):
    text: str
    """A summary of the reasoning output from the model so far."""

    type: Literal["summary_text"]
    """The type of the object. Always `summary_text`."""


class MessageContentReasoningText(BaseModel):
    text: str
    """The reasoning text from the model."""

    type: Literal["reasoning_text"]
    """The type of the reasoning text. Always `reasoning_text`."""


class MessageContentRefusal(BaseModel):
    refusal: str
    """The refusal explanation from the model."""

    type: Literal["refusal"]
    """The type of the refusal. Always `refusal`."""


class MessageContentInputImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    type: Literal["input_image"]
    """The type of the input item. Always `input_image`."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    image_url: Optional[str] = None
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """


class MessageContentComputerScreenshot(BaseModel):
    file_id: Optional[str] = None
    """The identifier of an uploaded file that contains the screenshot."""

    image_url: Optional[str] = None
    """The URL of the screenshot image."""

    type: Literal["computer_screenshot"]
    """Specifies the event type.

    For a computer screenshot, this property is always set to `computer_screenshot`.
    """


class MessageContentInputFile(BaseModel):
    type: Literal["input_file"]
    """The type of the input item. Always `input_file`."""

    file_data: Optional[str] = None
    """The content of the file to be sent to the model."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    file_url: Optional[str] = None
    """The URL of the file to be sent to the model."""

    filename: Optional[str] = None
    """The name of the file to be sent to the model."""


MessageContent: TypeAlias = Annotated[
    Union[
        MessageContentInputText,
        MessageContentOutputText,
        MessageContentText,
        MessageContentSummaryText,
        MessageContentReasoningText,
        MessageContentRefusal,
        MessageContentInputImage,
        MessageContentComputerScreenshot,
        MessageContentInputFile,
    ],
    PropertyInfo(discriminator="type"),
]


class Message(BaseModel):
    id: str
    """The unique ID of the message."""

    content: List[MessageContent]
    """The content of the message"""

    role: Literal["unknown", "user", "assistant", "system", "critic", "discriminator", "developer", "tool"]
    """The role of the message.

    One of `unknown`, `user`, `assistant`, `system`, `critic`, `discriminator`,
    `developer`, or `tool`.
    """

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Literal["message"]
    """The type of the message. Always set to `message`."""


class FunctionCall(BaseModel):
    id: str
    """The unique ID of the function tool call."""

    arguments: str
    """A JSON string of the arguments to pass to the function."""

    call_id: str
    """The unique ID of the function tool call generated by the model."""

    name: str
    """The name of the function to run."""

    type: Literal["function_call"]
    """The type of the function tool call. Always `function_call`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


class FunctionCallOutputOutputOutputContentListInputText(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class FunctionCallOutputOutputOutputContentListInputImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    type: Literal["input_image"]
    """The type of the input item. Always `input_image`."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    image_url: Optional[str] = None
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """


class FunctionCallOutputOutputOutputContentListInputFile(BaseModel):
    type: Literal["input_file"]
    """The type of the input item. Always `input_file`."""

    file_data: Optional[str] = None
    """The content of the file to be sent to the model."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    file_url: Optional[str] = None
    """The URL of the file to be sent to the model."""

    filename: Optional[str] = None
    """The name of the file to be sent to the model."""


FunctionCallOutputOutputOutputContentList: TypeAlias = Annotated[
    Union[
        FunctionCallOutputOutputOutputContentListInputText,
        FunctionCallOutputOutputOutputContentListInputImage,
        FunctionCallOutputOutputOutputContentListInputFile,
    ],
    PropertyInfo(discriminator="type"),
]


class FunctionCallOutput(BaseModel):
    id: str
    """The unique ID of the function call tool output."""

    call_id: str
    """The unique ID of the function tool call generated by the model."""

    output: Union[str, List[FunctionCallOutputOutputOutputContentList]]
    """
    The output from the function call generated by your code. Can be a string or an
    list of output content.
    """

    type: Literal["function_call_output"]
    """The type of the function tool call output. Always `function_call_output`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


class FileSearchCallResult(BaseModel):
    attributes: Optional[Dict[str, Union[str, float, bool]]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard. Keys are
    strings with a maximum length of 64 characters. Values are strings with a
    maximum length of 512 characters, booleans, or numbers.
    """

    file_id: Optional[str] = None
    """The unique ID of the file."""

    filename: Optional[str] = None
    """The name of the file."""

    score: Optional[float] = None
    """The relevance score of the file - a value between 0 and 1."""

    text: Optional[str] = None
    """The text that was retrieved from the file."""


class FileSearchCall(BaseModel):
    id: str
    """The unique ID of the file search tool call."""

    queries: List[str]
    """The queries used to search for files."""

    status: Literal["in_progress", "searching", "completed", "incomplete", "failed"]
    """The status of the file search tool call.

    One of `in_progress`, `searching`, `incomplete` or `failed`,
    """

    type: Literal["file_search_call"]
    """The type of the file search tool call. Always `file_search_call`."""

    results: Optional[List[FileSearchCallResult]] = None
    """The results of the file search tool call."""


class WebSearchCallActionSearchSource(BaseModel):
    type: Literal["url"]
    """The type of source. Always `url`."""

    url: str
    """The URL of the source."""


class WebSearchCallActionSearch(BaseModel):
    query: str
    """The search query."""

    type: Literal["search"]
    """The action type."""

    sources: Optional[List[WebSearchCallActionSearchSource]] = None
    """The sources used in the search."""


class WebSearchCallActionOpenPage(BaseModel):
    type: Literal["open_page"]
    """The action type."""

    url: str
    """The URL opened by the model."""


class WebSearchCallActionFind(BaseModel):
    pattern: str
    """The pattern or text to search for within the page."""

    type: Literal["find"]
    """The action type."""

    url: str
    """The URL of the page searched for the pattern."""


WebSearchCallAction: TypeAlias = Annotated[
    Union[WebSearchCallActionSearch, WebSearchCallActionOpenPage, WebSearchCallActionFind],
    PropertyInfo(discriminator="type"),
]


class WebSearchCall(BaseModel):
    id: str
    """The unique ID of the web search tool call."""

    action: WebSearchCallAction
    """
    An object describing the specific action taken in this web search call. Includes
    details on how the model used the web (search, open_page, find).
    """

    status: Literal["in_progress", "searching", "completed", "failed"]
    """The status of the web search tool call."""

    type: Literal["web_search_call"]
    """The type of the web search tool call. Always `web_search_call`."""


class ImageGenerationCall(BaseModel):
    id: str
    """The unique ID of the image generation call."""

    result: Optional[str] = None
    """The generated image encoded in base64."""

    status: Literal["in_progress", "completed", "generating", "failed"]
    """The status of the image generation call."""

    type: Literal["image_generation_call"]
    """The type of the image generation call. Always `image_generation_call`."""


class ComputerCallActionClick(BaseModel):
    button: Literal["left", "right", "wheel", "back", "forward"]
    """Indicates which mouse button was pressed during the click.

    One of `left`, `right`, `wheel`, `back`, or `forward`.
    """

    type: Literal["click"]
    """Specifies the event type.

    For a click action, this property is always set to `click`.
    """

    x: int
    """The x-coordinate where the click occurred."""

    y: int
    """The y-coordinate where the click occurred."""


class ComputerCallActionDoubleClick(BaseModel):
    type: Literal["double_click"]
    """Specifies the event type.

    For a double click action, this property is always set to `double_click`.
    """

    x: int
    """The x-coordinate where the double click occurred."""

    y: int
    """The y-coordinate where the double click occurred."""


class ComputerCallActionDragPath(BaseModel):
    x: int
    """The x-coordinate."""

    y: int
    """The y-coordinate."""


class ComputerCallActionDrag(BaseModel):
    path: List[ComputerCallActionDragPath]
    """An array of coordinates representing the path of the drag action.

    Coordinates will appear as an array of objects, eg

    ```
    [
      { x: 100, y: 200 },
      { x: 200, y: 300 }
    ]
    ```
    """

    type: Literal["drag"]
    """Specifies the event type.

    For a drag action, this property is always set to `drag`.
    """


class ComputerCallActionKeypress(BaseModel):
    keys: List[str]
    """The combination of keys the model is requesting to be pressed.

    This is an array of strings, each representing a key.
    """

    type: Literal["keypress"]
    """Specifies the event type.

    For a keypress action, this property is always set to `keypress`.
    """


class ComputerCallActionMove(BaseModel):
    type: Literal["move"]
    """Specifies the event type.

    For a move action, this property is always set to `move`.
    """

    x: int
    """The x-coordinate to move to."""

    y: int
    """The y-coordinate to move to."""


class ComputerCallActionScreenshot(BaseModel):
    type: Literal["screenshot"]
    """Specifies the event type.

    For a screenshot action, this property is always set to `screenshot`.
    """


class ComputerCallActionScroll(BaseModel):
    scroll_x: int
    """The horizontal scroll distance."""

    scroll_y: int
    """The vertical scroll distance."""

    type: Literal["scroll"]
    """Specifies the event type.

    For a scroll action, this property is always set to `scroll`.
    """

    x: int
    """The x-coordinate where the scroll occurred."""

    y: int
    """The y-coordinate where the scroll occurred."""


class ComputerCallActionType(BaseModel):
    text: str
    """The text to type."""

    type: Literal["type"]
    """Specifies the event type.

    For a type action, this property is always set to `type`.
    """


class ComputerCallActionWait(BaseModel):
    type: Literal["wait"]
    """Specifies the event type.

    For a wait action, this property is always set to `wait`.
    """


ComputerCallAction: TypeAlias = Annotated[
    Union[
        ComputerCallActionClick,
        ComputerCallActionDoubleClick,
        ComputerCallActionDrag,
        ComputerCallActionKeypress,
        ComputerCallActionMove,
        ComputerCallActionScreenshot,
        ComputerCallActionScroll,
        ComputerCallActionType,
        ComputerCallActionWait,
    ],
    PropertyInfo(discriminator="type"),
]


class ComputerCallPendingSafetyCheck(BaseModel):
    id: str
    """The ID of the pending safety check."""

    code: str
    """The type of the pending safety check."""

    message: str
    """Details about the pending safety check."""


class ComputerCall(BaseModel):
    id: str
    """The unique ID of the computer call."""

    action: ComputerCallAction
    """A click action."""

    call_id: str
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: List[ComputerCallPendingSafetyCheck]
    """The pending safety checks for the computer call."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Literal["computer_call"]
    """The type of the computer call. Always `computer_call`."""


class ComputerCallOutputOutput(BaseModel):
    type: Literal["computer_screenshot"]
    """Specifies the event type.

    For a computer screenshot, this property is always set to `computer_screenshot`.
    """

    file_id: Optional[str] = None
    """The identifier of an uploaded file that contains the screenshot."""

    image_url: Optional[str] = None
    """The URL of the screenshot image."""


class ComputerCallOutputAcknowledgedSafetyCheck(BaseModel):
    id: str
    """The ID of the pending safety check."""

    code: str
    """The type of the pending safety check."""

    message: str
    """Details about the pending safety check."""


class ComputerCallOutput(BaseModel):
    id: str
    """The unique ID of the computer call tool output."""

    call_id: str
    """The ID of the computer tool call that produced the output."""

    output: ComputerCallOutputOutput
    """A computer screenshot image used with the computer use tool."""

    type: Literal["computer_call_output"]
    """The type of the computer tool call output. Always `computer_call_output`."""

    acknowledged_safety_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]] = None
    """
    The safety checks reported by the API that have been acknowledged by the
    developer.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """


class ReasoningSummary(BaseModel):
    text: str
    """A summary of the reasoning output from the model so far."""

    type: Literal["summary_text"]
    """The type of the object. Always `summary_text`."""


class ReasoningContent(BaseModel):
    text: str
    """The reasoning text from the model."""

    type: Literal["reasoning_text"]
    """The type of the reasoning text. Always `reasoning_text`."""


class Reasoning(BaseModel):
    id: str
    """The unique identifier of the reasoning content."""

    summary: List[ReasoningSummary]
    """Reasoning summary content."""

    type: Literal["reasoning"]
    """The type of the object. Always `reasoning`."""

    content: Optional[List[ReasoningContent]] = None
    """Reasoning text content."""

    encrypted_content: Optional[str] = None
    """
    The encrypted content of the reasoning item - populated when a response is
    generated with `reasoning.encrypted_content` in the `include` parameter.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


class CodeInterpreterCallOutputLogs(BaseModel):
    logs: str
    """The logs output from the code interpreter."""

    type: Literal["logs"]
    """The type of the output. Always 'logs'."""


class CodeInterpreterCallOutputImage(BaseModel):
    type: Literal["image"]
    """The type of the output. Always 'image'."""

    url: str
    """The URL of the image output from the code interpreter."""


CodeInterpreterCallOutput: TypeAlias = Annotated[
    Union[CodeInterpreterCallOutputLogs, CodeInterpreterCallOutputImage], PropertyInfo(discriminator="type")
]


class CodeInterpreterCall(BaseModel):
    id: str
    """The unique ID of the code interpreter tool call."""

    code: Optional[str] = None
    """The code to run, or null if not available."""

    container_id: str
    """The ID of the container used to run the code."""

    outputs: Optional[List[CodeInterpreterCallOutput]] = None
    """
    The outputs generated by the code interpreter, such as logs or images. Can be
    null if no outputs are available.
    """

    status: Literal["in_progress", "completed", "incomplete", "interpreting", "failed"]
    """The status of the code interpreter tool call.

    Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and
    `failed`.
    """

    type: Literal["code_interpreter_call"]
    """The type of the code interpreter tool call. Always `code_interpreter_call`."""


class LocalShellCallAction(BaseModel):
    command: List[str]
    """The command to run."""

    env: Dict[str, str]
    """Environment variables to set for the command."""

    type: Literal["exec"]
    """The type of the local shell action. Always `exec`."""

    timeout_ms: Optional[int] = None
    """Optional timeout in milliseconds for the command."""

    user: Optional[str] = None
    """Optional user to run the command as."""

    working_directory: Optional[str] = None
    """Optional working directory to run the command in."""


class LocalShellCall(BaseModel):
    id: str
    """The unique ID of the local shell call."""

    action: LocalShellCallAction
    """Execute a shell command on the server."""

    call_id: str
    """The unique ID of the local shell tool call generated by the model."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the local shell call."""

    type: Literal["local_shell_call"]
    """The type of the local shell call. Always `local_shell_call`."""


class LocalShellCallOutput(BaseModel):
    id: str
    """The unique ID of the local shell tool call generated by the model."""

    output: str
    """A JSON string of the output of the local shell tool call."""

    type: Literal["local_shell_call_output"]
    """The type of the local shell tool call output. Always `local_shell_call_output`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item. One of `in_progress`, `completed`, or `incomplete`."""


class McpListToolsTool(BaseModel):
    input_schema: object
    """The JSON schema describing the tool's input."""

    name: str
    """The name of the tool."""

    annotations: Optional[object] = None
    """Additional annotations about the tool."""

    description: Optional[str] = None
    """The description of the tool."""


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


class McpApprovalRequest(BaseModel):
    id: str
    """The unique ID of the approval request."""

    arguments: str
    """A JSON string of arguments for the tool."""

    name: str
    """The name of the tool to run."""

    server_label: str
    """The label of the MCP server making the request."""

    type: Literal["mcp_approval_request"]
    """The type of the item. Always `mcp_approval_request`."""


class McpApprovalResponse(BaseModel):
    id: str
    """The unique ID of the approval response"""

    approval_request_id: str
    """The ID of the approval request being answered."""

    approve: bool
    """Whether the request was approved."""

    type: Literal["mcp_approval_response"]
    """The type of the item. Always `mcp_approval_response`."""

    reason: Optional[str] = None
    """Optional reason for the decision."""


class McpCall(BaseModel):
    id: str
    """The unique ID of the tool call."""

    arguments: str
    """A JSON string of the arguments passed to the tool."""

    name: str
    """The name of the tool that was run."""

    server_label: str
    """The label of the MCP server running the tool."""

    type: Literal["mcp_call"]
    """The type of the item. Always `mcp_call`."""

    approval_request_id: Optional[str] = None
    """
    Unique identifier for the MCP tool call approval request. Include this value in
    a subsequent `mcp_approval_response` input to approve or reject the
    corresponding tool call.
    """

    error: Optional[str] = None
    """The error from the tool call, if any."""

    output: Optional[str] = None
    """The output from the tool call."""

    status: Optional[Literal["in_progress", "completed", "incomplete", "calling", "failed"]] = None
    """The status of the tool call.

    One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.
    """


class CustomToolCall(BaseModel):
    call_id: str
    """An identifier used to map this custom tool call to a tool call output."""

    input: str
    """The input for the custom tool call generated by the model."""

    name: str
    """The name of the custom tool being called."""

    type: Literal["custom_tool_call"]
    """The type of the custom tool call. Always `custom_tool_call`."""

    id: Optional[str] = None
    """The unique ID of the custom tool call in the EXCai platform."""


class CustomToolCallOutputOutputOutputContentListInputText(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class CustomToolCallOutputOutputOutputContentListInputImage(BaseModel):
    detail: Literal["low", "high", "auto"]
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    type: Literal["input_image"]
    """The type of the input item. Always `input_image`."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    image_url: Optional[str] = None
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """


class CustomToolCallOutputOutputOutputContentListInputFile(BaseModel):
    type: Literal["input_file"]
    """The type of the input item. Always `input_file`."""

    file_data: Optional[str] = None
    """The content of the file to be sent to the model."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    file_url: Optional[str] = None
    """The URL of the file to be sent to the model."""

    filename: Optional[str] = None
    """The name of the file to be sent to the model."""


CustomToolCallOutputOutputOutputContentList: TypeAlias = Annotated[
    Union[
        CustomToolCallOutputOutputOutputContentListInputText,
        CustomToolCallOutputOutputOutputContentListInputImage,
        CustomToolCallOutputOutputOutputContentListInputFile,
    ],
    PropertyInfo(discriminator="type"),
]


class CustomToolCallOutput(BaseModel):
    call_id: str
    """The call ID, used to map this custom tool call output to a custom tool call."""

    output: Union[str, List[CustomToolCallOutputOutputOutputContentList]]
    """
    The output from the custom tool call generated by your code. Can be a string or
    an list of output content.
    """

    type: Literal["custom_tool_call_output"]
    """The type of the custom tool call output. Always `custom_tool_call_output`."""

    id: Optional[str] = None
    """The unique ID of the custom tool call output in the EXCai platform."""


ItemRetrieveResponse: TypeAlias = Annotated[
    Union[
        Message,
        FunctionCall,
        FunctionCallOutput,
        FileSearchCall,
        WebSearchCall,
        ImageGenerationCall,
        ComputerCall,
        ComputerCallOutput,
        Reasoning,
        CodeInterpreterCall,
        LocalShellCall,
        LocalShellCallOutput,
        McpListTools,
        McpApprovalRequest,
        McpApprovalResponse,
        McpCall,
        CustomToolCall,
        CustomToolCallOutput,
    ],
    PropertyInfo(discriminator="type"),
]
