// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../resource';
import { isRequestOptions } from '../../../core';
import * as Core from '../../../core';
import * as RunsAPI from './runs';
import * as Shared from '../../shared';
import * as MessagesAPI from '../messages';
import * as ThreadsAPI from '../threads';
import * as StepsAPI from './steps';
import { StepListParams, StepListResponse, StepRetrieveParams, StepRetrieveResponse, Steps } from './steps';

export class Runs extends APIResource {
  steps: StepsAPI.Steps = new StepsAPI.Steps(this._client);

  /**
   * Create a run.
   *
   * @example
   * ```ts
   * const run = await client.threads.runs.create('thread_id', {
   *   assistant_id: 'assistant_id',
   * });
   * ```
   */
  create(
    threadId: string,
    params: RunCreateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<RunCreateResponse> {
    const { include, ...body } = params;
    return this._client.post(`/threads/${threadId}/runs`, { query: { include }, body, ...options });
  }

  /**
   * Retrieves a run.
   *
   * @example
   * ```ts
   * const run = await client.threads.runs.retrieve(
   *   'thread_id',
   *   'run_id',
   * );
   * ```
   */
  retrieve(
    threadId: string,
    runId: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<RunRetrieveResponse> {
    return this._client.get(`/threads/${threadId}/runs/${runId}`, options);
  }

  /**
   * Modifies a run.
   *
   * @example
   * ```ts
   * const run = await client.threads.runs.update(
   *   'thread_id',
   *   'run_id',
   * );
   * ```
   */
  update(
    threadId: string,
    runId: string,
    body: RunUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<RunUpdateResponse> {
    return this._client.post(`/threads/${threadId}/runs/${runId}`, { body, ...options });
  }

  /**
   * Returns a list of runs belonging to a thread.
   *
   * @example
   * ```ts
   * const runs = await client.threads.runs.list('thread_id');
   * ```
   */
  list(
    threadId: string,
    query?: RunListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<RunListResponse>;
  list(threadId: string, options?: Core.RequestOptions): Core.APIPromise<RunListResponse>;
  list(
    threadId: string,
    query: RunListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<RunListResponse> {
    if (isRequestOptions(query)) {
      return this.list(threadId, {}, query);
    }
    return this._client.get(`/threads/${threadId}/runs`, { query, ...options });
  }

  /**
   * Cancels a run that is `in_progress`.
   *
   * @example
   * ```ts
   * const response = await client.threads.runs.cancel(
   *   'thread_id',
   *   'run_id',
   * );
   * ```
   */
  cancel(threadId: string, runId: string, options?: Core.RequestOptions): Core.APIPromise<RunCancelResponse> {
    return this._client.post(`/threads/${threadId}/runs/${runId}/cancel`, options);
  }

  /**
   * Create a thread and run it in one request.
   *
   * @example
   * ```ts
   * const response = await client.threads.runs.createWithRun({
   *   assistant_id: 'assistant_id',
   * });
   * ```
   */
  createWithRun(
    body: RunCreateWithRunParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<RunCreateWithRunResponse> {
    return this._client.post('/threads/runs', { body, ...options });
  }

  /**
   * When a run has the `status: "requires_action"` and `required_action.type` is
   * `submit_tool_outputs`, this endpoint can be used to submit the outputs from the
   * tool calls once they're all completed. All outputs must be submitted in a single
   * request.
   *
   * @example
   * ```ts
   * const response =
   *   await client.threads.runs.submitToolOutputs(
   *     'thread_id',
   *     'run_id',
   *     { tool_outputs: [{}] },
   *   );
   * ```
   */
  submitToolOutputs(
    threadId: string,
    runId: string,
    body: RunSubmitToolOutputsParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<RunSubmitToolOutputsResponse> {
    return this._client.post(`/threads/${threadId}/runs/${runId}/submit_tool_outputs`, { body, ...options });
  }
}

/**
 * Specifies a tool the model should use. Use to force the model to call a specific
 * tool.
 */
export interface AssistantsNamedToolChoice {
  /**
   * The type of the tool. If type is `function`, the function name must be set
   */
  type: 'function' | 'code_interpreter' | 'file_search';

  function?: AssistantsNamedToolChoice.Function;
}

export namespace AssistantsNamedToolChoice {
  export interface Function {
    /**
     * The name of the function to call.
     */
    name: string;
  }
}

/**
 * Tool call objects
 */
export interface RunToolCallObject {
  /**
   * The ID of the tool call. This ID must be referenced when you submit the tool
   * outputs in using the
   * [Submit tool outputs to run](https://platform.excai.com/docs/api-reference/runs/submitToolOutputs)
   * endpoint.
   */
  id: string;

  /**
   * The function definition.
   */
  function: RunToolCallObject.Function;

  /**
   * The type of tool call the output is required for. For now, this is always
   * `function`.
   */
  type: 'function';
}

export namespace RunToolCallObject {
  /**
   * The function definition.
   */
  export interface Function {
    /**
     * The arguments that the model expects you to pass to the function.
     */
    arguments: string;

    /**
     * The name of the function.
     */
    name: string;
  }
}

/**
 * Controls for how a thread will be truncated prior to the run. Use this to
 * control the initial context window of the run.
 */
export interface TruncationObject {
  /**
   * The truncation strategy to use for the thread. The default is `auto`. If set to
   * `last_messages`, the thread will be truncated to the n most recent messages in
   * the thread. When set to `auto`, messages in the middle of the thread will be
   * dropped to fit the context length of the model, `max_prompt_tokens`.
   */
  type: 'auto' | 'last_messages';

  /**
   * The number of most recent messages from the thread when constructing the context
   * for the run.
   */
  last_messages?: number | null;
}

/**
 * Represents an execution run on a
 * [thread](https://platform.excai.com/docs/api-reference/threads).
 */
export interface RunCreateResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The ID of the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * execution of this run.
   */
  assistant_id: string;

  /**
   * The Unix timestamp (in seconds) for when the run was cancelled.
   */
  cancelled_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was completed.
   */
  completed_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was created.
   */
  created_at: number;

  /**
   * The Unix timestamp (in seconds) for when the run will expire.
   */
  expires_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run failed.
   */
  failed_at: number | null;

  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  incomplete_details: RunCreateResponse.IncompleteDetails | null;

  /**
   * The instructions that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  instructions: string;

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  last_error: RunCreateResponse.LastError | null;

  /**
   * The maximum number of completion tokens specified to have been used over the
   * course of the run.
   */
  max_completion_tokens: number | null;

  /**
   * The maximum number of prompt tokens specified to have been used over the course
   * of the run.
   */
  max_prompt_tokens: number | null;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata: { [key: string]: string } | null;

  /**
   * The model that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  model: string;

  /**
   * The object type, which is always `thread.run`.
   */
  object: 'thread.run';

  /**
   * Whether to enable
   * [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
   * during tool use.
   */
  parallel_tool_calls: boolean;

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  required_action: RunCreateResponse.RequiredAction | null;

  /**
   * Specifies the format that the model must output. Compatible with
   * [GPT-4o](https://platform.excai.com/docs/models#gpt-4o),
   * [GPT-4 Turbo](https://platform.excai.com/docs/models#gpt-4-turbo-and-gpt-4), and
   * all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.
   *
   * Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
   * Outputs which ensures the model will match your supplied JSON schema. Learn more
   * in the
   * [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
   *
   * Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
   * message the model generates is valid JSON.
   *
   * **Important:** when using JSON mode, you **must** also instruct the model to
   * produce JSON yourself via a system or user message. Without this, the model may
   * generate an unending stream of whitespace until the generation reaches the token
   * limit, resulting in a long-running and seemingly "stuck" request. Also note that
   * the message content may be partially cut off if `finish_reason="length"`, which
   * indicates the generation exceeded `max_tokens` or the conversation exceeded the
   * max context length.
   */
  response_format:
    | 'auto'
    | Shared.ResponseFormatText
    | Shared.ResponseFormatJsonObject
    | Shared.ResponseFormatJsonSchema
    | null;

  /**
   * The Unix timestamp (in seconds) for when the run was started.
   */
  started_at: number | null;

  /**
   * The status of the run, which can be either `queued`, `in_progress`,
   * `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`,
   * `incomplete`, or `expired`.
   */
  status:
    | 'queued'
    | 'in_progress'
    | 'requires_action'
    | 'cancelling'
    | 'cancelled'
    | 'failed'
    | 'completed'
    | 'incomplete'
    | 'expired';

  /**
   * The ID of the [thread](https://platform.excai.com/docs/api-reference/threads)
   * that was executed on as a part of this run.
   */
  thread_id: string;

  /**
   * Controls which (if any) tool is called by the model. `none` means the model will
   * not call any tools and instead generates a message. `auto` is the default value
   * and means the model can pick between generating a message or calling one or more
   * tools. `required` means the model must call one or more tools before responding
   * to the user. Specifying a particular tool like `{"type": "file_search"}` or
   * `{"type": "function", "function": {"name": "my_function"}}` forces the model to
   * call that tool.
   */
  tool_choice: 'none' | 'auto' | 'required' | AssistantsNamedToolChoice | null;

  /**
   * The list of tools that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  tools: Array<Shared.AssistantToolsCode | Shared.AssistantToolsFileSearch | Shared.AssistantToolsFunction>;

  /**
   * Controls for how a thread will be truncated prior to the run. Use this to
   * control the initial context window of the run.
   */
  truncation_strategy: TruncationObject | null;

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  usage: RunCreateResponse.Usage | null;

  /**
   * The sampling temperature used for this run. If not set, defaults to 1.
   */
  temperature?: number | null;

  /**
   * The nucleus sampling value used for this run. If not set, defaults to 1.
   */
  top_p?: number | null;
}

export namespace RunCreateResponse {
  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  export interface IncompleteDetails {
    /**
     * The reason why the run is incomplete. This will point to which specific token
     * limit was reached over the course of the run.
     */
    reason?: 'max_completion_tokens' | 'max_prompt_tokens';
  }

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  export interface LastError {
    /**
     * One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.
     */
    code: 'server_error' | 'rate_limit_exceeded' | 'invalid_prompt';

    /**
     * A human-readable description of the error.
     */
    message: string;
  }

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  export interface RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    submit_tool_outputs: RequiredAction.SubmitToolOutputs;

    /**
     * For now, this is always `submit_tool_outputs`.
     */
    type: 'submit_tool_outputs';
  }

  export namespace RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    export interface SubmitToolOutputs {
      /**
       * A list of the relevant tool calls.
       */
      tool_calls: Array<RunsAPI.RunToolCallObject>;
    }
  }

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  export interface Usage {
    /**
     * Number of completion tokens used over the course of the run.
     */
    completion_tokens: number;

    /**
     * Number of prompt tokens used over the course of the run.
     */
    prompt_tokens: number;

    /**
     * Total number of tokens used (prompt + completion).
     */
    total_tokens: number;
  }
}

/**
 * Represents an execution run on a
 * [thread](https://platform.excai.com/docs/api-reference/threads).
 */
export interface RunRetrieveResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The ID of the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * execution of this run.
   */
  assistant_id: string;

  /**
   * The Unix timestamp (in seconds) for when the run was cancelled.
   */
  cancelled_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was completed.
   */
  completed_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was created.
   */
  created_at: number;

  /**
   * The Unix timestamp (in seconds) for when the run will expire.
   */
  expires_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run failed.
   */
  failed_at: number | null;

  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  incomplete_details: RunRetrieveResponse.IncompleteDetails | null;

  /**
   * The instructions that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  instructions: string;

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  last_error: RunRetrieveResponse.LastError | null;

  /**
   * The maximum number of completion tokens specified to have been used over the
   * course of the run.
   */
  max_completion_tokens: number | null;

  /**
   * The maximum number of prompt tokens specified to have been used over the course
   * of the run.
   */
  max_prompt_tokens: number | null;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata: { [key: string]: string } | null;

  /**
   * The model that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  model: string;

  /**
   * The object type, which is always `thread.run`.
   */
  object: 'thread.run';

  /**
   * Whether to enable
   * [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
   * during tool use.
   */
  parallel_tool_calls: boolean;

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  required_action: RunRetrieveResponse.RequiredAction | null;

  /**
   * Specifies the format that the model must output. Compatible with
   * [GPT-4o](https://platform.excai.com/docs/models#gpt-4o),
   * [GPT-4 Turbo](https://platform.excai.com/docs/models#gpt-4-turbo-and-gpt-4), and
   * all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.
   *
   * Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
   * Outputs which ensures the model will match your supplied JSON schema. Learn more
   * in the
   * [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
   *
   * Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
   * message the model generates is valid JSON.
   *
   * **Important:** when using JSON mode, you **must** also instruct the model to
   * produce JSON yourself via a system or user message. Without this, the model may
   * generate an unending stream of whitespace until the generation reaches the token
   * limit, resulting in a long-running and seemingly "stuck" request. Also note that
   * the message content may be partially cut off if `finish_reason="length"`, which
   * indicates the generation exceeded `max_tokens` or the conversation exceeded the
   * max context length.
   */
  response_format:
    | 'auto'
    | Shared.ResponseFormatText
    | Shared.ResponseFormatJsonObject
    | Shared.ResponseFormatJsonSchema
    | null;

  /**
   * The Unix timestamp (in seconds) for when the run was started.
   */
  started_at: number | null;

  /**
   * The status of the run, which can be either `queued`, `in_progress`,
   * `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`,
   * `incomplete`, or `expired`.
   */
  status:
    | 'queued'
    | 'in_progress'
    | 'requires_action'
    | 'cancelling'
    | 'cancelled'
    | 'failed'
    | 'completed'
    | 'incomplete'
    | 'expired';

  /**
   * The ID of the [thread](https://platform.excai.com/docs/api-reference/threads)
   * that was executed on as a part of this run.
   */
  thread_id: string;

  /**
   * Controls which (if any) tool is called by the model. `none` means the model will
   * not call any tools and instead generates a message. `auto` is the default value
   * and means the model can pick between generating a message or calling one or more
   * tools. `required` means the model must call one or more tools before responding
   * to the user. Specifying a particular tool like `{"type": "file_search"}` or
   * `{"type": "function", "function": {"name": "my_function"}}` forces the model to
   * call that tool.
   */
  tool_choice: 'none' | 'auto' | 'required' | AssistantsNamedToolChoice | null;

  /**
   * The list of tools that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  tools: Array<Shared.AssistantToolsCode | Shared.AssistantToolsFileSearch | Shared.AssistantToolsFunction>;

  /**
   * Controls for how a thread will be truncated prior to the run. Use this to
   * control the initial context window of the run.
   */
  truncation_strategy: TruncationObject | null;

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  usage: RunRetrieveResponse.Usage | null;

  /**
   * The sampling temperature used for this run. If not set, defaults to 1.
   */
  temperature?: number | null;

  /**
   * The nucleus sampling value used for this run. If not set, defaults to 1.
   */
  top_p?: number | null;
}

export namespace RunRetrieveResponse {
  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  export interface IncompleteDetails {
    /**
     * The reason why the run is incomplete. This will point to which specific token
     * limit was reached over the course of the run.
     */
    reason?: 'max_completion_tokens' | 'max_prompt_tokens';
  }

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  export interface LastError {
    /**
     * One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.
     */
    code: 'server_error' | 'rate_limit_exceeded' | 'invalid_prompt';

    /**
     * A human-readable description of the error.
     */
    message: string;
  }

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  export interface RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    submit_tool_outputs: RequiredAction.SubmitToolOutputs;

    /**
     * For now, this is always `submit_tool_outputs`.
     */
    type: 'submit_tool_outputs';
  }

  export namespace RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    export interface SubmitToolOutputs {
      /**
       * A list of the relevant tool calls.
       */
      tool_calls: Array<RunsAPI.RunToolCallObject>;
    }
  }

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  export interface Usage {
    /**
     * Number of completion tokens used over the course of the run.
     */
    completion_tokens: number;

    /**
     * Number of prompt tokens used over the course of the run.
     */
    prompt_tokens: number;

    /**
     * Total number of tokens used (prompt + completion).
     */
    total_tokens: number;
  }
}

/**
 * Represents an execution run on a
 * [thread](https://platform.excai.com/docs/api-reference/threads).
 */
export interface RunUpdateResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The ID of the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * execution of this run.
   */
  assistant_id: string;

