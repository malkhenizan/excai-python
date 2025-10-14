// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';

export class Files extends APIResource {
  /**
   * Create a Container File
   *
   * You can send either a multipart/form-data request with the raw file content, or
   * a JSON request with a file ID.
   */
  create(
    containerId: string,
    body: FileCreateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileCreateResponse> {
    return this._client.post(
      `/containers/${containerId}/files`,
      Core.multipartFormRequestOptions({ body, ...options }),
    );
  }

  /**
   * Retrieve Container File
   */
  retrieve(
    containerId: string,
    fileId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileRetrieveResponse> {
    return this._client.get(`/containers/${containerId}/files/${fileId}`, options);
  }

  /**
   * List Container files
   */
  list(
    containerId: string,
    query?: FileListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileListResponse>;
  list(containerId: string, options?: Core.RequestOptions): Core.APIPromise<FileListResponse>;
  list(
    containerId: string,
    query: FileListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileListResponse> {
    if (isRequestOptions(query)) {
      return this.list(containerId, {}, query);
    }
    return this._client.get(`/containers/${containerId}/files`, { query, ...options });
  }

  /**
   * Delete Container File
   */
  delete(containerId: string, fileId: string, options?: Core.RequestOptions): Core.APIPromise<void> {
    return this._client.delete(`/containers/${containerId}/files/${fileId}`, {
      ...options,
      headers: { Accept: '*/*', ...options?.headers },
    });
  }

  /**
   * Retrieve Container File Content
   */
  retrieveContent(containerId: string, fileId: string, options?: Core.RequestOptions): Core.APIPromise<void> {
    return this._client.get(`/containers/${containerId}/files/${fileId}/content`, {
      ...options,
      headers: { Accept: '*/*', ...options?.headers },
    });
  }
}

export interface FileCreateResponse {
  /**
   * Unique identifier for the file.
   */
  id: string;

  /**
   * Size of the file in bytes.
   */
  bytes: number;

  /**
   * The container this file belongs to.
   */
  container_id: string;

  /**
   * Unix timestamp (in seconds) when the file was created.
   */
  created_at: number;

  /**
   * The type of this object (`container.file`).
   */
  object: 'container.file';

  /**
   * Path of the file in the container.
   */
  path: string;

  /**
   * Source of the file (e.g., `user`, `assistant`).
   */
  source: string;
}

export interface FileRetrieveResponse {
  /**
   * Unique identifier for the file.
   */
  id: string;

  /**
   * Size of the file in bytes.
   */
  bytes: number;

  /**
   * The container this file belongs to.
   */
  container_id: string;

  /**
   * Unix timestamp (in seconds) when the file was created.
   */
  created_at: number;

  /**
   * The type of this object (`container.file`).
   */
  object: 'container.file';

  /**
   * Path of the file in the container.
   */
  path: string;

  /**
   * Source of the file (e.g., `user`, `assistant`).
   */
  source: string;
}

export interface FileListResponse {
  /**
   * A list of container files.
   */
  data: Array<FileListResponse.Data>;

  /**
   * The ID of the first file in the list.
   */
  first_id: string;

  /**
   * Whether there are more files available.
   */
  has_more: boolean;

  /**
   * The ID of the last file in the list.
   */
  last_id: string;

  /**
   * The type of object returned, must be 'list'.
   */
  object: 'list';
}

export namespace FileListResponse {
  export interface Data {
    /**
     * Unique identifier for the file.
     */
    id: string;

    /**
     * Size of the file in bytes.
     */
    bytes: number;

    /**
     * The container this file belongs to.
     */
    container_id: string;

    /**
     * Unix timestamp (in seconds) when the file was created.
     */
    created_at: number;

    /**
     * The type of this object (`container.file`).
     */
    object: 'container.file';

    /**
     * Path of the file in the container.
     */
    path: string;

    /**
     * Source of the file (e.g., `user`, `assistant`).
     */
    source: string;
  }
}

export interface FileCreateParams {
  /**
   * The File object (not file name) to be uploaded.
   */
  file?: Core.Uploadable;

  /**
   * Name of the file to create.
   */
  file_id?: string;
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
    type FileListResponse as FileListResponse,
    type FileCreateParams as FileCreateParams,
    type FileListParams as FileListParams,
  };
}
