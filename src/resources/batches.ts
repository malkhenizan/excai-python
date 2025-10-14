// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import { isRequestOptions } from '../core';
import * as Core from '../core';
import * as BatchesAPI from './batches';

export class Batches extends APIResource {
  /**
   * Creates and executes a batch from an uploaded file of requests
   */
  create(body: BatchCreateParams, options?: Core.RequestOptions): Core.APIPromise<BatchCreateResponse> {
    return this._client.post('/batches', { body, ...options });
  }

  /**
   * Retrieves a batch.
   */
  retrieve(batchId: string, options?: Core.RequestOptions): Core.APIPromise<BatchRetrieveResponse> {
    return this._client.get(`/batches/${batchId}`, options);
  }

  /**
   * List your organization's batches.
   */
  list(query?: BatchListParams, options?: Core.RequestOptions): Core.APIPromise<BatchListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<BatchListResponse>;
  list(
    query: BatchListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<BatchListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/batches', { query, ...options });
  }

  /**
   * Cancels an in-progress batch. The batch will be in status `cancelling` for up to
   * 10 minutes, before changing to `cancelled`, where it will have partial results
   * (if any) available in the output file.
   */
  cancel(batchId: string, options?: Core.RequestOptions): Core.APIPromise<BatchCancelResponse> {
    return this._client.post(`/batches/${batchId}/cancel`, options);
  }
}

export interface BatchError {
  /**
   * An error code identifying the error type.
   */
  code?: string;

  /**
   * The line number of the input file where the error occurred, if applicable.
   */
  line?: number | null;

  /**
   * A human-readable message providing more details about the error.
   */
  message?: string;

  /**
   * The name of the parameter that caused the error, if applicable.
   */
  param?: string | null;
}

/**
 * The request counts for different statuses within the batch.
 */
export interface BatchRequestCounts {
  /**
   * Number of requests that have been completed successfully.
   */
  completed: number;

  /**
   * Number of requests that have failed.
   */
  failed: number;

  /**
   * Total number of requests in the batch.
   */
  total: number;
}

export interface BatchCreateResponse {
  id: string;

  /**
   * The time frame within which the batch should be processed.
   */
  completion_window: string;

  /**
   * The Unix timestamp (in seconds) for when the batch was created.
   */
  created_at: number;

  /**
   * The EXCai API endpoint used by the batch.
   */
  endpoint: string;

  /**
   * The ID of the input file for the batch.
   */
  input_file_id: string;

  /**
   * The object type, which is always `batch`.
   */
  object: 'batch';

  /**
   * The current status of the batch.
   */
  status:
    | 'validating'
    | 'failed'
    | 'in_progress'
    | 'finalizing'
    | 'completed'
    | 'expired'
    | 'cancelling'
    | 'cancelled';

  /**
   * The Unix timestamp (in seconds) for when the batch was cancelled.
   */
  cancelled_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch started cancelling.
   */
  cancelling_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch was completed.
   */
  completed_at?: number;

  /**
   * The ID of the file containing the outputs of requests with errors.
   */
  error_file_id?: string;

  errors?: BatchCreateResponse.Errors;

  /**
   * The Unix timestamp (in seconds) for when the batch expired.
   */
  expired_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch will expire.
   */
  expires_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch failed.
   */
  failed_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch started finalizing.
   */
  finalizing_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch started processing.
   */
  in_progress_at?: number;

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
   * Model ID used to process the batch, like `gpt-5-2025-08-07`. EXCai offers a wide
   * range of models with different capabilities, performance characteristics, and
   * price points. Refer to the [model guide](https://platform.excai.com/docs/models)
   * to browse and compare available models.
   */
  model?: string;

  /**
   * The ID of the file containing the outputs of successfully executed requests.
   */
  output_file_id?: string;

  /**
   * The request counts for different statuses within the batch.
   */
  request_counts?: BatchRequestCounts;

  /**
   * Represents token usage details including input tokens, output tokens, a
   * breakdown of output tokens, and the total tokens used. Only populated on batches
   * created after September 7, 2025.
   */
  usage?: BatchCreateResponse.Usage;
}

export namespace BatchCreateResponse {
  export interface Errors {
    data?: Array<BatchesAPI.BatchError>;

    /**
     * The object type, which is always `list`.
     */
    object?: string;
  }

  /**
   * Represents token usage details including input tokens, output tokens, a
   * breakdown of output tokens, and the total tokens used. Only populated on batches
   * created after September 7, 2025.
   */
  export interface Usage {
    /**
     * The number of input tokens.
     */
    input_tokens: number;

    /**
     * A detailed breakdown of the input tokens.
     */
    input_tokens_details: Usage.InputTokensDetails;

    /**
     * The number of output tokens.
     */
    output_tokens: number;

