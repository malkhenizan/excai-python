// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../resource';
import { isRequestOptions } from '../../../core';
import * as Core from '../../../core';
import * as JobsAPI from './jobs';
import * as Shared from '../../shared';
import * as FineTuningAPI from '../fine-tuning';
import * as CheckpointsAPI from './checkpoints';
import { CheckpointListParams, CheckpointListResponse, Checkpoints } from './checkpoints';
import * as EventsAPI from './events';
import { EventListParams, EventListResponse, Events } from './events';

export class Jobs extends APIResource {
  checkpoints: CheckpointsAPI.Checkpoints = new CheckpointsAPI.Checkpoints(this._client);
  events: EventsAPI.Events = new EventsAPI.Events(this._client);

  /**
   * Creates a fine-tuning job which begins the process of creating a new model from
   * a given dataset.
   *
   * Response includes details of the enqueued job including job status and the name
   * of the fine-tuned models once complete.
   *
   * [Learn more about fine-tuning](https://platform.excai.com/docs/guides/model-optimization)
   *
   * @example
   * ```ts
   * const job = await client.fineTuning.jobs.create({
   *   model: 'gpt-4o-mini',
   *   training_file: 'file-abc123',
   * });
   * ```
   */
  create(body: JobCreateParams, options?: Core.RequestOptions): Core.APIPromise<JobCreateResponse> {
    return this._client.post('/fine_tuning/jobs', { body, ...options });
  }

  /**
   * Get info about a fine-tuning job.
   *
   * [Learn more about fine-tuning](https://platform.excai.com/docs/guides/model-optimization)
   *
   * @example
   * ```ts
   * const job = await client.fineTuning.jobs.retrieve(
   *   'ft-AF1WoRqd3aJAHsqc9NY7iL8F',
   * );
   * ```
   */
  retrieve(fineTuningJobId: string, options?: Core.RequestOptions): Core.APIPromise<JobRetrieveResponse> {
    return this._client.get(`/fine_tuning/jobs/${fineTuningJobId}`, options);
  }

  /**
   * List your organization's fine-tuning jobs
   *
   * @example
   * ```ts
   * const jobs = await client.fineTuning.jobs.list();
   * ```
   */
  list(query?: JobListParams, options?: Core.RequestOptions): Core.APIPromise<JobListResponse>;
  list(options?: Core.RequestOptions): Core.APIPromise<JobListResponse>;
  list(
    query: JobListParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<JobListResponse> {
    if (isRequestOptions(query)) {
      return this.list({}, query);
    }
    return this._client.get('/fine_tuning/jobs', { query, ...options });
  }

  /**
   * Immediately cancel a fine-tune job.
   *
   * @example
   * ```ts
   * const response = await client.fineTuning.jobs.cancel(
   *   'ft-AF1WoRqd3aJAHsqc9NY7iL8F',
   * );
   * ```
   */
  cancel(fineTuningJobId: string, options?: Core.RequestOptions): Core.APIPromise<JobCancelResponse> {
    return this._client.post(`/fine_tuning/jobs/${fineTuningJobId}/cancel`, options);
  }

  /**
   * Pause a fine-tune job.
   *
   * @example
   * ```ts
   * const response = await client.fineTuning.jobs.pause(
   *   'ft-AF1WoRqd3aJAHsqc9NY7iL8F',
   * );
   * ```
   */
  pause(fineTuningJobId: string, options?: Core.RequestOptions): Core.APIPromise<JobPauseResponse> {
    return this._client.post(`/fine_tuning/jobs/${fineTuningJobId}/pause`, options);
  }

  /**
   * Resume a fine-tune job.
   *
   * @example
   * ```ts
   * const response = await client.fineTuning.jobs.resume(
   *   'ft-AF1WoRqd3aJAHsqc9NY7iL8F',
   * );
   * ```
   */
  resume(fineTuningJobId: string, options?: Core.RequestOptions): Core.APIPromise<JobResumeResponse> {
    return this._client.post(`/fine_tuning/jobs/${fineTuningJobId}/resume`, options);
  }
}

/**
 * The hyperparameters used for the DPO fine-tuning job.
 */
export interface FineTuneDpoHyperparameters {
  /**
   * Number of examples in each batch. A larger batch size means that model
   * parameters are updated less frequently, but with lower variance.
   */
  batch_size?: 'auto' | number;

  /**
   * The beta value for the DPO method. A higher beta value will increase the weight
   * of the penalty between the policy and reference model.
   */
  beta?: 'auto' | number;

  /**
   * Scaling factor for the learning rate. A smaller learning rate may be useful to
   * avoid overfitting.
   */
  learning_rate_multiplier?: 'auto' | number;

