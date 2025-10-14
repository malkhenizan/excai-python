# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "RunCancelResponse",
    "DataSource",
    "DataSourceJSONL",
    "DataSourceJSONLSource",
    "DataSourceJSONLSourceFileContent",
    "DataSourceJSONLSourceFileContentContent",
    "DataSourceJSONLSourceFileID",
    "DataSourceCompletions",
    "DataSourceCompletionsSource",
    "DataSourceCompletionsSourceFileContent",
    "DataSourceCompletionsSourceFileContentContent",
    "DataSourceCompletionsSourceFileID",
    "DataSourceCompletionsSourceStoredCompletions",
    "DataSourceCompletionsInputMessages",
    "DataSourceCompletionsInputMessagesTemplate",
    "DataSourceCompletionsInputMessagesTemplateTemplate",
    "DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessage",
    "DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentList",
    "DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputText",
    "DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputImage",
    "DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputFile",
    "DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudio",
    "DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudioInputAudio",
    "DataSourceCompletionsInputMessagesTemplateTemplateEvalItem",
    "DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContent",
    "DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputTextContent",
    "DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentOutputText",
    "DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputImage",
    "DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputAudio",
    "DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio",
    "DataSourceCompletionsInputMessagesItemReference",
    "DataSourceCompletionsSamplingParams",
    "DataSourceCompletionsSamplingParamsResponseFormat",
    "DataSourceCompletionsSamplingParamsResponseFormatResponseFormatText",
    "DataSourceCompletionsSamplingParamsResponseFormatResponseFormatJsonSchema",
    "DataSourceCompletionsSamplingParamsResponseFormatResponseFormatJsonSchemaJsonSchema",
    "DataSourceCompletionsSamplingParamsResponseFormatResponseFormatJsonObject",
    "DataSourceCompletionsSamplingParamsTool",
    "DataSourceCompletionsSamplingParamsToolFunction",
    "DataSourceResponses",
    "DataSourceResponsesSource",
    "DataSourceResponsesSourceFileContent",
    "DataSourceResponsesSourceFileContentContent",
    "DataSourceResponsesSourceFileID",
    "DataSourceResponsesSourceResponses",
    "DataSourceResponsesInputMessages",
    "DataSourceResponsesInputMessagesTemplate",
    "DataSourceResponsesInputMessagesTemplateTemplate",
    "DataSourceResponsesInputMessagesTemplateTemplateChatMessage",
    "DataSourceResponsesInputMessagesTemplateTemplateEvalItem",
    "DataSourceResponsesInputMessagesTemplateTemplateEvalItemContent",
    "DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputTextContent",
    "DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentOutputText",
    "DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputImage",
    "DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputAudio",
    "DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio",
    "DataSourceResponsesInputMessagesItemReference",
    "DataSourceResponsesSamplingParams",
    "DataSourceResponsesSamplingParamsText",
    "DataSourceResponsesSamplingParamsTextFormat",
    "DataSourceResponsesSamplingParamsTextFormatText",
    "DataSourceResponsesSamplingParamsTextFormatJsonSchema",
    "DataSourceResponsesSamplingParamsTextFormatJsonObject",
    "DataSourceResponsesSamplingParamsTool",
    "DataSourceResponsesSamplingParamsToolFunction",
    "DataSourceResponsesSamplingParamsToolFileSearch",
    "DataSourceResponsesSamplingParamsToolFileSearchFilters",
    "DataSourceResponsesSamplingParamsToolFileSearchFiltersComparisonFilter",
    "DataSourceResponsesSamplingParamsToolFileSearchFiltersCompoundFilter",
    "DataSourceResponsesSamplingParamsToolFileSearchFiltersCompoundFilterFilter",
    "DataSourceResponsesSamplingParamsToolFileSearchFiltersCompoundFilterFilterComparisonFilter",
    "DataSourceResponsesSamplingParamsToolFileSearchRankingOptions",
    "DataSourceResponsesSamplingParamsToolComputerUsePreview",
    "DataSourceResponsesSamplingParamsToolWebSearchTool",
    "DataSourceResponsesSamplingParamsToolWebSearchToolFilters",
    "DataSourceResponsesSamplingParamsToolWebSearchToolUserLocation",
    "DataSourceResponsesSamplingParamsToolMcp",
    "DataSourceResponsesSamplingParamsToolMcpAllowedTools",
    "DataSourceResponsesSamplingParamsToolMcpAllowedToolsMcpToolFilter",
    "DataSourceResponsesSamplingParamsToolMcpRequireApproval",
    "DataSourceResponsesSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilter",
    "DataSourceResponsesSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterAlways",
    "DataSourceResponsesSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterNever",
    "DataSourceResponsesSamplingParamsToolCodeInterpreter",
    "DataSourceResponsesSamplingParamsToolCodeInterpreterContainer",
    "DataSourceResponsesSamplingParamsToolCodeInterpreterContainerCodeInterpreterToolAuto",
    "DataSourceResponsesSamplingParamsToolImageGeneration",
    "DataSourceResponsesSamplingParamsToolImageGenerationInputImageMask",
    "DataSourceResponsesSamplingParamsToolLocalShell",
    "DataSourceResponsesSamplingParamsToolCustom",
    "DataSourceResponsesSamplingParamsToolCustomFormat",
    "DataSourceResponsesSamplingParamsToolCustomFormatText",
    "DataSourceResponsesSamplingParamsToolCustomFormatGrammar",
    "DataSourceResponsesSamplingParamsToolWebSearchPreviewTool",
    "DataSourceResponsesSamplingParamsToolWebSearchPreviewToolUserLocation",
    "Error",
    "PerModelUsage",
    "PerTestingCriteriaResult",
    "ResultCounts",
]


