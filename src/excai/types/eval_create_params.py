# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "EvalCreateParams",
    "DataSourceConfig",
    "DataSourceConfigCreateEvalCustomDataSourceConfig",
    "DataSourceConfigCreateEvalLogsDataSourceConfig",
    "TestingCriterion",
    "TestingCriterionCreateEvalLabelModelGrader",
    "TestingCriterionCreateEvalLabelModelGraderInput",
    "TestingCriterionCreateEvalLabelModelGraderInputSimpleInputMessage",
    "TestingCriterionCreateEvalLabelModelGraderInputEvalItem",
    "TestingCriterionCreateEvalLabelModelGraderInputEvalItemContent",
    "TestingCriterionCreateEvalLabelModelGraderInputEvalItemContentInputTextContent",
    "TestingCriterionCreateEvalLabelModelGraderInputEvalItemContentOutputText",
    "TestingCriterionEvalStringCheckGrader",
    "TestingCriterionEvalTextSimilarityGrader",
    "TestingCriterionEvalPythonGrader",
    "TestingCriterionEvalScoreModelGrader",
    "TestingCriterionEvalScoreModelGraderInput",
    "TestingCriterionEvalScoreModelGraderInputContent",
    "TestingCriterionEvalScoreModelGraderInputContentInputTextContent",
    "TestingCriterionEvalScoreModelGraderInputContentOutputText",
]


class EvalCreateParams(TypedDict, total=False):
    data_source_config: Required[DataSourceConfig]
    """The configuration for the data source used for the evaluation runs."""

    testing_criteria: Required[Iterable[TestingCriterion]]
    """A list of graders for all eval runs in this group."""

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: str
    """The name of the evaluation."""


class DataSourceConfigCreateEvalCustomDataSourceConfig(TypedDict, total=False):
    item_schema: Required[Dict[str, object]]
    """The json schema for each row in the data source."""

    type: Required[Literal["custom"]]
    """The type of data source. Always `custom`."""

    include_sample_schema: bool
    """
    Whether the eval should expect you to populate the sample namespace (ie, by
    generating responses off of your data source)
    """


class DataSourceConfigCreateEvalLogsDataSourceConfig(TypedDict, total=False):
    type: Required[Literal["logs"]]
    """The type of data source. Always `logs`."""

    metadata: Dict[str, object]
    """Metadata filters for the logs data source."""


DataSourceConfig: TypeAlias = Union[
    DataSourceConfigCreateEvalCustomDataSourceConfig, DataSourceConfigCreateEvalLogsDataSourceConfig
]


class TestingCriterionCreateEvalLabelModelGraderInputSimpleInputMessage(TypedDict, total=False):
    content: Required[str]
    """The content of the message."""

    role: Required[str]
    """The role of the message (e.g. "system", "assistant", "user")."""


class TestingCriterionCreateEvalLabelModelGraderInputEvalItemContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class TestingCriterionCreateEvalLabelModelGraderInputEvalItemContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


TestingCriterionCreateEvalLabelModelGraderInputEvalItemContent: TypeAlias = Union[
    str,
    TestingCriterionCreateEvalLabelModelGraderInputEvalItemContentInputTextContent,
    TestingCriterionCreateEvalLabelModelGraderInputEvalItemContentOutputText,
]


class TestingCriterionCreateEvalLabelModelGraderInputEvalItem(TypedDict, total=False):
    content: Required[TestingCriterionCreateEvalLabelModelGraderInputEvalItemContent]
    """Text inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


TestingCriterionCreateEvalLabelModelGraderInput: TypeAlias = Union[
    TestingCriterionCreateEvalLabelModelGraderInputSimpleInputMessage,
    TestingCriterionCreateEvalLabelModelGraderInputEvalItem,
]


class TestingCriterionCreateEvalLabelModelGrader(TypedDict, total=False):
    input: Required[Iterable[TestingCriterionCreateEvalLabelModelGraderInput]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    labels: Required[SequenceNotStr[str]]
    """The labels to classify to each item in the evaluation."""

    model: Required[str]
    """The model to use for the evaluation. Must support structured outputs."""

    name: Required[str]
    """The name of the grader."""

    passing_labels: Required[SequenceNotStr[str]]
    """The labels that indicate a passing result. Must be a subset of labels."""

    type: Required[Literal["label_model"]]
    """The object type, which is always `label_model`."""


class TestingCriterionEvalStringCheckGrader(TypedDict, total=False):
    input: Required[str]
    """The input text. This may include template strings."""

    name: Required[str]
    """The name of the grader."""

    operation: Required[Literal["eq", "ne", "like", "ilike"]]
    """The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`."""

    reference: Required[str]
    """The reference text. This may include template strings."""

    type: Required[Literal["string_check"]]
    """The object type, which is always `string_check`."""


class TestingCriterionEvalTextSimilarityGrader(TypedDict, total=False):
    evaluation_metric: Required[
        Literal[
            "fuzzy_match", "bleu", "gleu", "meteor", "rouge_1", "rouge_2", "rouge_3", "rouge_4", "rouge_5", "rouge_l"
        ]
    ]
    """The evaluation metric to use.

    One of `fuzzy_match`, `bleu`, `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`,
    `rouge_4`, `rouge_5`, or `rouge_l`.
    """

    input: Required[str]
    """The text being graded."""

    pass_threshold: Required[float]
    """A float score where a value greater than or equal indicates a passing grade."""

    reference: Required[str]
    """The text being graded against."""

    type: Required[Literal["text_similarity"]]
    """The type of grader."""

    name: str
    """The name of the grader."""


class TestingCriterionEvalPythonGrader(TypedDict, total=False):
    name: Required[str]
    """The name of the grader."""

    source: Required[str]
    """The source code of the python script."""

    type: Required[Literal["python"]]
    """The object type, which is always `python`."""

    image_tag: str
    """The image tag to use for the python script."""

    pass_threshold: float
    """The threshold for the score."""


class TestingCriterionEvalScoreModelGraderInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class TestingCriterionEvalScoreModelGraderInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


TestingCriterionEvalScoreModelGraderInputContent: TypeAlias = Union[
    str,
    TestingCriterionEvalScoreModelGraderInputContentInputTextContent,
    TestingCriterionEvalScoreModelGraderInputContentOutputText,
]


class TestingCriterionEvalScoreModelGraderInput(TypedDict, total=False):
    content: Required[TestingCriterionEvalScoreModelGraderInputContent]
    """Text inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class TestingCriterionEvalScoreModelGrader(TypedDict, total=False):
    input: Required[Iterable[TestingCriterionEvalScoreModelGraderInput]]
    """The input text. This may include template strings."""

    model: Required[str]
    """The model to use for the evaluation."""

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["score_model"]]
    """The object type, which is always `score_model`."""

    pass_threshold: float
    """The threshold for the score."""

    range: Iterable[float]
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: object
    """The sampling parameters for the model."""


TestingCriterion: TypeAlias = Union[
    TestingCriterionCreateEvalLabelModelGrader,
    TestingCriterionEvalStringCheckGrader,
    TestingCriterionEvalTextSimilarityGrader,
    TestingCriterionEvalPythonGrader,
    TestingCriterionEvalScoreModelGrader,
]
