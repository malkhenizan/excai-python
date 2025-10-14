// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../resource';
import { isRequestOptions } from '../../../core';
import * as Core from '../../../core';
import * as APIKeysAPI from './api-keys';
import {
  APIKeyDeleteResponse,
  APIKeyListParams,
  APIKeyListResponse,
  APIKeyRetrieveResponse,
  APIKeys,
} from './api-keys';
import * as CertificatesAPI from './certificates';
import {
  CertificateActivateParams,
  CertificateActivateResponse,
  CertificateDeactivateParams,
  CertificateDeactivateResponse,
  CertificateListParams,
  CertificateListResponse,
  Certificates,
} from './certificates';
import * as RateLimitsAPI from './rate-limits';
import {
  RateLimitListParams,
  RateLimitListResponse,
  RateLimitUpdateParams,
  RateLimitUpdateResponse,
  RateLimits,
} from './rate-limits';
import * as ServiceAccountsAPI from './service-accounts';
import {
  ServiceAccountCreateParams,
  ServiceAccountCreateResponse,
  ServiceAccountDeleteResponse,
  ServiceAccountListParams,
  ServiceAccountListResponse,
  ServiceAccounts,
} from './service-accounts';
import * as UsersAPI from './users';
import {
  UserCreateParams,
  UserDeleteResponse,
  UserListParams,
  UserListResponse,
  UserUpdateParams,
  Users,
} from './users';

export class Projects extends APIResource {
  apiKeys: APIKeysAPI.APIKeys = new APIKeysAPI.APIKeys(this._client);
  certificates: CertificatesAPI.Certificates = new CertificatesAPI.Certificates(this._client);
  rateLimits: RateLimitsAPI.RateLimits = new RateLimitsAPI.RateLimits(this._client);
  serviceAccounts: ServiceAccountsAPI.ServiceAccounts = new ServiceAccountsAPI.ServiceAccounts(this._client);
  users: UsersAPI.Users = new UsersAPI.Users(this._client);

  /**
   * Create a new project in the organization. Projects can be created and archived,
   * but cannot be deleted.
   *
   * @example
   * ```ts
   * const project = await client.organization.projects.create({
   *   name: 'name',
   * });
   * ```
   */
  create(body: ProjectCreateParams, options?: Core.RequestOptions): Core.APIPromise<ProjectCreateResponse> {
    return this._client.post('/organization/projects', { body, ...options });
  }

  /**
   * Retrieves a project.
   *
   * @example
   * ```ts
   * const project = await client.organization.projects.retrieve(
   *   'project_id',
   * );
   * ```
   */
  retrieve(projectId: string, options?: Core.RequestOptions): Core.APIPromise<ProjectRetrieveResponse> {
    return this._client.get(`/organization/projects/${projectId}`, options);
  }

  /**
   * Modifies a project in the organization.
   *
   * @example
   * ```ts
   * const project = await client.organization.projects.update(
   *   'project_id',
   *   { name: 'name' },
   * );
   * ```
   */
  update(
    projectId: string,
    body: ProjectUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ProjectUpdateResponse> {
    return this._client.post(`/organization/projects/${projectId}`, { body, ...options });
  }

  /**
   * Returns a list of projects.
   *
   * @example
   * ```ts
   * const projects = await client.organization.projects.list();
   * ```
   */
  list(query?: ProjectListParams, options?: Core.RequestOptions): Core.APIPromise<ProjectListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<ProjectListResponse>;
  list(
    query: ProjectListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<ProjectListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/organization/projects', { query, ...options });
  }

  /**
   * Archives a project in the organization. Archived projects cannot be used or
   * updated.
   *
   * @example
   * ```ts
   * const response = await client.organization.projects.archive(
   *   'project_id',
   * );
   * ```
   */
  archive(projectId: string, options?: Core.RequestOptions): Core.APIPromise<ProjectArchiveResponse> {
    return this._client.post(`/organization/projects/${projectId}/archive`, options);
  }
}

/**
 * Represents an individual service account in a project.
 */
export interface ProjectServiceAccount {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the service account was created
   */
  created_at: number;

  /**
   * The name of the service account
   */
  name: string;

  /**
   * The object type, which is always `organization.project.service_account`
   */
  object: 'organization.project.service_account';

  /**
   * `owner` or `member`
   */
  role: 'owner' | 'member';
}

/**
 * Represents an individual user in a project.
 */
export interface ProjectUser {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the project was added.
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
   * The object type, which is always `organization.project.user`
   */
  object: 'organization.project.user';

  /**
   * `owner` or `member`
   */
  role: 'owner' | 'member';
}

/**
 * Represents an individual project.
 */
export interface ProjectCreateResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the project was created.
   */
  created_at: number;

  /**
   * The name of the project. This appears in reporting.
   */
  name: string;

  /**
   * The object type, which is always `organization.project`
   */
  object: 'organization.project';

  /**
   * `active` or `archived`
   */
  status: 'active' | 'archived';

  /**
   * The Unix timestamp (in seconds) of when the project was archived or `null`.
   */
  archived_at?: number | null;
}

/**
 * Represents an individual project.
 */
export interface ProjectRetrieveResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the project was created.
   */
  created_at: number;

  /**
   * The name of the project. This appears in reporting.
   */
  name: string;

  /**
   * The object type, which is always `organization.project`
   */
  object: 'organization.project';

  /**
   * `active` or `archived`
   */
  status: 'active' | 'archived';

  /**
   * The Unix timestamp (in seconds) of when the project was archived or `null`.
   */
  archived_at?: number | null;
}

/**
 * Represents an individual project.
 */
