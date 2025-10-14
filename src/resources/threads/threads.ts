// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';
import * as ThreadsAPI from './threads';
import * as Shared from '../shared';
import * as MessagesAPI from './messages';
import {
  MessageContentImageFileObject,
  MessageContentImageURLObject,
  MessageContentRefusalObject,
  MessageContentTextAnnotationsFileCitationObject,
  MessageContentTextAnnotationsFilePathObject,
  MessageContentTextObject,
  MessageCreateParams,
  MessageCreateResponse,
  MessageDeleteResponse,
  MessageListParams,
  MessageListResponse,
  MessageRetrieveResponse,
  MessageUpdateParams,
  MessageUpdateResponse,
  Messages,
} from './messages';
import * as RunsAPI from './runs/runs';
import {
  AssistantsNamedToolChoice,
  RunCancelResponse,
  RunCreateParams,
  RunCreateResponse,
  RunCreateWithRunParams,
  RunCreateWithRunResponse,
  RunListParams,
  RunListResponse,
  RunRetrieveResponse,
  RunSubmitToolOutputsParams,
  RunSubmitToolOutputsResponse,
  RunToolCallObject,
  RunUpdateParams,
  RunUpdateResponse,
  Runs,
  TruncationObject,
} from './runs/runs';

export class Threads extends APIResource {
  runs: RunsAPI.Runs = new RunsAPI.Runs(this._client);
  messages: MessagesAPI.Messages = new MessagesAPI.Messages(this._client);

  /**
   * Create a thread.
   *
   * @example
   * ```ts
   * const thread = await client.threads.create();
   * ```
   */
  create(body?: ThreadCreateParams, options?: Core.RequestOptions): Core.APIPromise<ThreadCreateResponse>;
  create(options?: Core.RequestOptions): Core.APIPromise<ThreadCreateResponse>;
  create(
    body: ThreadCreateParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<ThreadCreateResponse> {
    if (isRequestOptions(body)) {
      return this.create({}, body);
    }
    return this._client.post('/threads', { body, ...options });
  }

  /**
   * Retrieves a thread.
   *
   * @example
   * ```ts
   * const thread = await client.threads.retrieve('thread_id');
   * ```
   */
  retrieve(threadId: string, options?: Core.RequestOptions): Core.APIPromise<ThreadRetrieveResponse> {
    return this._client.get(`/threads/${threadId}`, options);
  }

  /**
   * Modifies a thread.
   *
   * @example
   * ```ts
   * const thread = await client.threads.update('thread_id');
   * ```
   */
  update(
    threadId: string,
    body: ThreadUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ThreadUpdateResponse> {
    return this._client.post(`/threads/${threadId}`, { body, ...options });
  }

  /**
   * Delete a thread.
   *
   * @example
   * ```ts
   * const thread = await client.threads.delete('thread_id');
   * ```
   */
  delete(threadId: string, options?: Core.RequestOptions): Core.APIPromise<ThreadDeleteResponse> {
    return this._client.delete(`/threads/${threadId}`, options);
  }
}

export interface AssistantToolsFileSearchTypeOnly {
  /**
   * The type of tool being defined: `file_search`
   */
  type: 'file_search';
}

/**
 * Represents a thread that contains
 * [messages](https://platform.excai.com/docs/api-reference/messages).
 */
export interface ThreadCreateResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the thread was created.
   */
  created_at: number;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata: { [key: string]: string } | null;

  /**
   * The object type, which is always `thread`.
   */
  object: 'thread';

  /**
   * A set of resources that are made available to the assistant's tools in this
   * thread. The resources are specific to the type of tool. For example, the
   * `code_interpreter` tool requires a list of file IDs, while the `file_search`
   * tool requires a list of vector store IDs.
   */
  tool_resources: ThreadCreateResponse.ToolResources | null;
}

export namespace ThreadCreateResponse {
  /**
   * A set of resources that are made available to the assistant's tools in this
   * thread. The resources are specific to the type of tool. For example, the
   * `code_interpreter` tool requires a list of file IDs, while the `file_search`
   * tool requires a list of vector store IDs.
   */
  export interface ToolResources {
    code_interpreter?: ToolResources.CodeInterpreter;

