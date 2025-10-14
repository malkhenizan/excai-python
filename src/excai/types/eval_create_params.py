# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "EvalCreateParams",
    "DataSourceConfig",
    "DataSourceConfigCustom",
    "DataSourceConfigLogs",
    "DataSourceConfigStoredCompletions",
    "TestingCriterion",
    "TestingCriterionLabelModel",
    "TestingCriterionLabelModelInput",
    "TestingCriterionLabelModelInputSimpleInputMessage",
    "TestingCriterionLabelModelInputEvalItem",
    "TestingCriterionLabelModelInputEvalItemContent",
    "TestingCriterionLabelModelInputEvalItemContentInputTextContent",
    "TestingCriterionLabelModelInputEvalItemContentOutputText",
    "TestingCriterionLabelModelInputEvalItemContentInputImage",
    "TestingCriterionLabelModelInputEvalItemContentInputAudio",
    "TestingCriterionLabelModelInputEvalItemContentInputAudioInputAudio",
    "TestingCriterionStringCheck",
    "TestingCriterionTextSimilarity",
    "TestingCriterionPython",
    "TestingCriterionScoreModel",
    "TestingCriterionScoreModelInput",
    "TestingCriterionScoreModelInputContent",
    "TestingCriterionScoreModelInputContentInputTextContent",
    "TestingCriterionScoreModelInputContentOutputText",
    "TestingCriterionScoreModelInputContentInputImage",
    "TestingCriterionScoreModelInputContentInputAudio",
    "TestingCriterionScoreModelInputContentInputAudioInputAudio",
    "TestingCriterionScoreModelSamplingParams",
]


class EvalCreateParams(TypedDict, total=False):
    data_source_config: Required[DataSourceConfig]
    """The configuration for the data source used for the evaluation runs.

    Dictates the schema of the data used in the evaluation.
    """

    testing_criteria: Required[Iterable[TestingCriterion]]
    """A list of graders for all eval runs in this group.

    Graders can reference variables in the data source using double curly braces
    notation, like `{{item.variable_name}}`. To reference the model's output, use
    the `sample` namespace (ie, `{{sample.output_text}}`).
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: str
    """The name of the evaluation."""


class DataSourceConfigCustom(TypedDict, total=False):
    item_schema: Required[Dict[str, object]]
    """The json schema for each row in the data source."""

    type: Required[Literal["custom"]]
    """The type of data source. Always `custom`."""

    include_sample_schema: bool
    """
    Whether the eval should expect you to populate the sample namespace (ie, by
    generating responses off of your data source)
    """


class DataSourceConfigLogs(TypedDict, total=False):
    type: Required[Literal["logs"]]
    """The type of data source. Always `logs`."""

    metadata: Dict[str, object]
    """Metadata filters for the logs data source."""


class DataSourceConfigStoredCompletions(TypedDict, total=False):
    type: Required[Literal["stored_completions"]]
    """The type of data source. Always `stored_completions`."""

    metadata: Dict[str, object]
    """Metadata filters for the stored completions data source."""


DataSourceConfig: TypeAlias = Union[DataSourceConfigCustom, DataSourceConfigLogs, DataSourceConfigStoredCompletions]


class TestingCriterionLabelModelInputSimpleInputMessage(TypedDict, total=False):
    content: Required[str]
    """The content of the message."""

    role: Required[str]
    """The role of the message (e.g. "system", "assistant", "user")."""


class TestingCriterionLabelModelInputEvalItemContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class TestingCriterionLabelModelInputEvalItemContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class TestingCriterionLabelModelInputEvalItemContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class TestingCriterionLabelModelInputEvalItemContentInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class TestingCriterionLabelModelInputEvalItemContentInputAudio(TypedDict, total=False):
    input_audio: Required[TestingCriterionLabelModelInputEvalItemContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


TestingCriterionLabelModelInputEvalItemContent: TypeAlias = Union[
    str,
    TestingCriterionLabelModelInputEvalItemContentInputTextContent,
    TestingCriterionLabelModelInputEvalItemContentOutputText,
    TestingCriterionLabelModelInputEvalItemContentInputImage,
    TestingCriterionLabelModelInputEvalItemContentInputAudio,
    Iterable[object],
]


class TestingCriterionLabelModelInputEvalItem(TypedDict, total=False):
    content: Required[TestingCriterionLabelModelInputEvalItemContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


TestingCriterionLabelModelInput: TypeAlias = Union[
    TestingCriterionLabelModelInputSimpleInputMessage, TestingCriterionLabelModelInputEvalItem
]


class TestingCriterionLabelModel(TypedDict, total=False):
    input: Required[Iterable[TestingCriterionLabelModelInput]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the `item` namespace, ie {{item.name}}.
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


class TestingCriterionStringCheck(TypedDict, total=False):
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


class TestingCriterionTextSimilarity(TypedDict, total=False):
    evaluation_metric: Required[
        Literal[
            "cosine",
            "fuzzy_match",
            "bleu",
            "gleu",
            "meteor",
            "rouge_1",
            "rouge_2",
            "rouge_3",
            "rouge_4",
            "rouge_5",
            "rouge_l",
        ]
    ]
    """The evaluation metric to use.

    One of `cosine`, `fuzzy_match`, `bleu`, `gleu`, `meteor`, `rouge_1`, `rouge_2`,
    `rouge_3`, `rouge_4`, `rouge_5`, or `rouge_l`.
    """

    input: Required[str]
    """The text being graded."""

    name: Required[str]
    """The name of the grader."""

    pass_threshold: Required[float]
    """The threshold for the score."""

    reference: Required[str]
    """The text being graded against."""

    type: Required[Literal["text_similarity"]]
    """The type of grader."""


class TestingCriterionPython(TypedDict, total=False):
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


class TestingCriterionScoreModelInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class TestingCriterionScoreModelInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class TestingCriterionScoreModelInputContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class TestingCriterionScoreModelInputContentInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class TestingCriterionScoreModelInputContentInputAudio(TypedDict, total=False):
    input_audio: Required[TestingCriterionScoreModelInputContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


TestingCriterionScoreModelInputContent: TypeAlias = Union[
    str,
    TestingCriterionScoreModelInputContentInputTextContent,
    TestingCriterionScoreModelInputContentOutputText,
    TestingCriterionScoreModelInputContentInputImage,
    TestingCriterionScoreModelInputContentInputAudio,
    Iterable[object],
]


class TestingCriterionScoreModelInput(TypedDict, total=False):
    content: Required[TestingCriterionScoreModelInputContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class TestingCriterionScoreModelSamplingParams(TypedDict, total=False):
    max_completions_tokens: Optional[int]
    """The maximum number of tokens the grader model may generate in its response."""

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

    seed: Optional[int]
    """A seed value to initialize the randomness, during sampling."""

    temperature: Optional[float]
    """A higher temperature increases randomness in the outputs."""

    top_p: Optional[float]
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class TestingCriterionScoreModel(TypedDict, total=False):
    input: Required[Iterable[TestingCriterionScoreModelInput]]
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

    sampling_params: TestingCriterionScoreModelSamplingParams
    """The sampling parameters for the model."""


TestingCriterion: TypeAlias = Union[
    TestingCriterionLabelModel,
    TestingCriterionStringCheck,
    TestingCriterionTextSimilarity,
    TestingCriterionPython,
    TestingCriterionScoreModel,
]
