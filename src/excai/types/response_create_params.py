# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .reasoning_param import ReasoningParam
from .output_message_param import OutputMessageParam
from .shared_params.mcp_tool import McpTool
from .tool_choice_types_param import ToolChoiceTypesParam
from .function_tool_call_param import FunctionToolCallParam
from .tool_choice_custom_param import ToolChoiceCustomParam
from .shared_params.custom_tool import CustomTool
from .shared_params.input_audio import InputAudio
from .tool_choice_allowed_param import ToolChoiceAllowedParam
from .shared_params.function_tool import FunctionTool
from .shared_params.mcp_tool_call import McpToolCall
from .shared_params.image_gen_tool import ImageGenTool
from .shared_params.mcp_list_tools import McpListTools
from .shared_params.reasoning_item import ReasoningItem
from .shared_params.tool_choice_mcp import ToolChoiceMcp
from .shared_params.web_search_tool import WebSearchTool
from .evals.easy_input_message_param import EasyInputMessageParam
from .shared_params.custom_tool_call import CustomToolCall
from .shared_params.file_search_tool import FileSearchTool
from .shared_params.local_shell_tool import LocalShellTool
from .shared_params.computer_tool_call import ComputerToolCall
from .shared_params.input_file_content import InputFileContent
from .shared_params.input_text_content import InputTextContent
from .shared_params.image_gen_tool_call import ImageGenToolCall
from .shared_params.input_image_content import InputImageContent
from .shared_params.mcp_approval_request import McpApprovalRequest
from .shared_params.response_format_text import ResponseFormatText
from .shared_params.tool_choice_function import ToolChoiceFunction
from .shared_params.web_search_tool_call import WebSearchToolCall
from .shared_params.code_interpreter_tool import CodeInterpreterTool
from .shared_params.file_search_tool_call import FileSearchToolCall
from .shared_params.local_shell_tool_call import LocalShellToolCall
from .shared_params.web_search_preview_tool import WebSearchPreviewTool
from .shared_params.computer_screenshot_image import ComputerScreenshotImage
from .shared_params.computer_use_preview_tool import ComputerUsePreviewTool
from .shared_params.code_interpreter_tool_call import CodeInterpreterToolCall
from .shared_params.response_format_json_object import ResponseFormatJsonObject
from .shared_params.local_shell_tool_call_output import LocalShellToolCallOutput
from .conversations.custom_tool_call_output_param import CustomToolCallOutputParam
from .shared_params.text_response_format_json_schema import TextResponseFormatJsonSchema

__all__ = [
    "ResponseCreateParams",
    "Conversation",
    "ConversationConversationParam",
    "InputInputItemList",
    "InputInputItemListMessage",
    "InputInputItemListMessageContent",
    "InputInputItemListComputerCallOutput",
    "InputInputItemListComputerCallOutputAcknowledgedSafetyCheck",
    "InputInputItemListFunctionCallOutput",
    "InputInputItemListFunctionCallOutputOutputUnionMember1",
    "InputInputItemListFunctionCallOutputOutputUnionMember1InputText",
    "InputInputItemListFunctionCallOutputOutputUnionMember1InputImage",
    "InputInputItemListFunctionCallOutputOutputUnionMember1InputFile",
    "InputInputItemListMcpApprovalResponse",
    "InputInputItemListItemReference",
    "Prompt",
    "PromptVariables",
    "StreamOptions",
    "Text",
    "TextFormat",
    "ToolChoice",
    "Tool",
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

    reasoning: Optional[ReasoningParam]
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

InputInputItemListMessageContent: TypeAlias = Union[InputTextContent, InputImageContent, InputFileContent, InputAudio]


class InputInputItemListMessage(TypedDict, total=False):
    content: Required[Iterable[InputInputItemListMessageContent]]
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

    output: Required[ComputerScreenshotImage]
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


class InputInputItemListItemReference(TypedDict, total=False):
    id: Required[str]
    """The ID of the item to reference."""

    type: Optional[Literal["item_reference"]]
    """The type of item to reference. Always `item_reference`."""


InputInputItemList: TypeAlias = Union[
    EasyInputMessageParam,
    InputInputItemListMessage,
    OutputMessageParam,
    FileSearchToolCall,
    ComputerToolCall,
    InputInputItemListComputerCallOutput,
    WebSearchToolCall,
    FunctionToolCallParam,
    InputInputItemListFunctionCallOutput,
    ReasoningItem,
    ImageGenToolCall,
    CodeInterpreterToolCall,
    LocalShellToolCall,
    LocalShellToolCallOutput,
    McpListTools,
    McpApprovalRequest,
    InputInputItemListMcpApprovalResponse,
    McpToolCall,
    CustomToolCallOutputParam,
    CustomToolCall,
    InputInputItemListItemReference,
]

PromptVariables: TypeAlias = Union[str, InputTextContent, InputImageContent, InputFileContent]


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


TextFormat: TypeAlias = Union[ResponseFormatText, TextResponseFormatJsonSchema, ResponseFormatJsonObject]


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


ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"],
    ToolChoiceAllowedParam,
    ToolChoiceTypesParam,
    ToolChoiceFunction,
    ToolChoiceMcp,
    ToolChoiceCustomParam,
]

Tool: TypeAlias = Union[
    FunctionTool,
    FileSearchTool,
    ComputerUsePreviewTool,
    WebSearchTool,
    McpTool,
    CodeInterpreterTool,
    ImageGenTool,
    LocalShellTool,
    CustomTool,
    WebSearchPreviewTool,
]
