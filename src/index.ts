// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { type Agent } from './_shims/index';
import * as qs from './internal/qs';
import * as Core from './core';
import * as Errors from './error';
import * as Uploads from './uploads';
import * as API from './resources/index';
import {
  AssistantCreateParams,
  AssistantCreateResponse,
  AssistantDeleteResponse,
  AssistantListParams,
  AssistantListResponse,
  AssistantRetrieveResponse,
  AssistantUpdateParams,
  AssistantUpdateResponse,
  Assistants,
} from './resources/assistants';
import {
  Audio,
  AudioCreateSpeechParams,
  AudioCreateTranscriptionParams,
  AudioCreateTranscriptionResponse,
  AudioCreateTranslationParams,
  AudioCreateTranslationResponse,
} from './resources/audio';
import {
  BatchCancelResponse,
  BatchCreateParams,
  BatchCreateResponse,
  BatchError,
  BatchListParams,
  BatchListResponse,
  BatchRequestCounts,
  BatchRetrieveResponse,
  Batches,
} from './resources/batches';
import { CompletionCreateParams, CompletionCreateResponse, Completions } from './resources/completions';
import { EmbeddingCreateParams, EmbeddingCreateResponse, Embeddings } from './resources/embeddings';
import {
  FileDeleteResponse,
  FileListParams,
  FileListResponse,
  FileRetrieveContentResponse,
  FileUploadParams,
  Files,
} from './resources/files';
import {
  Image,
  ImageCreateEditParams,
  ImageCreateEditResponse,
  ImageCreateImageParams,
  ImageCreateImageResponse,
  ImageCreateVariationParams,
  ImageCreateVariationResponse,
  ImageGenInputUsageDetails,
  ImageGenUsage,
  Images,
} from './resources/images';
import { ModelDeleteResponse, ModelListResponse, ModelRetrieveResponse, Models } from './resources/models';
import { ModerationCreateParams, ModerationCreateResponse, Moderations } from './resources/moderations';
import {
  Conversation2,
  FunctionToolCall,
  OutputMessage,
  Reasoning,
  ResponseCancelResponse,
  ResponseCreateParams,
  ResponseCreateResponse,
  ResponseListInputItemsParams,
  ResponseListInputItemsResponse,
  ResponseRetrieveParams,
  ResponseRetrieveResponse,
  ResponseUsage,
  Responses,
  ToolChoiceAllowed,
  ToolChoiceCustom,
  ToolChoiceTypes,
} from './resources/responses';
import {
  UploadAddPartParams,
  UploadAddPartResponse,
  UploadCancelResponse,
  UploadCompleteParams,
  UploadCompleteResponse,
  UploadCreateParams,
  UploadCreateResponse,
  Uploads as UploadsAPIUploads,
} from './resources/uploads';
import {
  Error2,
  VideoCreateParams,
  VideoCreateResponse,
  VideoDeleteResponse,
  VideoListParams,
  VideoListResponse,
  VideoRemixParams,
  VideoRemixResponse,
  VideoRetrieveContentParams,
  VideoRetrieveContentResponse,
  VideoRetrieveResponse,
  Videos,
} from './resources/videos';
import { Chat } from './resources/chat/chat';
import { Chatkit, ChatkitUploadFileParams, ChatkitUploadFileResponse } from './resources/chatkit/chatkit';
import {
  ContainerCreateParams,
  ContainerCreateResponse,
  ContainerListParams,
  ContainerListResponse,
  ContainerRetrieveResponse,
  Containers,
} from './resources/containers/containers';
import {
  ConversationCreateParams,
  ConversationCreateResponse,
  ConversationDeleteResponse,
  ConversationRetrieveResponse,
  ConversationUpdateParams,
  ConversationUpdateResponse,
  Conversations,
} from './resources/conversations/conversations';
import {
  EvalCreateParams,
  EvalCreateResponse,
  EvalCustomDataSourceConfig,
  EvalDeleteResponse,
  EvalGraderPython,
  EvalGraderScoreModel,
  EvalGraderTextSimilarity,
  EvalListParams,
  EvalListResponse,
  EvalLogsDataSourceConfig,
  EvalRetrieveResponse,
  EvalStoredCompletionsDataSourceConfig,
  EvalUpdateParams,
  EvalUpdateResponse,
  Evals,
} from './resources/evals/evals';
import {
  FineTuning,
  GraderMulti,
  GraderPython,
  GraderScoreModel,
  GraderTextSimilarity,
} from './resources/fine-tuning/fine-tuning';
import {
  Certificate,
  CostsResult,
  Organization,
  OrganizationGetCostsParams,
  OrganizationGetCostsResponse,
  OrganizationListAuditLogsParams,
  OrganizationListAuditLogsResponse,
  UsageAudioSpeechesResult,
  UsageAudioTranscriptionsResult,
  UsageCodeInterpreterSessionsResult,
  UsageCompletionsResult,
  UsageEmbeddingsResult,
  UsageImagesResult,
  UsageModerationsResult,
  UsageTimeBucket,
  UsageVectorStoresResult,
} from './resources/organization/organization';
import {
  AudioTranscription,
  Realtime,
  RealtimeCreateClientSecretParams,
  RealtimeCreateClientSecretResponse,
  RealtimeCreateSessionParams,
  RealtimeCreateSessionResponse,
  RealtimeCreateTranscriptionSessionParams,
  RealtimeCreateTranscriptionSessionResponse,
  RealtimeFunctionTool,
} from './resources/realtime/realtime';
import {
  AssistantToolsFileSearchTypeOnly,
  ThreadCreateParams,
  ThreadCreateResponse,
  ThreadDeleteResponse,
  ThreadRetrieveResponse,
  ThreadUpdateParams,
  ThreadUpdateResponse,
  Threads,
} from './resources/threads/threads';
import {
  AutoChunkingStrategyRequestParam,
  OtherChunkingStrategyResponseParam,
  StaticChunkingStrategy,
  StaticChunkingStrategyRequestParam,
  StaticChunkingStrategyResponseParam,
  VectorStoreCreateParams,
  VectorStoreCreateResponse,
  VectorStoreDeleteResponse,
  VectorStoreExpirationAfter,
  VectorStoreListParams,
  VectorStoreListResponse,
  VectorStoreRetrieveResponse,
  VectorStoreSearchParams,
  VectorStoreSearchResponse,
  VectorStoreUpdateParams,
  VectorStoreUpdateResponse,
  VectorStores,
} from './resources/vector-stores/vector-stores';

