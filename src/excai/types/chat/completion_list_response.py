# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "CompletionListResponse",
    "Data",
    "DataChoice",
    "DataChoiceLogprobs",
    "DataChoiceLogprobsContent",
    "DataChoiceLogprobsContentTopLogprob",
    "DataChoiceLogprobsRefusal",
    "DataChoiceLogprobsRefusalTopLogprob",
    "DataChoiceMessage",
    "DataChoiceMessageAnnotation",
    "DataChoiceMessageAnnotationURLCitation",
    "DataChoiceMessageAudio",
    "DataChoiceMessageFunctionCall",
    "DataChoiceMessageToolCall",
    "DataChoiceMessageToolCallFunction",
    "DataUsage",
    "DataUsageCompletionTokensDetails",
    "DataUsagePromptTokensDetails",
]


class DataChoiceLogprobsContentTopLogprob(BaseModel):
    token: str
    """The token."""

    bytes: Optional[List[int]] = None
    """A list of integers representing the UTF-8 bytes representation of the token.

    Useful in instances where characters are represented by multiple tokens and
    their byte representations must be combined to generate the correct text
    representation. Can be `null` if there is no bytes representation for the token.
    """

    logprob: float
    """The log probability of this token, if it is within the top 20 most likely
    tokens.

    Otherwise, the value `-9999.0` is used to signify that the token is very
    unlikely.
    """


class DataChoiceLogprobsContent(BaseModel):
    token: str
    """The token."""

    bytes: Optional[List[int]] = None
    """A list of integers representing the UTF-8 bytes representation of the token.

    Useful in instances where characters are represented by multiple tokens and
    their byte representations must be combined to generate the correct text
    representation. Can be `null` if there is no bytes representation for the token.
    """

    logprob: float
    """The log probability of this token, if it is within the top 20 most likely
    tokens.

    Otherwise, the value `-9999.0` is used to signify that the token is very
    unlikely.
    """

    top_logprobs: List[DataChoiceLogprobsContentTopLogprob]
    """List of the most likely tokens and their log probability, at this token
    position.

    In rare cases, there may be fewer than the number of requested `top_logprobs`
    returned.
    """


class DataChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str
    """The token."""

    bytes: Optional[List[int]] = None
    """A list of integers representing the UTF-8 bytes representation of the token.

    Useful in instances where characters are represented by multiple tokens and
    their byte representations must be combined to generate the correct text
    representation. Can be `null` if there is no bytes representation for the token.
    """

    logprob: float
    """The log probability of this token, if it is within the top 20 most likely
    tokens.

    Otherwise, the value `-9999.0` is used to signify that the token is very
    unlikely.
    """


class DataChoiceLogprobsRefusal(BaseModel):
    token: str
    """The token."""

    bytes: Optional[List[int]] = None
    """A list of integers representing the UTF-8 bytes representation of the token.

    Useful in instances where characters are represented by multiple tokens and
    their byte representations must be combined to generate the correct text
    representation. Can be `null` if there is no bytes representation for the token.
    """

    logprob: float
    """The log probability of this token, if it is within the top 20 most likely
    tokens.

    Otherwise, the value `-9999.0` is used to signify that the token is very
    unlikely.
    """

    top_logprobs: List[DataChoiceLogprobsRefusalTopLogprob]
    """List of the most likely tokens and their log probability, at this token
    position.

    In rare cases, there may be fewer than the number of requested `top_logprobs`
    returned.
    """


class DataChoiceLogprobs(BaseModel):
    content: Optional[List[DataChoiceLogprobsContent]] = None
    """A list of message content tokens with log probability information."""

    refusal: Optional[List[DataChoiceLogprobsRefusal]] = None
    """A list of message refusal tokens with log probability information."""


class DataChoiceMessageAnnotationURLCitation(BaseModel):
    end_index: int
    """The index of the last character of the URL citation in the message."""

    start_index: int
    """The index of the first character of the URL citation in the message."""

    title: str
    """The title of the web resource."""

    url: str
    """The URL of the web resource."""


class DataChoiceMessageAnnotation(BaseModel):
    type: Literal["url_citation"]
    """The type of the URL citation. Always `url_citation`."""

    url_citation: DataChoiceMessageAnnotationURLCitation
    """A URL citation when using web search."""


class DataChoiceMessageAudio(BaseModel):
    id: str
    """Unique identifier for this audio response."""

    data: str
    """
    Base64 encoded audio bytes generated by the model, in the format specified in
    the request.
    """

    expires_at: int
    """
    The Unix timestamp (in seconds) for when this audio response will no longer be
    accessible on the server for use in multi-turn conversations.
    """

    transcript: str
    """Transcript of the audio generated by the model."""


class DataChoiceMessageFunctionCall(BaseModel):
    arguments: str
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: str
    """The name of the function to call."""


class DataChoiceMessageToolCallFunction(BaseModel):
    arguments: str
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: str
    """The name of the function to call."""


