# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ResponseCreateResponse",
    "Error",
    "IncompleteDetails",
    "InstructionsInputItemList",
    "InstructionsInputItemListMessage",
    "InstructionsInputItemListMessageContentInputMessageContentList",
    "InstructionsInputItemListMessageContentInputMessageContentListInputText",
    "InstructionsInputItemListMessageContentInputMessageContentListInputImage",
    "InstructionsInputItemListMessageContentInputMessageContentListInputFile",
    "InstructionsInputItemListMessageContentInputMessageContentListInputAudio",
    "InstructionsInputItemListMessageContentInputMessageContentListInputAudioInputAudio",
    "InstructionsInputItemListFileSearchCall",
    "InstructionsInputItemListFileSearchCallResult",
    "InstructionsInputItemListComputerCall",
    "InstructionsInputItemListComputerCallAction",
    "InstructionsInputItemListComputerCallActionClick",
    "InstructionsInputItemListComputerCallActionDoubleClick",
    "InstructionsInputItemListComputerCallActionDrag",
    "InstructionsInputItemListComputerCallActionDragPath",
    "InstructionsInputItemListComputerCallActionKeypress",
    "InstructionsInputItemListComputerCallActionMove",
    "InstructionsInputItemListComputerCallActionScreenshot",
    "InstructionsInputItemListComputerCallActionScroll",
    "InstructionsInputItemListComputerCallActionType",
    "InstructionsInputItemListComputerCallActionWait",
    "InstructionsInputItemListComputerCallPendingSafetyCheck",
    "InstructionsInputItemListComputerCallOutput",
    "InstructionsInputItemListComputerCallOutputOutput",
    "InstructionsInputItemListComputerCallOutputAcknowledgedSafetyCheck",
    "InstructionsInputItemListWebSearchCall",
    "InstructionsInputItemListWebSearchCallAction",
    "InstructionsInputItemListWebSearchCallActionSearch",
    "InstructionsInputItemListWebSearchCallActionSearchSource",
    "InstructionsInputItemListWebSearchCallActionOpenPage",
    "InstructionsInputItemListWebSearchCallActionFind",
    "InstructionsInputItemListFunctionCall",
    "InstructionsInputItemListFunctionCallOutput",
    "InstructionsInputItemListFunctionCallOutputOutputUnionMember1",
    "InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputText",
    "InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputImage",
    "InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputFile",
    "InstructionsInputItemListReasoning",
    "InstructionsInputItemListReasoningSummary",
    "InstructionsInputItemListReasoningContent",
    "InstructionsInputItemListImageGenerationCall",
    "InstructionsInputItemListCodeInterpreterCall",
    "InstructionsInputItemListCodeInterpreterCallOutput",
    "InstructionsInputItemListCodeInterpreterCallOutputLogs",
    "InstructionsInputItemListCodeInterpreterCallOutputImage",
    "InstructionsInputItemListLocalShellCall",
    "InstructionsInputItemListLocalShellCallAction",
    "InstructionsInputItemListLocalShellCallOutput",
    "InstructionsInputItemListMcpListTools",
    "InstructionsInputItemListMcpListToolsTool",
    "InstructionsInputItemListMcpApprovalRequest",
    "InstructionsInputItemListMcpApprovalResponse",
    "InstructionsInputItemListMcpCall",
    "InstructionsInputItemListCustomToolCallOutput",
    "InstructionsInputItemListCustomToolCallOutputOutputOutputContentList",
    "InstructionsInputItemListCustomToolCallOutputOutputOutputContentListInputText",
    "InstructionsInputItemListCustomToolCallOutputOutputOutputContentListInputImage",
    "InstructionsInputItemListCustomToolCallOutputOutputOutputContentListInputFile",
    "InstructionsInputItemListCustomToolCall",
    "InstructionsInputItemListItemReference",
    "Output",
    "OutputMessage",
    "OutputMessageContent",
    "OutputMessageContentOutputText",
    "OutputMessageContentOutputTextAnnotation",
    "OutputMessageContentOutputTextAnnotationFileCitation",
    "OutputMessageContentOutputTextAnnotationURLCitation",
    "OutputMessageContentOutputTextAnnotationContainerFileCitation",
    "OutputMessageContentOutputTextAnnotationFilePath",
    "OutputMessageContentOutputTextLogprob",
    "OutputMessageContentOutputTextLogprobTopLogprob",
    "OutputMessageContentRefusal",
    "OutputFileSearchCall",
    "OutputFileSearchCallResult",
    "OutputFunctionCall",
    "OutputWebSearchCall",
    "OutputWebSearchCallAction",
    "OutputWebSearchCallActionSearch",
    "OutputWebSearchCallActionSearchSource",
    "OutputWebSearchCallActionOpenPage",
    "OutputWebSearchCallActionFind",
    "OutputComputerCall",
    "OutputComputerCallAction",
    "OutputComputerCallActionClick",
    "OutputComputerCallActionDoubleClick",
    "OutputComputerCallActionDrag",
    "OutputComputerCallActionDragPath",
    "OutputComputerCallActionKeypress",
    "OutputComputerCallActionMove",
    "OutputComputerCallActionScreenshot",
    "OutputComputerCallActionScroll",
    "OutputComputerCallActionType",
    "OutputComputerCallActionWait",
    "OutputComputerCallPendingSafetyCheck",
    "OutputReasoning",
    "OutputReasoningSummary",
    "OutputReasoningContent",
    "OutputImageGenerationCall",
    "OutputCodeInterpreterCall",
    "OutputCodeInterpreterCallOutput",
    "OutputCodeInterpreterCallOutputLogs",
    "OutputCodeInterpreterCallOutputImage",
    "OutputLocalShellCall",
    "OutputLocalShellCallAction",
    "OutputMcpCall",
    "OutputMcpListTools",
    "OutputMcpListToolsTool",
    "OutputMcpApprovalRequest",
    "OutputCustomToolCall",
    "ToolChoice",
    "ToolChoiceToolChoiceAllowed",
    "ToolChoiceToolChoiceTypes",
    "ToolChoiceToolChoiceFunction",
    "ToolChoiceToolChoiceMcp",
    "ToolChoiceToolChoiceCustom",
    "Tool",
    "ToolFunction",
    "ToolFileSearch",
    "ToolFileSearchFilters",
    "ToolFileSearchFiltersComparisonFilter",
    "ToolFileSearchFiltersCompoundFilter",
    "ToolFileSearchFiltersCompoundFilterFilter",
    "ToolFileSearchFiltersCompoundFilterFilterComparisonFilter",
    "ToolFileSearchRankingOptions",
    "ToolComputerUsePreview",
    "ToolWebSearchTool",
    "ToolWebSearchToolFilters",
    "ToolWebSearchToolUserLocation",
    "ToolMcp",
    "ToolMcpAllowedTools",
    "ToolMcpAllowedToolsMcpToolFilter",
    "ToolMcpRequireApproval",
    "ToolMcpRequireApprovalMcpToolApprovalFilter",
    "ToolMcpRequireApprovalMcpToolApprovalFilterAlways",
    "ToolMcpRequireApprovalMcpToolApprovalFilterNever",
    "ToolCodeInterpreter",
    "ToolCodeInterpreterContainer",
    "ToolCodeInterpreterContainerCodeInterpreterToolAuto",
    "ToolImageGeneration",
    "ToolImageGenerationInputImageMask",
    "ToolLocalShell",
    "ToolCustom",
    "ToolCustomFormat",
    "ToolCustomFormatText",
    "ToolCustomFormatGrammar",
    "ToolWebSearchPreviewTool",
    "ToolWebSearchPreviewToolUserLocation",
    "Conversation",
    "Prompt",
    "PromptVariables",
    "PromptVariablesInputTextContent",
    "PromptVariablesInputImageContent",
    "PromptVariablesInputFileContent",
    "Reasoning",
    "Text",
    "TextFormat",
    "TextFormatText",
    "TextFormatJsonSchema",
    "TextFormatJsonObject",
    "Usage",
    "UsageInputTokensDetails",
    "UsageOutputTokensDetails",
]


