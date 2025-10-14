// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';

export class AdminAPIKeys extends APIResource {
  /**
   * Create an organization admin API key
   *
   * @example
   * ```ts
   * const adminAPIKey =
   *   await client.organization.adminAPIKeys.create({
   *     name: 'New Admin Key',
   *   });
   * ```
   */
  create(
    body: AdminAPIKeyCreateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<AdminAPIKeyCreateResponse> {
    return this._client.post('/organization/admin_api_keys', { body, ...options });
  }

  /**
   * Retrieve a single organization API key
   *
   * @example
   * ```ts
   * const adminAPIKey =
   *   await client.organization.adminAPIKeys.retrieve('key_id');
   * ```
   */
  retrieve(keyId: string, options?: Core.RequestOptions): Core.APIPromise<AdminAPIKeyRetrieveResponse> {
    return this._client.get(`/organization/admin_api_keys/${keyId}`, options);
  }

  /**
   * List organization API keys
   *
   * @example
   * ```ts
   * const adminAPIKeys =
   *   await client.organization.adminAPIKeys.list();
   * ```
   */
  list(
    query?: AdminAPIKeyListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<AdminAPIKeyListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<AdminAPIKeyListResponse>;
  list(
    query: AdminAPIKeyListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<AdminAPIKeyListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/organization/admin_api_keys', { query, ...options });
  }

  /**
   * Delete an organization admin API key
   *
   * @example
   * ```ts
   * const adminAPIKey =
   *   await client.organization.adminAPIKeys.delete('key_id');
   * ```
   */
  delete(keyId: string, options?: Core.RequestOptions): Core.APIPromise<AdminAPIKeyDeleteResponse> {
    return this._client.delete(`/organization/admin_api_keys/${keyId}`, options);
  }
}

/**
 * Represents an individual Admin API key in an org.
 */
export interface AdminAPIKeyCreateResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the API key was created
   */
  created_at: number;

  /**
   * The Unix timestamp (in seconds) of when the API key was last used
   */
  last_used_at: number | null;

  /**
   * The name of the API key
   */
  name: string;

  /**
   * The object type, which is always `organization.admin_api_key`
   */
  object: string;

  owner: AdminAPIKeyCreateResponse.Owner;

  /**
   * The redacted value of the API key
   */
  redacted_value: string;

  /**
   * The value of the API key. Only shown on create.
   */
  value?: string;
}

export namespace AdminAPIKeyCreateResponse {
  export interface Owner {
    /**
     * The identifier, which can be referenced in API endpoints
     */
    id?: string;

    /**
     * The Unix timestamp (in seconds) of when the user was created
     */
    created_at?: number;

    /**
     * The name of the user
     */
    name?: string;

    /**
     * The object type, which is always organization.user
     */
    object?: string;

    /**
     * Always `owner`
     */
    role?: string;

    /**
     * Always `user`
     */
    type?: string;
  }
}

/**
 * Represents an individual Admin API key in an org.
 */
export interface AdminAPIKeyRetrieveResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the API key was created
   */
  created_at: number;

  /**
   * The Unix timestamp (in seconds) of when the API key was last used
   */
  last_used_at: number | null;

  /**
   * The name of the API key
   */
  name: string;

  /**
   * The object type, which is always `organization.admin_api_key`
   */
  object: string;

  owner: AdminAPIKeyRetrieveResponse.Owner;

  /**
   * The redacted value of the API key
   */
  redacted_value: string;

  /**
   * The value of the API key. Only shown on create.
   */
  value?: string;
}

export namespace AdminAPIKeyRetrieveResponse {
  export interface Owner {
    /**
     * The identifier, which can be referenced in API endpoints
     */
    id?: string;

    /**
     * The Unix timestamp (in seconds) of when the user was created
     */
    created_at?: number;

    /**
     * The name of the user
     */
    name?: string;

    /**
     * The object type, which is always organization.user
     */
    object?: string;

    /**
     * Always `owner`
     */
    role?: string;

    /**
     * Always `user`
     */
    type?: string;
  }
}

export interface AdminAPIKeyListResponse {
  data?: Array<AdminAPIKeyListResponse.Data>;

  first_id?: string;

  has_more?: boolean;

  last_id?: string;

  object?: string;
}

export namespace AdminAPIKeyListResponse {
  /**
   * Represents an individual Admin API key in an org.
   */
  export interface Data {
    /**
     * The identifier, which can be referenced in API endpoints
     */
    id: string;

    /**
     * The Unix timestamp (in seconds) of when the API key was created
     */
    created_at: number;

    /**
     * The Unix timestamp (in seconds) of when the API key was last used
     */
    last_used_at: number | null;

    /**
     * The name of the API key
     */
    name: string;

    /**
     * The object type, which is always `organization.admin_api_key`
     */
    object: string;

    owner: Data.Owner;

    /**
     * The redacted value of the API key
     */
    redacted_value: string;

    /**
     * The value of the API key. Only shown on create.
     */
    value?: string;
  }

  export namespace Data {
    export interface Owner {
      /**
       * The identifier, which can be referenced in API endpoints
       */
      id?: string;

      /**
       * The Unix timestamp (in seconds) of when the user was created
       */
      created_at?: number;

      /**
       * The name of the user
       */
      name?: string;

      /**
       * The object type, which is always organization.user
       */
      object?: string;

      /**
       * Always `owner`
       */
      role?: string;

      /**
       * Always `user`
       */
      type?: string;
    }
  }
}

export interface AdminAPIKeyDeleteResponse {
  id?: string;

  deleted?: boolean;

  object?: string;
}

export interface AdminAPIKeyCreateParams {
  name: string;
}

export interface AdminAPIKeyListParams {
  /**
   * Return keys with IDs that come after this ID in the pagination order.
   */
  after?: string | null;

  /**
   * Maximum number of keys to return.
   */
  limit?: number;

  /**
   * Order results by creation time, ascending or descending.
   */
  order?: 'asc' | 'desc';
}

export declare namespace AdminAPIKeys {
  export {
    type AdminAPIKeyCreateResponse as AdminAPIKeyCreateResponse,
    type AdminAPIKeyRetrieveResponse as AdminAPIKeyRetrieveResponse,
    type AdminAPIKeyListResponse as AdminAPIKeyListResponse,
    type AdminAPIKeyDeleteResponse as AdminAPIKeyDeleteResponse,
    type AdminAPIKeyCreateParams as AdminAPIKeyCreateParams,
    type AdminAPIKeyListParams as AdminAPIKeyListParams,
  };
}