    file_search?: ToolResources.FileSearch;
  }

  export namespace ToolResources {
    export interface CodeInterpreter {
      /**
       * A list of [file](https://platform.excai.com/docs/api-reference/files) IDs made
       * available to the `code_interpreter` tool. There can be a maximum of 20 files
       * associated with the tool.
       */
      file_ids?: Array<string>;
    }

    export interface FileSearch {
      /**
       * The
       * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
       * attached to this thread. There can be a maximum of 1 vector store attached to
       * the thread.
       */
      vector_store_ids?: Array<string>;
    }
  }
}

/**
 * Represents a thread that contains
 * [messages](https://platform.excai.com/docs/api-reference/messages).
 */
export interface ThreadRetrieveResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the thread was created.
   */
  created_at: number;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata: { [key: string]: string } | null;

  /**
   * The object type, which is always `thread`.
   */
  object: 'thread';

  /**
   * A set of resources that are made available to the assistant's tools in this
   * thread. The resources are specific to the type of tool. For example, the
   * `code_interpreter` tool requires a list of file IDs, while the `file_search`
   * tool requires a list of vector store IDs.
   */
  tool_resources: ThreadRetrieveResponse.ToolResources | null;
}

export namespace ThreadRetrieveResponse {
  /**
   * A set of resources that are made available to the assistant's tools in this
   * thread. The resources are specific to the type of tool. For example, the
   * `code_interpreter` tool requires a list of file IDs, while the `file_search`
   * tool requires a list of vector store IDs.
   */
  export interface ToolResources {
    code_interpreter?: ToolResources.CodeInterpreter;

    file_search?: ToolResources.FileSearch;
  }

  export namespace ToolResources {
    export interface CodeInterpreter {
      /**
       * A list of [file](https://platform.excai.com/docs/api-reference/files) IDs made
       * available to the `code_interpreter` tool. There can be a maximum of 20 files
       * associated with the tool.
       */
      file_ids?: Array<string>;
    }

    export interface FileSearch {
      /**
       * The
       * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
       * attached to this thread. There can be a maximum of 1 vector store attached to
       * the thread.
       */
      vector_store_ids?: Array<string>;
    }
  }
}

/**
 * Represents a thread that contains
 * [messages](https://platform.excai.com/docs/api-reference/messages).
 */
export interface ThreadUpdateResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the thread was created.
   */
  created_at: number;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata: { [key: string]: string } | null;

  /**
   * The object type, which is always `thread`.
   */
  object: 'thread';

  /**
   * A set of resources that are made available to the assistant's tools in this
   * thread. The resources are specific to the type of tool. For example, the
   * `code_interpreter` tool requires a list of file IDs, while the `file_search`
   * tool requires a list of vector store IDs.
   */
  tool_resources: ThreadUpdateResponse.ToolResources | null;
}

export namespace ThreadUpdateResponse {
  /**
   * A set of resources that are made available to the assistant's tools in this
   * thread. The resources are specific to the type of tool. For example, the
   * `code_interpreter` tool requires a list of file IDs, while the `file_search`
   * tool requires a list of vector store IDs.
   */
  export interface ToolResources {
    code_interpreter?: ToolResources.CodeInterpreter;

    file_search?: ToolResources.FileSearch;
  }

  export namespace ToolResources {
    export interface CodeInterpreter {
      /**
       * A list of [file](https://platform.excai.com/docs/api-reference/files) IDs made
       * available to the `code_interpreter` tool. There can be a maximum of 20 files
       * associated with the tool.
       */
      file_ids?: Array<string>;
    }

    export interface FileSearch {
      /**
       * The
       * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
       * attached to this thread. There can be a maximum of 1 vector store attached to
       * the thread.
       */
      vector_store_ids?: Array<string>;
    }
  }
}

export interface ThreadDeleteResponse {
  id: string;

  deleted: boolean;

  object: 'thread.deleted';
}

