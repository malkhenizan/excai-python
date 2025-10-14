# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.eval_item import EvalItem
from .eval_responses_source_param import EvalResponsesSourceParam
from .eval_jsonl_file_id_source_param import EvalJSONLFileIDSourceParam
from .eval_jsonl_file_content_source_param import EvalJSONLFileContentSourceParam

__all__ = [
    "CreateEvalResponsesRunDataSourceParam",
    "Source",
    "InputMessages",
    "InputMessagesUnionMember0",
    "InputMessagesUnionMember0Template",
    "InputMessagesUnionMember0TemplateChatMessage",
    "InputMessagesUnionMember1",
    "SamplingParams",
]

Source: TypeAlias = Union[EvalJSONLFileContentSourceParam, EvalJSONLFileIDSourceParam, EvalResponsesSourceParam]


class InputMessagesUnionMember0TemplateChatMessage(TypedDict, total=False):
    content: Required[str]
    """The content of the message."""

    role: Required[str]
    """The role of the message (e.g. "system", "assistant", "user")."""


InputMessagesUnionMember0Template: TypeAlias = Union[InputMessagesUnionMember0TemplateChatMessage, EvalItem]


class InputMessagesUnionMember0(TypedDict, total=False):
    template: Required[Iterable[InputMessagesUnionMember0Template]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Required[Literal["template"]]
    """The type of input messages. Always `template`."""


class InputMessagesUnionMember1(TypedDict, total=False):
    item_reference: Required[str]
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Required[Literal["item_reference"]]
    """The type of input messages. Always `item_reference`."""


InputMessages: TypeAlias = Union[InputMessagesUnionMember0, InputMessagesUnionMember1]


class SamplingParams(TypedDict, total=False):
    max_completion_tokens: int
    """The maximum number of tokens in the generated output."""

    seed: int
    """A seed value to initialize the randomness, during sampling."""

    temperature: float
    """A higher temperature increases randomness in the outputs."""

    top_p: float
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class CreateEvalResponsesRunDataSourceParam(TypedDict, total=False):
    source: Required[Source]
    """A EvalResponsesSource object describing a run data source configuration."""

    type: Required[Literal["completions"]]
    """The type of run data source. Always `completions`."""

    input_messages: InputMessages

    model: str
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: SamplingParams
