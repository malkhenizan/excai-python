# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "RunCreateParams",
    "ResponseFormat",
    "ResponseFormatResponseFormatText",
    "ResponseFormatResponseFormatJsonObject",
    "ResponseFormatResponseFormatJsonSchema",
    "ResponseFormatResponseFormatJsonSchemaJsonSchema",
    "Thread",
    "ThreadMessage",
    "ThreadMessageContentArrayOfContentPart",
    "ThreadMessageContentArrayOfContentPartMessageContentImageFileObject",
    "ThreadMessageContentArrayOfContentPartMessageContentImageFileObjectImageFile",
    "ThreadMessageContentArrayOfContentPartMessageContentImageURLObject",
    "ThreadMessageContentArrayOfContentPartMessageContentImageURLObjectImageURL",
    "ThreadMessageContentArrayOfContentPartMessageRequestContentTextObject",
    "ThreadMessageAttachment",
    "ThreadMessageAttachmentTool",
    "ThreadMessageAttachmentToolAssistantToolsCode",
    "ThreadMessageAttachmentToolAssistantToolsFileSearchTypeOnly",
    "ThreadToolResources",
    "ThreadToolResourcesCodeInterpreter",
    "ThreadToolResourcesFileSearch",
    "ThreadToolResourcesFileSearchVectorStore",
    "ThreadToolResourcesFileSearchVectorStoreChunkingStrategy",
    "ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAutoChunkingStrategy",
    "ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategy",
    "ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategyStatic",
    "ToolChoice",
    "ToolChoiceAssistantsNamedToolChoice",
    "ToolChoiceAssistantsNamedToolChoiceFunction",
    "ToolResources",
    "ToolResourcesCodeInterpreter",
    "ToolResourcesFileSearch",
    "Tool",
    "ToolAssistantToolsCode",
    "ToolAssistantToolsFileSearch",
    "ToolAssistantToolsFileSearchFileSearch",
    "ToolAssistantToolsFileSearchFileSearchRankingOptions",
    "ToolAssistantToolsFunction",
    "ToolAssistantToolsFunctionFunction",
    "TruncationStrategy",
]


