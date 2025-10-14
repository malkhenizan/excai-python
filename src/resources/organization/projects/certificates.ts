// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../resource';
import { isRequestOptions } from '../../../core';
import * as Core from '../../../core';
import * as OrganizationAPI from '../organization';

export class Certificates extends APIResource {
  /**
   * List certificates for this project.
   *
   * @example
   * ```ts
   * const certificates =
   *   await client.organization.projects.certificates.list(
   *     'project_id',
   *   );
   * ```
   */
  list(
    projectId: string,
    query?: CertificateListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<CertificateListResponse>;
  list(projectId: string, options?: Core.RequestOptions): Core.APIPromise<CertificateListResponse>;
  list(
    projectId: string,
    query: CertificateListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<CertificateListResponse> {
    if (isRequestOptions(query)) {
      return this.list(projectId, {}, query);
    }
    return this._client.get(`/organization/projects/${projectId}/certificates`, { query, ...options });
  }

  /**
   * Activate certificates at the project level.
   *
   * You can atomically and idempotently activate up to 10 certificates at a time.
   *
   * @example
   * ```ts
   * const response =
   *   await client.organization.projects.certificates.activate(
   *     'project_id',
   *     { certificate_ids: ['cert_abc'] },
   *   );
   * ```
   */
  activate(
    projectId: string,
    body: CertificateActivateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<CertificateActivateResponse> {
    return this._client.post(`/organization/projects/${projectId}/certificates/activate`, {
      body,
      ...options,
    });
  }

  /**
   * Deactivate certificates at the project level. You can atomically and
   * idempotently deactivate up to 10 certificates at a time.
   *
   * @example
   * ```ts
   * const response =
   *   await client.organization.projects.certificates.deactivate(
   *     'project_id',
   *     { certificate_ids: ['cert_abc'] },
   *   );
   * ```
   */
  deactivate(
    projectId: string,
    body: CertificateDeactivateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<CertificateDeactivateResponse> {
    return this._client.post(`/organization/projects/${projectId}/certificates/deactivate`, {
      body,
      ...options,
    });
  }
}

export interface CertificateListResponse {
  data: Array<OrganizationAPI.Certificate>;

  has_more: boolean;

  object: 'list';

  first_id?: string;

  last_id?: string;
}

export interface CertificateActivateResponse {
  data: Array<OrganizationAPI.Certificate>;

  has_more: boolean;

  object: 'list';

  first_id?: string;

  last_id?: string;
}

export interface CertificateDeactivateResponse {
  data: Array<OrganizationAPI.Certificate>;

  has_more: boolean;

  object: 'list';

  first_id?: string;

  last_id?: string;
}

export interface CertificateListParams {
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

export interface CertificateActivateParams {
  certificate_ids: Array<string>;
}

export interface CertificateDeactivateParams {
  certificate_ids: Array<string>;
}

export declare namespace Certificates {
  export {
    type CertificateListResponse as CertificateListResponse,
    type CertificateActivateResponse as CertificateActivateResponse,
    type CertificateDeactivateResponse as CertificateDeactivateResponse,
    type CertificateListParams as CertificateListParams,
    type CertificateActivateParams as CertificateActivateParams,
    type CertificateDeactivateParams as CertificateDeactivateParams,
  };
}
