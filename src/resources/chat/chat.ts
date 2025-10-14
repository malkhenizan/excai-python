// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import * as CompletionsAPI from './completions';
import {
  ChatCompletionMessageCustomToolCall,
  ChatCompletionMessageToolCall,
  ChatCompletionResponseMessage,
  ChatCompletionTokenLogprob,
  CompletionCreateParams,
  CompletionCreateResponse,
  CompletionDeleteResponse,
  CompletionGetMessagesParams,
  CompletionGetMessagesResponse,
  CompletionListParams,
  CompletionListResponse,
  CompletionRetrieveResponse,
  CompletionUpdateParams,
  CompletionUpdateResponse,
  Completions,
} from './completions';

export class Chat extends APIResource {
  completions: CompletionsAPI.Completions = new CompletionsAPI.Completions(this._client);
}

Chat.Completions = Completions;

export declare namespace Chat {
  export {
    Completions as Completions,
    type ChatCompletionMessageCustomToolCall as ChatCompletionMessageCustomToolCall,
    type ChatCompletionMessageToolCall as ChatCompletionMessageToolCall,
    type ChatCompletionResponseMessage as ChatCompletionResponseMessage,
    type ChatCompletionTokenLogprob as ChatCompletionTokenLogprob,
    type CompletionCreateResponse as CompletionCreateResponse,
    type CompletionRetrieveResponse as CompletionRetrieveResponse,
    type CompletionUpdateResponse as CompletionUpdateResponse,
    type CompletionListResponse as CompletionListResponse,
    type CompletionDeleteResponse as CompletionDeleteResponse,
    type CompletionGetMessagesResponse as CompletionGetMessagesResponse,
    type CompletionCreateParams as CompletionCreateParams,
    type CompletionUpdateParams as CompletionUpdateParams,
    type CompletionListParams as CompletionListParams,
    type CompletionGetMessagesParams as CompletionGetMessagesParams,
  };
}