  /**
   * The Unix timestamp (in seconds) for when the run was cancelled.
   */
  cancelled_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was completed.
   */
  completed_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was created.
   */
  created_at: number;

  /**
   * The Unix timestamp (in seconds) for when the run will expire.
   */
  expires_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run failed.
   */
  failed_at: number | null;

  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  incomplete_details: RunUpdateResponse.IncompleteDetails | null;

  /**
   * The instructions that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  instructions: string;

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  last_error: RunUpdateResponse.LastError | null;

  /**
   * The maximum number of completion tokens specified to have been used over the
   * course of the run.
   */
  max_completion_tokens: number | null;

  /**
   * The maximum number of prompt tokens specified to have been used over the course
   * of the run.
   */
  max_prompt_tokens: number | null;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata: { [key: string]: string } | null;

  /**
   * The model that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  model: string;

  /**
   * The object type, which is always `thread.run`.
   */
  object: 'thread.run';

  /**
   * Whether to enable
   * [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
   * during tool use.
   */
  parallel_tool_calls: boolean;

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  required_action: RunUpdateResponse.RequiredAction | null;

  /**
   * Specifies the format that the model must output. Compatible with
   * [GPT-4o](https://platform.excai.com/docs/models#gpt-4o),
   * [GPT-4 Turbo](https://platform.excai.com/docs/models#gpt-4-turbo-and-gpt-4), and
   * all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.
   *
   * Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
   * Outputs which ensures the model will match your supplied JSON schema. Learn more
   * in the
   * [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
   *
   * Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
   * message the model generates is valid JSON.
   *
   * **Important:** when using JSON mode, you **must** also instruct the model to
   * produce JSON yourself via a system or user message. Without this, the model may
   * generate an unending stream of whitespace until the generation reaches the token
   * limit, resulting in a long-running and seemingly "stuck" request. Also note that
   * the message content may be partially cut off if `finish_reason="length"`, which
   * indicates the generation exceeded `max_tokens` or the conversation exceeded the
   * max context length.
   */
  response_format:
    | 'auto'
    | Shared.ResponseFormatText
    | Shared.ResponseFormatJsonObject
    | Shared.ResponseFormatJsonSchema
    | null;