class DataSourceJSONLSourceFileContentContent(BaseModel):
    item: Dict[str, object]

    sample: Optional[Dict[str, object]] = None


class DataSourceJSONLSourceFileContent(BaseModel):
    content: List[DataSourceJSONLSourceFileContentContent]
    """The content of the jsonl file."""

    type: Literal["file_content"]
    """The type of jsonl source. Always `file_content`."""


class DataSourceJSONLSourceFileID(BaseModel):
    id: str
    """The identifier of the file."""

    type: Literal["file_id"]
    """The type of jsonl source. Always `file_id`."""


DataSourceJSONLSource: TypeAlias = Annotated[
    Union[DataSourceJSONLSourceFileContent, DataSourceJSONLSourceFileID], PropertyInfo(discriminator="type")
]


class DataSourceJSONL(BaseModel):
    source: DataSourceJSONLSource
    """Determines what populates the `item` namespace in the data source."""

    type: Literal["jsonl"]
    """The type of data source. Always `jsonl`."""


class DataSourceCompletionsSourceFileContentContent(BaseModel):
    item: Dict[str, object]

    sample: Optional[Dict[str, object]] = None


class DataSourceCompletionsSourceFileContent(BaseModel):
    content: List[DataSourceCompletionsSourceFileContentContent]
    """The content of the jsonl file."""

    type: Literal["file_content"]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCompletionsSourceFileID(BaseModel):
    id: str
    """The identifier of the file."""

    type: Literal["file_id"]
    """The type of jsonl source. Always `file_id`."""


class DataSourceCompletionsSourceStoredCompletions(BaseModel):
    type: Literal["stored_completions"]
    """The type of source. Always `stored_completions`."""

    created_after: Optional[int] = None
    """An optional Unix timestamp to filter items created after this time."""

    created_before: Optional[int] = None
    """An optional Unix timestamp to filter items created before this time."""

    limit: Optional[int] = None
    """An optional maximum number of items to return."""

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    model: Optional[str] = None
    """An optional model to filter by (e.g., 'gpt-4o')."""


DataSourceCompletionsSource: TypeAlias = Annotated[
    Union[
        DataSourceCompletionsSourceFileContent,
        DataSourceCompletionsSourceFileID,
        DataSourceCompletionsSourceStoredCompletions,
    ],
    PropertyInfo(discriminator="type"),
]


class DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputText(
    BaseModel
):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputImage(
    BaseModel
):
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


class DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputFile(
    BaseModel
):
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


class DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudioInputAudio(
    BaseModel
):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudio(
    BaseModel
):
    input_audio: DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentList: TypeAlias = Annotated[
    Union[
        DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputText,
        DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputImage,
        DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputFile,
        DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentListInputAudio,
    ],
    PropertyInfo(discriminator="type"),
]


class DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessage(BaseModel):
    content: Union[
        str, List[DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessageContentInputMessageContentList]
    ]
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


class DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputAudio(BaseModel):
    input_audio: DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContent: TypeAlias = Union[
    str,
    DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputTextContent,
    DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentOutputText,
    DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputImage,
    DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContentInputAudio,
    List[object],
]


class DataSourceCompletionsInputMessagesTemplateTemplateEvalItem(BaseModel):
    content: DataSourceCompletionsInputMessagesTemplateTemplateEvalItemContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


DataSourceCompletionsInputMessagesTemplateTemplate: TypeAlias = Union[
    DataSourceCompletionsInputMessagesTemplateTemplateEasyInputMessage,
    DataSourceCompletionsInputMessagesTemplateTemplateEvalItem,
]


class DataSourceCompletionsInputMessagesTemplate(BaseModel):
    template: List[DataSourceCompletionsInputMessagesTemplateTemplate]
    """A list of chat messages forming the prompt or context.

    May include variable references to the `item` namespace, ie {{item.name}}.
    """

    type: Literal["template"]
    """The type of input messages. Always `template`."""


class DataSourceCompletionsInputMessagesItemReference(BaseModel):
    item_reference: str
    """A reference to a variable in the `item` namespace. Ie, "item.input_trajectory" """

    type: Literal["item_reference"]
    """The type of input messages. Always `item_reference`."""


DataSourceCompletionsInputMessages: TypeAlias = Annotated[
    Union[DataSourceCompletionsInputMessagesTemplate, DataSourceCompletionsInputMessagesItemReference],
    PropertyInfo(discriminator="type"),
]


class DataSourceCompletionsSamplingParamsResponseFormatResponseFormatText(BaseModel):
    type: Literal["text"]
    """The type of response format being defined. Always `text`."""