export interface ClientOptions {
  /**
   * Defaults to process.env['EXCAI_API_KEY'].
   */
  apiKey?: string | null | undefined;

  /**
   * Override the default base URL for the API, e.g., "https://api.example.com/v2/"
   *
   * Defaults to process.env['EX_CAI_BASE_URL'].
   */
  baseURL?: string | null | undefined;

  /**
   * The maximum amount of time (in milliseconds) that the client should wait for a response
   * from the server before timing out a single request.
   *
   * Note that request timeouts are retried by default, so in a worst-case scenario you may wait
   * much longer than this timeout before the promise succeeds or fails.
   *
   * @unit milliseconds
   */
  timeout?: number | undefined;

  /**
   * An HTTP agent used to manage HTTP(S) connections.
   *
   * If not provided, an agent will be constructed by default in the Node.js environment,
   * otherwise no agent is used.
   */
  httpAgent?: Agent | undefined;

  /**
   * Specify a custom `fetch` function implementation.
   *
   * If not provided, we use `node-fetch` on Node.js and otherwise expect that `fetch` is
   * defined globally.
   */
  fetch?: Core.Fetch | undefined;

  /**
   * The maximum number of times that the client will retry a request in case of a
   * temporary failure, like a network error or a 5XX error from the server.
   *
   * @default 2
   */
  maxRetries?: number | undefined;

  /**
   * Default headers to include with every request to the API.
   *
   * These can be removed in individual requests by explicitly setting the
   * header to `undefined` or `null` in request options.
   */
  defaultHeaders?: Core.Headers | undefined;

  /**
   * Default query parameters to include with every request to the API.
   *
   * These can be removed in individual requests by explicitly setting the
   * param to `undefined` in request options.
   */
  defaultQuery?: Core.DefaultQuery | undefined;
}

/**
 * API Client for interfacing with the Ex Cai API.
 */
export class ExCai extends Core.APIClient {
  apiKey: string | null;

  private _options: ClientOptions;

