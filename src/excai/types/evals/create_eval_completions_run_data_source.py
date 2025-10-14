# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..shared.eval_item import EvalItem
from .easy_input_message import EasyInputMessage
from .eval_jsonl_file_id_source import EvalJSONLFileIDSource
from .eval_jsonl_file_content_source import EvalJSONLFileContentSource
from .eval_stored_completions_source import EvalStoredCompletionsSource

__all__ = [
    "CreateEvalCompletionsRunDataSource",
    "Source",
    "InputMessages",
    "InputMessagesTemplateInputMessages",
    "InputMessagesTemplateInputMessagesTemplate",
    "InputMessagesItemReferenceInputMessages",
    "SamplingParams",
]

Source: TypeAlias = Union[EvalJSONLFileContentSource, EvalJSONLFileIDSource, EvalStoredCompletionsSource]

InputMessagesTemplateInputMessagesTemplate: TypeAlias = Union[EasyInputMessage, EvalItem]


class InputMessagesTemplateInputMessages(BaseModel):
    template: List[InputMessagesTemplateInputMessagesTemplate]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Literal["template"]
    """The type of input messages. Always `template`."""


class InputMessagesItemReferenceInputMessages(BaseModel):
    item_reference: str
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Literal["item_reference"]
    """The type of input messages. Always `item_reference`."""


InputMessages: TypeAlias = Union[InputMessagesTemplateInputMessages, InputMessagesItemReferenceInputMessages]


class SamplingParams(BaseModel):
    max_completion_tokens: Optional[int] = None
    """The maximum number of tokens in the generated output."""

    seed: Optional[int] = None
    """A seed value to initialize the randomness, during sampling."""

    temperature: Optional[float] = None
    """A higher temperature increases randomness in the outputs."""

    top_p: Optional[float] = None
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class CreateEvalCompletionsRunDataSource(BaseModel):
    source: Source
    """A StoredCompletionsRunDataSource configuration describing a set of filters"""

    type: Literal["completions"]
    """The type of run data source. Always `completions`."""

    input_messages: Optional[InputMessages] = None

    model: Optional[str] = None
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[SamplingParams] = None
