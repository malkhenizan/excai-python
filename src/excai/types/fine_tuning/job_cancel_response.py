# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "JobCancelResponse",
    "Error",
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


class Error(BaseModel):
    code: str
    """A machine-readable error code."""

    message: str
    """A human-readable error message."""

    param: Optional[str] = None
    """The parameter that was invalid, usually `training_file` or `validation_file`.

    This field will be null if the failure was not parameter-specific.
    """


class Hyperparameters(BaseModel):
    batch_size: Union[Literal["auto"], int, None] = None
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    learning_rate_multiplier: Union[Literal["auto"], float, None] = None
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int, None] = None
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class IntegrationWandb(BaseModel):
    project: str
    """The name of the project that the new run will be created under."""

    entity: Optional[str] = None
    """The entity to use for the run.

    This allows you to set the team or username of the WandB user that you would
    like associated with the run. If not set, the default entity for the registered
    WandB API key is used.
    """

    name: Optional[str] = None
    """A display name to set for the run.

    If not set, we will use the Job ID as the name.
    """

    tags: Optional[List[str]] = None
    """A list of tags to be attached to the newly created run.

    These tags are passed through directly to WandB. Some default tags are generated
    by EXCai: "excai/finetune", "excai/{base-model}", "excai/{ftjob-abcdef}".
    """


class Integration(BaseModel):
    type: Literal["wandb"]
    """The type of the integration being enabled for the fine-tuning job"""

    wandb: IntegrationWandb
    """The settings for your integration with Weights and Biases.

    This payload specifies the project that metrics will be sent to. Optionally, you
    can set an explicit display name for your run, add tags to your run, and set a
    default entity (team, username, etc) to be associated with your run.
    """


class MethodDpoHyperparameters(BaseModel):
    batch_size: Union[Literal["auto"], int, None] = None
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    beta: Union[Literal["auto"], float, None] = None
    """The beta value for the DPO method.

    A higher beta value will increase the weight of the penalty between the policy
    and reference model.
    """

    learning_rate_multiplier: Union[Literal["auto"], float, None] = None
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int, None] = None
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class MethodDpo(BaseModel):
    hyperparameters: Optional[MethodDpoHyperparameters] = None
    """The hyperparameters used for the DPO fine-tuning job."""


class MethodReinforcementGraderGraderStringCheck(BaseModel):
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


class MethodReinforcementGraderGraderTextSimilarity(BaseModel):
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


class MethodReinforcementGraderGraderPython(BaseModel):
    name: str
    """The name of the grader."""

    source: str
    """The source code of the python script."""

    type: Literal["python"]
    """The object type, which is always `python`."""

    image_tag: Optional[str] = None
    """The image tag to use for the python script."""


class MethodReinforcementGraderGraderScoreModelInputContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class MethodReinforcementGraderGraderScoreModelInputContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class MethodReinforcementGraderGraderScoreModelInputContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class MethodReinforcementGraderGraderScoreModelInputContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class MethodReinforcementGraderGraderScoreModelInputContentInputAudio(BaseModel):
    input_audio: MethodReinforcementGraderGraderScoreModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


MethodReinforcementGraderGraderScoreModelInputContent: TypeAlias = Union[
    str,
    MethodReinforcementGraderGraderScoreModelInputContentInputTextContent,
    MethodReinforcementGraderGraderScoreModelInputContentOutputText,
    MethodReinforcementGraderGraderScoreModelInputContentInputImage,
    MethodReinforcementGraderGraderScoreModelInputContentInputAudio,
    List[object],
]


class MethodReinforcementGraderGraderScoreModelInput(BaseModel):
    content: MethodReinforcementGraderGraderScoreModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class MethodReinforcementGraderGraderScoreModelSamplingParams(BaseModel):
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


class MethodReinforcementGraderGraderScoreModel(BaseModel):
    input: List[MethodReinforcementGraderGraderScoreModelInput]
    """The input text. This may include template strings."""

    model: str
    """The model to use for the evaluation."""

    name: str
    """The name of the grader."""

    type: Literal["score_model"]
    """The object type, which is always `score_model`."""

    range: Optional[List[float]] = None
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: Optional[MethodReinforcementGraderGraderScoreModelSamplingParams] = None
    """The sampling parameters for the model."""


class MethodReinforcementGraderGraderMultiGradersGraderStringCheck(BaseModel):
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


class MethodReinforcementGraderGraderMultiGradersGraderTextSimilarity(BaseModel):
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


class MethodReinforcementGraderGraderMultiGradersGraderPython(BaseModel):
    name: str
    """The name of the grader."""

    source: str
    """The source code of the python script."""

    type: Literal["python"]
    """The object type, which is always `python`."""

    image_tag: Optional[str] = None
    """The image tag to use for the python script."""


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudio(BaseModel):
    input_audio: MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContent: TypeAlias = Union[
    str,
    MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputTextContent,
    MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentOutputText,
    MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputImage,
    MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudio,
    List[object],
]


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelInput(BaseModel):
    content: MethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class MethodReinforcementGraderGraderMultiGradersGraderScoreModelSamplingParams(BaseModel):
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


class MethodReinforcementGraderGraderMultiGradersGraderScoreModel(BaseModel):
    input: List[MethodReinforcementGraderGraderMultiGradersGraderScoreModelInput]
    """The input text. This may include template strings."""

    model: str
    """The model to use for the evaluation."""

    name: str
    """The name of the grader."""

    type: Literal["score_model"]
    """The object type, which is always `score_model`."""

    range: Optional[List[float]] = None
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: Optional[MethodReinforcementGraderGraderMultiGradersGraderScoreModelSamplingParams] = None
    """The sampling parameters for the model."""


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudio(BaseModel):
    input_audio: MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContent: TypeAlias = Union[
    str,
    MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputTextContent,
    MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentOutputText,
    MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputImage,
    MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudio,
    List[object],
]


