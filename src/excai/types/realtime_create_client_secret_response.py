# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "RealtimeCreateClientSecretResponse",
    "Session",
    "SessionRealtime",
    "SessionRealtimeClientSecret",
    "SessionRealtimeAudio",
    "SessionRealtimeAudioInput",
    "SessionRealtimeAudioInputFormat",
    "SessionRealtimeAudioInputFormatAudioPcm",
    "SessionRealtimeAudioInputFormatAudioPcmu",
    "SessionRealtimeAudioInputFormatAudioPcma",
    "SessionRealtimeAudioInputNoiseReduction",
    "SessionRealtimeAudioInputTranscription",
    "SessionRealtimeAudioInputTurnDetection",
    "SessionRealtimeAudioInputTurnDetectionServerVad",
    "SessionRealtimeAudioInputTurnDetectionSemanticVad",
    "SessionRealtimeAudioOutput",
    "SessionRealtimeAudioOutputFormat",
    "SessionRealtimeAudioOutputFormatAudioPcm",
    "SessionRealtimeAudioOutputFormatAudioPcmu",
    "SessionRealtimeAudioOutputFormatAudioPcma",
    "SessionRealtimePrompt",
    "SessionRealtimePromptVariables",
    "SessionRealtimePromptVariablesInputTextContent",
    "SessionRealtimePromptVariablesInputImageContent",
    "SessionRealtimePromptVariablesInputFileContent",
    "SessionRealtimeToolChoice",
    "SessionRealtimeToolChoiceToolChoiceFunction",
    "SessionRealtimeToolChoiceToolChoiceMcp",
    "SessionRealtimeTool",
    "SessionRealtimeToolRealtimeFunctionTool",
    "SessionRealtimeToolMcpTool",
    "SessionRealtimeToolMcpToolAllowedTools",
    "SessionRealtimeToolMcpToolAllowedToolsMcpToolFilter",
    "SessionRealtimeToolMcpToolRequireApproval",
    "SessionRealtimeToolMcpToolRequireApprovalMcpToolApprovalFilter",
    "SessionRealtimeToolMcpToolRequireApprovalMcpToolApprovalFilterAlways",
    "SessionRealtimeToolMcpToolRequireApprovalMcpToolApprovalFilterNever",
    "SessionRealtimeTracing",
    "SessionRealtimeTracingTracingConfiguration",
    "SessionRealtimeTruncation",
    "SessionRealtimeTruncationRetentionRatioTruncation",
    "SessionTranscription",
    "SessionTranscriptionAudio",
    "SessionTranscriptionAudioInput",
    "SessionTranscriptionAudioInputFormat",
    "SessionTranscriptionAudioInputFormatAudioPcm",
    "SessionTranscriptionAudioInputFormatAudioPcmu",
    "SessionTranscriptionAudioInputFormatAudioPcma",
    "SessionTranscriptionAudioInputNoiseReduction",
    "SessionTranscriptionAudioInputTranscription",
    "SessionTranscriptionAudioInputTurnDetection",
]


class SessionRealtimeClientSecret(BaseModel):
    expires_at: int
    """Timestamp for when the token expires.

    Currently, all tokens expire after one minute.
    """

    value: str
    """
    Ephemeral key usable in client environments to authenticate connections to the
    Realtime API. Use this in client-side environments rather than a standard API
    token, which should only be used server-side.
    """


class SessionRealtimeAudioInputFormatAudioPcm(BaseModel):
    rate: Optional[Literal[24000]] = None
    """The sample rate of the audio. Always `24000`."""

    type: Optional[Literal["audio/pcm"]] = None
    """The audio format. Always `audio/pcm`."""


class SessionRealtimeAudioInputFormatAudioPcmu(BaseModel):
    type: Optional[Literal["audio/pcmu"]] = None
    """The audio format. Always `audio/pcmu`."""


class SessionRealtimeAudioInputFormatAudioPcma(BaseModel):
    type: Optional[Literal["audio/pcma"]] = None
    """The audio format. Always `audio/pcma`."""


