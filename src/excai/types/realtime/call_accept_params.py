# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "CallAcceptParams",
    "Audio",
    "AudioInput",
    "AudioInputFormat",
    "AudioInputFormatAudioPcm",
    "AudioInputFormatAudioPcmu",
    "AudioInputFormatAudioPcma",
    "AudioInputNoiseReduction",
    "AudioInputTranscription",
    "AudioInputTurnDetection",
    "AudioInputTurnDetectionServerVad",
    "AudioInputTurnDetectionSemanticVad",
    "AudioOutput",
    "AudioOutputFormat",
    "AudioOutputFormatAudioPcm",
    "AudioOutputFormatAudioPcmu",
    "AudioOutputFormatAudioPcma",
    "Prompt",
    "PromptVariables",
    "PromptVariablesInputTextContent",
    "PromptVariablesInputImageContent",
    "PromptVariablesInputFileContent",
    "ToolChoice",
    "ToolChoiceToolChoiceFunction",
    "ToolChoiceToolChoiceMcp",
    "Tool",
    "ToolFunction",
    "ToolMcp",
    "ToolMcpAllowedTools",
    "ToolMcpAllowedToolsMcpToolFilter",
    "ToolMcpRequireApproval",
    "ToolMcpRequireApprovalMcpToolApprovalFilter",
    "ToolMcpRequireApprovalMcpToolApprovalFilterAlways",
    "ToolMcpRequireApprovalMcpToolApprovalFilterNever",
    "Tracing",
    "TracingTracingConfiguration",
    "Truncation",
    "TruncationRetentionRatioTruncation",
]


class CallAcceptParams(TypedDict, total=False):
    type: Required[Literal["realtime"]]
    """The type of session to create. Always `realtime` for the Realtime API."""

    audio: Audio
    """Configuration for input and output audio."""

    include: List[Literal["item.input_audio_transcription.logprobs"]]
    """Additional fields to include in server outputs.

    `item.input_audio_transcription.logprobs`: Include logprobs for input audio
    transcription.
    """

    instructions: str
    """The default system instructions (i.e.

    system message) prepended to model calls. This field allows the client to guide
    the model on desired responses. The model can be instructed on response content
    and format, (e.g. "be extremely succinct", "act friendly", "here are examples of
    good responses") and on audio behavior (e.g. "talk quickly", "inject emotion
    into your voice", "laugh frequently"). The instructions are not guaranteed to be
    followed by the model, but they provide guidance to the model on the desired
    behavior.

    Note that the server sets default instructions which will be used if this field
    is not set and are visible in the `session.created` event at the start of the
    session.
    """

    max_output_tokens: Union[int, Literal["inf"]]
    """
    Maximum number of output tokens for a single assistant response, inclusive of
    tool calls. Provide an integer between 1 and 4096 to limit output tokens, or
    `inf` for the maximum available tokens for a given model. Defaults to `inf`.
    """

    model: Union[
        str,
        Literal[
            "gpt-realtime",
            "gpt-realtime-2025-08-28",
            "gpt-4o-realtime-preview",
            "gpt-4o-realtime-preview-2024-10-01",
            "gpt-4o-realtime-preview-2024-12-17",
            "gpt-4o-realtime-preview-2025-06-03",
            "gpt-4o-mini-realtime-preview",
            "gpt-4o-mini-realtime-preview-2024-12-17",
            "gpt-realtime-mini",
            "gpt-realtime-mini-2025-10-06",
            "gpt-audio-mini",
            "gpt-audio-mini-2025-10-06",
        ],
    ]
    """The Realtime model used for this session."""

    output_modalities: List[Literal["text", "audio"]]
    """The set of modalities the model can respond with.

    It defaults to `["audio"]`, indicating that the model will respond with audio
    plus a transcript. `["text"]` can be used to make the model respond with text
    only. It is not possible to request both `text` and `audio` at the same time.
    """

    prompt: Optional[Prompt]
    """
    Reference to a prompt template and its variables.
    [Learn more](https://platform.excai.com/docs/guides/text?api-mode=responses#reusable-prompts).
    """

    tool_choice: ToolChoice
    """How the model chooses tools.

    Provide one of the string modes or force a specific function/MCP tool.
    """

    tools: Iterable[Tool]
    """Tools available to the model."""

    tracing: Optional[Tracing]
    """
    Realtime API can write session traces to the
    [Traces Dashboard](/logs?api=traces). Set to null to disable tracing. Once
    tracing is enabled for a session, the configuration cannot be modified.

    `auto` will create a trace for the session with default values for the workflow
    name, group id, and metadata.
    """

    truncation: Truncation
    """
    Controls how the realtime conversation is truncated prior to model inference.
    The default is `auto`.
    """


