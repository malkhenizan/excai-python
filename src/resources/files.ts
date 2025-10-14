// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import { isRequestOptions } from '../core';
import * as Core from '../core';
import * as Shared from './shared';

export class Files extends APIResource {
  /**
   * Returns information about a specific file.
   */
  retrieve(fileId: string, options?: Core.RequestOptions): Core.APIPromise<Shared.ExCaiFile> {
    return this._client.get(`/files/${fileId}`, options);
  }

  /**
   * Returns a list of files.
   */
  list(query?: FileListParams, options?: Core.RequestOptions): Core.APIPromise<FileListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<FileListResponse>;
  list(
    query: FileListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<FileListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/files', { query, ...options });
  }

  /**
   * Delete a file and remove it from all vector stores.
   */
  delete(fileId: string, options?: Core.RequestOptions): Core.APIPromise<FileDeleteResponse> {
    return this._client.delete(`/files/${fileId}`, options);
  }

  /**
   * Returns the contents of the specified file.
   */
  retrieveContent(fileId: string, options?: Core.RequestOptions): Core.APIPromise<string> {
    return this._client.get(`/files/${fileId}/content`, options);
  }

  /**
   * Upload a file that can be used across various endpoints. Individual files can be
   * up to 512 MB, and the size of all files uploaded by one organization can be up
   * to 1 TB.
   *
   * The Assistants API supports files up to 2 million tokens and of specific file
   * types. See the
   * [Assistants Tools guide](https://platform.excai.com/docs/assistants/tools) for
   * details.
   *
   * The Fine-tuning API only supports `.jsonl` files. The input also has certain
   * required formats for fine-tuning
   * [chat](https://platform.excai.com/docs/api-reference/fine-tuning/chat-input) or
   * [completions](https://platform.excai.com/docs/api-reference/fine-tuning/completions-input)
   * models.
   *
   * The Batch API only supports `.jsonl` files up to 200 MB in size. The input also
   * has a specific required
   * [format](https://platform.excai.com/docs/api-reference/batch/request-input).
   *
   * Please [contact us](https://help.excai.com/) if you need to increase these
   * storage limits.
   */
  upload(body: FileUploadParams, options?: Core.RequestOptions): Core.APIPromise<Shared.ExCaiFile> {
    return this._client.post('/files', Core.multipartFormRequestOptions({ body, ...options }));
  }
}

export interface FileListResponse {
  data: Array<Shared.ExCaiFile>;

  first_id: string;

  has_more: boolean;

  last_id: string;

  object: string;
}

export interface FileDeleteResponse {
  id: string;

  deleted: boolean;

  object: 'file';
}

export type FileRetrieveContentResponse = string;

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
   * 10,000, and the default is 10,000.
   */
  limit?: number;

  /**
   * Sort order by the `created_at` timestamp of the objects. `asc` for ascending
   * order and `desc` for descending order.
   */
  order?: 'asc' | 'desc';

  /**
   * Only return files with the given purpose.
   */
  purpose?: string;
}

export interface FileUploadParams {
  /**
   * The File object (not file name) to be uploaded.
   */
  file: Core.Uploadable;

  /**
   * The intended purpose of the uploaded file. One of: - `assistants`: Used in the
   * Assistants API - `batch`: Used in the Batch API - `fine-tune`: Used for
   * fine-tuning - `vision`: Images used for vision fine-tuning - `user_data`:
   * Flexible file type for any purpose - `evals`: Used for eval data sets
   */
  purpose: 'assistants' | 'batch' | 'fine-tune' | 'vision' | 'user_data' | 'evals';

  /**
   * The expiration policy for a file. By default, files with `purpose=batch` expire
   * after 30 days and all other files are persisted until they are manually deleted.
   */
  expires_after?: FileUploadParams.ExpiresAfter;
}

export namespace FileUploadParams {
  /**
   * The expiration policy for a file. By default, files with `purpose=batch` expire
   * after 30 days and all other files are persisted until they are manually deleted.
   */
  export interface ExpiresAfter {
    /**
     * Anchor timestamp after which the expiration policy applies. Supported anchors:
     * `created_at`.
     */
    anchor: 'created_at';

    /**
     * The number of seconds after the anchor time that the file will expire. Must be
     * between 3600 (1 hour) and 2592000 (30 days).
     */
    seconds: number;
  }
}

export declare namespace Files {
  export {
    type FileListResponse as FileListResponse,
    type FileDeleteResponse as FileDeleteResponse,
    type FileRetrieveContentResponse as FileRetrieveContentResponse,
    type FileListParams as FileListParams,
    type FileUploadParams as FileUploadParams,
  };
}
