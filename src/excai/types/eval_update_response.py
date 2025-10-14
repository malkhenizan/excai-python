# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "EvalUpdateResponse",
    "DataSourceConfig",
    "DataSourceConfigCustom",
    "DataSourceConfigLogs",
    "DataSourceConfigStoredCompletions",
    "TestingCriterion",
    "TestingCriterionGraderLabelModel",
    "TestingCriterionGraderLabelModelInput",
    "TestingCriterionGraderLabelModelInputContent",
    "TestingCriterionGraderLabelModelInputContentInputTextContent",
    "TestingCriterionGraderLabelModelInputContentOutputText",
    "TestingCriterionGraderLabelModelInputContentInputImage",
    "TestingCriterionGraderLabelModelInputContentInputAudio",
    "TestingCriterionGraderLabelModelInputContentInputAudioInputAudio",
    "TestingCriterionGraderStringCheck",
    "TestingCriterionEvalGraderTextSimilarity",
    "TestingCriterionEvalGraderPython",
    "TestingCriterionEvalGraderScoreModel",
    "TestingCriterionEvalGraderScoreModelInput",
    "TestingCriterionEvalGraderScoreModelInputContent",
    "TestingCriterionEvalGraderScoreModelInputContentInputTextContent",
    "TestingCriterionEvalGraderScoreModelInputContentOutputText",
    "TestingCriterionEvalGraderScoreModelInputContentInputImage",
    "TestingCriterionEvalGraderScoreModelInputContentInputAudio",
    "TestingCriterionEvalGraderScoreModelInputContentInputAudioInputAudio",
    "TestingCriterionEvalGraderScoreModelSamplingParams",
]


class DataSourceConfigCustom(BaseModel):
    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """
    The json schema for the run data source items. Learn how to build JSON schemas
    [here](https://json-schema.org/).
    """

    type: Literal["custom"]
    """The type of data source. Always `custom`."""


