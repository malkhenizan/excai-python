// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import * as Core from '../core';
import { type Response } from '../_shims/index';

export class Audio extends APIResource {
  /**
   * Generates audio from the input text.
   *
   * @example
   * ```ts
   * const response = await client.audio.createSpeech({
   *   input: 'input',
   *   model: 'string',
   *   voice: 'ash',
   * });
   *
   * const content = await response.blob();
   * console.log(content);
   * ```
   */
  createSpeech(body: AudioCreateSpeechParams, options?: Core.RequestOptions): Core.APIPromise<Response> {
    return this._client.post('/audio/speech', {
      body,
      ...options,
      headers: { Accept: 'application/octet-stream', ...options?.headers },
      __binaryResponse: true,
    });
  }

  /**
   * Transcribes audio into the input language.
   *
   * @example
   * ```ts
   * const response = await client.audio.createTranscription({
   *   file: fs.createReadStream('speech.mp3'),
   *   model: 'gpt-4o-transcribe',
   * });
   * ```
   */
  createTranscription(
    body: AudioCreateTranscriptionParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<AudioCreateTranscriptionResponse> {
    return this._client.post('/audio/transcriptions', Core.multipartFormRequestOptions({ body, ...options }));
  }

  /**
   * Translates audio into English.
   *
   * @example
   * ```ts
   * const response = await client.audio.createTranslation({
   *   file: fs.createReadStream('speech.mp3'),
   *   model: 'whisper-1',
   * });
   * ```
   */
  createTranslation(
    body: AudioCreateTranslationParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<AudioCreateTranslationResponse> {
    return this._client.post('/audio/translations', Core.multipartFormRequestOptions({ body, ...options }));
  }
}

/**
 * Represents a transcription response returned by model, based on the provided
 * input.
 */
export type AudioCreateTranscriptionResponse =
  | AudioCreateTranscriptionResponse.CreateTranscriptionResponseJson
  | AudioCreateTranscriptionResponse.CreateTranscriptionResponseVerboseJson;

export namespace AudioCreateTranscriptionResponse {
  /**
   * Represents a transcription response returned by model, based on the provided
   * input.
   */
  export interface CreateTranscriptionResponseJson {
    /**
     * The transcribed text.
     */
    text: string;

    /**
     * The log probabilities of the tokens in the transcription. Only returned with the
     * models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added
     * to the `include` array.
     */
    logprobs?: Array<CreateTranscriptionResponseJson.Logprob>;

    /**
     * Token usage statistics for the request.
     */
    usage?: CreateTranscriptionResponseJson.Tokens | CreateTranscriptionResponseJson.Duration;
  }

  export namespace CreateTranscriptionResponseJson {
    export interface Logprob {
      /**
       * The token in the transcription.
       */
      token?: string;

      /**
       * The bytes of the token.
       */
      bytes?: Array<number>;

      /**
       * The log probability of the token.
       */
      logprob?: number;
    }

    /**
     * Usage statistics for models billed by token usage.
     */
    export interface Tokens {
      /**
       * Number of input tokens billed for this request.
       */
      input_tokens: number;

      /**
       * Number of output tokens generated.
       */
      output_tokens: number;

      /**
       * Total number of tokens used (input + output).
       */
      total_tokens: number;

      /**
       * The type of the usage object. Always `tokens` for this variant.
       */
      type: 'tokens';

      /**
       * Details about the input tokens billed for this request.
       */
      input_token_details?: Tokens.InputTokenDetails;
    }

    export namespace Tokens {
      /**
       * Details about the input tokens billed for this request.
       */
      export interface InputTokenDetails {
        /**
         * Number of audio tokens billed for this request.
         */
        audio_tokens?: number;

        /**
         * Number of text tokens billed for this request.
         */
        text_tokens?: number;
      }
    }

    /**
     * Usage statistics for models billed by audio input duration.
     */
    export interface Duration {
      /**
       * Duration of the input audio in seconds.
       */
      seconds: number;

      /**
       * The type of the usage object. Always `duration` for this variant.
       */
      type: 'duration';
    }
  }

  /**
   * Represents a verbose json transcription response returned by model, based on the
   * provided input.
   */
  export interface CreateTranscriptionResponseVerboseJson {
    /**
     * The duration of the input audio.
     */
    duration: number;

    /**
     * The language of the input audio.
     */
    language: string;

    /**
     * The transcribed text.
     */
    text: string;

    /**
     * Segments of the transcribed text and their corresponding details.
     */
    segments?: Array<CreateTranscriptionResponseVerboseJson.Segment>;

    /**
     * Usage statistics for models billed by audio input duration.
     */
    usage?: CreateTranscriptionResponseVerboseJson.Usage;

    /**
     * Extracted words and their corresponding timestamps.
     */
    words?: Array<CreateTranscriptionResponseVerboseJson.Word>;
  }

  export namespace CreateTranscriptionResponseVerboseJson {
    export interface Segment {
      /**
       * Unique identifier of the segment.
       */
      id: number;

      /**
       * Average logprob of the segment. If the value is lower than -1, consider the
       * logprobs failed.
       */
      avg_logprob: number;

      /**
       * Compression ratio of the segment. If the value is greater than 2.4, consider the
       * compression failed.
       */
      compression_ratio: number;

      /**
       * End time of the segment in seconds.
       */
      end: number;

      /**
       * Probability of no speech in the segment. If the value is higher than 1.0 and the
       * `avg_logprob` is below -1, consider this segment silent.
       */
      no_speech_prob: number;

      /**
       * Seek offset of the segment.
       */
      seek: number;

      /**
       * Start time of the segment in seconds.
       */
      start: number;

      /**
       * Temperature parameter used for generating the segment.
       */
      temperature: number;

      /**
       * Text content of the segment.
       */
      text: string;

      /**
       * Array of token IDs for the text content.
       */
      tokens: Array<number>;
    }

    /**
     * Usage statistics for models billed by audio input duration.
     */
    export interface Usage {
      /**
       * Duration of the input audio in seconds.
       */
      seconds: number;

      /**
       * The type of the usage object. Always `duration` for this variant.
       */
      type: 'duration';
    }

    export interface Word {
      /**
       * End time of the word in seconds.
       */
      end: number;

      /**
       * Start time of the word in seconds.
       */
      start: number;

      /**
       * The text content of the word.
       */
      word: string;
    }
  }
}

export type AudioCreateTranslationResponse =
  | AudioCreateTranslationResponse.CreateTranslationResponseJson
  | AudioCreateTranslationResponse.CreateTranslationResponseVerboseJson;

export namespace AudioCreateTranslationResponse {
  export interface CreateTranslationResponseJson {
    text: string;
  }

  export interface CreateTranslationResponseVerboseJson {
    /**
     * The duration of the input audio.
     */
    duration: number;

    /**
     * The language of the output translation (always `english`).
     */
    language: string;

    /**
     * The translated text.
     */
    text: string;

    /**
     * Segments of the translated text and their corresponding details.
     */
    segments?: Array<CreateTranslationResponseVerboseJson.Segment>;
  }

  export namespace CreateTranslationResponseVerboseJson {
    export interface Segment {
      /**
       * Unique identifier of the segment.
       */
      id: number;

      /**
       * Average logprob of the segment. If the value is lower than -1, consider the
       * logprobs failed.
       */
      avg_logprob: number;

      /**
       * Compression ratio of the segment. If the value is greater than 2.4, consider the
       * compression failed.
       */
      compression_ratio: number;

      /**
       * End time of the segment in seconds.
       */
      end: number;

      /**
       * Probability of no speech in the segment. If the value is higher than 1.0 and the
       * `avg_logprob` is below -1, consider this segment silent.
       */
      no_speech_prob: number;

      /**
       * Seek offset of the segment.
       */
      seek: number;

      /**
       * Start time of the segment in seconds.
       */
      start: number;

      /**
       * Temperature parameter used for generating the segment.
       */
      temperature: number;

      /**
       * Text content of the segment.
       */
      text: string;

      /**
       * Array of token IDs for the text content.
       */
      tokens: Array<number>;
    }
  }
}

export interface AudioCreateSpeechParams {
  /**
   * The text to generate audio for. The maximum length is 4096 characters.
   */
  input: string;

  /**
   * One of the available [TTS models](https://platform.excai.com/docs/models#tts):
   * `tts-1`, `tts-1-hd` or `gpt-4o-mini-tts`.
   */
  model: (string & {}) | 'tts-1' | 'tts-1-hd' | 'gpt-4o-mini-tts';

  /**
   * The voice to use when generating the audio. Supported voices are `alloy`, `ash`,
   * `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, and
   * `verse`. Previews of the voices are available in the
   * [Text to speech guide](https://platform.excai.com/docs/guides/text-to-speech#voice-options).
   */
  voice:
    | (string & {})
    | 'alloy'
    | 'ash'
    | 'ballad'
    | 'coral'
    | 'echo'
    | 'sage'
    | 'shimmer'
    | 'verse'
    | 'marin'
    | 'cedar';

  /**
   * Control the voice of your generated audio with additional instructions. Does not
   * work with `tts-1` or `tts-1-hd`.
   */
  instructions?: string;

  /**
   * The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`,
   * `wav`, and `pcm`.
   */
  response_format?: 'mp3' | 'opus' | 'aac' | 'flac' | 'wav' | 'pcm';

  /**
   * The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is
   * the default.
   */
  speed?: number;

  /**
   * The format to stream the audio in. Supported formats are `sse` and `audio`.
   * `sse` is not supported for `tts-1` or `tts-1-hd`.
   */
  stream_format?: 'sse' | 'audio';
}

export interface AudioCreateTranscriptionParams {
  /**
   * The audio file object (not file name) to transcribe, in one of these formats:
   * flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.
   */
  file: Core.Uploadable;

  /**
   * ID of the model to use. The options are `gpt-4o-transcribe`,
   * `gpt-4o-mini-transcribe`, and `whisper-1` (which is powered by our open source
   * Whisper V2 model).
   */
  model: (string & {}) | 'whisper-1' | 'gpt-4o-transcribe' | 'gpt-4o-mini-transcribe';

  /**
   * Controls how the audio is cut into chunks. When set to `"auto"`, the server
   * first normalizes loudness and then uses voice activity detection (VAD) to choose
   * boundaries. `server_vad` object can be provided to tweak VAD detection
   * parameters manually. If unset, the audio is transcribed as a single block.
   */
  chunking_strategy?: 'auto' | AudioCreateTranscriptionParams.VadConfig | null;

  /**
   * Additional information to include in the transcription response. `logprobs` will
   * return the log probabilities of the tokens in the response to understand the
   * model's confidence in the transcription. `logprobs` only works with
   * response_format set to `json` and only with the models `gpt-4o-transcribe` and
   * `gpt-4o-mini-transcribe`.
   */
  include?: Array<'logprobs'>;

  /**
   * The language of the input audio. Supplying the input language in
   * [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`)
   * format will improve accuracy and latency.
   */
  language?: string;

  /**
   * An optional text to guide the model's style or continue a previous audio
   * segment. The
   * [prompt](https://platform.excai.com/docs/guides/speech-to-text#prompting) should
   * match the audio language.
   */
  prompt?: string;

  /**
   * The format of the output, in one of these options: `json`, `text`, `srt`,
   * `verbose_json`, or `vtt`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`,
   * the only supported format is `json`.
   */
  response_format?: 'json' | 'text' | 'srt' | 'verbose_json' | 'vtt';

  /**
   * If set to true, the model response data will be streamed to the client as it is
   * generated using
   * [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
   * See the
   * [Streaming section of the Speech-to-Text guide](https://platform.excai.com/docs/guides/speech-to-text?lang=curl#streaming-transcriptions)
   * for more information.
   *
   * Note: Streaming is not supported for the `whisper-1` model and will be ignored.
   */
  stream?: boolean | null;

  /**
   * The sampling temperature, between 0 and 1. Higher values like 0.8 will make the
   * output more random, while lower values like 0.2 will make it more focused and
   * deterministic. If set to 0, the model will use
   * [log probability](https://en.wikipedia.org/wiki/Log_probability) to
   * automatically increase the temperature until certain thresholds are hit.
   */
  temperature?: number;

  /**
   * The timestamp granularities to populate for this transcription.
   * `response_format` must be set `verbose_json` to use timestamp granularities.
   * Either or both of these options are supported: `word`, or `segment`. Note: There
   * is no additional latency for segment timestamps, but generating word timestamps
   * incurs additional latency.
   */
  timestamp_granularities?: Array<'word' | 'segment'>;
}

export namespace AudioCreateTranscriptionParams {
  export interface VadConfig {
    /**
     * Must be set to `server_vad` to enable manual chunking using server side VAD.
     */
    type: 'server_vad';

    /**
     * Amount of audio to include before the VAD detected speech (in milliseconds).
     */
    prefix_padding_ms?: number;

    /**
     * Duration of silence to detect speech stop (in milliseconds). With shorter values
     * the model will respond more quickly, but may jump in on short pauses from the
     * user.
     */
    silence_duration_ms?: number;

    /**
     * Sensitivity threshold (0.0 to 1.0) for voice activity detection. A higher
     * threshold will require louder audio to activate the model, and thus might
     * perform better in noisy environments.
     */
    threshold?: number;
  }
}

export interface AudioCreateTranslationParams {
  /**
   * The audio file object (not file name) translate, in one of these formats: flac,
   * mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.
   */
  file: Core.Uploadable;

  /**
   * ID of the model to use. Only `whisper-1` (which is powered by our open source
   * Whisper V2 model) is currently available.
   */
  model: (string & {}) | 'whisper-1';

  /**
   * An optional text to guide the model's style or continue a previous audio
   * segment. The
   * [prompt](https://platform.excai.com/docs/guides/speech-to-text#prompting) should
   * be in English.
   */
  prompt?: string;

  /**
   * The format of the output, in one of these options: `json`, `text`, `srt`,
   * `verbose_json`, or `vtt`.
   */
  response_format?: 'json' | 'text' | 'srt' | 'verbose_json' | 'vtt';

  /**
   * The sampling temperature, between 0 and 1. Higher values like 0.8 will make the
   * output more random, while lower values like 0.2 will make it more focused and
   * deterministic. If set to 0, the model will use
   * [log probability](https://en.wikipedia.org/wiki/Log_probability) to
   * automatically increase the temperature until certain thresholds are hit.
   */
  temperature?: number;
}

export declare namespace Audio {
  export {
    type AudioCreateTranscriptionResponse as AudioCreateTranscriptionResponse,
    type AudioCreateTranslationResponse as AudioCreateTranslationResponse,
    type AudioCreateSpeechParams as AudioCreateSpeechParams,
    type AudioCreateTranscriptionParams as AudioCreateTranscriptionParams,
    type AudioCreateTranslationParams as AudioCreateTranslationParams,
  };
}
