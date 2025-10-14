// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import type { ExCai } from './index';

export abstract class APIResource {
  protected _client: ExCai;

  constructor(client: ExCai) {
    this._client = client;
  }
}
