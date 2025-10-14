// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';
import * as ResponsesAPI from '../responses';
import * as Shared from '../shared';
import * as ItemsAPI from './items';
import {
  ComputerScreenshotContent,
  CustomToolCallOutput,
  ItemCreateParams,
  ItemCreateResponse,
  ItemDeleteResponse,
  ItemListParams,
  ItemListResponse,
  ItemRetrieveParams,
  ItemRetrieveResponse,
  Items,
  Message as ItemsAPIMessage,
  SummaryTextContent,
  TextContent,
} from './items';
import * as RunsAPI from '../evals/runs/runs';

export class Conversations extends APIResource {
  items: ItemsAPI.Items = new ItemsAPI.Items(this._client);

  /**
   * Create a conversation.
   */
  create(
    body?: ConversationCreateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ConversationCreateResponse>;
  create(options?: Core.RequestOptions): Core.APIPromise<ConversationCreateResponse>;
  create(
    body: ConversationCreateParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<ConversationCreateResponse> {
    if (isRequestOptions(body)) {
      return this.create({}, body);
    }
    return this._client.post('/conversations', { body, ...options });
  }

  /**
   * Get a conversation
   */
  retrieve(
    conversationId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ConversationRetrieveResponse> {
    return this._client.get(`/conversations/${conversationId}`, options);
  }

  /**
   * Update a conversation
   */
  update(
    conversationId: string,
    body: ConversationUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ConversationUpdateResponse> {
    return this._client.post(`/conversations/${conversationId}`, { body, ...options });
  }

  /**
   * Delete a conversation. Items in the conversation will not be deleted.
   */
  delete(conversationId: string, options?: Core.RequestOptions): Core.APIPromise<ConversationDeleteResponse> {
    return this._client.delete(`/conversations/${conversationId}`, options);
  }
}

export interface ConversationCreateResponse {
  /**
   * The unique ID of the conversation.
   */
  id: string;

  /**
   * The time at which the conversation was created, measured in seconds since the
   * Unix epoch.
   */
  created_at: number;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard. Keys are strings with a maximum
   * length of 64 characters. Values are strings with a maximum length of 512
   * characters.
   */
  metadata: unknown;

  /**
   * The object type, which is always `conversation`.
   */
  object: 'conversation';
}

export interface ConversationRetrieveResponse {
  /**
   * The unique ID of the conversation.
   */
  id: string;

  /**
   * The time at which the conversation was created, measured in seconds since the
   * Unix epoch.
   */
  created_at: number;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard. Keys are strings with a maximum
   * length of 64 characters. Values are strings with a maximum length of 512
   * characters.
   */
  metadata: unknown;

  /**
   * The object type, which is always `conversation`.
   */
  object: 'conversation';
}

export interface ConversationUpdateResponse {
  /**
   * The unique ID of the conversation.
   */
  id: string;

  /**
   * The time at which the conversation was created, measured in seconds since the
   * Unix epoch.
   */
  created_at: number;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard. Keys are strings with a maximum
   * length of 64 characters. Values are strings with a maximum length of 512
   * characters.
   */
  metadata: unknown;

  /**
   * The object type, which is always `conversation`.
   */
  object: 'conversation';
}

export interface ConversationDeleteResponse {
  id: string;

  deleted: boolean;

  object: 'conversation.deleted';
}

export interface ConversationCreateParams {
  /**
   * Initial items to include in the conversation context. You may add up to 20 items
   * at a time.
   */
  items?: Array<
    | RunsAPI.EasyInputMessage
    | ConversationCreateParams.Message
    | ResponsesAPI.OutputMessage
    | Shared.FileSearchToolCall
    | Shared.ComputerToolCall
    | ConversationCreateParams.ComputerCallOutput
    | Shared.WebSearchToolCall
    | ResponsesAPI.FunctionToolCall
    | ConversationCreateParams.FunctionCallOutput
    | Shared.ReasoningItem
    | Shared.ImageGenToolCall
    | Shared.CodeInterpreterToolCall
    | Shared.LocalShellToolCall
    | Shared.LocalShellToolCallOutput
    | Shared.McpListTools
    | Shared.McpApprovalRequest
    | ConversationCreateParams.McpApprovalResponse
    | Shared.McpToolCall
    | ItemsAPI.CustomToolCallOutput
    | Shared.CustomToolCall
    | ConversationCreateParams.ItemReference
  > | null;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata?: { [key: string]: string } | null;
}

export namespace ConversationCreateParams {
  /**
   * A message input to the model with a role indicating instruction following
   * hierarchy. Instructions given with the `developer` or `system` role take
   * precedence over instructions given with the `user` role.
   */
  export interface Message {
    /**
     * A list of one or many input items to the model, containing different content
     * types.
     */
    content: Array<
      Shared.InputTextContent | Shared.InputImageContent | Shared.InputFileContent | Shared.InputAudio
    >;

    /**
     * The role of the message input. One of `user`, `system`, or `developer`.
     */
    role: 'user' | 'system' | 'developer';

    /**
     * The status of item. One of `in_progress`, `completed`, or `incomplete`.
     * Populated when items are returned via API.
     */
    status?: 'in_progress' | 'completed' | 'incomplete';

    /**
     * The type of the message input. Always set to `message`.
     */
    type?: 'message';
  }

  /**
   * The output of a computer tool call.
   */
  export interface ComputerCallOutput {
    /**
     * The ID of the computer tool call that produced the output.
     */
    call_id: string;

    /**
     * A computer screenshot image used with the computer use tool.
     */
    output: Shared.ComputerScreenshotImage;

    /**
     * The type of the computer tool call output. Always `computer_call_output`.
     */
    type: 'computer_call_output';

    /**
     * The ID of the computer tool call output.
     */
    id?: string | null;

    /**
     * The safety checks reported by the API that have been acknowledged by the
     * developer.
     */
    acknowledged_safety_checks?: Array<ComputerCallOutput.AcknowledgedSafetyCheck> | null;

    /**
     * The status of the message input. One of `in_progress`, `completed`, or
     * `incomplete`. Populated when input items are returned via API.
     */
    status?: 'in_progress' | 'completed' | 'incomplete' | null;
  }

  export namespace ComputerCallOutput {
    /**
     * A pending safety check for the computer call.
     */
    export interface AcknowledgedSafetyCheck {
      /**
       * The ID of the pending safety check.
       */
      id: string;

      /**
       * The type of the pending safety check.
       */
      code?: string | null;

      /**
       * Details about the pending safety check.
       */
      message?: string | null;
    }
  }

  /**
   * The output of a function tool call.
   */
  export interface FunctionCallOutput {
    /**
     * The unique ID of the function tool call generated by the model.
     */
    call_id: string;

    /**
     * Text, image, or file output of the function tool call.
     */
    output:
      | string
      | Array<FunctionCallOutput.InputText | FunctionCallOutput.InputImage | FunctionCallOutput.InputFile>;

    /**
     * The type of the function tool call output. Always `function_call_output`.
     */
    type: 'function_call_output';

    /**
     * The unique ID of the function tool call output. Populated when this item is
     * returned via API.
     */
    id?: string | null;

    /**
     * The status of the item. One of `in_progress`, `completed`, or `incomplete`.
     * Populated when items are returned via API.
     */
    status?: 'in_progress' | 'completed' | 'incomplete' | null;
  }

  export namespace FunctionCallOutput {
    /**
     * A text input to the model.
     */
    export interface InputText {
      /**
       * The text input to the model.
       */
      text: string;

      /**
       * The type of the input item. Always `input_text`.
       */
      type: 'input_text';
    }

    /**
     * An image input to the model. Learn about
     * [image inputs](https://platform.excai.com/docs/guides/vision)
     */
    export interface InputImage {
      /**
       * The type of the input item. Always `input_image`.
       */
      type: 'input_image';

      /**
       * The detail level of the image to be sent to the model. One of `high`, `low`, or
       * `auto`. Defaults to `auto`.
       */
      detail?: 'low' | 'high' | 'auto' | null;

      /**
       * The ID of the file to be sent to the model.
       */
      file_id?: string | null;

      /**
       * The URL of the image to be sent to the model. A fully qualified URL or base64
       * encoded image in a data URL.
       */
      image_url?: string | null;
    }

    /**
     * A file input to the model.
     */
    export interface InputFile {
      /**
       * The type of the input item. Always `input_file`.
       */
      type: 'input_file';

      /**
       * The base64-encoded data of the file to be sent to the model.
       */
      file_data?: string | null;

      /**
       * The ID of the file to be sent to the model.
       */
      file_id?: string | null;

      /**
       * The URL of the file to be sent to the model.
       */
      file_url?: string | null;

      /**
       * The name of the file to be sent to the model.
       */
      filename?: string | null;
    }
  }

  /**
   * A response to an MCP approval request.
   */
  export interface McpApprovalResponse {
    /**
     * The ID of the approval request being answered.
     */
    approval_request_id: string;

    /**
     * Whether the request was approved.
     */
    approve: boolean;

    /**
     * The type of the item. Always `mcp_approval_response`.
     */
    type: 'mcp_approval_response';

    /**
     * The unique ID of the approval response
     */
    id?: string | null;

    /**
     * Optional reason for the decision.
     */
    reason?: string | null;
  }

  /**
   * An internal identifier for an item to reference.
   */
  export interface ItemReference {
    /**
     * The ID of the item to reference.
     */
    id: string;

    /**
     * The type of item to reference. Always `item_reference`.
     */
    type?: 'item_reference' | null;
  }
}

export interface ConversationUpdateParams {
  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata: { [key: string]: string } | null;
}

Conversations.Items = Items;

export declare namespace Conversations {
  export {
    type ConversationCreateResponse as ConversationCreateResponse,
    type ConversationRetrieveResponse as ConversationRetrieveResponse,
    type ConversationUpdateResponse as ConversationUpdateResponse,
    type ConversationDeleteResponse as ConversationDeleteResponse,
    type ConversationCreateParams as ConversationCreateParams,
    type ConversationUpdateParams as ConversationUpdateParams,
  };

  export {
    Items as Items,
    type ComputerScreenshotContent as ComputerScreenshotContent,
    type CustomToolCallOutput as CustomToolCallOutput,
    type ItemsAPIMessage as Message,
    type SummaryTextContent as SummaryTextContent,
    type TextContent as TextContent,
    type ItemCreateResponse as ItemCreateResponse,
    type ItemRetrieveResponse as ItemRetrieveResponse,
    type ItemListResponse as ItemListResponse,
    type ItemDeleteResponse as ItemDeleteResponse,
    type ItemCreateParams as ItemCreateParams,
    type ItemRetrieveParams as ItemRetrieveParams,
    type ItemListParams as ItemListParams,
  };
}
