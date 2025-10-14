// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import { isRequestOptions } from '../core';
import * as Core from '../core';
import * as VideosAPI from './videos';

export class Videos extends APIResource {
  /**
   * Create a video
   */
  create(body: VideoCreateParams, options?: Core.RequestOptions): Core.APIPromise<VideoCreateResponse> {
    return this._client.post('/videos', Core.maybeMultipartFormRequestOptions({ body, ...options }));
  }

  /**
   * Retrieve a video
   */
  retrieve(videoId: string, options?: Core.RequestOptions): Core.APIPromise<VideoRetrieveResponse> {
    return this._client.get(`/videos/${videoId}`, options);
  }

  /**
   * List videos
   */
  list(query?: VideoListParams, options?: Core.RequestOptions): Core.APIPromise<VideoListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<VideoListResponse>;
  list(
    query: VideoListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<VideoListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/videos', { query, ...options });
  }

  /**
   * Delete a video
   */
  delete(videoId: string, options?: Core.RequestOptions): Core.APIPromise<VideoDeleteResponse> {
    return this._client.delete(`/videos/${videoId}`, options);
  }

  /**
   * Create a video remix
   */
  remix(
    videoId: string,
    body: VideoRemixParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<VideoRemixResponse> {
    return this._client.post(
      `/videos/${videoId}/remix`,
      Core.maybeMultipartFormRequestOptions({ body, ...options }),
    );
  }

  /**
   * Download video content
   */
  retrieveContent(
    videoId: string,
    query?: VideoRetrieveContentParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<string>;
  retrieveContent(videoId: string, options?: Core.RequestOptions): Core.APIPromise<string>;
  retrieveContent(
    videoId: string,
    query: VideoRetrieveContentParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<string> {
    if (isRequestOptions(query)) {
      return this.retrieveContent(videoId, {}, query);
    }
    return this._client.get(`/videos/${videoId}/content`, { query, ...options });
  }
}

export interface Error2 {
  code: string;

  message: string;
}

/**
 * Structured information describing a generated video job.
 */
export interface VideoCreateResponse {
  /**
   * Unique identifier for the video job.
   */
  id: string;

  /**
   * Unix timestamp (seconds) for when the job completed, if finished.
   */
  completed_at: number | null;

  /**
   * Unix timestamp (seconds) for when the job was created.
   */
  created_at: number;

  /**
   * Error payload that explains why generation failed, if applicable.
   */
  error: Error2 | null;

  /**
   * Unix timestamp (seconds) for when the downloadable assets expire, if set.
   */
  expires_at: number | null;

  /**
   * The video generation model that produced the job.
   */
  model: 'sora-2' | 'sora-2-pro';

  /**
   * The object type, which is always `video`.
   */
  object: 'video';

  /**
   * Approximate completion percentage for the generation task.
   */
  progress: number;

  /**
   * Identifier of the source video if this video is a remix.
   */
  remixed_from_video_id: string | null;

  /**
   * Duration of the generated clip in seconds.
   */
  seconds: '4' | '8' | '12';

  /**
   * The resolution of the generated video.
   */
  size: '720x1280' | '1280x720' | '1024x1792' | '1792x1024';

  /**
   * Current lifecycle status of the video job.
   */
  status: 'queued' | 'in_progress' | 'completed' | 'failed';
}

/**
 * Structured information describing a generated video job.
 */
export interface VideoRetrieveResponse {
  /**
   * Unique identifier for the video job.
   */
  id: string;

  /**
   * Unix timestamp (seconds) for when the job completed, if finished.
   */
  completed_at: number | null;

  /**
   * Unix timestamp (seconds) for when the job was created.
   */
  created_at: number;

  /**
   * Error payload that explains why generation failed, if applicable.
   */
  error: Error2 | null;

  /**
   * Unix timestamp (seconds) for when the downloadable assets expire, if set.
   */
  expires_at: number | null;

  /**
   * The video generation model that produced the job.
   */
  model: 'sora-2' | 'sora-2-pro';

  /**
   * The object type, which is always `video`.
   */
  object: 'video';

  /**
   * Approximate completion percentage for the generation task.
   */
  progress: number;

  /**
   * Identifier of the source video if this video is a remix.
   */
  remixed_from_video_id: string | null;

  /**
   * Duration of the generated clip in seconds.
   */
  seconds: '4' | '8' | '12';

  /**
   * The resolution of the generated video.
   */
  size: '720x1280' | '1280x720' | '1024x1792' | '1792x1024';

  /**
   * Current lifecycle status of the video job.
   */
  status: 'queued' | 'in_progress' | 'completed' | 'failed';
}

export interface VideoListResponse {
  /**
   * A list of items
   */
  data: Array<VideoListResponse.Data>;

  /**
   * The ID of the first item in the list.
   */
  first_id: string | null;

  /**
   * Whether there are more items available.
   */
  has_more: boolean;

  /**
   * The ID of the last item in the list.
   */
  last_id: string | null;

  /**
   * The type of object returned, must be `list`.
   */
  object: 'list';
}

export namespace VideoListResponse {
  /**
   * Structured information describing a generated video job.
   */
  export interface Data {
    /**
     * Unique identifier for the video job.
     */
    id: string;

    /**
     * Unix timestamp (seconds) for when the job completed, if finished.
     */
    completed_at: number | null;

    /**
     * Unix timestamp (seconds) for when the job was created.
     */
    created_at: number;

    /**
     * Error payload that explains why generation failed, if applicable.
     */
    error: VideosAPI.Error2 | null;

    /**
     * Unix timestamp (seconds) for when the downloadable assets expire, if set.
     */
    expires_at: number | null;

    /**
     * The video generation model that produced the job.
     */
    model: 'sora-2' | 'sora-2-pro';

    /**
     * The object type, which is always `video`.
     */
    object: 'video';

    /**
     * Approximate completion percentage for the generation task.
     */
    progress: number;

    /**
     * Identifier of the source video if this video is a remix.
     */
    remixed_from_video_id: string | null;

    /**
     * Duration of the generated clip in seconds.
     */
    seconds: '4' | '8' | '12';

    /**
     * The resolution of the generated video.
     */
    size: '720x1280' | '1280x720' | '1024x1792' | '1792x1024';

    /**
     * Current lifecycle status of the video job.
     */
    status: 'queued' | 'in_progress' | 'completed' | 'failed';
  }
}

/**
 * Confirmation payload returned after deleting a video.
 */
export interface VideoDeleteResponse {
  /**
   * Identifier of the deleted video.
   */
  id: string;

  /**
   * Indicates that the video resource was deleted.
   */
  deleted: boolean;

  /**
   * The object type that signals the deletion response.
   */
  object: 'video.deleted';
}

/**
 * Structured information describing a generated video job.
 */
export interface VideoRemixResponse {
  /**
   * Unique identifier for the video job.
   */
  id: string;

  /**
   * Unix timestamp (seconds) for when the job completed, if finished.
   */
  completed_at: number | null;

  /**
   * Unix timestamp (seconds) for when the job was created.
   */
  created_at: number;

  /**
   * Error payload that explains why generation failed, if applicable.
   */
  error: Error2 | null;

  /**
   * Unix timestamp (seconds) for when the downloadable assets expire, if set.
   */
  expires_at: number | null;

  /**
   * The video generation model that produced the job.
   */
  model: 'sora-2' | 'sora-2-pro';

  /**
   * The object type, which is always `video`.
   */
  object: 'video';

  /**
   * Approximate completion percentage for the generation task.
   */
  progress: number;

  /**
   * Identifier of the source video if this video is a remix.
   */
  remixed_from_video_id: string | null;

  /**
   * Duration of the generated clip in seconds.
   */
  seconds: '4' | '8' | '12';

  /**
   * The resolution of the generated video.
   */
  size: '720x1280' | '1280x720' | '1024x1792' | '1792x1024';

  /**
   * Current lifecycle status of the video job.
   */
  status: 'queued' | 'in_progress' | 'completed' | 'failed';
}

export type VideoRetrieveContentResponse = string;

export interface VideoCreateParams {
  /**
   * Text prompt that describes the video to generate.
   */
  prompt: string;

  /**
   * Optional image reference that guides generation.
   */
  input_reference?: Core.Uploadable;

  /**
   * The video generation model to use. Defaults to `sora-2`.
   */
  model?: 'sora-2' | 'sora-2-pro';

  /**
   * Clip duration in seconds. Defaults to 4 seconds.
   */
  seconds?: '4' | '8' | '12';

  /**
   * Output resolution formatted as width x height. Defaults to 720x1280.
   */
  size?: '720x1280' | '1280x720' | '1024x1792' | '1792x1024';
}

export interface VideoListParams {
  /**
   * Identifier for the last item from the previous pagination request
   */
  after?: string;

  /**
   * Number of items to retrieve
   */
  limit?: number;

  /**
   * Sort order of results by timestamp. Use `asc` for ascending order or `desc` for
   * descending order.
   */
  order?: 'asc' | 'desc';
}

export interface VideoRemixParams {
  /**
   * Updated text prompt that directs the remix generation.
   */
  prompt: string;
}

export interface VideoRetrieveContentParams {
  /**
   * Which downloadable asset to return. Defaults to the MP4 video.
   */
  variant?: 'video' | 'thumbnail' | 'spritesheet';
}

export declare namespace Videos {
  export {
    type Error2 as Error2,
    type VideoCreateResponse as VideoCreateResponse,
    type VideoRetrieveResponse as VideoRetrieveResponse,
    type VideoListResponse as VideoListResponse,
    type VideoDeleteResponse as VideoDeleteResponse,
    type VideoRemixResponse as VideoRemixResponse,
    type VideoRetrieveContentResponse as VideoRetrieveContentResponse,
    type VideoCreateParams as VideoCreateParams,
    type VideoListParams as VideoListParams,
    type VideoRemixParams as VideoRemixParams,
    type VideoRetrieveContentParams as VideoRetrieveContentParams,
  };
}
