// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';
import * as FilesAPI from './files';
import {
  FileCreateParams,
  FileCreateResponse,
  FileListParams,
  FileListResponse,
  FileRetrieveResponse,
  Files,
} from './files';

export class Containers extends APIResource {
  files: FilesAPI.Files = new FilesAPI.Files(this._client);

  /**
   * Create Container
   */
  create(
    body: ContainerCreateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ContainerCreateResponse> {
    return this._client.post('/containers', { body, ...options });
  }

  /**
   * Retrieve Container
   */
  retrieve(containerId: string, options?: Core.RequestOptions): Core.APIPromise<ContainerRetrieveResponse> {
    return this._client.get(`/containers/${containerId}`, options);
  }

  /**
   * List Containers
   */
  list(query?: ContainerListParams, options?: Core.RequestOptions): Core.APIPromise<ContainerListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<ContainerListResponse>;
  list(
    query: ContainerListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<ContainerListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/containers', { query, ...options });
  }

  /**
   * Delete Container
   */
  delete(containerId: string, options?: Core.RequestOptions): Core.APIPromise<void> {
    return this._client.delete(`/containers/${containerId}`, {
      ...options,
      headers: { Accept: '*/*', ...options?.headers },
    });
  }
}

export interface ContainerCreateResponse {
  /**
   * Unique identifier for the container.
   */
  id: string;

  /**
   * Unix timestamp (in seconds) when the container was created.
   */
  created_at: number;

  /**
   * Name of the container.
   */
  name: string;

  /**
   * The type of this object.
   */
  object: string;

  /**
   * Status of the container (e.g., active, deleted).
   */
  status: string;

  /**
   * The container will expire after this time period. The anchor is the reference
   * point for the expiration. The minutes is the number of minutes after the anchor
   * before the container expires.
   */
  expires_after?: ContainerCreateResponse.ExpiresAfter;
}

export namespace ContainerCreateResponse {
  /**
   * The container will expire after this time period. The anchor is the reference
   * point for the expiration. The minutes is the number of minutes after the anchor
   * before the container expires.
   */
  export interface ExpiresAfter {
    /**
     * The reference point for the expiration.
     */
    anchor?: 'last_active_at';

    /**
     * The number of minutes after the anchor before the container expires.
     */
    minutes?: number;
  }
}

export interface ContainerRetrieveResponse {
  /**
   * Unique identifier for the container.
   */
  id: string;

  /**
   * Unix timestamp (in seconds) when the container was created.
   */
  created_at: number;

  /**
   * Name of the container.
   */
  name: string;

  /**
   * The type of this object.
   */
  object: string;

  /**
   * Status of the container (e.g., active, deleted).
   */
  status: string;

  /**
   * The container will expire after this time period. The anchor is the reference
   * point for the expiration. The minutes is the number of minutes after the anchor
   * before the container expires.
   */
  expires_after?: ContainerRetrieveResponse.ExpiresAfter;
}

export namespace ContainerRetrieveResponse {
  /**
   * The container will expire after this time period. The anchor is the reference
   * point for the expiration. The minutes is the number of minutes after the anchor
   * before the container expires.
   */
  export interface ExpiresAfter {
    /**
     * The reference point for the expiration.
     */
    anchor?: 'last_active_at';

    /**
     * The number of minutes after the anchor before the container expires.
     */
    minutes?: number;
  }
}

export interface ContainerListResponse {
  /**
   * A list of containers.
   */
  data: Array<ContainerListResponse.Data>;

  /**
   * The ID of the first container in the list.
   */
  first_id: string;

  /**
   * Whether there are more containers available.
   */
  has_more: boolean;

  /**
   * The ID of the last container in the list.
   */
  last_id: string;

  /**
   * The type of object returned, must be 'list'.
   */
  object: 'list';
}

export namespace ContainerListResponse {
  export interface Data {
    /**
     * Unique identifier for the container.
     */
    id: string;

    /**
     * Unix timestamp (in seconds) when the container was created.
     */
    created_at: number;

    /**
     * Name of the container.
     */
    name: string;

    /**
     * The type of this object.
     */
    object: string;

    /**
     * Status of the container (e.g., active, deleted).
     */
    status: string;

    /**
     * The container will expire after this time period. The anchor is the reference
     * point for the expiration. The minutes is the number of minutes after the anchor
     * before the container expires.
     */
    expires_after?: Data.ExpiresAfter;
  }

  export namespace Data {
    /**
     * The container will expire after this time period. The anchor is the reference
     * point for the expiration. The minutes is the number of minutes after the anchor
     * before the container expires.
     */
    export interface ExpiresAfter {
      /**
       * The reference point for the expiration.
       */
      anchor?: 'last_active_at';

      /**
       * The number of minutes after the anchor before the container expires.
       */
      minutes?: number;
    }
  }
}

export interface ContainerCreateParams {
  /**
   * Name of the container to create.
   */
  name: string;

  /**
   * Container expiration time in seconds relative to the 'anchor' time.
   */
  expires_after?: ContainerCreateParams.ExpiresAfter;

  /**
   * IDs of files to copy to the container.
   */
  file_ids?: Array<string>;
}

export namespace ContainerCreateParams {
  /**
   * Container expiration time in seconds relative to the 'anchor' time.
   */
  export interface ExpiresAfter {
    /**
     * Time anchor for the expiration time. Currently only 'last_active_at' is
     * supported.
     */
    anchor: 'last_active_at';

    minutes: number;
  }
}

export interface ContainerListParams {
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

Containers.Files = Files;

export declare namespace Containers {
  export {
    type ContainerCreateResponse as ContainerCreateResponse,
    type ContainerRetrieveResponse as ContainerRetrieveResponse,
    type ContainerListResponse as ContainerListResponse,
    type ContainerCreateParams as ContainerCreateParams,
    type ContainerListParams as ContainerListParams,
  };

  export {
    Files as Files,
    type FileCreateResponse as FileCreateResponse,
    type FileRetrieveResponse as FileRetrieveResponse,
    type FileListResponse as FileListResponse,
    type FileCreateParams as FileCreateParams,
    type FileListParams as FileListParams,
  };
}
