# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "RunCreateParams",
    "DataSource",
    "DataSourceCreateEvalJSONLRunDataSource",
    "DataSourceCreateEvalJSONLRunDataSourceSource",
    "DataSourceCreateEvalJSONLRunDataSourceSourceFileContent",
    "DataSourceCreateEvalJSONLRunDataSourceSourceFileContentContent",
    "DataSourceCreateEvalJSONLRunDataSourceSourceFileID",
    "DataSourceCreateEvalCompletionsRunDataSource",
    "DataSourceCreateEvalCompletionsRunDataSourceSource",
    "DataSourceCreateEvalCompletionsRunDataSourceSourceFileContent",
    "DataSourceCreateEvalCompletionsRunDataSourceSourceFileContentContent",
    "DataSourceCreateEvalCompletionsRunDataSourceSourceFileID",
    "DataSourceCreateEvalCompletionsRunDataSourceSourceStoredCompletions",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessages",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplate",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplate",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessage",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentList",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputText",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputImage",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputFile",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudio",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudioInputAudio",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItem",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContent",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputTextContent",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudio",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReference",
    "DataSourceCreateEvalCompletionsRunDataSourceSamplingParams",
    "DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormat",
    "DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatText",
    "DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatJsonSchema",
    "DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatJsonSchemaJsonSchema",
    "DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatJsonObject",
    "DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsTool",
    "DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsToolFunction",
    "DataSourceCreateEvalResponsesRunDataSource",
    "DataSourceCreateEvalResponsesRunDataSourceSource",
    "DataSourceCreateEvalResponsesRunDataSourceSourceFileContent",
    "DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent",
    "DataSourceCreateEvalResponsesRunDataSourceSourceFileID",
    "DataSourceCreateEvalResponsesRunDataSourceSourceResponses",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessages",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputTextContent",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudio",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParams",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsText",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormat",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormatText",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormatJsonSchema",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormatJsonObject",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTool",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFunction",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearch",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFilters",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersComparisonFilter",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersCompoundFilter",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersCompoundFilterFilter",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersCompoundFilterFilterComparisonFilter",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchRankingOptions",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolComputerUsePreview",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchTool",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchToolFilters",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchToolUserLocation",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcp",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpAllowedTools",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpAllowedToolsMcpToolFilter",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApproval",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilter",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterAlways",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterNever",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCodeInterpreter",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCodeInterpreterContainer",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCodeInterpreterContainerCodeInterpreterToolAuto",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolImageGeneration",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolImageGenerationInputImageMask",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolLocalShell",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustom",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustomFormat",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustomFormatText",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustomFormatGrammar",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchPreviewTool",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchPreviewToolUserLocation",
]


class RunCreateParams(TypedDict, total=False):
    data_source: Required[DataSource]
    """Details about the run's data source."""

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: str
    """The name of the run."""


class DataSourceCreateEvalJSONLRunDataSourceSourceFileContentContent(TypedDict, total=False):
    item: Required[Dict[str, object]]

    sample: Dict[str, object]


class DataSourceCreateEvalJSONLRunDataSourceSourceFileContent(TypedDict, total=False):
    content: Required[Iterable[DataSourceCreateEvalJSONLRunDataSourceSourceFileContentContent]]
    """The content of the jsonl file."""

    type: Required[Literal["file_content"]]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalJSONLRunDataSourceSourceFileID(TypedDict, total=False):
    id: Required[str]
    """The identifier of the file."""

    type: Required[Literal["file_id"]]
    """The type of jsonl source. Always `file_id`."""


DataSourceCreateEvalJSONLRunDataSourceSource: TypeAlias = Union[
    DataSourceCreateEvalJSONLRunDataSourceSourceFileContent, DataSourceCreateEvalJSONLRunDataSourceSourceFileID
]


class DataSourceCreateEvalJSONLRunDataSource(TypedDict, total=False):
    source: Required[DataSourceCreateEvalJSONLRunDataSourceSource]
    """Determines what populates the `item` namespace in the data source."""

    type: Required[Literal["jsonl"]]
    """The type of data source. Always `jsonl`."""


class DataSourceCreateEvalCompletionsRunDataSourceSourceFileContentContent(TypedDict, total=False):
    item: Required[Dict[str, object]]

    sample: Dict[str, object]