    /**
     * A detailed breakdown of the output tokens.
     */
    output_tokens_details: Usage.OutputTokensDetails;

    /**
     * The total number of tokens used.
     */
    total_tokens: number;
  }

  export namespace Usage {
    /**
     * A detailed breakdown of the input tokens.
     */
    export interface InputTokensDetails {
      /**
       * The number of tokens that were retrieved from the cache.
       * [More on prompt caching](https://platform.excai.com/docs/guides/prompt-caching).
       */
      cached_tokens: number;
    }

    /**
     * A detailed breakdown of the output tokens.
     */
    export interface OutputTokensDetails {
      /**
       * The number of reasoning tokens.
       */
      reasoning_tokens: number;
    }
  }
}

export interface BatchRetrieveResponse {
  id: string;

  /**
   * The time frame within which the batch should be processed.
   */
  completion_window: string;

  /**
   * The Unix timestamp (in seconds) for when the batch was created.
   */
  created_at: number;

  /**
   * The EXCai API endpoint used by the batch.
   */
  endpoint: string;

  /**
   * The ID of the input file for the batch.
   */
  input_file_id: string;

  /**
   * The object type, which is always `batch`.
   */
  object: 'batch';

  /**
   * The current status of the batch.
   */
  status:
    | 'validating'
    | 'failed'
    | 'in_progress'
    | 'finalizing'
    | 'completed'
    | 'expired'
    | 'cancelling'
    | 'cancelled';

  /**
   * The Unix timestamp (in seconds) for when the batch was cancelled.
   */
  cancelled_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch started cancelling.
   */
  cancelling_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch was completed.
   */
  completed_at?: number;

  /**
   * The ID of the file containing the outputs of requests with errors.
   */
  error_file_id?: string;

  errors?: BatchRetrieveResponse.Errors;

  /**
   * The Unix timestamp (in seconds) for when the batch expired.
   */
  expired_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch will expire.
   */
  expires_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch failed.
   */
  failed_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch started finalizing.
   */
  finalizing_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch started processing.
   */
  in_progress_at?: number;

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
   * Model ID used to process the batch, like `gpt-5-2025-08-07`. EXCai offers a wide
   * range of models with different capabilities, performance characteristics, and
   * price points. Refer to the [model guide](https://platform.excai.com/docs/models)
   * to browse and compare available models.
   */
  model?: string;

  /**
   * The ID of the file containing the outputs of successfully executed requests.
   */
  output_file_id?: string;

  /**
   * The request counts for different statuses within the batch.
   */
  request_counts?: BatchRequestCounts;

  /**
   * Represents token usage details including input tokens, output tokens, a
   * breakdown of output tokens, and the total tokens used. Only populated on batches
   * created after September 7, 2025.
   */
  usage?: BatchRetrieveResponse.Usage;
}

export namespace BatchRetrieveResponse {
  export interface Errors {
    data?: Array<BatchesAPI.BatchError>;

    /**
     * The object type, which is always `list`.
     */
    object?: string;
  }

  /**
   * Represents token usage details including input tokens, output tokens, a
   * breakdown of output tokens, and the total tokens used. Only populated on batches
   * created after September 7, 2025.
   */
  export interface Usage {
    /**
     * The number of input tokens.
     */
    input_tokens: number;

    /**
     * A detailed breakdown of the input tokens.
     */
    input_tokens_details: Usage.InputTokensDetails;

    /**
     * The number of output tokens.
     */
    output_tokens: number;

    /**
     * A detailed breakdown of the output tokens.
     */
    output_tokens_details: Usage.OutputTokensDetails;

    /**
     * The total number of tokens used.
     */
    total_tokens: number;
  }

  export namespace Usage {
    /**
     * A detailed breakdown of the input tokens.
     */
    export interface InputTokensDetails {
      /**
       * The number of tokens that were retrieved from the cache.
       * [More on prompt caching](https://platform.excai.com/docs/guides/prompt-caching).
       */
      cached_tokens: number;
    }

    /**
     * A detailed breakdown of the output tokens.
     */
    export interface OutputTokensDetails {
      /**
       * The number of reasoning tokens.
       */
      reasoning_tokens: number;
    }
  }
}

export interface BatchListResponse {
  data: Array<BatchListResponse.Data>;

  has_more: boolean;

  object: 'list';

  first_id?: string;

  last_id?: string;
}

export namespace BatchListResponse {
  export interface Data {
    id: string;

    /**
     * The time frame within which the batch should be processed.
     */
    completion_window: string;

    /**
     * The Unix timestamp (in seconds) for when the batch was created.
     */
    created_at: number;

    /**
     * The EXCai API endpoint used by the batch.
     */
    endpoint: string;

    /**
     * The ID of the input file for the batch.
     */
    input_file_id: string;

