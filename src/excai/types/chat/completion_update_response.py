# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "CompletionUpdateResponse",
    "Choice",
    "ChoiceLogprobs",
    "ChoiceLogprobsContent",
    "ChoiceLogprobsContentTopLogprob",
    "ChoiceLogprobsRefusal",
    "ChoiceLogprobsRefusalTopLogprob",
    "ChoiceMessage",
    "ChoiceMessageAnnotation",
    "ChoiceMessageAnnotationURLCitation",
    "ChoiceMessageAudio",
    "ChoiceMessageFunctionCall",
    "ChoiceMessageToolCall",
    "ChoiceMessageToolCallFunction",
    "ChoiceMessageToolCallFunctionFunction",
    "ChoiceMessageToolCallCustom",
    "ChoiceMessageToolCallCustomCustom",
    "Usage",
    "UsageCompletionTokensDetails",
    "UsagePromptTokensDetails",
]


class ChoiceLogprobsContentTopLogprob(BaseModel):
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


class ChoiceLogprobsContent(BaseModel):
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

    top_logprobs: List[ChoiceLogprobsContentTopLogprob]
    """List of the most likely tokens and their log probability, at this token
    position.

    In rare cases, there may be fewer than the number of requested `top_logprobs`
    returned.
    """


class ChoiceLogprobsRefusalTopLogprob(BaseModel):
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


class ChoiceLogprobsRefusal(BaseModel):
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

    top_logprobs: List[ChoiceLogprobsRefusalTopLogprob]
    """List of the most likely tokens and their log probability, at this token
    position.

    In rare cases, there may be fewer than the number of requested `top_logprobs`
    returned.
    """


class ChoiceLogprobs(BaseModel):
    content: Optional[List[ChoiceLogprobsContent]] = None
    """A list of message content tokens with log probability information."""

    refusal: Optional[List[ChoiceLogprobsRefusal]] = None
    """A list of message refusal tokens with log probability information."""


class ChoiceMessageAnnotationURLCitation(BaseModel):
    end_index: int
    """The index of the last character of the URL citation in the message."""

    start_index: int
    """The index of the first character of the URL citation in the message."""

    title: str
    """The title of the web resource."""

    url: str
    """The URL of the web resource."""


class ChoiceMessageAnnotation(BaseModel):
    type: Literal["url_citation"]
    """The type of the URL citation. Always `url_citation`."""

    url_citation: ChoiceMessageAnnotationURLCitation
    """A URL citation when using web search."""


class ChoiceMessageAudio(BaseModel):
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


class ChoiceMessageFunctionCall(BaseModel):
    arguments: str
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: str
    """The name of the function to call."""


class ChoiceMessageToolCallFunctionFunction(BaseModel):
    arguments: str
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: str
    """The name of the function to call."""


class ChoiceMessageToolCallFunction(BaseModel):
    id: str
    """The ID of the tool call."""

    function: ChoiceMessageToolCallFunctionFunction
    """The function that the model called."""

    type: Literal["function"]
    """The type of the tool. Currently, only `function` is supported."""


class ChoiceMessageToolCallCustomCustom(BaseModel):
    input: str
    """The input for the custom tool call generated by the model."""

    name: str
    """The name of the custom tool to call."""


class ChoiceMessageToolCallCustom(BaseModel):
    id: str
    """The ID of the tool call."""

    custom: ChoiceMessageToolCallCustomCustom
    """The custom tool that the model called."""

    type: Literal["custom"]
    """The type of the tool. Always `custom`."""


ChoiceMessageToolCall: TypeAlias = Annotated[
    Union[ChoiceMessageToolCallFunction, ChoiceMessageToolCallCustom], PropertyInfo(discriminator="type")
]


class ChoiceMessage(BaseModel):
    content: Optional[str] = None
    """The contents of the message."""

    refusal: Optional[str] = None
    """The refusal message generated by the model."""

    role: Literal["assistant"]
    """The role of the author of this message."""

    annotations: Optional[List[ChoiceMessageAnnotation]] = None
    """
    Annotations for the message, when applicable, as when using the
    [web search tool](https://platform.excai.com/docs/guides/tools-web-search?api-mode=chat).
    """

    audio: Optional[ChoiceMessageAudio] = None
    """
    If the audio output modality is requested, this object contains data about the
    audio response from the model.
    [Learn more](https://platform.excai.com/docs/guides/audio).
    """

    function_call: Optional[ChoiceMessageFunctionCall] = None
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the
    model.
    """

    tool_calls: Optional[List[ChoiceMessageToolCall]] = None
    """The tool calls generated by the model, such as function calls."""


class Choice(BaseModel):
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

    logprobs: Optional[ChoiceLogprobs] = None
    """Log probability information for the choice."""

    message: ChoiceMessage
    """A chat completion message generated by the model."""


class UsageCompletionTokensDetails(BaseModel):
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


class UsagePromptTokensDetails(BaseModel):
    audio_tokens: Optional[int] = None
    """Audio input tokens present in the prompt."""

    cached_tokens: Optional[int] = None
    """Cached tokens present in the prompt."""


class Usage(BaseModel):
    completion_tokens: int
    """Number of tokens in the generated completion."""

    prompt_tokens: int
    """Number of tokens in the prompt."""

    total_tokens: int
    """Total number of tokens used in the request (prompt + completion)."""

    completion_tokens_details: Optional[UsageCompletionTokensDetails] = None
    """Breakdown of tokens used in a completion."""

    prompt_tokens_details: Optional[UsagePromptTokensDetails] = None
    """Breakdown of tokens used in the prompt."""


class CompletionUpdateResponse(BaseModel):
    id: str
    """A unique identifier for the chat completion."""

    choices: List[Choice]
    """A list of chat completion choices.

    Can be more than one if `n` is greater than 1.
    """

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created."""

    model: str
    """The model used for the chat completion."""

    object: Literal["chat.completion"]
    """The object type, which is always `chat.completion`."""

    service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] = None
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

    system_fingerprint: Optional[str] = None
    """This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when
    backend changes have been made that might impact determinism.
    """

    usage: Optional[Usage] = None
    """Usage statistics for the completion request."""
