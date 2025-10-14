// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../resource';
import { isRequestOptions } from '../../../core';
import * as Core from '../../../core';
import * as ProjectsAPI from './projects';

export class APIKeys extends APIResource {
  /**
   * Retrieves an API key in the project.
   *
   * @example
   * ```ts
   * const apiKey =
   *   await client.organization.projects.apiKeys.retrieve(
   *     'project_id',
   *     'key_id',
   *   );
   * ```
   */
  retrieve(
    projectId: string,
    keyId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<APIKeyRetrieveResponse> {
    return this._client.get(`/organization/projects/${projectId}/api_keys/${keyId}`, options);
  }

  /**
   * Returns a list of API keys in the project.
   *
   * @example
   * ```ts
   * const apiKeys =
   *   await client.organization.projects.apiKeys.list(
   *     'project_id',
   *   );
   * ```
   */
  list(
    projectId: string,
    query?: APIKeyListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<APIKeyListResponse>;
  list(projectId: string, options?: Core.RequestOptions): Core.APIPromise<APIKeyListResponse>;
  list(
    projectId: string,
    query: APIKeyListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<APIKeyListResponse> {
    if (isRequestOptions(query)) {
      return this.list(projectId, {}, query);
    }
    return this._client.get(`/organization/projects/${projectId}/api_keys`, { query, ...options });
  }

  /**
   * Deletes an API key from the project.
   *
   * @example
   * ```ts
   * const apiKey =
   *   await client.organization.projects.apiKeys.delete(
   *     'project_id',
   *     'key_id',
   *   );
   * ```
   */
  delete(
    projectId: string,
    keyId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<APIKeyDeleteResponse> {
    return this._client.delete(`/organization/projects/${projectId}/api_keys/${keyId}`, options);
  }
}

/**
 * Represents an individual API key in a project.
 */
export interface APIKeyRetrieveResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the API key was created
   */
  created_at: number;

  /**
   * The Unix timestamp (in seconds) of when the API key was last used.
   */
  last_used_at: number;

  /**
   * The name of the API key
   */
  name: string;

  /**
   * The object type, which is always `organization.project.api_key`
   */
  object: 'organization.project.api_key';

  owner: APIKeyRetrieveResponse.Owner;

  /**
   * The redacted value of the API key
   */
  redacted_value: string;
}

export namespace APIKeyRetrieveResponse {
  export interface Owner {
    /**
     * Represents an individual service account in a project.
     */
    service_account?: ProjectsAPI.ProjectServiceAccount;

    /**
     * `user` or `service_account`
     */
    type?: 'user' | 'service_account';

    /**
     * Represents an individual user in a project.
     */
    user?: ProjectsAPI.ProjectUser;
  }
}

export interface APIKeyListResponse {
  data: Array<APIKeyListResponse.Data>;

  first_id: string;

  has_more: boolean;

  last_id: string;

  object: 'list';
}

export namespace APIKeyListResponse {
  /**
   * Represents an individual API key in a project.
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
     * The Unix timestamp (in seconds) of when the API key was last used.
     */
    last_used_at: number;

    /**
     * The name of the API key
     */
    name: string;

    /**
     * The object type, which is always `organization.project.api_key`
     */
    object: 'organization.project.api_key';

    owner: Data.Owner;

    /**
     * The redacted value of the API key
     */
    redacted_value: string;
  }

  export namespace Data {
    export interface Owner {
      /**
       * Represents an individual service account in a project.
       */
      service_account?: ProjectsAPI.ProjectServiceAccount;

      /**
       * `user` or `service_account`
       */
      type?: 'user' | 'service_account';

      /**
       * Represents an individual user in a project.
       */
      user?: ProjectsAPI.ProjectUser;
    }
  }
}

export interface APIKeyDeleteResponse {
  id: string;

  deleted: boolean;

  object: 'organization.project.api_key.deleted';
}

export interface APIKeyListParams {
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

export declare namespace APIKeys {
  export {
    type APIKeyRetrieveResponse as APIKeyRetrieveResponse,
    type APIKeyListResponse as APIKeyListResponse,
    type APIKeyDeleteResponse as APIKeyDeleteResponse,
    type APIKeyListParams as APIKeyListParams,
  };
}
