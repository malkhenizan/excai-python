# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ResponseCreateParams",
    "Conversation",
    "ConversationConversationParam",
    "InputInputItemList",
    "InputInputItemListMessage",
    "InputInputItemListMessageContentInputMessageContentList",
    "InputInputItemListMessageContentInputMessageContentListInputText",
    "InputInputItemListMessageContentInputMessageContentListInputImage",
    "InputInputItemListMessageContentInputMessageContentListInputFile",
    "InputInputItemListMessageContentInputMessageContentListInputAudio",
    "InputInputItemListMessageContentInputMessageContentListInputAudioInputAudio",
    "InputInputItemListFileSearchCall",
    "InputInputItemListFileSearchCallResult",
    "InputInputItemListComputerCall",
    "InputInputItemListComputerCallAction",
    "InputInputItemListComputerCallActionClick",
    "InputInputItemListComputerCallActionDoubleClick",
    "InputInputItemListComputerCallActionDrag",
    "InputInputItemListComputerCallActionDragPath",
    "InputInputItemListComputerCallActionKeypress",
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
    "InputInputItemListWebSearchCallAction",
    "InputInputItemListWebSearchCallActionSearch",
    "InputInputItemListWebSearchCallActionSearchSource",
    "InputInputItemListWebSearchCallActionOpenPage",
    "InputInputItemListWebSearchCallActionFind",
    "InputInputItemListFunctionCall",
    "InputInputItemListFunctionCallOutput",
    "InputInputItemListFunctionCallOutputOutputUnionMember1",
    "InputInputItemListFunctionCallOutputOutputUnionMember1InputText",
    "InputInputItemListFunctionCallOutputOutputUnionMember1InputImage",
    "InputInputItemListFunctionCallOutputOutputUnionMember1InputFile",
    "InputInputItemListReasoning",
    "InputInputItemListReasoningSummary",
    "InputInputItemListReasoningContent",
    "InputInputItemListImageGenerationCall",
    "InputInputItemListCodeInterpreterCall",
    "InputInputItemListCodeInterpreterCallOutput",
    "InputInputItemListCodeInterpreterCallOutputLogs",
    "InputInputItemListCodeInterpreterCallOutputImage",
    "InputInputItemListLocalShellCall",
    "InputInputItemListLocalShellCallAction",
    "InputInputItemListLocalShellCallOutput",
    "InputInputItemListMcpListTools",
    "InputInputItemListMcpListToolsTool",
    "InputInputItemListMcpApprovalRequest",
    "InputInputItemListMcpApprovalResponse",
    "InputInputItemListMcpCall",
    "InputInputItemListCustomToolCallOutput",
    "InputInputItemListCustomToolCallOutputOutputOutputContentList",
    "InputInputItemListCustomToolCallOutputOutputOutputContentListInputText",
    "InputInputItemListCustomToolCallOutputOutputOutputContentListInputImage",
    "InputInputItemListCustomToolCallOutputOutputOutputContentListInputFile",
    "InputInputItemListCustomToolCall",
    "InputInputItemListItemReference",
    "Prompt",
    "PromptVariables",
    "PromptVariablesInputTextContent",
    "PromptVariablesInputImageContent",
    "PromptVariablesInputFileContent",
    "Reasoning",
    "StreamOptions",
    "Text",
    "TextFormat",
    "TextFormatText",
    "TextFormatJsonSchema",
    "TextFormatJsonObject",
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
]