  /**
   * The number of epochs to train the model for. An epoch refers to one full cycle
   * through the training dataset.
   */
  n_epochs?: 'auto' | number;
}

/**
 * Configuration for the DPO fine-tuning method.
 */
export interface FineTuneDpoMethod {
  /**
   * The hyperparameters used for the DPO fine-tuning job.
   */
  hyperparameters?: FineTuneDpoHyperparameters;
}

/**
 * The method used for fine-tuning.
 */
export interface FineTuneMethod {
  /**
   * The type of method. Is either `supervised`, `dpo`, or `reinforcement`.
   */
  type: 'supervised' | 'dpo' | 'reinforcement';

  /**
   * Configuration for the DPO fine-tuning method.
   */
  dpo?: FineTuneDpoMethod;

  /**
   * Configuration for the reinforcement fine-tuning method.
   */
  reinforcement?: FineTuneReinforcementMethod;

  /**
   * Configuration for the supervised fine-tuning method.
   */
  supervised?: FineTuneSupervisedMethod;
}

/**
 * The hyperparameters used for the reinforcement fine-tuning job.
 */
export interface FineTuneReinforcementHyperparameters {
  /**
   * Number of examples in each batch. A larger batch size means that model
   * parameters are updated less frequently, but with lower variance.
   */
  batch_size?: 'auto' | number;

  /**
   * Multiplier on amount of compute used for exploring search space during training.
   */
  compute_multiplier?: 'auto' | number;

  /**
   * The number of training steps between evaluation runs.
   */
  eval_interval?: 'auto' | number;

  /**
   * Number of evaluation samples to generate per training step.
   */
  eval_samples?: 'auto' | number;

  /**
   * Scaling factor for the learning rate. A smaller learning rate may be useful to
   * avoid overfitting.
   */
  learning_rate_multiplier?: 'auto' | number;

  /**
   * The number of epochs to train the model for. An epoch refers to one full cycle
   * through the training dataset.
   */
  n_epochs?: 'auto' | number;

  /**
   * Level of reasoning effort.
   */
  reasoning_effort?: 'default' | 'low' | 'medium' | 'high';
}

/**
 * Configuration for the reinforcement fine-tuning method.
 */
export interface FineTuneReinforcementMethod {
  /**
   * The grader used for the fine-tuning job.
   */
  grader:
    | Shared.GraderStringCheck
    | FineTuningAPI.GraderTextSimilarity
    | FineTuningAPI.GraderPython
    | FineTuningAPI.GraderScoreModel
    | FineTuningAPI.GraderMulti;

  /**
   * The hyperparameters used for the reinforcement fine-tuning job.
   */
  hyperparameters?: FineTuneReinforcementHyperparameters;
}

/**
 * The hyperparameters used for the fine-tuning job.
 */
export interface FineTuneSupervisedHyperparameters {
  /**
   * Number of examples in each batch. A larger batch size means that model
   * parameters are updated less frequently, but with lower variance.
   */
  batch_size?: 'auto' | number;

  /**
   * Scaling factor for the learning rate. A smaller learning rate may be useful to
   * avoid overfitting.
   */
  learning_rate_multiplier?: 'auto' | number;

  /**
   * The number of epochs to train the model for. An epoch refers to one full cycle
   * through the training dataset.
   */
  n_epochs?: 'auto' | number;
}

/**
 * Configuration for the supervised fine-tuning method.
 */
export interface FineTuneSupervisedMethod {
  /**
   * The hyperparameters used for the fine-tuning job.
   */
  hyperparameters?: FineTuneSupervisedHyperparameters;
}

export interface FineTuningIntegration {
  /**
   * The type of the integration being enabled for the fine-tuning job
   */
  type: 'wandb';

  /**
   * The settings for your integration with Weights and Biases. This payload
   * specifies the project that metrics will be sent to. Optionally, you can set an
   * explicit display name for your run, add tags to your run, and set a default
   * entity (team, username, etc) to be associated with your run.
   */
  wandb: FineTuningIntegration.Wandb;
}

export namespace FineTuningIntegration {
  /**
   * The settings for your integration with Weights and Biases. This payload
   * specifies the project that metrics will be sent to. Optionally, you can set an
   * explicit display name for your run, add tags to your run, and set a default
   * entity (team, username, etc) to be associated with your run.
   */
  export interface Wandb {
    /**
     * The name of the project that the new run will be created under.
     */
    project: string;

    /**
     * The entity to use for the run. This allows you to set the team or username of
     * the WandB user that you would like associated with the run. If not set, the
     * default entity for the registered WandB API key is used.
     */
    entity?: string | null;

