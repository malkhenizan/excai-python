# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "StepListResponse",
    "Data",
    "DataLastError",
    "DataStepDetails",
    "DataStepDetailsRunStepDetailsMessageCreationObject",
    "DataStepDetailsRunStepDetailsMessageCreationObjectMessageCreation",
    "DataStepDetailsRunStepDetailsToolCallsObject",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCall",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObject",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreter",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutput",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputLogsObject",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObject",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObjectImage",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObject",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearch",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchRankingOptions",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResult",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResultContent",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObject",
    "DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObjectFunction",
    "DataUsage",
]


class DataLastError(BaseModel):
    code: Literal["server_error", "rate_limit_exceeded"]
    """One of `server_error` or `rate_limit_exceeded`."""

    message: str
    """A human-readable description of the error."""


class DataStepDetailsRunStepDetailsMessageCreationObjectMessageCreation(BaseModel):
    message_id: str
    """The ID of the message that was created by this run step."""


class DataStepDetailsRunStepDetailsMessageCreationObject(BaseModel):
    message_creation: DataStepDetailsRunStepDetailsMessageCreationObjectMessageCreation

    type: Literal["message_creation"]
    """Always `message_creation`."""


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputLogsObject(
    BaseModel
):
    logs: str
    """The text output from the Code Interpreter tool call."""

    type: Literal["logs"]
    """Always `logs`."""


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObjectImage(
    BaseModel
):
    file_id: str
    """The [file](/docs/api-reference/files) ID of the image."""


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObject(
    BaseModel
):
    image: DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObjectImage

    type: Literal["image"]
    """Always `image`."""


DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutput: TypeAlias = Union[
    DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputLogsObject,
    DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutputRunStepDetailsToolCallsCodeOutputImageObject,
]


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreter(BaseModel):
    input: str
    """The input to the Code Interpreter tool call."""

    outputs: List[
        DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreterOutput
    ]
    """The outputs from the Code Interpreter tool call.

    Code Interpreter can output one or more items, including text (`logs`) or images
    (`image`). Each of these are represented by a different object type.
    """


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObject(BaseModel):
    id: str
    """The ID of the tool call."""

    code_interpreter: (
        DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObjectCodeInterpreter
    )
    """The Code Interpreter tool call definition."""

    type: Literal["code_interpreter"]
    """The type of tool call.

    This is always going to be `code_interpreter` for this type of tool call.
    """


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchRankingOptions(
    BaseModel
):
    ranker: Literal["auto", "default_2024_08_21"]
    """The ranker to use for the file search.

    If not specified will use the `auto` ranker.
    """

    score_threshold: float
    """The score threshold for the file search.

    All values must be a floating point number between 0 and 1.
    """


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResultContent(
    BaseModel
):
    text: Optional[str] = None
    """The text content of the file."""

    type: Optional[Literal["text"]] = None
    """The type of the content."""


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResult(
    BaseModel
):
    file_id: str
    """The ID of the file that result was found in."""

    file_name: str
    """The name of the file that result was found in."""

    score: float
    """The score of the result.

    All values must be a floating point number between 0 and 1.
    """

    content: Optional[
        List[
            DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResultContent
        ]
    ] = None
    """The content of the result that was found.

    The content is only included if requested via the include query parameter.
    """


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearch(BaseModel):
    ranking_options: Optional[
        DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchRankingOptions
    ] = None
    """The ranking options for the file search."""

    results: Optional[
        List[
            DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearchResult
        ]
    ] = None
    """The results of the file search."""


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObject(BaseModel):
    id: str
    """The ID of the tool call object."""

    file_search: DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObjectFileSearch
    """For now, this is always going to be an empty object."""

    type: Literal["file_search"]
    """The type of tool call.

    This is always going to be `file_search` for this type of tool call.
    """


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObjectFunction(BaseModel):
    arguments: str
    """The arguments passed to the function."""

    name: str
    """The name of the function."""

    output: Optional[str] = None
    """The output of the function.

    This will be `null` if the outputs have not been
    [submitted](/docs/api-reference/runs/submitToolOutputs) yet.
    """


class DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObject(BaseModel):
    id: str
    """The ID of the tool call object."""

    function: DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObjectFunction
    """The definition of the function that was called."""

    type: Literal["function"]
    """The type of tool call.

    This is always going to be `function` for this type of tool call.
    """


DataStepDetailsRunStepDetailsToolCallsObjectToolCall: TypeAlias = Union[
    DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsCodeObject,
    DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFileSearchObject,
    DataStepDetailsRunStepDetailsToolCallsObjectToolCallRunStepDetailsToolCallsFunctionObject,
]


class DataStepDetailsRunStepDetailsToolCallsObject(BaseModel):
    tool_calls: List[DataStepDetailsRunStepDetailsToolCallsObjectToolCall]
    """An array of tool calls the run step was involved in.

    These can be associated with one of three types of tools: `code_interpreter`,
    `file_search`, or `function`.
    """

    type: Literal["tool_calls"]
    """Always `tool_calls`."""


DataStepDetails: TypeAlias = Union[
    DataStepDetailsRunStepDetailsMessageCreationObject, DataStepDetailsRunStepDetailsToolCallsObject
]


class DataUsage(BaseModel):
    completion_tokens: int
    """Number of completion tokens used over the course of the run step."""

    prompt_tokens: int
    """Number of prompt tokens used over the course of the run step."""

    total_tokens: int
    """Total number of tokens used (prompt + completion)."""


class Data(BaseModel):
    id: str
    """The identifier of the run step, which can be referenced in API endpoints."""

    assistant_id: str
    """
    The ID of the [assistant](/docs/api-reference/assistants) associated with the
    run step.
    """

    cancelled_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run step was cancelled."""

    completed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run step completed."""

    created_at: int
    """The Unix timestamp (in seconds) for when the run step was created."""

    expired_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run step expired.

    A step is considered expired if the parent run is expired.
    """

    failed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the run step failed."""

    last_error: Optional[DataLastError] = None
    """The last error associated with this run step.

    Will be `null` if there are no errors.
    """

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    object: Literal["thread.run.step"]
    """The object type, which is always `thread.run.step`."""

    run_id: str
    """The ID of the [run](/docs/api-reference/runs) that this run step is a part of."""

    status: Literal["in_progress", "cancelled", "failed", "completed", "expired"]
    """
    The status of the run step, which can be either `in_progress`, `cancelled`,
    `failed`, `completed`, or `expired`.
    """

    step_details: DataStepDetails
    """The details of the run step."""

    thread_id: str
    """The ID of the [thread](/docs/api-reference/threads) that was run."""

    type: Literal["message_creation", "tool_calls"]
    """The type of run step, which can be either `message_creation` or `tool_calls`."""

    usage: Optional[DataUsage] = None
    """Usage statistics related to the run step.

    This value will be `null` while the run step's status is `in_progress`.
    """


class StepListResponse(BaseModel):
    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: str
