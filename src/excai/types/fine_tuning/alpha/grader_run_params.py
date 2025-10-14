# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "GraderRunParams",
    "Grader",
    "GraderStringCheck",
    "GraderTextSimilarity",
    "GraderPython",
    "GraderScoreModel",
    "GraderScoreModelInput",
    "GraderScoreModelInputContent",
    "GraderScoreModelInputContentInputTextContent",
    "GraderScoreModelInputContentOutputText",
    "GraderScoreModelInputContentInputImage",
    "GraderScoreModelInputContentInputAudio",
    "GraderScoreModelInputContentInputAudioInputAudio",
    "GraderScoreModelSamplingParams",
    "GraderMulti",
    "GraderMultiGraders",
    "GraderMultiGradersGraderStringCheck",
    "GraderMultiGradersGraderTextSimilarity",
    "GraderMultiGradersGraderPython",
    "GraderMultiGradersGraderScoreModel",
    "GraderMultiGradersGraderScoreModelInput",
    "GraderMultiGradersGraderScoreModelInputContent",
    "GraderMultiGradersGraderScoreModelInputContentInputTextContent",
    "GraderMultiGradersGraderScoreModelInputContentOutputText",
    "GraderMultiGradersGraderScoreModelInputContentInputImage",
    "GraderMultiGradersGraderScoreModelInputContentInputAudio",
    "GraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio",
    "GraderMultiGradersGraderScoreModelSamplingParams",
    "GraderMultiGradersGraderLabelModel",
    "GraderMultiGradersGraderLabelModelInput",
    "GraderMultiGradersGraderLabelModelInputContent",
    "GraderMultiGradersGraderLabelModelInputContentInputTextContent",
    "GraderMultiGradersGraderLabelModelInputContentOutputText",
    "GraderMultiGradersGraderLabelModelInputContentInputImage",
    "GraderMultiGradersGraderLabelModelInputContentInputAudio",
    "GraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio",
]


class GraderRunParams(TypedDict, total=False):
    grader: Required[Grader]
    """The grader used for the fine-tuning job."""

    model_sample: Required[str]
    """The model sample to be evaluated.

    This value will be used to populate the `sample` namespace. See
    [the guide](https://platform.excai.com/docs/guides/graders) for more details.
    The `output_json` variable will be populated if the model sample is a valid JSON
    string.
    """

    item: object
    """The dataset item provided to the grader.

    This will be used to populate the `item` namespace. See
    [the guide](https://platform.excai.com/docs/guides/graders) for more details.
    """


class GraderStringCheck(TypedDict, total=False):
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


class GraderTextSimilarity(TypedDict, total=False):
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


class GraderPython(TypedDict, total=False):
    name: Required[str]
    """The name of the grader."""

    source: Required[str]
    """The source code of the python script."""

    type: Required[Literal["python"]]
    """The object type, which is always `python`."""

    image_tag: str
    """The image tag to use for the python script."""


class GraderScoreModelInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class GraderScoreModelInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class GraderScoreModelInputContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class GraderScoreModelInputContentInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class GraderScoreModelInputContentInputAudio(TypedDict, total=False):
    input_audio: Required[GraderScoreModelInputContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


GraderScoreModelInputContent: TypeAlias = Union[
    str,
    GraderScoreModelInputContentInputTextContent,
    GraderScoreModelInputContentOutputText,
    GraderScoreModelInputContentInputImage,
    GraderScoreModelInputContentInputAudio,
    Iterable[object],
]


class GraderScoreModelInput(TypedDict, total=False):
    content: Required[GraderScoreModelInputContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class GraderScoreModelSamplingParams(TypedDict, total=False):
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


class GraderScoreModel(TypedDict, total=False):
    input: Required[Iterable[GraderScoreModelInput]]
    """The input text. This may include template strings."""

    model: Required[str]
    """The model to use for the evaluation."""

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["score_model"]]
    """The object type, which is always `score_model`."""

    range: Iterable[float]
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: GraderScoreModelSamplingParams
    """The sampling parameters for the model."""


class GraderMultiGradersGraderStringCheck(TypedDict, total=False):
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


class GraderMultiGradersGraderTextSimilarity(TypedDict, total=False):
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


class GraderMultiGradersGraderPython(TypedDict, total=False):
    name: Required[str]
    """The name of the grader."""

    source: Required[str]
    """The source code of the python script."""

    type: Required[Literal["python"]]
    """The object type, which is always `python`."""

    image_tag: str
    """The image tag to use for the python script."""


class GraderMultiGradersGraderScoreModelInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class GraderMultiGradersGraderScoreModelInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class GraderMultiGradersGraderScoreModelInputContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class GraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class GraderMultiGradersGraderScoreModelInputContentInputAudio(TypedDict, total=False):
    input_audio: Required[GraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


GraderMultiGradersGraderScoreModelInputContent: TypeAlias = Union[
    str,
    GraderMultiGradersGraderScoreModelInputContentInputTextContent,
    GraderMultiGradersGraderScoreModelInputContentOutputText,
    GraderMultiGradersGraderScoreModelInputContentInputImage,
    GraderMultiGradersGraderScoreModelInputContentInputAudio,
    Iterable[object],
]


class GraderMultiGradersGraderScoreModelInput(TypedDict, total=False):
    content: Required[GraderMultiGradersGraderScoreModelInputContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class GraderMultiGradersGraderScoreModelSamplingParams(TypedDict, total=False):
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


class GraderMultiGradersGraderScoreModel(TypedDict, total=False):
    input: Required[Iterable[GraderMultiGradersGraderScoreModelInput]]
    """The input text. This may include template strings."""

    model: Required[str]
    """The model to use for the evaluation."""

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["score_model"]]
    """The object type, which is always `score_model`."""

    range: Iterable[float]
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: GraderMultiGradersGraderScoreModelSamplingParams
    """The sampling parameters for the model."""


class GraderMultiGradersGraderLabelModelInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class GraderMultiGradersGraderLabelModelInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class GraderMultiGradersGraderLabelModelInputContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class GraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class GraderMultiGradersGraderLabelModelInputContentInputAudio(TypedDict, total=False):
    input_audio: Required[GraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


GraderMultiGradersGraderLabelModelInputContent: TypeAlias = Union[
    str,
    GraderMultiGradersGraderLabelModelInputContentInputTextContent,
    GraderMultiGradersGraderLabelModelInputContentOutputText,
    GraderMultiGradersGraderLabelModelInputContentInputImage,
    GraderMultiGradersGraderLabelModelInputContentInputAudio,
    Iterable[object],
]


class GraderMultiGradersGraderLabelModelInput(TypedDict, total=False):
    content: Required[GraderMultiGradersGraderLabelModelInputContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class GraderMultiGradersGraderLabelModel(TypedDict, total=False):
    input: Required[Iterable[GraderMultiGradersGraderLabelModelInput]]

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


GraderMultiGraders: TypeAlias = Union[
    GraderMultiGradersGraderStringCheck,
    GraderMultiGradersGraderTextSimilarity,
    GraderMultiGradersGraderPython,
    GraderMultiGradersGraderScoreModel,
    GraderMultiGradersGraderLabelModel,
]


class GraderMulti(TypedDict, total=False):
    calculate_output: Required[str]
    """A formula to calculate the output based on grader results."""

    graders: Required[GraderMultiGraders]
    """
    A StringCheckGrader object that performs a string comparison between input and
    reference using a specified operation.
    """

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["multi"]]
    """The object type, which is always `multi`."""


Grader: TypeAlias = Union[GraderStringCheck, GraderTextSimilarity, GraderPython, GraderScoreModel, GraderMulti]