  /**
   * API Client for interfacing with the Ex Cai API.
   *
   * @param {string | null | undefined} [opts.apiKey=process.env['EXCAI_API_KEY'] ?? null]
   * @param {string} [opts.baseURL=process.env['EX_CAI_BASE_URL'] ?? https://api-main.excai.ai/api/v1/] - Override the default base URL for the API.
   * @param {number} [opts.timeout=1 minute] - The maximum amount of time (in milliseconds) the client will wait for a response before timing out.
   * @param {number} [opts.httpAgent] - An HTTP agent used to manage HTTP(s) connections.
   * @param {Core.Fetch} [opts.fetch] - Specify a custom `fetch` function implementation.
   * @param {number} [opts.maxRetries=2] - The maximum number of times the client will retry a request.
   * @param {Core.Headers} opts.defaultHeaders - Default headers to include with every request to the API.
   * @param {Core.DefaultQuery} opts.defaultQuery - Default query parameters to include with every request to the API.
   */
  constructor({
    baseURL = Core.readEnv('EX_CAI_BASE_URL'),
    apiKey = Core.readEnv('EXCAI_API_KEY') ?? null,
    ...opts
  }: ClientOptions = {}) {
    const options: ClientOptions = {
      apiKey,
      ...opts,
      baseURL: baseURL || `https://api-main.excai.ai/api/v1/`,
    };

    super({
      baseURL: options.baseURL!,
      baseURLOverridden: baseURL ? baseURL !== 'https://api-main.excai.ai/api/v1/' : false,
      timeout: options.timeout ?? 60000 /* 1 minute */,
      httpAgent: options.httpAgent,
      maxRetries: options.maxRetries,
      fetch: options.fetch,
    });

    this._options = options;

    this.apiKey = apiKey;
  }

  assistants: API.Assistants = new API.Assistants(this);
  audio: API.Audio = new API.Audio(this);
  batches: API.Batches = new API.Batches(this);
  chat: API.Chat = new API.Chat(this);
  completions: API.Completions = new API.Completions(this);
  containers: API.Containers = new API.Containers(this);
  conversations: API.Conversations = new API.Conversations(this);
  embeddings: API.Embeddings = new API.Embeddings(this);
  evals: API.Evals = new API.Evals(this);
  files: API.Files = new API.Files(this);
  fineTuning: API.FineTuning = new API.FineTuning(this);
  images: API.Images = new API.Images(this);
  models: API.Models = new API.Models(this);
  moderations: API.Moderations = new API.Moderations(this);
  organization: API.Organization = new API.Organization(this);
  realtime: API.Realtime = new API.Realtime(this);
  responses: API.Responses = new API.Responses(this);
  threads: API.Threads = new API.Threads(this);
  uploads: API.Uploads = new API.Uploads(this);
  vectorStores: API.VectorStores = new API.VectorStores(this);
  videos: API.Videos = new API.Videos(this);
  chatkit: API.Chatkit = new API.Chatkit(this);

  /**
   * Check whether the base URL is set to its default.
   */
  #baseURLOverridden(): boolean {
    return this.baseURL !== 'https://api-main.excai.ai/api/v1/';
  }

  protected override defaultQuery(): Core.DefaultQuery | undefined {
    return this._options.defaultQuery;
  }

  protected override defaultHeaders(opts: Core.FinalRequestOptions): Core.Headers {
    return {
      ...super.defaultHeaders(opts),
      ...this._options.defaultHeaders,
    };
  }

  protected override validateHeaders(headers: Core.Headers, customHeaders: Core.Headers) {
    if (this.apiKey && headers['authorization']) {
      return;
    }
    if (customHeaders['authorization'] === null) {
      return;
    }

    throw new Error(
      'Could not resolve authentication method. Expected the apiKey to be set. Or for the "Authorization" headers to be explicitly omitted',
    );
  }

  protected override authHeaders(opts: Core.FinalRequestOptions): Core.Headers {
    if (this.apiKey == null) {
      return {};
    }
    return { Authorization: `Bearer ${this.apiKey}` };
  }

  protected override stringifyQuery(query: Record<string, unknown>): string {
    return qs.stringify(query, { arrayFormat: 'brackets' });
  }

  static ExCai = this;
  static DEFAULT_TIMEOUT = 60000; // 1 minute

  static ExCaiError = Errors.ExCaiError;
  static APIError = Errors.APIError;
  static APIConnectionError = Errors.APIConnectionError;
  static APIConnectionTimeoutError = Errors.APIConnectionTimeoutError;
  static APIUserAbortError = Errors.APIUserAbortError;
  static NotFoundError = Errors.NotFoundError;
  static ConflictError = Errors.ConflictError;
  static RateLimitError = Errors.RateLimitError;
  static BadRequestError = Errors.BadRequestError;
  static AuthenticationError = Errors.AuthenticationError;
  static InternalServerError = Errors.InternalServerError;
  static PermissionDeniedError = Errors.PermissionDeniedError;
  static UnprocessableEntityError = Errors.UnprocessableEntityError;

  static toFile = Uploads.toFile;
  static fileFromPath = Uploads.fileFromPath;
}