export interface ProjectUpdateResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the project was created.
   */
  created_at: number;

  /**
   * The name of the project. This appears in reporting.
   */
  name: string;

  /**
   * The object type, which is always `organization.project`
   */
  object: 'organization.project';

  /**
   * `active` or `archived`
   */
  status: 'active' | 'archived';

  /**
   * The Unix timestamp (in seconds) of when the project was archived or `null`.
   */
  archived_at?: number | null;
}

export interface ProjectListResponse {
  data: Array<ProjectListResponse.Data>;

  first_id: string;

  has_more: boolean;

  last_id: string;

  object: 'list';
}

export namespace ProjectListResponse {
  /**
   * Represents an individual project.
   */
  export interface Data {
    /**
     * The identifier, which can be referenced in API endpoints
     */
    id: string;

    /**
     * The Unix timestamp (in seconds) of when the project was created.
     */
    created_at: number;

    /**
     * The name of the project. This appears in reporting.
     */
    name: string;

    /**
     * The object type, which is always `organization.project`
     */
    object: 'organization.project';

    /**
     * `active` or `archived`
     */
    status: 'active' | 'archived';

    /**
     * The Unix timestamp (in seconds) of when the project was archived or `null`.
     */
    archived_at?: number | null;
  }
}

/**
 * Represents an individual project.
 */
export interface ProjectArchiveResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) of when the project was created.
   */
  created_at: number;

  /**
   * The name of the project. This appears in reporting.
   */
  name: string;

  /**
   * The object type, which is always `organization.project`
   */
  object: 'organization.project';

  /**
   * `active` or `archived`
   */
  status: 'active' | 'archived';

  /**
   * The Unix timestamp (in seconds) of when the project was archived or `null`.
   */
  archived_at?: number | null;
}

export interface ProjectCreateParams {
  /**
   * The friendly name of the project, this name appears in reports.
   */
  name: string;

  /**
   * Create the project with the specified data residency region. Your organization
   * must have access to Data residency functionality in order to use. See
   * [data residency controls](https://platform.excai.com/docs/guides/your-data#data-residency-controls)
   * to review the functionality and limitations of setting this field.
   */
  geography?: 'US' | 'EU' | 'JP' | 'IN' | 'KR' | 'CA' | 'AU' | 'SG';
}

export interface ProjectUpdateParams {
  /**
   * The updated name of the project, this name appears in reports.
   */
  name: string;
}

export interface ProjectListParams {
  /**
   * A cursor for use in pagination. `after` is an object ID that defines your place
   * in the list. For instance, if you make a list request and receive 100 objects,
   * ending with obj_foo, your subsequent call can include after=obj_foo in order to
   * fetch the next page of the list.
   */
  after?: string;

  /**
   * If `true` returns all projects including those that have been `archived`.
   * Archived projects are not included by default.
   */
  include_archived?: boolean;

  /**
   * A limit on the number of objects to be returned. Limit can range between 1 and
   * 100, and the default is 20.
   */
  limit?: number;
}

Projects.APIKeys = APIKeys;
Projects.Certificates = Certificates;
Projects.RateLimits = RateLimits;
Projects.ServiceAccounts = ServiceAccounts;
Projects.Users = Users;

export declare namespace Projects {
  export {
    type ProjectServiceAccount as ProjectServiceAccount,
    type ProjectUser as ProjectUser,
    type ProjectCreateResponse as ProjectCreateResponse,
    type ProjectRetrieveResponse as ProjectRetrieveResponse,
    type ProjectUpdateResponse as ProjectUpdateResponse,
    type ProjectListResponse as ProjectListResponse,
    type ProjectArchiveResponse as ProjectArchiveResponse,
    type ProjectCreateParams as ProjectCreateParams,
    type ProjectUpdateParams as ProjectUpdateParams,
    type ProjectListParams as ProjectListParams,
  };

  export {
    APIKeys as APIKeys,
    type APIKeyRetrieveResponse as APIKeyRetrieveResponse,
    type APIKeyListResponse as APIKeyListResponse,
    type APIKeyDeleteResponse as APIKeyDeleteResponse,
    type APIKeyListParams as APIKeyListParams,
  };

  export {
    Certificates as Certificates,
    type CertificateListResponse as CertificateListResponse,
    type CertificateActivateResponse as CertificateActivateResponse,
    type CertificateDeactivateResponse as CertificateDeactivateResponse,
    type CertificateListParams as CertificateListParams,
    type CertificateActivateParams as CertificateActivateParams,
    type CertificateDeactivateParams as CertificateDeactivateParams,
  };

  export {
    RateLimits as RateLimits,
    type RateLimitUpdateResponse as RateLimitUpdateResponse,
    type RateLimitListResponse as RateLimitListResponse,
    type RateLimitUpdateParams as RateLimitUpdateParams,
    type RateLimitListParams as RateLimitListParams,
  };

  export {
    ServiceAccounts as ServiceAccounts,
    type ServiceAccountCreateResponse as ServiceAccountCreateResponse,
    type ServiceAccountListResponse as ServiceAccountListResponse,
    type ServiceAccountDeleteResponse as ServiceAccountDeleteResponse,
    type ServiceAccountCreateParams as ServiceAccountCreateParams,
    type ServiceAccountListParams as ServiceAccountListParams,
  };

  export {
    Users as Users,
    type UserListResponse as UserListResponse,
    type UserDeleteResponse as UserDeleteResponse,
    type UserCreateParams as UserCreateParams,
    type UserUpdateParams as UserUpdateParams,
    type UserListParams as UserListParams,
  };
}
