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
    "Output",
    "OutputMessage",
    "OutputMessageContent",
    "OutputMessageContentOutputTextContent",
    "OutputMessageContentOutputTextContentAnnotation",
    "OutputMessageContentOutputTextContentAnnotationFileCitation",
    "OutputMessageContentOutputTextContentAnnotationURLCitation",
    "OutputMessageContentOutputTextContentAnnotationFilePath",
    "OutputMessageContentRefusalContent",
    "OutputFileSearchCall",
    "OutputFileSearchCallResult",
    "OutputFunctionCall",
    "OutputWebSearchCall",
    "OutputComputerCall",
    "OutputComputerCallAction",
    "OutputComputerCallActionClick",
    "OutputComputerCallActionDoubleClick",
    "OutputComputerCallActionDrag",
    "OutputComputerCallActionDragPath",
    "OutputComputerCallActionKeyPress",
    "OutputComputerCallActionMove",
    "OutputComputerCallActionScreenshot",
    "OutputComputerCallActionScroll",
    "OutputComputerCallActionType",
    "OutputComputerCallActionWait",
    "OutputComputerCallPendingSafetyCheck",
    "OutputReasoning",
    "OutputReasoningSummary",
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
    "Reasoning",
    "Text",
    "TextFormat",
    "TextFormatResponseFormatText",
    "TextFormatTextResponseFormatJsonSchema",
    "TextFormatResponseFormatJsonObject",
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


class OutputMessageContentOutputTextContentAnnotationFileCitation(BaseModel):
    file_id: str
    """The ID of the file."""

    index: int
    """The index of the file in the list of files."""

    type: Literal["file_citation"]
    """The type of the file citation. Always `file_citation`."""


class OutputMessageContentOutputTextContentAnnotationURLCitation(BaseModel):
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


class OutputMessageContentOutputTextContentAnnotationFilePath(BaseModel):
    file_id: str
    """The ID of the file."""

    index: int
    """The index of the file in the list of files."""

    type: Literal["file_path"]
    """The type of the file path. Always `file_path`."""