  /**
   * The Unix timestamp (in seconds) for when the run was started.
   */
  started_at: number | null;

  /**
   * The status of the run, which can be either `queued`, `in_progress`,
   * `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`,
   * `incomplete`, or `expired`.
   */
  status:
    | 'queued'
    | 'in_progress'
    | 'requires_action'
    | 'cancelling'
    | 'cancelled'
    | 'failed'
    | 'completed'
    | 'incomplete'
    | 'expired';

  /**
   * The ID of the [thread](https://platform.excai.com/docs/api-reference/threads)
   * that was executed on as a part of this run.
   */
  thread_id: string;

  /**
   * Controls which (if any) tool is called by the model. `none` means the model will
   * not call any tools and instead generates a message. `auto` is the default value
   * and means the model can pick between generating a message or calling one or more
   * tools. `required` means the model must call one or more tools before responding
   * to the user. Specifying a particular tool like `{"type": "file_search"}` or
   * `{"type": "function", "function": {"name": "my_function"}}` forces the model to
   * call that tool.
   */
  tool_choice: 'none' | 'auto' | 'required' | AssistantsNamedToolChoice | null;

  /**
   * The list of tools that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  tools: Array<Shared.AssistantToolsCode | Shared.AssistantToolsFileSearch | Shared.AssistantToolsFunction>;

  /**
   * Controls for how a thread will be truncated prior to the run. Use this to
   * control the initial context window of the run.
   */
  truncation_strategy: TruncationObject | null;

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  usage: RunUpdateResponse.Usage | null;

  /**
   * The sampling temperature used for this run. If not set, defaults to 1.
   */
  temperature?: number | null;

  /**
   * The nucleus sampling value used for this run. If not set, defaults to 1.
   */
  top_p?: number | null;
}

export namespace RunUpdateResponse {
  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  export interface IncompleteDetails {
    /**
     * The reason why the run is incomplete. This will point to which specific token
     * limit was reached over the course of the run.
     */
    reason?: 'max_completion_tokens' | 'max_prompt_tokens';
  }

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  export interface LastError {
    /**
     * One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.
     */
    code: 'server_error' | 'rate_limit_exceeded' | 'invalid_prompt';

    /**
     * A human-readable description of the error.
     */
    message: string;
  }

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  export interface RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    submit_tool_outputs: RequiredAction.SubmitToolOutputs;

    /**
     * For now, this is always `submit_tool_outputs`.
     */
    type: 'submit_tool_outputs';
  }

  export namespace RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    export interface SubmitToolOutputs {
      /**
       * A list of the relevant tool calls.
       */
      tool_calls: Array<RunsAPI.RunToolCallObject>;
    }
  }

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  export interface Usage {
    /**
     * Number of completion tokens used over the course of the run.
     */
    completion_tokens: number;

    /**
     * Number of prompt tokens used over the course of the run.
     */
    prompt_tokens: number;

    /**
     * Total number of tokens used (prompt + completion).
     */
    total_tokens: number;
  }
}

export interface RunListResponse {
  data: Array<RunListResponse.Data>;

  first_id: string;

  has_more: boolean;

  last_id: string;

  object: string;
}

export namespace RunListResponse {
  /**
   * Represents an execution run on a
   * [thread](https://platform.excai.com/docs/api-reference/threads).
   */
  export interface Data {
    /**
     * The identifier, which can be referenced in API endpoints.
     */
    id: string;

    /**
     * The ID of the
     * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
     * execution of this run.
     */
    assistant_id: string;

    /**
     * The Unix timestamp (in seconds) for when the run was cancelled.
     */
    cancelled_at: number | null;

    /**
     * The Unix timestamp (in seconds) for when the run was completed.
     */
    completed_at: number | null;

    /**
     * The Unix timestamp (in seconds) for when the run was created.
     */
    created_at: number;

    /**
     * The Unix timestamp (in seconds) for when the run will expire.
     */
    expires_at: number | null;

    /**
     * The Unix timestamp (in seconds) for when the run failed.
     */
    failed_at: number | null;

    /**
     * Details on why the run is incomplete. Will be `null` if the run is not
     * incomplete.
     */
    incomplete_details: Data.IncompleteDetails | null;

    /**
     * The instructions that the
     * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
     * this run.
     */
    instructions: string;

    /**
     * The last error associated with this run. Will be `null` if there are no errors.
     */
    last_error: Data.LastError | null;

    /**
     * The maximum number of completion tokens specified to have been used over the
     * course of the run.
     */
    max_completion_tokens: number | null;

    /**
     * The maximum number of prompt tokens specified to have been used over the course
     * of the run.
     */
    max_prompt_tokens: number | null;

    /**
     * Set of 16 key-value pairs that can be attached to an object. This can be useful
     * for storing additional information about the object in a structured format, and
     * querying for objects via API or the dashboard.
     *
     * Keys are strings with a maximum length of 64 characters. Values are strings with
     * a maximum length of 512 characters.
     */
    metadata: { [key: string]: string } | null;

    /**
     * The model that the
     * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
     * this run.
     */
    model: string;

    /**
     * The object type, which is always `thread.run`.
     */
    object: 'thread.run';

    /**
     * Whether to enable
     * [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
     * during tool use.
     */
    parallel_tool_calls: boolean;

    /**
     * Details on the action required to continue the run. Will be `null` if no action
     * is required.
     */
    required_action: Data.RequiredAction | null;

    /**
     * Specifies the format that the model must output. Compatible with
     * [GPT-4o](https://platform.excai.com/docs/models#gpt-4o),
     * [GPT-4 Turbo](https://platform.excai.com/docs/models#gpt-4-turbo-and-gpt-4), and
     * all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.
     *
     * Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
     * Outputs which ensures the model will match your supplied JSON schema. Learn more
     * in the
     * [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
     *
     * Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
     * message the model generates is valid JSON.
     *
     * **Important:** when using JSON mode, you **must** also instruct the model to
     * produce JSON yourself via a system or user message. Without this, the model may
     * generate an unending stream of whitespace until the generation reaches the token
     * limit, resulting in a long-running and seemingly "stuck" request. Also note that
     * the message content may be partially cut off if `finish_reason="length"`, which
     * indicates the generation exceeded `max_tokens` or the conversation exceeded the
     * max context length.
     */
    response_format:
      | 'auto'
      | Shared.ResponseFormatText
      | Shared.ResponseFormatJsonObject
      | Shared.ResponseFormatJsonSchema
      | null;

    /**
     * The Unix timestamp (in seconds) for when the run was started.
     */
    started_at: number | null;

    /**
     * The status of the run, which can be either `queued`, `in_progress`,
     * `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`,
     * `incomplete`, or `expired`.
     */
    status:
      | 'queued'
      | 'in_progress'
      | 'requires_action'
      | 'cancelling'
      | 'cancelled'
      | 'failed'
      | 'completed'
      | 'incomplete'
      | 'expired';

    /**
     * The ID of the [thread](https://platform.excai.com/docs/api-reference/threads)
     * that was executed on as a part of this run.
     */
    thread_id: string;

    /**
     * Controls which (if any) tool is called by the model. `none` means the model will
     * not call any tools and instead generates a message. `auto` is the default value
     * and means the model can pick between generating a message or calling one or more
     * tools. `required` means the model must call one or more tools before responding
     * to the user. Specifying a particular tool like `{"type": "file_search"}` or
     * `{"type": "function", "function": {"name": "my_function"}}` forces the model to
     * call that tool.
     */
    tool_choice: 'none' | 'auto' | 'required' | RunsAPI.AssistantsNamedToolChoice | null;

    /**
     * The list of tools that the
     * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
     * this run.
     */
    tools: Array<Shared.AssistantToolsCode | Shared.AssistantToolsFileSearch | Shared.AssistantToolsFunction>;

    /**
     * Controls for how a thread will be truncated prior to the run. Use this to
     * control the initial context window of the run.
     */
    truncation_strategy: RunsAPI.TruncationObject | null;

