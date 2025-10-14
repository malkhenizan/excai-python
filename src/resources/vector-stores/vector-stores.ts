// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';
import * as VectorStoresAPI from './vector-stores';
import * as Shared from '../shared';
import * as FileBatchesAPI from './file-batches';
import {
  FileBatchCancelResponse,
  FileBatchCreateParams,
  FileBatchCreateResponse,
  FileBatchListFilesParams,
  FileBatchListFilesResponse,
  FileBatchRetrieveResponse,
  FileBatches,
} from './file-batches';
import * as FilesAPI from './files';
import {
  FileCreateParams,
  FileCreateResponse,
  FileDeleteResponse,
  FileListParams,
  FileListResponse,
  FileRetrieveContentResponse,
  FileRetrieveResponse,
  FileUpdateParams,
  FileUpdateResponse,
  Files,
} from './files';

export class VectorStores extends APIResource {
  fileBatches: FileBatchesAPI.FileBatches = new FileBatchesAPI.FileBatches(this._client);
  files: FilesAPI.Files = new FilesAPI.Files(this._client);

  /**
   * Create a vector store.
   */
  create(
    body: VectorStoreCreateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<VectorStoreCreateResponse> {
    return this._client.post('/vector_stores', { body, ...options });
  }

  /**
   * Retrieves a vector store.
   */
  retrieve(
    vectorStoreId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<VectorStoreRetrieveResponse> {
    return this._client.get(`/vector_stores/${vectorStoreId}`, options);
  }

  /**
   * Modifies a vector store.
   */
  update(
    vectorStoreId: string,
    body: VectorStoreUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<VectorStoreUpdateResponse> {
    return this._client.post(`/vector_stores/${vectorStoreId}`, { body, ...options });
  }

  /**
   * Returns a list of vector stores.
   */
  list(
    query?: VectorStoreListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<VectorStoreListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<VectorStoreListResponse>;
  list(
    query: VectorStoreListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<VectorStoreListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/vector_stores', { query, ...options });
  }

  /**
   * Delete a vector store.
   */
  delete(vectorStoreId: string, options?: Core.RequestOptions): Core.APIPromise<VectorStoreDeleteResponse> {
    return this._client.delete(`/vector_stores/${vectorStoreId}`, options);
  }

  /**
   * Search a vector store for relevant chunks based on a query and file attributes
   * filter.
   */
  search(
    vectorStoreId: string,
    body: VectorStoreSearchParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<VectorStoreSearchResponse> {
    return this._client.post(`/vector_stores/${vectorStoreId}/search`, { body, ...options });
  }
}

/**
 * The default strategy. This strategy currently uses a `max_chunk_size_tokens` of
 * `800` and `chunk_overlap_tokens` of `400`.
 */
export interface AutoChunkingStrategyRequestParam {
  /**
   * Always `auto`.
   */
  type: 'auto';
}

/**
 * This is returned when the chunking strategy is unknown. Typically, this is
 * because the file was indexed before the `chunking_strategy` concept was
 * introduced in the API.
 */
export interface OtherChunkingStrategyResponseParam {
  /**
   * Always `other`.
   */
  type: 'other';
}

export interface StaticChunkingStrategy {
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

/**
 * Customize your own chunking strategy by setting chunk size and chunk overlap.
 */
export interface StaticChunkingStrategyRequestParam {
  static: StaticChunkingStrategy;

  /**
   * Always `static`.
   */
  type: 'static';
}

export interface StaticChunkingStrategyResponseParam {
  static: StaticChunkingStrategy;

  /**
   * Always `static`.
   */
  type: 'static';
}

/**
 * The expiration policy for a vector store.
 */
export interface VectorStoreExpirationAfter {
  /**
   * Anchor timestamp after which the expiration policy applies. Supported anchors:
   * `last_active_at`.
   */
  anchor: 'last_active_at';

  /**
   * The number of days after the anchor time that the vector store will expire.
   */
  days: number;
}

/**
 * A vector store is a collection of processed files can be used by the
 * `file_search` tool.
 */
export interface VectorStoreCreateResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the vector store was created.
   */
  created_at: number;

  file_counts: VectorStoreCreateResponse.FileCounts;

  /**
   * The Unix timestamp (in seconds) for when the vector store was last active.
   */
  last_active_at: number | null;

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
   * The name of the vector store.
   */
  name: string;

  /**
   * The object type, which is always `vector_store`.
   */
  object: 'vector_store';

  /**
   * The status of the vector store, which can be either `expired`, `in_progress`, or
   * `completed`. A status of `completed` indicates that the vector store is ready
   * for use.
   */
  status: 'expired' | 'in_progress' | 'completed';

  /**
   * The total number of bytes used by the files in the vector store.
   */
  usage_bytes: number;

  /**
   * The expiration policy for a vector store.
   */
  expires_after?: VectorStoreExpirationAfter;

  /**
   * The Unix timestamp (in seconds) for when the vector store will expire.
   */
  expires_at?: number | null;
}

export namespace VectorStoreCreateResponse {
  export interface FileCounts {
    /**
     * The number of files that were cancelled.
     */
    cancelled: number;

    /**
     * The number of files that have been successfully processed.
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
 * A vector store is a collection of processed files can be used by the
 * `file_search` tool.
 */
export interface VectorStoreRetrieveResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the vector store was created.
   */
  created_at: number;

  file_counts: VectorStoreRetrieveResponse.FileCounts;

  /**
   * The Unix timestamp (in seconds) for when the vector store was last active.
   */
  last_active_at: number | null;

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
   * The name of the vector store.
   */
  name: string;

  /**
   * The object type, which is always `vector_store`.
   */
  object: 'vector_store';

  /**
   * The status of the vector store, which can be either `expired`, `in_progress`, or
   * `completed`. A status of `completed` indicates that the vector store is ready
   * for use.
   */
  status: 'expired' | 'in_progress' | 'completed';

  /**
   * The total number of bytes used by the files in the vector store.
   */
  usage_bytes: number;

  /**
   * The expiration policy for a vector store.
   */
  expires_after?: VectorStoreExpirationAfter;

  /**
   * The Unix timestamp (in seconds) for when the vector store will expire.
   */
  expires_at?: number | null;
}

export namespace VectorStoreRetrieveResponse {
  export interface FileCounts {
    /**
     * The number of files that were cancelled.
     */
    cancelled: number;

    /**
     * The number of files that have been successfully processed.
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
 * A vector store is a collection of processed files can be used by the
 * `file_search` tool.
 */
export interface VectorStoreUpdateResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the vector store was created.
   */
  created_at: number;

  file_counts: VectorStoreUpdateResponse.FileCounts;

  /**
   * The Unix timestamp (in seconds) for when the vector store was last active.
   */
  last_active_at: number | null;

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
   * The name of the vector store.
   */
  name: string;

  /**
   * The object type, which is always `vector_store`.
   */
  object: 'vector_store';

  /**
   * The status of the vector store, which can be either `expired`, `in_progress`, or
   * `completed`. A status of `completed` indicates that the vector store is ready
   * for use.
   */
  status: 'expired' | 'in_progress' | 'completed';

  /**
   * The total number of bytes used by the files in the vector store.
   */
  usage_bytes: number;

  /**
   * The expiration policy for a vector store.
   */
  expires_after?: VectorStoreExpirationAfter;

  /**
   * The Unix timestamp (in seconds) for when the vector store will expire.
   */
  expires_at?: number | null;
}

export namespace VectorStoreUpdateResponse {
  export interface FileCounts {
    /**
     * The number of files that were cancelled.
     */
    cancelled: number;

    /**
     * The number of files that have been successfully processed.
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

export interface VectorStoreListResponse {
  data: Array<VectorStoreListResponse.Data>;

  first_id: string;

  has_more: boolean;

  last_id: string;

  object: string;
}

export namespace VectorStoreListResponse {
  /**
   * A vector store is a collection of processed files can be used by the
   * `file_search` tool.
   */
  export interface Data {
    /**
     * The identifier, which can be referenced in API endpoints.
     */
    id: string;

    /**
     * The Unix timestamp (in seconds) for when the vector store was created.
     */
    created_at: number;

    file_counts: Data.FileCounts;

    /**
     * The Unix timestamp (in seconds) for when the vector store was last active.
     */
    last_active_at: number | null;

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
     * The name of the vector store.
     */
    name: string;

    /**
     * The object type, which is always `vector_store`.
     */
    object: 'vector_store';

    /**
     * The status of the vector store, which can be either `expired`, `in_progress`, or
     * `completed`. A status of `completed` indicates that the vector store is ready
     * for use.
     */
    status: 'expired' | 'in_progress' | 'completed';

    /**
     * The total number of bytes used by the files in the vector store.
     */
    usage_bytes: number;

    /**
     * The expiration policy for a vector store.
     */
    expires_after?: VectorStoresAPI.VectorStoreExpirationAfter;

    /**
     * The Unix timestamp (in seconds) for when the vector store will expire.
     */
    expires_at?: number | null;
  }

  export namespace Data {
    export interface FileCounts {
      /**
       * The number of files that were cancelled.
       */
      cancelled: number;

      /**
       * The number of files that have been successfully processed.
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
}

export interface VectorStoreDeleteResponse {
  id: string;

  deleted: boolean;

  object: 'vector_store.deleted';
}

export interface VectorStoreSearchResponse {
  /**
   * The list of search result items.
   */
  data: Array<VectorStoreSearchResponse.Data>;

  /**
   * Indicates if there are more results to fetch.
   */
  has_more: boolean;

  /**
   * The token for the next page, if any.
   */
  next_page: string | null;

  /**
   * The object type, which is always `vector_store.search_results.page`
   */
  object: 'vector_store.search_results.page';

  search_query: Array<string>;
}

export namespace VectorStoreSearchResponse {
  export interface Data {
    /**
     * Set of 16 key-value pairs that can be attached to an object. This can be useful
     * for storing additional information about the object in a structured format, and
     * querying for objects via API or the dashboard. Keys are strings with a maximum
     * length of 64 characters. Values are strings with a maximum length of 512
     * characters, booleans, or numbers.
     */
    attributes: { [key: string]: string | number | boolean } | null;

    /**
     * Content chunks from the file.
     */
    content: Array<Data.Content>;

    /**
     * The ID of the vector store file.
     */
    file_id: string;

    /**
     * The name of the vector store file.
     */
    filename: string;

    /**
     * The similarity score for the result.
     */
    score: number;
  }

  export namespace Data {
    export interface Content {
      /**
       * The text content returned from search.
       */
      text: string;

      /**
       * The type of content.
       */
      type: 'text';
    }
  }
}

export interface VectorStoreCreateParams {
  /**
   * The chunking strategy used to chunk the file(s). If not set, will use the `auto`
   * strategy. Only applicable if `file_ids` is non-empty.
   */
  chunking_strategy?: AutoChunkingStrategyRequestParam | StaticChunkingStrategyRequestParam;

  /**
   * The expiration policy for a vector store.
   */
  expires_after?: VectorStoreExpirationAfter;

  /**
   * A list of [File](https://platform.excai.com/docs/api-reference/files) IDs that
   * the vector store should use. Useful for tools like `file_search` that can access
   * files.
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

  /**
   * The name of the vector store.
   */
  name?: string;
}

export interface VectorStoreUpdateParams {
  /**
   * The expiration policy for a vector store.
   */
  expires_after?: VectorStoreExpirationAfter | null;

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
   * The name of the vector store.
   */
  name?: string | null;
}

export interface VectorStoreListParams {
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

export interface VectorStoreSearchParams {
  /**
   * A query string for a search
   */
  query: string | Array<string>;

  /**
   * A filter to apply based on file attributes.
   */
  filters?: Shared.ComparisonFilter | Shared.CompoundFilter;

  /**
   * The maximum number of results to return. This number should be between 1 and 50
   * inclusive.
   */
  max_num_results?: number;

  /**
   * Ranking options for search.
   */
  ranking_options?: VectorStoreSearchParams.RankingOptions;

  /**
   * Whether to rewrite the natural language query for vector search.
   */
  rewrite_query?: boolean;
}

export namespace VectorStoreSearchParams {
  /**
   * Ranking options for search.
   */
  export interface RankingOptions {
    /**
     * Enable re-ranking; set to `none` to disable, which can help reduce latency.
     */
    ranker?: 'none' | 'auto' | 'default-2024-11-15';

    score_threshold?: number;
  }
}

VectorStores.FileBatches = FileBatches;
VectorStores.Files = Files;

export declare namespace VectorStores {
  export {
    type AutoChunkingStrategyRequestParam as AutoChunkingStrategyRequestParam,
    type OtherChunkingStrategyResponseParam as OtherChunkingStrategyResponseParam,
    type StaticChunkingStrategy as StaticChunkingStrategy,
    type StaticChunkingStrategyRequestParam as StaticChunkingStrategyRequestParam,
    type StaticChunkingStrategyResponseParam as StaticChunkingStrategyResponseParam,
    type VectorStoreExpirationAfter as VectorStoreExpirationAfter,
    type VectorStoreCreateResponse as VectorStoreCreateResponse,
    type VectorStoreRetrieveResponse as VectorStoreRetrieveResponse,
    type VectorStoreUpdateResponse as VectorStoreUpdateResponse,
    type VectorStoreListResponse as VectorStoreListResponse,
    type VectorStoreDeleteResponse as VectorStoreDeleteResponse,
    type VectorStoreSearchResponse as VectorStoreSearchResponse,
    type VectorStoreCreateParams as VectorStoreCreateParams,
    type VectorStoreUpdateParams as VectorStoreUpdateParams,
    type VectorStoreListParams as VectorStoreListParams,
    type VectorStoreSearchParams as VectorStoreSearchParams,
  };

  export {
    FileBatches as FileBatches,
    type FileBatchCreateResponse as FileBatchCreateResponse,
    type FileBatchRetrieveResponse as FileBatchRetrieveResponse,
    type FileBatchCancelResponse as FileBatchCancelResponse,
    type FileBatchListFilesResponse as FileBatchListFilesResponse,
    type FileBatchCreateParams as FileBatchCreateParams,
    type FileBatchListFilesParams as FileBatchListFilesParams,
  };

  export {
    Files as Files,
    type FileCreateResponse as FileCreateResponse,
    type FileRetrieveResponse as FileRetrieveResponse,
    type FileUpdateResponse as FileUpdateResponse,
    type FileListResponse as FileListResponse,
    type FileDeleteResponse as FileDeleteResponse,
    type FileRetrieveContentResponse as FileRetrieveContentResponse,
    type FileCreateParams as FileCreateParams,
    type FileUpdateParams as FileUpdateParams,
    type FileListParams as FileListParams,
  };
}