    /**
     * A display name to set for the run. If not set, we will use the Job ID as the
     * name.
     */
    name?: string | null;

    /**
     * A list of tags to be attached to the newly created run. These tags are passed
     * through directly to WandB. Some default tags are generated by EXCai:
     * "excai/finetune", "excai/{base-model}", "excai/{ftjob-abcdef}".
     */
    tags?: Array<string>;
  }
}

/**
 * The `fine_tuning.job` object represents a fine-tuning job that has been created
 * through the API.
 */
export interface JobCreateResponse {
  /**
   * The object identifier, which can be referenced in the API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job was created.
   */
  created_at: number;

  /**
   * For fine-tuning jobs that have `failed`, this will contain more information on
   * the cause of the failure.
   */
  error: JobCreateResponse.Error | null;

  /**
   * The name of the fine-tuned model that is being created. The value will be null
   * if the fine-tuning job is still running.
   */
  fine_tuned_model: string | null;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job was finished. The
   * value will be null if the fine-tuning job is still running.
   */
  finished_at: number | null;

  /**
   * The hyperparameters used for the fine-tuning job. This value will only be
   * returned when running `supervised` jobs.
   */
  hyperparameters: JobCreateResponse.Hyperparameters;

  /**
   * The base model that is being fine-tuned.
   */
  model: string;

  /**
   * The object type, which is always "fine_tuning.job".
   */
  object: 'fine_tuning.job';

  /**
   * The organization that owns the fine-tuning job.
   */
  organization_id: string;

  /**
   * The compiled results file ID(s) for the fine-tuning job. You can retrieve the
   * results with the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  result_files: Array<string>;

  /**
   * The seed used for the fine-tuning job.
   */
  seed: number;

  /**
   * The current status of the fine-tuning job, which can be either
   * `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.
   */
  status: 'validating_files' | 'queued' | 'running' | 'succeeded' | 'failed' | 'cancelled';

  /**
   * The total number of billable tokens processed by this fine-tuning job. The value
   * will be null if the fine-tuning job is still running.
   */
  trained_tokens: number | null;

  /**
   * The file ID used for training. You can retrieve the training data with the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  training_file: string;

  /**
   * The file ID used for validation. You can retrieve the validation results with
   * the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  validation_file: string | null;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job is estimated to
   * finish. The value will be null if the fine-tuning job is not running.
   */
  estimated_finish?: number | null;

  /**
   * A list of integrations to enable for this fine-tuning job.
   */
  integrations?: Array<FineTuningIntegration> | null;

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
   * The method used for fine-tuning.
   */
  method?: FineTuneMethod;
}

export namespace JobCreateResponse {
  /**
   * For fine-tuning jobs that have `failed`, this will contain more information on
   * the cause of the failure.
   */
  export interface Error {
    /**
     * A machine-readable error code.
     */
    code: string;

    /**
     * A human-readable error message.
     */
    message: string;

    /**
     * The parameter that was invalid, usually `training_file` or `validation_file`.
     * This field will be null if the failure was not parameter-specific.
     */
    param: string | null;
  }

  /**
   * The hyperparameters used for the fine-tuning job. This value will only be
   * returned when running `supervised` jobs.
   */
  export interface Hyperparameters {
    /**
     * Number of examples in each batch. A larger batch size means that model
     * parameters are updated less frequently, but with lower variance.
     */
    batch_size?: 'auto' | number | null;

    /**
     * Scaling factor for the learning rate. A smaller learning rate may be useful to
     * avoid overfitting.
     */
    learning_rate_multiplier?: 'auto' | number;

    /**
     * The number of epochs to train the model for. An epoch refers to one full cycle
     * through the training dataset.
     */
    n_epochs?: 'auto' | number;
  }
}

/**
 * The `fine_tuning.job` object represents a fine-tuning job that has been created
 * through the API.
 */
export interface JobRetrieveResponse {
  /**
   * The object identifier, which can be referenced in the API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job was created.
   */
  created_at: number;

  /**
   * For fine-tuning jobs that have `failed`, this will contain more information on
   * the cause of the failure.
   */
  error: JobRetrieveResponse.Error | null;

  /**
   * The name of the fine-tuned model that is being created. The value will be null
   * if the fine-tuning job is still running.
   */
  fine_tuned_model: string | null;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job was finished. The
   * value will be null if the fine-tuning job is still running.
   */
  finished_at: number | null;

  /**
   * The hyperparameters used for the fine-tuning job. This value will only be
   * returned when running `supervised` jobs.
   */
  hyperparameters: JobRetrieveResponse.Hyperparameters;

  /**
   * The base model that is being fine-tuned.
   */
  model: string;

