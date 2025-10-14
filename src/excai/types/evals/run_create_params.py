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


class DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSourceContent(TypedDict, total=False):
    item: Required[Dict[str, object]]

    sample: Dict[str, object]


class DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSource(TypedDict, total=False):
    content: Required[Iterable[DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSourceContent]]
    """The content of the jsonl file."""

    type: Required[Literal["file_content"]]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileIDSource(TypedDict, total=False):
    id: Required[str]
    """The identifier of the file."""

    type: Required[Literal["file_id"]]
    """The type of jsonl source. Always `file_id`."""


DataSourceCreateEvalJSONLRunDataSourceSource: TypeAlias = Union[
    DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileContentSource,
    DataSourceCreateEvalJSONLRunDataSourceSourceEvalJSONLFileIDSource,
]


class DataSourceCreateEvalJSONLRunDataSource(TypedDict, total=False):
    source: Required[DataSourceCreateEvalJSONLRunDataSourceSource]

    type: Required[Literal["jsonl"]]
    """The type of data source. Always `jsonl`."""


class DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSourceContent(TypedDict, total=False):
    item: Required[Dict[str, object]]

    sample: Dict[str, object]


class DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSource(TypedDict, total=False):
    content: Required[Iterable[DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSourceContent]]
    """The content of the jsonl file."""

    type: Required[Literal["file_content"]]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileIDSource(TypedDict, total=False):
    id: Required[str]
    """The identifier of the file."""

    type: Required[Literal["file_id"]]
    """The type of jsonl source. Always `file_id`."""


