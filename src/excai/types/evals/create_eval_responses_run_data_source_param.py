# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.mcp_tool import McpTool
from ..shared_params.eval_item import EvalItem
from ..shared_params.custom_tool import CustomTool
from .eval_responses_source_param import EvalResponsesSourceParam
from ..shared_params.function_tool import FunctionTool
from ..shared_params.image_gen_tool import ImageGenTool
from ..shared_params.web_search_tool import WebSearchTool
from ..shared_params.file_search_tool import FileSearchTool
from ..shared_params.local_shell_tool import LocalShellTool
from .eval_jsonl_file_id_source_param import EvalJSONLFileIDSourceParam
from ..shared_params.response_format_text import ResponseFormatText
from ..shared_params.code_interpreter_tool import CodeInterpreterTool
from .eval_jsonl_file_content_source_param import EvalJSONLFileContentSourceParam
from ..shared_params.web_search_preview_tool import WebSearchPreviewTool
from ..shared_params.computer_use_preview_tool import ComputerUsePreviewTool
from ..shared_params.response_format_json_object import ResponseFormatJsonObject
from ..shared_params.text_response_format_json_schema import TextResponseFormatJsonSchema

__all__ = [
    "CreateEvalResponsesRunDataSourceParam",
    "Source",
    "InputMessages",
    "InputMessagesTemplate",
    "InputMessagesTemplateTemplate",
    "InputMessagesTemplateTemplateChatMessage",
    "InputMessagesItemReference",
    "SamplingParams",
    "SamplingParamsText",
    "SamplingParamsTextFormat",
    "SamplingParamsTool",
]

Source: TypeAlias = Union[EvalJSONLFileContentSourceParam, EvalJSONLFileIDSourceParam, EvalResponsesSourceParam]


class InputMessagesTemplateTemplateChatMessage(TypedDict, total=False):
    content: Required[str]
    """The content of the message."""

    role: Required[str]
    """The role of the message (e.g. "system", "assistant", "user")."""


InputMessagesTemplateTemplate: TypeAlias = Union[InputMessagesTemplateTemplateChatMessage, EvalItem]


class InputMessagesTemplate(TypedDict, total=False):
    template: Required[Iterable[InputMessagesTemplateTemplate]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the `item` namespace, ie {{item.name}}.
    """

    type: Required[Literal["template"]]
    """The type of input messages. Always `template`."""


class InputMessagesItemReference(TypedDict, total=False):
    item_reference: Required[str]
    """A reference to a variable in the `item` namespace. Ie, "item.name" """

    type: Required[Literal["item_reference"]]
    """The type of input messages. Always `item_reference`."""


InputMessages: TypeAlias = Union[InputMessagesTemplate, InputMessagesItemReference]

SamplingParamsTextFormat: TypeAlias = Union[ResponseFormatText, TextResponseFormatJsonSchema, ResponseFormatJsonObject]


class SamplingParamsText(TypedDict, total=False):
    format: SamplingParamsTextFormat
    """An object specifying the format that the model must output.

    Configuring `{ "type": "json_schema" }` enables Structured Outputs, which
    ensures the model will match your supplied JSON schema. Learn more in the
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).

    The default format is `{ "type": "text" }` with no additional options.

    **Not recommended for gpt-4o and newer models:**

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """


SamplingParamsTool: TypeAlias = Union[
    FunctionTool,
    FileSearchTool,
    ComputerUsePreviewTool,
    WebSearchTool,
    McpTool,
    CodeInterpreterTool,
    ImageGenTool,
    LocalShellTool,
    CustomTool,
    WebSearchPreviewTool,
]


class SamplingParams(TypedDict, total=False):
    max_completion_tokens: int
    """The maximum number of tokens in the generated output."""

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

    seed: int
    """A seed value to initialize the randomness, during sampling."""

    temperature: float
    """A higher temperature increases randomness in the outputs."""

    text: SamplingParamsText
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](https://platform.excai.com/docs/guides/text)
    - [Structured Outputs](https://platform.excai.com/docs/guides/structured-outputs)
    """

    tools: Iterable[SamplingParamsTool]
    """An array of tools the model may call while generating a response.

    You can specify which tool to use by setting the `tool_choice` parameter.

    The two categories of tools you can provide the model are:

    - **Built-in tools**: Tools that are provided by EXCai that extend the model's
      capabilities, like
      [web search](https://platform.excai.com/docs/guides/tools-web-search) or
      [file search](https://platform.excai.com/docs/guides/tools-file-search). Learn
      more about [built-in tools](https://platform.excai.com/docs/guides/tools).
    - **Function calls (custom tools)**: Functions that are defined by you, enabling
      the model to call your own code. Learn more about
      [function calling](https://platform.excai.com/docs/guides/function-calling).
    """

    top_p: float
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class CreateEvalResponsesRunDataSourceParam(TypedDict, total=False):
    source: Required[Source]
    """Determines what populates the `item` namespace in this run's data source."""

    type: Required[Literal["responses"]]
    """The type of run data source. Always `responses`."""

    input_messages: InputMessages
    """Used when sampling from a model.

    Dictates the structure of the messages passed into the model. Can either be a
    reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template
    with variable references to the `item` namespace.
    """

    model: str
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: SamplingParams
