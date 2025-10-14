// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../resource';
import { isRequestOptions } from '../../../core';
import * as Core from '../../../core';

export class RateLimits extends APIResource {
  /**
   * Updates a project rate limit.
   *
   * @example
   * ```ts
   * const rateLimit =
   *   await client.organization.projects.rateLimits.update(
   *     'project_id',
   *     'rate_limit_id',
   *   );
   * ```
   */
  update(
    projectId: string,
    rateLimitId: string,
    body: RateLimitUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<RateLimitUpdateResponse> {
    return this._client.post(`/organization/projects/${projectId}/rate_limits/${rateLimitId}`, {
      body,
      ...options,
    });
  }

  /**
   * Returns the rate limits per model for a project.
   *
   * @example
   * ```ts
   * const rateLimits =
   *   await client.organization.projects.rateLimits.list(
   *     'project_id',
   *   );
   * ```
   */
  list(
    projectId: string,
    query?: RateLimitListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<RateLimitListResponse>;
  list(projectId: string, options?: Core.RequestOptions): Core.APIPromise<RateLimitListResponse>;
  list(
    projectId: string,
    query: RateLimitListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<RateLimitListResponse> {
    if (isRequestOptions(query)) {
      return this.list(projectId, {}, query);
    }
    return this._client.get(`/organization/projects/${projectId}/rate_limits`, { query, ...options });
  }
}

/**
 * Represents a project rate limit config.
 */
export interface RateLimitUpdateResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The maximum requests per minute.
   */
  max_requests_per_1_minute: number;

  /**
   * The maximum tokens per minute.
   */
  max_tokens_per_1_minute: number;

  /**
   * The model this rate limit applies to.
   */
  model: string;

  /**
   * The object type, which is always `project.rate_limit`
   */
  object: 'project.rate_limit';

  /**
   * The maximum batch input tokens per day. Only present for relevant models.
   */
  batch_1_day_max_input_tokens?: number;

  /**
   * The maximum audio megabytes per minute. Only present for relevant models.
   */
  max_audio_megabytes_per_1_minute?: number;

  /**
   * The maximum images per minute. Only present for relevant models.
   */
  max_images_per_1_minute?: number;

  /**
   * The maximum requests per day. Only present for relevant models.
   */
  max_requests_per_1_day?: number;
}

export interface RateLimitListResponse {
  data: Array<RateLimitListResponse.Data>;

  first_id: string;

  has_more: boolean;

  last_id: string;

  object: 'list';
}

export namespace RateLimitListResponse {
  /**
   * Represents a project rate limit config.
   */
  export interface Data {
    /**
     * The identifier, which can be referenced in API endpoints.
     */
    id: string;

    /**
     * The maximum requests per minute.
     */
    max_requests_per_1_minute: number;

    /**
     * The maximum tokens per minute.
     */
    max_tokens_per_1_minute: number;

    /**
     * The model this rate limit applies to.
     */
    model: string;

    /**
     * The object type, which is always `project.rate_limit`
     */
    object: 'project.rate_limit';

    /**
     * The maximum batch input tokens per day. Only present for relevant models.
     */
    batch_1_day_max_input_tokens?: number;

    /**
     * The maximum audio megabytes per minute. Only present for relevant models.
     */
    max_audio_megabytes_per_1_minute?: number;

    /**
     * The maximum images per minute. Only present for relevant models.
     */
    max_images_per_1_minute?: number;

    /**
     * The maximum requests per day. Only present for relevant models.
     */
    max_requests_per_1_day?: number;
  }
}

export interface RateLimitUpdateParams {
  /**
   * The maximum batch input tokens per day. Only relevant for certain models.
   */
  batch_1_day_max_input_tokens?: number;

  /**
   * The maximum audio megabytes per minute. Only relevant for certain models.
   */
  max_audio_megabytes_per_1_minute?: number;

  /**
   * The maximum images per minute. Only relevant for certain models.
   */
  max_images_per_1_minute?: number;

  /**
   * The maximum requests per day. Only relevant for certain models.
   */
  max_requests_per_1_day?: number;

  /**
   * The maximum requests per minute.
   */
  max_requests_per_1_minute?: number;

  /**
   * The maximum tokens per minute.
   */
  max_tokens_per_1_minute?: number;
}

export interface RateLimitListParams {
  /**
   * A cursor for use in pagination. `after` is an object ID that defines your place
   * in the list. For instance, if you make a list request and receive 100 objects,
   * ending with obj_foo, your subsequent call can include after=obj_foo in order to
   * fetch the next page of the list.
   */
  after?: string;

  /**
   * A cursor for use in pagination. `before` is an object ID that defines your place
   * in the list. For instance, if you make a list request and receive 100 objects,
   * beginning with obj_foo, your subsequent call can include before=obj_foo in order
   * to fetch the previous page of the list.
   */
  before?: string;

  /**
   * A limit on the number of objects to be returned. The default is 100.
   */
  limit?: number;
}

export declare namespace RateLimits {
  export {
    type RateLimitUpdateResponse as RateLimitUpdateResponse,
    type RateLimitListResponse as RateLimitListResponse,
    type RateLimitUpdateParams as RateLimitUpdateParams,
    type RateLimitListParams as RateLimitListParams,
  };
}