class ResponseCreateParams(TypedDict, total=False):
    background: Optional[bool]
    """
    Whether to run the model response in the background.
    [Learn more](https://platform.excai.com/docs/guides/background).
    """

    conversation: Optional[Conversation]
    """The conversation that this response belongs to.

    Items from this conversation are prepended to `input_items` for this response
    request. Input items and output items from this response are automatically added
    to this conversation after this response completes.
    """

    include: Optional[
        List[
            Literal[
                "code_interpreter_call.outputs",
                "computer_call_output.output.image_url",
                "file_search_call.results",
                "message.input_image.image_url",
                "message.output_text.logprobs",
                "reasoning.encrypted_content",
            ]
        ]
    ]
    """Specify additional output data to include in the model response.

    Currently supported values are:

    - `web_search_call.action.sources`: Include the sources of the web search tool
      call.
    - `code_interpreter_call.outputs`: Includes the outputs of python code execution
      in code interpreter tool call items.
    - `computer_call_output.output.image_url`: Include image urls from the computer
      call output.
    - `file_search_call.results`: Include the search results of the file search tool
      call.
    - `message.input_image.image_url`: Include image urls from the input message.
    - `message.output_text.logprobs`: Include logprobs with assistant messages.
    - `reasoning.encrypted_content`: Includes an encrypted version of reasoning
      tokens in reasoning item outputs. This enables reasoning items to be used in
      multi-turn conversations when using the Responses API statelessly (like when
      the `store` parameter is set to `false`, or when an organization is enrolled
      in the zero data retention program).
    """

    input: Union[str, Iterable[InputInputItemList]]
    """Text, image, or file inputs to the model, used to generate a response.

    Learn more:

    - [Text inputs and outputs](https://platform.excai.com/docs/guides/text)
    - [Image inputs](https://platform.excai.com/docs/guides/images)
    - [File inputs](https://platform.excai.com/docs/guides/pdf-files)
    - [Conversation state](https://platform.excai.com/docs/guides/conversation-state)
    - [Function calling](https://platform.excai.com/docs/guides/function-calling)
    """

    instructions: Optional[str]
    """A system (or developer) message inserted into the model's context.

    When using along with `previous_response_id`, the instructions from a previous
    response will not be carried over to the next response. This makes it simple to
    swap out system (or developer) messages in new responses.
    """

    max_output_tokens: Optional[int]
    """
    An upper bound for the number of tokens that can be generated for a response,
    including visible output tokens and
    [reasoning tokens](https://platform.excai.com/docs/guides/reasoning).
    """

    max_tool_calls: Optional[int]
    """
    The maximum number of total calls to built-in tools that can be processed in a
    response. This maximum number applies across all built-in tool calls, not per
    individual tool. Any further attempts to call a tool by the model will be
    ignored.
    """

    metadata: Optional[Dict[str, str]]
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

    parallel_tool_calls: Optional[bool]
    """Whether to allow the model to run tool calls in parallel."""

    previous_response_id: Optional[str]
    """The unique ID of the previous response to the model.

    Use this to create multi-turn conversations. Learn more about
    [conversation state](https://platform.excai.com/docs/guides/conversation-state).
    Cannot be used in conjunction with `conversation`.
    """

    prompt: Optional[Prompt]
    """
    Reference to a prompt template and its variables.
    [Learn more](https://platform.excai.com/docs/guides/text?api-mode=responses#reusable-prompts).
    """

    prompt_cache_key: str
    """
    Used by EXCai to cache responses for similar requests to optimize your cache hit
    rates. Replaces the `user` field.
    [Learn more](https://platform.excai.com/docs/guides/prompt-caching).
    """

    reasoning: Optional[Reasoning]
    """**gpt-5 and o-series models only**

    Configuration options for
    [reasoning models](https://platform.excai.com/docs/guides/reasoning).
    """

    safety_identifier: str
    """
    A stable identifier used to help detect users of your application that may be
    violating EXCai's usage policies. The IDs should be a string that uniquely
    identifies each user. We recommend hashing their username or email address, in
    order to avoid sending us any identifying information.
    [Learn more](https://platform.excai.com/docs/guides/safety-best-practices#safety-identifiers).
    """

    service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]]
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

    store: Optional[bool]
    """Whether to store the generated model response for later retrieval via API."""

    stream: Optional[bool]
    """
    If set to true, the model response data will be streamed to the client as it is
    generated using
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
    See the
    [Streaming section below](https://platform.excai.com/docs/api-reference/responses-streaming)
    for more information.
    """

    stream_options: Optional[StreamOptions]
    """Options for streaming responses. Only set this when you set `stream: true`."""

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or `top_p` but not both.
    """

    text: Text
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](https://platform.excai.com/docs/guides/text)
    - [Structured Outputs](https://platform.excai.com/docs/guides/structured-outputs)
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

    top_logprobs: Optional[int]
    """
    An integer between 0 and 20 specifying the number of most likely tokens to
    return at each token position, each with an associated log probability.
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

    - `auto`: If the input to this Response exceeds the model's context window size,
      the model will truncate the response to fit the context window by dropping
      items from the beginning of the conversation.
    - `disabled` (default): If the input size will exceed the context window size
      for a model, the request will fail with a 400 error.
    """

    user: str
    """This field is being replaced by `safety_identifier` and `prompt_cache_key`.

    Use `prompt_cache_key` instead to maintain caching optimizations. A stable
    identifier for your end-users. Used to boost cache hit rates by better bucketing
    similar requests and to help EXCai detect and prevent abuse.
    [Learn more](https://platform.excai.com/docs/guides/safety-best-practices#safety-identifiers).
    """


class ConversationConversationParam(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the conversation."""


Conversation: TypeAlias = Union[str, ConversationConversationParam]


class InputInputItemListMessageContentInputMessageContentListInputText(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class InputInputItemListMessageContentInputMessageContentListInputImage(TypedDict, total=False):
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


class InputInputItemListMessageContentInputMessageContentListInputFile(TypedDict, total=False):
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


class InputInputItemListMessageContentInputMessageContentListInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class InputInputItemListMessageContentInputMessageContentListInputAudio(TypedDict, total=False):
    input_audio: Required[InputInputItemListMessageContentInputMessageContentListInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


InputInputItemListMessageContentInputMessageContentList: TypeAlias = Union[
    InputInputItemListMessageContentInputMessageContentListInputText,
    InputInputItemListMessageContentInputMessageContentListInputImage,
    InputInputItemListMessageContentInputMessageContentListInputFile,
    InputInputItemListMessageContentInputMessageContentListInputAudio,
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


class InputInputItemListComputerCallActionKeypress(TypedDict, total=False):
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
    InputInputItemListComputerCallActionKeypress,
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


class InputInputItemListWebSearchCallActionSearchSource(TypedDict, total=False):
    type: Required[Literal["url"]]
    """The type of source. Always `url`."""

    url: Required[str]
    """The URL of the source."""


class InputInputItemListWebSearchCallActionSearch(TypedDict, total=False):
    query: Required[str]
    """The search query."""

    type: Required[Literal["search"]]
    """The action type."""

    sources: Iterable[InputInputItemListWebSearchCallActionSearchSource]
    """The sources used in the search."""


class InputInputItemListWebSearchCallActionOpenPage(TypedDict, total=False):
    type: Required[Literal["open_page"]]
    """The action type."""

    url: Required[str]
    """The URL opened by the model."""


class InputInputItemListWebSearchCallActionFind(TypedDict, total=False):
    pattern: Required[str]
    """The pattern or text to search for within the page."""

    type: Required[Literal["find"]]
    """The action type."""

    url: Required[str]
    """The URL of the page searched for the pattern."""


InputInputItemListWebSearchCallAction: TypeAlias = Union[
    InputInputItemListWebSearchCallActionSearch,
    InputInputItemListWebSearchCallActionOpenPage,
    InputInputItemListWebSearchCallActionFind,
]


class InputInputItemListWebSearchCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the web search tool call."""

    action: Required[InputInputItemListWebSearchCallAction]
    """
    An object describing the specific action taken in this web search call. Includes
    details on how the model used the web (search, open_page, find).
    """

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


class InputInputItemListFunctionCallOutputOutputUnionMember1InputText(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class InputInputItemListFunctionCallOutputOutputUnionMember1InputImage(TypedDict, total=False):
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


class InputInputItemListFunctionCallOutputOutputUnionMember1InputFile(TypedDict, total=False):
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


InputInputItemListFunctionCallOutputOutputUnionMember1: TypeAlias = Union[
    InputInputItemListFunctionCallOutputOutputUnionMember1InputText,
    InputInputItemListFunctionCallOutputOutputUnionMember1InputImage,
    InputInputItemListFunctionCallOutputOutputUnionMember1InputFile,
]


class InputInputItemListFunctionCallOutput(TypedDict, total=False):
    call_id: Required[str]
    """The unique ID of the function tool call generated by the model."""

    output: Required[Union[str, Iterable[InputInputItemListFunctionCallOutputOutputUnionMember1]]]
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


class InputInputItemListReasoningSummary(TypedDict, total=False):
    text: Required[str]
    """A summary of the reasoning output from the model so far."""

    type: Required[Literal["summary_text"]]
    """The type of the object. Always `summary_text`."""


class InputInputItemListReasoningContent(TypedDict, total=False):
    text: Required[str]
    """The reasoning text from the model."""

    type: Required[Literal["reasoning_text"]]
    """The type of the reasoning text. Always `reasoning_text`."""


class InputInputItemListReasoning(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the reasoning content."""

    summary: Required[Iterable[InputInputItemListReasoningSummary]]
    """Reasoning summary content."""

    type: Required[Literal["reasoning"]]
    """The type of the object. Always `reasoning`."""

    content: Iterable[InputInputItemListReasoningContent]
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


class InputInputItemListImageGenerationCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the image generation call."""

    result: Required[Optional[str]]
    """The generated image encoded in base64."""

    status: Required[Literal["in_progress", "completed", "generating", "failed"]]
    """The status of the image generation call."""

    type: Required[Literal["image_generation_call"]]
    """The type of the image generation call. Always `image_generation_call`."""


class InputInputItemListCodeInterpreterCallOutputLogs(TypedDict, total=False):
    logs: Required[str]
    """The logs output from the code interpreter."""

    type: Required[Literal["logs"]]
    """The type of the output. Always 'logs'."""


class InputInputItemListCodeInterpreterCallOutputImage(TypedDict, total=False):
    type: Required[Literal["image"]]
    """The type of the output. Always 'image'."""

    url: Required[str]
    """The URL of the image output from the code interpreter."""


InputInputItemListCodeInterpreterCallOutput: TypeAlias = Union[
    InputInputItemListCodeInterpreterCallOutputLogs, InputInputItemListCodeInterpreterCallOutputImage
]


class InputInputItemListCodeInterpreterCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the code interpreter tool call."""

    code: Required[Optional[str]]
    """The code to run, or null if not available."""

    container_id: Required[str]
    """The ID of the container used to run the code."""

    outputs: Required[Optional[Iterable[InputInputItemListCodeInterpreterCallOutput]]]
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


class InputInputItemListLocalShellCallAction(TypedDict, total=False):
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


class InputInputItemListLocalShellCall(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the local shell call."""

    action: Required[InputInputItemListLocalShellCallAction]
    """Execute a shell command on the server."""

    call_id: Required[str]
    """The unique ID of the local shell tool call generated by the model."""

    status: Required[Literal["in_progress", "completed", "incomplete"]]
    """The status of the local shell call."""

    type: Required[Literal["local_shell_call"]]
    """The type of the local shell call. Always `local_shell_call`."""


class InputInputItemListLocalShellCallOutput(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the local shell tool call generated by the model."""

    output: Required[str]
    """A JSON string of the output of the local shell tool call."""

    type: Required[Literal["local_shell_call_output"]]
    """The type of the local shell tool call output. Always `local_shell_call_output`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """The status of the item. One of `in_progress`, `completed`, or `incomplete`."""


class InputInputItemListMcpListToolsTool(TypedDict, total=False):
    input_schema: Required[object]
    """The JSON schema describing the tool's input."""

    name: Required[str]
    """The name of the tool."""

    annotations: Optional[object]
    """Additional annotations about the tool."""

    description: Optional[str]
    """The description of the tool."""


class InputInputItemListMcpListTools(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the list."""

    server_label: Required[str]
    """The label of the MCP server."""

    tools: Required[Iterable[InputInputItemListMcpListToolsTool]]
    """The tools available on the server."""

    type: Required[Literal["mcp_list_tools"]]
    """The type of the item. Always `mcp_list_tools`."""

    error: Optional[str]
    """Error message if the server could not list tools."""


class InputInputItemListMcpApprovalRequest(TypedDict, total=False):
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


class InputInputItemListMcpApprovalResponse(TypedDict, total=False):
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


class InputInputItemListMcpCall(TypedDict, total=False):
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


class InputInputItemListCustomToolCallOutputOutputOutputContentListInputText(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class InputInputItemListCustomToolCallOutputOutputOutputContentListInputImage(TypedDict, total=False):
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


class InputInputItemListCustomToolCallOutputOutputOutputContentListInputFile(TypedDict, total=False):
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


InputInputItemListCustomToolCallOutputOutputOutputContentList: TypeAlias = Union[
    InputInputItemListCustomToolCallOutputOutputOutputContentListInputText,
    InputInputItemListCustomToolCallOutputOutputOutputContentListInputImage,
    InputInputItemListCustomToolCallOutputOutputOutputContentListInputFile,
]


class InputInputItemListCustomToolCallOutput(TypedDict, total=False):
    call_id: Required[str]
    """The call ID, used to map this custom tool call output to a custom tool call."""

    output: Required[Union[str, Iterable[InputInputItemListCustomToolCallOutputOutputOutputContentList]]]
    """
    The output from the custom tool call generated by your code. Can be a string or
    an list of output content.
    """

    type: Required[Literal["custom_tool_call_output"]]
    """The type of the custom tool call output. Always `custom_tool_call_output`."""

    id: str
    """The unique ID of the custom tool call output in the EXCai platform."""


class InputInputItemListCustomToolCall(TypedDict, total=False):
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
    InputInputItemListImageGenerationCall,
    InputInputItemListCodeInterpreterCall,
    InputInputItemListLocalShellCall,
    InputInputItemListLocalShellCallOutput,
    InputInputItemListMcpListTools,
    InputInputItemListMcpApprovalRequest,
    InputInputItemListMcpApprovalResponse,
    InputInputItemListMcpCall,
    InputInputItemListCustomToolCallOutput,
    InputInputItemListCustomToolCall,
    InputInputItemListItemReference,
]


class PromptVariablesInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class PromptVariablesInputImageContent(TypedDict, total=False):
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


class PromptVariablesInputFileContent(TypedDict, total=False):
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


PromptVariables: TypeAlias = Union[
    str, PromptVariablesInputTextContent, PromptVariablesInputImageContent, PromptVariablesInputFileContent
]


class Prompt(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the prompt template to use."""

    variables: Optional[Dict[str, PromptVariables]]
    """Optional map of values to substitute in for variables in your prompt.

    The substitution values can either be strings, or other Response input types
    like images or files.
    """

    version: Optional[str]
    """Optional version of the prompt template."""


class Reasoning(TypedDict, total=False):
    effort: Optional[Literal["minimal", "low", "medium", "high"]]
    """
    Constrains effort on reasoning for
    [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
    supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
    effort can result in faster responses and fewer tokens used on reasoning in a
    response.

    Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
    effort.
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


class StreamOptions(TypedDict, total=False):
    include_obfuscation: bool
    """When true, stream obfuscation will be enabled.

    Stream obfuscation adds random characters to an `obfuscation` field on streaming
    delta events to normalize payload sizes as a mitigation to certain side-channel
    attacks. These obfuscation fields are included by default, but add a small
    amount of overhead to the data stream. You can set `include_obfuscation` to
    false to optimize for bandwidth if you trust the network links between your
    application and the EXCai API.
    """


class TextFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]
    """The type of response format being defined. Always `text`."""


class TextFormatJsonSchema(TypedDict, total=False):
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
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
    """


class TextFormatJsonObject(TypedDict, total=False):
    type: Required[Literal["json_object"]]
    """The type of response format being defined. Always `json_object`."""


TextFormat: TypeAlias = Union[TextFormatText, TextFormatJsonSchema, TextFormatJsonObject]


class Text(TypedDict, total=False):
    format: TextFormat
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

    verbosity: Optional[Literal["low", "medium", "high"]]
    """Constrains the verbosity of the model's response.

    Lower values will result in more concise responses, while higher values will
    result in more verbose responses. Currently supported values are `low`,
    `medium`, and `high`.
    """


class ToolChoiceToolChoiceAllowed(TypedDict, total=False):
    mode: Required[Literal["auto", "required"]]
    """Constrains the tools available to the model to a pre-defined set.

    `auto` allows the model to pick from among the allowed tools and generate a
    message.

    `required` requires the model to call one or more of the allowed tools.
    """

    tools: Required[Iterable[Dict[str, object]]]
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

    type: Required[Literal["allowed_tools"]]
    """Allowed tool configuration type. Always `allowed_tools`."""


class ToolChoiceToolChoiceTypes(TypedDict, total=False):
    type: Required[
        Literal[
            "file_search",
            "web_search_preview",
            "computer_use_preview",
            "web_search_preview_2025_03_11",
            "image_generation",
            "code_interpreter",
        ]
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


class ToolChoiceToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""

    type: Required[Literal["function"]]
    """For function calling, the type is always `function`."""


class ToolChoiceToolChoiceMcp(TypedDict, total=False):
    server_label: Required[str]
    """The label of the MCP server to use."""

    type: Required[Literal["mcp"]]
    """For MCP tools, the type is always `mcp`."""

    name: Optional[str]
    """The name of the tool to call on the server."""


class ToolChoiceToolChoiceCustom(TypedDict, total=False):
    name: Required[str]
    """The name of the custom tool to call."""

    type: Required[Literal["custom"]]
    """For custom tool calling, the type is always `custom`."""


ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"],
    ToolChoiceToolChoiceAllowed,
    ToolChoiceToolChoiceTypes,
    ToolChoiceToolChoiceFunction,
    ToolChoiceToolChoiceMcp,
    ToolChoiceToolChoiceCustom,
]


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


class ToolFileSearchFiltersComparisonFilter(TypedDict, total=False):
    key: Required[str]
    """The key to compare against the value."""

    type: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte"]]
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

    value: Required[Union[str, float, bool, SequenceNotStr[Union[str, float]]]]
    """
    The value to compare against the attribute key; supports string, number, or
    boolean types.
    """


class ToolFileSearchFiltersCompoundFilterFilterComparisonFilter(TypedDict, total=False):
    key: Required[str]
    """The key to compare against the value."""

    type: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte"]]
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

    value: Required[Union[str, float, bool, SequenceNotStr[Union[str, float]]]]
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


class ToolComputerUsePreview(TypedDict, total=False):
    display_height: Required[int]
    """The height of the computer display."""

    display_width: Required[int]
    """The width of the computer display."""

    environment: Required[Literal["windows", "mac", "linux", "ubuntu", "browser"]]
    """The type of computer environment to control."""

    type: Required[Literal["computer_use_preview"]]
    """The type of the computer use tool. Always `computer_use_preview`."""


class ToolWebSearchToolFilters(TypedDict, total=False):
    allowed_domains: Optional[SequenceNotStr[str]]
    """Allowed domains for the search.

    If not provided, all domains are allowed. Subdomains of the provided domains are
    allowed as well.

    Example: `["pubmed.ncbi.nlm.nih.gov"]`
    """


class ToolWebSearchToolUserLocation(TypedDict, total=False):
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

    type: Literal["approximate"]
    """The type of location approximation. Always `approximate`."""


class ToolWebSearchTool(TypedDict, total=False):
    type: Required[Literal["web_search", "web_search_2025_08_26"]]
    """The type of the web search tool.

    One of `web_search` or `web_search_2025_08_26`.
    """

    filters: Optional[ToolWebSearchToolFilters]
    """Filters for the search."""

    search_context_size: Literal["low", "medium", "high"]
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[ToolWebSearchToolUserLocation]
    """The approximate location of the user."""


class ToolMcpAllowedToolsMcpToolFilter(TypedDict, total=False):
    read_only: bool
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: SequenceNotStr[str]
    """List of allowed tool names."""


ToolMcpAllowedTools: TypeAlias = Union[SequenceNotStr[str], ToolMcpAllowedToolsMcpToolFilter]


class ToolMcpRequireApprovalMcpToolApprovalFilterAlways(TypedDict, total=False):
    read_only: bool
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: SequenceNotStr[str]
    """List of allowed tool names."""


class ToolMcpRequireApprovalMcpToolApprovalFilterNever(TypedDict, total=False):
    read_only: bool
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: SequenceNotStr[str]
    """List of allowed tool names."""


class ToolMcpRequireApprovalMcpToolApprovalFilter(TypedDict, total=False):
    always: ToolMcpRequireApprovalMcpToolApprovalFilterAlways
    """A filter object to specify which tools are allowed."""

    never: ToolMcpRequireApprovalMcpToolApprovalFilterNever
    """A filter object to specify which tools are allowed."""


ToolMcpRequireApproval: TypeAlias = Union[ToolMcpRequireApprovalMcpToolApprovalFilter, Literal["always", "never"]]


class ToolMcp(TypedDict, total=False):
    server_label: Required[str]
    """A label for this MCP server, used to identify it in tool calls."""

    type: Required[Literal["mcp"]]
    """The type of the MCP tool. Always `mcp`."""

    allowed_tools: Optional[ToolMcpAllowedTools]
    """List of allowed tool names or a filter object."""

    authorization: str
    """
    An OAuth access token that can be used with a remote MCP server, either with a
    custom MCP server URL or a service connector. Your application must handle the
    OAuth authorization flow and provide the token here.
    """

    connector_id: Literal[
        "connector_dropbox",
        "connector_gmail",
        "connector_googlecalendar",
        "connector_googledrive",
        "connector_microsoftteams",
        "connector_outlookcalendar",
        "connector_outlookemail",
        "connector_sharepoint",
    ]
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

    headers: Optional[Dict[str, str]]
    """Optional HTTP headers to send to the MCP server.

    Use for authentication or other purposes.
    """

    require_approval: Optional[ToolMcpRequireApproval]
    """Specify which of the MCP server's tools require approval."""

    server_description: str
    """Optional description of the MCP server, used to provide more context."""

    server_url: str
    """The URL for the MCP server.

    One of `server_url` or `connector_id` must be provided.
    """


class ToolCodeInterpreterContainerCodeInterpreterToolAuto(TypedDict, total=False):
    type: Required[Literal["auto"]]
    """Always `auto`."""

    file_ids: SequenceNotStr[str]
    """An optional list of uploaded files to make available to your code."""


ToolCodeInterpreterContainer: TypeAlias = Union[str, ToolCodeInterpreterContainerCodeInterpreterToolAuto]


class ToolCodeInterpreter(TypedDict, total=False):
    container: Required[ToolCodeInterpreterContainer]
    """The code interpreter container.

    Can be a container ID or an object that specifies uploaded file IDs to make
    available to your code.
    """

    type: Required[Literal["code_interpreter"]]
    """The type of the code interpreter tool. Always `code_interpreter`."""


class ToolImageGenerationInputImageMask(TypedDict, total=False):
    file_id: str
    """File ID for the mask image."""

    image_url: str
    """Base64-encoded mask image."""


class ToolImageGeneration(TypedDict, total=False):
    type: Required[Literal["image_generation"]]
    """The type of the image generation tool. Always `image_generation`."""

    background: Literal["transparent", "opaque", "auto"]
    """Background type for the generated image.

    One of `transparent`, `opaque`, or `auto`. Default: `auto`.
    """

    input_fidelity: Optional[Literal["high", "low"]]
    """
    Control how much effort the model will exert to match the style and features,
    especially facial features, of input images. This parameter is only supported
    for `gpt-image-1`. Unsupported for `gpt-image-1-mini`. Supports `high` and
    `low`. Defaults to `low`.
    """

    input_image_mask: ToolImageGenerationInputImageMask
    """Optional mask for inpainting.

    Contains `image_url` (string, optional) and `file_id` (string, optional).
    """

    model: Literal["gpt-image-1", "gpt-image-1-mini"]
    """The image generation model to use. Default: `gpt-image-1`."""

    moderation: Literal["auto", "low"]
    """Moderation level for the generated image. Default: `auto`."""

    output_compression: int
    """Compression level for the output image. Default: 100."""

    output_format: Literal["png", "webp", "jpeg"]
    """The output format of the generated image.

    One of `png`, `webp`, or `jpeg`. Default: `png`.
    """

    partial_images: int
    """
    Number of partial images to generate in streaming mode, from 0 (default value)
    to 3.
    """

    quality: Literal["low", "medium", "high", "auto"]
    """The quality of the generated image.

    One of `low`, `medium`, `high`, or `auto`. Default: `auto`.
    """

    size: Literal["1024x1024", "1024x1536", "1536x1024", "auto"]
    """The size of the generated image.

    One of `1024x1024`, `1024x1536`, `1536x1024`, or `auto`. Default: `auto`.
    """


class ToolLocalShell(TypedDict, total=False):
    type: Required[Literal["local_shell"]]
    """The type of the local shell tool. Always `local_shell`."""


class ToolCustomFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]
    """Unconstrained text format. Always `text`."""


class ToolCustomFormatGrammar(TypedDict, total=False):
    definition: Required[str]
    """The grammar definition."""

    syntax: Required[Literal["lark", "regex"]]
    """The syntax of the grammar definition. One of `lark` or `regex`."""

    type: Required[Literal["grammar"]]
    """Grammar format. Always `grammar`."""


ToolCustomFormat: TypeAlias = Union[ToolCustomFormatText, ToolCustomFormatGrammar]


class ToolCustom(TypedDict, total=False):
    name: Required[str]
    """The name of the custom tool, used to identify it in tool calls."""

    type: Required[Literal["custom"]]
    """The type of the custom tool. Always `custom`."""

    description: str
    """Optional description of the custom tool, used to provide more context."""

    format: ToolCustomFormat
    """The input format for the custom tool. Default is unconstrained text."""


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


Tool: TypeAlias = Union[
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
]