    /**
     * Usage statistics related to the run. This value will be `null` if the run is not
     * in a terminal state (i.e. `in_progress`, `queued`, etc.).
     */
    usage: Data.Usage | null;

    /**
     * The sampling temperature used for this run. If not set, defaults to 1.
     */
    temperature?: number | null;

    /**
     * The nucleus sampling value used for this run. If not set, defaults to 1.
     */
    top_p?: number | null;
  }

  export namespace Data {
    /**
     * Details on why the run is incomplete. Will be `null` if the run is not
     * incomplete.
     */
    export interface IncompleteDetails {
      /**
       * The reason why the run is incomplete. This will point to which specific token
       * limit was reached over the course of the run.
       */
      reason?: 'max_completion_tokens' | 'max_prompt_tokens';
    }

    /**
     * The last error associated with this run. Will be `null` if there are no errors.
     */
    export interface LastError {
      /**
       * One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.
       */
      code: 'server_error' | 'rate_limit_exceeded' | 'invalid_prompt';

      /**
       * A human-readable description of the error.
       */
      message: string;
    }

    /**
     * Details on the action required to continue the run. Will be `null` if no action
     * is required.
     */
    export interface RequiredAction {
      /**
       * Details on the tool outputs needed for this run to continue.
       */
      submit_tool_outputs: RequiredAction.SubmitToolOutputs;

      /**
       * For now, this is always `submit_tool_outputs`.
       */
      type: 'submit_tool_outputs';
    }

    export namespace RequiredAction {
      /**
       * Details on the tool outputs needed for this run to continue.
       */
      export interface SubmitToolOutputs {
        /**
         * A list of the relevant tool calls.
         */
        tool_calls: Array<RunsAPI.RunToolCallObject>;
      }
    }

    /**
     * Usage statistics related to the run. This value will be `null` if the run is not
     * in a terminal state (i.e. `in_progress`, `queued`, etc.).
     */
    export interface Usage {
      /**
       * Number of completion tokens used over the course of the run.
       */
      completion_tokens: number;

      /**
       * Number of prompt tokens used over the course of the run.
       */
      prompt_tokens: number;

      /**
       * Total number of tokens used (prompt + completion).
       */
      total_tokens: number;
    }
  }
}

/**
 * Represents an execution run on a
 * [thread](https://platform.excai.com/docs/api-reference/threads).
 */
export interface RunCancelResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The ID of the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * execution of this run.
   */
  assistant_id: string;

  /**
   * The Unix timestamp (in seconds) for when the run was cancelled.
   */
  cancelled_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was completed.
   */
  completed_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was created.
   */
  created_at: number;

  /**
   * The Unix timestamp (in seconds) for when the run will expire.
   */
  expires_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run failed.
   */
  failed_at: number | null;

  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  incomplete_details: RunCancelResponse.IncompleteDetails | null;

  /**
   * The instructions that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  instructions: string;

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  last_error: RunCancelResponse.LastError | null;

  /**
   * The maximum number of completion tokens specified to have been used over the
   * course of the run.
   */
  max_completion_tokens: number | null;

  /**
   * The maximum number of prompt tokens specified to have been used over the course
   * of the run.
   */
  max_prompt_tokens: number | null;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata: { [key: string]: string } | null;

  /**
   * The model that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  model: string;

  /**
   * The object type, which is always `thread.run`.
   */
  object: 'thread.run';

  /**
   * Whether to enable
   * [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
   * during tool use.
   */
  parallel_tool_calls: boolean;

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  required_action: RunCancelResponse.RequiredAction | null;

  /**
   * Specifies the format that the model must output. Compatible with
   * [GPT-4o](https://platform.excai.com/docs/models#gpt-4o),
   * [GPT-4 Turbo](https://platform.excai.com/docs/models#gpt-4-turbo-and-gpt-4), and
   * all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.
   *
   * Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
   * Outputs which ensures the model will match your supplied JSON schema. Learn more
   * in the
   * [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
   *
   * Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
   * message the model generates is valid JSON.
   *
   * **Important:** when using JSON mode, you **must** also instruct the model to
   * produce JSON yourself via a system or user message. Without this, the model may
   * generate an unending stream of whitespace until the generation reaches the token
   * limit, resulting in a long-running and seemingly "stuck" request. Also note that
   * the message content may be partially cut off if `finish_reason="length"`, which
   * indicates the generation exceeded `max_tokens` or the conversation exceeded the
   * max context length.
   */
  response_format:
    | 'auto'
    | Shared.ResponseFormatText
    | Shared.ResponseFormatJsonObject
    | Shared.ResponseFormatJsonSchema
    | null;

  /**
   * The Unix timestamp (in seconds) for when the run was started.
   */
  started_at: number | null;

  /**
   * The status of the run, which can be either `queued`, `in_progress`,
   * `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`,
   * `incomplete`, or `expired`.
   */
  status:
    | 'queued'
    | 'in_progress'
    | 'requires_action'
    | 'cancelling'
    | 'cancelled'
    | 'failed'
    | 'completed'
    | 'incomplete'
    | 'expired';

  /**
   * The ID of the [thread](https://platform.excai.com/docs/api-reference/threads)
   * that was executed on as a part of this run.
   */
  thread_id: string;

  /**
   * Controls which (if any) tool is called by the model. `none` means the model will
   * not call any tools and instead generates a message. `auto` is the default value
   * and means the model can pick between generating a message or calling one or more
   * tools. `required` means the model must call one or more tools before responding
   * to the user. Specifying a particular tool like `{"type": "file_search"}` or
   * `{"type": "function", "function": {"name": "my_function"}}` forces the model to
   * call that tool.
   */
  tool_choice: 'none' | 'auto' | 'required' | AssistantsNamedToolChoice | null;

  /**
   * The list of tools that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  tools: Array<Shared.AssistantToolsCode | Shared.AssistantToolsFileSearch | Shared.AssistantToolsFunction>;

  /**
   * Controls for how a thread will be truncated prior to the run. Use this to
   * control the initial context window of the run.
   */
  truncation_strategy: TruncationObject | null;

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  usage: RunCancelResponse.Usage | null;

  /**
   * The sampling temperature used for this run. If not set, defaults to 1.
   */
  temperature?: number | null;

  /**
   * The nucleus sampling value used for this run. If not set, defaults to 1.
   */
  top_p?: number | null;
}

export namespace RunCancelResponse {
  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  export interface IncompleteDetails {
    /**
     * The reason why the run is incomplete. This will point to which specific token
     * limit was reached over the course of the run.
     */
    reason?: 'max_completion_tokens' | 'max_prompt_tokens';
  }

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  export interface LastError {
    /**
     * One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.
     */
    code: 'server_error' | 'rate_limit_exceeded' | 'invalid_prompt';

    /**
     * A human-readable description of the error.
     */
    message: string;
  }

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  export interface RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    submit_tool_outputs: RequiredAction.SubmitToolOutputs;

    /**
     * For now, this is always `submit_tool_outputs`.
     */
    type: 'submit_tool_outputs';
  }

  export namespace RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    export interface SubmitToolOutputs {
      /**
       * A list of the relevant tool calls.
       */
      tool_calls: Array<RunsAPI.RunToolCallObject>;
    }
  }

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  export interface Usage {
    /**
     * Number of completion tokens used over the course of the run.
     */
    completion_tokens: number;

    /**
     * Number of prompt tokens used over the course of the run.
     */
    prompt_tokens: number;

    /**
     * Total number of tokens used (prompt + completion).
     */
    total_tokens: number;
  }
}

/**
 * Represents an execution run on a
 * [thread](https://platform.excai.com/docs/api-reference/threads).
 */
