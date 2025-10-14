// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import * as Core from '../../core';
import * as SessionsAPI from './sessions';
import { SessionCancelResponse, SessionCreateParams, SessionCreateResponse, Sessions } from './sessions';
import * as ThreadsAPI from './threads';
import {
  ThreadDeleteResponse,
  ThreadListItemsParams,
  ThreadListItemsResponse,
  ThreadListParams,
  ThreadListResponse,
  ThreadRetrieveResponse,
  Threads,
} from './threads';

export class Chatkit extends APIResource {
  sessions: SessionsAPI.Sessions = new SessionsAPI.Sessions(this._client);
  threads: ThreadsAPI.Threads = new ThreadsAPI.Threads(this._client);

  /**
   * Upload a ChatKit file
   *
   * @example
   * ```ts
   * const response = await client.chatkit.uploadFile({
   *   file: fs.createReadStream('path/to/file'),
   * });
   * ```
   */
  uploadFile(
    body: ChatkitUploadFileParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ChatkitUploadFileResponse> {
    return this._client.post('/chatkit/files', Core.maybeMultipartFormRequestOptions({ body, ...options }));
  }
}

/**
 * Represents either a file or image attachment.
 */
export type ChatkitUploadFileResponse = ChatkitUploadFileResponse.File | ChatkitUploadFileResponse.Image;

export namespace ChatkitUploadFileResponse {
  /**
   * Metadata for a non-image file uploaded through ChatKit.
   */
  export interface File {
    /**
     * Unique identifier for the uploaded file.
     */
    id: string;

    /**
     * MIME type reported for the uploaded file. Defaults to null when unknown.
     */
    mime_type: string | null;

    /**
     * Original filename supplied by the uploader. Defaults to null when unnamed.
     */
    name: string | null;

    /**
     * Type discriminator that is always `file`.
     */
    type: 'file';

    /**
     * Signed URL for downloading the uploaded file. Defaults to null when no download
     * link is available.
     */
    upload_url: string | null;
  }

  /**
   * Metadata for an image uploaded through ChatKit.
   */
  export interface Image {
    /**
     * Unique identifier for the uploaded image.
     */
    id: string;

    /**
     * MIME type of the uploaded image.
     */
    mime_type: string;

    /**
     * Original filename for the uploaded image. Defaults to null when unnamed.
     */
    name: string | null;

    /**
     * Preview URL that can be rendered inline for the image.
     */
    preview_url: string;

    /**
     * Type discriminator that is always `image`.
     */
    type: 'image';

    /**
     * Signed URL for downloading the uploaded image. Defaults to null when no download
     * link is available.
     */
    upload_url: string | null;
  }
}

export interface ChatkitUploadFileParams {
  /**
   * Binary file contents to store with the ChatKit session. Supports PDFs and PNG,
   * JPG, JPEG, GIF, or WEBP images.
   */
  file: Core.Uploadable;
}

Chatkit.Sessions = Sessions;
Chatkit.Threads = Threads;

export declare namespace Chatkit {
  export {
    type ChatkitUploadFileResponse as ChatkitUploadFileResponse,
    type ChatkitUploadFileParams as ChatkitUploadFileParams,
  };

  export {
    Sessions as Sessions,
    type SessionCreateResponse as SessionCreateResponse,
    type SessionCancelResponse as SessionCancelResponse,
    type SessionCreateParams as SessionCreateParams,
  };

  export {
    Threads as Threads,
    type ThreadRetrieveResponse as ThreadRetrieveResponse,
    type ThreadListResponse as ThreadListResponse,
    type ThreadDeleteResponse as ThreadDeleteResponse,
    type ThreadListItemsResponse as ThreadListItemsResponse,
    type ThreadListParams as ThreadListParams,
    type ThreadListItemsParams as ThreadListItemsParams,
  };
}
