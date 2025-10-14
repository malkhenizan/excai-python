# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "GraderValidateResponse",
    "Grader",
    "GraderGraderStringCheck",
    "GraderGraderTextSimilarity",
    "GraderGraderPython",
    "GraderGraderScoreModel",
    "GraderGraderScoreModelInput",
    "GraderGraderScoreModelInputContent",
    "GraderGraderScoreModelInputContentInputTextContent",
    "GraderGraderScoreModelInputContentOutputText",
    "GraderGraderScoreModelInputContentInputImage",
    "GraderGraderScoreModelInputContentInputAudio",
    "GraderGraderScoreModelInputContentInputAudioInputAudio",
    "GraderGraderScoreModelSamplingParams",
    "GraderGraderMulti",
    "GraderGraderMultiGraders",
    "GraderGraderMultiGradersGraderStringCheck",
    "GraderGraderMultiGradersGraderTextSimilarity",
    "GraderGraderMultiGradersGraderPython",
    "GraderGraderMultiGradersGraderScoreModel",
    "GraderGraderMultiGradersGraderScoreModelInput",
    "GraderGraderMultiGradersGraderScoreModelInputContent",
    "GraderGraderMultiGradersGraderScoreModelInputContentInputTextContent",
    "GraderGraderMultiGradersGraderScoreModelInputContentOutputText",
    "GraderGraderMultiGradersGraderScoreModelInputContentInputImage",
    "GraderGraderMultiGradersGraderScoreModelInputContentInputAudio",
    "GraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio",
    "GraderGraderMultiGradersGraderScoreModelSamplingParams",
    "GraderGraderMultiGradersGraderLabelModel",
    "GraderGraderMultiGradersGraderLabelModelInput",
    "GraderGraderMultiGradersGraderLabelModelInputContent",
    "GraderGraderMultiGradersGraderLabelModelInputContentInputTextContent",
    "GraderGraderMultiGradersGraderLabelModelInputContentOutputText",
    "GraderGraderMultiGradersGraderLabelModelInputContentInputImage",
    "GraderGraderMultiGradersGraderLabelModelInputContentInputAudio",
    "GraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio",
]


class GraderGraderStringCheck(BaseModel):
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


class GraderGraderTextSimilarity(BaseModel):
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

    reference: str
    """The text being graded against."""

    type: Literal["text_similarity"]
    """The type of grader."""


class GraderGraderPython(BaseModel):
    name: str
    """The name of the grader."""

    source: str
    """The source code of the python script."""

    type: Literal["python"]
    """The object type, which is always `python`."""

    image_tag: Optional[str] = None
    """The image tag to use for the python script."""


class GraderGraderScoreModelInputContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class GraderGraderScoreModelInputContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class GraderGraderScoreModelInputContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class GraderGraderScoreModelInputContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class GraderGraderScoreModelInputContentInputAudio(BaseModel):
    input_audio: GraderGraderScoreModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


GraderGraderScoreModelInputContent: TypeAlias = Union[
    str,
    GraderGraderScoreModelInputContentInputTextContent,
    GraderGraderScoreModelInputContentOutputText,
    GraderGraderScoreModelInputContentInputImage,
    GraderGraderScoreModelInputContentInputAudio,
    List[object],
]


class GraderGraderScoreModelInput(BaseModel):
    content: GraderGraderScoreModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class GraderGraderScoreModelSamplingParams(BaseModel):
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


class GraderGraderScoreModel(BaseModel):
    input: List[GraderGraderScoreModelInput]
    """The input text. This may include template strings."""

    model: str
    """The model to use for the evaluation."""

    name: str
    """The name of the grader."""

    type: Literal["score_model"]
    """The object type, which is always `score_model`."""

    range: Optional[List[float]] = None
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: Optional[GraderGraderScoreModelSamplingParams] = None
    """The sampling parameters for the model."""


class GraderGraderMultiGradersGraderStringCheck(BaseModel):
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