export interface RunCreateWithRunResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The ID of the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * execution of this run.
   */
  assistant_id: string;

  /**
   * The Unix timestamp (in seconds) for when the run was cancelled.
   */
  cancelled_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was completed.
   */
  completed_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was created.
   */
  created_at: number;

  /**
   * The Unix timestamp (in seconds) for when the run will expire.
   */
  expires_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run failed.
   */
  failed_at: number | null;

  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  incomplete_details: RunCreateWithRunResponse.IncompleteDetails | null;

  /**
   * The instructions that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  instructions: string;

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  last_error: RunCreateWithRunResponse.LastError | null;

  /**
   * The maximum number of completion tokens specified to have been used over the
   * course of the run.
   */
  max_completion_tokens: number | null;

  /**
   * The maximum number of prompt tokens specified to have been used over the course
   * of the run.
   */
  max_prompt_tokens: number | null;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata: { [key: string]: string } | null;

  /**
   * The model that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  model: string;

  /**
   * The object type, which is always `thread.run`.
   */
  object: 'thread.run';

  /**
   * Whether to enable
   * [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
   * during tool use.
   */
  parallel_tool_calls: boolean;

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  required_action: RunCreateWithRunResponse.RequiredAction | null;

  /**
   * Specifies the format that the model must output. Compatible with
   * [GPT-4o](https://platform.excai.com/docs/models#gpt-4o),
   * [GPT-4 Turbo](https://platform.excai.com/docs/models#gpt-4-turbo-and-gpt-4), and
   * all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.
   *
   * Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
   * Outputs which ensures the model will match your supplied JSON schema. Learn more
   * in the
   * [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
   *
   * Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
   * message the model generates is valid JSON.
   *
   * **Important:** when using JSON mode, you **must** also instruct the model to
   * produce JSON yourself via a system or user message. Without this, the model may
   * generate an unending stream of whitespace until the generation reaches the token
   * limit, resulting in a long-running and seemingly "stuck" request. Also note that
   * the message content may be partially cut off if `finish_reason="length"`, which
   * indicates the generation exceeded `max_tokens` or the conversation exceeded the
   * max context length.
   */
  response_format:
    | 'auto'
    | Shared.ResponseFormatText
    | Shared.ResponseFormatJsonObject
    | Shared.ResponseFormatJsonSchema
    | null;

  /**
   * The Unix timestamp (in seconds) for when the run was started.
   */
  started_at: number | null;

  /**
   * The status of the run, which can be either `queued`, `in_progress`,
   * `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`,
   * `incomplete`, or `expired`.
   */
  status:
    | 'queued'
    | 'in_progress'
    | 'requires_action'
    | 'cancelling'
    | 'cancelled'
    | 'failed'
    | 'completed'
    | 'incomplete'
    | 'expired';

  /**
   * The ID of the [thread](https://platform.excai.com/docs/api-reference/threads)
   * that was executed on as a part of this run.
   */
  thread_id: string;

  /**
   * Controls which (if any) tool is called by the model. `none` means the model will
   * not call any tools and instead generates a message. `auto` is the default value
   * and means the model can pick between generating a message or calling one or more
   * tools. `required` means the model must call one or more tools before responding
   * to the user. Specifying a particular tool like `{"type": "file_search"}` or
   * `{"type": "function", "function": {"name": "my_function"}}` forces the model to
   * call that tool.
   */
  tool_choice: 'none' | 'auto' | 'required' | AssistantsNamedToolChoice | null;

  /**
   * The list of tools that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  tools: Array<Shared.AssistantToolsCode | Shared.AssistantToolsFileSearch | Shared.AssistantToolsFunction>;

  /**
   * Controls for how a thread will be truncated prior to the run. Use this to
   * control the initial context window of the run.
   */
  truncation_strategy: TruncationObject | null;

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  usage: RunCreateWithRunResponse.Usage | null;

  /**
   * The sampling temperature used for this run. If not set, defaults to 1.
   */
  temperature?: number | null;

  /**
   * The nucleus sampling value used for this run. If not set, defaults to 1.
   */
  top_p?: number | null;
}

export namespace RunCreateWithRunResponse {
  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  export interface IncompleteDetails {
    /**
     * The reason why the run is incomplete. This will point to which specific token
     * limit was reached over the course of the run.
     */
    reason?: 'max_completion_tokens' | 'max_prompt_tokens';
  }

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  export interface LastError {
    /**
     * One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.
     */
    code: 'server_error' | 'rate_limit_exceeded' | 'invalid_prompt';

    /**
     * A human-readable description of the error.
     */
    message: string;
  }

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  export interface RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    submit_tool_outputs: RequiredAction.SubmitToolOutputs;

    /**
     * For now, this is always `submit_tool_outputs`.
     */
    type: 'submit_tool_outputs';
  }

  export namespace RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    export interface SubmitToolOutputs {
      /**
       * A list of the relevant tool calls.
       */
      tool_calls: Array<RunsAPI.RunToolCallObject>;
    }
  }

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  export interface Usage {
    /**
     * Number of completion tokens used over the course of the run.
     */
    completion_tokens: number;

    /**
     * Number of prompt tokens used over the course of the run.
     */
    prompt_tokens: number;

    /**
     * Total number of tokens used (prompt + completion).
     */
    total_tokens: number;
  }
}

/**
 * Represents an execution run on a
 * [thread](https://platform.excai.com/docs/api-reference/threads).
 */
export interface RunSubmitToolOutputsResponse {
  /**
   * The identifier, which can be referenced in API endpoints.
   */
  id: string;

  /**
   * The ID of the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * execution of this run.
   */
  assistant_id: string;

  /**
   * The Unix timestamp (in seconds) for when the run was cancelled.
   */
  cancelled_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was completed.
   */
  completed_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run was created.
   */
  created_at: number;

  /**
   * The Unix timestamp (in seconds) for when the run will expire.
   */
  expires_at: number | null;

  /**
   * The Unix timestamp (in seconds) for when the run failed.
   */
  failed_at: number | null;

  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  incomplete_details: RunSubmitToolOutputsResponse.IncompleteDetails | null;

  /**
   * The instructions that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  instructions: string;

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  last_error: RunSubmitToolOutputsResponse.LastError | null;

  /**
   * The maximum number of completion tokens specified to have been used over the
   * course of the run.
   */
  max_completion_tokens: number | null;

  /**
   * The maximum number of prompt tokens specified to have been used over the course
   * of the run.
   */
  max_prompt_tokens: number | null;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata: { [key: string]: string } | null;

  /**
   * The model that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  model: string;

  /**
   * The object type, which is always `thread.run`.
   */
  object: 'thread.run';

  /**
   * Whether to enable
   * [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
   * during tool use.
   */
  parallel_tool_calls: boolean;

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  required_action: RunSubmitToolOutputsResponse.RequiredAction | null;

  /**
   * Specifies the format that the model must output. Compatible with
   * [GPT-4o](https://platform.excai.com/docs/models#gpt-4o),
   * [GPT-4 Turbo](https://platform.excai.com/docs/models#gpt-4-turbo-and-gpt-4), and
   * all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.
   *
   * Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
   * Outputs which ensures the model will match your supplied JSON schema. Learn more
   * in the
   * [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
   *
   * Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
   * message the model generates is valid JSON.
   *
   * **Important:** when using JSON mode, you **must** also instruct the model to
   * produce JSON yourself via a system or user message. Without this, the model may
   * generate an unending stream of whitespace until the generation reaches the token
   * limit, resulting in a long-running and seemingly "stuck" request. Also note that
   * the message content may be partially cut off if `finish_reason="length"`, which
   * indicates the generation exceeded `max_tokens` or the conversation exceeded the
   * max context length.
   */
  response_format:
    | 'auto'
    | Shared.ResponseFormatText
    | Shared.ResponseFormatJsonObject
    | Shared.ResponseFormatJsonSchema
    | null;

  /**
   * The Unix timestamp (in seconds) for when the run was started.
   */
  started_at: number | null;

  /**
   * The status of the run, which can be either `queued`, `in_progress`,
   * `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`,
   * `incomplete`, or `expired`.
   */
  status:
    | 'queued'
    | 'in_progress'
    | 'requires_action'
    | 'cancelling'
    | 'cancelled'
    | 'failed'
    | 'completed'
    | 'incomplete'
    | 'expired';

  /**
   * The ID of the [thread](https://platform.excai.com/docs/api-reference/threads)
   * that was executed on as a part of this run.
   */
  thread_id: string;

  /**
   * Controls which (if any) tool is called by the model. `none` means the model will
   * not call any tools and instead generates a message. `auto` is the default value
   * and means the model can pick between generating a message or calling one or more
   * tools. `required` means the model must call one or more tools before responding
   * to the user. Specifying a particular tool like `{"type": "file_search"}` or
   * `{"type": "function", "function": {"name": "my_function"}}` forces the model to
   * call that tool.
   */
  tool_choice: 'none' | 'auto' | 'required' | AssistantsNamedToolChoice | null;

  /**
   * The list of tools that the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) used for
   * this run.
   */
  tools: Array<Shared.AssistantToolsCode | Shared.AssistantToolsFileSearch | Shared.AssistantToolsFunction>;

  /**
   * Controls for how a thread will be truncated prior to the run. Use this to
   * control the initial context window of the run.
   */
  truncation_strategy: TruncationObject | null;

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  usage: RunSubmitToolOutputsResponse.Usage | null;

  /**
   * The sampling temperature used for this run. If not set, defaults to 1.
   */
  temperature?: number | null;

  /**
   * The nucleus sampling value used for this run. If not set, defaults to 1.
   */
  top_p?: number | null;
}

export namespace RunSubmitToolOutputsResponse {
  /**
   * Details on why the run is incomplete. Will be `null` if the run is not
   * incomplete.
   */
  export interface IncompleteDetails {
    /**
     * The reason why the run is incomplete. This will point to which specific token
     * limit was reached over the course of the run.
     */
    reason?: 'max_completion_tokens' | 'max_prompt_tokens';
  }

