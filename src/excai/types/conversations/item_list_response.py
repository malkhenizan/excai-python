# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ItemListResponse",
    "Data",
    "DataMessage",
    "DataMessageContent",
    "DataMessageContentInputText",
    "DataMessageContentOutputText",
    "DataMessageContentOutputTextAnnotation",
    "DataMessageContentOutputTextAnnotationFileCitation",
    "DataMessageContentOutputTextAnnotationURLCitation",
    "DataMessageContentOutputTextAnnotationContainerFileCitation",
    "DataMessageContentOutputTextAnnotationFilePath",
    "DataMessageContentOutputTextLogprob",
    "DataMessageContentOutputTextLogprobTopLogprob",
    "DataMessageContentText",
    "DataMessageContentSummaryText",
    "DataMessageContentReasoningText",
    "DataMessageContentRefusal",
    "DataMessageContentInputImage",
    "DataMessageContentComputerScreenshot",
    "DataMessageContentInputFile",
    "DataFunctionCall",
    "DataFunctionCallOutput",
    "DataFunctionCallOutputOutputOutputContentList",
    "DataFunctionCallOutputOutputOutputContentListInputText",
    "DataFunctionCallOutputOutputOutputContentListInputImage",
    "DataFunctionCallOutputOutputOutputContentListInputFile",
    "DataFileSearchCall",
    "DataFileSearchCallResult",
    "DataWebSearchCall",
    "DataWebSearchCallAction",
    "DataWebSearchCallActionSearch",
    "DataWebSearchCallActionSearchSource",
    "DataWebSearchCallActionOpenPage",
    "DataWebSearchCallActionFind",
    "DataImageGenerationCall",
    "DataComputerCall",
    "DataComputerCallAction",
    "DataComputerCallActionClick",
    "DataComputerCallActionDoubleClick",
    "DataComputerCallActionDrag",
    "DataComputerCallActionDragPath",
    "DataComputerCallActionKeypress",
    "DataComputerCallActionMove",
    "DataComputerCallActionScreenshot",
    "DataComputerCallActionScroll",
    "DataComputerCallActionType",
    "DataComputerCallActionWait",
    "DataComputerCallPendingSafetyCheck",
    "DataComputerCallOutput",
    "DataComputerCallOutputOutput",
    "DataComputerCallOutputAcknowledgedSafetyCheck",
    "DataReasoning",
    "DataReasoningSummary",
    "DataReasoningContent",
    "DataCodeInterpreterCall",
    "DataCodeInterpreterCallOutput",
    "DataCodeInterpreterCallOutputLogs",
    "DataCodeInterpreterCallOutputImage",
    "DataLocalShellCall",
    "DataLocalShellCallAction",
    "DataLocalShellCallOutput",
    "DataMcpListTools",
    "DataMcpListToolsTool",
    "DataMcpApprovalRequest",
    "DataMcpApprovalResponse",
    "DataMcpCall",
    "DataCustomToolCall",
    "DataCustomToolCallOutput",
    "DataCustomToolCallOutputOutputOutputContentList",
    "DataCustomToolCallOutputOutputOutputContentListInputText",
    "DataCustomToolCallOutputOutputOutputContentListInputImage",
    "DataCustomToolCallOutputOutputOutputContentListInputFile",
]