export interface ThreadCreateParams {
  /**
   * A list of [messages](https://platform.excai.com/docs/api-reference/messages) to
   * start the thread with.
   */
  messages?: Array<ThreadCreateParams.Message>;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata?: { [key: string]: string } | null;

  /**
   * A set of resources that are made available to the assistant's tools in this
   * thread. The resources are specific to the type of tool. For example, the
   * `code_interpreter` tool requires a list of file IDs, while the `file_search`
   * tool requires a list of vector store IDs.
   */
  tool_resources?: ThreadCreateParams.ToolResources | null;
}

export namespace ThreadCreateParams {
  export interface Message {
    /**
     * The text contents of the message.
     */
    content:
      | string
      | Array<
          MessagesAPI.MessageContentImageFileObject | MessagesAPI.MessageContentImageURLObject | Message.Text
        >;

    /**
     * The role of the entity that is creating the message. Allowed values include:
     *
     * - `user`: Indicates the message is sent by an actual user and should be used in
     *   most cases to represent user-generated messages.
     * - `assistant`: Indicates the message is generated by the assistant. Use this
     *   value to insert messages from the assistant into the conversation.
     */
    role: 'user' | 'assistant';

    /**
     * A list of files attached to the message, and the tools they should be added to.
     */
    attachments?: Array<Message.Attachment> | null;

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

  export namespace Message {
    /**
     * The text content that is part of a message.
     */
    export interface Text {
      /**
       * Text content to be sent to the model
       */
      text: string;

      /**
       * Always `text`.
       */
      type: 'text';
    }

    export interface Attachment {
      /**
       * The ID of the file to attach to the message.
       */
      file_id?: string;

      /**
       * The tools to add this file to.
       */
      tools?: Array<Shared.AssistantToolsCode | ThreadsAPI.AssistantToolsFileSearchTypeOnly>;
    }
  }

  /**
   * A set of resources that are made available to the assistant's tools in this
   * thread. The resources are specific to the type of tool. For example, the
   * `code_interpreter` tool requires a list of file IDs, while the `file_search`
   * tool requires a list of vector store IDs.
   */
  export interface ToolResources {
    code_interpreter?: ToolResources.CodeInterpreter;

    file_search?: ToolResources.FileSearch;
  }

  export namespace ToolResources {
    export interface CodeInterpreter {
      /**
       * A list of [file](https://platform.excai.com/docs/api-reference/files) IDs made
       * available to the `code_interpreter` tool. There can be a maximum of 20 files
       * associated with the tool.
       */
      file_ids?: Array<string>;
    }

    export interface FileSearch {
      /**
       * The
       * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
       * attached to this thread. There can be a maximum of 1 vector store attached to
       * the thread.
       */
      vector_store_ids?: Array<string>;

      /**
       * A helper to create a
       * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
       * with file_ids and attach it to this thread. There can be a maximum of 1 vector
       * store attached to the thread.
       */
      vector_stores?: Array<FileSearch.VectorStore>;
    }

    export namespace FileSearch {
      export interface VectorStore {
        /**
         * The chunking strategy used to chunk the file(s). If not set, will use the `auto`
         * strategy.
         */
        chunking_strategy?: VectorStore.Auto | VectorStore.Static;

        /**
         * A list of [file](https://platform.excai.com/docs/api-reference/files) IDs to add
         * to the vector store. There can be a maximum of 10000 files in a vector store.
         */
        file_ids?: Array<string>;

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

      export namespace VectorStore {
        /**
         * The default strategy. This strategy currently uses a `max_chunk_size_tokens` of
         * `800` and `chunk_overlap_tokens` of `400`.
         */
        export interface Auto {
          /**
           * Always `auto`.
           */
          type: 'auto';
        }

        export interface Static {
          static: Static.Static;

          /**
           * Always `static`.
           */
          type: 'static';
        }

        export namespace Static {
          export interface Static {
            /**
             * The number of tokens that overlap between chunks. The default value is `400`.
             *
             * Note that the overlap must not exceed half of `max_chunk_size_tokens`.
             */
            chunk_overlap_tokens: number;