    /**
     * The object type, which is always `batch`.
     */
    object: 'batch';

    /**
     * The current status of the batch.
     */
    status:
      | 'validating'
      | 'failed'
      | 'in_progress'
      | 'finalizing'
      | 'completed'
      | 'expired'
      | 'cancelling'
      | 'cancelled';

    /**
     * The Unix timestamp (in seconds) for when the batch was cancelled.
     */
    cancelled_at?: number;

    /**
     * The Unix timestamp (in seconds) for when the batch started cancelling.
     */
    cancelling_at?: number;

    /**
     * The Unix timestamp (in seconds) for when the batch was completed.
     */
    completed_at?: number;

    /**
     * The ID of the file containing the outputs of requests with errors.
     */
    error_file_id?: string;

    errors?: Data.Errors;

    /**
     * The Unix timestamp (in seconds) for when the batch expired.
     */
    expired_at?: number;

    /**
     * The Unix timestamp (in seconds) for when the batch will expire.
     */
    expires_at?: number;

    /**
     * The Unix timestamp (in seconds) for when the batch failed.
     */
    failed_at?: number;

    /**
     * The Unix timestamp (in seconds) for when the batch started finalizing.
     */
    finalizing_at?: number;

    /**
     * The Unix timestamp (in seconds) for when the batch started processing.
     */
    in_progress_at?: number;

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
     * Model ID used to process the batch, like `gpt-5-2025-08-07`. EXCai offers a wide
     * range of models with different capabilities, performance characteristics, and
     * price points. Refer to the [model guide](https://platform.excai.com/docs/models)
     * to browse and compare available models.
     */
    model?: string;

    /**
     * The ID of the file containing the outputs of successfully executed requests.
     */
    output_file_id?: string;

    /**
     * The request counts for different statuses within the batch.
     */
    request_counts?: BatchesAPI.BatchRequestCounts;

    /**
     * Represents token usage details including input tokens, output tokens, a
     * breakdown of output tokens, and the total tokens used. Only populated on batches
     * created after September 7, 2025.
     */
    usage?: Data.Usage;
  }

  export namespace Data {
    export interface Errors {
      data?: Array<BatchesAPI.BatchError>;

      /**
       * The object type, which is always `list`.
       */
      object?: string;
    }

    /**
     * Represents token usage details including input tokens, output tokens, a
     * breakdown of output tokens, and the total tokens used. Only populated on batches
     * created after September 7, 2025.
     */
    export interface Usage {
      /**
       * The number of input tokens.
       */
      input_tokens: number;

      /**
       * A detailed breakdown of the input tokens.
       */
      input_tokens_details: Usage.InputTokensDetails;

      /**
       * The number of output tokens.
       */
      output_tokens: number;

      /**
       * A detailed breakdown of the output tokens.
       */
      output_tokens_details: Usage.OutputTokensDetails;

      /**
       * The total number of tokens used.
       */
      total_tokens: number;
    }

    export namespace Usage {
      /**
       * A detailed breakdown of the input tokens.
       */
      export interface InputTokensDetails {
        /**
         * The number of tokens that were retrieved from the cache.
         * [More on prompt caching](https://platform.excai.com/docs/guides/prompt-caching).
         */
        cached_tokens: number;
      }

      /**
       * A detailed breakdown of the output tokens.
       */
      export interface OutputTokensDetails {
        /**
         * The number of reasoning tokens.
         */
        reasoning_tokens: number;
      }
    }
  }
}

export interface BatchCancelResponse {
  id: string;

  /**
   * The time frame within which the batch should be processed.
   */
  completion_window: string;

  /**
   * The Unix timestamp (in seconds) for when the batch was created.
   */
  created_at: number;

  /**
   * The EXCai API endpoint used by the batch.
   */
  endpoint: string;

  /**
   * The ID of the input file for the batch.
   */
  input_file_id: string;

  /**
   * The object type, which is always `batch`.
   */
  object: 'batch';

  /**
   * The current status of the batch.
   */
  status:
    | 'validating'
    | 'failed'
    | 'in_progress'
    | 'finalizing'
    | 'completed'
    | 'expired'
    | 'cancelling'
    | 'cancelled';

  /**
   * The Unix timestamp (in seconds) for when the batch was cancelled.
   */
  cancelled_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch started cancelling.
   */
  cancelling_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch was completed.
   */
  completed_at?: number;

  /**
   * The ID of the file containing the outputs of requests with errors.
   */
  error_file_id?: string;

  errors?: BatchCancelResponse.Errors;

  /**
   * The Unix timestamp (in seconds) for when the batch expired.
   */
  expired_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch will expire.
   */
  expires_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch failed.
   */
  failed_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch started finalizing.
   */
  finalizing_at?: number;