class DataSourceCreateEvalCompletionsRunDataSourceSourceFileContent(TypedDict, total=False):
    content: Required[Iterable[DataSourceCreateEvalCompletionsRunDataSourceSourceFileContentContent]]
    """The content of the jsonl file."""

    type: Required[Literal["file_content"]]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalCompletionsRunDataSourceSourceFileID(TypedDict, total=False):
    id: Required[str]
    """The identifier of the file."""

    type: Required[Literal["file_id"]]
    """The type of jsonl source. Always `file_id`."""


class DataSourceCreateEvalCompletionsRunDataSourceSourceStoredCompletions(TypedDict, total=False):
    type: Required[Literal["stored_completions"]]
    """The type of source. Always `stored_completions`."""

    created_after: Optional[int]
    """An optional Unix timestamp to filter items created after this time."""

    created_before: Optional[int]
    """An optional Unix timestamp to filter items created before this time."""

    limit: Optional[int]
    """An optional maximum number of items to return."""

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    model: Optional[str]
    """An optional model to filter by (e.g., 'gpt-4o')."""


DataSourceCreateEvalCompletionsRunDataSourceSource: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceSourceFileContent,
    DataSourceCreateEvalCompletionsRunDataSourceSourceFileID,
    DataSourceCreateEvalCompletionsRunDataSourceSourceStoredCompletions,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputText(
    TypedDict, total=False
):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputImage(
    TypedDict, total=False
):
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


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputFile(
    TypedDict, total=False
):
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


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudioInputAudio(
    TypedDict, total=False
):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudio(
    TypedDict, total=False
):
    input_audio: Required[
        DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudioInputAudio
    ]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentList: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputText,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputImage,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputFile,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudio,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessage(TypedDict, total=False):
    content: Required[
        Union[
            str,
            Iterable[
                DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentList
            ],
        ]
    ]
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


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputTextContent(
    TypedDict, total=False
):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText(
    TypedDict, total=False
):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage(
    TypedDict, total=False
):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio(
    TypedDict, total=False
):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudio(
    TypedDict, total=False
):
    input_audio: Required[
        DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio
    ]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContent: TypeAlias = Union[
    str,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputTextContent,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudio,
    Iterable[object],
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItem(TypedDict, total=False):
    content: Required[DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItemContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplate: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEasyInputMessage,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplateEvalItem,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplate(TypedDict, total=False):
    template: Required[Iterable[DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateTemplate]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the `item` namespace, ie {{item.name}}.
    """

    type: Required[Literal["template"]]
    """The type of input messages. Always `template`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReference(TypedDict, total=False):
    item_reference: Required[str]
    """A reference to a variable in the `item` namespace. Ie, "item.input_trajectory" """

    type: Required[Literal["item_reference"]]
    """The type of input messages. Always `item_reference`."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessages: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplate,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReference,
]


class DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatText(
    TypedDict, total=False
):
    type: Required[Literal["text"]]
    """The type of response format being defined. Always `text`."""


class DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatJsonSchemaJsonSchema(
    TypedDict, total=False
):
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
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
    """


class DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatJsonSchema(
    TypedDict, total=False
):
    json_schema: Required[
        DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatJsonSchemaJsonSchema
    ]
    """Structured Outputs configuration options, including a JSON Schema."""

    type: Required[Literal["json_schema"]]
    """The type of response format being defined. Always `json_schema`."""


class DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatJsonObject(
    TypedDict, total=False
):
    type: Required[Literal["json_object"]]
    """The type of response format being defined. Always `json_object`."""


DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormat: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatText,
    DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatJsonSchema,
    DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormatResponseFormatJsonObject,
]


class DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsToolFunction(TypedDict, total=False):
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

    See the [guide](https://platform.excai.com/docs/guides/function-calling) for
    examples, and the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.
    """

    strict: Optional[bool]
    """Whether to enable strict schema adherence when generating the function call.

    If set to true, the model will follow the exact schema defined in the
    `parameters` field. Only a subset of JSON Schema is supported when `strict` is
    `true`. Learn more about Structured Outputs in the
    [function calling guide](https://platform.excai.com/docs/guides/function-calling).
    """


class DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsTool(TypedDict, total=False):
    function: Required[DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsToolFunction]

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class DataSourceCreateEvalCompletionsRunDataSourceSamplingParams(TypedDict, total=False):
    max_completion_tokens: int
    """The maximum number of tokens in the generated output."""

    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]]
    """
    Constrains effort on reasoning for
    [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
    supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
    effort can result in faster responses and fewer tokens used on reasoning in a
    response.

    Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
    effort.
    """

    response_format: DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsResponseFormat
    """An object specifying the format that the model must output.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
    Outputs which ensures the model will match your supplied JSON schema. Learn more
    in the
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """

    seed: int
    """A seed value to initialize the randomness, during sampling."""

    temperature: float
    """A higher temperature increases randomness in the outputs."""

    tools: Iterable[DataSourceCreateEvalCompletionsRunDataSourceSamplingParamsTool]
    """A list of tools the model may call.

    Currently, only functions are supported as a tool. Use this to provide a list of
    functions the model may generate JSON inputs for. A max of 128 functions are
    supported.
    """

    top_p: float
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataSourceCreateEvalCompletionsRunDataSource(TypedDict, total=False):
    source: Required[DataSourceCreateEvalCompletionsRunDataSourceSource]
    """Determines what populates the `item` namespace in this run's data source."""

    type: Required[Literal["completions"]]
    """The type of run data source. Always `completions`."""

    input_messages: DataSourceCreateEvalCompletionsRunDataSourceInputMessages
    """Used when sampling from a model.

    Dictates the structure of the messages passed into the model. Can either be a
    reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template
    with variable references to the `item` namespace.
    """

    model: str
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: DataSourceCreateEvalCompletionsRunDataSourceSamplingParams


class DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent(TypedDict, total=False):
    item: Required[Dict[str, object]]

    sample: Dict[str, object]


class DataSourceCreateEvalResponsesRunDataSourceSourceFileContent(TypedDict, total=False):
    content: Required[Iterable[DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent]]
    """The content of the jsonl file."""

    type: Required[Literal["file_content"]]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalResponsesRunDataSourceSourceFileID(TypedDict, total=False):
    id: Required[str]
    """The identifier of the file."""

    type: Required[Literal["file_id"]]
    """The type of jsonl source. Always `file_id`."""


class DataSourceCreateEvalResponsesRunDataSourceSourceResponses(TypedDict, total=False):
    type: Required[Literal["responses"]]
    """The type of run data source. Always `responses`."""

    created_after: Optional[int]
    """Only include items created after this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    created_before: Optional[int]
    """Only include items created before this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    instructions_search: Optional[str]
    """Optional string to search the 'instructions' field.

    This is a query parameter used to select responses.
    """

    metadata: Optional[object]
    """Metadata filter for the responses.

    This is a query parameter used to select responses.
    """

    model: Optional[str]
    """The name of the model to find responses for.

    This is a query parameter used to select responses.
    """

    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]]
    """
    Constrains effort on reasoning for
    [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
    supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
    effort can result in faster responses and fewer tokens used on reasoning in a
    response.

    Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
    effort.
    """

    temperature: Optional[float]
    """Sampling temperature. This is a query parameter used to select responses."""

    tools: Optional[SequenceNotStr[str]]
    """List of tool names. This is a query parameter used to select responses."""

    top_p: Optional[float]
    """Nucleus sampling parameter. This is a query parameter used to select responses."""

    users: Optional[SequenceNotStr[str]]
    """List of user identifiers. This is a query parameter used to select responses."""


DataSourceCreateEvalResponsesRunDataSourceSource: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceSourceFileContent,
    DataSourceCreateEvalResponsesRunDataSourceSourceFileID,
    DataSourceCreateEvalResponsesRunDataSourceSourceResponses,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage(TypedDict, total=False):
    content: Required[str]
    """The content of the message."""

    role: Required[str]
    """The role of the message (e.g. "system", "assistant", "user")."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputTextContent(
    TypedDict, total=False
):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText(
    TypedDict, total=False
):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage(
    TypedDict, total=False
):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio(
    TypedDict, total=False
):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudio(
    TypedDict, total=False
):
    input_audio: Required[
        DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio
    ]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent: TypeAlias = Union[
    str,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputTextContent,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputAudio,
    Iterable[object],
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem(TypedDict, total=False):
    content: Required[DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate(TypedDict, total=False):
    template: Required[Iterable[DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the `item` namespace, ie {{item.name}}.
    """

    type: Required[Literal["template"]]
    """The type of input messages. Always `template`."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference(TypedDict, total=False):
    item_reference: Required[str]
    """A reference to a variable in the `item` namespace. Ie, "item.name" """

    type: Required[Literal["item_reference"]]
    """The type of input messages. Always `item_reference`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessages: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference,
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]
    """The type of response format being defined. Always `text`."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormatJsonSchema(TypedDict, total=False):
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


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormatJsonObject(TypedDict, total=False):
    type: Required[Literal["json_object"]]
    """The type of response format being defined. Always `json_object`."""


DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormat: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormatText,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormatJsonSchema,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormatJsonObject,
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsText(TypedDict, total=False):
    format: DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTextFormat
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


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFunction(TypedDict, total=False):
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


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersComparisonFilter(
    TypedDict, total=False
):
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


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersCompoundFilterFilterComparisonFilter(
    TypedDict, total=False
):
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


DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersCompoundFilterFilter: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersCompoundFilterFilterComparisonFilter,
    object,
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersCompoundFilter(
    TypedDict, total=False
):
    filters: Required[
        Iterable[DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersCompoundFilterFilter]
    ]
    """Array of filters to combine.

    Items can be `ComparisonFilter` or `CompoundFilter`.
    """

    type: Required[Literal["and", "or"]]
    """Type of operation: `and` or `or`."""


DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFilters: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersComparisonFilter,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFiltersCompoundFilter,
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchRankingOptions(TypedDict, total=False):
    ranker: Literal["auto", "default-2024-11-15"]
    """The ranker to use for the file search."""

    score_threshold: float
    """The score threshold for the file search, a number between 0 and 1.

    Numbers closer to 1 will attempt to return only the most relevant results, but
    may return fewer results.
    """


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearch(TypedDict, total=False):
    type: Required[Literal["file_search"]]
    """The type of the file search tool. Always `file_search`."""

    vector_store_ids: Required[SequenceNotStr[str]]
    """The IDs of the vector stores to search."""

    filters: Optional[DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchFilters]
    """A filter to apply."""

    max_num_results: int
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearchRankingOptions
    """Ranking options for search."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolComputerUsePreview(TypedDict, total=False):
    display_height: Required[int]
    """The height of the computer display."""

    display_width: Required[int]
    """The width of the computer display."""

    environment: Required[Literal["windows", "mac", "linux", "ubuntu", "browser"]]
    """The type of computer environment to control."""

    type: Required[Literal["computer_use_preview"]]
    """The type of the computer use tool. Always `computer_use_preview`."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchToolFilters(TypedDict, total=False):
    allowed_domains: Optional[SequenceNotStr[str]]
    """Allowed domains for the search.

    If not provided, all domains are allowed. Subdomains of the provided domains are
    allowed as well.

    Example: `["pubmed.ncbi.nlm.nih.gov"]`
    """


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchToolUserLocation(TypedDict, total=False):
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


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchTool(TypedDict, total=False):
    type: Required[Literal["web_search", "web_search_2025_08_26"]]
    """The type of the web search tool.

    One of `web_search` or `web_search_2025_08_26`.
    """

    filters: Optional[DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchToolFilters]
    """Filters for the search."""

    search_context_size: Literal["low", "medium", "high"]
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchToolUserLocation]
    """The approximate location of the user."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpAllowedToolsMcpToolFilter(TypedDict, total=False):
    read_only: bool
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: SequenceNotStr[str]
    """List of allowed tool names."""


DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpAllowedTools: TypeAlias = Union[
    SequenceNotStr[str], DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpAllowedToolsMcpToolFilter
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterAlways(
    TypedDict, total=False
):
    read_only: bool
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: SequenceNotStr[str]
    """List of allowed tool names."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterNever(
    TypedDict, total=False
):
    read_only: bool
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: SequenceNotStr[str]
    """List of allowed tool names."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilter(
    TypedDict, total=False
):
    always: DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterAlways
    """A filter object to specify which tools are allowed."""

    never: DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterNever
    """A filter object to specify which tools are allowed."""


DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApproval: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilter,
    Literal["always", "never"],
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcp(TypedDict, total=False):
    server_label: Required[str]
    """A label for this MCP server, used to identify it in tool calls."""

    type: Required[Literal["mcp"]]
    """The type of the MCP tool. Always `mcp`."""

    allowed_tools: Optional[DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpAllowedTools]
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

    require_approval: Optional[DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcpRequireApproval]
    """Specify which of the MCP server's tools require approval."""

    server_description: str
    """Optional description of the MCP server, used to provide more context."""

    server_url: str
    """The URL for the MCP server.

    One of `server_url` or `connector_id` must be provided.
    """


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCodeInterpreterContainerCodeInterpreterToolAuto(
    TypedDict, total=False
):
    type: Required[Literal["auto"]]
    """Always `auto`."""

    file_ids: SequenceNotStr[str]
    """An optional list of uploaded files to make available to your code."""


DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCodeInterpreterContainer: TypeAlias = Union[
    str, DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCodeInterpreterContainerCodeInterpreterToolAuto
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCodeInterpreter(TypedDict, total=False):
    container: Required[DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCodeInterpreterContainer]
    """The code interpreter container.

    Can be a container ID or an object that specifies uploaded file IDs to make
    available to your code.
    """

    type: Required[Literal["code_interpreter"]]
    """The type of the code interpreter tool. Always `code_interpreter`."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolImageGenerationInputImageMask(TypedDict, total=False):
    file_id: str
    """File ID for the mask image."""

    image_url: str
    """Base64-encoded mask image."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolImageGeneration(TypedDict, total=False):
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

    input_image_mask: DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolImageGenerationInputImageMask
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


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolLocalShell(TypedDict, total=False):
    type: Required[Literal["local_shell"]]
    """The type of the local shell tool. Always `local_shell`."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustomFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]
    """Unconstrained text format. Always `text`."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustomFormatGrammar(TypedDict, total=False):
    definition: Required[str]
    """The grammar definition."""

    syntax: Required[Literal["lark", "regex"]]
    """The syntax of the grammar definition. One of `lark` or `regex`."""

    type: Required[Literal["grammar"]]
    """Grammar format. Always `grammar`."""


DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustomFormat: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustomFormatText,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustomFormatGrammar,
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustom(TypedDict, total=False):
    name: Required[str]
    """The name of the custom tool, used to identify it in tool calls."""

    type: Required[Literal["custom"]]
    """The type of the custom tool. Always `custom`."""

    description: str
    """Optional description of the custom tool, used to provide more context."""

    format: DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustomFormat
    """The input format for the custom tool. Default is unconstrained text."""


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchPreviewToolUserLocation(
    TypedDict, total=False
):
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


class DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchPreviewTool(TypedDict, total=False):
    type: Required[Literal["web_search_preview", "web_search_preview_2025_03_11"]]
    """The type of the web search tool.

    One of `web_search_preview` or `web_search_preview_2025_03_11`.
    """

    search_context_size: Literal["low", "medium", "high"]
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[
        DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchPreviewToolUserLocation
    ]
    """The user's location."""


DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTool: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFunction,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolFileSearch,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolComputerUsePreview,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchTool,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolMcp,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCodeInterpreter,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolImageGeneration,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolLocalShell,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolCustom,
    DataSourceCreateEvalResponsesRunDataSourceSamplingParamsToolWebSearchPreviewTool,
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParams(TypedDict, total=False):
    max_completion_tokens: int
    """The maximum number of tokens in the generated output."""

    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]]
    """
    Constrains effort on reasoning for
    [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
    supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
    effort can result in faster responses and fewer tokens used on reasoning in a
    response.

    Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
    effort.
    """

    seed: int
    """A seed value to initialize the randomness, during sampling."""

    temperature: float
    """A higher temperature increases randomness in the outputs."""

    text: DataSourceCreateEvalResponsesRunDataSourceSamplingParamsText
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](https://platform.excai.com/docs/guides/text)
    - [Structured Outputs](https://platform.excai.com/docs/guides/structured-outputs)
    """

    tools: Iterable[DataSourceCreateEvalResponsesRunDataSourceSamplingParamsTool]
    """An array of tools the model may call while generating a response.

    You can specify which tool to use by setting the `tool_choice` parameter.

    The two categories of tools you can provide the model are:

    - **Built-in tools**: Tools that are provided by EXCai that extend the model's
      capabilities, like
      [web search](https://platform.excai.com/docs/guides/tools-web-search) or
      [file search](https://platform.excai.com/docs/guides/tools-file-search). Learn
      more about [built-in tools](https://platform.excai.com/docs/guides/tools).
    - **Function calls (custom tools)**: Functions that are defined by you, enabling
      the model to call your own code. Learn more about
      [function calling](https://platform.excai.com/docs/guides/function-calling).
    """

    top_p: float
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataSourceCreateEvalResponsesRunDataSource(TypedDict, total=False):
    source: Required[DataSourceCreateEvalResponsesRunDataSourceSource]
    """Determines what populates the `item` namespace in this run's data source."""

    type: Required[Literal["responses"]]
    """The type of run data source. Always `responses`."""

    input_messages: DataSourceCreateEvalResponsesRunDataSourceInputMessages
    """Used when sampling from a model.

    Dictates the structure of the messages passed into the model. Can either be a
    reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template
    with variable references to the `item` namespace.
    """

    model: str
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: DataSourceCreateEvalResponsesRunDataSourceSamplingParams


DataSource: TypeAlias = Union[
    DataSourceCreateEvalJSONLRunDataSource,
    DataSourceCreateEvalCompletionsRunDataSource,
    DataSourceCreateEvalResponsesRunDataSource,
]