OutputMessageContentOutputTextContentAnnotation: TypeAlias = Annotated[
    Union[
        OutputMessageContentOutputTextContentAnnotationFileCitation,
        OutputMessageContentOutputTextContentAnnotationURLCitation,
        OutputMessageContentOutputTextContentAnnotationFilePath,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputMessageContentOutputTextContent(BaseModel):
    annotations: List[OutputMessageContentOutputTextContentAnnotation]
    """The annotations of the text output."""

    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class OutputMessageContentRefusalContent(BaseModel):
    refusal: str
    """The refusal explanationfrom the model."""

    type: Literal["refusal"]
    """The type of the refusal. Always `refusal`."""


OutputMessageContent: TypeAlias = Union[OutputMessageContentOutputTextContent, OutputMessageContentRefusalContent]


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


class OutputWebSearchCall(BaseModel):
    id: str
    """The unique ID of the web search tool call."""

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


class OutputComputerCallActionKeyPress(BaseModel):
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


OutputComputerCallAction: TypeAlias = Union[
    OutputComputerCallActionClick,
    OutputComputerCallActionDoubleClick,
    OutputComputerCallActionDrag,
    OutputComputerCallActionKeyPress,
    OutputComputerCallActionMove,
    OutputComputerCallActionScreenshot,
    OutputComputerCallActionScroll,
    OutputComputerCallActionType,
    OutputComputerCallActionWait,
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
    """
    A short summary of the reasoning used by the model when generating the response.
    """

    type: Literal["summary_text"]
    """The type of the object. Always `summary_text`."""


class OutputReasoning(BaseModel):
    id: str
    """The unique identifier of the reasoning content."""

    summary: List[OutputReasoningSummary]
    """Reasoning text contents."""

    type: Literal["reasoning"]
    """The type of the object. Always `reasoning`."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """


Output: TypeAlias = Annotated[
    Union[
        OutputMessage,
        OutputFileSearchCall,
        OutputFunctionCall,
        OutputWebSearchCall,
        OutputComputerCall,
        OutputReasoning,
    ],
    PropertyInfo(discriminator="type"),
]


class ToolChoiceToolChoiceTypes(BaseModel):
    type: Literal["file_search", "web_search_preview", "computer_use_preview", "web_search_preview_2025_03_11"]
    """The type of hosted tool the model should to use.

    Learn more about [built-in tools](/docs/guides/tools).

    Allowed values are:

    - `file_search`
    - `web_search_preview`
    - `computer_use_preview`
    """


class ToolChoiceToolChoiceFunction(BaseModel):
    name: str
    """The name of the function to call."""

    type: Literal["function"]
    """For function calling, the type is always `function`."""


ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"], ToolChoiceToolChoiceTypes, ToolChoiceToolChoiceFunction
]


class ToolFileSearchFiltersComparisonFilter(BaseModel):
    key: str
    """The key to compare against the value."""

    type: Literal["eq", "ne", "gt", "gte", "lt", "lte"]
    """Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    """

    value: Union[str, float, bool]
    """
    The value to compare against the attribute key; supports string, number, or
    boolean types.
    """


class ToolFileSearchFiltersCompoundFilterFilterComparisonFilter(BaseModel):
    key: str
    """The key to compare against the value."""

    type: Literal["eq", "ne", "gt", "gte", "lt", "lte"]
    """Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    """

    value: Union[str, float, bool]
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


class ToolComputerUsePreview(BaseModel):
    display_height: int
    """The height of the computer display."""

    display_width: int
    """The width of the computer display."""

    environment: Literal["windows", "mac", "linux", "ubuntu", "browser"]
    """The type of computer environment to control."""

    type: Literal["computer_use_preview"]
    """The type of the computer use tool. Always `computer_use_preview`."""


Tool: TypeAlias = Annotated[
    Union[ToolFileSearch, ToolFunction, ToolWebSearchPreviewTool, ToolComputerUsePreview],
    PropertyInfo(discriminator="type"),
]


class Reasoning(BaseModel):
    effort: Optional[Literal["low", "medium", "high"]] = None
    """**o-series models only**

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
    supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
    result in faster responses and fewer tokens used on reasoning in a response.
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


class TextFormatResponseFormatText(BaseModel):
    type: Literal["text"]
    """The type of response format being defined. Always `text`."""


class TextFormatTextResponseFormatJsonSchema(BaseModel):
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
    [Structured Outputs guide](/docs/guides/structured-outputs).
    """


class TextFormatResponseFormatJsonObject(BaseModel):
    type: Literal["json_object"]
    """The type of response format being defined. Always `json_object`."""


TextFormat: TypeAlias = Union[
    TextFormatResponseFormatText, TextFormatTextResponseFormatJsonSchema, TextFormatResponseFormatJsonObject
]


class Text(BaseModel):
    format: Optional[TextFormat] = None
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


class UsageInputTokensDetails(BaseModel):
    cached_tokens: int
    """The number of tokens that were retrieved from the cache.

    [More on prompt caching](/docs/guides/prompt-caching).
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

    instructions: Optional[str] = None
    """
    Inserts a system (or developer) message as the first item in the model's
    context.

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
    """Model ID used to generate the response, like `gpt-4o` or `o3`.

    OpenAI offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model guide](/docs/models) to
    browse and compare available models.
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

    The two categories of tools you can provide the model are:

    - **Built-in tools**: Tools that are provided by OpenAI that extend the model's
      capabilities, like [web search](/docs/guides/tools-web-search) or
      [file search](/docs/guides/tools-file-search). Learn more about
      [built-in tools](/docs/guides/tools).
    - **Function calls (custom tools)**: Functions that are defined by you, enabling
      the model to call your own code. Learn more about
      [function calling](/docs/guides/function-calling).
    """

    top_p: Optional[float] = None
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """

    max_output_tokens: Optional[int] = None
    """
    An upper bound for the number of tokens that can be generated for a response,
    including visible output tokens and [reasoning tokens](/docs/guides/reasoning).
    """

    output_text: Optional[str] = None
    """
    SDK-only convenience property that contains the aggregated text output from all
    `output_text` items in the `output` array, if any are present. Supported in the
    Python and JavaScript SDKs.
    """

    previous_response_id: Optional[str] = None
    """The unique ID of the previous response to the model.

    Use this to create multi-turn conversations. Learn more about
    [conversation state](/docs/guides/conversation-state).
    """

    reasoning: Optional[Reasoning] = None
    """**o-series models only**

    Configuration options for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    """

    service_tier: Optional[Literal["auto", "default", "flex"]] = None
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

    status: Optional[Literal["completed", "failed", "in_progress", "incomplete"]] = None
    """The status of the response generation.

    One of `completed`, `failed`, `in_progress`, or `incomplete`.
    """

    text: Optional[Text] = None
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](/docs/guides/text)
    - [Structured Outputs](/docs/guides/structured-outputs)
    """

    truncation: Optional[Literal["auto", "disabled"]] = None
    """The truncation strategy to use for the model response.

    - `auto`: If the context of this response and previous ones exceeds the model's
      context window size, the model will truncate the response to fit the context
      window by dropping input items in the middle of the conversation.
    - `disabled` (default): If a model response will exceed the context window size
      for a model, the request will fail with a 400 error.
    """

    usage: Optional[Usage] = None
    """
    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used.
    """

    user: Optional[str] = None
    """
    A unique identifier representing your end-user, which can help OpenAI to monitor
    and detect abuse. [Learn more](/docs/guides/safety-best-practices#end-user-ids).
    """
