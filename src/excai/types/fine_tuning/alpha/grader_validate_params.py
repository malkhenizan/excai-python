# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "GraderValidateParams",
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


class GraderValidateParams(TypedDict, total=False):
    grader: Required[Grader]
    """The grader used for the fine-tuning job."""


class GraderGraderStringCheck(TypedDict, total=False):
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


class GraderGraderTextSimilarity(TypedDict, total=False):
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

    reference: Required[str]
    """The text being graded against."""

    type: Required[Literal["text_similarity"]]
    """The type of grader."""


class GraderGraderPython(TypedDict, total=False):
    name: Required[str]
    """The name of the grader."""

    source: Required[str]
    """The source code of the python script."""

    type: Required[Literal["python"]]
    """The object type, which is always `python`."""

    image_tag: str
    """The image tag to use for the python script."""


class GraderGraderScoreModelInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class GraderGraderScoreModelInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class GraderGraderScoreModelInputContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class GraderGraderScoreModelInputContentInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class GraderGraderScoreModelInputContentInputAudio(TypedDict, total=False):
    input_audio: Required[GraderGraderScoreModelInputContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


GraderGraderScoreModelInputContent: TypeAlias = Union[
    str,
    GraderGraderScoreModelInputContentInputTextContent,
    GraderGraderScoreModelInputContentOutputText,
    GraderGraderScoreModelInputContentInputImage,
    GraderGraderScoreModelInputContentInputAudio,
    Iterable[object],
]


class GraderGraderScoreModelInput(TypedDict, total=False):
    content: Required[GraderGraderScoreModelInputContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class GraderGraderScoreModelSamplingParams(TypedDict, total=False):
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


class GraderGraderScoreModel(TypedDict, total=False):
    input: Required[Iterable[GraderGraderScoreModelInput]]
    """The input text. This may include template strings."""

    model: Required[str]
    """The model to use for the evaluation."""

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["score_model"]]
    """The object type, which is always `score_model`."""

    range: Iterable[float]
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: GraderGraderScoreModelSamplingParams
    """The sampling parameters for the model."""


class GraderGraderMultiGradersGraderStringCheck(TypedDict, total=False):
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


class GraderGraderMultiGradersGraderTextSimilarity(TypedDict, total=False):
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

    reference: Required[str]
    """The text being graded against."""

    type: Required[Literal["text_similarity"]]
    """The type of grader."""


class GraderGraderMultiGradersGraderPython(TypedDict, total=False):
    name: Required[str]
    """The name of the grader."""

    source: Required[str]
    """The source code of the python script."""

    type: Required[Literal["python"]]
    """The object type, which is always `python`."""

    image_tag: str
    """The image tag to use for the python script."""


class GraderGraderMultiGradersGraderScoreModelInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class GraderGraderMultiGradersGraderScoreModelInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class GraderGraderMultiGradersGraderScoreModelInputContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class GraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class GraderGraderMultiGradersGraderScoreModelInputContentInputAudio(TypedDict, total=False):
    input_audio: Required[GraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


GraderGraderMultiGradersGraderScoreModelInputContent: TypeAlias = Union[
    str,
    GraderGraderMultiGradersGraderScoreModelInputContentInputTextContent,
    GraderGraderMultiGradersGraderScoreModelInputContentOutputText,
    GraderGraderMultiGradersGraderScoreModelInputContentInputImage,
    GraderGraderMultiGradersGraderScoreModelInputContentInputAudio,
    Iterable[object],
]


class GraderGraderMultiGradersGraderScoreModelInput(TypedDict, total=False):
    content: Required[GraderGraderMultiGradersGraderScoreModelInputContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class GraderGraderMultiGradersGraderScoreModelSamplingParams(TypedDict, total=False):
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


class GraderGraderMultiGradersGraderScoreModel(TypedDict, total=False):
    input: Required[Iterable[GraderGraderMultiGradersGraderScoreModelInput]]
    """The input text. This may include template strings."""

    model: Required[str]
    """The model to use for the evaluation."""

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["score_model"]]
    """The object type, which is always `score_model`."""

    range: Iterable[float]
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: GraderGraderMultiGradersGraderScoreModelSamplingParams
    """The sampling parameters for the model."""


class GraderGraderMultiGradersGraderLabelModelInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class GraderGraderMultiGradersGraderLabelModelInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class GraderGraderMultiGradersGraderLabelModelInputContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class GraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class GraderGraderMultiGradersGraderLabelModelInputContentInputAudio(TypedDict, total=False):
    input_audio: Required[GraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


GraderGraderMultiGradersGraderLabelModelInputContent: TypeAlias = Union[
    str,
    GraderGraderMultiGradersGraderLabelModelInputContentInputTextContent,
    GraderGraderMultiGradersGraderLabelModelInputContentOutputText,
    GraderGraderMultiGradersGraderLabelModelInputContentInputImage,
    GraderGraderMultiGradersGraderLabelModelInputContentInputAudio,
    Iterable[object],
]


class GraderGraderMultiGradersGraderLabelModelInput(TypedDict, total=False):
    content: Required[GraderGraderMultiGradersGraderLabelModelInputContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class GraderGraderMultiGradersGraderLabelModel(TypedDict, total=False):
    input: Required[Iterable[GraderGraderMultiGradersGraderLabelModelInput]]

    labels: Required[SequenceNotStr[str]]
    """The labels to assign to each item in the evaluation."""

    model: Required[str]
    """The model to use for the evaluation. Must support structured outputs."""

    name: Required[str]
    """The name of the grader."""

    passing_labels: Required[SequenceNotStr[str]]
    """The labels that indicate a passing result. Must be a subset of labels."""

    type: Required[Literal["label_model"]]
    """The object type, which is always `label_model`."""


GraderGraderMultiGraders: TypeAlias = Union[
    GraderGraderMultiGradersGraderStringCheck,
    GraderGraderMultiGradersGraderTextSimilarity,
    GraderGraderMultiGradersGraderPython,
    GraderGraderMultiGradersGraderScoreModel,
    GraderGraderMultiGradersGraderLabelModel,
]


class GraderGraderMulti(TypedDict, total=False):
    calculate_output: Required[str]
    """A formula to calculate the output based on grader results."""

    graders: Required[GraderGraderMultiGraders]
    """
    A StringCheckGrader object that performs a string comparison between input and
    reference using a specified operation.
    """

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["multi"]]
    """The object type, which is always `multi`."""


Grader: TypeAlias = Union[
    GraderGraderStringCheck, GraderGraderTextSimilarity, GraderGraderPython, GraderGraderScoreModel, GraderGraderMulti
]