class DataSourceConfigLogs(BaseModel):
    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """
    The json schema for the run data source items. Learn how to build JSON schemas
    [here](https://json-schema.org/).
    """

    type: Literal["logs"]
    """The type of data source. Always `logs`."""

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """


class DataSourceConfigStoredCompletions(BaseModel):
    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """
    The json schema for the run data source items. Learn how to build JSON schemas
    [here](https://json-schema.org/).
    """

    type: Literal["stored_completions"]
    """The type of data source. Always `stored_completions`."""

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """


DataSourceConfig: TypeAlias = Annotated[
    Union[DataSourceConfigCustom, DataSourceConfigLogs, DataSourceConfigStoredCompletions],
    PropertyInfo(discriminator="type"),
]


class TestingCriterionGraderLabelModelInputContentInputTextContent(BaseModel):
    __test__ = False
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class TestingCriterionGraderLabelModelInputContentOutputText(BaseModel):
    __test__ = False
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class TestingCriterionGraderLabelModelInputContentInputImage(BaseModel):
    __test__ = False
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class TestingCriterionGraderLabelModelInputContentInputAudioInputAudio(BaseModel):
    __test__ = False
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class TestingCriterionGraderLabelModelInputContentInputAudio(BaseModel):
    __test__ = False
    input_audio: TestingCriterionGraderLabelModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


TestingCriterionGraderLabelModelInputContent: TypeAlias = Union[
    str,
    TestingCriterionGraderLabelModelInputContentInputTextContent,
    TestingCriterionGraderLabelModelInputContentOutputText,
    TestingCriterionGraderLabelModelInputContentInputImage,
    TestingCriterionGraderLabelModelInputContentInputAudio,
    List[object],
]


class TestingCriterionGraderLabelModelInput(BaseModel):
    __test__ = False
    content: TestingCriterionGraderLabelModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class TestingCriterionGraderLabelModel(BaseModel):
    __test__ = False
    input: List[TestingCriterionGraderLabelModelInput]

    labels: List[str]
    """The labels to assign to each item in the evaluation."""

    model: str
    """The model to use for the evaluation. Must support structured outputs."""

    name: str
    """The name of the grader."""

    passing_labels: List[str]
    """The labels that indicate a passing result. Must be a subset of labels."""

    type: Literal["label_model"]
    """The object type, which is always `label_model`."""


class TestingCriterionGraderStringCheck(BaseModel):
    __test__ = False
    input: str
    """The input text. This may include template strings."""

    name: str
    """The name of the grader."""

    operation: Literal["eq", "ne", "like", "ilike"]
    """The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`."""

    reference: str
    """The reference text. This may include template strings."""

    type: Literal["string_check"]
    """The object type, which is always `string_check`."""


class TestingCriterionEvalGraderTextSimilarity(BaseModel):
    __test__ = False
    evaluation_metric: Literal[
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
    """The evaluation metric to use.

    One of `cosine`, `fuzzy_match`, `bleu`, `gleu`, `meteor`, `rouge_1`, `rouge_2`,
    `rouge_3`, `rouge_4`, `rouge_5`, or `rouge_l`.
    """

    input: str
    """The text being graded."""

    name: str
    """The name of the grader."""

    pass_threshold: float
    """The threshold for the score."""

    reference: str
    """The text being graded against."""

    type: Literal["text_similarity"]
    """The type of grader."""


class TestingCriterionEvalGraderPython(BaseModel):
    __test__ = False
    name: str
    """The name of the grader."""

    source: str
    """The source code of the python script."""

    type: Literal["python"]
    """The object type, which is always `python`."""

    image_tag: Optional[str] = None
    """The image tag to use for the python script."""

    pass_threshold: Optional[float] = None
    """The threshold for the score."""


class TestingCriterionEvalGraderScoreModelInputContentInputTextContent(BaseModel):
    __test__ = False
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class TestingCriterionEvalGraderScoreModelInputContentOutputText(BaseModel):
    __test__ = False
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class TestingCriterionEvalGraderScoreModelInputContentInputImage(BaseModel):
    __test__ = False
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class TestingCriterionEvalGraderScoreModelInputContentInputAudioInputAudio(BaseModel):
    __test__ = False
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class TestingCriterionEvalGraderScoreModelInputContentInputAudio(BaseModel):
    __test__ = False
    input_audio: TestingCriterionEvalGraderScoreModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


TestingCriterionEvalGraderScoreModelInputContent: TypeAlias = Union[
    str,
    TestingCriterionEvalGraderScoreModelInputContentInputTextContent,
    TestingCriterionEvalGraderScoreModelInputContentOutputText,
    TestingCriterionEvalGraderScoreModelInputContentInputImage,
    TestingCriterionEvalGraderScoreModelInputContentInputAudio,
    List[object],
]


class TestingCriterionEvalGraderScoreModelInput(BaseModel):
    __test__ = False
    content: TestingCriterionEvalGraderScoreModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class TestingCriterionEvalGraderScoreModelSamplingParams(BaseModel):
    __test__ = False
    max_completions_tokens: Optional[int] = None
    """The maximum number of tokens the grader model may generate in its response."""

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

    top_p: Optional[float] = None
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class TestingCriterionEvalGraderScoreModel(BaseModel):
    __test__ = False
    input: List[TestingCriterionEvalGraderScoreModelInput]
    """The input text. This may include template strings."""

    model: str
    """The model to use for the evaluation."""

    name: str
    """The name of the grader."""

    type: Literal["score_model"]
    """The object type, which is always `score_model`."""

    pass_threshold: Optional[float] = None
    """The threshold for the score."""

    range: Optional[List[float]] = None
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: Optional[TestingCriterionEvalGraderScoreModelSamplingParams] = None
    """The sampling parameters for the model."""


TestingCriterion: TypeAlias = Union[
    TestingCriterionGraderLabelModel,
    TestingCriterionGraderStringCheck,
    TestingCriterionEvalGraderTextSimilarity,
    TestingCriterionEvalGraderPython,
    TestingCriterionEvalGraderScoreModel,
]


class EvalUpdateResponse(BaseModel):
    id: str
    """Unique identifier for the evaluation."""

    created_at: int
    """The Unix timestamp (in seconds) for when the eval was created."""

    data_source_config: DataSourceConfig
    """Configuration of data sources used in runs of the evaluation."""

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: str
    """The name of the evaluation."""

    object: Literal["eval"]
    """The object type."""

    testing_criteria: List[TestingCriterion]
    """A list of testing criteria."""