class Error(BaseModel):
    code: Literal[
        "server_error",
        "rate_limit_exceeded",
        "invalid_prompt",
        "vector_store_timeout",
        "invalid_image",
        "invalid_image_format",
        "invalid_base64_image",
        "invalid_image_url",
        "image_too_large",
        "image_too_small",
        "image_parse_error",
        "image_content_policy_violation",
        "invalid_image_mode",
        "image_file_too_large",
        "unsupported_image_media_type",
        "empty_image_file",
        "failed_to_download_image",
        "image_file_not_found",
    ]
    """The error code for the response."""

    message: str
    """A human-readable description of the error."""


class IncompleteDetails(BaseModel):
    reason: Optional[Literal["max_output_tokens", "content_filter"]] = None
    """The reason why the response is incomplete."""


class InstructionsInputItemListMessageContentInputMessageContentListInputText(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class InstructionsInputItemListMessageContentInputMessageContentListInputImage(BaseModel):
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


class InstructionsInputItemListMessageContentInputMessageContentListInputFile(BaseModel):
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


class InstructionsInputItemListMessageContentInputMessageContentListInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class InstructionsInputItemListMessageContentInputMessageContentListInputAudio(BaseModel):
    input_audio: InstructionsInputItemListMessageContentInputMessageContentListInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


InstructionsInputItemListMessageContentInputMessageContentList: TypeAlias = Annotated[
    Union[
        InstructionsInputItemListMessageContentInputMessageContentListInputText,
        InstructionsInputItemListMessageContentInputMessageContentListInputImage,
        InstructionsInputItemListMessageContentInputMessageContentListInputFile,
        InstructionsInputItemListMessageContentInputMessageContentListInputAudio,
    ],
    PropertyInfo(discriminator="type"),
]


class InstructionsInputItemListMessage(BaseModel):
    content: Union[str, List[InstructionsInputItemListMessageContentInputMessageContentList]]
    """
    Text, image, or audio input to the model, used to generate a response. Can also
    contain previous assistant responses.
    """

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class InstructionsInputItemListFileSearchCallResult(BaseModel):
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


class InstructionsInputItemListFileSearchCall(BaseModel):
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

    results: Optional[List[InstructionsInputItemListFileSearchCallResult]] = None
    """The results of the file search tool call."""


class InstructionsInputItemListComputerCallActionClick(BaseModel):
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


class InstructionsInputItemListComputerCallActionDoubleClick(BaseModel):
    type: Literal["double_click"]
    """Specifies the event type.

    For a double click action, this property is always set to `double_click`.
    """

    x: int
    """The x-coordinate where the double click occurred."""

    y: int
    """The y-coordinate where the double click occurred."""


class InstructionsInputItemListComputerCallActionDragPath(BaseModel):
    x: int
    """The x-coordinate."""

    y: int
    """The y-coordinate."""


class InstructionsInputItemListComputerCallActionDrag(BaseModel):
    path: List[InstructionsInputItemListComputerCallActionDragPath]
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


class InstructionsInputItemListComputerCallActionKeypress(BaseModel):
    keys: List[str]
    """The combination of keys the model is requesting to be pressed.

    This is an array of strings, each representing a key.
    """

    type: Literal["keypress"]
    """Specifies the event type.

    For a keypress action, this property is always set to `keypress`.
    """


class InstructionsInputItemListComputerCallActionMove(BaseModel):
    type: Literal["move"]
    """Specifies the event type.

    For a move action, this property is always set to `move`.
    """

    x: int
    """The x-coordinate to move to."""

    y: int
    """The y-coordinate to move to."""


class InstructionsInputItemListComputerCallActionScreenshot(BaseModel):
    type: Literal["screenshot"]
    """Specifies the event type.

    For a screenshot action, this property is always set to `screenshot`.
    """


class InstructionsInputItemListComputerCallActionScroll(BaseModel):
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


class InstructionsInputItemListComputerCallActionType(BaseModel):
    text: str
    """The text to type."""

    type: Literal["type"]
    """Specifies the event type.

    For a type action, this property is always set to `type`.
    """


class InstructionsInputItemListComputerCallActionWait(BaseModel):
    type: Literal["wait"]
    """Specifies the event type.

    For a wait action, this property is always set to `wait`.
    """


InstructionsInputItemListComputerCallAction: TypeAlias = Annotated[
    Union[
        InstructionsInputItemListComputerCallActionClick,
        InstructionsInputItemListComputerCallActionDoubleClick,
        InstructionsInputItemListComputerCallActionDrag,
        InstructionsInputItemListComputerCallActionKeypress,
        InstructionsInputItemListComputerCallActionMove,
        InstructionsInputItemListComputerCallActionScreenshot,
        InstructionsInputItemListComputerCallActionScroll,
        InstructionsInputItemListComputerCallActionType,
        InstructionsInputItemListComputerCallActionWait,
    ],
    PropertyInfo(discriminator="type"),
]


class InstructionsInputItemListComputerCallPendingSafetyCheck(BaseModel):
    id: str
    """The ID of the pending safety check."""

    code: str
    """The type of the pending safety check."""

    message: str
    """Details about the pending safety check."""


class InstructionsInputItemListComputerCall(BaseModel):
    id: str
    """The unique ID of the computer call."""

    action: InstructionsInputItemListComputerCallAction
    """A click action."""

    call_id: str
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: List[InstructionsInputItemListComputerCallPendingSafetyCheck]
    """The pending safety checks for the computer call."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Literal["computer_call"]
    """The type of the computer call. Always `computer_call`."""


class InstructionsInputItemListComputerCallOutputOutput(BaseModel):
    type: Literal["computer_screenshot"]
    """Specifies the event type.

    For a computer screenshot, this property is always set to `computer_screenshot`.
    """

    file_id: Optional[str] = None
    """The identifier of an uploaded file that contains the screenshot."""

    image_url: Optional[str] = None
    """The URL of the screenshot image."""


class InstructionsInputItemListComputerCallOutputAcknowledgedSafetyCheck(BaseModel):
    id: str
    """The ID of the pending safety check."""

    code: Optional[str] = None
    """The type of the pending safety check."""

    message: Optional[str] = None
    """Details about the pending safety check."""


class InstructionsInputItemListComputerCallOutput(BaseModel):
    call_id: str
    """The ID of the computer tool call that produced the output."""

    output: InstructionsInputItemListComputerCallOutputOutput
    """A computer screenshot image used with the computer use tool."""

    type: Literal["computer_call_output"]
    """The type of the computer tool call output. Always `computer_call_output`."""

    id: Optional[str] = None
    """The ID of the computer tool call output."""

    acknowledged_safety_checks: Optional[List[InstructionsInputItemListComputerCallOutputAcknowledgedSafetyCheck]] = (
        None
    )
    """
    The safety checks reported by the API that have been acknowledged by the
    developer.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """


class InstructionsInputItemListWebSearchCallActionSearchSource(BaseModel):
    type: Literal["url"]
    """The type of source. Always `url`."""

    url: str
    """The URL of the source."""


class InstructionsInputItemListWebSearchCallActionSearch(BaseModel):
    query: str
    """The search query."""

    type: Literal["search"]
    """The action type."""

    sources: Optional[List[InstructionsInputItemListWebSearchCallActionSearchSource]] = None
    """The sources used in the search."""


class InstructionsInputItemListWebSearchCallActionOpenPage(BaseModel):
    type: Literal["open_page"]
    """The action type."""

    url: str
    """The URL opened by the model."""


class InstructionsInputItemListWebSearchCallActionFind(BaseModel):
    pattern: str
    """The pattern or text to search for within the page."""

    type: Literal["find"]
    """The action type."""

    url: str
    """The URL of the page searched for the pattern."""


InstructionsInputItemListWebSearchCallAction: TypeAlias = Annotated[
    Union[
        InstructionsInputItemListWebSearchCallActionSearch,
        InstructionsInputItemListWebSearchCallActionOpenPage,
        InstructionsInputItemListWebSearchCallActionFind,
    ],
    PropertyInfo(discriminator="type"),
]


class InstructionsInputItemListWebSearchCall(BaseModel):
    id: str
    """The unique ID of the web search tool call."""

    action: InstructionsInputItemListWebSearchCallAction
    """
    An object describing the specific action taken in this web search call. Includes
    details on how the model used the web (search, open_page, find).
    """

    status: Literal["in_progress", "searching", "completed", "failed"]
    """The status of the web search tool call."""

    type: Literal["web_search_call"]
    """The type of the web search tool call. Always `web_search_call`."""


class InstructionsInputItemListFunctionCall(BaseModel):
    arguments: str
    """A JSON string of the arguments to pass to the function."""

    call_id: str
    """The unique ID of the function tool call generated by the model."""

    name: str
    """The name of the function to run."""

    type: Literal["function_call"]
    """The type of the function tool call. Always `function_call`."""

    id: Optional[str] = None
    """The unique ID of the function tool call."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


class InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputText(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputImage(BaseModel):
    type: Literal["input_image"]
    """The type of the input item. Always `input_image`."""

    detail: Optional[Literal["low", "high", "auto"]] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    image_url: Optional[str] = None
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """


class InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputFile(BaseModel):
    type: Literal["input_file"]
    """The type of the input item. Always `input_file`."""

    file_data: Optional[str] = None
    """The base64-encoded data of the file to be sent to the model."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    file_url: Optional[str] = None
    """The URL of the file to be sent to the model."""

    filename: Optional[str] = None
    """The name of the file to be sent to the model."""


InstructionsInputItemListFunctionCallOutputOutputUnionMember1: TypeAlias = Annotated[
    Union[
        InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputText,
        InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputImage,
        InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputFile,
    ],
    PropertyInfo(discriminator="type"),
]


class InstructionsInputItemListFunctionCallOutput(BaseModel):
    call_id: str
    """The unique ID of the function tool call generated by the model."""

    output: Union[str, List[InstructionsInputItemListFunctionCallOutputOutputUnionMember1]]
    """Text, image, or file output of the function tool call."""

    type: Literal["function_call_output"]
    """The type of the function tool call output. Always `function_call_output`."""

    id: Optional[str] = None
    """The unique ID of the function tool call output.

    Populated when this item is returned via API.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


class InstructionsInputItemListReasoningSummary(BaseModel):
    text: str
    """A summary of the reasoning output from the model so far."""

    type: Literal["summary_text"]
    """The type of the object. Always `summary_text`."""


class InstructionsInputItemListReasoningContent(BaseModel):
    text: str
    """The reasoning text from the model."""

    type: Literal["reasoning_text"]
    """The type of the reasoning text. Always `reasoning_text`."""


class InstructionsInputItemListReasoning(BaseModel):
    id: str
    """The unique identifier of the reasoning content."""

    summary: List[InstructionsInputItemListReasoningSummary]
    """Reasoning summary content."""

    type: Literal["reasoning"]
    """The type of the object. Always `reasoning`."""

    content: Optional[List[InstructionsInputItemListReasoningContent]] = None
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


class InstructionsInputItemListImageGenerationCall(BaseModel):
    id: str
    """The unique ID of the image generation call."""

    result: Optional[str] = None
    """The generated image encoded in base64."""

    status: Literal["in_progress", "completed", "generating", "failed"]
    """The status of the image generation call."""

    type: Literal["image_generation_call"]
    """The type of the image generation call. Always `image_generation_call`."""


class InstructionsInputItemListCodeInterpreterCallOutputLogs(BaseModel):
    logs: str
    """The logs output from the code interpreter."""

    type: Literal["logs"]
    """The type of the output. Always 'logs'."""


class InstructionsInputItemListCodeInterpreterCallOutputImage(BaseModel):
    type: Literal["image"]
    """The type of the output. Always 'image'."""

    url: str
    """The URL of the image output from the code interpreter."""


InstructionsInputItemListCodeInterpreterCallOutput: TypeAlias = Annotated[
    Union[
        InstructionsInputItemListCodeInterpreterCallOutputLogs, InstructionsInputItemListCodeInterpreterCallOutputImage
    ],
    PropertyInfo(discriminator="type"),
]


class InstructionsInputItemListCodeInterpreterCall(BaseModel):
    id: str
    """The unique ID of the code interpreter tool call."""

    code: Optional[str] = None
    """The code to run, or null if not available."""

    container_id: str
    """The ID of the container used to run the code."""

    outputs: Optional[List[InstructionsInputItemListCodeInterpreterCallOutput]] = None
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


class InstructionsInputItemListLocalShellCallAction(BaseModel):
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


class InstructionsInputItemListLocalShellCall(BaseModel):
    id: str
    """The unique ID of the local shell call."""

    action: InstructionsInputItemListLocalShellCallAction
    """Execute a shell command on the server."""

    call_id: str
    """The unique ID of the local shell tool call generated by the model."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the local shell call."""

    type: Literal["local_shell_call"]
    """The type of the local shell call. Always `local_shell_call`."""


class InstructionsInputItemListLocalShellCallOutput(BaseModel):
    id: str
    """The unique ID of the local shell tool call generated by the model."""

    output: str
    """A JSON string of the output of the local shell tool call."""

    type: Literal["local_shell_call_output"]
    """The type of the local shell tool call output. Always `local_shell_call_output`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item. One of `in_progress`, `completed`, or `incomplete`."""


class InstructionsInputItemListMcpListToolsTool(BaseModel):
    input_schema: object
    """The JSON schema describing the tool's input."""

    name: str
    """The name of the tool."""

    annotations: Optional[object] = None
    """Additional annotations about the tool."""

    description: Optional[str] = None
    """The description of the tool."""


class InstructionsInputItemListMcpListTools(BaseModel):
    id: str
    """The unique ID of the list."""

    server_label: str
    """The label of the MCP server."""

    tools: List[InstructionsInputItemListMcpListToolsTool]
    """The tools available on the server."""

    type: Literal["mcp_list_tools"]
    """The type of the item. Always `mcp_list_tools`."""

    error: Optional[str] = None
    """Error message if the server could not list tools."""


class InstructionsInputItemListMcpApprovalRequest(BaseModel):
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


class InstructionsInputItemListMcpApprovalResponse(BaseModel):
    approval_request_id: str
    """The ID of the approval request being answered."""

    approve: bool
    """Whether the request was approved."""

    type: Literal["mcp_approval_response"]
    """The type of the item. Always `mcp_approval_response`."""

    id: Optional[str] = None
    """The unique ID of the approval response"""

    reason: Optional[str] = None
    """Optional reason for the decision."""


class InstructionsInputItemListMcpCall(BaseModel):
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


class InstructionsInputItemListCustomToolCallOutputOutputOutputContentListInputText(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class InstructionsInputItemListCustomToolCallOutputOutputOutputContentListInputImage(BaseModel):
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


class InstructionsInputItemListCustomToolCallOutputOutputOutputContentListInputFile(BaseModel):
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


InstructionsInputItemListCustomToolCallOutputOutputOutputContentList: TypeAlias = Annotated[
    Union[
        InstructionsInputItemListCustomToolCallOutputOutputOutputContentListInputText,
        InstructionsInputItemListCustomToolCallOutputOutputOutputContentListInputImage,
        InstructionsInputItemListCustomToolCallOutputOutputOutputContentListInputFile,
    ],
    PropertyInfo(discriminator="type"),
]


class InstructionsInputItemListCustomToolCallOutput(BaseModel):
    call_id: str
    """The call ID, used to map this custom tool call output to a custom tool call."""

    output: Union[str, List[InstructionsInputItemListCustomToolCallOutputOutputOutputContentList]]
    """
    The output from the custom tool call generated by your code. Can be a string or
    an list of output content.
    """

    type: Literal["custom_tool_call_output"]
    """The type of the custom tool call output. Always `custom_tool_call_output`."""

    id: Optional[str] = None
    """The unique ID of the custom tool call output in the EXCai platform."""


class InstructionsInputItemListCustomToolCall(BaseModel):
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


class InstructionsInputItemListItemReference(BaseModel):
    id: str
    """The ID of the item to reference."""

    type: Optional[Literal["item_reference"]] = None
    """The type of item to reference. Always `item_reference`."""


InstructionsInputItemList: TypeAlias = Annotated[
    Union[
        InstructionsInputItemListMessage,
        InstructionsInputItemListMessage,
        InstructionsInputItemListMessage,
        InstructionsInputItemListFileSearchCall,
        InstructionsInputItemListComputerCall,
        InstructionsInputItemListComputerCallOutput,
        InstructionsInputItemListWebSearchCall,
        InstructionsInputItemListFunctionCall,
        InstructionsInputItemListFunctionCallOutput,
        InstructionsInputItemListReasoning,
        InstructionsInputItemListImageGenerationCall,
        InstructionsInputItemListCodeInterpreterCall,
        InstructionsInputItemListLocalShellCall,
        InstructionsInputItemListLocalShellCallOutput,
        InstructionsInputItemListMcpListTools,
        InstructionsInputItemListMcpApprovalRequest,
        InstructionsInputItemListMcpApprovalResponse,
        InstructionsInputItemListMcpCall,
        InstructionsInputItemListCustomToolCallOutput,
        InstructionsInputItemListCustomToolCall,
        InstructionsInputItemListItemReference,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputMessageContentOutputTextAnnotationFileCitation(BaseModel):
    file_id: str
    """The ID of the file."""

    filename: str
    """The filename of the file cited."""

    index: int
    """The index of the file in the list of files."""

    type: Literal["file_citation"]
    """The type of the file citation. Always `file_citation`."""


class OutputMessageContentOutputTextAnnotationURLCitation(BaseModel):
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


class OutputMessageContentOutputTextAnnotationContainerFileCitation(BaseModel):
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


class OutputMessageContentOutputTextAnnotationFilePath(BaseModel):
    file_id: str
    """The ID of the file."""

    index: int
    """The index of the file in the list of files."""

    type: Literal["file_path"]
    """The type of the file path. Always `file_path`."""


OutputMessageContentOutputTextAnnotation: TypeAlias = Annotated[
    Union[
        OutputMessageContentOutputTextAnnotationFileCitation,
        OutputMessageContentOutputTextAnnotationURLCitation,
        OutputMessageContentOutputTextAnnotationContainerFileCitation,
        OutputMessageContentOutputTextAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputMessageContentOutputTextLogprobTopLogprob(BaseModel):
    token: str

    bytes: List[int]

    logprob: float


class OutputMessageContentOutputTextLogprob(BaseModel):
    token: str

    bytes: List[int]

    logprob: float

    top_logprobs: List[OutputMessageContentOutputTextLogprobTopLogprob]


class OutputMessageContentOutputText(BaseModel):
    annotations: List[OutputMessageContentOutputTextAnnotation]
    """The annotations of the text output."""

    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""

    logprobs: Optional[List[OutputMessageContentOutputTextLogprob]] = None


class OutputMessageContentRefusal(BaseModel):
    refusal: str
    """The refusal explanation from the model."""

    type: Literal["refusal"]
    """The type of the refusal. Always `refusal`."""


OutputMessageContent: TypeAlias = Annotated[
    Union[OutputMessageContentOutputText, OutputMessageContentRefusal], PropertyInfo(discriminator="type")
]


class OutputMessage(BaseModel):
    id: str
    """The unique ID of the output message."""

    content: List[OutputMessageContent]
    """The content of the output message."""

    role: Literal["assistant"]
    """The role of the output message. Always `assistant`."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """

    type: Literal["message"]
    """The type of the output message. Always `message`."""


class OutputFileSearchCallResult(BaseModel):
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


class OutputFileSearchCall(BaseModel):
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

    results: Optional[List[OutputFileSearchCallResult]] = None
    """The results of the file search tool call."""


class OutputFunctionCall(BaseModel):
    arguments: str
    """A JSON string of the arguments to pass to the function."""

    call_id: str
    """The unique ID of the function tool call generated by the model."""

    name: str
    """The name of the function to run."""

    type: Literal["function_call"]
    """The type of the function tool call. Always `function_call`."""

    id: Optional[str] = None
    """The unique ID of the function tool call."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


class OutputWebSearchCallActionSearchSource(BaseModel):
    type: Literal["url"]
    """The type of source. Always `url`."""

    url: str
    """The URL of the source."""


class OutputWebSearchCallActionSearch(BaseModel):
    query: str
    """The search query."""

    type: Literal["search"]
    """The action type."""

    sources: Optional[List[OutputWebSearchCallActionSearchSource]] = None
    """The sources used in the search."""


class OutputWebSearchCallActionOpenPage(BaseModel):
    type: Literal["open_page"]
    """The action type."""

    url: str
    """The URL opened by the model."""


class OutputWebSearchCallActionFind(BaseModel):
    pattern: str
    """The pattern or text to search for within the page."""

    type: Literal["find"]
    """The action type."""

    url: str
    """The URL of the page searched for the pattern."""


OutputWebSearchCallAction: TypeAlias = Annotated[
    Union[OutputWebSearchCallActionSearch, OutputWebSearchCallActionOpenPage, OutputWebSearchCallActionFind],
    PropertyInfo(discriminator="type"),
]


class OutputWebSearchCall(BaseModel):
    id: str
    """The unique ID of the web search tool call."""

    action: OutputWebSearchCallAction
    """
    An object describing the specific action taken in this web search call. Includes
    details on how the model used the web (search, open_page, find).
    """

    status: Literal["in_progress", "searching", "completed", "failed"]
    """The status of the web search tool call."""

    type: Literal["web_search_call"]
    """The type of the web search tool call. Always `web_search_call`."""


class OutputComputerCallActionClick(BaseModel):
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


class OutputComputerCallActionDoubleClick(BaseModel):
    type: Literal["double_click"]
    """Specifies the event type.

    For a double click action, this property is always set to `double_click`.
    """

    x: int
    """The x-coordinate where the double click occurred."""

    y: int
    """The y-coordinate where the double click occurred."""


class OutputComputerCallActionDragPath(BaseModel):
    x: int
    """The x-coordinate."""

    y: int
    """The y-coordinate."""


class OutputComputerCallActionDrag(BaseModel):
    path: List[OutputComputerCallActionDragPath]
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


class OutputComputerCallActionKeypress(BaseModel):
    keys: List[str]
    """The combination of keys the model is requesting to be pressed.

    This is an array of strings, each representing a key.
    """

    type: Literal["keypress"]
    """Specifies the event type.

    For a keypress action, this property is always set to `keypress`.
    """


class OutputComputerCallActionMove(BaseModel):
    type: Literal["move"]
    """Specifies the event type.

    For a move action, this property is always set to `move`.
    """

    x: int
    """The x-coordinate to move to."""

    y: int
    """The y-coordinate to move to."""


class OutputComputerCallActionScreenshot(BaseModel):
    type: Literal["screenshot"]
    """Specifies the event type.

    For a screenshot action, this property is always set to `screenshot`.
    """


class OutputComputerCallActionScroll(BaseModel):
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


class OutputComputerCallActionType(BaseModel):
    text: str
    """The text to type."""

    type: Literal["type"]
    """Specifies the event type.

    For a type action, this property is always set to `type`.
    """


class OutputComputerCallActionWait(BaseModel):
    type: Literal["wait"]
    """Specifies the event type.

    For a wait action, this property is always set to `wait`.
    """


OutputComputerCallAction: TypeAlias = Annotated[
    Union[
        OutputComputerCallActionClick,
        OutputComputerCallActionDoubleClick,
        OutputComputerCallActionDrag,
        OutputComputerCallActionKeypress,
        OutputComputerCallActionMove,
        OutputComputerCallActionScreenshot,
        OutputComputerCallActionScroll,
        OutputComputerCallActionType,
        OutputComputerCallActionWait,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputComputerCallPendingSafetyCheck(BaseModel):
    id: str
    """The ID of the pending safety check."""

    code: str
    """The type of the pending safety check."""

    message: str
    """Details about the pending safety check."""


class OutputComputerCall(BaseModel):
    id: str
    """The unique ID of the computer call."""

    action: OutputComputerCallAction
    """A click action."""

    call_id: str
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: List[OutputComputerCallPendingSafetyCheck]
    """The pending safety checks for the computer call."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Literal["computer_call"]
    """The type of the computer call. Always `computer_call`."""


class OutputReasoningSummary(BaseModel):
    text: str
    """A summary of the reasoning output from the model so far."""

    type: Literal["summary_text"]
    """The type of the object. Always `summary_text`."""


class OutputReasoningContent(BaseModel):
    text: str
    """The reasoning text from the model."""

    type: Literal["reasoning_text"]
    """The type of the reasoning text. Always `reasoning_text`."""


class OutputReasoning(BaseModel):
    id: str
    """The unique identifier of the reasoning content."""

    summary: List[OutputReasoningSummary]
    """Reasoning summary content."""

    type: Literal["reasoning"]
    """The type of the object. Always `reasoning`."""

    content: Optional[List[OutputReasoningContent]] = None
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


class OutputImageGenerationCall(BaseModel):
    id: str
    """The unique ID of the image generation call."""

    result: Optional[str] = None
    """The generated image encoded in base64."""

    status: Literal["in_progress", "completed", "generating", "failed"]
    """The status of the image generation call."""

    type: Literal["image_generation_call"]
    """The type of the image generation call. Always `image_generation_call`."""


class OutputCodeInterpreterCallOutputLogs(BaseModel):
    logs: str
    """The logs output from the code interpreter."""

    type: Literal["logs"]
    """The type of the output. Always 'logs'."""


class OutputCodeInterpreterCallOutputImage(BaseModel):
    type: Literal["image"]
    """The type of the output. Always 'image'."""

    url: str
    """The URL of the image output from the code interpreter."""


OutputCodeInterpreterCallOutput: TypeAlias = Annotated[
    Union[OutputCodeInterpreterCallOutputLogs, OutputCodeInterpreterCallOutputImage], PropertyInfo(discriminator="type")
]


class OutputCodeInterpreterCall(BaseModel):
    id: str
    """The unique ID of the code interpreter tool call."""

    code: Optional[str] = None
    """The code to run, or null if not available."""

    container_id: str
    """The ID of the container used to run the code."""

    outputs: Optional[List[OutputCodeInterpreterCallOutput]] = None
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


class OutputLocalShellCallAction(BaseModel):
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


class OutputLocalShellCall(BaseModel):
    id: str
    """The unique ID of the local shell call."""

    action: OutputLocalShellCallAction
    """Execute a shell command on the server."""

    call_id: str
    """The unique ID of the local shell tool call generated by the model."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the local shell call."""

    type: Literal["local_shell_call"]
    """The type of the local shell call. Always `local_shell_call`."""


class OutputMcpCall(BaseModel):
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


class OutputMcpListToolsTool(BaseModel):
    input_schema: object
    """The JSON schema describing the tool's input."""

    name: str
    """The name of the tool."""

    annotations: Optional[object] = None
    """Additional annotations about the tool."""

    description: Optional[str] = None
    """The description of the tool."""


class OutputMcpListTools(BaseModel):
    id: str
    """The unique ID of the list."""

    server_label: str
    """The label of the MCP server."""

    tools: List[OutputMcpListToolsTool]
    """The tools available on the server."""

    type: Literal["mcp_list_tools"]
    """The type of the item. Always `mcp_list_tools`."""

    error: Optional[str] = None
    """Error message if the server could not list tools."""


class OutputMcpApprovalRequest(BaseModel):
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


class OutputCustomToolCall(BaseModel):
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


Output: TypeAlias = Annotated[
    Union[
        OutputMessage,
        OutputFileSearchCall,
        OutputFunctionCall,
        OutputWebSearchCall,
        OutputComputerCall,
        OutputReasoning,
        OutputImageGenerationCall,
        OutputCodeInterpreterCall,
        OutputLocalShellCall,
        OutputMcpCall,
        OutputMcpListTools,
        OutputMcpApprovalRequest,
        OutputCustomToolCall,
    ],
    PropertyInfo(discriminator="type"),
]


class ToolChoiceToolChoiceAllowed(BaseModel):
    mode: Literal["auto", "required"]
    """Constrains the tools available to the model to a pre-defined set.

    `auto` allows the model to pick from among the allowed tools and generate a
    message.

    `required` requires the model to call one or more of the allowed tools.
    """

    tools: List[Dict[str, object]]
    """A list of tool definitions that the model should be allowed to call.

    For the Responses API, the list of tool definitions might look like:

    ```json
    [
      { "type": "function", "name": "get_weather" },
      { "type": "mcp", "server_label": "deepwiki" },
      { "type": "image_generation" }
    ]
    ```
    """

    type: Literal["allowed_tools"]
    """Allowed tool configuration type. Always `allowed_tools`."""


class ToolChoiceToolChoiceTypes(BaseModel):
    type: Literal[
        "file_search",
        "web_search_preview",
        "computer_use_preview",
        "web_search_preview_2025_03_11",
        "image_generation",
        "code_interpreter",
    ]
    """The type of hosted tool the model should to use.

    Learn more about [built-in tools](https://platform.excai.com/docs/guides/tools).

    Allowed values are:

    - `file_search`
    - `web_search_preview`
    - `computer_use_preview`
    - `code_interpreter`
    - `image_generation`
    """


class ToolChoiceToolChoiceFunction(BaseModel):
    name: str
    """The name of the function to call."""

    type: Literal["function"]
    """For function calling, the type is always `function`."""


class ToolChoiceToolChoiceMcp(BaseModel):
    server_label: str
    """The label of the MCP server to use."""

    type: Literal["mcp"]
    """For MCP tools, the type is always `mcp`."""

    name: Optional[str] = None
    """The name of the tool to call on the server."""


class ToolChoiceToolChoiceCustom(BaseModel):
    name: str
    """The name of the custom tool to call."""

    type: Literal["custom"]
    """For custom tool calling, the type is always `custom`."""


ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"],
    ToolChoiceToolChoiceAllowed,
    ToolChoiceToolChoiceTypes,
    ToolChoiceToolChoiceFunction,
    ToolChoiceToolChoiceMcp,
    ToolChoiceToolChoiceCustom,
]


class ToolFunction(BaseModel):
    name: str
    """The name of the function to call."""

    parameters: Optional[Dict[str, object]] = None
    """A JSON schema object describing the parameters of the function."""

    strict: Optional[bool] = None
    """Whether to enforce strict parameter validation. Default `true`."""

    type: Literal["function"]
    """The type of the function tool. Always `function`."""

    description: Optional[str] = None
    """A description of the function.

    Used by the model to determine whether or not to call the function.
    """


class ToolFileSearchFiltersComparisonFilter(BaseModel):
    key: str
    """The key to compare against the value."""

    type: Literal["eq", "ne", "gt", "gte", "lt", "lte"]
    """
    Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`,
    `nin`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    - `in`: in
    - `nin`: not in
    """

    value: Union[str, float, bool, List[Union[str, float]]]
    """
    The value to compare against the attribute key; supports string, number, or
    boolean types.
    """


class ToolFileSearchFiltersCompoundFilterFilterComparisonFilter(BaseModel):
    key: str
    """The key to compare against the value."""

    type: Literal["eq", "ne", "gt", "gte", "lt", "lte"]
    """
    Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`,
    `nin`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    - `in`: in
    - `nin`: not in
    """

    value: Union[str, float, bool, List[Union[str, float]]]
    """
    The value to compare against the attribute key; supports string, number, or
    boolean types.
    """


ToolFileSearchFiltersCompoundFilterFilter: TypeAlias = Union[
    ToolFileSearchFiltersCompoundFilterFilterComparisonFilter, object
]


class ToolFileSearchFiltersCompoundFilter(BaseModel):
    filters: List[ToolFileSearchFiltersCompoundFilterFilter]
    """Array of filters to combine.

    Items can be `ComparisonFilter` or `CompoundFilter`.
    """

    type: Literal["and", "or"]
    """Type of operation: `and` or `or`."""


ToolFileSearchFilters: TypeAlias = Union[
    ToolFileSearchFiltersComparisonFilter, ToolFileSearchFiltersCompoundFilter, None
]


class ToolFileSearchRankingOptions(BaseModel):
    ranker: Optional[Literal["auto", "default-2024-11-15"]] = None
    """The ranker to use for the file search."""

    score_threshold: Optional[float] = None
    """The score threshold for the file search, a number between 0 and 1.

    Numbers closer to 1 will attempt to return only the most relevant results, but
    may return fewer results.
    """


class ToolFileSearch(BaseModel):
    type: Literal["file_search"]
    """The type of the file search tool. Always `file_search`."""

    vector_store_ids: List[str]
    """The IDs of the vector stores to search."""

    filters: Optional[ToolFileSearchFilters] = None
    """A filter to apply."""

    max_num_results: Optional[int] = None
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: Optional[ToolFileSearchRankingOptions] = None
    """Ranking options for search."""


class ToolComputerUsePreview(BaseModel):
    display_height: int
    """The height of the computer display."""

    display_width: int
    """The width of the computer display."""

    environment: Literal["windows", "mac", "linux", "ubuntu", "browser"]
    """The type of computer environment to control."""

    type: Literal["computer_use_preview"]
    """The type of the computer use tool. Always `computer_use_preview`."""


class ToolWebSearchToolFilters(BaseModel):
    allowed_domains: Optional[List[str]] = None
    """Allowed domains for the search.

    If not provided, all domains are allowed. Subdomains of the provided domains are
    allowed as well.

    Example: `["pubmed.ncbi.nlm.nih.gov"]`
    """


class ToolWebSearchToolUserLocation(BaseModel):
    city: Optional[str] = None
    """Free text input for the city of the user, e.g. `San Francisco`."""

    country: Optional[str] = None
    """
    The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of
    the user, e.g. `US`.
    """

    region: Optional[str] = None
    """Free text input for the region of the user, e.g. `California`."""

    timezone: Optional[str] = None
    """
    The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the
    user, e.g. `America/Los_Angeles`.
    """

    type: Optional[Literal["approximate"]] = None
    """The type of location approximation. Always `approximate`."""


class ToolWebSearchTool(BaseModel):
    type: Literal["web_search", "web_search_2025_08_26"]
    """The type of the web search tool.

    One of `web_search` or `web_search_2025_08_26`.
    """

    filters: Optional[ToolWebSearchToolFilters] = None
    """Filters for the search."""

    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[ToolWebSearchToolUserLocation] = None
    """The approximate location of the user."""


class ToolMcpAllowedToolsMcpToolFilter(BaseModel):
    read_only: Optional[bool] = None
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


ToolMcpAllowedTools: TypeAlias = Union[List[str], ToolMcpAllowedToolsMcpToolFilter, None]


class ToolMcpRequireApprovalMcpToolApprovalFilterAlways(BaseModel):
    read_only: Optional[bool] = None
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


class ToolMcpRequireApprovalMcpToolApprovalFilterNever(BaseModel):
    read_only: Optional[bool] = None
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


class ToolMcpRequireApprovalMcpToolApprovalFilter(BaseModel):
    always: Optional[ToolMcpRequireApprovalMcpToolApprovalFilterAlways] = None
    """A filter object to specify which tools are allowed."""

    never: Optional[ToolMcpRequireApprovalMcpToolApprovalFilterNever] = None
    """A filter object to specify which tools are allowed."""


ToolMcpRequireApproval: TypeAlias = Union[ToolMcpRequireApprovalMcpToolApprovalFilter, Literal["always", "never"], None]


class ToolMcp(BaseModel):
    server_label: str
    """A label for this MCP server, used to identify it in tool calls."""

    type: Literal["mcp"]
    """The type of the MCP tool. Always `mcp`."""

    allowed_tools: Optional[ToolMcpAllowedTools] = None
    """List of allowed tool names or a filter object."""

    authorization: Optional[str] = None
    """
    An OAuth access token that can be used with a remote MCP server, either with a
    custom MCP server URL or a service connector. Your application must handle the
    OAuth authorization flow and provide the token here.
    """

    connector_id: Optional[
        Literal[
            "connector_dropbox",
            "connector_gmail",
            "connector_googlecalendar",
            "connector_googledrive",
            "connector_microsoftteams",
            "connector_outlookcalendar",
            "connector_outlookemail",
            "connector_sharepoint",
        ]
    ] = None
    """Identifier for service connectors, like those available in ChatGPT.

    One of `server_url` or `connector_id` must be provided. Learn more about service
    connectors
    [here](https://platform.excai.com/docs/guides/tools-remote-mcp#connectors).

    Currently supported `connector_id` values are:

    - Dropbox: `connector_dropbox`
    - Gmail: `connector_gmail`
    - Google Calendar: `connector_googlecalendar`
    - Google Drive: `connector_googledrive`
    - Microsoft Teams: `connector_microsoftteams`
    - Outlook Calendar: `connector_outlookcalendar`
    - Outlook Email: `connector_outlookemail`
    - SharePoint: `connector_sharepoint`
    """

    headers: Optional[Dict[str, str]] = None
    """Optional HTTP headers to send to the MCP server.

    Use for authentication or other purposes.
    """

    require_approval: Optional[ToolMcpRequireApproval] = None
    """Specify which of the MCP server's tools require approval."""

    server_description: Optional[str] = None
    """Optional description of the MCP server, used to provide more context."""

    server_url: Optional[str] = None
    """The URL for the MCP server.

    One of `server_url` or `connector_id` must be provided.
    """


class ToolCodeInterpreterContainerCodeInterpreterToolAuto(BaseModel):
    type: Literal["auto"]
    """Always `auto`."""

    file_ids: Optional[List[str]] = None
    """An optional list of uploaded files to make available to your code."""


ToolCodeInterpreterContainer: TypeAlias = Union[str, ToolCodeInterpreterContainerCodeInterpreterToolAuto]


class ToolCodeInterpreter(BaseModel):
    container: ToolCodeInterpreterContainer
    """The code interpreter container.

    Can be a container ID or an object that specifies uploaded file IDs to make
    available to your code.
    """

    type: Literal["code_interpreter"]
    """The type of the code interpreter tool. Always `code_interpreter`."""


class ToolImageGenerationInputImageMask(BaseModel):
    file_id: Optional[str] = None
    """File ID for the mask image."""

    image_url: Optional[str] = None
    """Base64-encoded mask image."""


class ToolImageGeneration(BaseModel):
    type: Literal["image_generation"]
    """The type of the image generation tool. Always `image_generation`."""

    background: Optional[Literal["transparent", "opaque", "auto"]] = None
    """Background type for the generated image.

    One of `transparent`, `opaque`, or `auto`. Default: `auto`.
    """

    input_fidelity: Optional[Literal["high", "low"]] = None
    """
    Control how much effort the model will exert to match the style and features,
    especially facial features, of input images. This parameter is only supported
    for `gpt-image-1`. Unsupported for `gpt-image-1-mini`. Supports `high` and
    `low`. Defaults to `low`.
    """

    input_image_mask: Optional[ToolImageGenerationInputImageMask] = None
    """Optional mask for inpainting.

    Contains `image_url` (string, optional) and `file_id` (string, optional).
    """

    model: Optional[Literal["gpt-image-1", "gpt-image-1-mini"]] = None
    """The image generation model to use. Default: `gpt-image-1`."""

    moderation: Optional[Literal["auto", "low"]] = None
    """Moderation level for the generated image. Default: `auto`."""

    output_compression: Optional[int] = None
    """Compression level for the output image. Default: 100."""

    output_format: Optional[Literal["png", "webp", "jpeg"]] = None
    """The output format of the generated image.

    One of `png`, `webp`, or `jpeg`. Default: `png`.
    """

    partial_images: Optional[int] = None
    """
    Number of partial images to generate in streaming mode, from 0 (default value)
    to 3.
    """

    quality: Optional[Literal["low", "medium", "high", "auto"]] = None
    """The quality of the generated image.

    One of `low`, `medium`, `high`, or `auto`. Default: `auto`.
    """

    size: Optional[Literal["1024x1024", "1024x1536", "1536x1024", "auto"]] = None
    """The size of the generated image.

    One of `1024x1024`, `1024x1536`, `1536x1024`, or `auto`. Default: `auto`.
    """


class ToolLocalShell(BaseModel):
    type: Literal["local_shell"]
    """The type of the local shell tool. Always `local_shell`."""


class ToolCustomFormatText(BaseModel):
    type: Literal["text"]
    """Unconstrained text format. Always `text`."""


class ToolCustomFormatGrammar(BaseModel):
    definition: str
    """The grammar definition."""

    syntax: Literal["lark", "regex"]
    """The syntax of the grammar definition. One of `lark` or `regex`."""

    type: Literal["grammar"]
    """Grammar format. Always `grammar`."""


ToolCustomFormat: TypeAlias = Annotated[
    Union[ToolCustomFormatText, ToolCustomFormatGrammar], PropertyInfo(discriminator="type")
]


class ToolCustom(BaseModel):
    name: str
    """The name of the custom tool, used to identify it in tool calls."""

    type: Literal["custom"]
    """The type of the custom tool. Always `custom`."""

    description: Optional[str] = None
    """Optional description of the custom tool, used to provide more context."""

    format: Optional[ToolCustomFormat] = None
    """The input format for the custom tool. Default is unconstrained text."""


class ToolWebSearchPreviewToolUserLocation(BaseModel):
    type: Literal["approximate"]
    """The type of location approximation. Always `approximate`."""

    city: Optional[str] = None
    """Free text input for the city of the user, e.g. `San Francisco`."""

    country: Optional[str] = None
    """
    The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of
    the user, e.g. `US`.
    """

    region: Optional[str] = None
    """Free text input for the region of the user, e.g. `California`."""

    timezone: Optional[str] = None
    """
    The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the
    user, e.g. `America/Los_Angeles`.
    """


class ToolWebSearchPreviewTool(BaseModel):
    type: Literal["web_search_preview", "web_search_preview_2025_03_11"]
    """The type of the web search tool.

    One of `web_search_preview` or `web_search_preview_2025_03_11`.
    """

    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[ToolWebSearchPreviewToolUserLocation] = None
    """The user's location."""


Tool: TypeAlias = Annotated[
    Union[
        ToolFunction,
        ToolFileSearch,
        ToolComputerUsePreview,
        ToolWebSearchTool,
        ToolMcp,
        ToolCodeInterpreter,
        ToolImageGeneration,
        ToolLocalShell,
        ToolCustom,
        ToolWebSearchPreviewTool,
    ],
    PropertyInfo(discriminator="type"),
]


class Conversation(BaseModel):
    id: str
    """The unique ID of the conversation."""


class PromptVariablesInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class PromptVariablesInputImageContent(BaseModel):
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


class PromptVariablesInputFileContent(BaseModel):
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


PromptVariables: TypeAlias = Union[
    str, PromptVariablesInputTextContent, PromptVariablesInputImageContent, PromptVariablesInputFileContent
]


class Prompt(BaseModel):
    id: str
    """The unique identifier of the prompt template to use."""

    variables: Optional[Dict[str, PromptVariables]] = None
    """Optional map of values to substitute in for variables in your prompt.

    The substitution values can either be strings, or other Response input types
    like images or files.
    """

    version: Optional[str] = None
    """Optional version of the prompt template."""


class Reasoning(BaseModel):
    effort: Optional[Literal["minimal", "low", "medium", "high"]] = None
    """
    Constrains effort on reasoning for
    [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
    supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
    effort can result in faster responses and fewer tokens used on reasoning in a
    response.

    Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
    effort.
    """

    generate_summary: Optional[Literal["auto", "concise", "detailed"]] = None
    """**Deprecated:** use `summary` instead.

    A summary of the reasoning performed by the model. This can be useful for
    debugging and understanding the model's reasoning process. One of `auto`,
    `concise`, or `detailed`.
    """

    summary: Optional[Literal["auto", "concise", "detailed"]] = None
    """A summary of the reasoning performed by the model.

    This can be useful for debugging and understanding the model's reasoning
    process. One of `auto`, `concise`, or `detailed`.
    """


class TextFormatText(BaseModel):
    type: Literal["text"]
    """The type of response format being defined. Always `text`."""


class TextFormatJsonSchema(BaseModel):
    name: str
    """The name of the response format.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """
    The schema for the response format, described as a JSON Schema object. Learn how
    to build JSON schemas [here](https://json-schema.org/).
    """

    type: Literal["json_schema"]
    """The type of response format being defined. Always `json_schema`."""

    description: Optional[str] = None
    """
    A description of what the response format is for, used by the model to determine
    how to respond in the format.
    """

    strict: Optional[bool] = None
    """
    Whether to enable strict schema adherence when generating the output. If set to
    true, the model will always follow the exact schema defined in the `schema`
    field. Only a subset of JSON Schema is supported when `strict` is `true`. To
    learn more, read the
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
    """


class TextFormatJsonObject(BaseModel):
    type: Literal["json_object"]
    """The type of response format being defined. Always `json_object`."""


TextFormat: TypeAlias = Annotated[
    Union[TextFormatText, TextFormatJsonSchema, TextFormatJsonObject], PropertyInfo(discriminator="type")
]


class Text(BaseModel):
    format: Optional[TextFormat] = None
    """An object specifying the format that the model must output.

    Configuring `{ "type": "json_schema" }` enables Structured Outputs, which
    ensures the model will match your supplied JSON schema. Learn more in the
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).

    The default format is `{ "type": "text" }` with no additional options.

    **Not recommended for gpt-4o and newer models:**

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """

    verbosity: Optional[Literal["low", "medium", "high"]] = None
    """Constrains the verbosity of the model's response.

    Lower values will result in more concise responses, while higher values will
    result in more verbose responses. Currently supported values are `low`,
    `medium`, and `high`.
    """


class UsageInputTokensDetails(BaseModel):
    cached_tokens: int
    """The number of tokens that were retrieved from the cache.

    [More on prompt caching](https://platform.excai.com/docs/guides/prompt-caching).
    """


class UsageOutputTokensDetails(BaseModel):
    reasoning_tokens: int
    """The number of reasoning tokens."""


class Usage(BaseModel):
    input_tokens: int
    """The number of input tokens."""

    input_tokens_details: UsageInputTokensDetails
    """A detailed breakdown of the input tokens."""

    output_tokens: int
    """The number of output tokens."""

    output_tokens_details: UsageOutputTokensDetails
    """A detailed breakdown of the output tokens."""

    total_tokens: int
    """The total number of tokens used."""


class ResponseCreateResponse(BaseModel):
    id: str
    """Unique identifier for this Response."""

    created_at: float
    """Unix timestamp (in seconds) of when this Response was created."""

    error: Optional[Error] = None
    """An error object returned when the model fails to generate a Response."""

    incomplete_details: Optional[IncompleteDetails] = None
    """Details about why the response is incomplete."""

    instructions: Union[str, List[InstructionsInputItemList], None] = None
    """A system (or developer) message inserted into the model's context.

    When using along with `previous_response_id`, the instructions from a previous
    response will not be carried over to the next response. This makes it simple to
    swap out system (or developer) messages in new responses.
    """

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    model: Union[
        Literal[
            "gpt-5",
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5-2025-08-07",
            "gpt-5-mini-2025-08-07",
            "gpt-5-nano-2025-08-07",
            "gpt-5-chat-latest",
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "gpt-4.1-2025-04-14",
            "gpt-4.1-mini-2025-04-14",
            "gpt-4.1-nano-2025-04-14",
            "o4-mini",
            "o4-mini-2025-04-16",
            "o3",
            "o3-2025-04-16",
            "o3-mini",
            "o3-mini-2025-01-31",
            "o1",
            "o1-2024-12-17",
            "o1-preview",
            "o1-preview-2024-09-12",
            "o1-mini",
            "o1-mini-2024-09-12",
            "gpt-4o",
            "gpt-4o-2024-11-20",
            "gpt-4o-2024-08-06",
            "gpt-4o-2024-05-13",
            "gpt-4o-audio-preview",
            "gpt-4o-audio-preview-2024-10-01",
            "gpt-4o-audio-preview-2024-12-17",
            "gpt-4o-audio-preview-2025-06-03",
            "gpt-4o-mini-audio-preview",
            "gpt-4o-mini-audio-preview-2024-12-17",
            "gpt-4o-search-preview",
            "gpt-4o-mini-search-preview",
            "gpt-4o-search-preview-2025-03-11",
            "gpt-4o-mini-search-preview-2025-03-11",
            "chatgpt-4o-latest",
            "codex-mini-latest",
            "gpt-4o-mini",
            "gpt-4o-mini-2024-07-18",
            "gpt-4-turbo",
            "gpt-4-turbo-2024-04-09",
            "gpt-4-0125-preview",
            "gpt-4-turbo-preview",
            "gpt-4-1106-preview",
            "gpt-4-vision-preview",
            "gpt-4",
            "gpt-4-0314",
            "gpt-4-0613",
            "gpt-4-32k",
            "gpt-4-32k-0314",
            "gpt-4-32k-0613",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-0301",
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-1106",
            "gpt-3.5-turbo-0125",
            "gpt-3.5-turbo-16k-0613",
            "o1-pro",
            "o1-pro-2025-03-19",
            "o3-pro",
            "o3-pro-2025-06-10",
            "o3-deep-research",
            "o3-deep-research-2025-06-26",
            "o4-mini-deep-research",
            "o4-mini-deep-research-2025-06-26",
            "computer-use-preview",
            "computer-use-preview-2025-03-11",
            "gpt-5-codex",
            "gpt-5-pro",
            "gpt-5-pro-2025-10-06",
        ],
        str,
    ]
    """Model ID used to generate the response, like `gpt-4o` or `o3`.

    EXCai offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the
    [model guide](https://platform.excai.com/docs/models) to browse and compare
    available models.
    """

    object: Literal["response"]
    """The object type of this resource - always set to `response`."""

    output: List[Output]
    """An array of content items generated by the model.

    - The length and order of items in the `output` array is dependent on the
      model's response.
    - Rather than accessing the first item in the `output` array and assuming it's
      an `assistant` message with the content generated by the model, you might
      consider using the `output_text` property where supported in SDKs.
    """

    parallel_tool_calls: bool
    """Whether to allow the model to run tool calls in parallel."""

    temperature: Optional[float] = None
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or `top_p` but not both.
    """

    tool_choice: ToolChoice
    """
    How the model should select which tool (or tools) to use when generating a
    response. See the `tools` parameter to see how to specify which tools the model
    can call.
    """

    tools: List[Tool]
    """An array of tools the model may call while generating a response.

    You can specify which tool to use by setting the `tool_choice` parameter.

    We support the following categories of tools:

    - **Built-in tools**: Tools that are provided by EXCai that extend the model's
      capabilities, like
      [web search](https://platform.excai.com/docs/guides/tools-web-search) or
      [file search](https://platform.excai.com/docs/guides/tools-file-search). Learn
      more about [built-in tools](https://platform.excai.com/docs/guides/tools).
    - **MCP Tools**: Integrations with third-party systems via custom MCP servers or
      predefined connectors such as Google Drive and SharePoint. Learn more about
      [MCP Tools](https://platform.excai.com/docs/guides/tools-connectors-mcp).
    - **Function calls (custom tools)**: Functions that are defined by you, enabling
      the model to call your own code with strongly typed arguments and outputs.
      Learn more about
      [function calling](https://platform.excai.com/docs/guides/function-calling).
      You can also use custom tools to call your own code.
    """

    top_p: Optional[float] = None
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """

    background: Optional[bool] = None
    """
    Whether to run the model response in the background.
    [Learn more](https://platform.excai.com/docs/guides/background).
    """

    conversation: Optional[Conversation] = None
    """The conversation that this response belongs to.

    Input items and output items from this response are automatically added to this
    conversation.
    """

    max_output_tokens: Optional[int] = None
    """
    An upper bound for the number of tokens that can be generated for a response,
    including visible output tokens and
    [reasoning tokens](https://platform.excai.com/docs/guides/reasoning).
    """

    max_tool_calls: Optional[int] = None
    """
    The maximum number of total calls to built-in tools that can be processed in a
    response. This maximum number applies across all built-in tool calls, not per
    individual tool. Any further attempts to call a tool by the model will be
    ignored.
    """

    previous_response_id: Optional[str] = None
    """The unique ID of the previous response to the model.

    Use this to create multi-turn conversations. Learn more about
    [conversation state](https://platform.excai.com/docs/guides/conversation-state).
    Cannot be used in conjunction with `conversation`.
    """

    prompt: Optional[Prompt] = None
    """
    Reference to a prompt template and its variables.
    [Learn more](https://platform.excai.com/docs/guides/text?api-mode=responses#reusable-prompts).
    """

    prompt_cache_key: Optional[str] = None
    """
    Used by EXCai to cache responses for similar requests to optimize your cache hit
    rates. Replaces the `user` field.
    [Learn more](https://platform.excai.com/docs/guides/prompt-caching).
    """

    reasoning: Optional[Reasoning] = None
    """**gpt-5 and o-series models only**

    Configuration options for
    [reasoning models](https://platform.excai.com/docs/guides/reasoning).
    """

    safety_identifier: Optional[str] = None
    """
    A stable identifier used to help detect users of your application that may be
    violating EXCai's usage policies. The IDs should be a string that uniquely
    identifies each user. We recommend hashing their username or email address, in
    order to avoid sending us any identifying information.
    [Learn more](https://platform.excai.com/docs/guides/safety-best-practices#safety-identifiers).
    """

    service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] = None
    """Specifies the processing type used for serving the request.

    - If set to 'auto', then the request will be processed with the service tier
      configured in the Project settings. Unless otherwise configured, the Project
      will use 'default'.
    - If set to 'default', then the request will be processed with the standard
      pricing and performance for the selected model.
    - If set to '[flex](https://platform.excai.com/docs/guides/flex-processing)' or
      '[priority](https://excai.com/api-priority-processing/)', then the request
      will be processed with the corresponding service tier.
    - When not set, the default behavior is 'auto'.

    When the `service_tier` parameter is set, the response body will include the
    `service_tier` value based on the processing mode actually used to serve the
    request. This response value may be different from the value set in the
    parameter.
    """

    status: Optional[Literal["completed", "failed", "in_progress", "cancelled", "queued", "incomplete"]] = None
    """The status of the response generation.

    One of `completed`, `failed`, `in_progress`, `cancelled`, `queued`, or
    `incomplete`.
    """

    text: Optional[Text] = None
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](https://platform.excai.com/docs/guides/text)
    - [Structured Outputs](https://platform.excai.com/docs/guides/structured-outputs)
    """

    top_logprobs: Optional[int] = None
    """
    An integer between 0 and 20 specifying the number of most likely tokens to
    return at each token position, each with an associated log probability.
    """

    truncation: Optional[Literal["auto", "disabled"]] = None
    """The truncation strategy to use for the model response.

    - `auto`: If the input to this Response exceeds the model's context window size,
      the model will truncate the response to fit the context window by dropping
      items from the beginning of the conversation.
    - `disabled` (default): If the input size will exceed the context window size
      for a model, the request will fail with a 400 error.
    """

    usage: Optional[Usage] = None
    """
    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used.
    """

    user: Optional[str] = None
    """This field is being replaced by `safety_identifier` and `prompt_cache_key`.

    Use `prompt_cache_key` instead to maintain caching optimizations. A stable
    identifier for your end-users. Used to boost cache hit rates by better bucketing
    similar requests and to help EXCai detect and prevent abuse.
    [Learn more](https://platform.excai.com/docs/guides/safety-best-practices#safety-identifiers).
    """
