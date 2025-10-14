// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';
import * as OrganizationAPI from './organization';

export class Certificates extends APIResource {
  /**
   * Get a certificate that has been uploaded to the organization.
   *
   * You can get a certificate regardless of whether it is active or not.
   *
   * @example
   * ```ts
   * const certificate =
   *   await client.organization.certificates.retrieve(
   *     'certificate_id',
   *   );
   * ```
   */
  retrieve(
    certificateId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<OrganizationAPI.Certificate> {
    return this._client.get(`/organization/certificates/${certificateId}`, options);
  }

  /**
   * Modify a certificate. Note that only the name can be modified.
   *
   * @example
   * ```ts
   * const certificate =
   *   await client.organization.certificates.update(
   *     'certificate_id',
   *     { name: 'name' },
   *   );
   * ```
   */
  update(
    certificateId: string,
    body: CertificateUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<OrganizationAPI.Certificate> {
    return this._client.post(`/organization/certificates/${certificateId}`, { body, ...options });
  }

  /**
   * List uploaded certificates for this organization.
   *
   * @example
   * ```ts
   * const certificates =
   *   await client.organization.certificates.list();
   * ```
   */
  list(
    query?: CertificateListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<CertificateListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<CertificateListResponse>;
  list(
    query: CertificateListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<CertificateListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/organization/certificates', { query, ...options });
  }

  /**
   * Delete a certificate from the organization.
   *
   * The certificate must be inactive for the organization and all projects.
   *
   * @example
   * ```ts
   * const certificate =
   *   await client.organization.certificates.delete(
   *     'certificate_id',
   *   );
   * ```
   */
  delete(certificateId: string, options?: Core.RequestOptions): Core.APIPromise<CertificateDeleteResponse> {
    return this._client.delete(`/organization/certificates/${certificateId}`, options);
  }

  /**
   * Activate certificates at the organization level.
   *
   * You can atomically and idempotently activate up to 10 certificates at a time.
   *
   * @example
   * ```ts
   * const response =
   *   await client.organization.certificates.activate({
   *     certificate_ids: ['cert_abc'],
   *   });
   * ```
   */
  activate(
    body: CertificateActivateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<CertificateActivateResponse> {
    return this._client.post('/organization/certificates/activate', { body, ...options });
  }

  /**
   * Deactivate certificates at the organization level.
   *
   * You can atomically and idempotently deactivate up to 10 certificates at a time.
   *
   * @example
   * ```ts
   * const response =
   *   await client.organization.certificates.deactivate({
   *     certificate_ids: ['cert_abc'],
   *   });
   * ```
   */
  deactivate(
    body: CertificateDeactivateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<CertificateDeactivateResponse> {
    return this._client.post('/organization/certificates/deactivate', { body, ...options });
  }

  /**
   * Upload a certificate to the organization. This does **not** automatically
   * activate the certificate.
   *
   * Organizations can upload up to 50 certificates.
   *
   * @example
   * ```ts
   * const certificate =
   *   await client.organization.certificates.upload({
   *     content: 'content',
   *   });
   * ```
   */
  upload(
    body: CertificateUploadParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<OrganizationAPI.Certificate> {
    return this._client.post('/organization/certificates', { body, ...options });
  }
}

export interface CertificateListResponse {
  data: Array<OrganizationAPI.Certificate>;

  has_more: boolean;

  object: 'list';

  first_id?: string;

  last_id?: string;
}

export interface CertificateDeleteResponse {
  /**
   * The ID of the certificate that was deleted.
   */
  id: string;

  /**
   * The object type, must be `certificate.deleted`.
   */
  object: 'certificate.deleted';
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

export interface CertificateUpdateParams {
  /**
   * The updated name for the certificate
   */
  name: string;
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

export interface CertificateUploadParams {
  /**
   * The certificate content in PEM format
   */
  content: string;

  /**
   * An optional name for the certificate
   */
  name?: string;
}

export declare namespace Certificates {
  export {
    type CertificateListResponse as CertificateListResponse,
    type CertificateDeleteResponse as CertificateDeleteResponse,
    type CertificateActivateResponse as CertificateActivateResponse,
    type CertificateDeactivateResponse as CertificateDeactivateResponse,
    type CertificateUpdateParams as CertificateUpdateParams,
    type CertificateListParams as CertificateListParams,
    type CertificateActivateParams as CertificateActivateParams,
    type CertificateDeactivateParams as CertificateDeactivateParams,
    type CertificateUploadParams as CertificateUploadParams,
  };
}
