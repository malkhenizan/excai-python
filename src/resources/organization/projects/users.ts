// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../resource';
import { isRequestOptions } from '../../../core';
import * as Core from '../../../core';
import * as ProjectsAPI from './projects';

export class Users extends APIResource {
  /**
   * Adds a user to the project. Users must already be members of the organization to
   * be added to a project.
   *
   * @example
   * ```ts
   * const projectUser =
   *   await client.organization.projects.users.create(
   *     'project_id',
   *     { role: 'owner', user_id: 'user_id' },
   *   );
   * ```
   */
  create(
    projectId: string,
    body: UserCreateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ProjectsAPI.ProjectUser> {
    return this._client.post(`/organization/projects/${projectId}/users`, { body, ...options });
  }

  /**
   * Retrieves a user in the project.
   *
   * @example
   * ```ts
   * const projectUser =
   *   await client.organization.projects.users.retrieve(
   *     'project_id',
   *     'user_id',
   *   );
   * ```
   */
  retrieve(
    projectId: string,
    userId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ProjectsAPI.ProjectUser> {
    return this._client.get(`/organization/projects/${projectId}/users/${userId}`, options);
  }

  /**
   * Modifies a user's role in the project.
   *
   * @example
   * ```ts
   * const projectUser =
   *   await client.organization.projects.users.update(
   *     'project_id',
   *     'user_id',
   *     { role: 'owner' },
   *   );
   * ```
   */
  update(
    projectId: string,
    userId: string,
    body: UserUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ProjectsAPI.ProjectUser> {
    return this._client.post(`/organization/projects/${projectId}/users/${userId}`, { body, ...options });
  }

  /**
   * Returns a list of users in the project.
   *
   * @example
   * ```ts
   * const users = await client.organization.projects.users.list(
   *   'project_id',
   * );
   * ```
   */
  list(
    projectId: string,
    query?: UserListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<UserListResponse>;
  list(projectId: string, options?: Core.RequestOptions): Core.APIPromise<UserListResponse>;
  list(
    projectId: string,
    query: UserListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<UserListResponse> {
    if (isRequestOptions(query)) {
      return this.list(projectId, {}, query);
    }
    return this._client.get(`/organization/projects/${projectId}/users`, { query, ...options });
  }

  /**
   * Deletes a user from the project.
   *
   * @example
   * ```ts
   * const user =
   *   await client.organization.projects.users.delete(
   *     'project_id',
   *     'user_id',
   *   );
   * ```
   */
  delete(
    projectId: string,
    userId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<UserDeleteResponse> {
    return this._client.delete(`/organization/projects/${projectId}/users/${userId}`, options);
  }
}

export interface UserListResponse {
  data: Array<ProjectsAPI.ProjectUser>;

  first_id: string;

  has_more: boolean;

  last_id: string;

  object: string;
}

export interface UserDeleteResponse {
  id: string;

  deleted: boolean;

  object: 'organization.project.user.deleted';
}

export interface UserCreateParams {
  /**
   * `owner` or `member`
   */
  role: 'owner' | 'member';

  /**
   * The ID of the user.
   */
  user_id: string;
}

export interface UserUpdateParams {
  /**
   * `owner` or `member`
   */
  role: 'owner' | 'member';
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
   * A limit on the number of objects to be returned. Limit can range between 1 and
   * 100, and the default is 20.
   */
  limit?: number;
}

export declare namespace Users {
  export {
    type UserListResponse as UserListResponse,
    type UserDeleteResponse as UserDeleteResponse,
    type UserCreateParams as UserCreateParams,
    type UserUpdateParams as UserUpdateParams,
    type UserListParams as UserListParams,
  };
}
