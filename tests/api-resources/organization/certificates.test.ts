// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ExCai from 'excai';
import { Response } from 'node-fetch';

const client = new ExCai({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource certificates', () => {
  // Prism tests are disabled
  test.skip('retrieve', async () => {
    const responsePromise = client.organization.certificates.retrieve('certificate_id');
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
      client.organization.certificates.retrieve('certificate_id', { path: '/_stainless_unknown_path' }),
    ).rejects.toThrow(ExCai.NotFoundError);
  });

  // Prism tests are disabled
  test.skip('update: only required params', async () => {
    const responsePromise = client.organization.certificates.update('certificate_id', { name: 'name' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('update: required and optional params', async () => {
    const response = await client.organization.certificates.update('certificate_id', { name: 'name' });
  });

  // Prism tests are disabled
  test.skip('list', async () => {
    const responsePromise = client.organization.certificates.list();
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('list: request options instead of params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(client.organization.certificates.list({ path: '/_stainless_unknown_path' })).rejects.toThrow(
      ExCai.NotFoundError,
    );
  });

  // Prism tests are disabled
  test.skip('list: request options and params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.organization.certificates.list(
        { after: 'after', limit: 0, order: 'asc' },
        { path: '/_stainless_unknown_path' },
      ),
    ).rejects.toThrow(ExCai.NotFoundError);
  });

  // Prism tests are disabled
  test.skip('delete', async () => {
    const responsePromise = client.organization.certificates.delete('certificate_id');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('delete: request options instead of params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(
      client.organization.certificates.delete('certificate_id', { path: '/_stainless_unknown_path' }),
    ).rejects.toThrow(ExCai.NotFoundError);
  });

  // Prism tests are disabled
  test.skip('activate: only required params', async () => {
    const responsePromise = client.organization.certificates.activate({ certificate_ids: ['cert_abc'] });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('activate: required and optional params', async () => {
    const response = await client.organization.certificates.activate({ certificate_ids: ['cert_abc'] });
  });

  // Prism tests are disabled
  test.skip('deactivate: only required params', async () => {
    const responsePromise = client.organization.certificates.deactivate({ certificate_ids: ['cert_abc'] });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('deactivate: required and optional params', async () => {
    const response = await client.organization.certificates.deactivate({ certificate_ids: ['cert_abc'] });
  });

  // Prism tests are disabled
  test.skip('upload: only required params', async () => {
    const responsePromise = client.organization.certificates.upload({ content: 'content' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('upload: required and optional params', async () => {
    const response = await client.organization.certificates.upload({ content: 'content', name: 'name' });
  });
});
