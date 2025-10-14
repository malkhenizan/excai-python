# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "RunCreateResponse",
    "DataSource",
    "DataSourceCreateEvalJSONLRunDataSource",
    "DataSourceCreateEvalJSONLRunDataSourceSource",
    "DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSource",
    "DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSourceContent",
    "DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileIDSource",
    "DataSourceCreateEvalCompletionsRunDataSource",
    "DataSourceCreateEvalCompletionsRunDataSourceSource",
    "DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSource",
    "DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSourceContent",
    "DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileIDSource",
    "DataSourceCreateEvalCompletionsRunDataSourceSourceEvalStoredCompletionsSource",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessages",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessages",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplate",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessage",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentList",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputTextContent",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputImageContent",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputFileContent",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItem",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContent",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentInputTextContent",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentOutputText",
    "DataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReferenceInputMessages",
    "DataSourceCreateEvalCompletionsRunDataSourceSamplingParams",
    "DataSourceCreateEvalResponsesRunDataSource",
    "DataSourceCreateEvalResponsesRunDataSourceSource",
    "DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSource",
    "DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSourceContent",
    "DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileIDSource",
    "DataSourceCreateEvalResponsesRunDataSourceSourceEvalResponsesSource",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessages",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0Template",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateChatMessage",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItem",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContent",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentInputTextContent",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentOutputText",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember1",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParams",
    "Error",
    "PerModelUsage",
    "PerTestingCriteriaResult",
    "ResultCounts",
]


class DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSourceContent(BaseModel):
    item: Dict[str, object]

    sample: Optional[Dict[str, object]] = None


class DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSource(BaseModel):
    content: List[DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSourceContent]
    """The content of the jsonl file."""

    type: Literal["file_content"]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileIDSource(BaseModel):
    id: str
    """The identifier of the file."""

    type: Literal["file_id"]
    """The type of jsonl source. Always `file_id`."""


DataSourceCreateEvalJSONLRunDataSourceSource: TypeAlias = Union[
    DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSource,
    DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileIDSource,
]


class DataSourceCreateEvalJSONLRunDataSource(BaseModel):
    source: DataSourceCreateEvalJSONLRunDataSourceSource

    type: Literal["jsonl"]
    """The type of data source. Always `jsonl`."""


class DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSourceContent(BaseModel):
    item: Dict[str, object]

    sample: Optional[Dict[str, object]] = None


class DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSource(BaseModel):
    content: List[DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSourceContent]
    """The content of the jsonl file."""

    type: Literal["file_content"]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileIDSource(BaseModel):
    id: str
    """The identifier of the file."""

    type: Literal["file_id"]
    """The type of jsonl source. Always `file_id`."""


class DataSourceCreateEvalCompletionsRunDataSourceSourceEvalStoredCompletionsSource(BaseModel):
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