class DataChoiceMessageToolCall(BaseModel):
    id: str
    """The ID of the tool call."""

    function: DataChoiceMessageToolCallFunction
    """The function that the model called."""

    type: Literal["function"]
    """The type of the tool. Currently, only `function` is supported."""


class DataChoiceMessage(BaseModel):
    content: Optional[str] = None
    """The contents of the message."""

    refusal: Optional[str] = None
    """The refusal message generated by the model."""

    role: Literal["assistant"]
    """The role of the author of this message."""

    annotations: Optional[List[DataChoiceMessageAnnotation]] = None
    """
    Annotations for the message, when applicable, as when using the
    [web search tool](/docs/guides/tools-web-search?api-mode=chat).
    """

    audio: Optional[DataChoiceMessageAudio] = None
    """
    If the audio output modality is requested, this object contains data about the
    audio response from the model. [Learn more](/docs/guides/audio).
    """

    function_call: Optional[DataChoiceMessageFunctionCall] = None
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the
    model.
    """

    tool_calls: Optional[List[DataChoiceMessageToolCall]] = None
    """The tool calls generated by the model, such as function calls."""


class DataChoice(BaseModel):
    finish_reason: Literal["stop", "length", "tool_calls", "content_filter", "function_call"]
    """The reason the model stopped generating tokens.

    This will be `stop` if the model hit a natural stop point or a provided stop
    sequence, `length` if the maximum number of tokens specified in the request was
    reached, `content_filter` if content was omitted due to a flag from our content
    filters, `tool_calls` if the model called a tool, or `function_call`
    (deprecated) if the model called a function.
    """

    index: int
    """The index of the choice in the list of choices."""

    logprobs: Optional[DataChoiceLogprobs] = None
    """Log probability information for the choice."""

    message: DataChoiceMessage
    """A chat completion message generated by the model."""


class DataUsageCompletionTokensDetails(BaseModel):
    accepted_prediction_tokens: Optional[int] = None
    """
    When using Predicted Outputs, the number of tokens in the prediction that
    appeared in the completion.
    """

    audio_tokens: Optional[int] = None
    """Audio input tokens generated by the model."""

    reasoning_tokens: Optional[int] = None
    """Tokens generated by the model for reasoning."""

    rejected_prediction_tokens: Optional[int] = None
    """
    When using Predicted Outputs, the number of tokens in the prediction that did
    not appear in the completion. However, like reasoning tokens, these tokens are
    still counted in the total completion tokens for purposes of billing, output,
    and context window limits.
    """


class DataUsagePromptTokensDetails(BaseModel):
    audio_tokens: Optional[int] = None
    """Audio input tokens present in the prompt."""

    cached_tokens: Optional[int] = None
    """Cached tokens present in the prompt."""


class DataUsage(BaseModel):
    completion_tokens: int
    """Number of tokens in the generated completion."""

    prompt_tokens: int
    """Number of tokens in the prompt."""

    total_tokens: int
    """Total number of tokens used in the request (prompt + completion)."""

    completion_tokens_details: Optional[DataUsageCompletionTokensDetails] = None
    """Breakdown of tokens used in a completion."""

    prompt_tokens_details: Optional[DataUsagePromptTokensDetails] = None
    """Breakdown of tokens used in the prompt."""


class Data(BaseModel):
    id: str
    """A unique identifier for the chat completion."""

    choices: List[DataChoice]
    """A list of chat completion choices.

    Can be more than one if `n` is greater than 1.
    """

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created."""

    model: str
    """The model used for the chat completion."""

    object: Literal["chat.completion"]
    """The object type, which is always `chat.completion`."""

    service_tier: Optional[Literal["auto", "default", "flex"]] = None
    """Specifies the latency tier to use for processing the request.

    This parameter is relevant for customers subscribed to the scale tier service:

    - If set to 'auto', and the Project is Scale tier enabled, the system will
      utilize scale tier credits until they are exhausted.
    - If set to 'auto', and the Project is not Scale tier enabled, the request will
      be processed using the default service tier with a lower uptime SLA and no
      latency guarentee.
    - If set to 'default', the request will be processed using the default service
      tier with a lower uptime SLA and no latency guarentee.
    - If set to 'flex', the request will be processed with the Flex Processing
      service tier. [Learn more](/docs/guides/flex-processing).
    - When not set, the default behavior is 'auto'.

    When this parameter is set, the response body will include the `service_tier`
    utilized.
    """

    system_fingerprint: Optional[str] = None
    """This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when
    backend changes have been made that might impact determinism.
    """

    usage: Optional[DataUsage] = None
    """Usage statistics for the completion request."""


class CompletionListResponse(BaseModel):
    data: List[Data]
    """An array of chat completion objects."""

    first_id: str
    """The identifier of the first chat completion in the data array."""

    has_more: bool
    """Indicates whether there are more Chat Completions available."""

    last_id: str
    """The identifier of the last chat completion in the data array."""

    object: Literal["list"]
    """The type of this object. It is always set to "list"."""