ExCai.Assistants = Assistants;
ExCai.Audio = Audio;
ExCai.Batches = Batches;
ExCai.Chat = Chat;
ExCai.Completions = Completions;
ExCai.Containers = Containers;
ExCai.Conversations = Conversations;
ExCai.Embeddings = Embeddings;
ExCai.Evals = Evals;
ExCai.Files = Files;
ExCai.FineTuning = FineTuning;
ExCai.Images = Images;
ExCai.Models = Models;
ExCai.Moderations = Moderations;
ExCai.Organization = Organization;
ExCai.Realtime = Realtime;
ExCai.Responses = Responses;
ExCai.Threads = Threads;
ExCai.Uploads = UploadsAPIUploads;
ExCai.VectorStores = VectorStores;
ExCai.Videos = Videos;
ExCai.Chatkit = Chatkit;

export declare namespace ExCai {
  export type RequestOptions = Core.RequestOptions;

  export {
    Assistants as Assistants,
    type AssistantCreateResponse as AssistantCreateResponse,
    type AssistantRetrieveResponse as AssistantRetrieveResponse,
    type AssistantUpdateResponse as AssistantUpdateResponse,
    type AssistantListResponse as AssistantListResponse,
    type AssistantDeleteResponse as AssistantDeleteResponse,
    type AssistantCreateParams as AssistantCreateParams,
    type AssistantUpdateParams as AssistantUpdateParams,
    type AssistantListParams as AssistantListParams,
  };

  export {
    Audio as Audio,
    type AudioCreateTranscriptionResponse as AudioCreateTranscriptionResponse,
    type AudioCreateTranslationResponse as AudioCreateTranslationResponse,
    type AudioCreateSpeechParams as AudioCreateSpeechParams,
    type AudioCreateTranscriptionParams as AudioCreateTranscriptionParams,
    type AudioCreateTranslationParams as AudioCreateTranslationParams,
  };

  export {
    Batches as Batches,
    type BatchError as BatchError,
    type BatchRequestCounts as BatchRequestCounts,
    type BatchCreateResponse as BatchCreateResponse,
    type BatchRetrieveResponse as BatchRetrieveResponse,
    type BatchListResponse as BatchListResponse,
    type BatchCancelResponse as BatchCancelResponse,
    type BatchCreateParams as BatchCreateParams,
    type BatchListParams as BatchListParams,
  };

  export { Chat as Chat };

  export {
    Completions as Completions,
    type CompletionCreateResponse as CompletionCreateResponse,
    type CompletionCreateParams as CompletionCreateParams,
  };

  export {
    Containers as Containers,
    type ContainerCreateResponse as ContainerCreateResponse,
    type ContainerRetrieveResponse as ContainerRetrieveResponse,
    type ContainerListResponse as ContainerListResponse,
    type ContainerCreateParams as ContainerCreateParams,
    type ContainerListParams as ContainerListParams,
  };

  export {
    Conversations as Conversations,
    type ConversationCreateResponse as ConversationCreateResponse,
    type ConversationRetrieveResponse as ConversationRetrieveResponse,
    type ConversationUpdateResponse as ConversationUpdateResponse,
    type ConversationDeleteResponse as ConversationDeleteResponse,
    type ConversationCreateParams as ConversationCreateParams,
    type ConversationUpdateParams as ConversationUpdateParams,
  };

  export {
    Embeddings as Embeddings,
    type EmbeddingCreateResponse as EmbeddingCreateResponse,
    type EmbeddingCreateParams as EmbeddingCreateParams,
  };

