// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ExCai from 'excai';
import { Response } from 'node-fetch';

const client = new ExCai({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource sessions', () => {
  // Prism tests are disabled
  test.skip('create: only required params', async () => {
    const responsePromise = client.chatkit.sessions.create({ user: 'x', workflow: { id: 'id' } });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('create: required and optional params', async () => {
    const response = await client.chatkit.sessions.create({
      user: 'x',
      workflow: {
        id: 'id',
        state_variables: { foo: 'string' },
        tracing: { enabled: true },
        version: 'version',
      },
      chatkit_configuration: {
        automatic_thread_titling: { enabled: true },
        file_upload: { enabled: true, max_file_size: 1, max_files: 1 },
        history: { enabled: true, recent_threads: 1 },
      },
      expires_after: { anchor: 'created_at', seconds: 1 },
      rate_limits: { max_requests_per_1_minute: 1 },
    });
  });

  // Prism tests are disabled
  test.skip('cancel', async () => {
    const responsePromise = client.chatkit.sessions.cancel('cksess_123');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('cancel: request options instead of params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.chatkit.sessions.cancel('cksess_123', { path: '/_stainless_unknown_path' }),
    ).rejects.toThrow(ExCai.NotFoundError);
  });
});