  /**
   * The Unix timestamp (in seconds) for when the batch started processing.
   */
  in_progress_at?: number;

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
   * Model ID used to process the batch, like `gpt-5-2025-08-07`. EXCai offers a wide
   * range of models with different capabilities, performance characteristics, and
   * price points. Refer to the [model guide](https://platform.excai.com/docs/models)
   * to browse and compare available models.
   */
  model?: string;

  /**
   * The ID of the file containing the outputs of successfully executed requests.
   */
  output_file_id?: string;

  /**
   * The request counts for different statuses within the batch.
   */
  request_counts?: BatchRequestCounts;

  /**
   * Represents token usage details including input tokens, output tokens, a
   * breakdown of output tokens, and the total tokens used. Only populated on batches
   * created after September 7, 2025.
   */
  usage?: BatchCancelResponse.Usage;
}

export namespace BatchCancelResponse {
  export interface Errors {
    data?: Array<BatchesAPI.BatchError>;

    /**
     * The object type, which is always `list`.
     */
    object?: string;
  }

  /**
   * Represents token usage details including input tokens, output tokens, a
   * breakdown of output tokens, and the total tokens used. Only populated on batches
   * created after September 7, 2025.
   */
  export interface Usage {
    /**
     * The number of input tokens.
     */
    input_tokens: number;

    /**
     * A detailed breakdown of the input tokens.
     */
    input_tokens_details: Usage.InputTokensDetails;

    /**
     * The number of output tokens.
     */
    output_tokens: number;

    /**
     * A detailed breakdown of the output tokens.
     */
    output_tokens_details: Usage.OutputTokensDetails;

    /**
     * The total number of tokens used.
     */
    total_tokens: number;
  }

  export namespace Usage {
    /**
     * A detailed breakdown of the input tokens.
     */
    export interface InputTokensDetails {
      /**
       * The number of tokens that were retrieved from the cache.
       * [More on prompt caching](https://platform.excai.com/docs/guides/prompt-caching).
       */
      cached_tokens: number;
    }

    /**
     * A detailed breakdown of the output tokens.
     */
    export interface OutputTokensDetails {
      /**
       * The number of reasoning tokens.
       */
      reasoning_tokens: number;
    }
  }
}

export interface BatchCreateParams {
  /**
   * The time frame within which the batch should be processed. Currently only `24h`
   * is supported.
   */
  completion_window: '24h';

  /**
   * The endpoint to be used for all requests in the batch. Currently
   * `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, and `/v1/completions`
   * are supported. Note that `/v1/embeddings` batches are also restricted to a
   * maximum of 50,000 embedding inputs across all requests in the batch.
   */
  endpoint: '/v1/responses' | '/v1/chat/completions' | '/v1/embeddings' | '/v1/completions';

  /**
   * The ID of an uploaded file that contains requests for the new batch.
   *
   * See [upload file](https://platform.excai.com/docs/api-reference/files/create)
   * for how to upload a file.
   *
   * Your input file must be formatted as a
   * [JSONL file](https://platform.excai.com/docs/api-reference/batch/request-input),
   * and must be uploaded with the purpose `batch`. The file can contain up to 50,000
   * requests, and can be up to 200 MB in size.
   */
  input_file_id: string;

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
   * The expiration policy for the output and/or error file that are generated for a
   * batch.
   */
  output_expires_after?: BatchCreateParams.OutputExpiresAfter;
}

export namespace BatchCreateParams {
  /**
   * The expiration policy for the output and/or error file that are generated for a
   * batch.
   */
  export interface OutputExpiresAfter {
    /**
     * Anchor timestamp after which the expiration policy applies. Supported anchors:
     * `created_at`. Note that the anchor is the file creation time, not the time the
     * batch is created.
     */
    anchor: 'created_at';

    /**
     * The number of seconds after the anchor time that the file will expire. Must be
     * between 3600 (1 hour) and 2592000 (30 days).
     */
    seconds: number;
  }
}

export interface BatchListParams {
  /**
   * A cursor for use in pagination. `after` is an object ID that defines your place
   * in the list. For instance, if you make a list request and receive 100 objects,
   * ending with obj_foo, your subsequent call can include after=obj_foo in order to
   * fetch the next page of the list.
   */
  after?: string;

  /**
   * A limit on the number of objects to be returned. Limit can range between 1 and
   * 100, and the default is 20.
   */
  limit?: number;
}

export declare namespace Batches {
  export {
    type BatchError as BatchError,
    type BatchRequestCounts as BatchRequestCounts,
    type BatchCreateResponse as BatchCreateResponse,
    type BatchRetrieveResponse as BatchRetrieveResponse,
    type BatchListResponse as BatchListResponse,
    type BatchCancelResponse as BatchCancelResponse,
    type BatchCreateParams as BatchCreateParams,
    type BatchListParams as BatchListParams,
  };
}
