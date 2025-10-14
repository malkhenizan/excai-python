# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .reasoning import Reasoning
from .conversation_2 import Conversation2
from .output_message import OutputMessage
from .response_usage import ResponseUsage
from .shared.mcp_tool import McpTool
from .tool_choice_types import ToolChoiceTypes
from .function_tool_call import FunctionToolCall
from .shared.custom_tool import CustomTool
from .shared.input_audio import InputAudio
from .tool_choice_custom import ToolChoiceCustom
from .tool_choice_allowed import ToolChoiceAllowed
from .shared.function_tool import FunctionTool
from .shared.mcp_tool_call import McpToolCall
from .shared.image_gen_tool import ImageGenTool
from .shared.mcp_list_tools import McpListTools
from .shared.reasoning_item import ReasoningItem
from .shared.tool_choice_mcp import ToolChoiceMcp
from .shared.web_search_tool import WebSearchTool
from .shared.custom_tool_call import CustomToolCall
from .shared.file_search_tool import FileSearchTool
from .shared.local_shell_tool import LocalShellTool
from .evals.easy_input_message import EasyInputMessage
from .shared.computer_tool_call import ComputerToolCall
from .shared.input_file_content import InputFileContent
from .shared.input_text_content import InputTextContent
from .shared.image_gen_tool_call import ImageGenToolCall
from .shared.input_image_content import InputImageContent
from .shared.mcp_approval_request import McpApprovalRequest
from .shared.response_format_text import ResponseFormatText
from .shared.tool_choice_function import ToolChoiceFunction
from .shared.web_search_tool_call import WebSearchToolCall
from .shared.code_interpreter_tool import CodeInterpreterTool
from .shared.file_search_tool_call import FileSearchToolCall
from .shared.local_shell_tool_call import LocalShellToolCall
from .shared.web_search_preview_tool import WebSearchPreviewTool
from .shared.computer_screenshot_image import ComputerScreenshotImage
from .shared.computer_use_preview_tool import ComputerUsePreviewTool
from .shared.code_interpreter_tool_call import CodeInterpreterToolCall
from .shared.response_format_json_object import ResponseFormatJsonObject
from .shared.local_shell_tool_call_output import LocalShellToolCallOutput
from .conversations.custom_tool_call_output import CustomToolCallOutput
from .shared.text_response_format_json_schema import TextResponseFormatJsonSchema

__all__ = [
    "ResponseCreateResponse",
    "Error",
    "IncompleteDetails",
    "InstructionsInputItemList",
    "InstructionsInputItemListMessage",
    "InstructionsInputItemListMessageContent",
    "InstructionsInputItemListComputerCallOutput",
    "InstructionsInputItemListComputerCallOutputAcknowledgedSafetyCheck",
    "InstructionsInputItemListFunctionCallOutput",
    "InstructionsInputItemListFunctionCallOutputOutputUnionMember1",
    "InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputText",
    "InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputImage",
    "InstructionsInputItemListFunctionCallOutputOutputUnionMember1InputFile",
    "InstructionsInputItemListMcpApprovalResponse",
    "InstructionsInputItemListItemReference",
    "Output",
    "ToolChoice",
    "Tool",
    "Prompt",
    "PromptVariables",
    "Text",
    "TextFormat",
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


InstructionsInputItemListMessageContent: TypeAlias = Annotated[
    Union[InputTextContent, InputImageContent, InputFileContent, InputAudio], PropertyInfo(discriminator="type")
]


class InstructionsInputItemListMessage(BaseModel):
    content: List[InstructionsInputItemListMessageContent]
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

    output: ComputerScreenshotImage
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


class InstructionsInputItemListItemReference(BaseModel):
    id: str
    """The ID of the item to reference."""

    type: Optional[Literal["item_reference"]] = None
    """The type of item to reference. Always `item_reference`."""


InstructionsInputItemList: TypeAlias = Annotated[
    Union[
        EasyInputMessage,
        InstructionsInputItemListMessage,
        OutputMessage,
        FileSearchToolCall,
        ComputerToolCall,
        InstructionsInputItemListComputerCallOutput,
        WebSearchToolCall,
        FunctionToolCall,
        InstructionsInputItemListFunctionCallOutput,
        ReasoningItem,
        ImageGenToolCall,
        CodeInterpreterToolCall,
        LocalShellToolCall,
        LocalShellToolCallOutput,
        McpListTools,
        McpApprovalRequest,
        InstructionsInputItemListMcpApprovalResponse,
        McpToolCall,
        CustomToolCallOutput,
        CustomToolCall,
        InstructionsInputItemListItemReference,
    ],
    PropertyInfo(discriminator="type"),
]

Output: TypeAlias = Annotated[
    Union[
        OutputMessage,
        FileSearchToolCall,
        FunctionToolCall,
        WebSearchToolCall,
        ComputerToolCall,
        ReasoningItem,
        ImageGenToolCall,
        CodeInterpreterToolCall,
        LocalShellToolCall,
        McpToolCall,
        McpListTools,
        McpApprovalRequest,
        CustomToolCall,
    ],
    PropertyInfo(discriminator="type"),
]

ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"],
    ToolChoiceAllowed,
    ToolChoiceTypes,
    ToolChoiceFunction,
    ToolChoiceMcp,
    ToolChoiceCustom,
]

Tool: TypeAlias = Annotated[
    Union[
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
    ],
    PropertyInfo(discriminator="type"),
]

PromptVariables: TypeAlias = Union[str, InputTextContent, InputImageContent, InputFileContent]


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


TextFormat: TypeAlias = Annotated[
    Union[ResponseFormatText, TextResponseFormatJsonSchema, ResponseFormatJsonObject],
    PropertyInfo(discriminator="type"),
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

    conversation: Optional[Conversation2] = None
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

    usage: Optional[ResponseUsage] = None
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