class RunCreateParams(TypedDict, total=False):
    assistant_id: Required[str]
    """
    The ID of the [assistant](/docs/api-reference/assistants) to use to execute this
    run.
    """

    instructions: Optional[str]
    """Override the default system message of the assistant.

    This is useful for modifying the behavior on a per-run basis.
    """

    max_completion_tokens: Optional[int]
    """
    The maximum number of completion tokens that may be used over the course of the
    run. The run will make a best effort to use only the number of completion tokens
    specified, across multiple turns of the run. If the run exceeds the number of
    completion tokens specified, the run will end with status `incomplete`. See
    `incomplete_details` for more info.
    """

    max_prompt_tokens: Optional[int]
    """The maximum number of prompt tokens that may be used over the course of the run.

    The run will make a best effort to use only the number of prompt tokens
    specified, across multiple turns of the run. If the run exceeds the number of
    prompt tokens specified, the run will end with status `incomplete`. See
    `incomplete_details` for more info.
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    model: Union[
        str,
        Literal[
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "gpt-4.1-2025-04-14",
            "gpt-4.1-mini-2025-04-14",
            "gpt-4.1-nano-2025-04-14",
            "gpt-4o",
            "gpt-4o-2024-11-20",
            "gpt-4o-2024-08-06",
            "gpt-4o-2024-05-13",
            "gpt-4o-mini",
            "gpt-4o-mini-2024-07-18",
            "gpt-4.5-preview",
            "gpt-4.5-preview-2025-02-27",
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
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-1106",
            "gpt-3.5-turbo-0125",
            "gpt-3.5-turbo-16k-0613",
        ],
        None,
    ]
    """The ID of the [Model](/docs/api-reference/models) to be used to execute this
    run.

    If a value is provided here, it will override the model associated with the
    assistant. If not, the model associated with the assistant will be used.
    """

    parallel_tool_calls: bool
    """
    Whether to enable
    [parallel function calling](/docs/guides/function-calling#configuring-parallel-function-calling)
    during tool use.
    """

    response_format: Optional[ResponseFormat]
    """Specifies the format that the model must output.

    Compatible with [GPT-4o](/docs/models#gpt-4o),
    [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models
    since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
    Outputs which ensures the model will match your supplied JSON schema. Learn more
    in the [Structured Outputs guide](/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
    message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to
    produce JSON yourself via a system or user message. Without this, the model may
    generate an unending stream of whitespace until the generation reaches the token
    limit, resulting in a long-running and seemingly "stuck" request. Also note that
    the message content may be partially cut off if `finish_reason="length"`, which
    indicates the generation exceeded `max_tokens` or the conversation exceeded the
    max context length.
    """

    stream: Optional[bool]
    """
    If `true`, returns a stream of events that happen during the Run as server-sent
    events, terminating when the Run enters a terminal state with a `data: [DONE]`
    message.
    """

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic.
    """

    thread: Thread
    """Options to create a new thread.

    If no thread is provided when running a request, an empty thread will be
    created.
    """

    tool_choice: Optional[ToolChoice]
    """
    Controls which (if any) tool is called by the model. `none` means the model will
    not call any tools and instead generates a message. `auto` is the default value
    and means the model can pick between generating a message or calling one or more
    tools. `required` means the model must call one or more tools before responding
    to the user. Specifying a particular tool like `{"type": "file_search"}` or
    `{"type": "function", "function": {"name": "my_function"}}` forces the model to
    call that tool.
    """

    tool_resources: Optional[ToolResources]
    """A set of resources that are used by the assistant's tools.

    The resources are specific to the type of tool. For example, the
    `code_interpreter` tool requires a list of file IDs, while the `file_search`
    tool requires a list of vector store IDs.
    """

    tools: Optional[Iterable[Tool]]
    """Override the tools the assistant can use for this run.

    This is useful for modifying the behavior on a per-run basis.
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.
    """

    truncation_strategy: Optional[TruncationStrategy]
    """Controls for how a thread will be truncated prior to the run.

    Use this to control the intial context window of the run.
    """


class ResponseFormatResponseFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]
    """The type of response format being defined. Always `text`."""


class ResponseFormatResponseFormatJsonObject(TypedDict, total=False):
    type: Required[Literal["json_object"]]
    """The type of response format being defined. Always `json_object`."""


class ResponseFormatResponseFormatJsonSchemaJsonSchema(TypedDict, total=False):
    name: Required[str]
    """The name of the response format.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the response format is for, used by the model to determine
    how to respond in the format.
    """

    schema: Dict[str, object]
    """
    The schema for the response format, described as a JSON Schema object. Learn how
    to build JSON schemas [here](https://json-schema.org/).
    """

    strict: Optional[bool]
    """
    Whether to enable strict schema adherence when generating the output. If set to
    true, the model will always follow the exact schema defined in the `schema`
    field. Only a subset of JSON Schema is supported when `strict` is `true`. To
    learn more, read the
    [Structured Outputs guide](/docs/guides/structured-outputs).
    """


class ResponseFormatResponseFormatJsonSchema(TypedDict, total=False):
    json_schema: Required[ResponseFormatResponseFormatJsonSchemaJsonSchema]
    """Structured Outputs configuration options, including a JSON Schema."""

    type: Required[Literal["json_schema"]]
    """The type of response format being defined. Always `json_schema`."""


ResponseFormat: TypeAlias = Union[
    Literal["auto"],
    ResponseFormatResponseFormatText,
    ResponseFormatResponseFormatJsonObject,
    ResponseFormatResponseFormatJsonSchema,
]


class ThreadMessageContentArrayOfContentPartMessageContentImageFileObjectImageFile(TypedDict, total=False):
    file_id: Required[str]
    """The [File](/docs/api-reference/files) ID of the image in the message content.

    Set `purpose="vision"` when uploading the File if you need to later display the
    file content.
    """

    detail: Literal["auto", "low", "high"]
    """Specifies the detail level of the image if specified by the user.

    `low` uses fewer tokens, you can opt in to high resolution using `high`.
    """


class ThreadMessageContentArrayOfContentPartMessageContentImageFileObject(TypedDict, total=False):
    image_file: Required[ThreadMessageContentArrayOfContentPartMessageContentImageFileObjectImageFile]

    type: Required[Literal["image_file"]]
    """Always `image_file`."""


class ThreadMessageContentArrayOfContentPartMessageContentImageURLObjectImageURL(TypedDict, total=False):
    url: Required[str]
    """
    The external URL of the image, must be a supported image types: jpeg, jpg, png,
    gif, webp.
    """

    detail: Literal["auto", "low", "high"]
    """Specifies the detail level of the image.

    `low` uses fewer tokens, you can opt in to high resolution using `high`. Default
    value is `auto`
    """


class ThreadMessageContentArrayOfContentPartMessageContentImageURLObject(TypedDict, total=False):
    image_url: Required[ThreadMessageContentArrayOfContentPartMessageContentImageURLObjectImageURL]

    type: Required[Literal["image_url"]]
    """The type of the content part."""


class ThreadMessageContentArrayOfContentPartMessageRequestContentTextObject(TypedDict, total=False):
    text: Required[str]
    """Text content to be sent to the model"""

    type: Required[Literal["text"]]
    """Always `text`."""


ThreadMessageContentArrayOfContentPart: TypeAlias = Union[
    ThreadMessageContentArrayOfContentPartMessageContentImageFileObject,
    ThreadMessageContentArrayOfContentPartMessageContentImageURLObject,
    ThreadMessageContentArrayOfContentPartMessageRequestContentTextObject,
]


class ThreadMessageAttachmentToolAssistantToolsCode(TypedDict, total=False):
    type: Required[Literal["code_interpreter"]]
    """The type of tool being defined: `code_interpreter`"""


class ThreadMessageAttachmentToolAssistantToolsFileSearchTypeOnly(TypedDict, total=False):
    type: Required[Literal["file_search"]]
    """The type of tool being defined: `file_search`"""


ThreadMessageAttachmentTool: TypeAlias = Union[
    ThreadMessageAttachmentToolAssistantToolsCode, ThreadMessageAttachmentToolAssistantToolsFileSearchTypeOnly
]


class ThreadMessageAttachment(TypedDict, total=False):
    file_id: str
    """The ID of the file to attach to the message."""

    tools: Iterable[ThreadMessageAttachmentTool]
    """The tools to add this file to."""


class ThreadMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[ThreadMessageContentArrayOfContentPart]]]
    """The text contents of the message."""

    role: Required[Literal["user", "assistant"]]
    """The role of the entity that is creating the message. Allowed values include:

    - `user`: Indicates the message is sent by an actual user and should be used in
      most cases to represent user-generated messages.
    - `assistant`: Indicates the message is generated by the assistant. Use this
      value to insert messages from the assistant into the conversation.
    """

    attachments: Optional[Iterable[ThreadMessageAttachment]]
    """A list of files attached to the message, and the tools they should be added to."""

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """


class ThreadToolResourcesCodeInterpreter(TypedDict, total=False):
    file_ids: SequenceNotStr[str]
    """
    A list of [file](/docs/api-reference/files) IDs made available to the
    `code_interpreter` tool. There can be a maximum of 20 files associated with the
    tool.
    """


class ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAutoChunkingStrategy(TypedDict, total=False):
    type: Required[Literal["auto"]]
    """Always `auto`."""


class ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategyStatic(TypedDict, total=False):
    chunk_overlap_tokens: Required[int]
    """The number of tokens that overlap between chunks. The default value is `400`.

    Note that the overlap must not exceed half of `max_chunk_size_tokens`.
    """

    max_chunk_size_tokens: Required[int]
    """The maximum number of tokens in each chunk.

    The default value is `800`. The minimum value is `100` and the maximum value is
    `4096`.
    """


class ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategy(TypedDict, total=False):
    static: Required[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategyStatic]

    type: Required[Literal["static"]]
    """Always `static`."""


ThreadToolResourcesFileSearchVectorStoreChunkingStrategy: TypeAlias = Union[
    ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAutoChunkingStrategy,
    ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticChunkingStrategy,
]


class ThreadToolResourcesFileSearchVectorStore(TypedDict, total=False):
    chunking_strategy: ThreadToolResourcesFileSearchVectorStoreChunkingStrategy
    """The chunking strategy used to chunk the file(s).

    If not set, will use the `auto` strategy.
    """

    file_ids: SequenceNotStr[str]
    """A list of [file](/docs/api-reference/files) IDs to add to the vector store.

    There can be a maximum of 10000 files in a vector store.
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """


class ThreadToolResourcesFileSearch(TypedDict, total=False):
    vector_store_ids: SequenceNotStr[str]
    """
    The [vector store](/docs/api-reference/vector-stores/object) attached to this
    thread. There can be a maximum of 1 vector store attached to the thread.
    """

    vector_stores: Iterable[ThreadToolResourcesFileSearchVectorStore]
    """
    A helper to create a [vector store](/docs/api-reference/vector-stores/object)
    with file_ids and attach it to this thread. There can be a maximum of 1 vector
    store attached to the thread.
    """


class ThreadToolResources(TypedDict, total=False):
    code_interpreter: ThreadToolResourcesCodeInterpreter

    file_search: ThreadToolResourcesFileSearch


class Thread(TypedDict, total=False):
    messages: Iterable[ThreadMessage]
    """A list of [messages](/docs/api-reference/messages) to start the thread with."""

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    tool_resources: Optional[ThreadToolResources]
    """
    A set of resources that are made available to the assistant's tools in this
    thread. The resources are specific to the type of tool. For example, the
    `code_interpreter` tool requires a list of file IDs, while the `file_search`
    tool requires a list of vector store IDs.
    """


class ToolChoiceAssistantsNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""


class ToolChoiceAssistantsNamedToolChoice(TypedDict, total=False):
    type: Required[Literal["function", "code_interpreter", "file_search"]]
    """The type of the tool. If type is `function`, the function name must be set"""

    function: ToolChoiceAssistantsNamedToolChoiceFunction


ToolChoice: TypeAlias = Union[Literal["none", "auto", "required"], ToolChoiceAssistantsNamedToolChoice]


class ToolResourcesCodeInterpreter(TypedDict, total=False):
    file_ids: SequenceNotStr[str]
    """
    A list of [file](/docs/api-reference/files) IDs made available to the
    `code_interpreter` tool. There can be a maximum of 20 files associated with the
    tool.
    """


class ToolResourcesFileSearch(TypedDict, total=False):
    vector_store_ids: SequenceNotStr[str]
    """
    The ID of the [vector store](/docs/api-reference/vector-stores/object) attached
    to this assistant. There can be a maximum of 1 vector store attached to the
    assistant.
    """


class ToolResources(TypedDict, total=False):
    code_interpreter: ToolResourcesCodeInterpreter

    file_search: ToolResourcesFileSearch


class ToolAssistantToolsCode(TypedDict, total=False):
    type: Required[Literal["code_interpreter"]]
    """The type of tool being defined: `code_interpreter`"""


class ToolAssistantToolsFileSearchFileSearchRankingOptions(TypedDict, total=False):
    score_threshold: Required[float]
    """The score threshold for the file search.

    All values must be a floating point number between 0 and 1.
    """

    ranker: Literal["auto", "default_2024_08_21"]
    """The ranker to use for the file search.

    If not specified will use the `auto` ranker.
    """


class ToolAssistantToolsFileSearchFileSearch(TypedDict, total=False):
    max_num_results: int
    """The maximum number of results the file search tool should output.

    The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number
    should be between 1 and 50 inclusive.

    Note that the file search tool may output fewer than `max_num_results` results.
    See the
    [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings)
    for more information.
    """

    ranking_options: ToolAssistantToolsFileSearchFileSearchRankingOptions
    """The ranking options for the file search.

    If not specified, the file search tool will use the `auto` ranker and a
    score_threshold of 0.

    See the
    [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings)
    for more information.
    """


class ToolAssistantToolsFileSearch(TypedDict, total=False):
    type: Required[Literal["file_search"]]
    """The type of tool being defined: `file_search`"""

    file_search: ToolAssistantToolsFileSearchFileSearch
    """Overrides for the file search tool."""


class ToolAssistantToolsFunctionFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Dict[str, object]
    """The parameters the functions accepts, described as a JSON Schema object.

    See the [guide](/docs/guides/function-calling) for examples, and the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.
    """

    strict: Optional[bool]
    """Whether to enable strict schema adherence when generating the function call.

    If set to true, the model will follow the exact schema defined in the
    `parameters` field. Only a subset of JSON Schema is supported when `strict` is
    `true`. Learn more about Structured Outputs in the
    [function calling guide](docs/guides/function-calling).
    """


class ToolAssistantToolsFunction(TypedDict, total=False):
    function: Required[ToolAssistantToolsFunctionFunction]

    type: Required[Literal["function"]]
    """The type of tool being defined: `function`"""


Tool: TypeAlias = Union[ToolAssistantToolsCode, ToolAssistantToolsFileSearch, ToolAssistantToolsFunction]


class TruncationStrategy(TypedDict, total=False):
    type: Required[Literal["auto", "last_messages"]]
    """The truncation strategy to use for the thread.

    The default is `auto`. If set to `last_messages`, the thread will be truncated
    to the n most recent messages in the thread. When set to `auto`, messages in the
    middle of the thread will be dropped to fit the context length of the model,
    `max_prompt_tokens`.
    """

    last_messages: Optional[int]
    """
    The number of most recent messages from the thread when constructing the context
    for the run.
    """