  /**
   * The object type, which is always "fine_tuning.job".
   */
  object: 'fine_tuning.job';

  /**
   * The organization that owns the fine-tuning job.
   */
  organization_id: string;

  /**
   * The compiled results file ID(s) for the fine-tuning job. You can retrieve the
   * results with the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  result_files: Array<string>;

  /**
   * The seed used for the fine-tuning job.
   */
  seed: number;

  /**
   * The current status of the fine-tuning job, which can be either
   * `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.
   */
  status: 'validating_files' | 'queued' | 'running' | 'succeeded' | 'failed' | 'cancelled';

  /**
   * The total number of billable tokens processed by this fine-tuning job. The value
   * will be null if the fine-tuning job is still running.
   */
  trained_tokens: number | null;

  /**
   * The file ID used for training. You can retrieve the training data with the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  training_file: string;

  /**
   * The file ID used for validation. You can retrieve the validation results with
   * the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  validation_file: string | null;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job is estimated to
   * finish. The value will be null if the fine-tuning job is not running.
   */
  estimated_finish?: number | null;

  /**
   * A list of integrations to enable for this fine-tuning job.
   */
  integrations?: Array<FineTuningIntegration> | null;

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
   * The method used for fine-tuning.
   */
  method?: FineTuneMethod;
}

export namespace JobRetrieveResponse {
  /**
   * For fine-tuning jobs that have `failed`, this will contain more information on
   * the cause of the failure.
   */
  export interface Error {
    /**
     * A machine-readable error code.
     */
    code: string;

    /**
     * A human-readable error message.
     */
    message: string;

    /**
     * The parameter that was invalid, usually `training_file` or `validation_file`.
     * This field will be null if the failure was not parameter-specific.
     */
    param: string | null;
  }

  /**
   * The hyperparameters used for the fine-tuning job. This value will only be
   * returned when running `supervised` jobs.
   */
  export interface Hyperparameters {
    /**
     * Number of examples in each batch. A larger batch size means that model
     * parameters are updated less frequently, but with lower variance.
     */
    batch_size?: 'auto' | number | null;

    /**
     * Scaling factor for the learning rate. A smaller learning rate may be useful to
     * avoid overfitting.
     */
    learning_rate_multiplier?: 'auto' | number;

    /**
     * The number of epochs to train the model for. An epoch refers to one full cycle
     * through the training dataset.
     */
    n_epochs?: 'auto' | number;
  }
}

export interface JobListResponse {
  data: Array<JobListResponse.Data>;

  has_more: boolean;

  object: 'list';
}

export namespace JobListResponse {
  /**
   * The `fine_tuning.job` object represents a fine-tuning job that has been created
   * through the API.
   */
  export interface Data {
    /**
     * The object identifier, which can be referenced in the API endpoints.
     */
    id: string;

    /**
     * The Unix timestamp (in seconds) for when the fine-tuning job was created.
     */
    created_at: number;

    /**
     * For fine-tuning jobs that have `failed`, this will contain more information on
     * the cause of the failure.
     */
    error: Data.Error | null;

    /**
     * The name of the fine-tuned model that is being created. The value will be null
     * if the fine-tuning job is still running.
     */
    fine_tuned_model: string | null;

    /**
     * The Unix timestamp (in seconds) for when the fine-tuning job was finished. The
     * value will be null if the fine-tuning job is still running.
     */
    finished_at: number | null;

    /**
     * The hyperparameters used for the fine-tuning job. This value will only be
     * returned when running `supervised` jobs.
     */
    hyperparameters: Data.Hyperparameters;

    /**
     * The base model that is being fine-tuned.
     */
    model: string;

    /**
     * The object type, which is always "fine_tuning.job".
     */
    object: 'fine_tuning.job';

    /**
     * The organization that owns the fine-tuning job.
     */
    organization_id: string;

    /**
     * The compiled results file ID(s) for the fine-tuning job. You can retrieve the
     * results with the
     * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
     */
    result_files: Array<string>;

    /**
     * The seed used for the fine-tuning job.
     */
    seed: number;

    /**
     * The current status of the fine-tuning job, which can be either
     * `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.
     */
    status: 'validating_files' | 'queued' | 'running' | 'succeeded' | 'failed' | 'cancelled';

    /**
     * The total number of billable tokens processed by this fine-tuning job. The value
     * will be null if the fine-tuning job is still running.
     */
    trained_tokens: number | null;

    /**
     * The file ID used for training. You can retrieve the training data with the
     * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
     */
    training_file: string;

    /**
     * The file ID used for validation. You can retrieve the validation results with
     * the
     * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
     */
    validation_file: string | null;