class DataSourceCompletionsSamplingParamsResponseFormatResponseFormatJsonSchemaJsonSchema(BaseModel):
    name: str
    """The name of the response format.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: Optional[str] = None
    """
    A description of what the response format is for, used by the model to determine
    how to respond in the format.
    """

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)
    """
    The schema for the response format, described as a JSON Schema object. Learn how
    to build JSON schemas [here](https://json-schema.org/).
    """

    strict: Optional[bool] = None
    """
    Whether to enable strict schema adherence when generating the output. If set to
    true, the model will always follow the exact schema defined in the `schema`
    field. Only a subset of JSON Schema is supported when `strict` is `true`. To
    learn more, read the
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
    """


class DataSourceCompletionsSamplingParamsResponseFormatResponseFormatJsonSchema(BaseModel):
    json_schema: DataSourceCompletionsSamplingParamsResponseFormatResponseFormatJsonSchemaJsonSchema
    """Structured Outputs configuration options, including a JSON Schema."""

    type: Literal["json_schema"]
    """The type of response format being defined. Always `json_schema`."""


class DataSourceCompletionsSamplingParamsResponseFormatResponseFormatJsonObject(BaseModel):
    type: Literal["json_object"]
    """The type of response format being defined. Always `json_object`."""


DataSourceCompletionsSamplingParamsResponseFormat: TypeAlias = Union[
    DataSourceCompletionsSamplingParamsResponseFormatResponseFormatText,
    DataSourceCompletionsSamplingParamsResponseFormatResponseFormatJsonSchema,
    DataSourceCompletionsSamplingParamsResponseFormatResponseFormatJsonObject,
]


class DataSourceCompletionsSamplingParamsToolFunction(BaseModel):
    name: str
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: Optional[str] = None
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Optional[Dict[str, object]] = None
    """The parameters the functions accepts, described as a JSON Schema object.

    See the [guide](https://platform.excai.com/docs/guides/function-calling) for
    examples, and the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.
    """

    strict: Optional[bool] = None
    """Whether to enable strict schema adherence when generating the function call.

    If set to true, the model will follow the exact schema defined in the
    `parameters` field. Only a subset of JSON Schema is supported when `strict` is
    `true`. Learn more about Structured Outputs in the
    [function calling guide](https://platform.excai.com/docs/guides/function-calling).
    """


class DataSourceCompletionsSamplingParamsTool(BaseModel):
    function: DataSourceCompletionsSamplingParamsToolFunction

    type: Literal["function"]
    """The type of the tool. Currently, only `function` is supported."""


class DataSourceCompletionsSamplingParams(BaseModel):
    max_completion_tokens: Optional[int] = None
    """The maximum number of tokens in the generated output."""

    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] = None
    """
    Constrains effort on reasoning for
    [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
    supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
    effort can result in faster responses and fewer tokens used on reasoning in a
    response.

    Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
    effort.
    """

    response_format: Optional[DataSourceCompletionsSamplingParamsResponseFormat] = None
    """An object specifying the format that the model must output.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
    Outputs which ensures the model will match your supplied JSON schema. Learn more
    in the
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """

    seed: Optional[int] = None
    """A seed value to initialize the randomness, during sampling."""

    temperature: Optional[float] = None
    """A higher temperature increases randomness in the outputs."""

    tools: Optional[List[DataSourceCompletionsSamplingParamsTool]] = None
    """A list of tools the model may call.

    Currently, only functions are supported as a tool. Use this to provide a list of
    functions the model may generate JSON inputs for. A max of 128 functions are
    supported.
    """

    top_p: Optional[float] = None
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataSourceCompletions(BaseModel):
    source: DataSourceCompletionsSource
    """Determines what populates the `item` namespace in this run's data source."""

    type: Literal["completions"]
    """The type of run data source. Always `completions`."""

    input_messages: Optional[DataSourceCompletionsInputMessages] = None
    """Used when sampling from a model.

    Dictates the structure of the messages passed into the model. Can either be a
    reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template
    with variable references to the `item` namespace.
    """

    model: Optional[str] = None
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[DataSourceCompletionsSamplingParams] = None


class DataSourceResponsesSourceFileContentContent(BaseModel):
    item: Dict[str, object]

    sample: Optional[Dict[str, object]] = None


class DataSourceResponsesSourceFileContent(BaseModel):
    content: List[DataSourceResponsesSourceFileContentContent]
    """The content of the jsonl file."""

    type: Literal["file_content"]
    """The type of jsonl source. Always `file_content`."""


class DataSourceResponsesSourceFileID(BaseModel):
    id: str
    """The identifier of the file."""

    type: Literal["file_id"]
    """The type of jsonl source. Always `file_id`."""


class DataSourceResponsesSourceResponses(BaseModel):
    type: Literal["responses"]
    """The type of run data source. Always `responses`."""

    created_after: Optional[int] = None
    """Only include items created after this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    created_before: Optional[int] = None
    """Only include items created before this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    instructions_search: Optional[str] = None
    """Optional string to search the 'instructions' field.

    This is a query parameter used to select responses.
    """

    metadata: Optional[object] = None
    """Metadata filter for the responses.

    This is a query parameter used to select responses.
    """

    model: Optional[str] = None
    """The name of the model to find responses for.

    This is a query parameter used to select responses.
    """

    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] = None
    """
    Constrains effort on reasoning for
    [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
    supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
    effort can result in faster responses and fewer tokens used on reasoning in a
    response.

    Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
    effort.
    """

    temperature: Optional[float] = None
    """Sampling temperature. This is a query parameter used to select responses."""

    tools: Optional[List[str]] = None
    """List of tool names. This is a query parameter used to select responses."""

    top_p: Optional[float] = None
    """Nucleus sampling parameter. This is a query parameter used to select responses."""

    users: Optional[List[str]] = None
    """List of user identifiers. This is a query parameter used to select responses."""


DataSourceResponsesSource: TypeAlias = Annotated[
    Union[DataSourceResponsesSourceFileContent, DataSourceResponsesSourceFileID, DataSourceResponsesSourceResponses],
    PropertyInfo(discriminator="type"),
]


class DataSourceResponsesInputMessagesTemplateTemplateChatMessage(BaseModel):
    content: str
    """The content of the message."""

    role: str
    """The role of the message (e.g. "system", "assistant", "user")."""


class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputAudio(BaseModel):
    input_audio: DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


DataSourceResponsesInputMessagesTemplateTemplateEvalItemContent: TypeAlias = Union[
    str,
    DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputTextContent,
    DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentOutputText,
    DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputImage,
    DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputAudio,
    List[object],
]


class DataSourceResponsesInputMessagesTemplateTemplateEvalItem(BaseModel):
    content: DataSourceResponsesInputMessagesTemplateTemplateEvalItemContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


DataSourceResponsesInputMessagesTemplateTemplate: TypeAlias = Union[
    DataSourceResponsesInputMessagesTemplateTemplateChatMessage,
    DataSourceResponsesInputMessagesTemplateTemplateEvalItem,
]


class DataSourceResponsesInputMessagesTemplate(BaseModel):
    template: List[DataSourceResponsesInputMessagesTemplateTemplate]
    """A list of chat messages forming the prompt or context.

    May include variable references to the `item` namespace, ie {{item.name}}.
    """

    type: Literal["template"]
    """The type of input messages. Always `template`."""


class DataSourceResponsesInputMessagesItemReference(BaseModel):
    item_reference: str
    """A reference to a variable in the `item` namespace. Ie, "item.name" """

    type: Literal["item_reference"]
    """The type of input messages. Always `item_reference`."""


DataSourceResponsesInputMessages: TypeAlias = Annotated[
    Union[DataSourceResponsesInputMessagesTemplate, DataSourceResponsesInputMessagesItemReference],
    PropertyInfo(discriminator="type"),
]


class DataSourceResponsesSamplingParamsTextFormatText(BaseModel):
    type: Literal["text"]
    """The type of response format being defined. Always `text`."""


class DataSourceResponsesSamplingParamsTextFormatJsonSchema(BaseModel):
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


class DataSourceResponsesSamplingParamsTextFormatJsonObject(BaseModel):
    type: Literal["json_object"]
    """The type of response format being defined. Always `json_object`."""


DataSourceResponsesSamplingParamsTextFormat: TypeAlias = Annotated[
    Union[
        DataSourceResponsesSamplingParamsTextFormatText,
        DataSourceResponsesSamplingParamsTextFormatJsonSchema,
        DataSourceResponsesSamplingParamsTextFormatJsonObject,
    ],
    PropertyInfo(discriminator="type"),
]


class DataSourceResponsesSamplingParamsText(BaseModel):
    format: Optional[DataSourceResponsesSamplingParamsTextFormat] = None
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


class DataSourceResponsesSamplingParamsToolFunction(BaseModel):
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


class DataSourceResponsesSamplingParamsToolFileSearchFiltersComparisonFilter(BaseModel):
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


class DataSourceResponsesSamplingParamsToolFileSearchFiltersCompoundFilterFilterComparisonFilter(BaseModel):
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


DataSourceResponsesSamplingParamsToolFileSearchFiltersCompoundFilterFilter: TypeAlias = Union[
    DataSourceResponsesSamplingParamsToolFileSearchFiltersCompoundFilterFilterComparisonFilter, object
]


class DataSourceResponsesSamplingParamsToolFileSearchFiltersCompoundFilter(BaseModel):
    filters: List[DataSourceResponsesSamplingParamsToolFileSearchFiltersCompoundFilterFilter]
    """Array of filters to combine.

    Items can be `ComparisonFilter` or `CompoundFilter`.
    """

    type: Literal["and", "or"]
    """Type of operation: `and` or `or`."""


DataSourceResponsesSamplingParamsToolFileSearchFilters: TypeAlias = Union[
    DataSourceResponsesSamplingParamsToolFileSearchFiltersComparisonFilter,
    DataSourceResponsesSamplingParamsToolFileSearchFiltersCompoundFilter,
    None,
]


class DataSourceResponsesSamplingParamsToolFileSearchRankingOptions(BaseModel):
    ranker: Optional[Literal["auto", "default-2024-11-15"]] = None
    """The ranker to use for the file search."""

    score_threshold: Optional[float] = None
    """The score threshold for the file search, a number between 0 and 1.

    Numbers closer to 1 will attempt to return only the most relevant results, but
    may return fewer results.
    """


class DataSourceResponsesSamplingParamsToolFileSearch(BaseModel):
    type: Literal["file_search"]
    """The type of the file search tool. Always `file_search`."""

    vector_store_ids: List[str]
    """The IDs of the vector stores to search."""

    filters: Optional[DataSourceResponsesSamplingParamsToolFileSearchFilters] = None
    """A filter to apply."""

    max_num_results: Optional[int] = None
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: Optional[DataSourceResponsesSamplingParamsToolFileSearchRankingOptions] = None
    """Ranking options for search."""


class DataSourceResponsesSamplingParamsToolComputerUsePreview(BaseModel):
    display_height: int
    """The height of the computer display."""

    display_width: int
    """The width of the computer display."""

    environment: Literal["windows", "mac", "linux", "ubuntu", "browser"]
    """The type of computer environment to control."""

    type: Literal["computer_use_preview"]
    """The type of the computer use tool. Always `computer_use_preview`."""


class DataSourceResponsesSamplingParamsToolWebSearchToolFilters(BaseModel):
    allowed_domains: Optional[List[str]] = None
    """Allowed domains for the search.

    If not provided, all domains are allowed. Subdomains of the provided domains are
    allowed as well.

    Example: `["pubmed.ncbi.nlm.nih.gov"]`
    """


class DataSourceResponsesSamplingParamsToolWebSearchToolUserLocation(BaseModel):
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


class DataSourceResponsesSamplingParamsToolWebSearchTool(BaseModel):
    type: Literal["web_search", "web_search_2025_08_26"]
    """The type of the web search tool.

    One of `web_search` or `web_search_2025_08_26`.
    """

    filters: Optional[DataSourceResponsesSamplingParamsToolWebSearchToolFilters] = None
    """Filters for the search."""

    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[DataSourceResponsesSamplingParamsToolWebSearchToolUserLocation] = None
    """The approximate location of the user."""


class DataSourceResponsesSamplingParamsToolMcpAllowedToolsMcpToolFilter(BaseModel):
    read_only: Optional[bool] = None
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


DataSourceResponsesSamplingParamsToolMcpAllowedTools: TypeAlias = Union[
    List[str], DataSourceResponsesSamplingParamsToolMcpAllowedToolsMcpToolFilter, None
]


class DataSourceResponsesSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterAlways(BaseModel):
    read_only: Optional[bool] = None
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


class DataSourceResponsesSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterNever(BaseModel):
    read_only: Optional[bool] = None
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


class DataSourceResponsesSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilter(BaseModel):
    always: Optional[DataSourceResponsesSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterAlways] = None
    """A filter object to specify which tools are allowed."""

    never: Optional[DataSourceResponsesSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilterNever] = None
    """A filter object to specify which tools are allowed."""


DataSourceResponsesSamplingParamsToolMcpRequireApproval: TypeAlias = Union[
    DataSourceResponsesSamplingParamsToolMcpRequireApprovalMcpToolApprovalFilter, Literal["always", "never"], None
]


class DataSourceResponsesSamplingParamsToolMcp(BaseModel):
    server_label: str
    """A label for this MCP server, used to identify it in tool calls."""

    type: Literal["mcp"]
    """The type of the MCP tool. Always `mcp`."""

    allowed_tools: Optional[DataSourceResponsesSamplingParamsToolMcpAllowedTools] = None
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

    require_approval: Optional[DataSourceResponsesSamplingParamsToolMcpRequireApproval] = None
    """Specify which of the MCP server's tools require approval."""

    server_description: Optional[str] = None
    """Optional description of the MCP server, used to provide more context."""

    server_url: Optional[str] = None
    """The URL for the MCP server.

    One of `server_url` or `connector_id` must be provided.
    """


class DataSourceResponsesSamplingParamsToolCodeInterpreterContainerCodeInterpreterToolAuto(BaseModel):
    type: Literal["auto"]
    """Always `auto`."""

    file_ids: Optional[List[str]] = None
    """An optional list of uploaded files to make available to your code."""


DataSourceResponsesSamplingParamsToolCodeInterpreterContainer: TypeAlias = Union[
    str, DataSourceResponsesSamplingParamsToolCodeInterpreterContainerCodeInterpreterToolAuto
]


class DataSourceResponsesSamplingParamsToolCodeInterpreter(BaseModel):
    container: DataSourceResponsesSamplingParamsToolCodeInterpreterContainer
    """The code interpreter container.

    Can be a container ID or an object that specifies uploaded file IDs to make
    available to your code.
    """

    type: Literal["code_interpreter"]
    """The type of the code interpreter tool. Always `code_interpreter`."""


class DataSourceResponsesSamplingParamsToolImageGenerationInputImageMask(BaseModel):
    file_id: Optional[str] = None
    """File ID for the mask image."""

    image_url: Optional[str] = None
    """Base64-encoded mask image."""


class DataSourceResponsesSamplingParamsToolImageGeneration(BaseModel):
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

    input_image_mask: Optional[DataSourceResponsesSamplingParamsToolImageGenerationInputImageMask] = None
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


class DataSourceResponsesSamplingParamsToolLocalShell(BaseModel):
    type: Literal["local_shell"]
    """The type of the local shell tool. Always `local_shell`."""


class DataSourceResponsesSamplingParamsToolCustomFormatText(BaseModel):
    type: Literal["text"]
    """Unconstrained text format. Always `text`."""


class DataSourceResponsesSamplingParamsToolCustomFormatGrammar(BaseModel):
    definition: str
    """The grammar definition."""

    syntax: Literal["lark", "regex"]
    """The syntax of the grammar definition. One of `lark` or `regex`."""

    type: Literal["grammar"]
    """Grammar format. Always `grammar`."""


DataSourceResponsesSamplingParamsToolCustomFormat: TypeAlias = Annotated[
    Union[
        DataSourceResponsesSamplingParamsToolCustomFormatText, DataSourceResponsesSamplingParamsToolCustomFormatGrammar
    ],
    PropertyInfo(discriminator="type"),
]


class DataSourceResponsesSamplingParamsToolCustom(BaseModel):
    name: str
    """The name of the custom tool, used to identify it in tool calls."""

    type: Literal["custom"]
    """The type of the custom tool. Always `custom`."""

    description: Optional[str] = None
    """Optional description of the custom tool, used to provide more context."""

    format: Optional[DataSourceResponsesSamplingParamsToolCustomFormat] = None
    """The input format for the custom tool. Default is unconstrained text."""


class DataSourceResponsesSamplingParamsToolWebSearchPreviewToolUserLocation(BaseModel):
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


class DataSourceResponsesSamplingParamsToolWebSearchPreviewTool(BaseModel):
    type: Literal["web_search_preview", "web_search_preview_2025_03_11"]
    """The type of the web search tool.

    One of `web_search_preview` or `web_search_preview_2025_03_11`.
    """

    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[DataSourceResponsesSamplingParamsToolWebSearchPreviewToolUserLocation] = None
    """The user's location."""


DataSourceResponsesSamplingParamsTool: TypeAlias = Annotated[
    Union[
        DataSourceResponsesSamplingParamsToolFunction,
        DataSourceResponsesSamplingParamsToolFileSearch,
        DataSourceResponsesSamplingParamsToolComputerUsePreview,
        DataSourceResponsesSamplingParamsToolWebSearchTool,
        DataSourceResponsesSamplingParamsToolMcp,
        DataSourceResponsesSamplingParamsToolCodeInterpreter,
        DataSourceResponsesSamplingParamsToolImageGeneration,
        DataSourceResponsesSamplingParamsToolLocalShell,
        DataSourceResponsesSamplingParamsToolCustom,
        DataSourceResponsesSamplingParamsToolWebSearchPreviewTool,
    ],
    PropertyInfo(discriminator="type"),
]


class DataSourceResponsesSamplingParams(BaseModel):
    max_completion_tokens: Optional[int] = None
    """The maximum number of tokens in the generated output."""

    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] = None
    """
    Constrains effort on reasoning for
    [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
    supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
    effort can result in faster responses and fewer tokens used on reasoning in a
    response.

    Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
    effort.
    """

    seed: Optional[int] = None
    """A seed value to initialize the randomness, during sampling."""

    temperature: Optional[float] = None
    """A higher temperature increases randomness in the outputs."""

    text: Optional[DataSourceResponsesSamplingParamsText] = None
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](https://platform.excai.com/docs/guides/text)
    - [Structured Outputs](https://platform.excai.com/docs/guides/structured-outputs)
    """

    tools: Optional[List[DataSourceResponsesSamplingParamsTool]] = None
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

    top_p: Optional[float] = None
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataSourceResponses(BaseModel):
    source: DataSourceResponsesSource
    """Determines what populates the `item` namespace in this run's data source."""

    type: Literal["responses"]
    """The type of run data source. Always `responses`."""

    input_messages: Optional[DataSourceResponsesInputMessages] = None
    """Used when sampling from a model.

    Dictates the structure of the messages passed into the model. Can either be a
    reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template
    with variable references to the `item` namespace.
    """

    model: Optional[str] = None
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[DataSourceResponsesSamplingParams] = None


DataSource: TypeAlias = Annotated[
    Union[DataSourceJSONL, DataSourceCompletions, DataSourceResponses], PropertyInfo(discriminator="type")
]


class Error(BaseModel):
    code: str
    """The error code."""

    message: str
    """The error message."""


class PerModelUsage(BaseModel):
    cached_tokens: int
    """The number of tokens retrieved from cache."""

    completion_tokens: int
    """The number of completion tokens generated."""

    invocation_count: int
    """The number of invocations."""

    run_model_name: str = FieldInfo(alias="model_name")
    """The name of the model."""

    prompt_tokens: int
    """The number of prompt tokens used."""

    total_tokens: int
    """The total number of tokens used."""


class PerTestingCriteriaResult(BaseModel):
    failed: int
    """Number of tests failed for this criteria."""

    passed: int
    """Number of tests passed for this criteria."""

    testing_criteria: str
    """A description of the testing criteria."""


class ResultCounts(BaseModel):
    errored: int
    """Number of output items that resulted in an error."""

    failed: int
    """Number of output items that failed to pass the evaluation."""

    passed: int
    """Number of output items that passed the evaluation."""

    total: int
    """Total number of executed output items."""


class RunCancelResponse(BaseModel):
    id: str
    """Unique identifier for the evaluation run."""

    created_at: int
    """Unix timestamp (in seconds) when the evaluation run was created."""

    data_source: DataSource
    """Information about the run's data source."""

    error: Error
    """An object representing an error response from the Eval API."""

    eval_id: str
    """The identifier of the associated evaluation."""

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    model: str
    """The model that is evaluated, if applicable."""

    name: str
    """The name of the evaluation run."""

    object: Literal["eval.run"]
    """The type of the object. Always "eval.run"."""

    per_model_usage: List[PerModelUsage]
    """Usage statistics for each model during the evaluation run."""

    per_testing_criteria_results: List[PerTestingCriteriaResult]
    """Results per testing criteria applied during the evaluation run."""

    report_url: str
    """The URL to the rendered evaluation run report on the UI dashboard."""

    result_counts: ResultCounts
    """Counters summarizing the outcomes of the evaluation run."""

    status: str
    """The status of the evaluation run."""