SessionRealtimeAudioInputFormat: TypeAlias = Annotated[
    Union[
        SessionRealtimeAudioInputFormatAudioPcm,
        SessionRealtimeAudioInputFormatAudioPcmu,
        SessionRealtimeAudioInputFormatAudioPcma,
    ],
    PropertyInfo(discriminator="type"),
]


class SessionRealtimeAudioInputNoiseReduction(BaseModel):
    type: Optional[Literal["near_field", "far_field"]] = None
    """Type of noise reduction.

    `near_field` is for close-talking microphones such as headphones, `far_field` is
    for far-field microphones such as laptop or conference room microphones.
    """


class SessionRealtimeAudioInputTranscription(BaseModel):
    language: Optional[str] = None
    """The language of the input audio.

    Supplying the input language in
    [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`)
    format will improve accuracy and latency.
    """

    model: Optional[Literal["whisper-1", "gpt-4o-transcribe-latest", "gpt-4o-mini-transcribe", "gpt-4o-transcribe"]] = (
        None
    )
    """The model to use for transcription.

    Current options are `whisper-1`, `gpt-4o-transcribe-latest`,
    `gpt-4o-mini-transcribe`, and `gpt-4o-transcribe`.
    """

    prompt: Optional[str] = None
    """
    An optional text to guide the model's style or continue a previous audio
    segment. For `whisper-1`, the
    [prompt is a list of keywords](https://platform.excai.com/docs/guides/speech-to-text#prompting).
    For `gpt-4o-transcribe` models, the prompt is a free text string, for example
    "expect words related to technology".
    """


class SessionRealtimeAudioInputTurnDetectionServerVad(BaseModel):
    type: Literal["server_vad"]
    """Type of turn detection, `server_vad` to turn on simple Server VAD."""

    create_response: Optional[bool] = None
    """
    Whether or not to automatically generate a response when a VAD stop event
    occurs.
    """

    idle_timeout_ms: Optional[int] = None
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

    interrupt_response: Optional[bool] = None
    """
    Whether or not to automatically interrupt any ongoing response with output to
    the default conversation (i.e. `conversation` of `auto`) when a VAD start event
    occurs.
    """

    prefix_padding_ms: Optional[int] = None
    """Used only for `server_vad` mode.

    Amount of audio to include before the VAD detected speech (in milliseconds).
    Defaults to 300ms.
    """

    silence_duration_ms: Optional[int] = None
    """Used only for `server_vad` mode.

    Duration of silence to detect speech stop (in milliseconds). Defaults to 500ms.
    With shorter values the model will respond more quickly, but may jump in on
    short pauses from the user.
    """

    threshold: Optional[float] = None
    """Used only for `server_vad` mode.

    Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A higher
    threshold will require louder audio to activate the model, and thus might
    perform better in noisy environments.
    """


class SessionRealtimeAudioInputTurnDetectionSemanticVad(BaseModel):
    type: Literal["semantic_vad"]
    """Type of turn detection, `semantic_vad` to turn on Semantic VAD."""

    create_response: Optional[bool] = None
    """
    Whether or not to automatically generate a response when a VAD stop event
    occurs.
    """

    eagerness: Optional[Literal["low", "medium", "high", "auto"]] = None
    """Used only for `semantic_vad` mode.

    The eagerness of the model to respond. `low` will wait longer for the user to
    continue speaking, `high` will respond more quickly. `auto` is the default and
    is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s,
    4s, and 2s respectively.
    """

    interrupt_response: Optional[bool] = None
    """
    Whether or not to automatically interrupt any ongoing response with output to
    the default conversation (i.e. `conversation` of `auto`) when a VAD start event
    occurs.
    """


SessionRealtimeAudioInputTurnDetection: TypeAlias = Annotated[
    Union[SessionRealtimeAudioInputTurnDetectionServerVad, SessionRealtimeAudioInputTurnDetectionSemanticVad, None],
    PropertyInfo(discriminator="type"),
]


