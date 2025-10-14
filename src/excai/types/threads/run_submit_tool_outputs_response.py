# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .truncation_object import TruncationObject
from .run_tool_call_object import RunToolCallObject
from ..shared.assistant_tools_code import AssistantToolsCode
from ..shared.response_format_text import ResponseFormatText
from .assistants_named_tool_choice import AssistantsNamedToolChoice
from ..shared.assistant_tools_function import AssistantToolsFunction
from ..shared.assistant_tools_file_search import AssistantToolsFileSearch
from ..shared.response_format_json_object import ResponseFormatJsonObject
from ..shared.response_format_json_schema import ResponseFormatJsonSchema

__all__ = [
    "RunSubmitToolOutputsResponse",
    "IncompleteDetails",
    "LastError",
    "RequiredAction",
    "RequiredActionSubmitToolOutputs",
    "ResponseFormat",
    "ToolChoice",
    "Tool",
    "Usage",
]


class IncompleteDetails(BaseModel):
    reason: Optional[Literal["max_completion_tokens", "max_prompt_tokens"]] = None
    """The reason why the run is incomplete.

    This will point to which specific token limit was reached over the course of the
    run.
    """


class LastError(BaseModel):
    code: Literal["server_error", "rate_limit_exceeded", "invalid_prompt"]
    """One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`."""

    message: str
    """A human-readable description of the error."""


class RequiredActionSubmitToolOutputs(BaseModel):
    tool_calls: List[RunToolCallObject]
    """A list of the relevant tool calls."""


class RequiredAction(BaseModel):
    submit_tool_outputs: RequiredActionSubmitToolOutputs
    """Details on the tool outputs needed for this run to continue."""

    type: Literal["submit_tool_outputs"]
    """For now, this is always `submit_tool_outputs`."""


ResponseFormat: TypeAlias = Union[
    Literal["auto"], ResponseFormatText, ResponseFormatJsonObject, ResponseFormatJsonSchema, None
]

ToolChoice: TypeAlias = Union[Literal["none", "auto", "required"], AssistantsNamedToolChoice, None]

Tool: TypeAlias = Annotated[
    Union[AssistantToolsCode, AssistantToolsFileSearch, AssistantToolsFunction], PropertyInfo(discriminator="type")
]


class Usage(BaseModel):
    completion_tokens: int
    """Number of completion tokens used over the course of the run."""

    prompt_tokens: int
    """Number of prompt tokens used over the course of the run."""

    total_tokens: int
    """Total number of tokens used (prompt + completion)."""


class RunSubmitToolOutputsResponse(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints."""

    assistant_id: str
    """
    The ID of the
    [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
    execution of this run.
    """

    cancelled_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run was cancelled."""

    completed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run was completed."""

    created_at: int
    """The Unix timestamp (in seconds) for when the run was created."""

    expires_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run will expire."""

    failed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run failed."""

    incomplete_details: Optional[IncompleteDetails] = None
    """Details on why the run is incomplete.

    Will be `null` if the run is not incomplete.
    """

    instructions: str
    """
    The instructions that the
    [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
    this run.
    """

    last_error: Optional[LastError] = None
    """The last error associated with this run. Will be `null` if there are no errors."""

    max_completion_tokens: Optional[int] = None
    """
    The maximum number of completion tokens specified to have been used over the
    course of the run.
    """

    max_prompt_tokens: Optional[int] = None
    """
    The maximum number of prompt tokens specified to have been used over the course
    of the run.
    """

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    model: str
    """
    The model that the
    [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
    this run.
    """

    object: Literal["thread.run"]
    """The object type, which is always `thread.run`."""

    parallel_tool_calls: bool
    """
    Whether to enable
    [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
    during tool use.
    """

    required_action: Optional[RequiredAction] = None
    """Details on the action required to continue the run.

    Will be `null` if no action is required.
    """

    response_format: Optional[ResponseFormat] = None
    """Specifies the format that the model must output.

    Compatible with [GPT-4o](https://platform.excai.com/docs/models#gpt-4o),
    [GPT-4 Turbo](https://platform.excai.com/docs/models#gpt-4-turbo-and-gpt-4), and
    all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
    Outputs which ensures the model will match your supplied JSON schema. Learn more
    in the
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
    message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to
    produce JSON yourself via a system or user message. Without this, the model may
    generate an unending stream of whitespace until the generation reaches the token
    limit, resulting in a long-running and seemingly "stuck" request. Also note that
    the message content may be partially cut off if `finish_reason="length"`, which
    indicates the generation exceeded `max_tokens` or the conversation exceeded the
    max context length.
    """

    started_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run was started."""

    status: Literal[
        "queued",
        "in_progress",
        "requires_action",
        "cancelling",
        "cancelled",
        "failed",
        "completed",
        "incomplete",
        "expired",
    ]
    """
    The status of the run, which can be either `queued`, `in_progress`,
    `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`,
    `incomplete`, or `expired`.
    """

    thread_id: str
    """
    The ID of the [thread](https://platform.excai.com/docs/api-reference/threads)
    that was executed on as a part of this run.
    """

    tool_choice: Optional[ToolChoice] = None
    """
    Controls which (if any) tool is called by the model. `none` means the model will
    not call any tools and instead generates a message. `auto` is the default value
    and means the model can pick between generating a message or calling one or more
    tools. `required` means the model must call one or more tools before responding
    to the user. Specifying a particular tool like `{"type": "file_search"}` or
    `{"type": "function", "function": {"name": "my_function"}}` forces the model to
    call that tool.
    """

    tools: List[Tool]
    """
    The list of tools that the
    [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
    this run.
    """

    truncation_strategy: Optional[TruncationObject] = None
    """Controls for how a thread will be truncated prior to the run.

    Use this to control the initial context window of the run.
    """

    usage: Optional[Usage] = None
    """Usage statistics related to the run.

    This value will be `null` if the run is not in a terminal state (i.e.
    `in_progress`, `queued`, etc.).
    """

    temperature: Optional[float] = None
    """The sampling temperature used for this run. If not set, defaults to 1."""

    top_p: Optional[float] = None
    """The nucleus sampling value used for this run. If not set, defaults to 1."""
