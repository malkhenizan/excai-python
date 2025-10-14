// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';

export class Users extends APIResource {
  /**
   * Retrieves a user by their identifier.
   *
   * @example
   * ```ts
   * const user = await client.organization.users.retrieve(
   *   'user_id',
   * );
   * ```
   */
  retrieve(userId: string, options?: Core.RequestOptions): Core.APIPromise<UserRetrieveResponse> {
    return this._client.get(`/organization/users/${userId}`, options);
  }

  /**
   * Modifies a user's role in the organization.
   *
   * @example
   * ```ts
   * const user = await client.organization.users.update(
   *   'user_id',
   *   { role: 'owner' },
   * );
   * ```
   */
  update(
    userId: string,
    body: UserUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<UserUpdateResponse> {
    return this._client.post(`/organization/users/${userId}`, { body, ...options });
  }

  /**
   * Lists all of the users in the organization.
   *
   * @example
   * ```ts
   * const users = await client.organization.users.list();
   * ```
   */
  list(query?: UserListParams, options?: Core.RequestOptions): Core.APIPromise<UserListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<UserListResponse>;
  list(
    query: UserListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<UserListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/organization/users', { query, ...options });
  }

  /**
   * Deletes a user from the organization.
   *
   * @example
   * ```ts
   * const user = await client.organization.users.delete(
   *   'user_id',
   * );
   * ```
   */
  delete(userId: string, options?: Core.RequestOptions): Core.APIPromise<UserDeleteResponse> {
    return this._client.delete(`/organization/users/${userId}`, options);
  }
}

/**
 * Represents an individual `user` within an organization.
 */
export interface UserRetrieveResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the user was added.
   */
  added_at: number;

  /**
   * The email address of the user
   */
  email: string;

  /**
   * The name of the user
   */
  name: string;

  /**
   * The object type, which is always `organization.user`
   */
  object: 'organization.user';

  /**
   * `owner` or `reader`
   */
  role: 'owner' | 'reader';
}

/**
 * Represents an individual `user` within an organization.
 */
export interface UserUpdateResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the user was added.
   */
  added_at: number;

  /**
   * The email address of the user
   */
  email: string;

  /**
   * The name of the user
   */
  name: string;

  /**
   * The object type, which is always `organization.user`
   */
  object: 'organization.user';

  /**
   * `owner` or `reader`
   */
  role: 'owner' | 'reader';
}

export interface UserListResponse {
  data: Array<UserListResponse.Data>;

  first_id: string;

  has_more: boolean;

  last_id: string;

  object: 'list';
}

export namespace UserListResponse {
  /**
   * Represents an individual `user` within an organization.
   */
  export interface Data {
    /**
     * The identifier, which can be referenced in API endpoints
     */
    id: string;

    /**
     * The Unix timestamp (in seconds) of when the user was added.
     */
    added_at: number;

    /**
     * The email address of the user
     */
    email: string;

    /**
     * The name of the user
     */
    name: string;

    /**
     * The object type, which is always `organization.user`
     */
    object: 'organization.user';

    /**
     * `owner` or `reader`
     */
    role: 'owner' | 'reader';
  }
}

export interface UserDeleteResponse {
  id: string;

  deleted: boolean;

  object: 'organization.user.deleted';
}

export interface UserUpdateParams {
  /**
   * `owner` or `reader`
   */
  role: 'owner' | 'reader';
}

export interface UserListParams {
  /**
   * A cursor for use in pagination. `after` is an object ID that defines your place
   * in the list. For instance, if you make a list request and receive 100 objects,
   * ending with obj_foo, your subsequent call can include after=obj_foo in order to
   * fetch the next page of the list.
   */
  after?: string;

  /**
   * Filter by the email address of users.
   */
  emails?: Array<string>;

  /**
   * A limit on the number of objects to be returned. Limit can range between 1 and
   * 100, and the default is 20.
   */
  limit?: number;
}

export declare namespace Users {
  export {
    type UserRetrieveResponse as UserRetrieveResponse,
    type UserUpdateResponse as UserUpdateResponse,
    type UserListResponse as UserListResponse,
    type UserDeleteResponse as UserDeleteResponse,
    type UserUpdateParams as UserUpdateParams,
    type UserListParams as UserListParams,
  };
}
