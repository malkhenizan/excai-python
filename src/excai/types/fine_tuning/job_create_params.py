# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "JobCreateParams",
    "Hyperparameters",
    "Integration",
    "IntegrationWandb",
    "Method",
    "MethodDpo",
    "MethodDpoHyperparameters",
    "MethodReinforcement",
    "MethodReinforcementGrader",
    "MethodReinforcementGraderGraderStringCheck",
    "MethodReinforcementGraderGraderTextSimilarity",
    "MethodReinforcementGraderGraderPython",
    "MethodReinforcementGraderGraderScoreModel",
    "MethodReinforcementGraderGraderScoreModelInput",
    "MethodReinforcementGraderGraderScoreModelInputContent",
    "MethodReinforcementGraderGraderScoreModelInputContentInputTextContent",
    "MethodReinforcementGraderGraderScoreModelInputContentOutputText",
    "MethodReinforcementGraderGraderScoreModelInputContentInputImage",
    "MethodReinforcementGraderGraderScoreModelInputContentInputAudio",
    "MethodReinforcementGraderGraderScoreModelInputContentInputAudioInputAudio",
    "MethodReinforcementGraderGraderScoreModelSamplingParams",
    "MethodReinforcementGraderGraderMulti",
    "MethodReinforcementGraderGraderMultiGraders",
    "MethodReinforcementGraderGraderMultiGradersGraderStringCheck",
    "MethodReinforcementGraderGraderMultiGradersGraderTextSimilarity",
    "MethodReinforcementGraderGraderMultiGradersGraderPython",
    "MethodReinforcementGraderGraderMultiGradersGraderScoreModel",
    "MethodReinforcementGraderGraderMultiGradersGraderScoreModelInput",
    "MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContent",
    "MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputTextContent",
    "MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentOutputText",
    "MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputImage",
    "MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudio",
    "MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio",
    "MethodReinforcementGraderGraderMultiGradersGraderScoreModelSamplingParams",
    "MethodReinforcementGraderGraderMultiGradersGraderLabelModel",
    "MethodReinforcementGraderGraderMultiGradersGraderLabelModelInput",
    "MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContent",
    "MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputTextContent",
    "MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentOutputText",
    "MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputImage",
    "MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudio",
    "MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio",
    "MethodReinforcementHyperparameters",
    "MethodSupervised",
    "MethodSupervisedHyperparameters",
]


class JobCreateParams(TypedDict, total=False):
    model: Required[Union[str, Literal["babbage-002", "davinci-002", "gpt-3.5-turbo", "gpt-4o-mini"]]]
    """The name of the model to fine-tune.

    You can select one of the
    [supported models](https://platform.excai.com/docs/guides/fine-tuning#which-models-can-be-fine-tuned).
    """

    training_file: Required[str]
    """The ID of an uploaded file that contains training data.

    See [upload file](https://platform.excai.com/docs/api-reference/files/create)
    for how to upload a file.

    Your dataset must be formatted as a JSONL file. Additionally, you must upload
    your file with the purpose `fine-tune`.

    The contents of the file should differ depending on if the model uses the
    [chat](https://platform.excai.com/docs/api-reference/fine-tuning/chat-input),
    [completions](https://platform.excai.com/docs/api-reference/fine-tuning/completions-input)
    format, or if the fine-tuning method uses the
    [preference](https://platform.excai.com/docs/api-reference/fine-tuning/preference-input)
    format.

    See the
    [fine-tuning guide](https://platform.excai.com/docs/guides/model-optimization)
    for more details.
    """

    hyperparameters: Hyperparameters
    """
    The hyperparameters used for the fine-tuning job. This value is now deprecated
    in favor of `method`, and should be passed in under the `method` parameter.
    """

    integrations: Optional[Iterable[Integration]]
    """A list of integrations to enable for your fine-tuning job."""

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    method: Method
    """The method used for fine-tuning."""

    seed: Optional[int]
    """The seed controls the reproducibility of the job.

    Passing in the same seed and job parameters should produce the same results, but
    may differ in rare cases. If a seed is not specified, one will be generated for
    you.
    """

    suffix: Optional[str]
    """
    A string of up to 64 characters that will be added to your fine-tuned model
    name.

    For example, a `suffix` of "custom-model-name" would produce a model name like
    `ft:gpt-4o-mini:excai:custom-model-name:7p4lURel`.
    """

    validation_file: Optional[str]
    """The ID of an uploaded file that contains validation data.

    If you provide this file, the data is used to generate validation metrics
    periodically during fine-tuning. These metrics can be viewed in the fine-tuning
    results file. The same data should not be present in both train and validation
    files.

    Your dataset must be formatted as a JSONL file. You must upload your file with
    the purpose `fine-tune`.

    See the
    [fine-tuning guide](https://platform.excai.com/docs/guides/model-optimization)
    for more details.
    """