  export {
    Evals as Evals,
    type EvalCustomDataSourceConfig as EvalCustomDataSourceConfig,
    type EvalGraderPython as EvalGraderPython,
    type EvalGraderScoreModel as EvalGraderScoreModel,
    type EvalGraderTextSimilarity as EvalGraderTextSimilarity,
    type EvalLogsDataSourceConfig as EvalLogsDataSourceConfig,
    type EvalStoredCompletionsDataSourceConfig as EvalStoredCompletionsDataSourceConfig,
    type EvalCreateResponse as EvalCreateResponse,
    type EvalRetrieveResponse as EvalRetrieveResponse,
    type EvalUpdateResponse as EvalUpdateResponse,
    type EvalListResponse as EvalListResponse,
    type EvalDeleteResponse as EvalDeleteResponse,
    type EvalCreateParams as EvalCreateParams,
    type EvalUpdateParams as EvalUpdateParams,
    type EvalListParams as EvalListParams,
  };

  export {
    Files as Files,
    type FileListResponse as FileListResponse,
    type FileDeleteResponse as FileDeleteResponse,
    type FileRetrieveContentResponse as FileRetrieveContentResponse,
    type FileListParams as FileListParams,
    type FileUploadParams as FileUploadParams,
  };

  export {
    FineTuning as FineTuning,
    type GraderMulti as GraderMulti,
    type GraderPython as GraderPython,
    type GraderScoreModel as GraderScoreModel,
    type GraderTextSimilarity as GraderTextSimilarity,
  };

  export {
    Images as Images,
    type Image as Image,
    type ImageGenInputUsageDetails as ImageGenInputUsageDetails,
    type ImageGenUsage as ImageGenUsage,
    type ImageCreateEditResponse as ImageCreateEditResponse,
    type ImageCreateImageResponse as ImageCreateImageResponse,
    type ImageCreateVariationResponse as ImageCreateVariationResponse,
    type ImageCreateEditParams as ImageCreateEditParams,
    type ImageCreateImageParams as ImageCreateImageParams,
    type ImageCreateVariationParams as ImageCreateVariationParams,
  };

  export {
    Models as Models,
    type ModelRetrieveResponse as ModelRetrieveResponse,
    type ModelListResponse as ModelListResponse,
    type ModelDeleteResponse as ModelDeleteResponse,
  };

  export {
    Moderations as Moderations,
    type ModerationCreateResponse as ModerationCreateResponse,
    type ModerationCreateParams as ModerationCreateParams,
  };

  export {
    Organization as Organization,
    type Certificate as Certificate,
    type CostsResult as CostsResult,
    type UsageAudioSpeechesResult as UsageAudioSpeechesResult,
    type UsageAudioTranscriptionsResult as UsageAudioTranscriptionsResult,
    type UsageCodeInterpreterSessionsResult as UsageCodeInterpreterSessionsResult,
    type UsageCompletionsResult as UsageCompletionsResult,
    type UsageEmbeddingsResult as UsageEmbeddingsResult,
    type UsageImagesResult as UsageImagesResult,
    type UsageModerationsResult as UsageModerationsResult,
    type UsageTimeBucket as UsageTimeBucket,
    type UsageVectorStoresResult as UsageVectorStoresResult,
    type OrganizationGetCostsResponse as OrganizationGetCostsResponse,
    type OrganizationListAuditLogsResponse as OrganizationListAuditLogsResponse,
    type OrganizationGetCostsParams as OrganizationGetCostsParams,
    type OrganizationListAuditLogsParams as OrganizationListAuditLogsParams,
  };

  export {
    Realtime as Realtime,
    type AudioTranscription as AudioTranscription,
    type RealtimeFunctionTool as RealtimeFunctionTool,
    type RealtimeCreateClientSecretResponse as RealtimeCreateClientSecretResponse,
    type RealtimeCreateSessionResponse as RealtimeCreateSessionResponse,
    type RealtimeCreateTranscriptionSessionResponse as RealtimeCreateTranscriptionSessionResponse,
    type RealtimeCreateClientSecretParams as RealtimeCreateClientSecretParams,
    type RealtimeCreateSessionParams as RealtimeCreateSessionParams,
    type RealtimeCreateTranscriptionSessionParams as RealtimeCreateTranscriptionSessionParams,
  };

  export {
    Responses as Responses,
    type Conversation2 as Conversation2,
    type FunctionToolCall as FunctionToolCall,
    type OutputMessage as OutputMessage,
    type Reasoning as Reasoning,
    type ResponseUsage as ResponseUsage,
    type ToolChoiceAllowed as ToolChoiceAllowed,
    type ToolChoiceCustom as ToolChoiceCustom,
    type ToolChoiceTypes as ToolChoiceTypes,
    type ResponseCreateResponse as ResponseCreateResponse,
    type ResponseRetrieveResponse as ResponseRetrieveResponse,
    type ResponseCancelResponse as ResponseCancelResponse,
    type ResponseListInputItemsResponse as ResponseListInputItemsResponse,
    type ResponseCreateParams as ResponseCreateParams,
    type ResponseRetrieveParams as ResponseRetrieveParams,
    type ResponseListInputItemsParams as ResponseListInputItemsParams,
  };