class AudioInputFormatAudioPcm(TypedDict, total=False):
    rate: Literal[24000]
    """The sample rate of the audio. Always `24000`."""

    type: Literal["audio/pcm"]
    """The audio format. Always `audio/pcm`."""


class AudioInputFormatAudioPcmu(TypedDict, total=False):
    type: Literal["audio/pcmu"]
    """The audio format. Always `audio/pcmu`."""


class AudioInputFormatAudioPcma(TypedDict, total=False):
    type: Literal["audio/pcma"]
    """The audio format. Always `audio/pcma`."""


AudioInputFormat: TypeAlias = Union[AudioInputFormatAudioPcm, AudioInputFormatAudioPcmu, AudioInputFormatAudioPcma]


class AudioInputNoiseReduction(TypedDict, total=False):
    type: Literal["near_field", "far_field"]
    """Type of noise reduction.

    `near_field` is for close-talking microphones such as headphones, `far_field` is
    for far-field microphones such as laptop or conference room microphones.
    """


class AudioInputTranscription(TypedDict, total=False):
    language: str
    """The language of the input audio.

    Supplying the input language in
    [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`)
    format will improve accuracy and latency.
    """

    model: Literal["whisper-1", "gpt-4o-transcribe-latest", "gpt-4o-mini-transcribe", "gpt-4o-transcribe"]
    """The model to use for transcription.

    Current options are `whisper-1`, `gpt-4o-transcribe-latest`,
    `gpt-4o-mini-transcribe`, and `gpt-4o-transcribe`.
    """

    prompt: str
    """
    An optional text to guide the model's style or continue a previous audio
    segment. For `whisper-1`, the
    [prompt is a list of keywords](https://platform.excai.com/docs/guides/speech-to-text#prompting).
    For `gpt-4o-transcribe` models, the prompt is a free text string, for example
    "expect words related to technology".
    """


class AudioInputTurnDetectionServerVad(TypedDict, total=False):
    type: Required[Literal["server_vad"]]
    """Type of turn detection, `server_vad` to turn on simple Server VAD."""

    create_response: bool
    """
    Whether or not to automatically generate a response when a VAD stop event
    occurs.
    """

    idle_timeout_ms: Optional[int]
    """Optional timeout after which a model response will be triggered automatically.

    This is useful for situations in which a long pause from the user is unexpected,
    such as a phone call. The model will effectively prompt the user to continue the
    conversation based on the current context.

    The timeout value will be applied after the last model response's audio has
    finished playing, i.e. it's set to the `response.done` time plus audio playback
    duration.

    An `input_audio_buffer.timeout_triggered` event (plus events associated with the
    Response) will be emitted when the timeout is reached. Idle timeout is currently
    only supported for `server_vad` mode.
    """

    interrupt_response: bool
    """
    Whether or not to automatically interrupt any ongoing response with output to
    the default conversation (i.e. `conversation` of `auto`) when a VAD start event
    occurs.
    """

    prefix_padding_ms: int
    """Used only for `server_vad` mode.

    Amount of audio to include before the VAD detected speech (in milliseconds).
    Defaults to 300ms.
    """

    silence_duration_ms: int
    """Used only for `server_vad` mode.

    Duration of silence to detect speech stop (in milliseconds). Defaults to 500ms.
    With shorter values the model will respond more quickly, but may jump in on
    short pauses from the user.
    """

    threshold: float
    """Used only for `server_vad` mode.

    Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A higher
    threshold will require louder audio to activate the model, and thus might
    perform better in noisy environments.
    """


class AudioInputTurnDetectionSemanticVad(TypedDict, total=False):
    type: Required[Literal["semantic_vad"]]
    """Type of turn detection, `semantic_vad` to turn on Semantic VAD."""

    create_response: bool
    """
    Whether or not to automatically generate a response when a VAD stop event
    occurs.
    """

    eagerness: Literal["low", "medium", "high", "auto"]
    """Used only for `semantic_vad` mode.

    The eagerness of the model to respond. `low` will wait longer for the user to
    continue speaking, `high` will respond more quickly. `auto` is the default and
    is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s,
    4s, and 2s respectively.
    """

    interrupt_response: bool
    """
    Whether or not to automatically interrupt any ongoing response with output to
    the default conversation (i.e. `conversation` of `auto`) when a VAD start event
    occurs.
    """


AudioInputTurnDetection: TypeAlias = Union[AudioInputTurnDetectionServerVad, AudioInputTurnDetectionSemanticVad]


