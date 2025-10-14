# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.eval_item import EvalItem
from .easy_input_message_param import EasyInputMessageParam
from .eval_jsonl_file_id_source_param import EvalJSONLFileIDSourceParam
from .eval_jsonl_file_content_source_param import EvalJSONLFileContentSourceParam
from .eval_stored_completions_source_param import EvalStoredCompletionsSourceParam

__all__ = [
    "CreateEvalCompletionsRunDataSourceParam",
    "Source",
    "InputMessages",
    "InputMessagesTemplateInputMessages",
    "InputMessagesTemplateInputMessagesTemplate",
    "InputMessagesItemReferenceInputMessages",
    "SamplingParams",
]

Source: TypeAlias = Union[EvalJSONLFileContentSourceParam, EvalJSONLFileIDSourceParam, EvalStoredCompletionsSourceParam]

InputMessagesTemplateInputMessagesTemplate: TypeAlias = Union[EasyInputMessageParam, EvalItem]


class InputMessagesTemplateInputMessages(TypedDict, total=False):
    template: Required[Iterable[InputMessagesTemplateInputMessagesTemplate]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Required[Literal["template"]]
    """The type of input messages. Always `template`."""


class InputMessagesItemReferenceInputMessages(TypedDict, total=False):
    item_reference: Required[str]
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Required[Literal["item_reference"]]
    """The type of input messages. Always `item_reference`."""


InputMessages: TypeAlias = Union[InputMessagesTemplateInputMessages, InputMessagesItemReferenceInputMessages]


class SamplingParams(TypedDict, total=False):
    max_completion_tokens: int
    """The maximum number of tokens in the generated output."""

    seed: int
    """A seed value to initialize the randomness, during sampling."""

    temperature: float
    """A higher temperature increases randomness in the outputs."""

    top_p: float
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class CreateEvalCompletionsRunDataSourceParam(TypedDict, total=False):
    source: Required[Source]
    """A StoredCompletionsRunDataSource configuration describing a set of filters"""

    type: Required[Literal["completions"]]
    """The type of run data source. Always `completions`."""

    input_messages: InputMessages

    model: str
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: SamplingParams