DataSourceCreateEvalCompletionsRunDataSourceSource: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSource,
    DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileIDSource,
    DataSourceCreateEvalCompletionsRunDataSourceSourceEvalStoredCompletionsSource,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputTextContent(
    BaseModel
):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputImageContent(
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


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputFileContent(
    BaseModel
):
    type: Literal["input_file"]
    """The type of the input item. Always `input_file`."""

    file_data: Optional[str] = None
    """The content of the file to be sent to the model."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    filename: Optional[str] = None
    """The name of the file to be sent to the model."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentList: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputTextContent,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputImageContent,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputFileContent,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessage(BaseModel):
    content: Union[
        str,
        List[
            DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentList
        ],
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


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentInputTextContent(
    BaseModel
):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentOutputText(
    BaseModel
):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContent: TypeAlias = Union[
    str,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentInputTextContent,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentOutputText,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItem(BaseModel):
    content: DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContent
    """Text inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplate: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessage,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItem,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessages(BaseModel):
    template: List[DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplate]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Literal["template"]
    """The type of input messages. Always `template`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReferenceInputMessages(BaseModel):
    item_reference: str
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Literal["item_reference"]
    """The type of input messages. Always `item_reference`."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessages: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessages,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReferenceInputMessages,
]


class DataSourceCreateEvalCompletionsRunDataSourceSamplingParams(BaseModel):
    max_completion_tokens: Optional[int] = None
    """The maximum number of tokens in the generated output."""

    seed: Optional[int] = None
    """A seed value to initialize the randomness, during sampling."""

    temperature: Optional[float] = None
    """A higher temperature increases randomness in the outputs."""

    top_p: Optional[float] = None
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataSourceCreateEvalCompletionsRunDataSource(BaseModel):
    source: DataSourceCreateEvalCompletionsRunDataSourceSource
    """A StoredCompletionsRunDataSource configuration describing a set of filters"""

    type: Literal["completions"]
    """The type of run data source. Always `completions`."""

    input_messages: Optional[DataSourceCreateEvalCompletionsRunDataSourceInputMessages] = None

    model: Optional[str] = None
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[DataSourceCreateEvalCompletionsRunDataSourceSamplingParams] = None


class DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSourceContent(BaseModel):
    item: Dict[str, object]

    sample: Optional[Dict[str, object]] = None


class DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSource(BaseModel):
    content: List[DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSourceContent]
    """The content of the jsonl file."""

    type: Literal["file_content"]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileIDSource(BaseModel):
    id: str
    """The identifier of the file."""

    type: Literal["file_id"]
    """The type of jsonl source. Always `file_id`."""


class DataSourceCreateEvalResponsesRunDataSourceSourceEvalResponsesSource(BaseModel):
    type: Literal["responses"]
    """The type of run data source. Always `responses`."""

    allow_parallel_tool_calls: Optional[bool] = None
    """Whether to allow parallel tool calls.

    This is a query parameter used to select responses.
    """

    created_after: Optional[int] = None
    """Only include items created after this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    created_before: Optional[int] = None
    """Only include items created before this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    has_tool_calls: Optional[bool] = None
    """Whether the response has tool calls.

    This is a query parameter used to select responses.
    """

    instructions_search: Optional[str] = None
    """Optional search string for instructions.

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

    reasoning_effort: Optional[Literal["low", "medium", "high"]] = None
    """Optional reasoning effort parameter.

    This is a query parameter used to select responses.
    """

    temperature: Optional[float] = None
    """Sampling temperature. This is a query parameter used to select responses."""

    top_p: Optional[float] = None
    """Nucleus sampling parameter. This is a query parameter used to select responses."""

    users: Optional[List[str]] = None
    """List of user identifiers. This is a query parameter used to select responses."""


DataSourceCreateEvalResponsesRunDataSourceSource: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSource,
    DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileIDSource,
    DataSourceCreateEvalResponsesRunDataSourceSourceEvalResponsesSource,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateChatMessage(BaseModel):
    content: str
    """The content of the message."""

    role: str
    """The role of the message (e.g. "system", "assistant", "user")."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentInputTextContent(
    BaseModel
):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContent: TypeAlias = Union[
    str,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentInputTextContent,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentOutputText,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItem(BaseModel):
    content: DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContent
    """Text inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0Template: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateChatMessage,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItem,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0(BaseModel):
    template: List[DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0Template]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Literal["template"]
    """The type of input messages. Always `template`."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember1(BaseModel):
    item_reference: str
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Literal["item_reference"]
    """The type of input messages. Always `item_reference`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessages: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember1,
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParams(BaseModel):
    max_completion_tokens: Optional[int] = None
    """The maximum number of tokens in the generated output."""

    seed: Optional[int] = None
    """A seed value to initialize the randomness, during sampling."""

    temperature: Optional[float] = None
    """A higher temperature increases randomness in the outputs."""

    top_p: Optional[float] = None
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataSourceCreateEvalResponsesRunDataSource(BaseModel):
    source: DataSourceCreateEvalResponsesRunDataSourceSource
    """A EvalResponsesSource object describing a run data source configuration."""

    type: Literal["completions"]
    """The type of run data source. Always `completions`."""

    input_messages: Optional[DataSourceCreateEvalResponsesRunDataSourceInputMessages] = None

    model: Optional[str] = None
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[DataSourceCreateEvalResponsesRunDataSourceSamplingParams] = None


DataSource: TypeAlias = Union[
    DataSourceCreateEvalJSONLRunDataSource,
    DataSourceCreateEvalCompletionsRunDataSource,
    DataSourceCreateEvalResponsesRunDataSource,
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

    api_model_name: str = FieldInfo(alias="model_name")
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


class RunCreateResponse(BaseModel):
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
