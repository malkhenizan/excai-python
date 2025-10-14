// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ExCai from 'excai';
import { Response } from 'node-fetch';

const client = new ExCai({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource completions', () => {
  // Prism tests are disabled
  test.skip('create: only required params', async () => {
    const responsePromise = client.completions.create({ model: 'string', prompt: 'This is a test.' });
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
    const response = await client.completions.create({
      model: 'string',
      prompt: 'This is a test.',
      best_of: 0,
      echo: true,
      frequency_penalty: -2,
      logit_bias: { foo: 0 },
      logprobs: 0,
      max_tokens: 16,
      n: 1,
      presence_penalty: -2,
      seed: 0,
      stop: '\n',
      stream: true,
      stream_options: { include_obfuscation: true, include_usage: true },
      suffix: 'test.',
      temperature: 1,
      top_p: 1,
      user: 'user-1234',
    });
  });
});
