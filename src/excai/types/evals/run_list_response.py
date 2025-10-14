# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "RunListResponse",
    "Data",
    "DataDataSource",
    "DataDataSourceCreateEvalJSONLRunDataSource",
    "DataDataSourceCreateEvalJSONLRunDataSourceSource",
    "DataDataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSource",
    "DataDataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSourceContent",
    "DataDataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileIDSource",
    "DataDataSourceCreateEvalCompletionsRunDataSource",
    "DataDataSourceCreateEvalCompletionsRunDataSourceSource",
    "DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSource",
    "DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSourceContent",
    "DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileIDSource",
    "DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalStoredCompletionsSource",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessages",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessages",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplate",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessage",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentList",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputTextContent",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputImageContent",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputFileContent",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItem",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContent",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentInputTextContent",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentOutputText",
    "DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReferenceInputMessages",
    "DataDataSourceCreateEvalCompletionsRunDataSourceSamplingParams",
    "DataDataSourceCreateEvalResponsesRunDataSource",
    "DataDataSourceCreateEvalResponsesRunDataSourceSource",
    "DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSource",
    "DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSourceContent",
    "DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileIDSource",
    "DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalResponsesSource",
    "DataDataSourceCreateEvalResponsesRunDataSourceInputMessages",
    "DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0",
    "DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0Template",
    "DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateChatMessage",
    "DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItem",
    "DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContent",
    "DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentInputTextContent",
    "DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentOutputText",
    "DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember1",
    "DataDataSourceCreateEvalResponsesRunDataSourceSamplingParams",
    "DataError",
    "DataPerModelUsage",
    "DataPerTestingCriteriaResult",
    "DataResultCounts",
]


class DataDataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSourceContent(BaseModel):
    item: Dict[str, object]

    sample: Optional[Dict[str, object]] = None


class DataDataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSource(BaseModel):
    content: List[DataDataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSourceContent]
    """The content of the jsonl file."""

    type: Literal["file_content"]
    """The type of jsonl source. Always `file_content`."""


class DataDataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileIDSource(BaseModel):
    id: str
    """The identifier of the file."""

    type: Literal["file_id"]
    """The type of jsonl source. Always `file_id`."""


DataDataSourceCreateEvalJSONLRunDataSourceSource: TypeAlias = Union[
    DataDataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSource,
    DataDataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileIDSource,
]


class DataDataSourceCreateEvalJSONLRunDataSource(BaseModel):
    source: DataDataSourceCreateEvalJSONLRunDataSourceSource

    type: Literal["jsonl"]
    """The type of data source. Always `jsonl`."""


class DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSourceContent(BaseModel):
    item: Dict[str, object]

    sample: Optional[Dict[str, object]] = None


class DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSource(BaseModel):
    content: List[DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSourceContent]
    """The content of the jsonl file."""

    type: Literal["file_content"]
    """The type of jsonl source. Always `file_content`."""


class DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileIDSource(BaseModel):
    id: str
    """The identifier of the file."""

    type: Literal["file_id"]
    """The type of jsonl source. Always `file_id`."""


class DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalStoredCompletionsSource(BaseModel):
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


DataDataSourceCreateEvalCompletionsRunDataSourceSource: TypeAlias = Union[
    DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSource,
    DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileIDSource,
    DataDataSourceCreateEvalCompletionsRunDataSourceSourceEvalStoredCompletionsSource,
]


class DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputTextContent(
    BaseModel
):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputImageContent(
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


class DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputFileContent(
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


DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentList: TypeAlias = Union[
    DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputTextContent,
    DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputImageContent,
    DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputFileContent,
]


class DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessage(
    BaseModel
):
    content: Union[
        str,
        List[
            DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentList
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


class DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentInputTextContent(
    BaseModel
):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentOutputText(
    BaseModel
):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContent: TypeAlias = Union[
    str,
    DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentInputTextContent,
    DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentOutputText,
]


class DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItem(BaseModel):
    content: DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContent
    """Text inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplate: TypeAlias = Union[
    DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessage,
    DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItem,
]


class DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessages(BaseModel):
    template: List[DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplate]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Literal["template"]
    """The type of input messages. Always `template`."""


class DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReferenceInputMessages(BaseModel):
    item_reference: str
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Literal["item_reference"]
    """The type of input messages. Always `item_reference`."""


DataDataSourceCreateEvalCompletionsRunDataSourceInputMessages: TypeAlias = Union[
    DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessages,
    DataDataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReferenceInputMessages,
]


class DataDataSourceCreateEvalCompletionsRunDataSourceSamplingParams(BaseModel):
    max_completion_tokens: Optional[int] = None
    """The maximum number of tokens in the generated output."""

    seed: Optional[int] = None
    """A seed value to initialize the randomness, during sampling."""

    temperature: Optional[float] = None
    """A higher temperature increases randomness in the outputs."""

    top_p: Optional[float] = None
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataDataSourceCreateEvalCompletionsRunDataSource(BaseModel):
    source: DataDataSourceCreateEvalCompletionsRunDataSourceSource
    """A StoredCompletionsRunDataSource configuration describing a set of filters"""

    type: Literal["completions"]
    """The type of run data source. Always `completions`."""

    input_messages: Optional[DataDataSourceCreateEvalCompletionsRunDataSourceInputMessages] = None

    model: Optional[str] = None
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[DataDataSourceCreateEvalCompletionsRunDataSourceSamplingParams] = None


class DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSourceContent(BaseModel):
    item: Dict[str, object]

    sample: Optional[Dict[str, object]] = None


class DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSource(BaseModel):
    content: List[DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSourceContent]
    """The content of the jsonl file."""

    type: Literal["file_content"]
    """The type of jsonl source. Always `file_content`."""


class DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileIDSource(BaseModel):
    id: str
    """The identifier of the file."""

    type: Literal["file_id"]
    """The type of jsonl source. Always `file_id`."""


class DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalResponsesSource(BaseModel):
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


DataDataSourceCreateEvalResponsesRunDataSourceSource: TypeAlias = Union[
    DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSource,
    DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileIDSource,
    DataDataSourceCreateEvalResponsesRunDataSourceSourceEvalResponsesSource,
]


class DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateChatMessage(BaseModel):
    content: str
    """The content of the message."""

    role: str
    """The role of the message (e.g. "system", "assistant", "user")."""


class DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentInputTextContent(
    BaseModel
):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentOutputText(
    BaseModel
):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContent: TypeAlias = Union[
    str,
    DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentInputTextContent,
    DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentOutputText,
]


class DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItem(BaseModel):
    content: DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContent
    """Text inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0Template: TypeAlias = Union[
    DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateChatMessage,
    DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItem,
]


class DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0(BaseModel):
    template: List[DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0Template]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Literal["template"]
    """The type of input messages. Always `template`."""


class DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember1(BaseModel):
    item_reference: str
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Literal["item_reference"]
    """The type of input messages. Always `item_reference`."""


DataDataSourceCreateEvalResponsesRunDataSourceInputMessages: TypeAlias = Union[
    DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0,
    DataDataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember1,
]


class DataDataSourceCreateEvalResponsesRunDataSourceSamplingParams(BaseModel):
    max_completion_tokens: Optional[int] = None
    """The maximum number of tokens in the generated output."""

    seed: Optional[int] = None
    """A seed value to initialize the randomness, during sampling."""

    temperature: Optional[float] = None
    """A higher temperature increases randomness in the outputs."""

    top_p: Optional[float] = None
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataDataSourceCreateEvalResponsesRunDataSource(BaseModel):
    source: DataDataSourceCreateEvalResponsesRunDataSourceSource
    """A EvalResponsesSource object describing a run data source configuration."""

    type: Literal["completions"]
    """The type of run data source. Always `completions`."""

    input_messages: Optional[DataDataSourceCreateEvalResponsesRunDataSourceInputMessages] = None

    model: Optional[str] = None
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[DataDataSourceCreateEvalResponsesRunDataSourceSamplingParams] = None


DataDataSource: TypeAlias = Union[
    DataDataSourceCreateEvalJSONLRunDataSource,
    DataDataSourceCreateEvalCompletionsRunDataSource,
    DataDataSourceCreateEvalResponsesRunDataSource,
]


class DataError(BaseModel):
    code: str
    """The error code."""

    message: str
    """The error message."""


class DataPerModelUsage(BaseModel):
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


class DataPerTestingCriteriaResult(BaseModel):
    failed: int
    """Number of tests failed for this criteria."""

    passed: int
    """Number of tests passed for this criteria."""

    testing_criteria: str
    """A description of the testing criteria."""


class DataResultCounts(BaseModel):
    errored: int
    """Number of output items that resulted in an error."""

    failed: int
    """Number of output items that failed to pass the evaluation."""

    passed: int
    """Number of output items that passed the evaluation."""

    total: int
    """Total number of executed output items."""


class Data(BaseModel):
    id: str
    """Unique identifier for the evaluation run."""

    created_at: int
    """Unix timestamp (in seconds) when the evaluation run was created."""

    data_source: DataDataSource
    """Information about the run's data source."""

    error: DataError
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

    per_model_usage: List[DataPerModelUsage]
    """Usage statistics for each model during the evaluation run."""

    per_testing_criteria_results: List[DataPerTestingCriteriaResult]
    """Results per testing criteria applied during the evaluation run."""

    report_url: str
    """The URL to the rendered evaluation run report on the UI dashboard."""

    result_counts: DataResultCounts
    """Counters summarizing the outcomes of the evaluation run."""

    status: str
    """The status of the evaluation run."""


class RunListResponse(BaseModel):
    data: List[Data]
    """An array of eval run objects."""

    first_id: str
    """The identifier of the first eval run in the data array."""

    has_more: bool
    """Indicates whether there are more evals available."""

    last_id: str
    """The identifier of the last eval run in the data array."""

    object: Literal["list"]
    """The type of this object. It is always set to "list"."""
