// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';
import * as VectorStoresAPI from './vector-stores';

export class Files extends APIResource {
  /**
   * Create a vector store file by attaching a
   * [File](https://platform.excai.com/docs/api-reference/files) to a
   * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object).
   */
  create(
    vectorStoreId: string,
    body: FileCreateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileCreateResponse> {
    return this._client.post(`/vector_stores/${vectorStoreId}/files`, { body, ...options });
  }

  /**
   * Retrieves a vector store file.
   */
  retrieve(
    vectorStoreId: string,
    fileId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileRetrieveResponse> {
    return this._client.get(`/vector_stores/${vectorStoreId}/files/${fileId}`, options);
  }

  /**
   * Update attributes on a vector store file.
   */
  update(
    vectorStoreId: string,
    fileId: string,
    body: FileUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileUpdateResponse> {
    return this._client.post(`/vector_stores/${vectorStoreId}/files/${fileId}`, { body, ...options });
  }

  /**
   * Returns a list of vector store files.
   */
  list(
    vectorStoreId: string,
    query?: FileListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileListResponse>;
  list(vectorStoreId: string, options?: Core.RequestOptions): Core.APIPromise<FileListResponse>;
  list(
    vectorStoreId: string,
    query: FileListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileListResponse> {
    if (isRequestOptions(query)) {
      return this.list(vectorStoreId, {}, query);
    }
    return this._client.get(`/vector_stores/${vectorStoreId}/files`, { query, ...options });
  }

  /**
   * Delete a vector store file. This will remove the file from the vector store but
   * the file itself will not be deleted. To delete the file, use the
   * [delete file](https://platform.excai.com/docs/api-reference/files/delete)
   * endpoint.
   */
  delete(
    vectorStoreId: string,
    fileId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileDeleteResponse> {
    return this._client.delete(`/vector_stores/${vectorStoreId}/files/${fileId}`, options);
  }

  /**
   * Retrieve the parsed contents of a vector store file.
   */
  retrieveContent(
    vectorStoreId: string,
    fileId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileRetrieveContentResponse> {
    return this._client.get(`/vector_stores/${vectorStoreId}/files/${fileId}/content`, options);
  }
}

/**
 * A list of files attached to a vector store.
 */
export interface FileCreateResponse {
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
  last_error: FileCreateResponse.LastError | null;

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

export namespace FileCreateResponse {
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

/**
 * A list of files attached to a vector store.
 */
export interface FileRetrieveResponse {
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
  last_error: FileRetrieveResponse.LastError | null;

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

export namespace FileRetrieveResponse {
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

/**
 * A list of files attached to a vector store.
 */
export interface FileUpdateResponse {
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
  last_error: FileUpdateResponse.LastError | null;

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

export namespace FileUpdateResponse {
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

export interface FileListResponse {
  data: Array<FileListResponse.Data>;

  first_id: string;

  has_more: boolean;

  last_id: string;

  object: string;
}

export namespace FileListResponse {
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

export interface FileDeleteResponse {
  id: string;

  deleted: boolean;

  object: 'vector_store.file.deleted';
}

/**
 * Represents the parsed content of a vector store file.
 */
export interface FileRetrieveContentResponse {
  /**
   * Parsed content of the file.
   */
  data: Array<FileRetrieveContentResponse.Data>;

  /**
   * Indicates if there are more content pages to fetch.
   */
  has_more: boolean;

  /**
   * The token for the next page, if any.
   */
  next_page: string | null;

  /**
   * The object type, which is always `vector_store.file_content.page`
   */
  object: 'vector_store.file_content.page';
}

export namespace FileRetrieveContentResponse {
  export interface Data {
    /**
     * The text content
     */
    text?: string;

    /**
     * The content type (currently only `"text"`)
     */
    type?: string;
  }
}

export interface FileCreateParams {
  /**
   * A [File](https://platform.excai.com/docs/api-reference/files) ID that the vector
   * store should use. Useful for tools like `file_search` that can access files.
   */
  file_id: string;

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

export interface FileUpdateParams {
  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard. Keys are strings with a maximum
   * length of 64 characters. Values are strings with a maximum length of 512
   * characters, booleans, or numbers.
   */
  attributes: { [key: string]: string | number | boolean } | null;
}

export interface FileListParams {
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

export declare namespace Files {
  export {
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
