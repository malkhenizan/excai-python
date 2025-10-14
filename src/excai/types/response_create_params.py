# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ResponseCreateParams",
    "InputInputItemList",
    "InputInputItemListMessage",
    "InputInputItemListMessageContentInputMessageContentList",
    "InputInputItemListMessageContentInputMessageContentListInputTextContent",
    "InputInputItemListMessageContentInputMessageContentListInputImageContent",
    "InputInputItemListMessageContentInputMessageContentListInputFileContent",
    "InputInputItemListFileSearchCall",
    "InputInputItemListFileSearchCallResult",
    "InputInputItemListComputerCall",
    "InputInputItemListComputerCallAction",
    "InputInputItemListComputerCallActionClick",
    "InputInputItemListComputerCallActionDoubleClick",
    "InputInputItemListComputerCallActionDrag",
    "InputInputItemListComputerCallActionDragPath",
    "InputInputItemListComputerCallActionKeyPress",
    "InputInputItemListComputerCallActionMove",
    "InputInputItemListComputerCallActionScreenshot",
    "InputInputItemListComputerCallActionScroll",
    "InputInputItemListComputerCallActionType",
    "InputInputItemListComputerCallActionWait",
    "InputInputItemListComputerCallPendingSafetyCheck",
    "InputInputItemListComputerCallOutput",
    "InputInputItemListComputerCallOutputOutput",
    "InputInputItemListComputerCallOutputAcknowledgedSafetyCheck",
    "InputInputItemListWebSearchCall",
    "InputInputItemListFunctionCall",
    "InputInputItemListFunctionCallOutput",
    "InputInputItemListReasoning",
    "InputInputItemListReasoningSummary",
    "InputInputItemListItemReference",
    "Reasoning",
    "Text",
    "TextFormat",
    "TextFormatResponseFormatText",
    "TextFormatTextResponseFormatJsonSchema",
    "TextFormatResponseFormatJsonObject",
    "ToolChoice",
    "ToolChoiceToolChoiceTypes",
    "ToolChoiceToolChoiceFunction",
    "Tool",
    "ToolFileSearch",
    "ToolFileSearchFilters",
    "ToolFileSearchFiltersComparisonFilter",
    "ToolFileSearchFiltersCompoundFilter",
    "ToolFileSearchFiltersCompoundFilterFilter",
    "ToolFileSearchFiltersCompoundFilterFilterComparisonFilter",
    "ToolFileSearchRankingOptions",
    "ToolFunction",
    "ToolWebSearchPreviewTool",
    "ToolWebSearchPreviewToolUserLocation",
    "ToolComputerUsePreview",
]


