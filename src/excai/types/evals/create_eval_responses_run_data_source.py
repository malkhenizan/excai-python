# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..shared.mcp_tool import McpTool
from ..shared.eval_item import EvalItem
from ..shared.custom_tool import CustomTool
from ..shared.function_tool import FunctionTool
from .eval_responses_source import EvalResponsesSource
from ..shared.image_gen_tool import ImageGenTool
from ..shared.web_search_tool import WebSearchTool
from ..shared.file_search_tool import FileSearchTool
from ..shared.local_shell_tool import LocalShellTool
from .eval_jsonl_file_id_source import EvalJSONLFileIDSource
from ..shared.response_format_text import ResponseFormatText
from ..shared.code_interpreter_tool import CodeInterpreterTool
from .eval_jsonl_file_content_source import EvalJSONLFileContentSource
from ..shared.web_search_preview_tool import WebSearchPreviewTool
from ..shared.computer_use_preview_tool import ComputerUsePreviewTool
from ..shared.response_format_json_object import ResponseFormatJsonObject
from ..shared.text_response_format_json_schema import TextResponseFormatJsonSchema

__all__ = [
    "CreateEvalResponsesRunDataSource",
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

Source: TypeAlias = Annotated[
    Union[EvalJSONLFileContentSource, EvalJSONLFileIDSource, EvalResponsesSource], PropertyInfo(discriminator="type")
]


class InputMessagesTemplateTemplateChatMessage(BaseModel):
    content: str
    """The content of the message."""

    role: str
    """The role of the message (e.g. "system", "assistant", "user")."""


InputMessagesTemplateTemplate: TypeAlias = Union[InputMessagesTemplateTemplateChatMessage, EvalItem]


class InputMessagesTemplate(BaseModel):
    template: List[InputMessagesTemplateTemplate]
    """A list of chat messages forming the prompt or context.

    May include variable references to the `item` namespace, ie {{item.name}}.
    """

    type: Literal["template"]
    """The type of input messages. Always `template`."""


class InputMessagesItemReference(BaseModel):
    item_reference: str
    """A reference to a variable in the `item` namespace. Ie, "item.name" """

    type: Literal["item_reference"]
    """The type of input messages. Always `item_reference`."""


InputMessages: TypeAlias = Annotated[
    Union[InputMessagesTemplate, InputMessagesItemReference], PropertyInfo(discriminator="type")
]

SamplingParamsTextFormat: TypeAlias = Annotated[
    Union[ResponseFormatText, TextResponseFormatJsonSchema, ResponseFormatJsonObject],
    PropertyInfo(discriminator="type"),
]


class SamplingParamsText(BaseModel):
    format: Optional[SamplingParamsTextFormat] = None
    """An object specifying the format that the model must output.

    Configuring `{ "type": "json_schema" }` enables Structured Outputs, which
    ensures the model will match your supplied JSON schema. Learn more in the
    [Structured Outputs guide](https://main.excai.ai/docs/guides/structured-outputs).

    The default format is `{ "type": "text" }` with no additional options.

    **Not recommended for gpt-4o and newer models:**

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """


SamplingParamsTool: TypeAlias = Annotated[
    Union[
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
    ],
    PropertyInfo(discriminator="type"),
]


class SamplingParams(BaseModel):
    max_completion_tokens: Optional[int] = None
    """The maximum number of tokens in the generated output."""

    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] = None
    """
    Constrains effort on reasoning for
    [reasoning models](https://main.excai.ai/docs/guides/reasoning). Currently
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

    text: Optional[SamplingParamsText] = None
    """Configuration options for a text response from the model.

    Can be plain text or structured JSON data. Learn more:

    - [Text inputs and outputs](https://main.excai.ai/docs/guides/text)
    - [Structured Outputs](https://main.excai.ai/docs/guides/structured-outputs)
    """

    tools: Optional[List[SamplingParamsTool]] = None
    """An array of tools the model may call while generating a response.

    You can specify which tool to use by setting the `tool_choice` parameter.

    The two categories of tools you can provide the model are:

    - **Built-in tools**: Tools that are provided by EXCai that extend the model's
      capabilities, like
      [web search](https://main.excai.ai/docs/guides/tools-web-search) or
      [file search](https://main.excai.ai/docs/guides/tools-file-search). Learn more
      about [built-in tools](https://main.excai.ai/docs/guides/tools).
    - **Function calls (custom tools)**: Functions that are defined by you, enabling
      the model to call your own code. Learn more about
      [function calling](https://main.excai.ai/docs/guides/function-calling).
    """

    top_p: Optional[float] = None
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class CreateEvalResponsesRunDataSource(BaseModel):
    source: Source
    """Determines what populates the `item` namespace in this run's data source."""

    type: Literal["responses"]
    """The type of run data source. Always `responses`."""

    input_messages: Optional[InputMessages] = None
    """Used when sampling from a model.

    Dictates the structure of the messages passed into the model. Can either be a
    reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template
    with variable references to the `item` namespace.
    """

    model: Optional[str] = None
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[SamplingParams] = None