class SessionRealtimeAudioInput(BaseModel):
    format: Optional[SessionRealtimeAudioInputFormat] = None
    """The format of the input audio."""

    noise_reduction: Optional[SessionRealtimeAudioInputNoiseReduction] = None
    """Configuration for input audio noise reduction.

    This can be set to `null` to turn off. Noise reduction filters audio added to
    the input audio buffer before it is sent to VAD and the model. Filtering the
    audio can improve VAD and turn detection accuracy (reducing false positives) and
    model performance by improving perception of the input audio.
    """

    transcription: Optional[SessionRealtimeAudioInputTranscription] = None
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

    turn_detection: Optional[SessionRealtimeAudioInputTurnDetection] = None
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


class SessionRealtimeAudioOutputFormatAudioPcm(BaseModel):
    rate: Optional[Literal[24000]] = None
    """The sample rate of the audio. Always `24000`."""

    type: Optional[Literal["audio/pcm"]] = None
    """The audio format. Always `audio/pcm`."""


class SessionRealtimeAudioOutputFormatAudioPcmu(BaseModel):
    type: Optional[Literal["audio/pcmu"]] = None
    """The audio format. Always `audio/pcmu`."""


class SessionRealtimeAudioOutputFormatAudioPcma(BaseModel):
    type: Optional[Literal["audio/pcma"]] = None
    """The audio format. Always `audio/pcma`."""


SessionRealtimeAudioOutputFormat: TypeAlias = Annotated[
    Union[
        SessionRealtimeAudioOutputFormatAudioPcm,
        SessionRealtimeAudioOutputFormatAudioPcmu,
        SessionRealtimeAudioOutputFormatAudioPcma,
    ],
    PropertyInfo(discriminator="type"),
]


class SessionRealtimeAudioOutput(BaseModel):
    format: Optional[SessionRealtimeAudioOutputFormat] = None
    """The format of the output audio."""

    speed: Optional[float] = None
    """
    The speed of the model's spoken response as a multiple of the original speed.
    1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed.
    This value can only be changed in between model turns, not while a response is
    in progress.

    This parameter is a post-processing adjustment to the audio after it is
    generated, it's also possible to prompt the model to speak faster or slower.
    """

    voice: Union[
        str, Literal["alloy", "ash", "ballad", "coral", "echo", "sage", "shimmer", "verse", "marin", "cedar"], None
    ] = None
    """The voice the model uses to respond.

    Voice cannot be changed during the session once the model has responded with
    audio at least once. Current voice options are `alloy`, `ash`, `ballad`,
    `coral`, `echo`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. We recommend
    `marin` and `cedar` for best quality.
    """


class SessionRealtimeAudio(BaseModel):
    input: Optional[SessionRealtimeAudioInput] = None

    output: Optional[SessionRealtimeAudioOutput] = None


class SessionRealtimePromptVariablesInputTextContent(BaseModel):
    text: str
    """The text input to the model."""

    type: Literal["input_text"]
    """The type of the input item. Always `input_text`."""


class SessionRealtimePromptVariablesInputImageContent(BaseModel):
    detail: Literal["low", "high", "auto"]
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    type: Literal["input_image"]
    """The type of the input item. Always `input_image`."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    image_url: Optional[str] = None
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """


class SessionRealtimePromptVariablesInputFileContent(BaseModel):
    type: Literal["input_file"]
    """The type of the input item. Always `input_file`."""

    file_data: Optional[str] = None
    """The content of the file to be sent to the model."""

    file_id: Optional[str] = None
    """The ID of the file to be sent to the model."""

    file_url: Optional[str] = None
    """The URL of the file to be sent to the model."""

    filename: Optional[str] = None
    """The name of the file to be sent to the model."""


SessionRealtimePromptVariables: TypeAlias = Union[
    str,
    SessionRealtimePromptVariablesInputTextContent,
    SessionRealtimePromptVariablesInputImageContent,
    SessionRealtimePromptVariablesInputFileContent,
]


class SessionRealtimePrompt(BaseModel):
    id: str
    """The unique identifier of the prompt template to use."""

    variables: Optional[Dict[str, SessionRealtimePromptVariables]] = None
    """Optional map of values to substitute in for variables in your prompt.

    The substitution values can either be strings, or other Response input types
    like images or files.
    """

    version: Optional[str] = None
    """Optional version of the prompt template."""


