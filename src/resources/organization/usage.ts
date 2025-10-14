// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import * as Core from '../../core';
import * as OrganizationAPI from './organization';

export class Usage extends APIResource {
  /**
   * Get audio speeches usage details for the organization.
   *
   * @example
   * ```ts
   * const response =
   *   await client.organization.usage.audioSpeeches({
   *     start_time: 0,
   *   });
   * ```
   */
  audioSpeeches(
    query: UsageAudioSpeechesParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<UsageAudioSpeechesResponse> {
    return this._client.get('/organization/usage/audio_speeches', { query, ...options });
  }

  /**
   * Get audio transcriptions usage details for the organization.
   *
   * @example
   * ```ts
   * const response =
   *   await client.organization.usage.audioTranscriptions({
   *     start_time: 0,
   *   });
   * ```
   */
  audioTranscriptions(
    query: UsageAudioTranscriptionsParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<UsageAudioTranscriptionsResponse> {
    return this._client.get('/organization/usage/audio_transcriptions', { query, ...options });
  }

  /**
   * Get code interpreter sessions usage details for the organization.
   *
   * @example
   * ```ts
   * const response =
   *   await client.organization.usage.codeInterpreterSessions({
   *     start_time: 0,
   *   });
   * ```
   */
  codeInterpreterSessions(
    query: UsageCodeInterpreterSessionsParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<UsageCodeInterpreterSessionsResponse> {
    return this._client.get('/organization/usage/code_interpreter_sessions', { query, ...options });
  }

  /**
   * Get completions usage details for the organization.
   *
   * @example
   * ```ts
   * const response =
   *   await client.organization.usage.completions({
   *     start_time: 0,
   *   });
   * ```
   */
  completions(
    query: UsageCompletionsParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<UsageCompletionsResponse> {
    return this._client.get('/organization/usage/completions', { query, ...options });
  }

  /**
   * Get embeddings usage details for the organization.
   *
   * @example
   * ```ts
   * const response = await client.organization.usage.embeddings(
   *   { start_time: 0 },
   * );
   * ```
   */
  embeddings(
    query: UsageEmbeddingsParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<UsageEmbeddingsResponse> {
    return this._client.get('/organization/usage/embeddings', { query, ...options });
  }

  /**
   * Get images usage details for the organization.
   *
   * @example
   * ```ts
   * const response = await client.organization.usage.images({
   *   start_time: 0,
   * });
   * ```
   */
  images(query: UsageImagesParams, options?: Core.RequestOptions): Core.APIPromise<UsageImagesResponse> {
    return this._client.get('/organization/usage/images', { query, ...options });
  }

  /**
   * Get moderations usage details for the organization.
   *
   * @example
   * ```ts
   * const response =
   *   await client.organization.usage.moderations({
   *     start_time: 0,
   *   });
   * ```
   */
  moderations(
    query: UsageModerationsParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<UsageModerationsResponse> {
    return this._client.get('/organization/usage/moderations', { query, ...options });
  }

  /**
   * Get vector stores usage details for the organization.
   *
   * @example
   * ```ts
   * const response =
   *   await client.organization.usage.vectorStores({
   *     start_time: 0,
   *   });
   * ```
   */
  vectorStores(
    query: UsageVectorStoresParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<UsageVectorStoresResponse> {
    return this._client.get('/organization/usage/vector_stores', { query, ...options });
  }
}

export interface UsageAudioSpeechesResponse {
  data: Array<OrganizationAPI.UsageTimeBucket>;

  has_more: boolean;

  next_page: string;

  object: 'page';
}

export interface UsageAudioTranscriptionsResponse {
  data: Array<OrganizationAPI.UsageTimeBucket>;

  has_more: boolean;

  next_page: string;

  object: 'page';
}

export interface UsageCodeInterpreterSessionsResponse {
  data: Array<OrganizationAPI.UsageTimeBucket>;

  has_more: boolean;

  next_page: string;

  object: 'page';
}

export interface UsageCompletionsResponse {
  data: Array<OrganizationAPI.UsageTimeBucket>;

  has_more: boolean;

  next_page: string;

  object: 'page';
}

export interface UsageEmbeddingsResponse {
  data: Array<OrganizationAPI.UsageTimeBucket>;

  has_more: boolean;

  next_page: string;

  object: 'page';
}

export interface UsageImagesResponse {
  data: Array<OrganizationAPI.UsageTimeBucket>;

  has_more: boolean;

  next_page: string;

  object: 'page';
}

export interface UsageModerationsResponse {
  data: Array<OrganizationAPI.UsageTimeBucket>;

  has_more: boolean;

  next_page: string;

  object: 'page';
}

export interface UsageVectorStoresResponse {
  data: Array<OrganizationAPI.UsageTimeBucket>;

  has_more: boolean;

  next_page: string;

  object: 'page';
}

export interface UsageAudioSpeechesParams {
  /**
   * Start time (Unix seconds) of the query time range, inclusive.
   */
  start_time: number;

  /**
   * Return only usage for these API keys.
   */
  api_key_ids?: Array<string>;

  /**
   * Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
   * supported, default to `1d`.
   */
  bucket_width?: '1m' | '1h' | '1d';

  /**
   * End time (Unix seconds) of the query time range, exclusive.
   */
  end_time?: number;

  /**
   * Group the usage data by the specified fields. Support fields include
   * `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.
   */
  group_by?: Array<'project_id' | 'user_id' | 'api_key_id' | 'model'>;

  /**
   * Specifies the number of buckets to return.
   *
   * - `bucket_width=1d`: default: 7, max: 31
   * - `bucket_width=1h`: default: 24, max: 168
   * - `bucket_width=1m`: default: 60, max: 1440
   */
  limit?: number;

  /**
   * Return only usage for these models.
   */
  models?: Array<string>;

  /**
   * A cursor for use in pagination. Corresponding to the `next_page` field from the
   * previous response.
   */
  page?: string;

  /**
   * Return only usage for these projects.
   */
  project_ids?: Array<string>;

  /**
   * Return only usage for these users.
   */
  user_ids?: Array<string>;
}

export interface UsageAudioTranscriptionsParams {
  /**
   * Start time (Unix seconds) of the query time range, inclusive.
   */
  start_time: number;

  /**
   * Return only usage for these API keys.
   */
  api_key_ids?: Array<string>;

  /**
   * Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
   * supported, default to `1d`.
   */
  bucket_width?: '1m' | '1h' | '1d';

  /**
   * End time (Unix seconds) of the query time range, exclusive.
   */
  end_time?: number;

  /**
   * Group the usage data by the specified fields. Support fields include
   * `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.
   */
  group_by?: Array<'project_id' | 'user_id' | 'api_key_id' | 'model'>;

  /**
   * Specifies the number of buckets to return.
   *
   * - `bucket_width=1d`: default: 7, max: 31
   * - `bucket_width=1h`: default: 24, max: 168
   * - `bucket_width=1m`: default: 60, max: 1440
   */
  limit?: number;

  /**
   * Return only usage for these models.
   */
  models?: Array<string>;

  /**
   * A cursor for use in pagination. Corresponding to the `next_page` field from the
   * previous response.
   */
  page?: string;

  /**
   * Return only usage for these projects.
   */
  project_ids?: Array<string>;

  /**
   * Return only usage for these users.
   */
  user_ids?: Array<string>;
}

export interface UsageCodeInterpreterSessionsParams {
  /**
   * Start time (Unix seconds) of the query time range, inclusive.
   */
  start_time: number;

  /**
   * Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
   * supported, default to `1d`.
   */
  bucket_width?: '1m' | '1h' | '1d';

  /**
   * End time (Unix seconds) of the query time range, exclusive.
   */
  end_time?: number;

  /**
   * Group the usage data by the specified fields. Support fields include
   * `project_id`.
   */
  group_by?: Array<'project_id'>;

  /**
   * Specifies the number of buckets to return.
   *
   * - `bucket_width=1d`: default: 7, max: 31
   * - `bucket_width=1h`: default: 24, max: 168
   * - `bucket_width=1m`: default: 60, max: 1440
   */
  limit?: number;

  /**
   * A cursor for use in pagination. Corresponding to the `next_page` field from the
   * previous response.
   */
  page?: string;

  /**
   * Return only usage for these projects.
   */
  project_ids?: Array<string>;
}

export interface UsageCompletionsParams {
  /**
   * Start time (Unix seconds) of the query time range, inclusive.
   */
  start_time: number;

  /**
   * Return only usage for these API keys.
   */
  api_key_ids?: Array<string>;

  /**
   * If `true`, return batch jobs only. If `false`, return non-batch jobs only. By
   * default, return both.
   */
  batch?: boolean;

  /**
   * Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
   * supported, default to `1d`.
   */
  bucket_width?: '1m' | '1h' | '1d';

  /**
   * End time (Unix seconds) of the query time range, exclusive.
   */
  end_time?: number;

  /**
   * Group the usage data by the specified fields. Support fields include
   * `project_id`, `user_id`, `api_key_id`, `model`, `batch` or any combination of
   * them.
   */
  group_by?: Array<'project_id' | 'user_id' | 'api_key_id' | 'model' | 'batch'>;

  /**
   * Specifies the number of buckets to return.
   *
   * - `bucket_width=1d`: default: 7, max: 31
   * - `bucket_width=1h`: default: 24, max: 168
   * - `bucket_width=1m`: default: 60, max: 1440
   */
  limit?: number;

  /**
   * Return only usage for these models.
   */
  models?: Array<string>;

  /**
   * A cursor for use in pagination. Corresponding to the `next_page` field from the
   * previous response.
   */
  page?: string;

  /**
   * Return only usage for these projects.
   */
  project_ids?: Array<string>;

  /**
   * Return only usage for these users.
   */
  user_ids?: Array<string>;
}

export interface UsageEmbeddingsParams {
  /**
   * Start time (Unix seconds) of the query time range, inclusive.
   */
  start_time: number;

  /**
   * Return only usage for these API keys.
   */
  api_key_ids?: Array<string>;

  /**
   * Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
   * supported, default to `1d`.
   */
  bucket_width?: '1m' | '1h' | '1d';

  /**
   * End time (Unix seconds) of the query time range, exclusive.
   */
  end_time?: number;

  /**
   * Group the usage data by the specified fields. Support fields include
   * `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.
   */
  group_by?: Array<'project_id' | 'user_id' | 'api_key_id' | 'model'>;

  /**
   * Specifies the number of buckets to return.
   *
   * - `bucket_width=1d`: default: 7, max: 31
   * - `bucket_width=1h`: default: 24, max: 168
   * - `bucket_width=1m`: default: 60, max: 1440
   */
  limit?: number;

  /**
   * Return only usage for these models.
   */
  models?: Array<string>;

  /**
   * A cursor for use in pagination. Corresponding to the `next_page` field from the
   * previous response.
   */
  page?: string;

  /**
   * Return only usage for these projects.
   */
  project_ids?: Array<string>;

  /**
   * Return only usage for these users.
   */
  user_ids?: Array<string>;
}

export interface UsageImagesParams {
  /**
   * Start time (Unix seconds) of the query time range, inclusive.
   */
  start_time: number;

  /**
   * Return only usage for these API keys.
   */
  api_key_ids?: Array<string>;

  /**
   * Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
   * supported, default to `1d`.
   */
  bucket_width?: '1m' | '1h' | '1d';

  /**
   * End time (Unix seconds) of the query time range, exclusive.
   */
  end_time?: number;

  /**
   * Group the usage data by the specified fields. Support fields include
   * `project_id`, `user_id`, `api_key_id`, `model`, `size`, `source` or any
   * combination of them.
   */
  group_by?: Array<'project_id' | 'user_id' | 'api_key_id' | 'model' | 'size' | 'source'>;

  /**
   * Specifies the number of buckets to return.
   *
   * - `bucket_width=1d`: default: 7, max: 31
   * - `bucket_width=1h`: default: 24, max: 168
   * - `bucket_width=1m`: default: 60, max: 1440
   */
  limit?: number;

  /**
   * Return only usage for these models.
   */
  models?: Array<string>;

  /**
   * A cursor for use in pagination. Corresponding to the `next_page` field from the
   * previous response.
   */
  page?: string;

  /**
   * Return only usage for these projects.
   */
  project_ids?: Array<string>;

  /**
   * Return only usages for these image sizes. Possible values are `256x256`,
   * `512x512`, `1024x1024`, `1792x1792`, `1024x1792` or any combination of them.
   */
  sizes?: Array<'256x256' | '512x512' | '1024x1024' | '1792x1792' | '1024x1792'>;

  /**
   * Return only usages for these sources. Possible values are `image.generation`,
   * `image.edit`, `image.variation` or any combination of them.
   */
  sources?: Array<'image.generation' | 'image.edit' | 'image.variation'>;

  /**
   * Return only usage for these users.
   */
  user_ids?: Array<string>;
}

export interface UsageModerationsParams {
  /**
   * Start time (Unix seconds) of the query time range, inclusive.
   */
  start_time: number;

  /**
   * Return only usage for these API keys.
   */
  api_key_ids?: Array<string>;

  /**
   * Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
   * supported, default to `1d`.
   */
  bucket_width?: '1m' | '1h' | '1d';

  /**
   * End time (Unix seconds) of the query time range, exclusive.
   */
  end_time?: number;

  /**
   * Group the usage data by the specified fields. Support fields include
   * `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.
   */
  group_by?: Array<'project_id' | 'user_id' | 'api_key_id' | 'model'>;

  /**
   * Specifies the number of buckets to return.
   *
   * - `bucket_width=1d`: default: 7, max: 31
   * - `bucket_width=1h`: default: 24, max: 168
   * - `bucket_width=1m`: default: 60, max: 1440
   */
  limit?: number;

  /**
   * Return only usage for these models.
   */
  models?: Array<string>;

  /**
   * A cursor for use in pagination. Corresponding to the `next_page` field from the
   * previous response.
   */
  page?: string;

  /**
   * Return only usage for these projects.
   */
  project_ids?: Array<string>;

  /**
   * Return only usage for these users.
   */
  user_ids?: Array<string>;
}

export interface UsageVectorStoresParams {
  /**
   * Start time (Unix seconds) of the query time range, inclusive.
   */
  start_time: number;

  /**
   * Width of each time bucket in response. Currently `1m`, `1h` and `1d` are
   * supported, default to `1d`.
   */
  bucket_width?: '1m' | '1h' | '1d';

  /**
   * End time (Unix seconds) of the query time range, exclusive.
   */
  end_time?: number;

  /**
   * Group the usage data by the specified fields. Support fields include
   * `project_id`.
   */
  group_by?: Array<'project_id'>;

  /**
   * Specifies the number of buckets to return.
   *
   * - `bucket_width=1d`: default: 7, max: 31
   * - `bucket_width=1h`: default: 24, max: 168
   * - `bucket_width=1m`: default: 60, max: 1440
   */
  limit?: number;

  /**
   * A cursor for use in pagination. Corresponding to the `next_page` field from the
   * previous response.
   */
  page?: string;

  /**
   * Return only usage for these projects.
   */
  project_ids?: Array<string>;
}

export declare namespace Usage {
  export {
    type UsageAudioSpeechesResponse as UsageAudioSpeechesResponse,
    type UsageAudioTranscriptionsResponse as UsageAudioTranscriptionsResponse,
    type UsageCodeInterpreterSessionsResponse as UsageCodeInterpreterSessionsResponse,
    type UsageCompletionsResponse as UsageCompletionsResponse,
    type UsageEmbeddingsResponse as UsageEmbeddingsResponse,
    type UsageImagesResponse as UsageImagesResponse,
    type UsageModerationsResponse as UsageModerationsResponse,
    type UsageVectorStoresResponse as UsageVectorStoresResponse,
    type UsageAudioSpeechesParams as UsageAudioSpeechesParams,
    type UsageAudioTranscriptionsParams as UsageAudioTranscriptionsParams,
    type UsageCodeInterpreterSessionsParams as UsageCodeInterpreterSessionsParams,
    type UsageCompletionsParams as UsageCompletionsParams,
    type UsageEmbeddingsParams as UsageEmbeddingsParams,
    type UsageImagesParams as UsageImagesParams,
    type UsageModerationsParams as UsageModerationsParams,
    type UsageVectorStoresParams as UsageVectorStoresParams,
  };
}