  export {
    Threads as Threads,
    type AssistantToolsFileSearchTypeOnly as AssistantToolsFileSearchTypeOnly,
    type ThreadCreateResponse as ThreadCreateResponse,
    type ThreadRetrieveResponse as ThreadRetrieveResponse,
    type ThreadUpdateResponse as ThreadUpdateResponse,
    type ThreadDeleteResponse as ThreadDeleteResponse,
    type ThreadCreateParams as ThreadCreateParams,
    type ThreadUpdateParams as ThreadUpdateParams,
  };

  export {
    UploadsAPIUploads as Uploads,
    type UploadCreateResponse as UploadCreateResponse,
    type UploadAddPartResponse as UploadAddPartResponse,
    type UploadCancelResponse as UploadCancelResponse,
    type UploadCompleteResponse as UploadCompleteResponse,
    type UploadCreateParams as UploadCreateParams,
    type UploadAddPartParams as UploadAddPartParams,
    type UploadCompleteParams as UploadCompleteParams,
  };

  export {
    VectorStores as VectorStores,
    type AutoChunkingStrategyRequestParam as AutoChunkingStrategyRequestParam,
    type OtherChunkingStrategyResponseParam as OtherChunkingStrategyResponseParam,
    type StaticChunkingStrategy as StaticChunkingStrategy,
    type StaticChunkingStrategyRequestParam as StaticChunkingStrategyRequestParam,
    type StaticChunkingStrategyResponseParam as StaticChunkingStrategyResponseParam,
    type VectorStoreExpirationAfter as VectorStoreExpirationAfter,
    type VectorStoreCreateResponse as VectorStoreCreateResponse,
    type VectorStoreRetrieveResponse as VectorStoreRetrieveResponse,
    type VectorStoreUpdateResponse as VectorStoreUpdateResponse,
    type VectorStoreListResponse as VectorStoreListResponse,
    type VectorStoreDeleteResponse as VectorStoreDeleteResponse,
    type VectorStoreSearchResponse as VectorStoreSearchResponse,
    type VectorStoreCreateParams as VectorStoreCreateParams,
    type VectorStoreUpdateParams as VectorStoreUpdateParams,
    type VectorStoreListParams as VectorStoreListParams,
    type VectorStoreSearchParams as VectorStoreSearchParams,
  };

  export {
    Videos as Videos,
    type Error2 as Error2,
    type VideoCreateResponse as VideoCreateResponse,
    type VideoRetrieveResponse as VideoRetrieveResponse,
    type VideoListResponse as VideoListResponse,
    type VideoDeleteResponse as VideoDeleteResponse,
    type VideoRemixResponse as VideoRemixResponse,
    type VideoRetrieveContentResponse as VideoRetrieveContentResponse,
    type VideoCreateParams as VideoCreateParams,
    type VideoListParams as VideoListParams,
    type VideoRemixParams as VideoRemixParams,
    type VideoRetrieveContentParams as VideoRetrieveContentParams,
  };

  export {
    Chatkit as Chatkit,
    type ChatkitUploadFileResponse as ChatkitUploadFileResponse,
    type ChatkitUploadFileParams as ChatkitUploadFileParams,
  };

