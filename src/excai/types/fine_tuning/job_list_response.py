# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "JobListResponse",
    "Data",
    "DataError",
    "DataHyperparameters",
    "DataIntegration",
    "DataIntegrationWandb",
    "DataMethod",
    "DataMethodDpo",
    "DataMethodDpoHyperparameters",
    "DataMethodReinforcement",
    "DataMethodReinforcementGrader",
    "DataMethodReinforcementGraderGraderStringCheck",
    "DataMethodReinforcementGraderGraderTextSimilarity",
    "DataMethodReinforcementGraderGraderPython",
    "DataMethodReinforcementGraderGraderScoreModel",
    "DataMethodReinforcementGraderGraderScoreModelInput",
    "DataMethodReinforcementGraderGraderScoreModelInputContent",
    "DataMethodReinforcementGraderGraderScoreModelInputContentInputTextContent",
    "DataMethodReinforcementGraderGraderScoreModelInputContentOutputText",
    "DataMethodReinforcementGraderGraderScoreModelInputContentInputImage",
    "DataMethodReinforcementGraderGraderScoreModelInputContentInputAudio",
    "DataMethodReinforcementGraderGraderScoreModelInputContentInputAudioInputAudio",
    "DataMethodReinforcementGraderGraderScoreModelSamplingParams",
    "DataMethodReinforcementGraderGraderMulti",
    "DataMethodReinforcementGraderGraderMultiGraders",
    "DataMethodReinforcementGraderGraderMultiGradersGraderStringCheck",
    "DataMethodReinforcementGraderGraderMultiGradersGraderTextSimilarity",
    "DataMethodReinforcementGraderGraderMultiGradersGraderPython",
    "DataMethodReinforcementGraderGraderMultiGradersGraderScoreModel",
    "DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInput",
    "DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContent",
    "DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputTextContent",
    "DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentOutputText",
    "DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputImage",
    "DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudio",
    "DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio",
    "DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelSamplingParams",
    "DataMethodReinforcementGraderGraderMultiGradersGraderLabelModel",
    "DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInput",
    "DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContent",
    "DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputTextContent",
    "DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentOutputText",
    "DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputImage",
    "DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudio",
    "DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio",
    "DataMethodReinforcementHyperparameters",
    "DataMethodSupervised",
    "DataMethodSupervisedHyperparameters",
]


class DataError(BaseModel):
    code: str
    """A machine-readable error code."""

    message: str
    """A human-readable error message."""

    param: Optional[str] = None
    """The parameter that was invalid, usually `training_file` or `validation_file`.

    This field will be null if the failure was not parameter-specific.
    """


class DataHyperparameters(BaseModel):
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


class DataIntegrationWandb(BaseModel):
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


class DataIntegration(BaseModel):
    type: Literal["wandb"]
    """The type of the integration being enabled for the fine-tuning job"""

    wandb: DataIntegrationWandb
    """The settings for your integration with Weights and Biases.

    This payload specifies the project that metrics will be sent to. Optionally, you
    can set an explicit display name for your run, add tags to your run, and set a
    default entity (team, username, etc) to be associated with your run.
    """


class DataMethodDpoHyperparameters(BaseModel):
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


class DataMethodDpo(BaseModel):
    hyperparameters: Optional[DataMethodDpoHyperparameters] = None
    """The hyperparameters used for the DPO fine-tuning job."""


class DataMethodReinforcementGraderGraderStringCheck(BaseModel):
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


class DataMethodReinforcementGraderGraderTextSimilarity(BaseModel):
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


class DataMethodReinforcementGraderGraderPython(BaseModel):
    name: str
    """The name of the grader."""

    source: str
    """The source code of the python script."""

    type: Literal["python"]
    """The object type, which is always `python`."""

    image_tag: Optional[str] = None
    """The image tag to use for the python script."""


class DataMethodReinforcementGraderGraderScoreModelInputContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataMethodReinforcementGraderGraderScoreModelInputContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class DataMethodReinforcementGraderGraderScoreModelInputContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class DataMethodReinforcementGraderGraderScoreModelInputContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class DataMethodReinforcementGraderGraderScoreModelInputContentInputAudio(BaseModel):
    input_audio: DataMethodReinforcementGraderGraderScoreModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


DataMethodReinforcementGraderGraderScoreModelInputContent: TypeAlias = Union[
    str,
    DataMethodReinforcementGraderGraderScoreModelInputContentInputTextContent,
    DataMethodReinforcementGraderGraderScoreModelInputContentOutputText,
    DataMethodReinforcementGraderGraderScoreModelInputContentInputImage,
    DataMethodReinforcementGraderGraderScoreModelInputContentInputAudio,
    List[object],
]


class DataMethodReinforcementGraderGraderScoreModelInput(BaseModel):
    content: DataMethodReinforcementGraderGraderScoreModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class DataMethodReinforcementGraderGraderScoreModelSamplingParams(BaseModel):
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


class DataMethodReinforcementGraderGraderScoreModel(BaseModel):
    input: List[DataMethodReinforcementGraderGraderScoreModelInput]
    """The input text. This may include template strings."""

    model: str
    """The model to use for the evaluation."""

    name: str
    """The name of the grader."""

    type: Literal["score_model"]
    """The object type, which is always `score_model`."""

    range: Optional[List[float]] = None
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: Optional[DataMethodReinforcementGraderGraderScoreModelSamplingParams] = None
    """The sampling parameters for the model."""


