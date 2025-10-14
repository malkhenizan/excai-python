// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';
import * as VectorStoresAPI from './vector-stores';

export class FileBatches extends APIResource {
  /**
   * Create a vector store file batch.
   */
  create(
    vectorStoreId: string,
    body: FileBatchCreateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileBatchCreateResponse> {
    return this._client.post(`/vector_stores/${vectorStoreId}/file_batches`, { body, ...options });
  }

  /**
   * Retrieves a vector store file batch.
   */
  retrieve(
    vectorStoreId: string,
    batchId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileBatchRetrieveResponse> {
    return this._client.get(`/vector_stores/${vectorStoreId}/file_batches/${batchId}`, options);
  }

  /**
   * Cancel a vector store file batch. This attempts to cancel the processing of
   * files in this batch as soon as possible.
   */
  cancel(
    vectorStoreId: string,
    batchId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileBatchCancelResponse> {
    return this._client.post(`/vector_stores/${vectorStoreId}/file_batches/${batchId}/cancel`, options);
  }

  /**
   * Returns a list of vector store files in a batch.
   */
  listFiles(
    vectorStoreId: string,
    batchId: string,
    query?: FileBatchListFilesParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileBatchListFilesResponse>;
  listFiles(
    vectorStoreId: string,
    batchId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileBatchListFilesResponse>;
  listFiles(
    vectorStoreId: string,
    batchId: string,
    query: FileBatchListFilesParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileBatchListFilesResponse> {
    if (isRequestOptions(query)) {
      return this.listFiles(vectorStoreId, batchId, {}, query);
    }
    return this._client.get(`/vector_stores/${vectorStoreId}/file_batches/${batchId}/files`, {
      query,
      ...options,
    });
  }
}

/**
 * A batch of files attached to a vector store.
 */
export interface FileBatchCreateResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the vector store files batch was
   * created.
   */
  created_at: number;

  file_counts: FileBatchCreateResponse.FileCounts;

  /**
   * The object type, which is always `vector_store.file_batch`.
   */
  object: 'vector_store.files_batch';

  /**
   * The status of the vector store files batch, which can be either `in_progress`,
   * `completed`, `cancelled` or `failed`.
   */
  status: 'in_progress' | 'completed' | 'cancelled' | 'failed';

  /**
   * The ID of the
   * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
   * that the [File](https://platform.excai.com/docs/api-reference/files) is attached
   * to.
   */
  vector_store_id: string;
}

export namespace FileBatchCreateResponse {
  export interface FileCounts {
    /**
     * The number of files that where cancelled.
     */
    cancelled: number;

    /**
     * The number of files that have been processed.
     */
    completed: number;

    /**
     * The number of files that have failed to process.
     */
    failed: number;

    /**
     * The number of files that are currently being processed.
     */
    in_progress: number;

    /**
     * The total number of files.
     */
    total: number;
  }
}

/**
 * A batch of files attached to a vector store.
 */
export interface FileBatchRetrieveResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the vector store files batch was
   * created.
   */
  created_at: number;

  file_counts: FileBatchRetrieveResponse.FileCounts;

  /**
   * The object type, which is always `vector_store.file_batch`.
   */
  object: 'vector_store.files_batch';

  /**
   * The status of the vector store files batch, which can be either `in_progress`,
   * `completed`, `cancelled` or `failed`.
   */
  status: 'in_progress' | 'completed' | 'cancelled' | 'failed';

  /**
   * The ID of the
   * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
   * that the [File](https://platform.excai.com/docs/api-reference/files) is attached
   * to.
   */
  vector_store_id: string;
}

export namespace FileBatchRetrieveResponse {
  export interface FileCounts {
    /**
     * The number of files that where cancelled.
     */
    cancelled: number;

    /**
     * The number of files that have been processed.
     */
    completed: number;

    /**
     * The number of files that have failed to process.
     */
    failed: number;

    /**
     * The number of files that are currently being processed.
     */
    in_progress: number;

    /**
     * The total number of files.
     */
    total: number;
  }
}

/**
 * A batch of files attached to a vector store.
 */
export interface FileBatchCancelResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the vector store files batch was
   * created.
   */
  created_at: number;

  file_counts: FileBatchCancelResponse.FileCounts;

  /**
   * The object type, which is always `vector_store.file_batch`.
   */
  object: 'vector_store.files_batch';

  /**
   * The status of the vector store files batch, which can be either `in_progress`,
   * `completed`, `cancelled` or `failed`.
   */
  status: 'in_progress' | 'completed' | 'cancelled' | 'failed';

  /**
   * The ID of the
   * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
   * that the [File](https://platform.excai.com/docs/api-reference/files) is attached
   * to.
   */
  vector_store_id: string;
}

export namespace FileBatchCancelResponse {
  export interface FileCounts {
    /**
     * The number of files that where cancelled.
     */
    cancelled: number;

    /**
     * The number of files that have been processed.
     */
    completed: number;

    /**
     * The number of files that have failed to process.
     */
    failed: number;

    /**
     * The number of files that are currently being processed.
     */
    in_progress: number;

    /**
     * The total number of files.
     */
    total: number;
  }
}

export interface FileBatchListFilesResponse {
  data: Array<FileBatchListFilesResponse.Data>;

  first_id: string;

  has_more: boolean;

  last_id: string;

  object: string;
}

export namespace FileBatchListFilesResponse {
  /**
   * A list of files attached to a vector store.
   */
  export interface Data {
    /**
     * The identifier, which can be referenced in API endpoints.
     */
    id: string;

    /**
     * The Unix timestamp (in seconds) for when the vector store file was created.
     */
    created_at: number;

    /**
     * The last error associated with this vector store file. Will be `null` if there
     * are no errors.
     */
    last_error: Data.LastError | null;

    /**
     * The object type, which is always `vector_store.file`.
     */
    object: 'vector_store.file';

    /**
     * The status of the vector store file, which can be either `in_progress`,
     * `completed`, `cancelled`, or `failed`. The status `completed` indicates that the
     * vector store file is ready for use.
     */
    status: 'in_progress' | 'completed' | 'cancelled' | 'failed';

    /**
     * The total vector store usage in bytes. Note that this may be different from the
     * original file size.
     */
    usage_bytes: number;

    /**
     * The ID of the
     * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
     * that the [File](https://platform.excai.com/docs/api-reference/files) is attached
     * to.
     */
    vector_store_id: string;

    /**
     * Set of 16 key-value pairs that can be attached to an object. This can be useful
     * for storing additional information about the object in a structured format, and
     * querying for objects via API or the dashboard. Keys are strings with a maximum
     * length of 64 characters. Values are strings with a maximum length of 512
     * characters, booleans, or numbers.
     */
    attributes?: { [key: string]: string | number | boolean } | null;

    /**
     * The strategy used to chunk the file.
     */
    chunking_strategy?:
      | VectorStoresAPI.StaticChunkingStrategyResponseParam
      | VectorStoresAPI.OtherChunkingStrategyResponseParam;
  }

  export namespace Data {
    /**
     * The last error associated with this vector store file. Will be `null` if there
     * are no errors.
     */
    export interface LastError {
      /**
       * One of `server_error`, `unsupported_file`, or `invalid_file`.
       */
      code: 'server_error' | 'unsupported_file' | 'invalid_file';

      /**
       * A human-readable description of the error.
       */
      message: string;
    }
  }
}

export interface FileBatchCreateParams {
  /**
   * A list of [File](https://platform.excai.com/docs/api-reference/files) IDs that
   * the vector store should use. Useful for tools like `file_search` that can access
   * files.
   */
  file_ids: Array<string>;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard. Keys are strings with a maximum
   * length of 64 characters. Values are strings with a maximum length of 512
   * characters, booleans, or numbers.
   */
  attributes?: { [key: string]: string | number | boolean } | null;

  /**
   * The chunking strategy used to chunk the file(s). If not set, will use the `auto`
   * strategy. Only applicable if `file_ids` is non-empty.
   */
  chunking_strategy?:
    | VectorStoresAPI.AutoChunkingStrategyRequestParam
    | VectorStoresAPI.StaticChunkingStrategyRequestParam;
}

export interface FileBatchListFilesParams {
  /**
   * A cursor for use in pagination. `after` is an object ID that defines your place
   * in the list. For instance, if you make a list request and receive 100 objects,
   * ending with obj_foo, your subsequent call can include after=obj_foo in order to
   * fetch the next page of the list.
   */
  after?: string;

  /**
   * A cursor for use in pagination. `before` is an object ID that defines your place
   * in the list. For instance, if you make a list request and receive 100 objects,
   * starting with obj_foo, your subsequent call can include before=obj_foo in order
   * to fetch the previous page of the list.
   */
  before?: string;

  /**
   * Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.
   */
  filter?: 'in_progress' | 'completed' | 'failed' | 'cancelled';

  /**
   * A limit on the number of objects to be returned. Limit can range between 1 and
   * 100, and the default is 20.
   */
  limit?: number;

  /**
   * Sort order by the `created_at` timestamp of the objects. `asc` for ascending
   * order and `desc` for descending order.
   */
  order?: 'asc' | 'desc';
}

export declare namespace FileBatches {
  export {
    type FileBatchCreateResponse as FileBatchCreateResponse,
    type FileBatchRetrieveResponse as FileBatchRetrieveResponse,
    type FileBatchCancelResponse as FileBatchCancelResponse,
    type FileBatchListFilesResponse as FileBatchListFilesResponse,
    type FileBatchCreateParams as FileBatchCreateParams,
    type FileBatchListFilesParams as FileBatchListFilesParams,
  };
}