class GraderGraderMultiGradersGraderTextSimilarity(BaseModel):
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

    reference: str
    """The text being graded against."""

    type: Literal["text_similarity"]
    """The type of grader."""


class GraderGraderMultiGradersGraderPython(BaseModel):
    name: str
    """The name of the grader."""

    source: str
    """The source code of the python script."""

    type: Literal["python"]
    """The object type, which is always `python`."""

    image_tag: Optional[str] = None
    """The image tag to use for the python script."""


class GraderGraderMultiGradersGraderScoreModelInputContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class GraderGraderMultiGradersGraderScoreModelInputContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class GraderGraderMultiGradersGraderScoreModelInputContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class GraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class GraderGraderMultiGradersGraderScoreModelInputContentInputAudio(BaseModel):
    input_audio: GraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


GraderGraderMultiGradersGraderScoreModelInputContent: TypeAlias = Union[
    str,
    GraderGraderMultiGradersGraderScoreModelInputContentInputTextContent,
    GraderGraderMultiGradersGraderScoreModelInputContentOutputText,
    GraderGraderMultiGradersGraderScoreModelInputContentInputImage,
    GraderGraderMultiGradersGraderScoreModelInputContentInputAudio,
    List[object],
]


class GraderGraderMultiGradersGraderScoreModelInput(BaseModel):
    content: GraderGraderMultiGradersGraderScoreModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class GraderGraderMultiGradersGraderScoreModelSamplingParams(BaseModel):
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


class GraderGraderMultiGradersGraderScoreModel(BaseModel):
    input: List[GraderGraderMultiGradersGraderScoreModelInput]
    """The input text. This may include template strings."""

    model: str
    """The model to use for the evaluation."""

    name: str
    """The name of the grader."""

    type: Literal["score_model"]
    """The object type, which is always `score_model`."""

    range: Optional[List[float]] = None
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: Optional[GraderGraderMultiGradersGraderScoreModelSamplingParams] = None
    """The sampling parameters for the model."""


class GraderGraderMultiGradersGraderLabelModelInputContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class GraderGraderMultiGradersGraderLabelModelInputContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class GraderGraderMultiGradersGraderLabelModelInputContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class GraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class GraderGraderMultiGradersGraderLabelModelInputContentInputAudio(BaseModel):
    input_audio: GraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


GraderGraderMultiGradersGraderLabelModelInputContent: TypeAlias = Union[
    str,
    GraderGraderMultiGradersGraderLabelModelInputContentInputTextContent,
    GraderGraderMultiGradersGraderLabelModelInputContentOutputText,
    GraderGraderMultiGradersGraderLabelModelInputContentInputImage,
    GraderGraderMultiGradersGraderLabelModelInputContentInputAudio,
    List[object],
]


class GraderGraderMultiGradersGraderLabelModelInput(BaseModel):
    content: GraderGraderMultiGradersGraderLabelModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class GraderGraderMultiGradersGraderLabelModel(BaseModel):
    input: List[GraderGraderMultiGradersGraderLabelModelInput]

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


GraderGraderMultiGraders: TypeAlias = Union[
    GraderGraderMultiGradersGraderStringCheck,
    GraderGraderMultiGradersGraderTextSimilarity,
    GraderGraderMultiGradersGraderPython,
    GraderGraderMultiGradersGraderScoreModel,
    GraderGraderMultiGradersGraderLabelModel,
]


class GraderGraderMulti(BaseModel):
    calculate_output: str
    """A formula to calculate the output based on grader results."""

    graders: GraderGraderMultiGraders
    """
    A StringCheckGrader object that performs a string comparison between input and
    reference using a specified operation.
    """

    name: str
    """The name of the grader."""

    type: Literal["multi"]
    """The object type, which is always `multi`."""


Grader: TypeAlias = Union[
    GraderGraderStringCheck, GraderGraderTextSimilarity, GraderGraderPython, GraderGraderScoreModel, GraderGraderMulti
]


class GraderValidateResponse(BaseModel):
    grader: Optional[Grader] = None
    """The grader used for the fine-tuning job."""