  /**
   * The last error associated with this run. Will be `null` if there are no errors.
   */
  export interface LastError {
    /**
     * One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.
     */
    code: 'server_error' | 'rate_limit_exceeded' | 'invalid_prompt';

    /**
     * A human-readable description of the error.
     */
    message: string;
  }

  /**
   * Details on the action required to continue the run. Will be `null` if no action
   * is required.
   */
  export interface RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    submit_tool_outputs: RequiredAction.SubmitToolOutputs;

    /**
     * For now, this is always `submit_tool_outputs`.
     */
    type: 'submit_tool_outputs';
  }

  export namespace RequiredAction {
    /**
     * Details on the tool outputs needed for this run to continue.
     */
    export interface SubmitToolOutputs {
      /**
       * A list of the relevant tool calls.
       */
      tool_calls: Array<RunsAPI.RunToolCallObject>;
    }
  }

  /**
   * Usage statistics related to the run. This value will be `null` if the run is not
   * in a terminal state (i.e. `in_progress`, `queued`, etc.).
   */
  export interface Usage {
    /**
     * Number of completion tokens used over the course of the run.
     */
    completion_tokens: number;

    /**
     * Number of prompt tokens used over the course of the run.
     */
    prompt_tokens: number;

    /**
     * Total number of tokens used (prompt + completion).
     */
    total_tokens: number;
  }
}

export interface RunCreateParams {
  /**
   * Body param: The ID of the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) to use to
   * execute this run.
   */
  assistant_id: string;

  /**
   * Query param: A list of additional fields to include in the response. Currently
   * the only supported value is
   * `step_details.tool_calls[*].file_search.results[*].content` to fetch the file
   * search result content.
   *
   * See the
   * [file search tool documentation](https://platform.excai.com/docs/assistants/tools/file-search#customizing-file-search-settings)
   * for more information.
   */
  include?: Array<'step_details.tool_calls[*].file_search.results[*].content'>;

  /**
   * Body param: Appends additional instructions at the end of the instructions for
   * the run. This is useful for modifying the behavior on a per-run basis without
   * overriding other instructions.
   */
  additional_instructions?: string | null;

  /**
   * Body param: Adds additional messages to the thread before creating the run.
   */
  additional_messages?: Array<RunCreateParams.AdditionalMessage> | null;

  /**
   * Body param: Overrides the
   * [instructions](https://platform.excai.com/docs/api-reference/assistants/createAssistant)
   * of the assistant. This is useful for modifying the behavior on a per-run basis.
   */
  instructions?: string | null;

  /**
   * Body param: The maximum number of completion tokens that may be used over the
   * course of the run. The run will make a best effort to use only the number of
   * completion tokens specified, across multiple turns of the run. If the run
   * exceeds the number of completion tokens specified, the run will end with status
   * `incomplete`. See `incomplete_details` for more info.
   */
  max_completion_tokens?: number | null;

  /**
   * Body param: The maximum number of prompt tokens that may be used over the course
   * of the run. The run will make a best effort to use only the number of prompt
   * tokens specified, across multiple turns of the run. If the run exceeds the
   * number of prompt tokens specified, the run will end with status `incomplete`.
   * See `incomplete_details` for more info.
   */
  max_prompt_tokens?: number | null;

  /**
   * Body param: Set of 16 key-value pairs that can be attached to an object. This
   * can be useful for storing additional information about the object in a
   * structured format, and querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata?: { [key: string]: string } | null;

  /**
   * Body param: The ID of the
   * [Model](https://platform.excai.com/docs/api-reference/models) to be used to
   * execute this run. If a value is provided here, it will override the model
   * associated with the assistant. If not, the model associated with the assistant
   * will be used.
   */
  model?:
    | (string & {})
    | 'gpt-5'
    | 'gpt-5-mini'
    | 'gpt-5-nano'
    | 'gpt-5-2025-08-07'
    | 'gpt-5-mini-2025-08-07'
    | 'gpt-5-nano-2025-08-07'
    | 'gpt-4.1'
    | 'gpt-4.1-mini'
    | 'gpt-4.1-nano'
    | 'gpt-4.1-2025-04-14'
    | 'gpt-4.1-mini-2025-04-14'
    | 'gpt-4.1-nano-2025-04-14'
    | 'o3-mini'
    | 'o3-mini-2025-01-31'
    | 'o1'
    | 'o1-2024-12-17'
    | 'gpt-4o'
    | 'gpt-4o-2024-11-20'
    | 'gpt-4o-2024-08-06'
    | 'gpt-4o-2024-05-13'
    | 'gpt-4o-mini'
    | 'gpt-4o-mini-2024-07-18'
    | 'gpt-4.5-preview'
    | 'gpt-4.5-preview-2025-02-27'
    | 'gpt-4-turbo'
    | 'gpt-4-turbo-2024-04-09'
    | 'gpt-4-0125-preview'
    | 'gpt-4-turbo-preview'
    | 'gpt-4-1106-preview'
    | 'gpt-4-vision-preview'
    | 'gpt-4'
    | 'gpt-4-0314'
    | 'gpt-4-0613'
    | 'gpt-4-32k'
    | 'gpt-4-32k-0314'
    | 'gpt-4-32k-0613'
    | 'gpt-3.5-turbo'
    | 'gpt-3.5-turbo-16k'
    | 'gpt-3.5-turbo-0613'
    | 'gpt-3.5-turbo-1106'
    | 'gpt-3.5-turbo-0125'
    | 'gpt-3.5-turbo-16k-0613'
    | null;

  /**
   * Body param: Whether to enable
   * [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
   * during tool use.
   */
  parallel_tool_calls?: boolean;

  /**
   * Body param: Constrains effort on reasoning for
   * [reasoning models](https://platform.excai.com/docs/guides/reasoning). Currently
   * supported values are `minimal`, `low`, `medium`, and `high`. Reducing reasoning
   * effort can result in faster responses and fewer tokens used on reasoning in a
   * response.
   *
   * Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning
   * effort.
   */
  reasoning_effort?: 'minimal' | 'low' | 'medium' | 'high' | null;

  /**
   * Body param: Specifies the format that the model must output. Compatible with
   * [GPT-4o](https://platform.excai.com/docs/models#gpt-4o),
   * [GPT-4 Turbo](https://platform.excai.com/docs/models#gpt-4-turbo-and-gpt-4), and
   * all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.
   *
   * Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
   * Outputs which ensures the model will match your supplied JSON schema. Learn more
   * in the
   * [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
   *
   * Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
   * message the model generates is valid JSON.
   *
   * **Important:** when using JSON mode, you **must** also instruct the model to
   * produce JSON yourself via a system or user message. Without this, the model may
   * generate an unending stream of whitespace until the generation reaches the token
   * limit, resulting in a long-running and seemingly "stuck" request. Also note that
   * the message content may be partially cut off if `finish_reason="length"`, which
   * indicates the generation exceeded `max_tokens` or the conversation exceeded the
   * max context length.
   */
  response_format?:
    | 'auto'
    | Shared.ResponseFormatText
    | Shared.ResponseFormatJsonObject
    | Shared.ResponseFormatJsonSchema
    | null;

  /**
   * Body param: If `true`, returns a stream of events that happen during the Run as
   * server-sent events, terminating when the Run enters a terminal state with a
   * `data: [DONE]` message.
   */
  stream?: boolean | null;

  /**
   * Body param: What sampling temperature to use, between 0 and 2. Higher values
   * like 0.8 will make the output more random, while lower values like 0.2 will make
   * it more focused and deterministic.
   */
  temperature?: number | null;

  /**
   * Body param: Controls which (if any) tool is called by the model. `none` means
   * the model will not call any tools and instead generates a message. `auto` is the
   * default value and means the model can pick between generating a message or
   * calling one or more tools. `required` means the model must call one or more
   * tools before responding to the user. Specifying a particular tool like
   * `{"type": "file_search"}` or
   * `{"type": "function", "function": {"name": "my_function"}}` forces the model to
   * call that tool.
   */
  tool_choice?: 'none' | 'auto' | 'required' | AssistantsNamedToolChoice | null;

  /**
   * Body param: Override the tools the assistant can use for this run. This is
   * useful for modifying the behavior on a per-run basis.
   */
  tools?: Array<
    Shared.AssistantToolsCode | Shared.AssistantToolsFileSearch | Shared.AssistantToolsFunction
  > | null;

  /**
   * Body param: An alternative to sampling with temperature, called nucleus
   * sampling, where the model considers the results of the tokens with top_p
   * probability mass. So 0.1 means only the tokens comprising the top 10%
   * probability mass are considered.
   *
   * We generally recommend altering this or temperature but not both.
   */
  top_p?: number | null;

  /**
   * Body param: Controls for how a thread will be truncated prior to the run. Use
   * this to control the initial context window of the run.
   */
  truncation_strategy?: TruncationObject | null;
}

