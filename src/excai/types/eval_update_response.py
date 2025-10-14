# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "EvalUpdateResponse",
    "DataSourceConfig",
    "DataSourceConfigEvalCustomDataSourceConfig",
    "DataSourceConfigEvalStoredCompletionsDataSourceConfig",
    "TestingCriterion",
    "TestingCriterionEvalLabelModelGrader",
    "TestingCriterionEvalLabelModelGraderInput",
    "TestingCriterionEvalLabelModelGraderInputContent",
    "TestingCriterionEvalLabelModelGraderInputContentInputTextContent",
    "TestingCriterionEvalLabelModelGraderInputContentOutputText",
    "TestingCriterionEvalStringCheckGrader",
    "TestingCriterionEvalTextSimilarityGrader",
    "TestingCriterionEvalPythonGrader",
    "TestingCriterionEvalScoreModelGrader",
    "TestingCriterionEvalScoreModelGraderInput",
    "TestingCriterionEvalScoreModelGraderInputContent",
    "TestingCriterionEvalScoreModelGraderInputContentInputTextContent",
    "TestingCriterionEvalScoreModelGraderInputContentOutputText",
]


class DataSourceConfigEvalCustomDataSourceConfig(BaseModel):
    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """
    The json schema for the run data source items. Learn how to build JSON schemas
    [here](https://json-schema.org/).
    """

    type: Literal["custom"]
    """The type of data source. Always `custom`."""


class DataSourceConfigEvalStoredCompletionsDataSourceConfig(BaseModel):
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


DataSourceConfig: TypeAlias = Union[
    DataSourceConfigEvalCustomDataSourceConfig, DataSourceConfigEvalStoredCompletionsDataSourceConfig
]


class TestingCriterionEvalLabelModelGraderInputContentInputTextContent(BaseModel):
    __test__ = False
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class TestingCriterionEvalLabelModelGraderInputContentOutputText(BaseModel):
    __test__ = False
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


TestingCriterionEvalLabelModelGraderInputContent: TypeAlias = Union[
    str,
    TestingCriterionEvalLabelModelGraderInputContentInputTextContent,
    TestingCriterionEvalLabelModelGraderInputContentOutputText,
]


class TestingCriterionEvalLabelModelGraderInput(BaseModel):
    __test__ = False
    content: TestingCriterionEvalLabelModelGraderInputContent
    """Text inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class TestingCriterionEvalLabelModelGrader(BaseModel):
    __test__ = False
    input: List[TestingCriterionEvalLabelModelGraderInput]

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


class TestingCriterionEvalStringCheckGrader(BaseModel):
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


class TestingCriterionEvalTextSimilarityGrader(BaseModel):
    __test__ = False
    evaluation_metric: Literal[
        "fuzzy_match", "bleu", "gleu", "meteor", "rouge_1", "rouge_2", "rouge_3", "rouge_4", "rouge_5", "rouge_l"
    ]
    """The evaluation metric to use.

    One of `fuzzy_match`, `bleu`, `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`,
    `rouge_4`, `rouge_5`, or `rouge_l`.
    """

    input: str
    """The text being graded."""

    pass_threshold: float
    """A float score where a value greater than or equal indicates a passing grade."""

    reference: str
    """The text being graded against."""

    type: Literal["text_similarity"]
    """The type of grader."""

    name: Optional[str] = None
    """The name of the grader."""


class TestingCriterionEvalPythonGrader(BaseModel):
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


class TestingCriterionEvalScoreModelGraderInputContentInputTextContent(BaseModel):
    __test__ = False
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class TestingCriterionEvalScoreModelGraderInputContentOutputText(BaseModel):
    __test__ = False
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


TestingCriterionEvalScoreModelGraderInputContent: TypeAlias = Union[
    str,
    TestingCriterionEvalScoreModelGraderInputContentInputTextContent,
    TestingCriterionEvalScoreModelGraderInputContentOutputText,
]


class TestingCriterionEvalScoreModelGraderInput(BaseModel):
    __test__ = False
    content: TestingCriterionEvalScoreModelGraderInputContent
    """Text inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class TestingCriterionEvalScoreModelGrader(BaseModel):
    __test__ = False
    input: List[TestingCriterionEvalScoreModelGraderInput]
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

    sampling_params: Optional[object] = None
    """The sampling parameters for the model."""


TestingCriterion: TypeAlias = Union[
    TestingCriterionEvalLabelModelGrader,
    TestingCriterionEvalStringCheckGrader,
    TestingCriterionEvalTextSimilarityGrader,
    TestingCriterionEvalPythonGrader,
    TestingCriterionEvalScoreModelGrader,
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