class SessionRealtimeToolChoiceToolChoiceFunction(BaseModel):
    name: str
    """The name of the function to call."""

    type: Literal["function"]
    """For function calling, the type is always `function`."""


class SessionRealtimeToolChoiceToolChoiceMcp(BaseModel):
    server_label: str
    """The label of the MCP server to use."""

    type: Literal["mcp"]
    """For MCP tools, the type is always `mcp`."""

    name: Optional[str] = None
    """The name of the tool to call on the server."""


SessionRealtimeToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"],
    SessionRealtimeToolChoiceToolChoiceFunction,
    SessionRealtimeToolChoiceToolChoiceMcp,
]


class SessionRealtimeToolRealtimeFunctionTool(BaseModel):
    description: Optional[str] = None
    """
    The description of the function, including guidance on when and how to call it,
    and guidance about what to tell the user when calling (if anything).
    """

    name: Optional[str] = None
    """The name of the function."""

    parameters: Optional[object] = None
    """Parameters of the function in JSON Schema."""

    type: Optional[Literal["function"]] = None
    """The type of the tool, i.e. `function`."""


class SessionRealtimeToolMcpToolAllowedToolsMcpToolFilter(BaseModel):
    read_only: Optional[bool] = None
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


SessionRealtimeToolMcpToolAllowedTools: TypeAlias = Union[
    List[str], SessionRealtimeToolMcpToolAllowedToolsMcpToolFilter, None
]


class SessionRealtimeToolMcpToolRequireApprovalMcpToolApprovalFilterAlways(BaseModel):
    read_only: Optional[bool] = None
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


class SessionRealtimeToolMcpToolRequireApprovalMcpToolApprovalFilterNever(BaseModel):
    read_only: Optional[bool] = None
    """Indicates whether or not a tool modifies data or is read-only.

    If an MCP server is
    [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
    it will match this filter.
    """

    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


class SessionRealtimeToolMcpToolRequireApprovalMcpToolApprovalFilter(BaseModel):
    always: Optional[SessionRealtimeToolMcpToolRequireApprovalMcpToolApprovalFilterAlways] = None
    """A filter object to specify which tools are allowed."""

    never: Optional[SessionRealtimeToolMcpToolRequireApprovalMcpToolApprovalFilterNever] = None
    """A filter object to specify which tools are allowed."""


SessionRealtimeToolMcpToolRequireApproval: TypeAlias = Union[
    SessionRealtimeToolMcpToolRequireApprovalMcpToolApprovalFilter, Literal["always", "never"], None
]


class SessionRealtimeToolMcpTool(BaseModel):
    server_label: str
    """A label for this MCP server, used to identify it in tool calls."""

    type: Literal["mcp"]
    """The type of the MCP tool. Always `mcp`."""

    allowed_tools: Optional[SessionRealtimeToolMcpToolAllowedTools] = None
    """List of allowed tool names or a filter object."""

    authorization: Optional[str] = None
    """
    An OAuth access token that can be used with a remote MCP server, either with a
    custom MCP server URL or a service connector. Your application must handle the
    OAuth authorization flow and provide the token here.
    """

    connector_id: Optional[
        Literal[
            "connector_dropbox",
            "connector_gmail",
            "connector_googlecalendar",
            "connector_googledrive",
            "connector_microsoftteams",
            "connector_outlookcalendar",
            "connector_outlookemail",
            "connector_sharepoint",
        ]
    ] = None
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

    headers: Optional[Dict[str, str]] = None
    """Optional HTTP headers to send to the MCP server.

    Use for authentication or other purposes.
    """

    require_approval: Optional[SessionRealtimeToolMcpToolRequireApproval] = None
    """Specify which of the MCP server's tools require approval."""

    server_description: Optional[str] = None
    """Optional description of the MCP server, used to provide more context."""

    server_url: Optional[str] = None
    """The URL for the MCP server.

    One of `server_url` or `connector_id` must be provided.
    """


