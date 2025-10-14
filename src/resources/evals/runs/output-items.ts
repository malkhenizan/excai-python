// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../resource';
import { isRequestOptions } from '../../../core';
import * as Core from '../../../core';
import * as RunsAPI from './runs';

export class OutputItems extends APIResource {
  /**
   * Get an evaluation run output item by ID.
   */
  retrieve(
    evalId: string,
    runId: string,
    outputItemId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<OutputItemRetrieveResponse> {
    return this._client.get(`/evals/${evalId}/runs/${runId}/output_items/${outputItemId}`, options);
  }

  /**
   * Get a list of output items for an evaluation run.
   */
  list(
    evalId: string,
    runId: string,
    query?: OutputItemListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<OutputItemListResponse>;
  list(evalId: string, runId: string, options?: Core.RequestOptions): Core.APIPromise<OutputItemListResponse>;
  list(
    evalId: string,
    runId: string,
    query: OutputItemListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<OutputItemListResponse> {
    if (isRequestOptions(query)) {
      return this.list(evalId, runId, {}, query);
    }
    return this._client.get(`/evals/${evalId}/runs/${runId}/output_items`, { query, ...options });
  }
}

/**
 * A schema representing an evaluation run output item.
 */
export interface OutputItemRetrieveResponse {
  /**
   * Unique identifier for the evaluation run output item.
   */
  id: string;

  /**
   * Unix timestamp (in seconds) when the evaluation run was created.
   */
  created_at: number;

  /**
   * Details of the input data source item.
   */
  datasource_item: { [key: string]: unknown };

  /**
   * The identifier for the data source item.
   */
  datasource_item_id: number;

  /**
   * The identifier of the evaluation group.
   */
  eval_id: string;

  /**
   * The type of the object. Always "eval.run.output_item".
   */
  object: 'eval.run.output_item';

  /**
   * A list of grader results for this output item.
   */
  results: Array<OutputItemRetrieveResponse.Result>;

  /**
   * The identifier of the evaluation run associated with this output item.
   */
  run_id: string;

  /**
   * A sample containing the input and output of the evaluation run.
   */
  sample: OutputItemRetrieveResponse.Sample;

  /**
   * The status of the evaluation run.
   */
  status: string;
}

export namespace OutputItemRetrieveResponse {
  /**
   * A single grader result for an evaluation run output item.
   */
  export interface Result {
    /**
     * The name of the grader.
     */
    name: string;

    /**
     * Whether the grader considered the output a pass.
     */
    passed: boolean;

    /**
     * The numeric score produced by the grader.
     */
    score: number;

    /**
     * Optional sample or intermediate data produced by the grader.
     */
    sample?: { [key: string]: unknown } | null;

    /**
     * The grader type (for example, "string-check-grader").
     */
    type?: string;

    [k: string]: unknown;
  }

  /**
   * A sample containing the input and output of the evaluation run.
   */
  export interface Sample {
    /**
     * An object representing an error response from the Eval API.
     */
    error: RunsAPI.EvalAPIError;

    /**
     * The reason why the sample generation was finished.
     */
    finish_reason: string;

    /**
     * An array of input messages.
     */
    input: Array<Sample.Input>;

    /**
     * The maximum number of tokens allowed for completion.
     */
    max_completion_tokens: number;

    /**
     * The model used for generating the sample.
     */
    model: string;

    /**
     * An array of output messages.
     */
    output: Array<Sample.Output>;

    /**
     * The seed used for generating the sample.
     */
    seed: number;

    /**
     * The sampling temperature used.
     */
    temperature: number;

    /**
     * The top_p value used for sampling.
     */
    top_p: number;

    /**
     * Token usage details for the sample.
     */
    usage: Sample.Usage;
  }

  export namespace Sample {
    /**
     * An input message.
     */
    export interface Input {
      /**
       * The content of the message.
       */
      content: string;

      /**
       * The role of the message sender (e.g., system, user, developer).
       */
      role: string;
    }

    export interface Output {
      /**
       * The content of the message.
       */
      content?: string;

      /**
       * The role of the message (e.g. "system", "assistant", "user").
       */
      role?: string;
    }

    /**
     * Token usage details for the sample.
     */
    export interface Usage {
      /**
       * The number of tokens retrieved from cache.
       */
      cached_tokens: number;

      /**
       * The number of completion tokens generated.
       */
      completion_tokens: number;

      /**
       * The number of prompt tokens used.
       */
      prompt_tokens: number;

      /**
       * The total number of tokens used.
       */
      total_tokens: number;
    }
  }
}

/**
 * An object representing a list of output items for an evaluation run.
 */
export interface OutputItemListResponse {
  /**
   * An array of eval run output item objects.
   */
  data: Array<OutputItemListResponse.Data>;

  /**
   * The identifier of the first eval run output item in the data array.
   */
  first_id: string;

  /**
   * Indicates whether there are more eval run output items available.
   */
  has_more: boolean;

  /**
   * The identifier of the last eval run output item in the data array.
   */
  last_id: string;

  /**
   * The type of this object. It is always set to "list".
   */
  object: 'list';
}

export namespace OutputItemListResponse {
  /**
   * A schema representing an evaluation run output item.
   */
  export interface Data {
    /**
     * Unique identifier for the evaluation run output item.
     */
    id: string;

    /**
     * Unix timestamp (in seconds) when the evaluation run was created.
     */
    created_at: number;

    /**
     * Details of the input data source item.
     */
    datasource_item: { [key: string]: unknown };

    /**
     * The identifier for the data source item.
     */
    datasource_item_id: number;

    /**
     * The identifier of the evaluation group.
     */
    eval_id: string;

    /**
     * The type of the object. Always "eval.run.output_item".
     */
    object: 'eval.run.output_item';

    /**
     * A list of grader results for this output item.
     */
    results: Array<Data.Result>;

    /**
     * The identifier of the evaluation run associated with this output item.
     */
    run_id: string;

    /**
     * A sample containing the input and output of the evaluation run.
     */
    sample: Data.Sample;

    /**
     * The status of the evaluation run.
     */
    status: string;
  }

  export namespace Data {
    /**
     * A single grader result for an evaluation run output item.
     */
    export interface Result {
      /**
       * The name of the grader.
       */
      name: string;

      /**
       * Whether the grader considered the output a pass.
       */
      passed: boolean;

      /**
       * The numeric score produced by the grader.
       */
      score: number;

      /**
       * Optional sample or intermediate data produced by the grader.
       */
      sample?: { [key: string]: unknown } | null;

      /**
       * The grader type (for example, "string-check-grader").
       */
      type?: string;

      [k: string]: unknown;
    }

    /**
     * A sample containing the input and output of the evaluation run.
     */
    export interface Sample {
      /**
       * An object representing an error response from the Eval API.
       */
      error: RunsAPI.EvalAPIError;

      /**
       * The reason why the sample generation was finished.
       */
      finish_reason: string;

      /**
       * An array of input messages.
       */
      input: Array<Sample.Input>;

      /**
       * The maximum number of tokens allowed for completion.
       */
      max_completion_tokens: number;

      /**
       * The model used for generating the sample.
       */
      model: string;

      /**
       * An array of output messages.
       */
      output: Array<Sample.Output>;

      /**
       * The seed used for generating the sample.
       */
      seed: number;

      /**
       * The sampling temperature used.
       */
      temperature: number;

      /**
       * The top_p value used for sampling.
       */
      top_p: number;

      /**
       * Token usage details for the sample.
       */
      usage: Sample.Usage;
    }

    export namespace Sample {
      /**
       * An input message.
       */
      export interface Input {
        /**
         * The content of the message.
         */
        content: string;

        /**
         * The role of the message sender (e.g., system, user, developer).
         */
        role: string;
      }

      export interface Output {
        /**
         * The content of the message.
         */
        content?: string;

        /**
         * The role of the message (e.g. "system", "assistant", "user").
         */
        role?: string;
      }

      /**
       * Token usage details for the sample.
       */
      export interface Usage {
        /**
         * The number of tokens retrieved from cache.
         */
        cached_tokens: number;

        /**
         * The number of completion tokens generated.
         */
        completion_tokens: number;

        /**
         * The number of prompt tokens used.
         */
        prompt_tokens: number;

        /**
         * The total number of tokens used.
         */
        total_tokens: number;
      }
    }
  }
}

export interface OutputItemListParams {
  /**
   * Identifier for the last output item from the previous pagination request.
   */
  after?: string;

  /**
   * Number of output items to retrieve.
   */
  limit?: number;

  /**
   * Sort order for output items by timestamp. Use `asc` for ascending order or
   * `desc` for descending order. Defaults to `asc`.
   */
  order?: 'asc' | 'desc';

  /**
   * Filter output items by status. Use `failed` to filter by failed output items or
   * `pass` to filter by passed output items.
   */
  status?: 'fail' | 'pass';
}

export declare namespace OutputItems {
  export {
    type OutputItemRetrieveResponse as OutputItemRetrieveResponse,
    type OutputItemListResponse as OutputItemListResponse,
    type OutputItemListParams as OutputItemListParams,
  };
}