class AudioInput(TypedDict, total=False):
    format: AudioInputFormat
    """The format of the input audio."""

    noise_reduction: AudioInputNoiseReduction
    """Configuration for input audio noise reduction.

    This can be set to `null` to turn off. Noise reduction filters audio added to
    the input audio buffer before it is sent to VAD and the model. Filtering the
    audio can improve VAD and turn detection accuracy (reducing false positives) and
    model performance by improving perception of the input audio.
    """

    transcription: AudioInputTranscription
    """
    Configuration for input audio transcription, defaults to off and can be set to
    `null` to turn off once on. Input audio transcription is not native to the
    model, since the model consumes audio directly. Transcription runs
    asynchronously through
    [the /audio/transcriptions endpoint](https://platform.excai.com/docs/api-reference/audio/createTranscription)
    and should be treated as guidance of input audio content rather than precisely
    what the model heard. The client can optionally set the language and prompt for
    transcription, these offer additional guidance to the transcription service.
    """

    turn_detection: Optional[AudioInputTurnDetection]
    """Configuration for turn detection, ether Server VAD or Semantic VAD.

    This can be set to `null` to turn off, in which case the client must manually
    trigger model response.

    Server VAD means that the model will detect the start and end of speech based on
    audio volume and respond at the end of user speech.

    Semantic VAD is more advanced and uses a turn detection model (in conjunction
    with VAD) to semantically estimate whether the user has finished speaking, then
    dynamically sets a timeout based on this probability. For example, if user audio
    trails off with "uhhm", the model will score a low probability of turn end and
    wait longer for the user to continue speaking. This can be useful for more
    natural conversations, but may have a higher latency.
    """


class AudioOutputFormatAudioPcm(TypedDict, total=False):
    rate: Literal[24000]
    """The sample rate of the audio. Always `24000`."""

    type: Literal["audio/pcm"]
    """The audio format. Always `audio/pcm`."""


class AudioOutputFormatAudioPcmu(TypedDict, total=False):
    type: Literal["audio/pcmu"]
    """The audio format. Always `audio/pcmu`."""


class AudioOutputFormatAudioPcma(TypedDict, total=False):
    type: Literal["audio/pcma"]
    """The audio format. Always `audio/pcma`."""


AudioOutputFormat: TypeAlias = Union[AudioOutputFormatAudioPcm, AudioOutputFormatAudioPcmu, AudioOutputFormatAudioPcma]


class AudioOutput(TypedDict, total=False):
    format: AudioOutputFormat
    """The format of the output audio."""

    speed: float
    """
    The speed of the model's spoken response as a multiple of the original speed.
    1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed.
    This value can only be changed in between model turns, not while a response is
    in progress.

    This parameter is a post-processing adjustment to the audio after it is
    generated, it's also possible to prompt the model to speak faster or slower.
    """

    voice: Union[str, Literal["alloy", "ash", "ballad", "coral", "echo", "sage", "shimmer", "verse", "marin", "cedar"]]
    """The voice the model uses to respond.

    Voice cannot be changed during the session once the model has responded with
    audio at least once. Current voice options are `alloy`, `ash`, `ballad`,
    `coral`, `echo`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. We recommend
    `marin` and `cedar` for best quality.
    """


class Audio(TypedDict, total=False):
    input: AudioInput

    output: AudioOutput


class PromptVariablesInputTextContent(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class PromptVariablesInputImageContent(TypedDict, total=False):
    detail: Required[Literal["low", "high", "auto"]]
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    type: Required[Literal["input_image"]]
    """The type of the input item. Always `input_image`."""

    file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    image_url: Optional[str]
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """


class PromptVariablesInputFileContent(TypedDict, total=False):
    type: Required[Literal["input_file"]]
    """The type of the input item. Always `input_file`."""

    file_data: str
    """The content of the file to be sent to the model."""

    file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    file_url: str
    """The URL of the file to be sent to the model."""

    filename: str
    """The name of the file to be sent to the model."""


PromptVariables: TypeAlias = Union[
    str, PromptVariablesInputTextContent, PromptVariablesInputImageContent, PromptVariablesInputFileContent
]


class Prompt(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the prompt template to use."""

    variables: Optional[Dict[str, PromptVariables]]
    """Optional map of values to substitute in for variables in your prompt.

    The substitution values can either be strings, or other Response input types
    like images or files.
    """

    version: Optional[str]
    """Optional version of the prompt template."""


class ToolChoiceToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""

    type: Required[Literal["function"]]
    """For function calling, the type is always `function`."""


class ToolChoiceToolChoiceMcp(TypedDict, total=False):
    server_label: Required[str]
    """The label of the MCP server to use."""

    type: Required[Literal["mcp"]]
    """For MCP tools, the type is always `mcp`."""

    name: Optional[str]
    """The name of the tool to call on the server."""


ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"], ToolChoiceToolChoiceFunction, ToolChoiceToolChoiceMcp
]