    /**
     * The Unix timestamp (in seconds) for when the fine-tuning job is estimated to
     * finish. The value will be null if the fine-tuning job is not running.
     */
    estimated_finish?: number | null;

    /**
     * A list of integrations to enable for this fine-tuning job.
     */
    integrations?: Array<JobsAPI.FineTuningIntegration> | null;

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
     * The method used for fine-tuning.
     */
    method?: JobsAPI.FineTuneMethod;
  }

  export namespace Data {
    /**
     * For fine-tuning jobs that have `failed`, this will contain more information on
     * the cause of the failure.
     */
    export interface Error {
      /**
       * A machine-readable error code.
       */
      code: string;

      /**
       * A human-readable error message.
       */
      message: string;

      /**
       * The parameter that was invalid, usually `training_file` or `validation_file`.
       * This field will be null if the failure was not parameter-specific.
       */
      param: string | null;
    }

    /**
     * The hyperparameters used for the fine-tuning job. This value will only be
     * returned when running `supervised` jobs.
     */
    export interface Hyperparameters {
      /**
       * Number of examples in each batch. A larger batch size means that model
       * parameters are updated less frequently, but with lower variance.
       */
      batch_size?: 'auto' | number | null;

      /**
       * Scaling factor for the learning rate. A smaller learning rate may be useful to
       * avoid overfitting.
       */
      learning_rate_multiplier?: 'auto' | number;

      /**
       * The number of epochs to train the model for. An epoch refers to one full cycle
       * through the training dataset.
       */
      n_epochs?: 'auto' | number;
    }
  }
}

/**
 * The `fine_tuning.job` object represents a fine-tuning job that has been created
 * through the API.
 */
export interface JobCancelResponse {
  /**
   * The object identifier, which can be referenced in the API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job was created.
   */
  created_at: number;

  /**
   * For fine-tuning jobs that have `failed`, this will contain more information on
   * the cause of the failure.
   */
  error: JobCancelResponse.Error | null;

  /**
   * The name of the fine-tuned model that is being created. The value will be null
   * if the fine-tuning job is still running.
   */
  fine_tuned_model: string | null;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job was finished. The
   * value will be null if the fine-tuning job is still running.
   */
  finished_at: number | null;

  /**
   * The hyperparameters used for the fine-tuning job. This value will only be
   * returned when running `supervised` jobs.
   */
  hyperparameters: JobCancelResponse.Hyperparameters;

  /**
   * The base model that is being fine-tuned.
   */
  model: string;

  /**
   * The object type, which is always "fine_tuning.job".
   */
  object: 'fine_tuning.job';

  /**
   * The organization that owns the fine-tuning job.
   */
  organization_id: string;

  /**
   * The compiled results file ID(s) for the fine-tuning job. You can retrieve the
   * results with the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  result_files: Array<string>;

  /**
   * The seed used for the fine-tuning job.
   */
  seed: number;

  /**
   * The current status of the fine-tuning job, which can be either
   * `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.
   */
  status: 'validating_files' | 'queued' | 'running' | 'succeeded' | 'failed' | 'cancelled';

  /**
   * The total number of billable tokens processed by this fine-tuning job. The value
   * will be null if the fine-tuning job is still running.
   */
  trained_tokens: number | null;

  /**
   * The file ID used for training. You can retrieve the training data with the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  training_file: string;

  /**
   * The file ID used for validation. You can retrieve the validation results with
   * the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  validation_file: string | null;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job is estimated to
   * finish. The value will be null if the fine-tuning job is not running.
   */
  estimated_finish?: number | null;

  /**
   * A list of integrations to enable for this fine-tuning job.
   */
  integrations?: Array<FineTuningIntegration> | null;

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
   * The method used for fine-tuning.
   */
  method?: FineTuneMethod;
}

export namespace JobCancelResponse {
  /**
   * For fine-tuning jobs that have `failed`, this will contain more information on
   * the cause of the failure.
   */
  export interface Error {
    /**
     * A machine-readable error code.
     */
    code: string;

    /**
     * A human-readable error message.
     */
    message: string;

    /**
     * The parameter that was invalid, usually `training_file` or `validation_file`.
     * This field will be null if the failure was not parameter-specific.
     */
    param: string | null;
  }

  /**
   * The hyperparameters used for the fine-tuning job. This value will only be
   * returned when running `supervised` jobs.
   */
  export interface Hyperparameters {
    /**
     * Number of examples in each batch. A larger batch size means that model
     * parameters are updated less frequently, but with lower variance.
     */
    batch_size?: 'auto' | number | null;

