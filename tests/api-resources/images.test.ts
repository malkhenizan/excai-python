// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ExCai, { toFile } from 'excai';
import { Response } from 'node-fetch';

const client = new ExCai({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource images', () => {
  // Prism tests are disabled
  test.skip('createEdit: only required params', async () => {
    const responsePromise = client.images.createEdit({
      image: await toFile(Buffer.from('# my file contents'), 'README.md'),
      prompt: 'A cute baby sea otter wearing a beret',
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('createEdit: required and optional params', async () => {
    const response = await client.images.createEdit({
      image: await toFile(Buffer.from('# my file contents'), 'README.md'),
      prompt: 'A cute baby sea otter wearing a beret',
      background: 'transparent',
      input_fidelity: 'high',
      mask: await toFile(Buffer.from('# my file contents'), 'README.md'),
      model: 'string',
      n: 1,
      output_compression: 100,
      output_format: 'png',
      partial_images: 1,
      quality: 'high',
      response_format: 'url',
      size: '1024x1024',
      stream: false,
      user: 'user-1234',
    });
  });

  // Prism tests are disabled
  test.skip('createImage: only required params', async () => {
    const responsePromise = client.images.createImage({ prompt: 'A cute baby sea otter' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('createImage: required and optional params', async () => {
    const response = await client.images.createImage({
      prompt: 'A cute baby sea otter',
      background: 'transparent',
      model: 'string',
      moderation: 'low',
      n: 1,
      output_compression: 100,
      output_format: 'png',
      partial_images: 1,
      quality: 'medium',
      response_format: 'url',
      size: '1024x1024',
      stream: false,
      style: 'vivid',
      user: 'user-1234',
    });
  });

  // Prism tests are disabled
  test.skip('createVariation: only required params', async () => {
    const responsePromise = client.images.createVariation({
      image: await toFile(Buffer.from('# my file contents'), 'README.md'),
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('createVariation: required and optional params', async () => {
    const response = await client.images.createVariation({
      image: await toFile(Buffer.from('# my file contents'), 'README.md'),
      model: 'string',
      n: 1,
      response_format: 'url',
      size: '1024x1024',
      user: 'user-1234',
    });
  });
});
