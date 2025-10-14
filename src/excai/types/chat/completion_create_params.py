# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "CompletionCreateParams",
    "Message",
    "MessageDeveloper",
    "MessageDeveloperContentArrayOfContentPart",
    "MessageSystem",
    "MessageSystemContentArrayOfContentPart",
    "MessageUser",
    "MessageUserContentArrayOfContentPart",
    "MessageUserContentArrayOfContentPartText",
    "MessageUserContentArrayOfContentPartImageURL",
    "MessageUserContentArrayOfContentPartImageURLImageURL",
    "MessageUserContentArrayOfContentPartInputAudio",
    "MessageUserContentArrayOfContentPartInputAudioInputAudio",
    "MessageUserContentArrayOfContentPartFile",
    "MessageUserContentArrayOfContentPartFileFile",
    "MessageAssistant",
    "MessageAssistantAudio",
    "MessageAssistantContentArrayOfContentPart",
    "MessageAssistantContentArrayOfContentPartText",
    "MessageAssistantContentArrayOfContentPartRefusal",
    "MessageAssistantFunctionCall",
    "MessageAssistantToolCall",
    "MessageAssistantToolCallFunction",
    "MessageAssistantToolCallFunctionFunction",
    "MessageAssistantToolCallCustom",
    "MessageAssistantToolCallCustomCustom",
    "MessageTool",
    "MessageToolContentArrayOfContentPart",
    "MessageFunction",
    "Audio",
    "FunctionCall",
    "FunctionCallFunctionCallOption",
    "Function",
    "Prediction",
    "PredictionContentArrayOfContentPart",
    "ResponseFormat",
    "ResponseFormatResponseFormatText",
    "ResponseFormatResponseFormatJsonSchema",
    "ResponseFormatResponseFormatJsonSchemaJsonSchema",
    "ResponseFormatResponseFormatJsonObject",
    "StreamOptions",
    "ToolChoice",
    "ToolChoiceChatCompletionAllowedToolsChoice",
    "ToolChoiceChatCompletionAllowedToolsChoiceAllowedTools",
    "ToolChoiceChatCompletionNamedToolChoice",
    "ToolChoiceChatCompletionNamedToolChoiceFunction",
    "ToolChoiceChatCompletionNamedToolChoiceCustom",
    "ToolChoiceChatCompletionNamedToolChoiceCustomCustom",
    "Tool",
    "ToolFunction",
    "ToolFunctionFunction",
    "ToolCustom",
    "ToolCustomCustom",
    "ToolCustomCustomFormat",
    "ToolCustomCustomFormatText",
    "ToolCustomCustomFormatGrammar",
    "ToolCustomCustomFormatGrammarGrammar",
    "WebSearchOptions",
    "WebSearchOptionsUserLocation",
    "WebSearchOptionsUserLocationApproximate",
]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """A list of messages comprising the conversation so far.

    Depending on the [model](https://platform.excai.com/docs/models) you use,
    different message types (modalities) are supported, like
    [text](https://platform.excai.com/docs/guides/text-generation),
    [images](https://platform.excai.com/docs/guides/vision), and
    [audio](https://platform.excai.com/docs/guides/audio).
    """

    model: Required[
        Union[
            str,
            Literal[
                "gpt-5",
                "gpt-5-mini",
                "gpt-5-nano",
                "gpt-5-2025-08-07",
                "gpt-5-mini-2025-08-07",
                "gpt-5-nano-2025-08-07",
                "gpt-5-chat-latest",
                "gpt-4.1",
                "gpt-4.1-mini",
                "gpt-4.1-nano",
                "gpt-4.1-2025-04-14",
                "gpt-4.1-mini-2025-04-14",
                "gpt-4.1-nano-2025-04-14",
                "o4-mini",
                "o4-mini-2025-04-16",
                "o3",
                "o3-2025-04-16",
                "o3-mini",
                "o3-mini-2025-01-31",
                "o1",
                "o1-2024-12-17",
                "o1-preview",
                "o1-preview-2024-09-12",
                "o1-mini",
                "o1-mini-2024-09-12",
                "gpt-4o",
                "gpt-4o-2024-11-20",
                "gpt-4o-2024-08-06",
                "gpt-4o-2024-05-13",
                "gpt-4o-audio-preview",
                "gpt-4o-audio-preview-2024-10-01",
                "gpt-4o-audio-preview-2024-12-17",
                "gpt-4o-audio-preview-2025-06-03",
                "gpt-4o-mini-audio-preview",
                "gpt-4o-mini-audio-preview-2024-12-17",
                "gpt-4o-search-preview",
                "gpt-4o-mini-search-preview",
                "gpt-4o-search-preview-2025-03-11",
                "gpt-4o-mini-search-preview-2025-03-11",
                "chatgpt-4o-latest",
                "codex-mini-latest",
                "gpt-4o-mini",
                "gpt-4o-mini-2024-07-18",
                "gpt-4-turbo",
                "gpt-4-turbo-2024-04-09",
                "gpt-4-0125-preview",
                "gpt-4-turbo-preview",
                "gpt-4-1106-preview",
                "gpt-4-vision-preview",
                "gpt-4",
                "gpt-4-0314",
                "gpt-4-0613",
                "gpt-4-32k",
                "gpt-4-32k-0314",
                "gpt-4-32k-0613",
                "gpt-3.5-turbo",
                "gpt-3.5-turbo-16k",
                "gpt-3.5-turbo-0301",
                "gpt-3.5-turbo-0613",
                "gpt-3.5-turbo-1106",
                "gpt-3.5-turbo-0125",
                "gpt-3.5-turbo-16k-0613",
            ],
        ]
    ]
    """Model ID used to generate the response, like `gpt-4o` or `o3`.

    EXCai offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the
    [model guide](https://platform.excai.com/docs/models) to browse and compare
    available models.
    """

    audio: Optional[Audio]
    """Parameters for audio output.

    Required when audio output is requested with `modalities: ["audio"]`.
    [Learn more](https://platform.excai.com/docs/guides/audio).
    """

    frequency_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """

    function_call: FunctionCall
    """Deprecated in favor of `tool_choice`.

    Controls which (if any) function is called by the model.

    `none` means the model will not call a function and instead generates a message.

    `auto` means the model can pick between generating a message or calling a
    function.

    Specifying a particular function via `{"name": "my_function"}` forces the model
    to call that function.

    `none` is the default when no functions are present. `auto` is the default if
    functions are present.
    """

    functions: Iterable[Function]
    """Deprecated in favor of `tools`.

    A list of functions the model may generate JSON inputs for.
    """

    logit_bias: Optional[Dict[str, int]]
    """Modify the likelihood of specified tokens appearing in the completion.

    Accepts a JSON object that maps tokens (specified by their token ID in the
    tokenizer) to an associated bias value from -100 to 100. Mathematically, the
    bias is added to the logits generated by the model prior to sampling. The exact
    effect will vary per model, but values between -1 and 1 should decrease or
    increase likelihood of selection; values like -100 or 100 should result in a ban
    or exclusive selection of the relevant token.
    """

    logprobs: Optional[bool]
    """Whether to return log probabilities of the output tokens or not.

    If true, returns the log probabilities of each output token returned in the
    `content` of `message`.
    """

    max_completion_tokens: Optional[int]
    """
    An upper bound for the number of tokens that can be generated for a completion,
    including visible output tokens and
    [reasoning tokens](https://platform.excai.com/docs/guides/reasoning).
    """

    max_tokens: Optional[int]
    """
    The maximum number of [tokens](/tokenizer) that can be generated in the chat
    completion. This value can be used to control
    [costs](https://excai.com/api/pricing/) for text generated via API.

    This value is now deprecated in favor of `max_completion_tokens`, and is not
    compatible with
    [o-series models](https://platform.excai.com/docs/guides/reasoning).
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    modalities: Optional[List[Literal["text", "audio"]]]
    """
    Output types that you would like the model to generate. Most models are capable
    of generating text, which is the default:

    `["text"]`

    The `gpt-4o-audio-preview` model can also be used to
    [generate audio](https://platform.excai.com/docs/guides/audio). To request that
    this model generate both text and audio responses, you can use:

    `["text", "audio"]`
    """

    n: Optional[int]
    """How many chat completion choices to generate for each input message.

    Note that you will be charged based on the number of generated tokens across all
    of the choices. Keep `n` as `1` to minimize costs.
    """

    parallel_tool_calls: bool
    """
    Whether to enable
    [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
    during tool use.
    """

    prediction: Optional[Prediction]
    """
    Static predicted output content, such as the content of a text file that is
    being regenerated.
    """

    presence_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.
    """

    prompt_cache_key: str
    """
    Used by EXCai to cache responses for similar requests to optimize your cache hit
    rates. Replaces the `user` field.
    [Learn more](https://platform.excai.com/docs/guides/prompt-caching).
    """

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

    response_format: ResponseFormat
    """An object specifying the format that the model must output.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
    Outputs which ensures the model will match your supplied JSON schema. Learn more
    in the
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """

    safety_identifier: str
    """
    A stable identifier used to help detect users of your application that may be
    violating EXCai's usage policies. The IDs should be a string that uniquely
    identifies each user. We recommend hashing their username or email address, in
    order to avoid sending us any identifying information.
    [Learn more](https://platform.excai.com/docs/guides/safety-best-practices#safety-identifiers).
    """

    seed: Optional[int]
    """
    This feature is in Beta. If specified, our system will make a best effort to
    sample deterministically, such that repeated requests with the same `seed` and
    parameters should return the same result. Determinism is not guaranteed, and you
    should refer to the `system_fingerprint` response parameter to monitor changes
    in the backend.
    """

    service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]]
    """Specifies the processing type used for serving the request.

    - If set to 'auto', then the request will be processed with the service tier
      configured in the Project settings. Unless otherwise configured, the Project
      will use 'default'.
    - If set to 'default', then the request will be processed with the standard
      pricing and performance for the selected model.
    - If set to '[flex](https://platform.excai.com/docs/guides/flex-processing)' or
      '[priority](https://excai.com/api-priority-processing/)', then the request
      will be processed with the corresponding service tier.
    - When not set, the default behavior is 'auto'.

    When the `service_tier` parameter is set, the response body will include the
    `service_tier` value based on the processing mode actually used to serve the
    request. This response value may be different from the value set in the
    parameter.
    """

    stop: Union[Optional[str], SequenceNotStr[str], None]
    """Not supported with latest reasoning models `o3` and `o4-mini`.

    Up to 4 sequences where the API will stop generating further tokens. The
    returned text will not contain the stop sequence.
    """

    store: Optional[bool]
    """
    Whether or not to store the output of this chat completion request for use in
    our [model distillation](https://platform.excai.com/docs/guides/distillation) or
    [evals](https://platform.excai.com/docs/guides/evals) products.

    Supports text and image inputs. Note: image inputs over 8MB will be dropped.
    """

    stream: Optional[bool]
    """
    If set to true, the model response data will be streamed to the client as it is
    generated using
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
    See the
    [Streaming section below](https://platform.excai.com/docs/api-reference/chat/streaming)
    for more information, along with the
    [streaming responses](https://platform.excai.com/docs/guides/streaming-responses)
    guide for more information on how to handle the streaming events.
    """

    stream_options: Optional[StreamOptions]
    """Options for streaming response. Only set this when you set `stream: true`."""

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or `top_p` but not both.
    """

    tool_choice: ToolChoice
    """
    Controls which (if any) tool is called by the model. `none` means the model will
    not call any tool and instead generates a message. `auto` means the model can
    pick between generating a message or calling one or more tools. `required` means
    the model must call one or more tools. Specifying a particular tool via
    `{"type": "function", "function": {"name": "my_function"}}` forces the model to
    call that tool.

    `none` is the default when no tools are present. `auto` is the default if tools
    are present.
    """

    tools: Iterable[Tool]
    """A list of tools the model may call.

    You can provide either
    [custom tools](https://platform.excai.com/docs/guides/function-calling#custom-tools)
    or [function tools](https://platform.excai.com/docs/guides/function-calling).
    """

    top_logprobs: Optional[int]
    """
    An integer between 0 and 20 specifying the number of most likely tokens to
    return at each token position, each with an associated log probability.
    `logprobs` must be set to `true` if this parameter is used.
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """

    user: str
    """This field is being replaced by `safety_identifier` and `prompt_cache_key`.

    Use `prompt_cache_key` instead to maintain caching optimizations. A stable
    identifier for your end-users. Used to boost cache hit rates by better bucketing
    similar requests and to help EXCai detect and prevent abuse.
    [Learn more](https://platform.excai.com/docs/guides/safety-best-practices#safety-identifiers).
    """

    verbosity: Optional[Literal["low", "medium", "high"]]
    """Constrains the verbosity of the model's response.

    Lower values will result in more concise responses, while higher values will
    result in more verbose responses. Currently supported values are `low`,
    `medium`, and `high`.
    """

    web_search_options: WebSearchOptions
    """
    This tool searches the web for relevant results to use in a response. Learn more
    about the
    [web search tool](https://platform.excai.com/docs/guides/tools-web-search?api-mode=chat).
    """


class MessageDeveloperContentArrayOfContentPart(TypedDict, total=False):
    text: Required[str]
    """The text content."""

    type: Required[Literal["text"]]
    """The type of the content part."""


class MessageDeveloper(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageDeveloperContentArrayOfContentPart]]]
    """The contents of the developer message."""

    role: Required[Literal["developer"]]
    """The role of the messages author, in this case `developer`."""

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """


class MessageSystemContentArrayOfContentPart(TypedDict, total=False):
    text: Required[str]
    """The text content."""

    type: Required[Literal["text"]]
    """The type of the content part."""


class MessageSystem(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageSystemContentArrayOfContentPart]]]
    """The contents of the system message."""

    role: Required[Literal["system"]]
    """The role of the messages author, in this case `system`."""

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """


class MessageUserContentArrayOfContentPartText(TypedDict, total=False):
    text: Required[str]
    """The text content."""

    type: Required[Literal["text"]]
    """The type of the content part."""


class MessageUserContentArrayOfContentPartImageURLImageURL(TypedDict, total=False):
    url: Required[str]
    """Either a URL of the image or the base64 encoded image data."""

    detail: Literal["auto", "low", "high"]
    """Specifies the detail level of the image.

    Learn more in the
    [Vision guide](https://platform.excai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).
    """


class MessageUserContentArrayOfContentPartImageURL(TypedDict, total=False):
    image_url: Required[MessageUserContentArrayOfContentPartImageURLImageURL]

    type: Required[Literal["image_url"]]
    """The type of the content part."""


class MessageUserContentArrayOfContentPartInputAudioInputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64 encoded audio data."""

    format: Required[Literal["wav", "mp3"]]
    """The format of the encoded audio data. Currently supports "wav" and "mp3"."""


class MessageUserContentArrayOfContentPartInputAudio(TypedDict, total=False):
    input_audio: Required[MessageUserContentArrayOfContentPartInputAudioInputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the content part. Always `input_audio`."""


class MessageUserContentArrayOfContentPartFileFile(TypedDict, total=False):
    file_data: str
    """
    The base64 encoded file data, used when passing the file to the model as a
    string.
    """

    file_id: str
    """The ID of an uploaded file to use as input."""

    filename: str
    """The name of the file, used when passing the file to the model as a string."""


class MessageUserContentArrayOfContentPartFile(TypedDict, total=False):
    file: Required[MessageUserContentArrayOfContentPartFileFile]

    type: Required[Literal["file"]]
    """The type of the content part. Always `file`."""


MessageUserContentArrayOfContentPart: TypeAlias = Union[
    MessageUserContentArrayOfContentPartText,
    MessageUserContentArrayOfContentPartImageURL,
    MessageUserContentArrayOfContentPartInputAudio,
    MessageUserContentArrayOfContentPartFile,
]


class MessageUser(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageUserContentArrayOfContentPart]]]
    """The contents of the user message."""

    role: Required[Literal["user"]]
    """The role of the messages author, in this case `user`."""

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """


class MessageAssistantAudio(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for a previous audio response from the model."""


class MessageAssistantContentArrayOfContentPartText(TypedDict, total=False):
    text: Required[str]
    """The text content."""

    type: Required[Literal["text"]]
    """The type of the content part."""


class MessageAssistantContentArrayOfContentPartRefusal(TypedDict, total=False):
    refusal: Required[str]
    """The refusal message generated by the model."""

    type: Required[Literal["refusal"]]
    """The type of the content part."""


MessageAssistantContentArrayOfContentPart: TypeAlias = Union[
    MessageAssistantContentArrayOfContentPartText, MessageAssistantContentArrayOfContentPartRefusal
]


class MessageAssistantFunctionCall(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class MessageAssistantToolCallFunctionFunction(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class MessageAssistantToolCallFunction(TypedDict, total=False):
    id: Required[str]
    """The ID of the tool call."""

    function: Required[MessageAssistantToolCallFunctionFunction]
    """The function that the model called."""

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class MessageAssistantToolCallCustomCustom(TypedDict, total=False):
    input: Required[str]
    """The input for the custom tool call generated by the model."""

    name: Required[str]
    """The name of the custom tool to call."""


class MessageAssistantToolCallCustom(TypedDict, total=False):
    id: Required[str]
    """The ID of the tool call."""

    custom: Required[MessageAssistantToolCallCustomCustom]
    """The custom tool that the model called."""

    type: Required[Literal["custom"]]
    """The type of the tool. Always `custom`."""


MessageAssistantToolCall: TypeAlias = Union[MessageAssistantToolCallFunction, MessageAssistantToolCallCustom]


class MessageAssistant(TypedDict, total=False):
    role: Required[Literal["assistant"]]
    """The role of the messages author, in this case `assistant`."""

    audio: Optional[MessageAssistantAudio]
    """
    Data about a previous audio response from the model.
    [Learn more](https://platform.excai.com/docs/guides/audio).
    """

    content: Union[str, Iterable[MessageAssistantContentArrayOfContentPart], None]
    """The contents of the assistant message.

    Required unless `tool_calls` or `function_call` is specified.
    """

    function_call: Optional[MessageAssistantFunctionCall]
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the
    model.
    """

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """

    refusal: Optional[str]
    """The refusal message by the assistant."""

    tool_calls: Iterable[MessageAssistantToolCall]
    """The tool calls generated by the model, such as function calls."""


class MessageToolContentArrayOfContentPart(TypedDict, total=False):
    text: Required[str]
    """The text content."""

    type: Required[Literal["text"]]
    """The type of the content part."""


class MessageTool(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageToolContentArrayOfContentPart]]]
    """The contents of the tool message."""

    role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""

    tool_call_id: Required[str]
    """Tool call that this message is responding to."""


class MessageFunction(TypedDict, total=False):
    content: Required[Optional[str]]
    """The contents of the function message."""

    name: Required[str]
    """The name of the function to call."""

    role: Required[Literal["function"]]
    """The role of the messages author, in this case `function`."""


Message: TypeAlias = Union[MessageDeveloper, MessageSystem, MessageUser, MessageAssistant, MessageTool, MessageFunction]


class Audio(TypedDict, total=False):
    format: Required[Literal["wav", "aac", "mp3", "flac", "opus", "pcm16"]]
    """Specifies the output audio format.

    Must be one of `wav`, `mp3`, `flac`, `opus`, or `pcm16`.
    """

    voice: Required[
        Union[str, Literal["alloy", "ash", "ballad", "coral", "echo", "sage", "shimmer", "verse", "marin", "cedar"]]
    ]
    """The voice the model uses to respond.

    Supported voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`,
    `onyx`, `sage`, and `shimmer`.
    """


class FunctionCallFunctionCallOption(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""


FunctionCall: TypeAlias = Union[Literal["none", "auto"], FunctionCallFunctionCallOption]


class Function(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Dict[str, object]
    """The parameters the functions accepts, described as a JSON Schema object.

    See the [guide](https://platform.excai.com/docs/guides/function-calling) for
    examples, and the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.
    """


class PredictionContentArrayOfContentPart(TypedDict, total=False):
    text: Required[str]
    """The text content."""

    type: Required[Literal["text"]]
    """The type of the content part."""


class Prediction(TypedDict, total=False):
    content: Required[Union[str, Iterable[PredictionContentArrayOfContentPart]]]
    """
    The content that should be matched when generating a model response. If
    generated tokens would match this content, the entire model response can be
    returned much more quickly.
    """

    type: Required[Literal["content"]]
    """The type of the predicted content you want to provide.

    This type is currently always `content`.
    """


class ResponseFormatResponseFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]
    """The type of response format being defined. Always `text`."""


class ResponseFormatResponseFormatJsonSchemaJsonSchema(TypedDict, total=False):
    name: Required[str]
    """The name of the response format.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the response format is for, used by the model to determine
    how to respond in the format.
    """

    schema: Dict[str, object]
    """
    The schema for the response format, described as a JSON Schema object. Learn how
    to build JSON schemas [here](https://json-schema.org/).
    """

    strict: Optional[bool]
    """
    Whether to enable strict schema adherence when generating the output. If set to
    true, the model will always follow the exact schema defined in the `schema`
    field. Only a subset of JSON Schema is supported when `strict` is `true`. To
    learn more, read the
    [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
    """


class ResponseFormatResponseFormatJsonSchema(TypedDict, total=False):
    json_schema: Required[ResponseFormatResponseFormatJsonSchemaJsonSchema]
    """Structured Outputs configuration options, including a JSON Schema."""

    type: Required[Literal["json_schema"]]
    """The type of response format being defined. Always `json_schema`."""


class ResponseFormatResponseFormatJsonObject(TypedDict, total=False):
    type: Required[Literal["json_object"]]
    """The type of response format being defined. Always `json_object`."""


ResponseFormat: TypeAlias = Union[
    ResponseFormatResponseFormatText, ResponseFormatResponseFormatJsonSchema, ResponseFormatResponseFormatJsonObject
]


class StreamOptions(TypedDict, total=False):
    include_obfuscation: bool
    """When true, stream obfuscation will be enabled.

    Stream obfuscation adds random characters to an `obfuscation` field on streaming
    delta events to normalize payload sizes as a mitigation to certain side-channel
    attacks. These obfuscation fields are included by default, but add a small
    amount of overhead to the data stream. You can set `include_obfuscation` to
    false to optimize for bandwidth if you trust the network links between your
    application and the EXCai API.
    """

    include_usage: bool
    """If set, an additional chunk will be streamed before the `data: [DONE]` message.

    The `usage` field on this chunk shows the token usage statistics for the entire
    request, and the `choices` field will always be an empty array.

    All other chunks will also include a `usage` field, but with a null value.
    **NOTE:** If the stream is interrupted, you may not receive the final usage
    chunk which contains the total token usage for the request.
    """


class ToolChoiceChatCompletionAllowedToolsChoiceAllowedTools(TypedDict, total=False):
    mode: Required[Literal["auto", "required"]]
    """Constrains the tools available to the model to a pre-defined set.

    `auto` allows the model to pick from among the allowed tools and generate a
    message.

    `required` requires the model to call one or more of the allowed tools.
    """

    tools: Required[Iterable[Dict[str, object]]]
    """A list of tool definitions that the model should be allowed to call.

    For the Chat Completions API, the list of tool definitions might look like:

    ```json
    [
      { "type": "function", "function": { "name": "get_weather" } },
      { "type": "function", "function": { "name": "get_time" } }
    ]
    ```
    """


class ToolChoiceChatCompletionAllowedToolsChoice(TypedDict, total=False):
    allowed_tools: Required[ToolChoiceChatCompletionAllowedToolsChoiceAllowedTools]
    """Constrains the tools available to the model to a pre-defined set."""

    type: Required[Literal["allowed_tools"]]
    """Allowed tool configuration type. Always `allowed_tools`."""


class ToolChoiceChatCompletionNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""


class ToolChoiceChatCompletionNamedToolChoice(TypedDict, total=False):
    function: Required[ToolChoiceChatCompletionNamedToolChoiceFunction]

    type: Required[Literal["function"]]
    """For function calling, the type is always `function`."""


class ToolChoiceChatCompletionNamedToolChoiceCustomCustom(TypedDict, total=False):
    name: Required[str]
    """The name of the custom tool to call."""


class ToolChoiceChatCompletionNamedToolChoiceCustom(TypedDict, total=False):
    custom: Required[ToolChoiceChatCompletionNamedToolChoiceCustomCustom]

    type: Required[Literal["custom"]]
    """For custom tool calling, the type is always `custom`."""


ToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"],
    ToolChoiceChatCompletionAllowedToolsChoice,
    ToolChoiceChatCompletionNamedToolChoice,
    ToolChoiceChatCompletionNamedToolChoiceCustom,
]


class ToolFunctionFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Dict[str, object]
    """The parameters the functions accepts, described as a JSON Schema object.

    See the [guide](https://platform.excai.com/docs/guides/function-calling) for
    examples, and the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.
    """

    strict: Optional[bool]
    """Whether to enable strict schema adherence when generating the function call.

    If set to true, the model will follow the exact schema defined in the
    `parameters` field. Only a subset of JSON Schema is supported when `strict` is
    `true`. Learn more about Structured Outputs in the
    [function calling guide](https://platform.excai.com/docs/guides/function-calling).
    """


class ToolFunction(TypedDict, total=False):
    function: Required[ToolFunctionFunction]

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class ToolCustomCustomFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]
    """Unconstrained text format. Always `text`."""


class ToolCustomCustomFormatGrammarGrammar(TypedDict, total=False):
    definition: Required[str]
    """The grammar definition."""

    syntax: Required[Literal["lark", "regex"]]
    """The syntax of the grammar definition. One of `lark` or `regex`."""


class ToolCustomCustomFormatGrammar(TypedDict, total=False):
    grammar: Required[ToolCustomCustomFormatGrammarGrammar]
    """Your chosen grammar."""

    type: Required[Literal["grammar"]]
    """Grammar format. Always `grammar`."""


ToolCustomCustomFormat: TypeAlias = Union[ToolCustomCustomFormatText, ToolCustomCustomFormatGrammar]


class ToolCustomCustom(TypedDict, total=False):
    name: Required[str]
    """The name of the custom tool, used to identify it in tool calls."""

    description: str
    """Optional description of the custom tool, used to provide more context."""

    format: ToolCustomCustomFormat
    """The input format for the custom tool. Default is unconstrained text."""


class ToolCustom(TypedDict, total=False):
    custom: Required[ToolCustomCustom]
    """Properties of the custom tool."""

    type: Required[Literal["custom"]]
    """The type of the custom tool. Always `custom`."""


Tool: TypeAlias = Union[ToolFunction, ToolCustom]


class WebSearchOptionsUserLocationApproximate(TypedDict, total=False):
    city: str
    """Free text input for the city of the user, e.g. `San Francisco`."""

    country: str
    """
    The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of
    the user, e.g. `US`.
    """

    region: str
    """Free text input for the region of the user, e.g. `California`."""

    timezone: str
    """
    The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the
    user, e.g. `America/Los_Angeles`.
    """


class WebSearchOptionsUserLocation(TypedDict, total=False):
    approximate: Required[WebSearchOptionsUserLocationApproximate]
    """Approximate location parameters for the search."""

    type: Required[Literal["approximate"]]
    """The type of location approximation. Always `approximate`."""


class WebSearchOptions(TypedDict, total=False):
    search_context_size: Literal["low", "medium", "high"]
    """
    High level guidance for the amount of context window space to use for the
    search. One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[WebSearchOptionsUserLocation]
    """Approximate location parameters for the search."""