    /**
     * Scaling factor for the learning rate. A smaller learning rate may be useful to
     * avoid overfitting.
     */
    learning_rate_multiplier?: 'auto' | number;

    /**
     * The number of epochs to train the model for. An epoch refers to one full cycle
     * through the training dataset.
     */
    n_epochs?: 'auto' | number;
  }
}

/**
 * The `fine_tuning.job` object represents a fine-tuning job that has been created
 * through the API.
 */
export interface JobPauseResponse {
  /**
   * The object identifier, which can be referenced in the API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job was created.
   */
  created_at: number;

  /**
   * For fine-tuning jobs that have `failed`, this will contain more information on
   * the cause of the failure.
   */
  error: JobPauseResponse.Error | null;

  /**
   * The name of the fine-tuned model that is being created. The value will be null
   * if the fine-tuning job is still running.
   */
  fine_tuned_model: string | null;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job was finished. The
   * value will be null if the fine-tuning job is still running.
   */
  finished_at: number | null;

  /**
   * The hyperparameters used for the fine-tuning job. This value will only be
   * returned when running `supervised` jobs.
   */
  hyperparameters: JobPauseResponse.Hyperparameters;

  /**
   * The base model that is being fine-tuned.
   */
  model: string;

  /**
   * The object type, which is always "fine_tuning.job".
   */
  object: 'fine_tuning.job';

  /**
   * The organization that owns the fine-tuning job.
   */
  organization_id: string;

  /**
   * The compiled results file ID(s) for the fine-tuning job. You can retrieve the
   * results with the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  result_files: Array<string>;

  /**
   * The seed used for the fine-tuning job.
   */
  seed: number;

  /**
   * The current status of the fine-tuning job, which can be either
   * `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.
   */
  status: 'validating_files' | 'queued' | 'running' | 'succeeded' | 'failed' | 'cancelled';

  /**
   * The total number of billable tokens processed by this fine-tuning job. The value
   * will be null if the fine-tuning job is still running.
   */
  trained_tokens: number | null;

  /**
   * The file ID used for training. You can retrieve the training data with the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  training_file: string;

  /**
   * The file ID used for validation. You can retrieve the validation results with
   * the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  validation_file: string | null;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job is estimated to
   * finish. The value will be null if the fine-tuning job is not running.
   */
  estimated_finish?: number | null;

  /**
   * A list of integrations to enable for this fine-tuning job.
   */
  integrations?: Array<FineTuningIntegration> | null;

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
   * The method used for fine-tuning.
   */
  method?: FineTuneMethod;
}

export namespace JobPauseResponse {
  /**
   * For fine-tuning jobs that have `failed`, this will contain more information on
   * the cause of the failure.
   */
  export interface Error {
    /**
     * A machine-readable error code.
     */
    code: string;

    /**
     * A human-readable error message.
     */
    message: string;

    /**
     * The parameter that was invalid, usually `training_file` or `validation_file`.
     * This field will be null if the failure was not parameter-specific.
     */
    param: string | null;
  }

  /**
   * The hyperparameters used for the fine-tuning job. This value will only be
   * returned when running `supervised` jobs.
   */
  export interface Hyperparameters {
    /**
     * Number of examples in each batch. A larger batch size means that model
     * parameters are updated less frequently, but with lower variance.
     */
    batch_size?: 'auto' | number | null;

    /**
     * Scaling factor for the learning rate. A smaller learning rate may be useful to
     * avoid overfitting.
     */
    learning_rate_multiplier?: 'auto' | number;

    /**
     * The number of epochs to train the model for. An epoch refers to one full cycle
     * through the training dataset.
     */
    n_epochs?: 'auto' | number;
  }
}

/**
 * The `fine_tuning.job` object represents a fine-tuning job that has been created
 * through the API.
 */
export interface JobResumeResponse {
  /**
   * The object identifier, which can be referenced in the API endpoints.
   */
  id: string;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job was created.
   */
  created_at: number;

  /**
   * For fine-tuning jobs that have `failed`, this will contain more information on
   * the cause of the failure.
   */
  error: JobResumeResponse.Error | null;

  /**
   * The name of the fine-tuned model that is being created. The value will be null
   * if the fine-tuning job is still running.
   */
  fine_tuned_model: string | null;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job was finished. The
   * value will be null if the fine-tuning job is still running.
   */
  finished_at: number | null;

  /**
   * The hyperparameters used for the fine-tuning job. This value will only be
   * returned when running `supervised` jobs.
   */
  hyperparameters: JobResumeResponse.Hyperparameters;

  /**
   * The base model that is being fine-tuned.
   */
  model: string;

  /**
   * The object type, which is always "fine_tuning.job".
   */
  object: 'fine_tuning.job';

