# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ResponseListInputItemsResponse",
    "Data",
    "DataMessage",
    "DataMessageContent",
    "DataMessageContentInputTextContent",
    "DataMessageContentInputImageContent",
    "DataMessageContentInputFileContent",
    "DataFileSearchCall",
    "DataFileSearchCallResult",
    "DataComputerCall",
    "DataComputerCallAction",
    "DataComputerCallActionClick",
    "DataComputerCallActionDoubleClick",
    "DataComputerCallActionDrag",
    "DataComputerCallActionDragPath",
    "DataComputerCallActionKeyPress",
    "DataComputerCallActionMove",
    "DataComputerCallActionScreenshot",
    "DataComputerCallActionScroll",
    "DataComputerCallActionType",
    "DataComputerCallActionWait",
    "DataComputerCallPendingSafetyCheck",
    "DataComputerCallOutput",
    "DataComputerCallOutputOutput",
    "DataComputerCallOutputAcknowledgedSafetyCheck",
    "DataWebSearchCall",
    "DataFunctionCall",
    "DataFunctionCallOutput",
]


class DataMessageContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataMessageContentInputImageContent(BaseModel):
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


class DataMessageContentInputFileContent(BaseModel):
    type: Literal["input_file"]
    """The type of the input item. Always `input_file`."""

    file_data: Optional[str] = None
    """The content of the file to be sent to the model."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    filename: Optional[str] = None
    """The name of the file to be sent to the model."""


DataMessageContent: TypeAlias = Union[
    DataMessageContentInputTextContent, DataMessageContentInputImageContent, DataMessageContentInputFileContent
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


class DataComputerCallActionKeyPress(BaseModel):
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


DataComputerCallAction: TypeAlias = Union[
    DataComputerCallActionClick,
    DataComputerCallActionDoubleClick,
    DataComputerCallActionDrag,
    DataComputerCallActionKeyPress,
    DataComputerCallActionMove,
    DataComputerCallActionScreenshot,
    DataComputerCallActionScroll,
    DataComputerCallActionType,
    DataComputerCallActionWait,
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


class DataWebSearchCall(BaseModel):
    id: str
    """The unique ID of the web search tool call."""

    status: Literal["in_progress", "searching", "completed", "failed"]
    """The status of the web search tool call."""

    type: Literal["web_search_call"]
    """The type of the web search tool call. Always `web_search_call`."""


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


class DataFunctionCallOutput(BaseModel):
    id: str
    """The unique ID of the function call tool output."""

    call_id: str
    """The unique ID of the function tool call generated by the model."""

    output: str
    """A JSON string of the output of the function tool call."""

    type: Literal["function_call_output"]
    """The type of the function tool call output. Always `function_call_output`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


Data: TypeAlias = Annotated[
    Union[
        DataMessage,
        DataMessage,
        DataFileSearchCall,
        DataComputerCall,
        DataComputerCallOutput,
        DataWebSearchCall,
        DataFunctionCall,
        DataFunctionCallOutput,
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
