// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import * as Shared from '../shared';
import * as AlphaAPI from './alpha/alpha';
import { Alpha } from './alpha/alpha';
import * as CheckpointsAPI from './checkpoints/checkpoints';
import { Checkpoints } from './checkpoints/checkpoints';
import * as JobsAPI from './jobs/jobs';
import {
  FineTuneDpoHyperparameters,
  FineTuneDpoMethod,
  FineTuneMethod,
  FineTuneReinforcementHyperparameters,
  FineTuneReinforcementMethod,
  FineTuneSupervisedHyperparameters,
  FineTuneSupervisedMethod,
  FineTuningIntegration,
  JobCancelResponse,
  JobCreateParams,
  JobCreateResponse,
  JobListParams,
  JobListResponse,
  JobPauseResponse,
  JobResumeResponse,
  JobRetrieveResponse,
  Jobs,
} from './jobs/jobs';

export class FineTuning extends APIResource {
  alpha: AlphaAPI.Alpha = new AlphaAPI.Alpha(this._client);
  checkpoints: CheckpointsAPI.Checkpoints = new CheckpointsAPI.Checkpoints(this._client);
  jobs: JobsAPI.Jobs = new JobsAPI.Jobs(this._client);
}

/**
 * A MultiGrader object combines the output of multiple graders to produce a single
 * score.
 */
export interface GraderMulti {
  /**
   * A formula to calculate the output based on grader results.
   */
  calculate_output: string;

  /**
   * A StringCheckGrader object that performs a string comparison between input and
   * reference using a specified operation.
   */
  graders:
    | Shared.GraderStringCheck
    | GraderTextSimilarity
    | GraderPython
    | GraderScoreModel
    | Shared.GraderLabelModel;

  /**
   * The name of the grader.
   */
  name: string;

  /**
   * The object type, which is always `multi`.
   */
  type: 'multi';
}

/**
 * A PythonGrader object that runs a python script on the input.
 */
export interface GraderPython {
  /**
   * The name of the grader.
   */
  name: string;

  /**
   * The source code of the python script.
   */
  source: string;

  /**
   * The object type, which is always `python`.
   */
  type: 'python';

  /**
   * The image tag to use for the python script.
   */
  image_tag?: string;
}

/**
 * A ScoreModelGrader object that uses a model to assign a score to the input.
 */
export interface GraderScoreModel {
  /**
   * The input text. This may include template strings.
   */
  input: Array<Shared.EvalItem>;

  /**
   * The model to use for the evaluation.
   */
  model: string;

  /**
   * The name of the grader.
   */
  name: string;

  /**
   * The object type, which is always `score_model`.
   */
  type: 'score_model';

  /**
   * The range of the score. Defaults to `[0, 1]`.
   */
  range?: Array<number>;

  /**
   * The sampling parameters for the model.
   */
  sampling_params?: GraderScoreModel.SamplingParams;
}

export namespace GraderScoreModel {
  /**
   * The sampling parameters for the model.
   */
  export interface SamplingParams {
    /**
     * The maximum number of tokens the grader model may generate in its response.
     */
    max_completions_tokens?: number | null;

    /**
     * Constrains effort on reasoning for
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
     * A seed value to initialize the randomness, during sampling.
     */
    seed?: number | null;

    /**
     * A higher temperature increases randomness in the outputs.
     */
    temperature?: number | null;

    /**
     * An alternative to temperature for nucleus sampling; 1.0 includes all tokens.
     */
    top_p?: number | null;
  }
}

/**
 * A TextSimilarityGrader object which grades text based on similarity metrics.
 */
export interface GraderTextSimilarity {
  /**
   * The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`, `gleu`,
   * `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`, or `rouge_l`.
   */
  evaluation_metric:
    | 'cosine'
    | 'fuzzy_match'
    | 'bleu'
    | 'gleu'
    | 'meteor'
    | 'rouge_1'
    | 'rouge_2'
    | 'rouge_3'
    | 'rouge_4'
    | 'rouge_5'
    | 'rouge_l';

  /**
   * The text being graded.
   */
  input: string;

  /**
   * The name of the grader.
   */
  name: string;

  /**
   * The text being graded against.
   */
  reference: string;

  /**
   * The type of grader.
   */
  type: 'text_similarity';
}

FineTuning.Alpha = Alpha;
FineTuning.Checkpoints = Checkpoints;
FineTuning.Jobs = Jobs;

export declare namespace FineTuning {
  export {
    type GraderMulti as GraderMulti,
    type GraderPython as GraderPython,
    type GraderScoreModel as GraderScoreModel,
    type GraderTextSimilarity as GraderTextSimilarity,
  };

  export { Alpha as Alpha };

  export { Checkpoints as Checkpoints };

  export {
    Jobs as Jobs,
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
}