  /**
   * The organization that owns the fine-tuning job.
   */
  organization_id: string;

  /**
   * The compiled results file ID(s) for the fine-tuning job. You can retrieve the
   * results with the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  result_files: Array<string>;

  /**
   * The seed used for the fine-tuning job.
   */
  seed: number;

  /**
   * The current status of the fine-tuning job, which can be either
   * `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.
   */
  status: 'validating_files' | 'queued' | 'running' | 'succeeded' | 'failed' | 'cancelled';

  /**
   * The total number of billable tokens processed by this fine-tuning job. The value
   * will be null if the fine-tuning job is still running.
   */
  trained_tokens: number | null;

  /**
   * The file ID used for training. You can retrieve the training data with the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  training_file: string;

  /**
   * The file ID used for validation. You can retrieve the validation results with
   * the
   * [Files API](https://platform.excai.com/docs/api-reference/files/retrieve-contents).
   */
  validation_file: string | null;

  /**
   * The Unix timestamp (in seconds) for when the fine-tuning job is estimated to
   * finish. The value will be null if the fine-tuning job is not running.
   */
  estimated_finish?: number | null;

  /**
   * A list of integrations to enable for this fine-tuning job.
   */
  integrations?: Array<FineTuningIntegration> | null;

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
   * The method used for fine-tuning.
   */
  method?: FineTuneMethod;
}

export namespace JobResumeResponse {
  /**
   * For fine-tuning jobs that have `failed`, this will contain more information on
   * the cause of the failure.
   */
  export interface Error {
    /**
     * A machine-readable error code.
     */
    code: string;

    /**
     * A human-readable error message.
     */
    message: string;

    /**
     * The parameter that was invalid, usually `training_file` or `validation_file`.
     * This field will be null if the failure was not parameter-specific.
     */
    param: string | null;
  }

  /**
   * The hyperparameters used for the fine-tuning job. This value will only be
   * returned when running `supervised` jobs.
   */
  export interface Hyperparameters {
    /**
     * Number of examples in each batch. A larger batch size means that model
     * parameters are updated less frequently, but with lower variance.
     */
    batch_size?: 'auto' | number | null;

    /**
     * Scaling factor for the learning rate. A smaller learning rate may be useful to
     * avoid overfitting.
     */
    learning_rate_multiplier?: 'auto' | number;

    /**
     * The number of epochs to train the model for. An epoch refers to one full cycle
     * through the training dataset.
     */
    n_epochs?: 'auto' | number;
  }
}

export interface JobCreateParams {
  /**
   * The name of the model to fine-tune. You can select one of the
   * [supported models](https://platform.excai.com/docs/guides/fine-tuning#which-models-can-be-fine-tuned).
   */
  model: (string & {}) | 'babbage-002' | 'davinci-002' | 'gpt-3.5-turbo' | 'gpt-4o-mini';

  /**
   * The ID of an uploaded file that contains training data.
   *
   * See [upload file](https://platform.excai.com/docs/api-reference/files/create)
   * for how to upload a file.
   *
   * Your dataset must be formatted as a JSONL file. Additionally, you must upload
   * your file with the purpose `fine-tune`.
   *
   * The contents of the file should differ depending on if the model uses the
   * [chat](https://platform.excai.com/docs/api-reference/fine-tuning/chat-input),
   * [completions](https://platform.excai.com/docs/api-reference/fine-tuning/completions-input)
   * format, or if the fine-tuning method uses the
   * [preference](https://platform.excai.com/docs/api-reference/fine-tuning/preference-input)
   * format.
   *
   * See the
   * [fine-tuning guide](https://platform.excai.com/docs/guides/model-optimization)
   * for more details.
   */
  training_file: string;

  /**
   * @deprecated The hyperparameters used for the fine-tuning job. This value is now
   * deprecated in favor of `method`, and should be passed in under the `method`
   * parameter.
   */
  hyperparameters?: JobCreateParams.Hyperparameters;

  /**
   * A list of integrations to enable for your fine-tuning job.
   */
  integrations?: Array<JobCreateParams.Integration> | null;

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
   * The method used for fine-tuning.
   */
  method?: FineTuneMethod;

  /**
   * The seed controls the reproducibility of the job. Passing in the same seed and
   * job parameters should produce the same results, but may differ in rare cases. If
   * a seed is not specified, one will be generated for you.
   */
  seed?: number | null;

  /**
   * A string of up to 64 characters that will be added to your fine-tuned model
   * name.
   *
   * For example, a `suffix` of "custom-model-name" would produce a model name like
   * `ft:gpt-4o-mini:excai:custom-model-name:7p4lURel`.
   */
  suffix?: string | null;