class DataMethodReinforcementGraderGraderMultiGradersGraderStringCheck(BaseModel):
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


class DataMethodReinforcementGraderGraderMultiGradersGraderTextSimilarity(BaseModel):
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


class DataMethodReinforcementGraderGraderMultiGradersGraderPython(BaseModel):
    name: str
    """The name of the grader."""

    source: str
    """The source code of the python script."""

    type: Literal["python"]
    """The object type, which is always `python`."""

    image_tag: Optional[str] = None
    """The image tag to use for the python script."""


class DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudio(BaseModel):
    input_audio: DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContent: TypeAlias = Union[
    str,
    DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputTextContent,
    DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentOutputText,
    DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputImage,
    DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContentInputAudio,
    List[object],
]


class DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInput(BaseModel):
    content: DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelSamplingParams(BaseModel):
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


class DataMethodReinforcementGraderGraderMultiGradersGraderScoreModel(BaseModel):
    input: List[DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelInput]
    """The input text. This may include template strings."""

    model: str
    """The model to use for the evaluation."""

    name: str
    """The name of the grader."""

    type: Literal["score_model"]
    """The object type, which is always `score_model`."""

    range: Optional[List[float]] = None
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: Optional[DataMethodReinforcementGraderGraderMultiGradersGraderScoreModelSamplingParams] = None
    """The sampling parameters for the model."""


class DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentOutputText(BaseModel):
    text: str
    """The text output from the model."""

    type: Literal["output_text"]
    """The type of the output text. Always `output_text`."""


class DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputImage(BaseModel):
    image_url: str
    """The URL of the image input."""

    type: Literal["input_image"]
    """The type of the image input. Always `input_image`."""

    detail: Optional[str] = None
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """


class DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio(BaseModel):
    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudio(BaseModel):
    input_audio: DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudioInputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""


DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContent: TypeAlias = Union[
    str,
    DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputTextContent,
    DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentOutputText,
    DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputImage,
    DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContentInputAudio,
    List[object],
]


class DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInput(BaseModel):
    content: DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInputContent
    """Inputs to the model - can contain template strings."""

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""


class DataMethodReinforcementGraderGraderMultiGradersGraderLabelModel(BaseModel):
    input: List[DataMethodReinforcementGraderGraderMultiGradersGraderLabelModelInput]

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


DataMethodReinforcementGraderGraderMultiGraders: TypeAlias = Union[
    DataMethodReinforcementGraderGraderMultiGradersGraderStringCheck,
    DataMethodReinforcementGraderGraderMultiGradersGraderTextSimilarity,
    DataMethodReinforcementGraderGraderMultiGradersGraderPython,
    DataMethodReinforcementGraderGraderMultiGradersGraderScoreModel,
    DataMethodReinforcementGraderGraderMultiGradersGraderLabelModel,
]


class DataMethodReinforcementGraderGraderMulti(BaseModel):
    calculate_output: str
    """A formula to calculate the output based on grader results."""

    graders: DataMethodReinforcementGraderGraderMultiGraders
    """
    A StringCheckGrader object that performs a string comparison between input and
    reference using a specified operation.
    """

    name: str
    """The name of the grader."""

    type: Literal["multi"]
    """The object type, which is always `multi`."""


DataMethodReinforcementGrader: TypeAlias = Union[
    DataMethodReinforcementGraderGraderStringCheck,
    DataMethodReinforcementGraderGraderTextSimilarity,
    DataMethodReinforcementGraderGraderPython,
    DataMethodReinforcementGraderGraderScoreModel,
    DataMethodReinforcementGraderGraderMulti,
]


class DataMethodReinforcementHyperparameters(BaseModel):
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


class DataMethodReinforcement(BaseModel):
    grader: DataMethodReinforcementGrader
    """The grader used for the fine-tuning job."""

    hyperparameters: Optional[DataMethodReinforcementHyperparameters] = None
    """The hyperparameters used for the reinforcement fine-tuning job."""


class DataMethodSupervisedHyperparameters(BaseModel):
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


class DataMethodSupervised(BaseModel):
    hyperparameters: Optional[DataMethodSupervisedHyperparameters] = None
    """The hyperparameters used for the fine-tuning job."""


class DataMethod(BaseModel):
    type: Literal["supervised", "dpo", "reinforcement"]
    """The type of method. Is either `supervised`, `dpo`, or `reinforcement`."""

    dpo: Optional[DataMethodDpo] = None
    """Configuration for the DPO fine-tuning method."""

    reinforcement: Optional[DataMethodReinforcement] = None
    """Configuration for the reinforcement fine-tuning method."""

    supervised: Optional[DataMethodSupervised] = None
    """Configuration for the supervised fine-tuning method."""


class Data(BaseModel):
    id: str
    """The object identifier, which can be referenced in the API endpoints."""

    created_at: int
    """The Unix timestamp (in seconds) for when the fine-tuning job was created."""

    error: Optional[DataError] = None
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

    hyperparameters: DataHyperparameters
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

    integrations: Optional[List[DataIntegration]] = None
    """A list of integrations to enable for this fine-tuning job."""

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    method: Optional[DataMethod] = None
    """The method used for fine-tuning."""


class JobListResponse(BaseModel):
    data: List[Data]

    has_more: bool

    object: Literal["list"]
