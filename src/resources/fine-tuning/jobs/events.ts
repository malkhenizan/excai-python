// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../resource';
import { isRequestOptions } from '../../../core';
import * as Core from '../../../core';

export class Events extends APIResource {
  /**
   * Get status updates for a fine-tuning job.
   *
   * @example
   * ```ts
   * const events = await client.fineTuning.jobs.events.list(
   *   'ft-AF1WoRqd3aJAHsqc9NY7iL8F',
   * );
   * ```
   */
  list(
    fineTuningJobId: string,
    query?: EventListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<EventListResponse>;
  list(fineTuningJobId: string, options?: Core.RequestOptions): Core.APIPromise<EventListResponse>;
  list(
    fineTuningJobId: string,
    query: EventListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<EventListResponse> {
    if (isRequestOptions(query)) {
      return this.list(fineTuningJobId, {}, query);
    }
    return this._client.get(`/fine_tuning/jobs/${fineTuningJobId}/events`, { query, ...options });
  }
}

export interface EventListResponse {
  data: Array<EventListResponse.Data>;

  has_more: boolean;

  object: 'list';
}

export namespace EventListResponse {
  /**
   * Fine-tuning job event object
   */
  export interface Data {
    /**
     * The object identifier.
     */
    id: string;

    /**
     * The Unix timestamp (in seconds) for when the fine-tuning job was created.
     */
    created_at: number;

    /**
     * The log level of the event.
     */
    level: 'info' | 'warn' | 'error';

    /**
     * The message of the event.
     */
    message: string;

    /**
     * The object type, which is always "fine_tuning.job.event".
     */
    object: 'fine_tuning.job.event';

    /**
     * The data associated with the event.
     */
    data?: unknown;

    /**
     * The type of event.
     */
    type?: 'message' | 'metrics';
  }
}

export interface EventListParams {
  /**
   * Identifier for the last event from the previous pagination request.
   */
  after?: string;

  /**
   * Number of events to retrieve.
   */
  limit?: number;
}

export declare namespace Events {
  export { type EventListResponse as EventListResponse, type EventListParams as EventListParams };
}