SessionRealtimeTool: TypeAlias = Union[SessionRealtimeToolRealtimeFunctionTool, SessionRealtimeToolMcpTool]


class SessionRealtimeTracingTracingConfiguration(BaseModel):
    group_id: Optional[str] = None
    """
    The group id to attach to this trace to enable filtering and grouping in the
    Traces Dashboard.
    """

    metadata: Optional[object] = None
    """
    The arbitrary metadata to attach to this trace to enable filtering in the Traces
    Dashboard.
    """

    workflow_name: Optional[str] = None
    """The name of the workflow to attach to this trace.

    This is used to name the trace in the Traces Dashboard.
    """


SessionRealtimeTracing: TypeAlias = Union[Literal["auto"], SessionRealtimeTracingTracingConfiguration, None]


class SessionRealtimeTruncationRetentionRatioTruncation(BaseModel):
    retention_ratio: float
    """
    Fraction of post-instruction conversation tokens to retain (0.0 - 1.0) when the
    conversation exceeds the input token limit.
    """

    type: Literal["retention_ratio"]
    """Use retention ratio truncation."""


SessionRealtimeTruncation: TypeAlias = Union[
    Literal["auto", "disabled"], SessionRealtimeTruncationRetentionRatioTruncation
]


class SessionRealtime(BaseModel):
    client_secret: SessionRealtimeClientSecret
    """Ephemeral key returned by the API."""

    type: Literal["realtime"]
    """The type of session to create. Always `realtime` for the Realtime API."""

    audio: Optional[SessionRealtimeAudio] = None
    """Configuration for input and output audio."""

    include: Optional[List[Literal["item.input_audio_transcription.logprobs"]]] = None
    """Additional fields to include in server outputs.

    `item.input_audio_transcription.logprobs`: Include logprobs for input audio
    transcription.
    """

    instructions: Optional[str] = None
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

    max_output_tokens: Union[int, Literal["inf"], None] = None
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
        None,
    ] = None
    """The Realtime model used for this session."""

    output_modalities: Optional[List[Literal["text", "audio"]]] = None
    """The set of modalities the model can respond with.

    It defaults to `["audio"]`, indicating that the model will respond with audio
    plus a transcript. `["text"]` can be used to make the model respond with text
    only. It is not possible to request both `text` and `audio` at the same time.
    """

    prompt: Optional[SessionRealtimePrompt] = None
    """
    Reference to a prompt template and its variables.
    [Learn more](https://platform.excai.com/docs/guides/text?api-mode=responses#reusable-prompts).
    """

    tool_choice: Optional[SessionRealtimeToolChoice] = None
    """How the model chooses tools.

    Provide one of the string modes or force a specific function/MCP tool.
    """

    tools: Optional[List[SessionRealtimeTool]] = None
    """Tools available to the model."""

    tracing: Optional[SessionRealtimeTracing] = None
    """
    Realtime API can write session traces to the
    [Traces Dashboard](/logs?api=traces). Set to null to disable tracing. Once
    tracing is enabled for a session, the configuration cannot be modified.

    `auto` will create a trace for the session with default values for the workflow
    name, group id, and metadata.
    """

    truncation: Optional[SessionRealtimeTruncation] = None
    """
    Controls how the realtime conversation is truncated prior to model inference.
    The default is `auto`.
    """


class SessionTranscriptionAudioInputFormatAudioPcm(BaseModel):
    rate: Optional[Literal[24000]] = None
    """The sample rate of the audio. Always `24000`."""

    type: Optional[Literal["audio/pcm"]] = None
    """The audio format. Always `audio/pcm`."""


class SessionTranscriptionAudioInputFormatAudioPcmu(BaseModel):
    type: Optional[Literal["audio/pcmu"]] = None
    """The audio format. Always `audio/pcmu`."""


class SessionTranscriptionAudioInputFormatAudioPcma(BaseModel):
    type: Optional[Literal["audio/pcma"]] = None
    """The audio format. Always `audio/pcma`."""


