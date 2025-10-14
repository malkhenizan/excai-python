// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../resource';
import { isRequestOptions } from '../../../core';
import * as Core from '../../../core';

export class Permissions extends APIResource {
  /**
   * **NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).
   *
   * This enables organization owners to share fine-tuned models with other projects
   * in their organization.
   *
   * @example
   * ```ts
   * const permission =
   *   await client.fineTuning.checkpoints.permissions.create(
   *     'ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd',
   *     { project_ids: ['string'] },
   *   );
   * ```
   */
  create(
    fineTunedModelCheckpoint: string,
    body: PermissionCreateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<PermissionCreateResponse> {
    return this._client.post(`/fine_tuning/checkpoints/${fineTunedModelCheckpoint}/permissions`, {
      body,
      ...options,
    });
  }

  /**
   * **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).
   *
   * Organization owners can use this endpoint to view all permissions for a
   * fine-tuned model checkpoint.
   *
   * @example
   * ```ts
   * const permissions =
   *   await client.fineTuning.checkpoints.permissions.list(
   *     'ft-AF1WoRqd3aJAHsqc9NY7iL8F',
   *   );
   * ```
   */
  list(
    fineTunedModelCheckpoint: string,
    query?: PermissionListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<PermissionListResponse>;
  list(
    fineTunedModelCheckpoint: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<PermissionListResponse>;
  list(
    fineTunedModelCheckpoint: string,
    query: PermissionListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<PermissionListResponse> {
    if (isRequestOptions(query)) {
      return this.list(fineTunedModelCheckpoint, {}, query);
    }
    return this._client.get(`/fine_tuning/checkpoints/${fineTunedModelCheckpoint}/permissions`, {
      query,
      ...options,
    });
  }

  /**
   * **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).
   *
   * Organization owners can use this endpoint to delete a permission for a
   * fine-tuned model checkpoint.
   *
   * @example
   * ```ts
   * const permission =
   *   await client.fineTuning.checkpoints.permissions.delete(
   *     'ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd',
   *     'cp_zc4Q7MP6XxulcVzj4MZdwsAB',
   *   );
   * ```
   */
  delete(
    fineTunedModelCheckpoint: string,
    permissionId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<PermissionDeleteResponse> {
    return this._client.delete(
      `/fine_tuning/checkpoints/${fineTunedModelCheckpoint}/permissions/${permissionId}`,
      options,
    );
  }
}

export interface PermissionCreateResponse {
  data: Array<PermissionCreateResponse.Data>;

  has_more: boolean;

  object: 'list';

  first_id?: string | null;

  last_id?: string | null;
}

export namespace PermissionCreateResponse {
  /**
   * The `checkpoint.permission` object represents a permission for a fine-tuned
   * model checkpoint.
   */
  export interface Data {
    /**
     * The permission identifier, which can be referenced in the API endpoints.
     */
    id: string;

    /**
     * The Unix timestamp (in seconds) for when the permission was created.
     */
    created_at: number;

    /**
     * The object type, which is always "checkpoint.permission".
     */
    object: 'checkpoint.permission';

    /**
     * The project identifier that the permission is for.
     */
    project_id: string;
  }
}

export interface PermissionListResponse {
  data: Array<PermissionListResponse.Data>;

  has_more: boolean;

  object: 'list';

  first_id?: string | null;

  last_id?: string | null;
}

export namespace PermissionListResponse {
  /**
   * The `checkpoint.permission` object represents a permission for a fine-tuned
   * model checkpoint.
   */
  export interface Data {
    /**
     * The permission identifier, which can be referenced in the API endpoints.
     */
    id: string;

    /**
     * The Unix timestamp (in seconds) for when the permission was created.
     */
    created_at: number;

    /**
     * The object type, which is always "checkpoint.permission".
     */
    object: 'checkpoint.permission';

    /**
     * The project identifier that the permission is for.
     */
    project_id: string;
  }
}

export interface PermissionDeleteResponse {
  /**
   * The ID of the fine-tuned model checkpoint permission that was deleted.
   */
  id: string;

  /**
   * Whether the fine-tuned model checkpoint permission was successfully deleted.
   */
  deleted: boolean;

  /**
   * The object type, which is always "checkpoint.permission".
   */
  object: 'checkpoint.permission';
}

export interface PermissionCreateParams {
  /**
   * The project identifiers to grant access to.
   */
  project_ids: Array<string>;
}

export interface PermissionListParams {
  /**
   * Identifier for the last permission ID from the previous pagination request.
   */
  after?: string;

  /**
   * Number of permissions to retrieve.
   */
  limit?: number;

  /**
   * The order in which to retrieve permissions.
   */
  order?: 'ascending' | 'descending';

  /**
   * The ID of the project to get permissions for.
   */
  project_id?: string;
}

export declare namespace Permissions {
  export {
    type PermissionCreateResponse as PermissionCreateResponse,
    type PermissionListResponse as PermissionListResponse,
    type PermissionDeleteResponse as PermissionDeleteResponse,
    type PermissionCreateParams as PermissionCreateParams,
    type PermissionListParams as PermissionListParams,
  };
}