export namespace RunCreateParams {
  export interface AdditionalMessage {
    /**
     * The text contents of the message.
     */
    content:
      | string
      | Array<
          | MessagesAPI.MessageContentImageFileObject
          | MessagesAPI.MessageContentImageURLObject
          | AdditionalMessage.Text
        >;

    /**
     * The role of the entity that is creating the message. Allowed values include:
     *
     * - `user`: Indicates the message is sent by an actual user and should be used in
     *   most cases to represent user-generated messages.
     * - `assistant`: Indicates the message is generated by the assistant. Use this
     *   value to insert messages from the assistant into the conversation.
     */
    role: 'user' | 'assistant';

    /**
     * A list of files attached to the message, and the tools they should be added to.
     */
    attachments?: Array<AdditionalMessage.Attachment> | null;

    /**
     * Set of 16 key-value pairs that can be attached to an object. This can be useful
     * for storing additional information about the object in a structured format, and
     * querying for objects via API or the dashboard.
     *
     * Keys are strings with a maximum length of 64 characters. Values are strings with
     * a maximum length of 512 characters.
     */
    metadata?: { [key: string]: string } | null;
  }

  export namespace AdditionalMessage {
    /**
     * The text content that is part of a message.
     */
    export interface Text {
      /**
       * Text content to be sent to the model
       */
      text: string;

      /**
       * Always `text`.
       */
      type: 'text';
    }

    export interface Attachment {
      /**
       * The ID of the file to attach to the message.
       */
      file_id?: string;

      /**
       * The tools to add this file to.
       */
      tools?: Array<Shared.AssistantToolsCode | ThreadsAPI.AssistantToolsFileSearchTypeOnly>;
    }
  }
}

export interface RunUpdateParams {
  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata?: { [key: string]: string } | null;
}

export interface RunListParams {
  /**
   * A cursor for use in pagination. `after` is an object ID that defines your place
   * in the list. For instance, if you make a list request and receive 100 objects,
   * ending with obj_foo, your subsequent call can include after=obj_foo in order to
   * fetch the next page of the list.
   */
  after?: string;

  /**
   * A cursor for use in pagination. `before` is an object ID that defines your place
   * in the list. For instance, if you make a list request and receive 100 objects,
   * starting with obj_foo, your subsequent call can include before=obj_foo in order
   * to fetch the previous page of the list.
   */
  before?: string;

  /**
   * A limit on the number of objects to be returned. Limit can range between 1 and
   * 100, and the default is 20.
   */
  limit?: number;

  /**
   * Sort order by the `created_at` timestamp of the objects. `asc` for ascending
   * order and `desc` for descending order.
   */
  order?: 'asc' | 'desc';
}

export interface RunCreateWithRunParams {
  /**
   * The ID of the
   * [assistant](https://platform.excai.com/docs/api-reference/assistants) to use to
   * execute this run.
   */
  assistant_id: string;

  /**
   * Override the default system message of the assistant. This is useful for
   * modifying the behavior on a per-run basis.
   */
  instructions?: string | null;

  /**
   * The maximum number of completion tokens that may be used over the course of the
   * run. The run will make a best effort to use only the number of completion tokens
   * specified, across multiple turns of the run. If the run exceeds the number of
   * completion tokens specified, the run will end with status `incomplete`. See
   * `incomplete_details` for more info.
   */
  max_completion_tokens?: number | null;

  /**
   * The maximum number of prompt tokens that may be used over the course of the run.
   * The run will make a best effort to use only the number of prompt tokens
   * specified, across multiple turns of the run. If the run exceeds the number of
   * prompt tokens specified, the run will end with status `incomplete`. See
   * `incomplete_details` for more info.
   */
  max_prompt_tokens?: number | null;

  /**
   * Set of 16 key-value pairs that can be attached to an object. This can be useful
   * for storing additional information about the object in a structured format, and
   * querying for objects via API or the dashboard.
   *
   * Keys are strings with a maximum length of 64 characters. Values are strings with
   * a maximum length of 512 characters.
   */
  metadata?: { [key: string]: string } | null;

  /**
   * The ID of the [Model](https://platform.excai.com/docs/api-reference/models) to
   * be used to execute this run. If a value is provided here, it will override the
   * model associated with the assistant. If not, the model associated with the
   * assistant will be used.
   */
  model?:
    | (string & {})
    | 'gpt-5'
    | 'gpt-5-mini'
    | 'gpt-5-nano'
    | 'gpt-5-2025-08-07'
    | 'gpt-5-mini-2025-08-07'
    | 'gpt-5-nano-2025-08-07'
    | 'gpt-4.1'
    | 'gpt-4.1-mini'
    | 'gpt-4.1-nano'
    | 'gpt-4.1-2025-04-14'
    | 'gpt-4.1-mini-2025-04-14'
    | 'gpt-4.1-nano-2025-04-14'
    | 'gpt-4o'
    | 'gpt-4o-2024-11-20'
    | 'gpt-4o-2024-08-06'
    | 'gpt-4o-2024-05-13'
    | 'gpt-4o-mini'
    | 'gpt-4o-mini-2024-07-18'
    | 'gpt-4.5-preview'
    | 'gpt-4.5-preview-2025-02-27'
    | 'gpt-4-turbo'
    | 'gpt-4-turbo-2024-04-09'
    | 'gpt-4-0125-preview'
    | 'gpt-4-turbo-preview'
    | 'gpt-4-1106-preview'
    | 'gpt-4-vision-preview'
    | 'gpt-4'
    | 'gpt-4-0314'
    | 'gpt-4-0613'
    | 'gpt-4-32k'
    | 'gpt-4-32k-0314'
    | 'gpt-4-32k-0613'
    | 'gpt-3.5-turbo'
    | 'gpt-3.5-turbo-16k'
    | 'gpt-3.5-turbo-0613'
    | 'gpt-3.5-turbo-1106'
    | 'gpt-3.5-turbo-0125'
    | 'gpt-3.5-turbo-16k-0613'
    | null;

  /**
   * Whether to enable
   * [parallel function calling](https://platform.excai.com/docs/guides/function-calling#configuring-parallel-function-calling)
   * during tool use.
   */
  parallel_tool_calls?: boolean;

  /**
   * Specifies the format that the model must output. Compatible with
   * [GPT-4o](https://platform.excai.com/docs/models#gpt-4o),
   * [GPT-4 Turbo](https://platform.excai.com/docs/models#gpt-4-turbo-and-gpt-4), and
   * all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.
   *
   * Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
   * Outputs which ensures the model will match your supplied JSON schema. Learn more
   * in the
   * [Structured Outputs guide](https://platform.excai.com/docs/guides/structured-outputs).
   *
   * Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
   * message the model generates is valid JSON.
   *
   * **Important:** when using JSON mode, you **must** also instruct the model to
   * produce JSON yourself via a system or user message. Without this, the model may
   * generate an unending stream of whitespace until the generation reaches the token
   * limit, resulting in a long-running and seemingly "stuck" request. Also note that
   * the message content may be partially cut off if `finish_reason="length"`, which
   * indicates the generation exceeded `max_tokens` or the conversation exceeded the
   * max context length.
   */
  response_format?:
    | 'auto'
    | Shared.ResponseFormatText
    | Shared.ResponseFormatJsonObject
    | Shared.ResponseFormatJsonSchema
    | null;

  /**
   * If `true`, returns a stream of events that happen during the Run as server-sent
   * events, terminating when the Run enters a terminal state with a `data: [DONE]`
   * message.
   */
  stream?: boolean | null;

  /**
   * What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
   * make the output more random, while lower values like 0.2 will make it more
   * focused and deterministic.
   */
  temperature?: number | null;

  /**
   * Options to create a new thread. If no thread is provided when running a request,
   * an empty thread will be created.
   */
  thread?: RunCreateWithRunParams.Thread;

  /**
   * Controls which (if any) tool is called by the model. `none` means the model will
   * not call any tools and instead generates a message. `auto` is the default value
   * and means the model can pick between generating a message or calling one or more
   * tools. `required` means the model must call one or more tools before responding
   * to the user. Specifying a particular tool like `{"type": "file_search"}` or
   * `{"type": "function", "function": {"name": "my_function"}}` forces the model to
   * call that tool.
   */
  tool_choice?: 'none' | 'auto' | 'required' | AssistantsNamedToolChoice | null;

  /**
   * A set of resources that are used by the assistant's tools. The resources are
   * specific to the type of tool. For example, the `code_interpreter` tool requires
   * a list of file IDs, while the `file_search` tool requires a list of vector store
   * IDs.
   */
  tool_resources?: RunCreateWithRunParams.ToolResources | null;

  /**
   * Override the tools the assistant can use for this run. This is useful for
   * modifying the behavior on a per-run basis.
   */
  tools?: Array<
    Shared.AssistantToolsCode | Shared.AssistantToolsFileSearch | Shared.AssistantToolsFunction
  > | null;