class ToolFunction(TypedDict, total=False):
    description: str
    """
    The description of the function, including guidance on when and how to call it,
    and guidance about what to tell the user when calling (if anything).
    """

    name: str
    """The name of the function."""

    parameters: object
    """Parameters of the function in JSON Schema."""

    type: Literal["function"]
    """The type of the tool, i.e. `function`."""


class ToolMcpAllowedToolsMcpToolFilter(TypedDict, total=False):
    read_only: bool
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: SequenceNotStr[str]
    """List of allowed tool names."""


ToolMcpAllowedTools: TypeAlias = Union[SequenceNotStr[str], ToolMcpAllowedToolsMcpToolFilter]


class ToolMcpRequireApprovalMcpToolApprovalFilterAlways(TypedDict, total=False):
    read_only: bool
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: SequenceNotStr[str]
    """List of allowed tool names."""


class ToolMcpRequireApprovalMcpToolApprovalFilterNever(TypedDict, total=False):
    read_only: bool
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: SequenceNotStr[str]
    """List of allowed tool names."""


class ToolMcpRequireApprovalMcpToolApprovalFilter(TypedDict, total=False):
    always: ToolMcpRequireApprovalMcpToolApprovalFilterAlways
    """A filter object to specify which tools are allowed."""

    never: ToolMcpRequireApprovalMcpToolApprovalFilterNever
    """A filter object to specify which tools are allowed."""


ToolMcpRequireApproval: TypeAlias = Union[ToolMcpRequireApprovalMcpToolApprovalFilter, Literal["always", "never"]]


class ToolMcp(TypedDict, total=False):
    server_label: Required[str]
    """A label for this MCP server, used to identify it in tool calls."""

    type: Required[Literal["mcp"]]
    """The type of the MCP tool. Always `mcp`."""

    allowed_tools: Optional[ToolMcpAllowedTools]
    """List of allowed tool names or a filter object."""

    authorization: str
    """
    An OAuth access token that can be used with a remote MCP server, either with a
    custom MCP server URL or a service connector. Your application must handle the
    OAuth authorization flow and provide the token here.
    """

    connector_id: Literal[
        "connector_dropbox",
        "connector_gmail",
        "connector_googlecalendar",
        "connector_googledrive",
        "connector_microsoftteams",
        "connector_outlookcalendar",
        "connector_outlookemail",
        "connector_sharepoint",
    ]
    """Identifier for service connectors, like those available in ChatGPT.

    One of `server_url` or `connector_id` must be provided. Learn more about service
    connectors
    [here](https://platform.excai.com/docs/guides/tools-remote-mcp#connectors).

    Currently supported `connector_id` values are:

    - Dropbox: `connector_dropbox`
    - Gmail: `connector_gmail`
    - Google Calendar: `connector_googlecalendar`
    - Google Drive: `connector_googledrive`
    - Microsoft Teams: `connector_microsoftteams`
    - Outlook Calendar: `connector_outlookcalendar`
    - Outlook Email: `connector_outlookemail`
    - SharePoint: `connector_sharepoint`
    """

    headers: Optional[Dict[str, str]]
    """Optional HTTP headers to send to the MCP server.

    Use for authentication or other purposes.
    """

    require_approval: Optional[ToolMcpRequireApproval]
    """Specify which of the MCP server's tools require approval."""

    server_description: str
    """Optional description of the MCP server, used to provide more context."""

    server_url: str
    """The URL for the MCP server.

    One of `server_url` or `connector_id` must be provided.
    """


Tool: TypeAlias = Union[ToolFunction, ToolMcp]


class TracingTracingConfiguration(TypedDict, total=False):
    group_id: str
    """
    The group id to attach to this trace to enable filtering and grouping in the
    Traces Dashboard.
    """

    metadata: object
    """
    The arbitrary metadata to attach to this trace to enable filtering in the Traces
    Dashboard.
    """

    workflow_name: str
    """The name of the workflow to attach to this trace.

    This is used to name the trace in the Traces Dashboard.
    """


Tracing: TypeAlias = Union[Literal["auto"], TracingTracingConfiguration]


class TruncationRetentionRatioTruncation(TypedDict, total=False):
    retention_ratio: Required[float]
    """
    Fraction of post-instruction conversation tokens to retain (0.0 - 1.0) when the
    conversation exceeds the input token limit.
    """

    type: Required[Literal["retention_ratio"]]
    """Use retention ratio truncation."""


Truncation: TypeAlias = Union[Literal["auto", "disabled"], TruncationRetentionRatioTruncation]
