# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chat import (
    completion_list_params,
    completion_create_params,
    completion_update_params,
    completion_get_messages_params,
)
from ..._base_client import make_request_options
from ...types.chat.completion_list_response import CompletionListResponse
from ...types.chat.completion_create_response import CompletionCreateResponse
from ...types.chat.completion_delete_response import CompletionDeleteResponse
from ...types.chat.completion_update_response import CompletionUpdateResponse
from ...types.chat.completion_retrieve_response import CompletionRetrieveResponse
from ...types.chat.completion_get_messages_response import CompletionGetMessagesResponse

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/malkhenizan/excai-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/malkhenizan/excai-python#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messages: Iterable[completion_create_params.Message],
        model: Union[
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
        ],
        audio: Optional[completion_create_params.Audio] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        function_call: completion_create_params.FunctionCall | Omit = omit,
        functions: Iterable[completion_create_params.Function] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        modalities: Optional[List[Literal["text", "audio"]]] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        prediction: Optional[completion_create_params.Prediction] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        prompt_cache_key: str | Omit = omit,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        safety_identifier: str | Omit = omit,
        seed: Optional[int] | Omit = omit,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: completion_create_params.ToolChoice | Omit = omit,
        tools: Iterable[completion_create_params.Tool] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: str | Omit = omit,
        verbosity: Optional[Literal["low", "medium", "high"]] | Omit = omit,
        web_search_options: completion_create_params.WebSearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """
        **Starting a new project?** We recommend trying
        [Responses](https://platform.excai.com/docs/api-reference/responses) to take
        advantage of the latest EXCai platform features. Compare
        [Chat Completions with Responses](https://platform.excai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

        ---

        Creates a model response for the given chat conversation. Learn more in the
        [text generation](https://platform.excai.com/docs/guides/text-generation),
        [vision](https://platform.excai.com/docs/guides/vision), and
        [audio](https://platform.excai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.excai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.excai.com/docs/models) you use, different message types
              (modalities) are supported, like
              [text](https://platform.excai.com/docs/guides/text-generation),
              [images](https://platform.excai.com/docs/guides/vision), and
              [audio](https://platform.excai.com/docs/guides/audio).

          model: Model ID used to generate the response, like `gpt-4o` or `o3`. EXCai offers a
              wide range of models with different capabilities, performance characteristics,
              and price points. Refer to the
              [model guide](https://platform.excai.com/docs/models) to browse and compare
              available models.

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.excai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.excai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://excai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o-series models](https://platform.excai.com/docs/guides/reasoning).

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Output types that you would like the model to generate. Most models are capable
              of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.excai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt_cache_key: Used by EXCai to cache responses for similar requests to optimize your cache hit
              rates. Replaces the `user` field.
              [Learn more](https://platform.excai.com/docs/guides/prompt-caching).

          reasoning_effort: Constrains effort on reasoning for
              [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
              supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
              effort can result in faster responses and fewer tokens used on reasoning in a
              response.

              Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
              effort.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables the older JSON mode, which
              ensures the message the model generates is valid JSON. Using `json_schema` is
              preferred for models that support it.

          safety_identifier: A stable identifier used to help detect users of your application that may be
              violating EXCai's usage policies. The IDs should be a string that uniquely
              identifies each user. We recommend hashing their username or email address, in
              order to avoid sending us any identifying information.
              [Learn more](https://platform.excai.com/docs/guides/safety-best-practices#safety-identifiers).

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the processing type used for serving the request.

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

          stop: Not supported with latest reasoning models `o3` and `o4-mini`.

              Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.excai.com/docs/guides/distillation) or
              [evals](https://platform.excai.com/docs/guides/evals) products.

              Supports text and image inputs. Note: image inputs over 8MB will be dropped.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              See the
              [Streaming section below](https://platform.excai.com/docs/api-reference/chat/streaming)
              for more information, along with the
              [streaming responses](https://platform.excai.com/docs/guides/streaming-responses)
              guide for more information on how to handle the streaming events.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. You can provide either
              [custom tools](https://platform.excai.com/docs/guides/function-calling#custom-tools)
              or [function tools](https://platform.excai.com/docs/guides/function-calling).

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use
              `prompt_cache_key` instead to maintain caching optimizations. A stable
              identifier for your end-users. Used to boost cache hit rates by better bucketing
              similar requests and to help EXCai detect and prevent abuse.
              [Learn more](https://platform.excai.com/docs/guides/safety-best-practices#safety-identifiers).

          verbosity: Constrains the verbosity of the model's response. Lower values will result in
              more concise responses, while higher values will result in more verbose
              responses. Currently supported values are `low`, `medium`, and `high`.

          web_search_options: This tool searches the web for relevant results to use in a response. Learn more
              about the
              [web search tool](https://platform.excai.com/docs/guides/tools-web-search?api-mode=chat).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "audio": audio,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "modalities": modalities,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "prediction": prediction,
                    "presence_penalty": presence_penalty,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "safety_identifier": safety_identifier,
                    "seed": seed,
                    "service_tier": service_tier,
                    "stop": stop,
                    "store": store,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                    "verbosity": verbosity,
                    "web_search_options": web_search_options,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )

    def retrieve(
        self,
        completion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionRetrieveResponse:
        """Get a stored chat completion.

        Only Chat Completions that have been created with
        the `store` parameter set to `true` will be returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return self._get(
            f"/chat/completions/{completion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionRetrieveResponse,
        )

    def update(
        self,
        completion_id: str,
        *,
        metadata: Optional[Dict[str, str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionUpdateResponse:
        """Modify a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be modified. Currently, the only
        supported modification is to update the `metadata` field.

        Args:
          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return self._post(
            f"/chat/completions/{completion_id}",
            body=maybe_transform({"metadata": metadata}, completion_update_params.CompletionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        model: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionListResponse:
        """List stored Chat Completions.

        Only Chat Completions that have been stored with
        the `store` parameter set to `true` will be returned.

        Args:
          after: Identifier for the last chat completion from the previous pagination request.

          limit: Number of Chat Completions to retrieve.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          model: The model used to generate the Chat Completions.

          order: Sort order for Chat Completions by timestamp. Use `asc` for ascending order or
              `desc` for descending order. Defaults to `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/chat/completions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "metadata": metadata,
                        "model": model,
                        "order": order,
                    },
                    completion_list_params.CompletionListParams,
                ),
            ),
            cast_to=CompletionListResponse,
        )

    def delete(
        self,
        completion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionDeleteResponse:
        """Delete a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return self._delete(
            f"/chat/completions/{completion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionDeleteResponse,
        )

    def get_messages(
        self,
        completion_id: str,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionGetMessagesResponse:
        """Get the messages in a stored chat completion.

        Only Chat Completions that have
        been created with the `store` parameter set to `true` will be returned.

        Args:
          after: Identifier for the last message from the previous pagination request.

          limit: Number of messages to retrieve.

          order: Sort order for messages by timestamp. Use `asc` for ascending order or `desc`
              for descending order. Defaults to `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return self._get(
            f"/chat/completions/{completion_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "order": order,
                    },
                    completion_get_messages_params.CompletionGetMessagesParams,
                ),
            ),
            cast_to=CompletionGetMessagesResponse,
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/malkhenizan/excai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/malkhenizan/excai-python#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messages: Iterable[completion_create_params.Message],
        model: Union[
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
        ],
        audio: Optional[completion_create_params.Audio] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        function_call: completion_create_params.FunctionCall | Omit = omit,
        functions: Iterable[completion_create_params.Function] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        modalities: Optional[List[Literal["text", "audio"]]] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        prediction: Optional[completion_create_params.Prediction] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        prompt_cache_key: str | Omit = omit,
        reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] | Omit = omit,
        response_format: completion_create_params.ResponseFormat | Omit = omit,
        safety_identifier: str | Omit = omit,
        seed: Optional[int] | Omit = omit,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: completion_create_params.ToolChoice | Omit = omit,
        tools: Iterable[completion_create_params.Tool] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: str | Omit = omit,
        verbosity: Optional[Literal["low", "medium", "high"]] | Omit = omit,
        web_search_options: completion_create_params.WebSearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """
        **Starting a new project?** We recommend trying
        [Responses](https://platform.excai.com/docs/api-reference/responses) to take
        advantage of the latest EXCai platform features. Compare
        [Chat Completions with Responses](https://platform.excai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

        ---

        Creates a model response for the given chat conversation. Learn more in the
        [text generation](https://platform.excai.com/docs/guides/text-generation),
        [vision](https://platform.excai.com/docs/guides/vision), and
        [audio](https://platform.excai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.excai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.excai.com/docs/models) you use, different message types
              (modalities) are supported, like
              [text](https://platform.excai.com/docs/guides/text-generation),
              [images](https://platform.excai.com/docs/guides/vision), and
              [audio](https://platform.excai.com/docs/guides/audio).

          model: Model ID used to generate the response, like `gpt-4o` or `o3`. EXCai offers a
              wide range of models with different capabilities, performance characteristics,
              and price points. Refer to the
              [model guide](https://platform.excai.com/docs/models) to browse and compare
              available models.

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.excai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.excai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://excai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o-series models](https://platform.excai.com/docs/guides/reasoning).

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Output types that you would like the model to generate. Most models are capable
              of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.excai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt_cache_key: Used by EXCai to cache responses for similar requests to optimize your cache hit
              rates. Replaces the `user` field.
              [Learn more](https://platform.excai.com/docs/guides/prompt-caching).

          reasoning_effort: Constrains effort on reasoning for
              [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
              supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
              effort can result in faster responses and fewer tokens used on reasoning in a
              response.

              Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
              effort.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables the older JSON mode, which
              ensures the message the model generates is valid JSON. Using `json_schema` is
              preferred for models that support it.

          safety_identifier: A stable identifier used to help detect users of your application that may be
              violating EXCai's usage policies. The IDs should be a string that uniquely
              identifies each user. We recommend hashing their username or email address, in
              order to avoid sending us any identifying information.
              [Learn more](https://platform.excai.com/docs/guides/safety-best-practices#safety-identifiers).

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the processing type used for serving the request.

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

          stop: Not supported with latest reasoning models `o3` and `o4-mini`.

              Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.excai.com/docs/guides/distillation) or
              [evals](https://platform.excai.com/docs/guides/evals) products.

              Supports text and image inputs. Note: image inputs over 8MB will be dropped.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              See the
              [Streaming section below](https://platform.excai.com/docs/api-reference/chat/streaming)
              for more information, along with the
              [streaming responses](https://platform.excai.com/docs/guides/streaming-responses)
              guide for more information on how to handle the streaming events.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. You can provide either
              [custom tools](https://platform.excai.com/docs/guides/function-calling#custom-tools)
              or [function tools](https://platform.excai.com/docs/guides/function-calling).

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use
              `prompt_cache_key` instead to maintain caching optimizations. A stable
              identifier for your end-users. Used to boost cache hit rates by better bucketing
              similar requests and to help EXCai detect and prevent abuse.
              [Learn more](https://platform.excai.com/docs/guides/safety-best-practices#safety-identifiers).

          verbosity: Constrains the verbosity of the model's response. Lower values will result in
              more concise responses, while higher values will result in more verbose
              responses. Currently supported values are `low`, `medium`, and `high`.

          web_search_options: This tool searches the web for relevant results to use in a response. Learn more
              about the
              [web search tool](https://platform.excai.com/docs/guides/tools-web-search?api-mode=chat).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "audio": audio,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "modalities": modalities,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "prediction": prediction,
                    "presence_penalty": presence_penalty,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "safety_identifier": safety_identifier,
                    "seed": seed,
                    "service_tier": service_tier,
                    "stop": stop,
                    "store": store,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                    "verbosity": verbosity,
                    "web_search_options": web_search_options,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )

    async def retrieve(
        self,
        completion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionRetrieveResponse:
        """Get a stored chat completion.

        Only Chat Completions that have been created with
        the `store` parameter set to `true` will be returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return await self._get(
            f"/chat/completions/{completion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionRetrieveResponse,
        )

    async def update(
        self,
        completion_id: str,
        *,
        metadata: Optional[Dict[str, str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionUpdateResponse:
        """Modify a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be modified. Currently, the only
        supported modification is to update the `metadata` field.

        Args:
          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return await self._post(
            f"/chat/completions/{completion_id}",
            body=await async_maybe_transform({"metadata": metadata}, completion_update_params.CompletionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        model: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionListResponse:
        """List stored Chat Completions.

        Only Chat Completions that have been stored with
        the `store` parameter set to `true` will be returned.

        Args:
          after: Identifier for the last chat completion from the previous pagination request.

          limit: Number of Chat Completions to retrieve.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          model: The model used to generate the Chat Completions.

          order: Sort order for Chat Completions by timestamp. Use `asc` for ascending order or
              `desc` for descending order. Defaults to `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/chat/completions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "metadata": metadata,
                        "model": model,
                        "order": order,
                    },
                    completion_list_params.CompletionListParams,
                ),
            ),
            cast_to=CompletionListResponse,
        )

    async def delete(
        self,
        completion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionDeleteResponse:
        """Delete a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return await self._delete(
            f"/chat/completions/{completion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionDeleteResponse,
        )

    async def get_messages(
        self,
        completion_id: str,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionGetMessagesResponse:
        """Get the messages in a stored chat completion.

        Only Chat Completions that have
        been created with the `store` parameter set to `true` will be returned.

        Args:
          after: Identifier for the last message from the previous pagination request.

          limit: Number of messages to retrieve.

          order: Sort order for messages by timestamp. Use `asc` for ascending order or `desc`
              for descending order. Defaults to `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return await self._get(
            f"/chat/completions/{completion_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "order": order,
                    },
                    completion_get_messages_params.CompletionGetMessagesParams,
                ),
            ),
            cast_to=CompletionGetMessagesResponse,
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            completions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            completions.update,
        )
        self.list = to_raw_response_wrapper(
            completions.list,
        )
        self.delete = to_raw_response_wrapper(
            completions.delete,
        )
        self.get_messages = to_raw_response_wrapper(
            completions.get_messages,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            completions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            completions.update,
        )
        self.list = async_to_raw_response_wrapper(
            completions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            completions.delete,
        )
        self.get_messages = async_to_raw_response_wrapper(
            completions.get_messages,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            completions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            completions.update,
        )
        self.list = to_streamed_response_wrapper(
            completions.list,
        )
        self.delete = to_streamed_response_wrapper(
            completions.delete,
        )
        self.get_messages = to_streamed_response_wrapper(
            completions.get_messages,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            completions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            completions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            completions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            completions.delete,
        )
        self.get_messages = async_to_streamed_response_wrapper(
            completions.get_messages,
        )
