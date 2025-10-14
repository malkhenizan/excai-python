// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import { isRequestOptions } from '../../core';
import * as Core from '../../core';

export class Invites extends APIResource {
  /**
   * Create an invite for a user to the organization. The invite must be accepted by
   * the user before they have access to the organization.
   *
   * @example
   * ```ts
   * const invite = await client.organization.invites.create({
   *   email: 'email',
   *   role: 'reader',
   * });
   * ```
   */
  create(body: InviteCreateParams, options?: Core.RequestOptions): Core.APIPromise<InviteCreateResponse> {
    return this._client.post('/organization/invites', { body, ...options });
  }

  /**
   * Retrieves an invite.
   *
   * @example
   * ```ts
   * const invite = await client.organization.invites.retrieve(
   *   'invite_id',
   * );
   * ```
   */
  retrieve(inviteId: string, options?: Core.RequestOptions): Core.APIPromise<InviteRetrieveResponse> {
    return this._client.get(`/organization/invites/${inviteId}`, options);
  }

  /**
   * Returns a list of invites in the organization.
   *
   * @example
   * ```ts
   * const invites = await client.organization.invites.list();
   * ```
   */
  list(query?: InviteListParams, options?: Core.RequestOptions): Core.APIPromise<InviteListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<InviteListResponse>;
  list(
    query: InviteListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<InviteListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/organization/invites', { query, ...options });
  }

  /**
   * Delete an invite. If the invite has already been accepted, it cannot be deleted.
   *
   * @example
   * ```ts
   * const invite = await client.organization.invites.delete(
   *   'invite_id',
   * );
   * ```
   */
  delete(inviteId: string, options?: Core.RequestOptions): Core.APIPromise<InviteDeleteResponse> {
    return this._client.delete(`/organization/invites/${inviteId}`, options);
  }
}

/**
 * Represents an individual `invite` to the organization.
 */
export interface InviteCreateResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The email address of the individual to whom the invite was sent
   */
  email: string;

  /**
   * The Unix timestamp (in seconds) of when the invite expires.
   */
  expires_at: number;

  /**
   * The Unix timestamp (in seconds) of when the invite was sent.
   */
  invited_at: number;

  /**
   * The object type, which is always `organization.invite`
   */
  object: 'organization.invite';

  /**
   * `owner` or `reader`
   */
  role: 'owner' | 'reader';

  /**
   * `accepted`,`expired`, or `pending`
   */
  status: 'accepted' | 'expired' | 'pending';

  /**
   * The Unix timestamp (in seconds) of when the invite was accepted.
   */
  accepted_at?: number;

  /**
   * The projects that were granted membership upon acceptance of the invite.
   */
  projects?: Array<InviteCreateResponse.Project>;
}

export namespace InviteCreateResponse {
  export interface Project {
    /**
     * Project's public ID
     */
    id?: string;

    /**
     * Project membership role
     */
    role?: 'member' | 'owner';
  }
}

/**
 * Represents an individual `invite` to the organization.
 */
export interface InviteRetrieveResponse {
  /**
   * The identifier, which can be referenced in API endpoints
   */
  id: string;

  /**
   * The email address of the individual to whom the invite was sent
   */
  email: string;

  /**
   * The Unix timestamp (in seconds) of when the invite expires.
   */
  expires_at: number;

  /**
   * The Unix timestamp (in seconds) of when the invite was sent.
   */
  invited_at: number;

  /**
   * The object type, which is always `organization.invite`
   */
  object: 'organization.invite';

  /**
   * `owner` or `reader`
   */
  role: 'owner' | 'reader';

  /**
   * `accepted`,`expired`, or `pending`
   */
  status: 'accepted' | 'expired' | 'pending';

  /**
   * The Unix timestamp (in seconds) of when the invite was accepted.
   */
  accepted_at?: number;

  /**
   * The projects that were granted membership upon acceptance of the invite.
   */
  projects?: Array<InviteRetrieveResponse.Project>;
}

export namespace InviteRetrieveResponse {
  export interface Project {
    /**
     * Project's public ID
     */
    id?: string;

    /**
     * Project membership role
     */
    role?: 'member' | 'owner';
  }
}

export interface InviteListResponse {
  data: Array<InviteListResponse.Data>;

  /**
   * The object type, which is always `list`
   */
  object: 'list';

  /**
   * The first `invite_id` in the retrieved `list`
   */
  first_id?: string;

  /**
   * The `has_more` property is used for pagination to indicate there are additional
   * results.
   */
  has_more?: boolean;

  /**
   * The last `invite_id` in the retrieved `list`
   */
  last_id?: string;
}

export namespace InviteListResponse {
  /**
   * Represents an individual `invite` to the organization.
   */
  export interface Data {
    /**
     * The identifier, which can be referenced in API endpoints
     */
    id: string;

    /**
     * The email address of the individual to whom the invite was sent
     */
    email: string;

    /**
     * The Unix timestamp (in seconds) of when the invite expires.
     */
    expires_at: number;

    /**
     * The Unix timestamp (in seconds) of when the invite was sent.
     */
    invited_at: number;

    /**
     * The object type, which is always `organization.invite`
     */
    object: 'organization.invite';

    /**
     * `owner` or `reader`
     */
    role: 'owner' | 'reader';

    /**
     * `accepted`,`expired`, or `pending`
     */
    status: 'accepted' | 'expired' | 'pending';

    /**
     * The Unix timestamp (in seconds) of when the invite was accepted.
     */
    accepted_at?: number;

    /**
     * The projects that were granted membership upon acceptance of the invite.
     */
    projects?: Array<Data.Project>;
  }

  export namespace Data {
    export interface Project {
      /**
       * Project's public ID
       */
      id?: string;

      /**
       * Project membership role
       */
      role?: 'member' | 'owner';
    }
  }
}

export interface InviteDeleteResponse {
  id: string;

  deleted: boolean;

  /**
   * The object type, which is always `organization.invite.deleted`
   */
  object: 'organization.invite.deleted';
}

export interface InviteCreateParams {
  /**
   * Send an email to this address
   */
  email: string;

  /**
   * `owner` or `reader`
   */
  role: 'reader' | 'owner';

  /**
   * An array of projects to which membership is granted at the same time the org
   * invite is accepted. If omitted, the user will be invited to the default project
   * for compatibility with legacy behavior.
   */
  projects?: Array<InviteCreateParams.Project>;
}

export namespace InviteCreateParams {
  export interface Project {
    /**
     * Project's public ID
     */
    id: string;

    /**
     * Project membership role
     */
    role: 'member' | 'owner';
  }
}

export interface InviteListParams {
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

export declare namespace Invites {
  export {
    type InviteCreateResponse as InviteCreateResponse,
    type InviteRetrieveResponse as InviteRetrieveResponse,
    type InviteListResponse as InviteListResponse,
    type InviteDeleteResponse as InviteDeleteResponse,
    type InviteCreateParams as InviteCreateParams,
    type InviteListParams as InviteListParams,
  };
}