class ResponseCreateParams(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputInputItemList]]]
    """Text, image, or file inputs to the model, used to generate a response.

    Learn more:

    - [Text inputs and outputs](/docs/guides/text)
    - [Image inputs](/docs/guides/images)
    - [File inputs](/docs/guides/pdf-files)
    - [Conversation state](/docs/guides/conversation-state)
    - [Function calling](/docs/guides/function-calling)
    """

    model: Required[
        Union[
            Literal[
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
                "gpt-4o-mini-audio-preview",
                "gpt-4o-mini-audio-preview-2024-12-17",
                "gpt-4o-search-preview",
                "gpt-4o-mini-search-preview",
                "gpt-4o-search-preview-2025-03-11",
                "gpt-4o-mini-search-preview-2025-03-11",
                "chatgpt-4o-latest",
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
                "computer-use-preview",
                "computer-use-preview-2025-03-11",
            ],
            str,
        ]
    ]
    """Model ID used to generate the response, like `gpt-4o` or `o3`.

    OpenAI offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model guide](/docs/models) to
    browse and compare available models.
    """

    include: Optional[
        List[
            Literal[
                "file_search_call.results", "message.input_image.image_url", "computer_call_output.output.image_url"
            ]
        ]
    ]
    """Specify additional output data to include in the model response.

    Currently supported values are:

    - `file_search_call.results`: Include the search results of the file search tool
      call.
    - `message.input_image.image_url`: Include image urls from the input message.
    - `computer_call_output.output.image_url`: Include image urls from the computer
      call output.
    """

    instructions: Optional[str]
    """
    Inserts a system (or developer) message as the first item in the model's
    context.

    When using along with `previous_response_id`, the instructions from a previous
    response will not be carried over to the next response. This makes it simple to
    swap out system (or developer) messages in new responses.
    """

    max_output_tokens: Optional[int]
    """
    An upper bound for the number of tokens that can be generated for a response,
    including visible output tokens and [reasoning tokens](/docs/guides/reasoning).
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    parallel_tool_calls: Optional[bool]
    """Whether to allow the model to run tool calls in parallel."""

    previous_response_id: Optional[str]
    """The unique ID of the previous response to the model.

    Use this to create multi-turn conversations. Learn more about
    [conversation state](/docs/guides/conversation-state).
    """

    reasoning: Optional[Reasoning]
    """**o-series models only**

    Configuration options for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    """

    service_tier: Optional[Literal["auto", "default", "flex"]]
    """Specifies the latency tier to use for processing the request.

    This parameter is relevant for customers subscribed to the scale tier service:

    - If set to 'auto', and the Project is Scale tier enabled, the system will
      utilize scale tier credits until they are exhausted.
    - If set to 'auto', and the Project is not Scale tier enabled, the request will
      be processed using the default service tier with a lower uptime SLA and no
      latency guarentee.
    - If set to 'default', the request will be processed using the default service
      tier with a lower uptime SLA and no latency guarentee.
    - If set to 'flex', the request will be processed with the Flex Processing
      service tier. [Learn more](/docs/guides/flex-processing).
    - When not set, the default behavior is 'auto'.

    When this parameter is set, the response body will include the `service_tier`
    utilized.
    """

    store: Optional[bool]
    """Whether to store the generated model response for later retrieval via API."""

    stream: Optional[bool]
    """
    If set to true, the model response data will be streamed to the client as it is
    generated using
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
    See the [Streaming section below](/docs/api-reference/responses-streaming) for
    more information.
    """

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or `top_p` but not both.
    """

    text: Text
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](/docs/guides/text)
    - [Structured Outputs](/docs/guides/structured-outputs)
    """

    tool_choice: ToolChoice
    """
    How the model should select which tool (or tools) to use when generating a
    response. See the `tools` parameter to see how to specify which tools the model
    can call.
    """

    tools: Iterable[Tool]
    """An array of tools the model may call while generating a response.

    You can specify which tool to use by setting the `tool_choice` parameter.

    The two categories of tools you can provide the model are:

    - **Built-in tools**: Tools that are provided by OpenAI that extend the model's
      capabilities, like [web search](/docs/guides/tools-web-search) or
      [file search](/docs/guides/tools-file-search). Learn more about
      [built-in tools](/docs/guides/tools).
    - **Function calls (custom tools)**: Functions that are defined by you, enabling
      the model to call your own code. Learn more about
      [function calling](/docs/guides/function-calling).
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """

    truncation: Optional[Literal["auto", "disabled"]]
    """The truncation strategy to use for the model response.

    - `auto`: If the context of this response and previous ones exceeds the model's
      context window size, the model will truncate the response to fit the context
      window by dropping input items in the middle of the conversation.
    - `disabled` (default): If a model response will exceed the context window size
      for a model, the request will fail with a 400 error.
    """

    user: str
    """
    A unique identifier representing your end-user, which can help OpenAI to monitor
    and detect abuse. [Learn more](/docs/guides/safety-best-practices#end-user-ids).
    """


class InputInputItemListMessageContentInputMessageContentListInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class InputInputItemListMessageContentInputMessageContentListInputImageContent(TypedDict, total=False):
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


class InputInputItemListMessageContentInputMessageContentListInputFileContent(TypedDict, total=False):
    type: Required[Literal["input_file"]]
    """The type of the input item. Always `input_file`."""

    file_data: str
    """The content of the file to be sent to the model."""

    file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    filename: str
    """The name of the file to be sent to the model."""


InputInputItemListMessageContentInputMessageContentList: TypeAlias = Union[
    InputInputItemListMessageContentInputMessageContentListInputTextContent,
    InputInputItemListMessageContentInputMessageContentListInputImageContent,
    InputInputItemListMessageContentInputMessageContentListInputFileContent,
]


class InputInputItemListMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[InputInputItemListMessageContentInputMessageContentList]]]
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


class InputInputItemListFileSearchCallResult(TypedDict, total=False):
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


class InputInputItemListFileSearchCall(TypedDict, total=False):
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

    results: Optional[Iterable[InputInputItemListFileSearchCallResult]]
    """The results of the file search tool call."""


class InputInputItemListComputerCallActionClick(TypedDict, total=False):
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


class InputInputItemListComputerCallActionDoubleClick(TypedDict, total=False):
    type: Required[Literal["double_click"]]
    """Specifies the event type.

    For a double click action, this property is always set to `double_click`.
    """

    x: Required[int]
    """The x-coordinate where the double click occurred."""

    y: Required[int]
    """The y-coordinate where the double click occurred."""


class InputInputItemListComputerCallActionDragPath(TypedDict, total=False):
    x: Required[int]
    """The x-coordinate."""

    y: Required[int]
    """The y-coordinate."""


class InputInputItemListComputerCallActionDrag(TypedDict, total=False):
    path: Required[Iterable[InputInputItemListComputerCallActionDragPath]]
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


class InputInputItemListComputerCallActionKeyPress(TypedDict, total=False):
    keys: Required[SequenceNotStr[str]]
    """The combination of keys the model is requesting to be pressed.

    This is an array of strings, each representing a key.
    """

    type: Required[Literal["keypress"]]
    """Specifies the event type.

    For a keypress action, this property is always set to `keypress`.
    """


class InputInputItemListComputerCallActionMove(TypedDict, total=False):
    type: Required[Literal["move"]]
    """Specifies the event type.

    For a move action, this property is always set to `move`.
    """

    x: Required[int]
    """The x-coordinate to move to."""

    y: Required[int]
    """The y-coordinate to move to."""


class InputInputItemListComputerCallActionScreenshot(TypedDict, total=False):
    type: Required[Literal["screenshot"]]
    """Specifies the event type.

    For a screenshot action, this property is always set to `screenshot`.
    """


class InputInputItemListComputerCallActionScroll(TypedDict, total=False):
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


class InputInputItemListComputerCallActionType(TypedDict, total=False):
    text: Required[str]
    """The text to type."""

    type: Required[Literal["type"]]
    """Specifies the event type.

    For a type action, this property is always set to `type`.
    """


class InputInputItemListComputerCallActionWait(TypedDict, total=False):
    type: Required[Literal["wait"]]
    """Specifies the event type.

    For a wait action, this property is always set to `wait`.
    """


InputInputItemListComputerCallAction: TypeAlias = Union[
    InputInputItemListComputerCallActionClick,
    InputInputItemListComputerCallActionDoubleClick,
    InputInputItemListComputerCallActionDrag,
    InputInputItemListComputerCallActionKeyPress,
    InputInputItemListComputerCallActionMove,
    InputInputItemListComputerCallActionScreenshot,
    InputInputItemListComputerCallActionScroll,
    InputInputItemListComputerCallActionType,
    InputInputItemListComputerCallActionWait,
]


class InputInputItemListComputerCallPendingSafetyCheck(TypedDict, total=False):
    id: Required[str]
    """The ID of the pending safety check."""

    code: Required[str]
    """The type of the pending safety check."""

    message: Required[str]
    """Details about the pending safety check."""


class InputInputItemListComputerCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the computer call."""

    action: Required[InputInputItemListComputerCallAction]
    """A click action."""

    call_id: Required[str]
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: Required[Iterable[InputInputItemListComputerCallPendingSafetyCheck]]
    """The pending safety checks for the computer call."""

    status: Required[Literal["in_progress", "completed", "incomplete"]]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Required[Literal["computer_call"]]
    """The type of the computer call. Always `computer_call`."""


class InputInputItemListComputerCallOutputOutput(TypedDict, total=False):
    type: Required[Literal["computer_screenshot"]]
    """Specifies the event type.

    For a computer screenshot, this property is always set to `computer_screenshot`.
    """

    file_id: str
    """The identifier of an uploaded file that contains the screenshot."""

    image_url: str
    """The URL of the screenshot image."""


class InputInputItemListComputerCallOutputAcknowledgedSafetyCheck(TypedDict, total=False):
    id: Required[str]
    """The ID of the pending safety check."""

    code: Optional[str]
    """The type of the pending safety check."""

    message: Optional[str]
    """Details about the pending safety check."""


class InputInputItemListComputerCallOutput(TypedDict, total=False):
    call_id: Required[str]
    """The ID of the computer tool call that produced the output."""

    output: Required[InputInputItemListComputerCallOutputOutput]
    """A computer screenshot image used with the computer use tool."""

    type: Required[Literal["computer_call_output"]]
    """The type of the computer tool call output. Always `computer_call_output`."""

    id: Optional[str]
    """The ID of the computer tool call output."""

    acknowledged_safety_checks: Optional[Iterable[InputInputItemListComputerCallOutputAcknowledgedSafetyCheck]]
    """
    The safety checks reported by the API that have been acknowledged by the
    developer.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """The status of the message input.

    One of `in_progress`, `completed`, or `incomplete`. Populated when input items
    are returned via API.
    """


class InputInputItemListWebSearchCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the web search tool call."""

    status: Required[Literal["in_progress", "searching", "completed", "failed"]]
    """The status of the web search tool call."""

    type: Required[Literal["web_search_call"]]
    """The type of the web search tool call. Always `web_search_call`."""


class InputInputItemListFunctionCall(TypedDict, total=False):
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


class InputInputItemListFunctionCallOutput(TypedDict, total=False):
    call_id: Required[str]
    """The unique ID of the function tool call generated by the model."""

    output: Required[str]
    """A JSON string of the output of the function tool call."""

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


class InputInputItemListReasoningSummary(TypedDict, total=False):
    text: Required[str]
    """
    A short summary of the reasoning used by the model when generating the response.
    """

    type: Required[Literal["summary_text"]]
    """The type of the object. Always `summary_text`."""


class InputInputItemListReasoning(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the reasoning content."""

    summary: Required[Iterable[InputInputItemListReasoningSummary]]
    """Reasoning text contents."""

    type: Required[Literal["reasoning"]]
    """The type of the object. Always `reasoning`."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


class InputInputItemListItemReference(TypedDict, total=False):
    id: Required[str]
    """The ID of the item to reference."""

    type: Optional[Literal["item_reference"]]
    """The type of item to reference. Always `item_reference`."""


InputInputItemList: TypeAlias = Union[
    InputInputItemListMessage,
    InputInputItemListMessage,
    InputInputItemListMessage,
    InputInputItemListFileSearchCall,
    InputInputItemListComputerCall,
    InputInputItemListComputerCallOutput,
    InputInputItemListWebSearchCall,
    InputInputItemListFunctionCall,
    InputInputItemListFunctionCallOutput,
    InputInputItemListReasoning,
    InputInputItemListItemReference,
]


class Reasoning(TypedDict, total=False):
    effort: Optional[Literal["low", "medium", "high"]]
    """**o-series models only**

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
    supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
    result in faster responses and fewer tokens used on reasoning in a response.
    """

    generate_summary: Optional[Literal["auto", "concise", "detailed"]]
    """**Deprecated:** use `summary` instead.

    A summary of the reasoning performed by the model. This can be useful for
    debugging and understanding the model's reasoning process. One of `auto`,
    `concise`, or `detailed`.
    """

    summary: Optional[Literal["auto", "concise", "detailed"]]
    """A summary of the reasoning performed by the model.

    This can be useful for debugging and understanding the model's reasoning
    process. One of `auto`, `concise`, or `detailed`.
    """


class TextFormatResponseFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]
    """The type of response format being defined. Always `text`."""


class TextFormatTextResponseFormatJsonSchema(TypedDict, total=False):
    name: Required[str]
    """The name of the response format.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    schema: Required[Dict[str, object]]
    """
    The schema for the response format, described as a JSON Schema object. Learn how
    to build JSON schemas [here](https://json-schema.org/).
    """

    type: Required[Literal["json_schema"]]
    """The type of response format being defined. Always `json_schema`."""

    description: str
    """
    A description of what the response format is for, used by the model to determine
    how to respond in the format.
    """

    strict: Optional[bool]
    """
    Whether to enable strict schema adherence when generating the output. If set to
    true, the model will always follow the exact schema defined in the `schema`
    field. Only a subset of JSON Schema is supported when `strict` is `true`. To
    learn more, read the
    [Structured Outputs guide](/docs/guides/structured-outputs).
    """


class TextFormatResponseFormatJsonObject(TypedDict, total=False):
    type: Required[Literal["json_object"]]
    """The type of response format being defined. Always `json_object`."""


TextFormat: TypeAlias = Union[
    TextFormatResponseFormatText, TextFormatTextResponseFormatJsonSchema, TextFormatResponseFormatJsonObject
]


class Text(TypedDict, total=False):
    format: TextFormat
    """An object specifying the format that the model must output.

    Configuring `{ "type": "json_schema" }` enables Structured Outputs, which
    ensures the model will match your supplied JSON schema. Learn more in the
    [Structured Outputs guide](/docs/guides/structured-outputs).

    The default format is `{ "type": "text" }` with no additional options.

    **Not recommended for gpt-4o and newer models:**

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """


class ToolChoiceToolChoiceTypes(TypedDict, total=False):
    type: Required[
        Literal["file_search", "web_search_preview", "computer_use_preview", "web_search_preview_2025_03_11"]
    ]
    """The type of hosted tool the model should to use.

    Learn more about [built-in tools](/docs/guides/tools).

    Allowed values are:

    - `file_search`
    - `web_search_preview`
    - `computer_use_preview`
    """


class ToolChoiceToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""

    type: Required[Literal["function"]]
    """For function calling, the type is always `function`."""


ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"], ToolChoiceToolChoiceTypes, ToolChoiceToolChoiceFunction
]


class ToolFileSearchFiltersComparisonFilter(TypedDict, total=False):
    key: Required[str]
    """The key to compare against the value."""

    type: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte"]]
    """Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    """

    value: Required[Union[str, float, bool]]
    """
    The value to compare against the attribute key; supports string, number, or
    boolean types.
    """


class ToolFileSearchFiltersCompoundFilterFilterComparisonFilter(TypedDict, total=False):
    key: Required[str]
    """The key to compare against the value."""

    type: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte"]]
    """Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    """

    value: Required[Union[str, float, bool]]
    """
    The value to compare against the attribute key; supports string, number, or
    boolean types.
    """


ToolFileSearchFiltersCompoundFilterFilter: TypeAlias = Union[
    ToolFileSearchFiltersCompoundFilterFilterComparisonFilter, object
]


class ToolFileSearchFiltersCompoundFilter(TypedDict, total=False):
    filters: Required[Iterable[ToolFileSearchFiltersCompoundFilterFilter]]
    """Array of filters to combine.

    Items can be `ComparisonFilter` or `CompoundFilter`.
    """

    type: Required[Literal["and", "or"]]
    """Type of operation: `and` or `or`."""


ToolFileSearchFilters: TypeAlias = Union[ToolFileSearchFiltersComparisonFilter, ToolFileSearchFiltersCompoundFilter]


class ToolFileSearchRankingOptions(TypedDict, total=False):
    ranker: Literal["auto", "default-2024-11-15"]
    """The ranker to use for the file search."""

    score_threshold: float
    """The score threshold for the file search, a number between 0 and 1.

    Numbers closer to 1 will attempt to return only the most relevant results, but
    may return fewer results.
    """


class ToolFileSearch(TypedDict, total=False):
    type: Required[Literal["file_search"]]
    """The type of the file search tool. Always `file_search`."""

    vector_store_ids: Required[SequenceNotStr[str]]
    """The IDs of the vector stores to search."""

    filters: Optional[ToolFileSearchFilters]
    """A filter to apply."""

    max_num_results: int
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: ToolFileSearchRankingOptions
    """Ranking options for search."""


class ToolFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""

    parameters: Required[Optional[Dict[str, object]]]
    """A JSON schema object describing the parameters of the function."""

    strict: Required[Optional[bool]]
    """Whether to enforce strict parameter validation. Default `true`."""

    type: Required[Literal["function"]]
    """The type of the function tool. Always `function`."""

    description: Optional[str]
    """A description of the function.

    Used by the model to determine whether or not to call the function.
    """


class ToolWebSearchPreviewToolUserLocation(TypedDict, total=False):
    type: Required[Literal["approximate"]]
    """The type of location approximation. Always `approximate`."""

    city: Optional[str]
    """Free text input for the city of the user, e.g. `San Francisco`."""

    country: Optional[str]
    """
    The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of
    the user, e.g. `US`.
    """

    region: Optional[str]
    """Free text input for the region of the user, e.g. `California`."""

    timezone: Optional[str]
    """
    The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the
    user, e.g. `America/Los_Angeles`.
    """


class ToolWebSearchPreviewTool(TypedDict, total=False):
    type: Required[Literal["web_search_preview", "web_search_preview_2025_03_11"]]
    """The type of the web search tool.

    One of `web_search_preview` or `web_search_preview_2025_03_11`.
    """

    search_context_size: Literal["low", "medium", "high"]
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[ToolWebSearchPreviewToolUserLocation]
    """The user's location."""


class ToolComputerUsePreview(TypedDict, total=False):
    display_height: Required[int]
    """The height of the computer display."""

    display_width: Required[int]
    """The width of the computer display."""

    environment: Required[Literal["windows", "mac", "linux", "ubuntu", "browser"]]
    """The type of computer environment to control."""

    type: Required[Literal["computer_use_preview"]]
    """The type of the computer use tool. Always `computer_use_preview`."""


Tool: TypeAlias = Union[ToolFileSearch, ToolFunction, ToolWebSearchPreviewTool, ToolComputerUsePreview]