  /**
   * The ID of an uploaded file that contains validation data.
   *
   * If you provide this file, the data is used to generate validation metrics
   * periodically during fine-tuning. These metrics can be viewed in the fine-tuning
   * results file. The same data should not be present in both train and validation
   * files.
   *
   * Your dataset must be formatted as a JSONL file. You must upload your file with
   * the purpose `fine-tune`.
   *
   * See the
   * [fine-tuning guide](https://platform.excai.com/docs/guides/model-optimization)
   * for more details.
   */
  validation_file?: string | null;
}

export namespace JobCreateParams {
  /**
   * @deprecated The hyperparameters used for the fine-tuning job. This value is now
   * deprecated in favor of `method`, and should be passed in under the `method`
   * parameter.
   */
  export interface Hyperparameters {
    /**
     * Number of examples in each batch. A larger batch size means that model
     * parameters are updated less frequently, but with lower variance.
     */
    batch_size?: 'auto' | number;

    /**
     * Scaling factor for the learning rate. A smaller learning rate may be useful to
     * avoid overfitting.
     */
    learning_rate_multiplier?: 'auto' | number;

    /**
     * The number of epochs to train the model for. An epoch refers to one full cycle
     * through the training dataset.
     */
    n_epochs?: 'auto' | number;
  }

  export interface Integration {
    /**
     * The type of integration to enable. Currently, only "wandb" (Weights and Biases)
     * is supported.
     */
    type: 'wandb';

    /**
     * The settings for your integration with Weights and Biases. This payload
     * specifies the project that metrics will be sent to. Optionally, you can set an
     * explicit display name for your run, add tags to your run, and set a default
     * entity (team, username, etc) to be associated with your run.
     */
    wandb: Integration.Wandb;
  }

  export namespace Integration {
    /**
     * The settings for your integration with Weights and Biases. This payload
     * specifies the project that metrics will be sent to. Optionally, you can set an
     * explicit display name for your run, add tags to your run, and set a default
     * entity (team, username, etc) to be associated with your run.
     */
    export interface Wandb {
      /**
       * The name of the project that the new run will be created under.
       */
      project: string;

      /**
       * The entity to use for the run. This allows you to set the team or username of
       * the WandB user that you would like associated with the run. If not set, the
       * default entity for the registered WandB API key is used.
       */
      entity?: string | null;

      /**
       * A display name to set for the run. If not set, we will use the Job ID as the
       * name.
       */
      name?: string | null;

      /**
       * A list of tags to be attached to the newly created run. These tags are passed
       * through directly to WandB. Some default tags are generated by EXCai:
       * "excai/finetune", "excai/{base-model}", "excai/{ftjob-abcdef}".
       */
      tags?: Array<string>;
    }
  }
}

export interface JobListParams {
  /**
   * Identifier for the last job from the previous pagination request.
   */
  after?: string;

  /**
   * Number of fine-tuning jobs to retrieve.
   */
  limit?: number;

  /**
   * Optional metadata filter. To filter, use the syntax `metadata[k]=v`.
   * Alternatively, set `metadata=null` to indicate no metadata.
   */
  metadata?: { [key: string]: string } | null;
}

Jobs.Checkpoints = Checkpoints;
Jobs.Events = Events;

export declare namespace Jobs {
  export {
    type FineTuneDpoHyperparameters as FineTuneDpoHyperparameters,
    type FineTuneDpoMethod as FineTuneDpoMethod,
    type FineTuneMethod as FineTuneMethod,
    type FineTuneReinforcementHyperparameters as FineTuneReinforcementHyperparameters,
    type FineTuneReinforcementMethod as FineTuneReinforcementMethod,
    type FineTuneSupervisedHyperparameters as FineTuneSupervisedHyperparameters,
    type FineTuneSupervisedMethod as FineTuneSupervisedMethod,
    type FineTuningIntegration as FineTuningIntegration,
    type JobCreateResponse as JobCreateResponse,
    type JobRetrieveResponse as JobRetrieveResponse,
    type JobListResponse as JobListResponse,
    type JobCancelResponse as JobCancelResponse,
    type JobPauseResponse as JobPauseResponse,
    type JobResumeResponse as JobResumeResponse,
    type JobCreateParams as JobCreateParams,
    type JobListParams as JobListParams,
  };

  export {
    Checkpoints as Checkpoints,
    type CheckpointListResponse as CheckpointListResponse,
    type CheckpointListParams as CheckpointListParams,
  };

  export {
    Events as Events,
    type EventListResponse as EventListResponse,
    type EventListParams as EventListParams,
  };
}
