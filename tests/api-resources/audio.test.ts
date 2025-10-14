// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import ExCai, { toFile } from 'excai';
import { Response } from 'node-fetch';

const client = new ExCai({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource audio', () => {
  test('createSpeech: required and optional params', async () => {
    const response = await client.audio.createSpeech({
      input: 'input',
      model: 'string',
      voice: 'ash',
      instructions: 'instructions',
      response_format: 'mp3',
      speed: 0.25,
      stream_format: 'sse',
    });
  });

  // Prism tests are disabled
  test.skip('createTranscription: only required params', async () => {
    const responsePromise = client.audio.createTranscription({
      file: await toFile(Buffer.from('# my file contents'), 'README.md'),
      model: 'gpt-4o-transcribe',
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
  test.skip('createTranscription: required and optional params', async () => {
    const response = await client.audio.createTranscription({
      file: await toFile(Buffer.from('# my file contents'), 'README.md'),
      model: 'gpt-4o-transcribe',
      chunking_strategy: 'auto',
      include: ['logprobs'],
      language: 'language',
      prompt: 'prompt',
      response_format: 'json',
      stream: true,
      temperature: 0,
      timestamp_granularities: ['word'],
    });
  });

  // Prism tests are disabled
  test.skip('createTranslation: only required params', async () => {
    const responsePromise = client.audio.createTranslation({
      file: await toFile(Buffer.from('# my file contents'), 'README.md'),
      model: 'whisper-1',
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
  test.skip('createTranslation: required and optional params', async () => {
    const response = await client.audio.createTranslation({
      file: await toFile(Buffer.from('# my file contents'), 'README.md'),
      model: 'whisper-1',
      prompt: 'prompt',
      response_format: 'json',
      temperature: 0,
    });
  });
});