class MethodReinforcementGraderGraderMultiGradersGraderLabelModelInput(BaseModel):
    content: MethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class MethodReinforcementGraderGraderMultiGradersGraderLabelModel(BaseModel):
    input: List[MethodReinforcementGraderGraderMultiGradersGraderLabelModelInput]

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


MethodReinforcementGraderGraderMultiGraders: TypeAlias = Union[
    MethodReinforcementGraderGraderMultiGradersGraderStringCheck,
    MethodReinforcementGraderGraderMultiGradersGraderTextSimilarity,
    MethodReinforcementGraderGraderMultiGradersGraderPython,
    MethodReinforcementGraderGraderMultiGradersGraderScoreModel,
    MethodReinforcementGraderGraderMultiGradersGraderLabelModel,
]


class MethodReinforcementGraderGraderMulti(BaseModel):
    calculate_output: str
    """A formula to calculate the output based on grader results."""

    graders: MethodReinforcementGraderGraderMultiGraders
    """
    A StringCheckGrader object that performs a string comparison between input and
    reference using a specified operation.
    """

    name: str
    """The name of the grader."""

    type: Literal["multi"]
    """The object type, which is always `multi`."""


MethodReinforcementGrader: TypeAlias = Union[
    MethodReinforcementGraderGraderStringCheck,
    MethodReinforcementGraderGraderTextSimilarity,
    MethodReinforcementGraderGraderPython,
    MethodReinforcementGraderGraderScoreModel,
    MethodReinforcementGraderGraderMulti,
]


class MethodReinforcementHyperparameters(BaseModel):
    batch_size: Union[Literal["auto"], int, None] = None
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    compute_multiplier: Union[Literal["auto"], float, None] = None
    """
    Multiplier on amount of compute used for exploring search space during training.
    """

    eval_interval: Union[Literal["auto"], int, None] = None
    """The number of training steps between evaluation runs."""

    eval_samples: Union[Literal["auto"], int, None] = None
    """Number of evaluation samples to generate per training step."""

    learning_rate_multiplier: Union[Literal["auto"], float, None] = None
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int, None] = None
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """

    reasoning_effort: Optional[Literal["default", "low", "medium", "high"]] = None
    """Level of reasoning effort."""


class MethodReinforcement(BaseModel):
    grader: MethodReinforcementGrader
    """The grader used for the fine-tuning job."""

    hyperparameters: Optional[MethodReinforcementHyperparameters] = None
    """The hyperparameters used for the reinforcement fine-tuning job."""


class MethodSupervisedHyperparameters(BaseModel):
    batch_size: Union[Literal["auto"], int, None] = None
    """Number of examples in each batch.

    A larger batch size means that model parameters are updated less frequently, but
    with lower variance.
    """

    learning_rate_multiplier: Union[Literal["auto"], float, None] = None
    """Scaling factor for the learning rate.

    A smaller learning rate may be useful to avoid overfitting.
    """

    n_epochs: Union[Literal["auto"], int, None] = None
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class MethodSupervised(BaseModel):
    hyperparameters: Optional[MethodSupervisedHyperparameters] = None
    """The hyperparameters used for the fine-tuning job."""


class Method(BaseModel):
    type: Literal["supervised", "dpo", "reinforcement"]
    """The type of method. Is either `supervised`, `dpo`, or `reinforcement`."""

    dpo: Optional[MethodDpo] = None
    """Configuration for the DPO fine-tuning method."""

    reinforcement: Optional[MethodReinforcement] = None
    """Configuration for the reinforcement fine-tuning method."""

    supervised: Optional[MethodSupervised] = None
    """Configuration for the supervised fine-tuning method."""


class JobCancelResponse(BaseModel):
    id: str
    """The object identifier, which can be referenced in the API endpoints."""

    created_at: int
    """The Unix timestamp (in seconds) for when the fine-tuning job was created."""

    error: Optional[Error] = None
    """
    For fine-tuning jobs that have `failed`, this will contain more information on
    the cause of the failure.
    """

    fine_tuned_model: Optional[str] = None
    """The name of the fine-tuned model that is being created.

    The value will be null if the fine-tuning job is still running.
    """

    finished_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the fine-tuning job was finished.

    The value will be null if the fine-tuning job is still running.
    """

    hyperparameters: Hyperparameters
    """The hyperparameters used for the fine-tuning job.

    This value will only be returned when running `supervised` jobs.
    """

    model: str
    """The base model that is being fine-tuned."""

    object: Literal["fine_tuning.job"]
    """The object type, which is always "fine_tuning.job"."""

    organization_id: str
    """The organization that owns the fine-tuning job."""

    result_files: List[str]
    """The compiled results file ID(s) for the fine-tuning job.

    You can retrieve the results with the
    [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
    """

    seed: int
    """The seed used for the fine-tuning job."""

    status: Literal["validating_files", "queued", "running", "succeeded", "failed", "cancelled"]
    """
    The current status of the fine-tuning job, which can be either
    `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.
    """

    trained_tokens: Optional[int] = None
    """The total number of billable tokens processed by this fine-tuning job.

    The value will be null if the fine-tuning job is still running.
    """

    training_file: str
    """The file ID used for training.

    You can retrieve the training data with the
    [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
    """

    validation_file: Optional[str] = None
    """The file ID used for validation.

    You can retrieve the validation results with the
    [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
    """

    estimated_finish: Optional[int] = None
    """
    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to
    finish. The value will be null if the fine-tuning job is not running.
    """

    integrations: Optional[List[Integration]] = None
    """A list of integrations to enable for this fine-tuning job."""

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    method: Optional[Method] = None
    """The method used for fine-tuning."""