class Hyperparameters(TypedDict, total=False):
    batch_size: Union[Literal["auto"], int]
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    learning_rate_multiplier: Union[Literal["auto"], float]
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int]
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class IntegrationWandb(TypedDict, total=False):
    project: Required[str]
    """The name of the project that the new run will be created under."""

    entity: Optional[str]
    """The entity to use for the run.

    This allows you to set the team or username of the WandB user that you would
    like associated with the run. If not set, the default entity for the registered
    WandB API key is used.
    """

    name: Optional[str]
    """A display name to set for the run.

    If not set, we will use the Job ID as the name.
    """

    tags: SequenceNotStr[str]
    """A list of tags to be attached to the newly created run.

    These tags are passed through directly to WandB. Some default tags are generated
    by EXCai: "excai/finetune", "excai/{base-model}", "excai/{ftjob-abcdef}".
    """


class Integration(TypedDict, total=False):
    type: Required[Literal["wandb"]]
    """The type of integration to enable.

    Currently, only "wandb" (Weights and Biases) is supported.
    """

    wandb: Required[IntegrationWandb]
    """The settings for your integration with Weights and Biases.

    This payload specifies the project that metrics will be sent to. Optionally, you
    can set an explicit display name for your run, add tags to your run, and set a
    default entity (team, username, etc) to be associated with your run.
    """


class MethodDpoHyperparameters(TypedDict, total=False):
    batch_size: Union[Literal["auto"], int]
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    beta: Union[Literal["auto"], float]
    """The beta value for the DPO method.

    A higher beta value will increase the weight of the penalty between the policy
    and reference model.
    """

    learning_rate_multiplier: Union[Literal["auto"], float]
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int]
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class MethodDpo(TypedDict, total=False):
    hyperparameters: MethodDpoHyperparameters
    """The hyperparameters used for the DPO fine-tuning job."""


class MethodReinforcementGraderGraderStringCheck(TypedDict, total=False):
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


class MethodReinforcementGraderGraderTextSimilarity(TypedDict, total=False):
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


class MethodReinforcementGraderGraderPython(TypedDict, total=False):
    name: Required[str]
    """The name of the grader."""

    source: Required[str]
    """The source code of the python script."""

    type: Required[Literal["python"]]
    """The object type, which is always `python`."""

    image_tag: str
    """The image tag to use for the python script."""


class MethodReinforcementGraderGraderScoreModelInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class MethodReinforcementGraderGraderScoreModelInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class MethodReinforcementGraderGraderScoreModelInputContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class MethodReinforcementGraderGraderScoreModelInputContentInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class MethodReinforcementGraderGraderScoreModelInputContentInputAudio(TypedDict, total=False):
    input_audio: Required[MethodReinforcementGraderGraderScoreModelInputContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


MethodReinforcementGraderGraderScoreModelInputContent: TypeAlias = Union[
    str,
    MethodReinforcementGraderGraderScoreModelInputContentInputTextContent,
    MethodReinforcementGraderGraderScoreModelInputContentOutputText,
    MethodReinforcementGraderGraderScoreModelInputContentInputImage,
    MethodReinforcementGraderGraderScoreModelInputContentInputAudio,
    Iterable[object],
]


class MethodReinforcementGraderGraderScoreModelInput(TypedDict, total=False):
    content: Required[MethodReinforcementGraderGraderScoreModelInputContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class MethodReinforcementGraderGraderScoreModelSamplingParams(TypedDict, total=False):
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


class MethodReinforcementGraderGraderScoreModel(TypedDict, total=False):
    input: Required[Iterable[MethodReinforcementGraderGraderScoreModelInput]]
    """The input text. This may include template strings."""

    model: Required[str]
    """The model to use for the evaluation."""

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["score_model"]]
    """The object type, which is always `score_model`."""

    range: Iterable[float]
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: MethodReinforcementGraderGraderScoreModelSamplingParams
    """The sampling parameters for the model."""


class MethodReinforcementGraderGraderMultiGradersGraderStringCheck(TypedDict, total=False):
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


class MethodReinforcementGraderGraderMultiGradersGraderTextSimilarity(TypedDict, total=False):
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


class MethodReinforcementGraderGraderMultiGradersGraderPython(TypedDict, total=False):
    name: Required[str]
    """The name of the grader."""

    source: Required[str]
    """The source code of the python script."""

    type: Required[Literal["python"]]
    """The object type, which is always `python`."""

    image_tag: str
    """The image tag to use for the python script."""


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio(
    TypedDict, total=False
):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudio(TypedDict, total=False):
    input_audio: Required[MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContent: TypeAlias = Union[
    str,
    MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputTextContent,
    MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentOutputText,
    MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputImage,
    MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudio,
    Iterable[object],
]


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInput(TypedDict, total=False):
    content: Required[MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelSamplingParams(TypedDict, total=False):
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


class MethodReinforcementGraderGraderMultiGradersGraderScoreModel(TypedDict, total=False):
    input: Required[Iterable[MethodReinforcementGraderGraderMultiGradersGraderScoreModelInput]]
    """The input text. This may include template strings."""

    model: Required[str]
    """The model to use for the evaluation."""

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["score_model"]]
    """The object type, which is always `score_model`."""

    range: Iterable[float]
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: MethodReinforcementGraderGraderMultiGradersGraderScoreModelSamplingParams
    """The sampling parameters for the model."""


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentOutputText(TypedDict, total=False):
    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputImage(TypedDict, total=False):
    image_url: Required[str]
    """The URL of the image input."""

    type: Required[Literal["input_image"]]
    """The type of the image input. Always `input_image`."""

    detail: str
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio(
    TypedDict, total=False
):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudio(TypedDict, total=False):
    input_audio: Required[MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""


MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContent: TypeAlias = Union[
    str,
    MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputTextContent,
    MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentOutputText,
    MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputImage,
    MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudio,
    Iterable[object],
]


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInput(TypedDict, total=False):
    content: Required[MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContent]
    """Inputs to the model - can contain template strings."""

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class MethodReinforcementGraderGraderMultiGradersGraderLabelModel(TypedDict, total=False):
    input: Required[Iterable[MethodReinforcementGraderGraderMultiGradersGraderLabelModelInput]]

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


MethodReinforcementGraderGraderMultiGraders: TypeAlias = Union[
    MethodReinforcementGraderGraderMultiGradersGraderStringCheck,
    MethodReinforcementGraderGraderMultiGradersGraderTextSimilarity,
    MethodReinforcementGraderGraderMultiGradersGraderPython,
    MethodReinforcementGraderGraderMultiGradersGraderScoreModel,
    MethodReinforcementGraderGraderMultiGradersGraderLabelModel,
]


class MethodReinforcementGraderGraderMulti(TypedDict, total=False):
    calculate_output: Required[str]
    """A formula to calculate the output based on grader results."""

    graders: Required[MethodReinforcementGraderGraderMultiGraders]
    """
    A StringCheckGrader object that performs a string comparison between input and
    reference using a specified operation.
    """

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["multi"]]
    """The object type, which is always `multi`."""


MethodReinforcementGrader: TypeAlias = Union[
    MethodReinforcementGraderGraderStringCheck,
    MethodReinforcementGraderGraderTextSimilarity,
    MethodReinforcementGraderGraderPython,
    MethodReinforcementGraderGraderScoreModel,
    MethodReinforcementGraderGraderMulti,
]


class MethodReinforcementHyperparameters(TypedDict, total=False):
    batch_size: Union[Literal["auto"], int]
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    compute_multiplier: Union[Literal["auto"], float]
    """
    Multiplier on amount of compute used for exploring search space during training.
    """

    eval_interval: Union[Literal["auto"], int]
    """The number of training steps between evaluation runs."""

    eval_samples: Union[Literal["auto"], int]
    """Number of evaluation samples to generate per training step."""

    learning_rate_multiplier: Union[Literal["auto"], float]
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int]
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """

    reasoning_effort: Literal["default", "low", "medium", "high"]
    """Level of reasoning effort."""


class MethodReinforcement(TypedDict, total=False):
    grader: Required[MethodReinforcementGrader]
    """The grader used for the fine-tuning job."""

    hyperparameters: MethodReinforcementHyperparameters
    """The hyperparameters used for the reinforcement fine-tuning job."""


class MethodSupervisedHyperparameters(TypedDict, total=False):
    batch_size: Union[Literal["auto"], int]
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    learning_rate_multiplier: Union[Literal["auto"], float]
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int]
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class MethodSupervised(TypedDict, total=False):
    hyperparameters: MethodSupervisedHyperparameters
    """The hyperparameters used for the fine-tuning job."""


class Method(TypedDict, total=False):
    type: Required[Literal["supervised", "dpo", "reinforcement"]]
    """The type of method. Is either `supervised`, `dpo`, or `reinforcement`."""

    dpo: MethodDpo
    """Configuration for the DPO fine-tuning method."""

    reinforcement: MethodReinforcement
    """Configuration for the reinforcement fine-tuning method."""

    supervised: MethodSupervised
    """Configuration for the supervised fine-tuning method."""
