# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..shared.eval_item import EvalItem
from .easy_input_message import EasyInputMessage
from .chat_completion_tool import ChatCompletionTool
from .eval_jsonl_file_id_source import EvalJSONLFileIDSource
from ..shared.response_format_text import ResponseFormatText
from .eval_jsonl_file_content_source import EvalJSONLFileContentSource
from .eval_stored_completions_source import EvalStoredCompletionsSource
from ..shared.response_format_json_object import ResponseFormatJsonObject
from ..shared.response_format_json_schema import ResponseFormatJsonSchema

__all__ = [
    "CreateEvalCompletionsRunDataSource",
    "Source",
    "InputMessages",
    "InputMessagesTemplate",
    "InputMessagesTemplateTemplate",
    "InputMessagesItemReference",
    "SamplingParams",
    "SamplingParamsResponseFormat",
]

Source: TypeAlias = Annotated[
    Union[EvalJSONLFileContentSource, EvalJSONLFileIDSource, EvalStoredCompletionsSource],
    PropertyInfo(discriminator="type"),
]

InputMessagesTemplateTemplate: TypeAlias = Union[EasyInputMessage, EvalItem]


class InputMessagesTemplate(BaseModel):
    template: List[InputMessagesTemplateTemplate]
    """A list of chat messages forming the prompt or context.

    May include variable references to the `item` namespace, ie {{item.name}}.
    """

    type: Literal["template"]
    """The type of input messages. Always `template`."""


class InputMessagesItemReference(BaseModel):
    item_reference: str
    """A reference to a variable in the `item` namespace. Ie, "item.input_trajectory" """

    type: Literal["item_reference"]
    """The type of input messages. Always `item_reference`."""


InputMessages: TypeAlias = Annotated[
    Union[InputMessagesTemplate, InputMessagesItemReference], PropertyInfo(discriminator="type")
]

SamplingParamsResponseFormat: TypeAlias = Union[ResponseFormatText, ResponseFormatJsonSchema, ResponseFormatJsonObject]


class SamplingParams(BaseModel):
    max_completion_tokens: Optional[int] = None
    """The maximum number of tokens in the generated output."""

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

    response_format: Optional[SamplingParamsResponseFormat] = None
    """An object specifying the format that the model must output.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
    Outputs which ensures the model will match your supplied JSON schema. Learn more
    in the
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """

    seed: Optional[int] = None
    """A seed value to initialize the randomness, during sampling."""

    temperature: Optional[float] = None
    """A higher temperature increases randomness in the outputs."""

    tools: Optional[List[ChatCompletionTool]] = None
    """A list of tools the model may call.

    Currently, only functions are supported as a tool. Use this to provide a list of
    functions the model may generate JSON inputs for. A max of 128 functions are
    supported.
    """

    top_p: Optional[float] = None
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class CreateEvalCompletionsRunDataSource(BaseModel):
    source: Source
    """Determines what populates the `item` namespace in this run's data source."""

    type: Literal["completions"]
    """The type of run data source. Always `completions`."""

    input_messages: Optional[InputMessages] = None
    """Used when sampling from a model.

    Dictates the structure of the messages passed into the model. Can either be a
    reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template
    with variable references to the `item` namespace.
    """

    model: Optional[str] = None
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[SamplingParams] = None