class DataSourceCreateEvalCompletionsRunDataSourceSourceEvalStoredCompletionsSource(TypedDict, total=False):
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
    DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileContentSource,
    DataSourceCreateEvalCompletionsRunDataSourceSourceEvalJSONLFileIDSource,
    DataSourceCreateEvalCompletionsRunDataSourceSourceEvalStoredCompletionsSource,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputTextContent(
    TypedDict, total=False
):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputImageContent(
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


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputFileContent(
    TypedDict, total=False
):
    type: Required[Literal["input_file"]]
    """The type of the input item. Always `input_file`."""

    file_data: str
    """The content of the file to be sent to the model."""

    file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    filename: str
    """The name of the file to be sent to the model."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentList: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputTextContent,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputImageContent,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentListInputFileContent,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessage(
    TypedDict, total=False
):
    content: Required[
        Union[
            str,
            Iterable[
                DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessageContentInputMessageContentList
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


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentInputTextContent(
    TypedDict, total=False
):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentOutputText(
    TypedDict, total=False
):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContent: TypeAlias = Union[
    str,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentInputTextContent,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContentOutputText,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItem(
    TypedDict, total=False
):
    content: Required[
        DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItemContent
    ]
    """Text inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplate: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEasyInputMessage,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplateEvalItem,
]


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessages(TypedDict, total=False):
    template: Required[Iterable[DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessagesTemplate]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Required[Literal["template"]]
    """The type of input messages. Always `template`."""


class DataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReferenceInputMessages(TypedDict, total=False):
    item_reference: Required[str]
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Required[Literal["item_reference"]]
    """The type of input messages. Always `item_reference`."""


DataSourceCreateEvalCompletionsRunDataSourceInputMessages: TypeAlias = Union[
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesTemplateInputMessages,
    DataSourceCreateEvalCompletionsRunDataSourceInputMessagesItemReferenceInputMessages,
]


class DataSourceCreateEvalCompletionsRunDataSourceSamplingParams(TypedDict, total=False):
    max_completion_tokens: int
    """The maximum number of tokens in the generated output."""

    seed: int
    """A seed value to initialize the randomness, during sampling."""

    temperature: float
    """A higher temperature increases randomness in the outputs."""

    top_p: float
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataSourceCreateEvalCompletionsRunDataSource(TypedDict, total=False):
    source: Required[DataSourceCreateEvalCompletionsRunDataSourceSource]
    """A StoredCompletionsRunDataSource configuration describing a set of filters"""

    type: Required[Literal["completions"]]
    """The type of run data source. Always `completions`."""

    input_messages: DataSourceCreateEvalCompletionsRunDataSourceInputMessages

    model: str
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: DataSourceCreateEvalCompletionsRunDataSourceSamplingParams


class DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSourceContent(TypedDict, total=False):
    item: Required[Dict[str, object]]

    sample: Dict[str, object]


class DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSource(TypedDict, total=False):
    content: Required[Iterable[DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSourceContent]]
    """The content of the jsonl file."""

    type: Required[Literal["file_content"]]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileIDSource(TypedDict, total=False):
    id: Required[str]
    """The identifier of the file."""

    type: Required[Literal["file_id"]]
    """The type of jsonl source. Always `file_id`."""


class DataSourceCreateEvalResponsesRunDataSourceSourceEvalResponsesSource(TypedDict, total=False):
    type: Required[Literal["responses"]]
    """The type of run data source. Always `responses`."""

    allow_parallel_tool_calls: Optional[bool]
    """Whether to allow parallel tool calls.

    This is a query parameter used to select responses.
    """

    created_after: Optional[int]
    """Only include items created after this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    created_before: Optional[int]
    """Only include items created before this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    has_tool_calls: Optional[bool]
    """Whether the response has tool calls.

    This is a query parameter used to select responses.
    """

    instructions_search: Optional[str]
    """Optional search string for instructions.

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

    reasoning_effort: Optional[Literal["low", "medium", "high"]]
    """Optional reasoning effort parameter.

    This is a query parameter used to select responses.
    """

    temperature: Optional[float]
    """Sampling temperature. This is a query parameter used to select responses."""

    top_p: Optional[float]
    """Nucleus sampling parameter. This is a query parameter used to select responses."""

    users: Optional[SequenceNotStr[str]]
    """List of user identifiers. This is a query parameter used to select responses."""


DataSourceCreateEvalResponsesRunDataSourceSource: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileContentSource,
    DataSourceCreateEvalResponsesRunDataSourceSourceEvalJSONLFileIDSource,
    DataSourceCreateEvalResponsesRunDataSourceSourceEvalResponsesSource,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateChatMessage(TypedDict, total=False):
    content: Required[str]
    """The content of the message."""

    role: Required[str]
    """The role of the message (e.g. "system", "assistant", "user")."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentInputTextContent(
    TypedDict, total=False
):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentOutputText(
    TypedDict, total=False
):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContent: TypeAlias = Union[
    str,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentInputTextContent,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContentOutputText,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItem(TypedDict, total=False):
    content: Required[DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItemContent]
    """Text inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0Template: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateChatMessage,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0TemplateEvalItem,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0(TypedDict, total=False):
    template: Required[Iterable[DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0Template]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Required[Literal["template"]]
    """The type of input messages. Always `template`."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember1(TypedDict, total=False):
    item_reference: Required[str]
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Required[Literal["item_reference"]]
    """The type of input messages. Always `item_reference`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessages: TypeAlias = Union[
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember0,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesUnionMember1,
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParams(TypedDict, total=False):
    max_completion_tokens: int
    """The maximum number of tokens in the generated output."""

    seed: int
    """A seed value to initialize the randomness, during sampling."""

    temperature: float
    """A higher temperature increases randomness in the outputs."""

    top_p: float
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataSourceCreateEvalResponsesRunDataSource(TypedDict, total=False):
    source: Required[DataSourceCreateEvalResponsesRunDataSourceSource]
    """A EvalResponsesSource object describing a run data source configuration."""

    type: Required[Literal["completions"]]
    """The type of run data source. Always `completions`."""

    input_messages: DataSourceCreateEvalResponsesRunDataSourceInputMessages

    model: str
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: DataSourceCreateEvalResponsesRunDataSourceSamplingParams


DataSource: TypeAlias = Union[
    DataSourceCreateEvalJSONLRunDataSource,
    DataSourceCreateEvalCompletionsRunDataSource,
    DataSourceCreateEvalResponsesRunDataSource,
]