  export type ApproximateLocation = API.ApproximateLocation;
  export type AssistantToolsCode = API.AssistantToolsCode;
  export type AssistantToolsFileSearch = API.AssistantToolsFileSearch;
  export type AssistantToolsFunction = API.AssistantToolsFunction;
  export type Click = API.Click;
  export type CodeInterpreterOutputImage = API.CodeInterpreterOutputImage;
  export type CodeInterpreterOutputLogs = API.CodeInterpreterOutputLogs;
  export type CodeInterpreterTool = API.CodeInterpreterTool;
  export type CodeInterpreterToolAuto = API.CodeInterpreterToolAuto;
  export type CodeInterpreterToolCall = API.CodeInterpreterToolCall;
  export type ComparisonFilter = API.ComparisonFilter;
  export type CompletionUsage = API.CompletionUsage;
  export type CompoundFilter = API.CompoundFilter;
  export type ComputerScreenshotImage = API.ComputerScreenshotImage;
  export type ComputerToolCall = API.ComputerToolCall;
  export type ComputerToolCallOutputResource = API.ComputerToolCallOutputResource;
  export type ComputerToolCallSafetyCheck = API.ComputerToolCallSafetyCheck;
  export type ComputerUsePreviewTool = API.ComputerUsePreviewTool;
  export type ContainerFileCitationBody = API.ContainerFileCitationBody;
  export type Coordinate = API.Coordinate;
  export type CustomTool = API.CustomTool;
  export type CustomToolCall = API.CustomToolCall;
  export type DoubleClick = API.DoubleClick;
  export type Drag = API.Drag;
  export type EvalItem = API.EvalItem;
  export type ExCaiFile = API.ExCaiFile;
  export type FileCitationBody = API.FileCitationBody;
  export type FilePath = API.FilePath;
  export type FileSearchRankingOptions = API.FileSearchRankingOptions;
  export type FileSearchTool = API.FileSearchTool;
  export type FileSearchToolCall = API.FileSearchToolCall;
  export type FunctionObject = API.FunctionObject;
  export type FunctionTool = API.FunctionTool;
  export type FunctionToolCallOutputResource = API.FunctionToolCallOutputResource;
  export type FunctionToolCallResource = API.FunctionToolCallResource;
  export type GraderLabelModel = API.GraderLabelModel;
  export type GraderStringCheck = API.GraderStringCheck;
  export type ImageGenTool = API.ImageGenTool;
  export type ImageGenToolCall = API.ImageGenToolCall;
  export type InputAudio = API.InputAudio;
  export type InputFileContent = API.InputFileContent;
  export type InputImageContent = API.InputImageContent;
  export type InputTextContent = API.InputTextContent;
  export type KeyPress = API.KeyPress;
  export type LocalShellExecAction = API.LocalShellExecAction;
  export type LocalShellTool = API.LocalShellTool;
  export type LocalShellToolCall = API.LocalShellToolCall;
  export type LocalShellToolCallOutput = API.LocalShellToolCallOutput;
  export type LogProb = API.LogProb;
  export type McpApprovalRequest = API.McpApprovalRequest;
  export type McpApprovalResponseResource = API.McpApprovalResponseResource;
  export type McpListTools = API.McpListTools;
  export type McpListToolsTool = API.McpListToolsTool;
  export type McpTool = API.McpTool;
  export type McpToolCall = API.McpToolCall;
  export type McpToolFilter = API.McpToolFilter;
  export type Move = API.Move;
  export type OutputTextContent = API.OutputTextContent;
  export type RankingOptions = API.RankingOptions;
  export type ReasoningItem = API.ReasoningItem;
  export type ReasoningTextContent = API.ReasoningTextContent;
  export type RefusalContent = API.RefusalContent;
  export type ResponseFormatJsonObject = API.ResponseFormatJsonObject;
  export type ResponseFormatJsonSchema = API.ResponseFormatJsonSchema;
  export type ResponseFormatText = API.ResponseFormatText;
  export type Screenshot = API.Screenshot;
  export type Scroll = API.Scroll;
  export type Summary = API.Summary;
  export type TextResponseFormatJsonSchema = API.TextResponseFormatJsonSchema;
  export type ToolChoiceFunction = API.ToolChoiceFunction;
  export type ToolChoiceMcp = API.ToolChoiceMcp;
  export type TopLogProb = API.TopLogProb;
  export type Type = API.Type;
  export type URLCitationBody = API.URLCitationBody;
  export type Wait = API.Wait;
  export type WebSearchActionFind = API.WebSearchActionFind;
  export type WebSearchActionOpenPage = API.WebSearchActionOpenPage;
  export type WebSearchActionSearch = API.WebSearchActionSearch;
  export type WebSearchPreviewTool = API.WebSearchPreviewTool;
  export type WebSearchTool = API.WebSearchTool;
  export type WebSearchToolCall = API.WebSearchToolCall;
}

export { toFile, fileFromPath } from './uploads';
export {
  ExCaiError,
  APIError,
  APIConnectionError,
  APIConnectionTimeoutError,
  APIUserAbortError,
  NotFoundError,
  ConflictError,
  RateLimitError,
  BadRequestError,
  AuthenticationError,
  InternalServerError,
  PermissionDeniedError,
  UnprocessableEntityError,
} from './error';

export default ExCai;
