// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ExCai from 'excai';
import { Response } from 'node-fetch';

const client = new ExCai({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource fileBatches', () => {
  // Prism tests are disabled
  test.skip('create: only required params', async () => {
    const responsePromise = client.vectorStores.fileBatches.create('vs_abc123', { file_ids: ['string'] });
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
    const response = await client.vectorStores.fileBatches.create('vs_abc123', {
      file_ids: ['string'],
      attributes: { foo: 'string' },
      chunking_strategy: { type: 'auto' },
    });
  });

  // Prism tests are disabled
  test.skip('retrieve', async () => {
    const responsePromise = client.vectorStores.fileBatches.retrieve('vs_abc123', 'vsfb_abc123');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('retrieve: request options instead of params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.vectorStores.fileBatches.retrieve('vs_abc123', 'vsfb_abc123', {
        path: '/_stainless_unknown_path',
      }),
    ).rejects.toThrow(ExCai.NotFoundError);
  });

  // Prism tests are disabled
  test.skip('cancel', async () => {
    const responsePromise = client.vectorStores.fileBatches.cancel('vector_store_id', 'batch_id');
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
      client.vectorStores.fileBatches.cancel('vector_store_id', 'batch_id', {
        path: '/_stainless_unknown_path',
      }),
    ).rejects.toThrow(ExCai.NotFoundError);
  });

  // Prism tests are disabled
  test.skip('listFiles', async () => {
    const responsePromise = client.vectorStores.fileBatches.listFiles('vector_store_id', 'batch_id');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('listFiles: request options instead of params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.vectorStores.fileBatches.listFiles('vector_store_id', 'batch_id', {
        path: '/_stainless_unknown_path',
      }),
    ).rejects.toThrow(ExCai.NotFoundError);
  });

  // Prism tests are disabled
  test.skip('listFiles: request options and params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.vectorStores.fileBatches.listFiles(
        'vector_store_id',
        'batch_id',
        { after: 'after', before: 'before', filter: 'in_progress', limit: 0, order: 'asc' },
        { path: '/_stainless_unknown_path' },
      ),
    ).rejects.toThrow(ExCai.NotFoundError);
  });
});