class DataMessageContentInputText(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataMessageContentOutputTextAnnotationFileCitation(BaseModel):
    file_id: str
    """The ID of the file."""

    filename: str
    """The filename of the file cited."""

    index: int
    """The index of the file in the list of files."""

    type: Literal["file_citation"]
    """The type of the file citation. Always `file_citation`."""


class DataMessageContentOutputTextAnnotationURLCitation(BaseModel):
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


class DataMessageContentOutputTextAnnotationContainerFileCitation(BaseModel):
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


class DataMessageContentOutputTextAnnotationFilePath(BaseModel):
    file_id: str
    """The ID of the file."""

    index: int
    """The index of the file in the list of files."""

    type: Literal["file_path"]
    """The type of the file path. Always `file_path`."""


DataMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        DataMessageContentOutputTextAnnotationFileCitation,
        DataMessageContentOutputTextAnnotationURLCitation,
        DataMessageContentOutputTextAnnotationContainerFileCitation,
        DataMessageContentOutputTextAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class DataMessageContentOutputTextLogprobTopLogprob(BaseModel):
    token: str

    bytes: List[int]

    logprob: float


class DataMessageContentOutputTextLogprob(BaseModel):
    token: str

    bytes: List[int]

    logprob: float

    top_logprobs: List[DataMessageContentOutputTextLogprobTopLogprob]


class DataMessageContentOutputText(BaseModel):
    annotations: List[DataMessageContentOutputTextAnnotation]
    """The annotations of the text output."""

    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""

    logprobs: Optional[List[DataMessageContentOutputTextLogprob]] = None


class DataMessageContentText(BaseModel):
    text: str

    type: Literal["text"]


class DataMessageContentSummaryText(BaseModel):
    text: str
    """A summary of the reasoning output from the model so far."""

    type: Literal["summary_text"]
    """The type of the object. Always `summary_text`."""


class DataMessageContentReasoningText(BaseModel):
    text: str
    """The reasoning text from the model."""

    type: Literal["reasoning_text"]
    """The type of the reasoning text. Always `reasoning_text`."""


class DataMessageContentRefusal(BaseModel):
    refusal: str
    """The refusal explanation from the model."""

    type: Literal["refusal"]
    """The type of the refusal. Always `refusal`."""


class DataMessageContentInputImage(BaseModel):
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


class DataMessageContentComputerScreenshot(BaseModel):
    file_id: Optional[str] = None
    """The identifier of an uploaded file that contains the screenshot."""

    image_url: Optional[str] = None
    """The URL of the screenshot image."""

    type: Literal["computer_screenshot"]
    """Specifies the event type.

    For a computer screenshot, this property is always set to `computer_screenshot`.
    """


class DataMessageContentInputFile(BaseModel):
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


DataMessageContent: TypeAlias = Annotated[
    Union[
        DataMessageContentInputText,
        DataMessageContentOutputText,
        DataMessageContentText,
        DataMessageContentSummaryText,
        DataMessageContentReasoningText,
        DataMessageContentRefusal,
        DataMessageContentInputImage,
        DataMessageContentComputerScreenshot,
        DataMessageContentInputFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataMessage(BaseModel):
    id: str
    """The unique ID of the message."""

    content: List[DataMessageContent]
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


class DataFunctionCall(BaseModel):
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


class DataFunctionCallOutputOutputOutputContentListInputText(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataFunctionCallOutputOutputOutputContentListInputImage(BaseModel):
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


class DataFunctionCallOutputOutputOutputContentListInputFile(BaseModel):
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


DataFunctionCallOutputOutputOutputContentList: TypeAlias = Annotated[
    Union[
        DataFunctionCallOutputOutputOutputContentListInputText,
        DataFunctionCallOutputOutputOutputContentListInputImage,
        DataFunctionCallOutputOutputOutputContentListInputFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataFunctionCallOutput(BaseModel):
    id: str
    """The unique ID of the function call tool output."""

    call_id: str
    """The unique ID of the function tool call generated by the model."""

    output: Union[str, List[DataFunctionCallOutputOutputOutputContentList]]
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


class DataFileSearchCallResult(BaseModel):
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


class DataFileSearchCall(BaseModel):
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

    results: Optional[List[DataFileSearchCallResult]] = None
    """The results of the file search tool call."""


class DataWebSearchCallActionSearchSource(BaseModel):
    type: Literal["url"]
    """The type of source. Always `url`."""

    url: str
    """The URL of the source."""


class DataWebSearchCallActionSearch(BaseModel):
    query: str
    """The search query."""

    type: Literal["search"]
    """The action type."""

    sources: Optional[List[DataWebSearchCallActionSearchSource]] = None
    """The sources used in the search."""


class DataWebSearchCallActionOpenPage(BaseModel):
    type: Literal["open_page"]
    """The action type."""

    url: str
    """The URL opened by the model."""


class DataWebSearchCallActionFind(BaseModel):
    pattern: str
    """The pattern or text to search for within the page."""

    type: Literal["find"]
    """The action type."""

    url: str
    """The URL of the page searched for the pattern."""


DataWebSearchCallAction: TypeAlias = Annotated[
    Union[DataWebSearchCallActionSearch, DataWebSearchCallActionOpenPage, DataWebSearchCallActionFind],
    PropertyInfo(discriminator="type"),
]


class DataWebSearchCall(BaseModel):
    id: str
    """The unique ID of the web search tool call."""

    action: DataWebSearchCallAction
    """
    An object describing the specific action taken in this web search call. Includes
    details on how the model used the web (search, open_page, find).
    """

    status: Literal["in_progress", "searching", "completed", "failed"]
    """The status of the web search tool call."""

    type: Literal["web_search_call"]
    """The type of the web search tool call. Always `web_search_call`."""


class DataImageGenerationCall(BaseModel):
    id: str
    """The unique ID of the image generation call."""

    result: Optional[str] = None
    """The generated image encoded in base64."""

    status: Literal["in_progress", "completed", "generating", "failed"]
    """The status of the image generation call."""

    type: Literal["image_generation_call"]
    """The type of the image generation call. Always `image_generation_call`."""


class DataComputerCallActionClick(BaseModel):
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


class DataComputerCallActionDoubleClick(BaseModel):
    type: Literal["double_click"]
    """Specifies the event type.

    For a double click action, this property is always set to `double_click`.
    """

    x: int
    """The x-coordinate where the double click occurred."""

    y: int
    """The y-coordinate where the double click occurred."""


class DataComputerCallActionDragPath(BaseModel):
    x: int
    """The x-coordinate."""

    y: int
    """The y-coordinate."""


class DataComputerCallActionDrag(BaseModel):
    path: List[DataComputerCallActionDragPath]
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


class DataComputerCallActionKeypress(BaseModel):
    keys: List[str]
    """The combination of keys the model is requesting to be pressed.

    This is an array of strings, each representing a key.
    """

    type: Literal["keypress"]
    """Specifies the event type.

    For a keypress action, this property is always set to `keypress`.
    """


class DataComputerCallActionMove(BaseModel):
    type: Literal["move"]
    """Specifies the event type.

    For a move action, this property is always set to `move`.
    """

    x: int
    """The x-coordinate to move to."""

    y: int
    """The y-coordinate to move to."""


class DataComputerCallActionScreenshot(BaseModel):
    type: Literal["screenshot"]
    """Specifies the event type.

    For a screenshot action, this property is always set to `screenshot`.
    """


class DataComputerCallActionScroll(BaseModel):
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


class DataComputerCallActionType(BaseModel):
    text: str
    """The text to type."""

    type: Literal["type"]
    """Specifies the event type.

    For a type action, this property is always set to `type`.
    """


class DataComputerCallActionWait(BaseModel):
    type: Literal["wait"]
    """Specifies the event type.

    For a wait action, this property is always set to `wait`.
    """


DataComputerCallAction: TypeAlias = Annotated[
    Union[
        DataComputerCallActionClick,
        DataComputerCallActionDoubleClick,
        DataComputerCallActionDrag,
        DataComputerCallActionKeypress,
        DataComputerCallActionMove,
        DataComputerCallActionScreenshot,
        DataComputerCallActionScroll,
        DataComputerCallActionType,
        DataComputerCallActionWait,
    ],
    PropertyInfo(discriminator="type"),
]


class DataComputerCallPendingSafetyCheck(BaseModel):
    id: str
    """The ID of the pending safety check."""

    code: str
    """The type of the pending safety check."""

    message: str
    """Details about the pending safety check."""


class DataComputerCall(BaseModel):
    id: str
    """The unique ID of the computer call."""

    action: DataComputerCallAction
    """A click action."""

    call_id: str
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: List[DataComputerCallPendingSafetyCheck]
    """The pending safety checks for the computer call."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Literal["computer_call"]
    """The type of the computer call. Always `computer_call`."""


class DataComputerCallOutputOutput(BaseModel):
    type: Literal["computer_screenshot"]
    """Specifies the event type.

    For a computer screenshot, this property is always set to `computer_screenshot`.
    """

    file_id: Optional[str] = None
    """The identifier of an uploaded file that contains the screenshot."""

    image_url: Optional[str] = None
    """The URL of the screenshot image."""


class DataComputerCallOutputAcknowledgedSafetyCheck(BaseModel):
    id: str
    """The ID of the pending safety check."""

    code: str
    """The type of the pending safety check."""

    message: str
    """Details about the pending safety check."""


class DataComputerCallOutput(BaseModel):
    id: str
    """The unique ID of the computer call tool output."""

    call_id: str
    """The ID of the computer tool call that produced the output."""

    output: DataComputerCallOutputOutput
    """A computer screenshot image used with the computer use tool."""

    type: Literal["computer_call_output"]
    """The type of the computer tool call output. Always `computer_call_output`."""

    acknowledged_safety_checks: Optional[List[DataComputerCallOutputAcknowledgedSafetyCheck]] = None
    """
    The safety checks reported by the API that have been acknowledged by the
    developer.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """


class DataReasoningSummary(BaseModel):
    text: str
    """A summary of the reasoning output from the model so far."""

    type: Literal["summary_text"]
    """The type of the object. Always `summary_text`."""


class DataReasoningContent(BaseModel):
    text: str
    """The reasoning text from the model."""

    type: Literal["reasoning_text"]
    """The type of the reasoning text. Always `reasoning_text`."""


class DataReasoning(BaseModel):
    id: str
    """The unique identifier of the reasoning content."""

    summary: List[DataReasoningSummary]
    """Reasoning summary content."""

    type: Literal["reasoning"]
    """The type of the object. Always `reasoning`."""

    content: Optional[List[DataReasoningContent]] = None
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


class DataCodeInterpreterCallOutputLogs(BaseModel):
    logs: str
    """The logs output from the code interpreter."""

    type: Literal["logs"]
    """The type of the output. Always 'logs'."""


class DataCodeInterpreterCallOutputImage(BaseModel):
    type: Literal["image"]
    """The type of the output. Always 'image'."""

    url: str
    """The URL of the image output from the code interpreter."""


DataCodeInterpreterCallOutput: TypeAlias = Annotated[
    Union[DataCodeInterpreterCallOutputLogs, DataCodeInterpreterCallOutputImage], PropertyInfo(discriminator="type")
]


class DataCodeInterpreterCall(BaseModel):
    id: str
    """The unique ID of the code interpreter tool call."""

    code: Optional[str] = None
    """The code to run, or null if not available."""

    container_id: str
    """The ID of the container used to run the code."""

    outputs: Optional[List[DataCodeInterpreterCallOutput]] = None
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


class DataLocalShellCallAction(BaseModel):
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


class DataLocalShellCall(BaseModel):
    id: str
    """The unique ID of the local shell call."""

    action: DataLocalShellCallAction
    """Execute a shell command on the server."""

    call_id: str
    """The unique ID of the local shell tool call generated by the model."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the local shell call."""

    type: Literal["local_shell_call"]
    """The type of the local shell call. Always `local_shell_call`."""


class DataLocalShellCallOutput(BaseModel):
    id: str
    """The unique ID of the local shell tool call generated by the model."""

    output: str
    """A JSON string of the output of the local shell tool call."""

    type: Literal["local_shell_call_output"]
    """The type of the local shell tool call output. Always `local_shell_call_output`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item. One of `in_progress`, `completed`, or `incomplete`."""


class DataMcpListToolsTool(BaseModel):
    input_schema: object
    """The JSON schema describing the tool's input."""

    name: str
    """The name of the tool."""

    annotations: Optional[object] = None
    """Additional annotations about the tool."""

    description: Optional[str] = None
    """The description of the tool."""


class DataMcpListTools(BaseModel):
    id: str
    """The unique ID of the list."""

    server_label: str
    """The label of the MCP server."""

    tools: List[DataMcpListToolsTool]
    """The tools available on the server."""

    type: Literal["mcp_list_tools"]
    """The type of the item. Always `mcp_list_tools`."""

    error: Optional[str] = None
    """Error message if the server could not list tools."""


class DataMcpApprovalRequest(BaseModel):
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


class DataMcpApprovalResponse(BaseModel):
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


class DataMcpCall(BaseModel):
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


class DataCustomToolCall(BaseModel):
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


class DataCustomToolCallOutputOutputOutputContentListInputText(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataCustomToolCallOutputOutputOutputContentListInputImage(BaseModel):
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


class DataCustomToolCallOutputOutputOutputContentListInputFile(BaseModel):
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


DataCustomToolCallOutputOutputOutputContentList: TypeAlias = Annotated[
    Union[
        DataCustomToolCallOutputOutputOutputContentListInputText,
        DataCustomToolCallOutputOutputOutputContentListInputImage,
        DataCustomToolCallOutputOutputOutputContentListInputFile,
    ],
    PropertyInfo(discriminator="type"),
]


class DataCustomToolCallOutput(BaseModel):
    call_id: str
    """The call ID, used to map this custom tool call output to a custom tool call."""

    output: Union[str, List[DataCustomToolCallOutputOutputOutputContentList]]
    """
    The output from the custom tool call generated by your code. Can be a string or
    an list of output content.
    """

    type: Literal["custom_tool_call_output"]
    """The type of the custom tool call output. Always `custom_tool_call_output`."""

    id: Optional[str] = None
    """The unique ID of the custom tool call output in the EXCai platform."""


Data: TypeAlias = Annotated[
    Union[
        DataMessage,
        DataFunctionCall,
        DataFunctionCallOutput,
        DataFileSearchCall,
        DataWebSearchCall,
        DataImageGenerationCall,
        DataComputerCall,
        DataComputerCallOutput,
        DataReasoning,
        DataCodeInterpreterCall,
        DataLocalShellCall,
        DataLocalShellCallOutput,
        DataMcpListTools,
        DataMcpApprovalRequest,
        DataMcpApprovalResponse,
        DataMcpCall,
        DataCustomToolCall,
        DataCustomToolCallOutput,
    ],
    PropertyInfo(discriminator="type"),
]


class ItemListResponse(BaseModel):
    data: List[Data]
    """A list of conversation items."""

    first_id: str
    """The ID of the first item in the list."""

    has_more: bool
    """Whether there are more items available."""

    last_id: str
    """The ID of the last item in the list."""

    object: Literal["list"]
    """The type of object returned, must be `list`."""