            /**
             * The maximum number of tokens in each chunk. The default value is `800`. The
             * minimum value is `100` and the maximum value is `4096`.
             */
            max_chunk_size_tokens: number;
          }
        }
      }
    }
  }
}

export interface ThreadUpdateParams {
  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata?: { [key: string]: string } | null;

  /**
   * A set of resources that are made available to the assistant's tools in this
   * thread. The resources are specific to the type of tool. For example, the
   * `code_interpreter` tool requires a list of file IDs, while the `file_search`
   * tool requires a list of vector store IDs.
   */
  tool_resources?: ThreadUpdateParams.ToolResources | null;
}

export namespace ThreadUpdateParams {
  /**
   * A set of resources that are made available to the assistant's tools in this
   * thread. The resources are specific to the type of tool. For example, the
   * `code_interpreter` tool requires a list of file IDs, while the `file_search`
   * tool requires a list of vector store IDs.
   */
  export interface ToolResources {
    code_interpreter?: ToolResources.CodeInterpreter;

    file_search?: ToolResources.FileSearch;
  }

  export namespace ToolResources {
    export interface CodeInterpreter {
      /**
       * A list of [file](https://platform.excai.com/docs/api-reference/files) IDs made
       * available to the `code_interpreter` tool. There can be a maximum of 20 files
       * associated with the tool.
       */
      file_ids?: Array<string>;
    }

    export interface FileSearch {
      /**
       * The
       * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
       * attached to this thread. There can be a maximum of 1 vector store attached to
       * the thread.
       */
      vector_store_ids?: Array<string>;
    }
  }
}

Threads.Runs = Runs;
Threads.Messages = Messages;

export declare namespace Threads {
  export {
    type AssistantToolsFileSearchTypeOnly as AssistantToolsFileSearchTypeOnly,
    type ThreadCreateResponse as ThreadCreateResponse,
    type ThreadRetrieveResponse as ThreadRetrieveResponse,
    type ThreadUpdateResponse as ThreadUpdateResponse,
    type ThreadDeleteResponse as ThreadDeleteResponse,
    type ThreadCreateParams as ThreadCreateParams,
    type ThreadUpdateParams as ThreadUpdateParams,
  };

  export {
    Runs as Runs,
    type AssistantsNamedToolChoice as AssistantsNamedToolChoice,
    type RunToolCallObject as RunToolCallObject,
    type TruncationObject as TruncationObject,
    type RunCreateResponse as RunCreateResponse,
    type RunRetrieveResponse as RunRetrieveResponse,
    type RunUpdateResponse as RunUpdateResponse,
    type RunListResponse as RunListResponse,
    type RunCancelResponse as RunCancelResponse,
    type RunCreateWithRunResponse as RunCreateWithRunResponse,
    type RunSubmitToolOutputsResponse as RunSubmitToolOutputsResponse,
    type RunCreateParams as RunCreateParams,
    type RunUpdateParams as RunUpdateParams,
    type RunListParams as RunListParams,
    type RunCreateWithRunParams as RunCreateWithRunParams,
    type RunSubmitToolOutputsParams as RunSubmitToolOutputsParams,
  };

  export {
    Messages as Messages,
    type MessageContentImageFileObject as MessageContentImageFileObject,
    type MessageContentImageURLObject as MessageContentImageURLObject,
    type MessageContentRefusalObject as MessageContentRefusalObject,
    type MessageContentTextAnnotationsFileCitationObject as MessageContentTextAnnotationsFileCitationObject,
    type MessageContentTextAnnotationsFilePathObject as MessageContentTextAnnotationsFilePathObject,
    type MessageContentTextObject as MessageContentTextObject,
    type MessageCreateResponse as MessageCreateResponse,
    type MessageRetrieveResponse as MessageRetrieveResponse,
    type MessageUpdateResponse as MessageUpdateResponse,
    type MessageListResponse as MessageListResponse,
    type MessageDeleteResponse as MessageDeleteResponse,
    type MessageCreateParams as MessageCreateParams,
    type MessageUpdateParams as MessageUpdateParams,
    type MessageListParams as MessageListParams,
  };
}