  /**
   * An alternative to sampling with temperature, called nucleus sampling, where the
   * model considers the results of the tokens with top_p probability mass. So 0.1
   * means only the tokens comprising the top 10% probability mass are considered.
   *
   * We generally recommend altering this or temperature but not both.
   */
  top_p?: number | null;

  /**
   * Controls for how a thread will be truncated prior to the run. Use this to
   * control the initial context window of the run.
   */
  truncation_strategy?: TruncationObject | null;
}

export namespace RunCreateWithRunParams {
  /**
   * Options to create a new thread. If no thread is provided when running a request,
   * an empty thread will be created.
   */
  export interface Thread {
    /**
     * A list of [messages](https://platform.excai.com/docs/api-reference/messages) to
     * start the thread with.
     */
    messages?: Array<Thread.Message>;

    /**
     * Set of 16 key-value pairs that can be attached to an object. This can be useful
     * for storing additional information about the object in a structured format, and
     * querying for objects via API or the dashboard.
     *
     * Keys are strings with a maximum length of 64 characters. Values are strings with
     * a maximum length of 512 characters.
     */
    metadata?: { [key: string]: string } | null;

    /**
     * A set of resources that are made available to the assistant's tools in this
     * thread. The resources are specific to the type of tool. For example, the
     * `code_interpreter` tool requires a list of file IDs, while the `file_search`
     * tool requires a list of vector store IDs.
     */
    tool_resources?: Thread.ToolResources | null;
  }

  export namespace Thread {
    export interface Message {
      /**
       * The text contents of the message.
       */
      content:
        | string
        | Array<
            | MessagesAPI.MessageContentImageFileObject
            | MessagesAPI.MessageContentImageURLObject
            | Message.Text
          >;

      /**
       * The role of the entity that is creating the message. Allowed values include:
       *
       * - `user`: Indicates the message is sent by an actual user and should be used in
       *   most cases to represent user-generated messages.
       * - `assistant`: Indicates the message is generated by the assistant. Use this
       *   value to insert messages from the assistant into the conversation.
       */
      role: 'user' | 'assistant';

      /**
       * A list of files attached to the message, and the tools they should be added to.
       */
      attachments?: Array<Message.Attachment> | null;

      /**
       * Set of 16 key-value pairs that can be attached to an object. This can be useful
       * for storing additional information about the object in a structured format, and
       * querying for objects via API or the dashboard.
       *
       * Keys are strings with a maximum length of 64 characters. Values are strings with
       * a maximum length of 512 characters.
       */
      metadata?: { [key: string]: string } | null;
    }

    export namespace Message {
      /**
       * The text content that is part of a message.
       */
      export interface Text {
        /**
         * Text content to be sent to the model
         */
        text: string;

        /**
         * Always `text`.
         */
        type: 'text';
      }

      export interface Attachment {
        /**
         * The ID of the file to attach to the message.
         */
        file_id?: string;

        /**
         * The tools to add this file to.
         */
        tools?: Array<Shared.AssistantToolsCode | ThreadsAPI.AssistantToolsFileSearchTypeOnly>;
      }
    }

    /**
     * A set of resources that are made available to the assistant's tools in this
     * thread. The resources are specific to the type of tool. For example, the
     * `code_interpreter` tool requires a list of file IDs, while the `file_search`
     * tool requires a list of vector store IDs.
     */
    export interface ToolResources {
      code_interpreter?: ToolResources.CodeInterpreter;

      file_search?: ToolResources.FileSearch;
    }

    export namespace ToolResources {
      export interface CodeInterpreter {
        /**
         * A list of [file](https://platform.excai.com/docs/api-reference/files) IDs made
         * available to the `code_interpreter` tool. There can be a maximum of 20 files
         * associated with the tool.
         */
        file_ids?: Array<string>;
      }

      export interface FileSearch {
        /**
         * The
         * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
         * attached to this thread. There can be a maximum of 1 vector store attached to
         * the thread.
         */
        vector_store_ids?: Array<string>;

        /**
         * A helper to create a
         * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
         * with file_ids and attach it to this thread. There can be a maximum of 1 vector
         * store attached to the thread.
         */
        vector_stores?: Array<FileSearch.VectorStore>;
      }

      export namespace FileSearch {
        export interface VectorStore {
          /**
           * The chunking strategy used to chunk the file(s). If not set, will use the `auto`
           * strategy.
           */
          chunking_strategy?: VectorStore.Auto | VectorStore.Static;

          /**
           * A list of [file](https://platform.excai.com/docs/api-reference/files) IDs to add
           * to the vector store. There can be a maximum of 10000 files in a vector store.
           */
          file_ids?: Array<string>;

          /**
           * Set of 16 key-value pairs that can be attached to an object. This can be useful
           * for storing additional information about the object in a structured format, and
           * querying for objects via API or the dashboard.
           *
           * Keys are strings with a maximum length of 64 characters. Values are strings with
           * a maximum length of 512 characters.
           */
          metadata?: { [key: string]: string } | null;
        }

        export namespace VectorStore {
          /**
           * The default strategy. This strategy currently uses a `max_chunk_size_tokens` of
           * `800` and `chunk_overlap_tokens` of `400`.
           */
          export interface Auto {
            /**
             * Always `auto`.
             */
            type: 'auto';
          }

          export interface Static {
            static: Static.Static;

            /**
             * Always `static`.
             */
            type: 'static';
          }

          export namespace Static {
            export interface Static {
              /**
               * The number of tokens that overlap between chunks. The default value is `400`.
               *
               * Note that the overlap must not exceed half of `max_chunk_size_tokens`.
               */
              chunk_overlap_tokens: number;

              /**
               * The maximum number of tokens in each chunk. The default value is `800`. The
               * minimum value is `100` and the maximum value is `4096`.
               */
              max_chunk_size_tokens: number;
            }
          }
        }
      }
    }
  }

  /**
   * A set of resources that are used by the assistant's tools. The resources are
   * specific to the type of tool. For example, the `code_interpreter` tool requires
   * a list of file IDs, while the `file_search` tool requires a list of vector store
   * IDs.
   */
  export interface ToolResources {
    code_interpreter?: ToolResources.CodeInterpreter;

    file_search?: ToolResources.FileSearch;
  }

  export namespace ToolResources {
    export interface CodeInterpreter {
      /**
       * A list of [file](https://platform.excai.com/docs/api-reference/files) IDs made
       * available to the `code_interpreter` tool. There can be a maximum of 20 files
       * associated with the tool.
       */
      file_ids?: Array<string>;
    }

    export interface FileSearch {
      /**
       * The ID of the
       * [vector store](https://platform.excai.com/docs/api-reference/vector-stores/object)
       * attached to this assistant. There can be a maximum of 1 vector store attached to
       * the assistant.
       */
      vector_store_ids?: Array<string>;
    }
  }
}

export interface RunSubmitToolOutputsParams {
  /**
   * A list of tools for which the outputs are being submitted.
   */
  tool_outputs: Array<RunSubmitToolOutputsParams.ToolOutput>;

  /**
   * If `true`, returns a stream of events that happen during the Run as server-sent
   * events, terminating when the Run enters a terminal state with a `data: [DONE]`
   * message.
   */
  stream?: boolean | null;
}

export namespace RunSubmitToolOutputsParams {
  export interface ToolOutput {
    /**
     * The output of the tool call to be submitted to continue the run.
     */
    output?: string;

    /**
     * The ID of the tool call in the `required_action` object within the run object
     * the output is being submitted for.
     */
    tool_call_id?: string;
  }
}

Runs.Steps = Steps;

export declare namespace Runs {
  export {
    type AssistantsNamedToolChoice as AssistantsNamedToolChoice,
    type RunToolCallObject as RunToolCallObject,
    type TruncationObject as TruncationObject,
    type RunCreateResponse as RunCreateResponse,
    type RunRetrieveResponse as RunRetrieveResponse,
    type RunUpdateResponse as RunUpdateResponse,
    type RunListResponse as RunListResponse,
    type RunCancelResponse as RunCancelResponse,
    type RunCreateWithRunResponse as RunCreateWithRunResponse,
    type RunSubmitToolOutputsResponse as RunSubmitToolOutputsResponse,
    type RunCreateParams as RunCreateParams,
    type RunUpdateParams as RunUpdateParams,
    type RunListParams as RunListParams,
    type RunCreateWithRunParams as RunCreateWithRunParams,
    type RunSubmitToolOutputsParams as RunSubmitToolOutputsParams,
  };

  export {
    Steps as Steps,
    type StepRetrieveResponse as StepRetrieveResponse,
    type StepListResponse as StepListResponse,
    type StepRetrieveParams as StepRetrieveParams,
    type StepListParams as StepListParams,
  };
}