SessionTranscriptionAudioInputFormat: TypeAlias = Annotated[
    Union[
        SessionTranscriptionAudioInputFormatAudioPcm,
        SessionTranscriptionAudioInputFormatAudioPcmu,
        SessionTranscriptionAudioInputFormatAudioPcma,
    ],
    PropertyInfo(discriminator="type"),
]


class SessionTranscriptionAudioInputNoiseReduction(BaseModel):
    type: Optional[Literal["near_field", "far_field"]] = None
    """Type of noise reduction.

    `near_field` is for close-talking microphones such as headphones, `far_field` is
    for far-field microphones such as laptop or conference room microphones.
    """


class SessionTranscriptionAudioInputTranscription(BaseModel):
    language: Optional[str] = None
    """The language of the input audio.

    Supplying the input language in
    [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`)
    format will improve accuracy and latency.
    """

    model: Optional[Literal["whisper-1", "gpt-4o-transcribe-latest", "gpt-4o-mini-transcribe", "gpt-4o-transcribe"]] = (
        None
    )
    """The model to use for transcription.

    Current options are `whisper-1`, `gpt-4o-transcribe-latest`,
    `gpt-4o-mini-transcribe`, and `gpt-4o-transcribe`.
    """

    prompt: Optional[str] = None
    """
    An optional text to guide the model's style or continue a previous audio
    segment. For `whisper-1`, the
    [prompt is a list of keywords](https://platform.excai.com/docs/guides/speech-to-text#prompting).
    For `gpt-4o-transcribe` models, the prompt is a free text string, for example
    "expect words related to technology".
    """


class SessionTranscriptionAudioInputTurnDetection(BaseModel):
    prefix_padding_ms: Optional[int] = None
    """Amount of audio to include before the VAD detected speech (in milliseconds).

    Defaults to 300ms.
    """

    silence_duration_ms: Optional[int] = None
    """Duration of silence to detect speech stop (in milliseconds).

    Defaults to 500ms. With shorter values the model will respond more quickly, but
    may jump in on short pauses from the user.
    """

    threshold: Optional[float] = None
    """Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5.

    A higher threshold will require louder audio to activate the model, and thus
    might perform better in noisy environments.
    """

    type: Optional[str] = None
    """Type of turn detection, only `server_vad` is currently supported."""


class SessionTranscriptionAudioInput(BaseModel):
    format: Optional[SessionTranscriptionAudioInputFormat] = None
    """The PCM audio format. Only a 24kHz sample rate is supported."""

    noise_reduction: Optional[SessionTranscriptionAudioInputNoiseReduction] = None
    """Configuration for input audio noise reduction."""

    transcription: Optional[SessionTranscriptionAudioInputTranscription] = None
    """Configuration of the transcription model."""

    turn_detection: Optional[SessionTranscriptionAudioInputTurnDetection] = None
    """Configuration for turn detection.

    Can be set to `null` to turn off. Server VAD means that the model will detect
    the start and end of speech based on audio volume and respond at the end of user
    speech.
    """


class SessionTranscriptionAudio(BaseModel):
    input: Optional[SessionTranscriptionAudioInput] = None


class SessionTranscription(BaseModel):
    id: str
    """Unique identifier for the session that looks like `sess_1234567890abcdef`."""

    object: str
    """The object type. Always `realtime.transcription_session`."""

    type: Literal["transcription"]
    """The type of session. Always `transcription` for transcription sessions."""

    audio: Optional[SessionTranscriptionAudio] = None
    """Configuration for input audio for the session."""

    expires_at: Optional[int] = None
    """Expiration timestamp for the session, in seconds since epoch."""

    include: Optional[List[Literal["item.input_audio_transcription.logprobs"]]] = None
    """Additional fields to include in server outputs.

    - `item.input_audio_transcription.logprobs`: Include logprobs for input audio
      transcription.
    """


Session: TypeAlias = Annotated[Union[SessionRealtime, SessionTranscription], PropertyInfo(discriminator="type")]


class RealtimeCreateClientSecretResponse(BaseModel):
    expires_at: int
    """Expiration timestamp for the client secret, in seconds since epoch."""

    session: Session
    """The session configuration for either a realtime or transcription session."""

    value: str
    """The generated client secret value."""
