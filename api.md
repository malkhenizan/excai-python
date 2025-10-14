# Assistants

Types:

```python
from excai.types import (
    AssistantCreateResponse,
    AssistantRetrieveResponse,
    AssistantUpdateResponse,
    AssistantListResponse,
    AssistantDeleteResponse,
)
```

Methods:

- <code title="post /assistants">client.assistants.<a href="./src/excai/resources/assistants.py">create</a>(\*\*<a href="src/excai/types/assistant_create_params.py">params</a>) -> <a href="./src/excai/types/assistant_create_response.py">AssistantCreateResponse</a></code>
- <code title="get /assistants/{assistant_id}">client.assistants.<a href="./src/excai/resources/assistants.py">retrieve</a>(assistant_id) -> <a href="./src/excai/types/assistant_retrieve_response.py">AssistantRetrieveResponse</a></code>
- <code title="post /assistants/{assistant_id}">client.assistants.<a href="./src/excai/resources/assistants.py">update</a>(assistant_id, \*\*<a href="src/excai/types/assistant_update_params.py">params</a>) -> <a href="./src/excai/types/assistant_update_response.py">AssistantUpdateResponse</a></code>
- <code title="get /assistants">client.assistants.<a href="./src/excai/resources/assistants.py">list</a>(\*\*<a href="src/excai/types/assistant_list_params.py">params</a>) -> <a href="./src/excai/types/assistant_list_response.py">AssistantListResponse</a></code>
- <code title="delete /assistants/{assistant_id}">client.assistants.<a href="./src/excai/resources/assistants.py">delete</a>(assistant_id) -> <a href="./src/excai/types/assistant_delete_response.py">AssistantDeleteResponse</a></code>

# Audio

Types:

```python
from excai.types import AudioTranscribeAudioResponse, AudioTranslateAudioResponse
```

Methods:

- <code title="post /audio/speech">client.audio.<a href="./src/excai/resources/audio.py">generate_audio</a>(\*\*<a href="src/excai/types/audio_generate_audio_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /audio/transcriptions">client.audio.<a href="./src/excai/resources/audio.py">transcribe_audio</a>(\*\*<a href="src/excai/types/audio_transcribe_audio_params.py">params</a>) -> <a href="./src/excai/types/audio_transcribe_audio_response.py">AudioTranscribeAudioResponse</a></code>
- <code title="post /audio/translations">client.audio.<a href="./src/excai/resources/audio.py">translate_audio</a>(\*\*<a href="src/excai/types/audio_translate_audio_params.py">params</a>) -> <a href="./src/excai/types/audio_translate_audio_response.py">AudioTranslateAudioResponse</a></code>

# Batches

Types:

```python
from excai.types import (
    BatchCreateResponse,
    BatchRetrieveResponse,
    BatchListResponse,
    BatchCancelResponse,
)
```

Methods:

- <code title="post /batches">client.batches.<a href="./src/excai/resources/batches.py">create</a>(\*\*<a href="src/excai/types/batch_create_params.py">params</a>) -> <a href="./src/excai/types/batch_create_response.py">BatchCreateResponse</a></code>
- <code title="get /batches/{batch_id}">client.batches.<a href="./src/excai/resources/batches.py">retrieve</a>(batch_id) -> <a href="./src/excai/types/batch_retrieve_response.py">BatchRetrieveResponse</a></code>
- <code title="get /batches">client.batches.<a href="./src/excai/resources/batches.py">list</a>(\*\*<a href="src/excai/types/batch_list_params.py">params</a>) -> <a href="./src/excai/types/batch_list_response.py">BatchListResponse</a></code>
- <code title="post /batches/{batch_id}/cancel">client.batches.<a href="./src/excai/resources/batches.py">cancel</a>(batch_id) -> <a href="./src/excai/types/batch_cancel_response.py">BatchCancelResponse</a></code>

# Chat

## Completions

Types:

```python
from excai.types.chat import (
    CompletionCreateResponse,
    CompletionRetrieveResponse,
    CompletionUpdateResponse,
    CompletionListResponse,
    CompletionDeleteResponse,
    CompletionListMessagesResponse,
)
```

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/excai/resources/chat/completions.py">create</a>(\*\*<a href="src/excai/types/chat/completion_create_params.py">params</a>) -> <a href="./src/excai/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>
- <code title="get /chat/completions/{completion_id}">client.chat.completions.<a href="./src/excai/resources/chat/completions.py">retrieve</a>(completion_id) -> <a href="./src/excai/types/chat/completion_retrieve_response.py">CompletionRetrieveResponse</a></code>
- <code title="post /chat/completions/{completion_id}">client.chat.completions.<a href="./src/excai/resources/chat/completions.py">update</a>(completion_id, \*\*<a href="src/excai/types/chat/completion_update_params.py">params</a>) -> <a href="./src/excai/types/chat/completion_update_response.py">CompletionUpdateResponse</a></code>
- <code title="get /chat/completions">client.chat.completions.<a href="./src/excai/resources/chat/completions.py">list</a>(\*\*<a href="src/excai/types/chat/completion_list_params.py">params</a>) -> <a href="./src/excai/types/chat/completion_list_response.py">CompletionListResponse</a></code>
- <code title="delete /chat/completions/{completion_id}">client.chat.completions.<a href="./src/excai/resources/chat/completions.py">delete</a>(completion_id) -> <a href="./src/excai/types/chat/completion_delete_response.py">CompletionDeleteResponse</a></code>
- <code title="get /chat/completions/{completion_id}/messages">client.chat.completions.<a href="./src/excai/resources/chat/completions.py">list_messages</a>(completion_id, \*\*<a href="src/excai/types/chat/completion_list_messages_params.py">params</a>) -> <a href="./src/excai/types/chat/completion_list_messages_response.py">CompletionListMessagesResponse</a></code>

# Completions

Types:

```python
from excai.types import CompletionCreateResponse
```

Methods:

- <code title="post /completions">client.completions.<a href="./src/excai/resources/completions.py">create</a>(\*\*<a href="src/excai/types/completion_create_params.py">params</a>) -> <a href="./src/excai/types/completion_create_response.py">CompletionCreateResponse</a></code>

# Embeddings

Types:

```python
from excai.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/excai/resources/embeddings.py">create</a>(\*\*<a href="src/excai/types/embedding_create_params.py">params</a>) -> <a href="./src/excai/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# Evals

Types:

```python
from excai.types import (
    EvalCreateResponse,
    EvalRetrieveResponse,
    EvalUpdateResponse,
    EvalListResponse,
    EvalDeleteResponse,
)
```

Methods:

- <code title="post /evals">client.evals.<a href="./src/excai/resources/evals/evals.py">create</a>(\*\*<a href="src/excai/types/eval_create_params.py">params</a>) -> <a href="./src/excai/types/eval_create_response.py">EvalCreateResponse</a></code>
- <code title="get /evals/{eval_id}">client.evals.<a href="./src/excai/resources/evals/evals.py">retrieve</a>(eval_id) -> <a href="./src/excai/types/eval_retrieve_response.py">EvalRetrieveResponse</a></code>
- <code title="post /evals/{eval_id}">client.evals.<a href="./src/excai/resources/evals/evals.py">update</a>(eval_id, \*\*<a href="src/excai/types/eval_update_params.py">params</a>) -> <a href="./src/excai/types/eval_update_response.py">EvalUpdateResponse</a></code>
- <code title="get /evals">client.evals.<a href="./src/excai/resources/evals/evals.py">list</a>(\*\*<a href="src/excai/types/eval_list_params.py">params</a>) -> <a href="./src/excai/types/eval_list_response.py">EvalListResponse</a></code>
- <code title="delete /evals/{eval_id}">client.evals.<a href="./src/excai/resources/evals/evals.py">delete</a>(eval_id) -> <a href="./src/excai/types/eval_delete_response.py">EvalDeleteResponse</a></code>

## Runs

Types:

```python
from excai.types.evals import (
    RunCreateResponse,
    RunRetrieveResponse,
    RunListResponse,
    RunDeleteResponse,
    RunCancelResponse,
)
```

Methods:

- <code title="post /evals/{eval_id}/runs">client.evals.runs.<a href="./src/excai/resources/evals/runs/runs.py">create</a>(eval_id, \*\*<a href="src/excai/types/evals/run_create_params.py">params</a>) -> <a href="./src/excai/types/evals/run_create_response.py">RunCreateResponse</a></code>
- <code title="get /evals/{eval_id}/runs/{run_id}">client.evals.runs.<a href="./src/excai/resources/evals/runs/runs.py">retrieve</a>(run_id, \*, eval_id) -> <a href="./src/excai/types/evals/run_retrieve_response.py">RunRetrieveResponse</a></code>
- <code title="get /evals/{eval_id}/runs">client.evals.runs.<a href="./src/excai/resources/evals/runs/runs.py">list</a>(eval_id, \*\*<a href="src/excai/types/evals/run_list_params.py">params</a>) -> <a href="./src/excai/types/evals/run_list_response.py">RunListResponse</a></code>
- <code title="delete /evals/{eval_id}/runs/{run_id}">client.evals.runs.<a href="./src/excai/resources/evals/runs/runs.py">delete</a>(run_id, \*, eval_id) -> <a href="./src/excai/types/evals/run_delete_response.py">RunDeleteResponse</a></code>
- <code title="post /evals/{eval_id}/runs/{run_id}">client.evals.runs.<a href="./src/excai/resources/evals/runs/runs.py">cancel</a>(run_id, \*, eval_id) -> <a href="./src/excai/types/evals/run_cancel_response.py">RunCancelResponse</a></code>

### OutputItems

Types:

```python
from excai.types.evals.runs import OutputItemRetrieveResponse, OutputItemListResponse
```

Methods:

- <code title="get /evals/{eval_id}/runs/{run_id}/output_items/{output_item_id}">client.evals.runs.output_items.<a href="./src/excai/resources/evals/runs/output_items.py">retrieve</a>(output_item_id, \*, eval_id, run_id) -> <a href="./src/excai/types/evals/runs/output_item_retrieve_response.py">OutputItemRetrieveResponse</a></code>
- <code title="get /evals/{eval_id}/runs/{run_id}/output_items">client.evals.runs.output_items.<a href="./src/excai/resources/evals/runs/output_items.py">list</a>(run_id, \*, eval_id, \*\*<a href="src/excai/types/evals/runs/output_item_list_params.py">params</a>) -> <a href="./src/excai/types/evals/runs/output_item_list_response.py">OutputItemListResponse</a></code>

# Files

Types:

```python
from excai.types import (
    FileRetrieveResponse,
    FileListResponse,
    FileDeleteResponse,
    FileRetrieveContentResponse,
    FileUploadResponse,
)
```

Methods:

- <code title="get /files/{file_id}">client.files.<a href="./src/excai/resources/files.py">retrieve</a>(file_id) -> <a href="./src/excai/types/file_retrieve_response.py">FileRetrieveResponse</a></code>
- <code title="get /files">client.files.<a href="./src/excai/resources/files.py">list</a>(\*\*<a href="src/excai/types/file_list_params.py">params</a>) -> <a href="./src/excai/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/excai/resources/files.py">delete</a>(file_id) -> <a href="./src/excai/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/excai/resources/files.py">retrieve_content</a>(file_id) -> str</code>
- <code title="post /files">client.files.<a href="./src/excai/resources/files.py">upload</a>(\*\*<a href="src/excai/types/file_upload_params.py">params</a>) -> <a href="./src/excai/types/file_upload_response.py">FileUploadResponse</a></code>

# FineTuning

## Checkpoints

### Permissions

Types:

```python
from excai.types.fine_tuning.checkpoints import (
    PermissionCreateResponse,
    PermissionRetrieveResponse,
    PermissionDeleteResponse,
)
```

Methods:

- <code title="post /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions">client.fine_tuning.checkpoints.permissions.<a href="./src/excai/resources/fine_tuning/checkpoints/permissions.py">create</a>(fine_tuned_model_checkpoint, \*\*<a href="src/excai/types/fine_tuning/checkpoints/permission_create_params.py">params</a>) -> <a href="./src/excai/types/fine_tuning/checkpoints/permission_create_response.py">PermissionCreateResponse</a></code>
- <code title="get /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions">client.fine_tuning.checkpoints.permissions.<a href="./src/excai/resources/fine_tuning/checkpoints/permissions.py">retrieve</a>(fine_tuned_model_checkpoint, \*\*<a href="src/excai/types/fine_tuning/checkpoints/permission_retrieve_params.py">params</a>) -> <a href="./src/excai/types/fine_tuning/checkpoints/permission_retrieve_response.py">PermissionRetrieveResponse</a></code>
- <code title="delete /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}">client.fine_tuning.checkpoints.permissions.<a href="./src/excai/resources/fine_tuning/checkpoints/permissions.py">delete</a>(permission_id, \*, fine_tuned_model_checkpoint) -> <a href="./src/excai/types/fine_tuning/checkpoints/permission_delete_response.py">PermissionDeleteResponse</a></code>

## Jobs

Types:

```python
from excai.types.fine_tuning import (
    JobCreateResponse,
    JobRetrieveResponse,
    JobListResponse,
    JobCancelResponse,
)
```

Methods:

- <code title="post /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/excai/resources/fine_tuning/jobs/jobs.py">create</a>(\*\*<a href="src/excai/types/fine_tuning/job_create_params.py">params</a>) -> <a href="./src/excai/types/fine_tuning/job_create_response.py">JobCreateResponse</a></code>
- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}">client.fine_tuning.jobs.<a href="./src/excai/resources/fine_tuning/jobs/jobs.py">retrieve</a>(fine_tuning_job_id) -> <a href="./src/excai/types/fine_tuning/job_retrieve_response.py">JobRetrieveResponse</a></code>
- <code title="get /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/excai/resources/fine_tuning/jobs/jobs.py">list</a>(\*\*<a href="src/excai/types/fine_tuning/job_list_params.py">params</a>) -> <a href="./src/excai/types/fine_tuning/job_list_response.py">JobListResponse</a></code>
- <code title="post /fine_tuning/jobs/{fine_tuning_job_id}/cancel">client.fine_tuning.jobs.<a href="./src/excai/resources/fine_tuning/jobs/jobs.py">cancel</a>(fine_tuning_job_id) -> <a href="./src/excai/types/fine_tuning/job_cancel_response.py">JobCancelResponse</a></code>

### Checkpoints

Types:

```python
from excai.types.fine_tuning.jobs import CheckpointRetrieveResponse
```

Methods:

- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints">client.fine_tuning.jobs.checkpoints.<a href="./src/excai/resources/fine_tuning/jobs/checkpoints.py">retrieve</a>(fine_tuning_job_id, \*\*<a href="src/excai/types/fine_tuning/jobs/checkpoint_retrieve_params.py">params</a>) -> <a href="./src/excai/types/fine_tuning/jobs/checkpoint_retrieve_response.py">CheckpointRetrieveResponse</a></code>

### Events

Types:

```python
from excai.types.fine_tuning.jobs import EventRetrieveResponse
```

Methods:

- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/events">client.fine_tuning.jobs.events.<a href="./src/excai/resources/fine_tuning/jobs/events.py">retrieve</a>(fine_tuning_job_id, \*\*<a href="src/excai/types/fine_tuning/jobs/event_retrieve_params.py">params</a>) -> <a href="./src/excai/types/fine_tuning/jobs/event_retrieve_response.py">EventRetrieveResponse</a></code>

# Images

Types:

```python
from excai.types import (
    ImageCreateEditResponse,
    ImageCreateGenerationResponse,
    ImageCreateVariationResponse,
)
```

Methods:

- <code title="post /images/edits">client.images.<a href="./src/excai/resources/images.py">create_edit</a>(\*\*<a href="src/excai/types/image_create_edit_params.py">params</a>) -> <a href="./src/excai/types/image_create_edit_response.py">ImageCreateEditResponse</a></code>
- <code title="post /images/generations">client.images.<a href="./src/excai/resources/images.py">create_generation</a>(\*\*<a href="src/excai/types/image_create_generation_params.py">params</a>) -> <a href="./src/excai/types/image_create_generation_response.py">ImageCreateGenerationResponse</a></code>
- <code title="post /images/variations">client.images.<a href="./src/excai/resources/images.py">create_variation</a>(\*\*<a href="src/excai/types/image_create_variation_params.py">params</a>) -> <a href="./src/excai/types/image_create_variation_response.py">ImageCreateVariationResponse</a></code>

# Models

Types:

```python
from excai.types import ModelRetrieveResponse, ModelListResponse, ModelDeleteResponse
```

Methods:

- <code title="get /models/{model}">client.models.<a href="./src/excai/resources/models.py">retrieve</a>(model) -> <a href="./src/excai/types/model_retrieve_response.py">ModelRetrieveResponse</a></code>
- <code title="get /models">client.models.<a href="./src/excai/resources/models.py">list</a>() -> <a href="./src/excai/types/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /models/{model}">client.models.<a href="./src/excai/resources/models.py">delete</a>(model) -> <a href="./src/excai/types/model_delete_response.py">ModelDeleteResponse</a></code>

# Moderations

Types:

```python
from excai.types import ModerationClassifyResponse
```

Methods:

- <code title="post /moderations">client.moderations.<a href="./src/excai/resources/moderations.py">classify</a>(\*\*<a href="src/excai/types/moderation_classify_params.py">params</a>) -> <a href="./src/excai/types/moderation_classify_response.py">ModerationClassifyResponse</a></code>

# Organization

Types:

```python
from excai.types import OrganizationGetCostsResponse, OrganizationListAuditLogsResponse
```

Methods:

- <code title="get /organization/costs">client.organization.<a href="./src/excai/resources/organization/organization.py">get_costs</a>(\*\*<a href="src/excai/types/organization_get_costs_params.py">params</a>) -> <a href="./src/excai/types/organization_get_costs_response.py">OrganizationGetCostsResponse</a></code>
- <code title="get /organization/audit_logs">client.organization.<a href="./src/excai/resources/organization/organization.py">list_audit_logs</a>(\*\*<a href="src/excai/types/organization_list_audit_logs_params.py">params</a>) -> <a href="./src/excai/types/organization_list_audit_logs_response.py">OrganizationListAuditLogsResponse</a></code>

## AdminAPIKeys

Types:

```python
from excai.types.organization import (
    AdminAPIKeyCreateResponse,
    AdminAPIKeyRetrieveResponse,
    AdminAPIKeyListResponse,
    AdminAPIKeyDeleteResponse,
)
```

Methods:

- <code title="post /organization/admin_api_keys">client.organization.admin_api_keys.<a href="./src/excai/resources/organization/admin_api_keys.py">create</a>(\*\*<a href="src/excai/types/organization/admin_api_key_create_params.py">params</a>) -> <a href="./src/excai/types/organization/admin_api_key_create_response.py">AdminAPIKeyCreateResponse</a></code>
- <code title="get /organization/admin_api_keys/{key_id}">client.organization.admin_api_keys.<a href="./src/excai/resources/organization/admin_api_keys.py">retrieve</a>(key_id) -> <a href="./src/excai/types/organization/admin_api_key_retrieve_response.py">AdminAPIKeyRetrieveResponse</a></code>
- <code title="get /organization/admin_api_keys">client.organization.admin_api_keys.<a href="./src/excai/resources/organization/admin_api_keys.py">list</a>(\*\*<a href="src/excai/types/organization/admin_api_key_list_params.py">params</a>) -> <a href="./src/excai/types/organization/admin_api_key_list_response.py">AdminAPIKeyListResponse</a></code>
- <code title="delete /organization/admin_api_keys/{key_id}">client.organization.admin_api_keys.<a href="./src/excai/resources/organization/admin_api_keys.py">delete</a>(key_id) -> <a href="./src/excai/types/organization/admin_api_key_delete_response.py">AdminAPIKeyDeleteResponse</a></code>

## Certificates

Types:

```python
from excai.types.organization import (
    CertificateRetrieveResponse,
    CertificateUpdateResponse,
    CertificateListResponse,
    CertificateDeleteResponse,
    CertificateActivateResponse,
    CertificateDeactivateResponse,
    CertificateUploadResponse,
)
```

Methods:

- <code title="get /organization/certificates/{certificate_id}">client.organization.certificates.<a href="./src/excai/resources/organization/certificates.py">retrieve</a>(certificate_id, \*\*<a href="src/excai/types/organization/certificate_retrieve_params.py">params</a>) -> <a href="./src/excai/types/organization/certificate_retrieve_response.py">CertificateRetrieveResponse</a></code>
- <code title="post /organization/certificates/{certificate_id}">client.organization.certificates.<a href="./src/excai/resources/organization/certificates.py">update</a>(certificate_id, \*\*<a href="src/excai/types/organization/certificate_update_params.py">params</a>) -> <a href="./src/excai/types/organization/certificate_update_response.py">CertificateUpdateResponse</a></code>
- <code title="get /organization/certificates">client.organization.certificates.<a href="./src/excai/resources/organization/certificates.py">list</a>(\*\*<a href="src/excai/types/organization/certificate_list_params.py">params</a>) -> <a href="./src/excai/types/organization/certificate_list_response.py">CertificateListResponse</a></code>
- <code title="delete /organization/certificates/{certificate_id}">client.organization.certificates.<a href="./src/excai/resources/organization/certificates.py">delete</a>(certificate_id) -> <a href="./src/excai/types/organization/certificate_delete_response.py">CertificateDeleteResponse</a></code>
- <code title="post /organization/certificates/activate">client.organization.certificates.<a href="./src/excai/resources/organization/certificates.py">activate</a>(\*\*<a href="src/excai/types/organization/certificate_activate_params.py">params</a>) -> <a href="./src/excai/types/organization/certificate_activate_response.py">CertificateActivateResponse</a></code>
- <code title="post /organization/certificates/deactivate">client.organization.certificates.<a href="./src/excai/resources/organization/certificates.py">deactivate</a>(\*\*<a href="src/excai/types/organization/certificate_deactivate_params.py">params</a>) -> <a href="./src/excai/types/organization/certificate_deactivate_response.py">CertificateDeactivateResponse</a></code>
- <code title="post /organization/certificates">client.organization.certificates.<a href="./src/excai/resources/organization/certificates.py">upload</a>(\*\*<a href="src/excai/types/organization/certificate_upload_params.py">params</a>) -> <a href="./src/excai/types/organization/certificate_upload_response.py">CertificateUploadResponse</a></code>

## Invites

Types:

```python
from excai.types.organization import (
    InviteCreateResponse,
    InviteRetrieveResponse,
    InviteListResponse,
    InviteDeleteResponse,
)
```

Methods:

- <code title="post /organization/invites">client.organization.invites.<a href="./src/excai/resources/organization/invites.py">create</a>(\*\*<a href="src/excai/types/organization/invite_create_params.py">params</a>) -> <a href="./src/excai/types/organization/invite_create_response.py">InviteCreateResponse</a></code>
- <code title="get /organization/invites/{invite_id}">client.organization.invites.<a href="./src/excai/resources/organization/invites.py">retrieve</a>(invite_id) -> <a href="./src/excai/types/organization/invite_retrieve_response.py">InviteRetrieveResponse</a></code>
- <code title="get /organization/invites">client.organization.invites.<a href="./src/excai/resources/organization/invites.py">list</a>(\*\*<a href="src/excai/types/organization/invite_list_params.py">params</a>) -> <a href="./src/excai/types/organization/invite_list_response.py">InviteListResponse</a></code>
- <code title="delete /organization/invites/{invite_id}">client.organization.invites.<a href="./src/excai/resources/organization/invites.py">delete</a>(invite_id) -> <a href="./src/excai/types/organization/invite_delete_response.py">InviteDeleteResponse</a></code>

## Projects

Types:

```python
from excai.types.organization import (
    ProjectCreateResponse,
    ProjectRetrieveResponse,
    ProjectUpdateResponse,
    ProjectListResponse,
    ProjectArchiveResponse,
)
```

Methods:

- <code title="post /organization/projects">client.organization.projects.<a href="./src/excai/resources/organization/projects/projects.py">create</a>(\*\*<a href="src/excai/types/organization/project_create_params.py">params</a>) -> <a href="./src/excai/types/organization/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /organization/projects/{project_id}">client.organization.projects.<a href="./src/excai/resources/organization/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/excai/types/organization/project_retrieve_response.py">ProjectRetrieveResponse</a></code>
- <code title="post /organization/projects/{project_id}">client.organization.projects.<a href="./src/excai/resources/organization/projects/projects.py">update</a>(project_id, \*\*<a href="src/excai/types/organization/project_update_params.py">params</a>) -> <a href="./src/excai/types/organization/project_update_response.py">ProjectUpdateResponse</a></code>
- <code title="get /organization/projects">client.organization.projects.<a href="./src/excai/resources/organization/projects/projects.py">list</a>(\*\*<a href="src/excai/types/organization/project_list_params.py">params</a>) -> <a href="./src/excai/types/organization/project_list_response.py">ProjectListResponse</a></code>
- <code title="post /organization/projects/{project_id}/archive">client.organization.projects.<a href="./src/excai/resources/organization/projects/projects.py">archive</a>(project_id) -> <a href="./src/excai/types/organization/project_archive_response.py">ProjectArchiveResponse</a></code>

### APIKeys

Types:

```python
from excai.types.organization.projects import (
    APIKeyRetrieveResponse,
    APIKeyListResponse,
    APIKeyDeleteResponse,
)
```

Methods:

- <code title="get /organization/projects/{project_id}/api_keys/{key_id}">client.organization.projects.api_keys.<a href="./src/excai/resources/organization/projects/api_keys.py">retrieve</a>(key_id, \*, project_id) -> <a href="./src/excai/types/organization/projects/api_key_retrieve_response.py">APIKeyRetrieveResponse</a></code>
- <code title="get /organization/projects/{project_id}/api_keys">client.organization.projects.api_keys.<a href="./src/excai/resources/organization/projects/api_keys.py">list</a>(project_id, \*\*<a href="src/excai/types/organization/projects/api_key_list_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /organization/projects/{project_id}/api_keys/{key_id}">client.organization.projects.api_keys.<a href="./src/excai/resources/organization/projects/api_keys.py">delete</a>(key_id, \*, project_id) -> <a href="./src/excai/types/organization/projects/api_key_delete_response.py">APIKeyDeleteResponse</a></code>

### Certificates

Types:

```python
from excai.types.organization.projects import (
    CertificateListResponse,
    CertificateActivateResponse,
    CertificateDeactivateResponse,
)
```

Methods:

- <code title="get /organization/projects/{project_id}/certificates">client.organization.projects.certificates.<a href="./src/excai/resources/organization/projects/certificates.py">list</a>(project_id, \*\*<a href="src/excai/types/organization/projects/certificate_list_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/certificate_list_response.py">CertificateListResponse</a></code>
- <code title="post /organization/projects/{project_id}/certificates/activate">client.organization.projects.certificates.<a href="./src/excai/resources/organization/projects/certificates.py">activate</a>(project_id, \*\*<a href="src/excai/types/organization/projects/certificate_activate_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/certificate_activate_response.py">CertificateActivateResponse</a></code>
- <code title="post /organization/projects/{project_id}/certificates/deactivate">client.organization.projects.certificates.<a href="./src/excai/resources/organization/projects/certificates.py">deactivate</a>(project_id, \*\*<a href="src/excai/types/organization/projects/certificate_deactivate_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/certificate_deactivate_response.py">CertificateDeactivateResponse</a></code>

### RateLimits

Types:

```python
from excai.types.organization.projects import RateLimitRetrieveResponse, RateLimitUpdateResponse
```

Methods:

- <code title="get /organization/projects/{project_id}/rate_limits">client.organization.projects.rate_limits.<a href="./src/excai/resources/organization/projects/rate_limits.py">retrieve</a>(project_id, \*\*<a href="src/excai/types/organization/projects/rate_limit_retrieve_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/rate_limit_retrieve_response.py">RateLimitRetrieveResponse</a></code>
- <code title="post /organization/projects/{project_id}/rate_limits/{rate_limit_id}">client.organization.projects.rate_limits.<a href="./src/excai/resources/organization/projects/rate_limits.py">update</a>(rate_limit_id, \*, project_id, \*\*<a href="src/excai/types/organization/projects/rate_limit_update_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/rate_limit_update_response.py">RateLimitUpdateResponse</a></code>

### ServiceAccounts

Types:

```python
from excai.types.organization.projects import (
    ServiceAccountCreateResponse,
    ServiceAccountRetrieveResponse,
    ServiceAccountListResponse,
    ServiceAccountDeleteResponse,
)
```

Methods:

- <code title="post /organization/projects/{project_id}/service_accounts">client.organization.projects.service_accounts.<a href="./src/excai/resources/organization/projects/service_accounts.py">create</a>(project_id, \*\*<a href="src/excai/types/organization/projects/service_account_create_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/service_account_create_response.py">ServiceAccountCreateResponse</a></code>
- <code title="get /organization/projects/{project_id}/service_accounts/{service_account_id}">client.organization.projects.service_accounts.<a href="./src/excai/resources/organization/projects/service_accounts.py">retrieve</a>(service_account_id, \*, project_id) -> <a href="./src/excai/types/organization/projects/service_account_retrieve_response.py">ServiceAccountRetrieveResponse</a></code>
- <code title="get /organization/projects/{project_id}/service_accounts">client.organization.projects.service_accounts.<a href="./src/excai/resources/organization/projects/service_accounts.py">list</a>(project_id, \*\*<a href="src/excai/types/organization/projects/service_account_list_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/service_account_list_response.py">ServiceAccountListResponse</a></code>
- <code title="delete /organization/projects/{project_id}/service_accounts/{service_account_id}">client.organization.projects.service_accounts.<a href="./src/excai/resources/organization/projects/service_accounts.py">delete</a>(service_account_id, \*, project_id) -> <a href="./src/excai/types/organization/projects/service_account_delete_response.py">ServiceAccountDeleteResponse</a></code>

### Users

Types:

```python
from excai.types.organization.projects import (
    UserRetrieveResponse,
    UserUpdateResponse,
    UserListResponse,
    UserDeleteResponse,
    UserAddResponse,
)
```

Methods:

- <code title="get /organization/projects/{project_id}/users/{user_id}">client.organization.projects.users.<a href="./src/excai/resources/organization/projects/users.py">retrieve</a>(user_id, \*, project_id) -> <a href="./src/excai/types/organization/projects/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="post /organization/projects/{project_id}/users/{user_id}">client.organization.projects.users.<a href="./src/excai/resources/organization/projects/users.py">update</a>(user_id, \*, project_id, \*\*<a href="src/excai/types/organization/projects/user_update_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /organization/projects/{project_id}/users">client.organization.projects.users.<a href="./src/excai/resources/organization/projects/users.py">list</a>(project_id, \*\*<a href="src/excai/types/organization/projects/user_list_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/user_list_response.py">UserListResponse</a></code>
- <code title="delete /organization/projects/{project_id}/users/{user_id}">client.organization.projects.users.<a href="./src/excai/resources/organization/projects/users.py">delete</a>(user_id, \*, project_id) -> <a href="./src/excai/types/organization/projects/user_delete_response.py">UserDeleteResponse</a></code>
- <code title="post /organization/projects/{project_id}/users">client.organization.projects.users.<a href="./src/excai/resources/organization/projects/users.py">add</a>(project_id, \*\*<a href="src/excai/types/organization/projects/user_add_params.py">params</a>) -> <a href="./src/excai/types/organization/projects/user_add_response.py">UserAddResponse</a></code>

## Usage

Types:

```python
from excai.types.organization import (
    UsageAudioSpeechesResponse,
    UsageAudioTranscriptionsResponse,
    UsageCodeInterpreterSessionsResponse,
    UsageCompletionsResponse,
    UsageEmbeddingsResponse,
    UsageImagesResponse,
    UsageModerationsResponse,
    UsageVectorStoresResponse,
)
```

Methods:

- <code title="get /organization/usage/audio_speeches">client.organization.usage.<a href="./src/excai/resources/organization/usage.py">audio_speeches</a>(\*\*<a href="src/excai/types/organization/usage_audio_speeches_params.py">params</a>) -> <a href="./src/excai/types/organization/usage_audio_speeches_response.py">UsageAudioSpeechesResponse</a></code>
- <code title="get /organization/usage/audio_transcriptions">client.organization.usage.<a href="./src/excai/resources/organization/usage.py">audio_transcriptions</a>(\*\*<a href="src/excai/types/organization/usage_audio_transcriptions_params.py">params</a>) -> <a href="./src/excai/types/organization/usage_audio_transcriptions_response.py">UsageAudioTranscriptionsResponse</a></code>
- <code title="get /organization/usage/code_interpreter_sessions">client.organization.usage.<a href="./src/excai/resources/organization/usage.py">code_interpreter_sessions</a>(\*\*<a href="src/excai/types/organization/usage_code_interpreter_sessions_params.py">params</a>) -> <a href="./src/excai/types/organization/usage_code_interpreter_sessions_response.py">UsageCodeInterpreterSessionsResponse</a></code>
- <code title="get /organization/usage/completions">client.organization.usage.<a href="./src/excai/resources/organization/usage.py">completions</a>(\*\*<a href="src/excai/types/organization/usage_completions_params.py">params</a>) -> <a href="./src/excai/types/organization/usage_completions_response.py">UsageCompletionsResponse</a></code>
- <code title="get /organization/usage/embeddings">client.organization.usage.<a href="./src/excai/resources/organization/usage.py">embeddings</a>(\*\*<a href="src/excai/types/organization/usage_embeddings_params.py">params</a>) -> <a href="./src/excai/types/organization/usage_embeddings_response.py">UsageEmbeddingsResponse</a></code>
- <code title="get /organization/usage/images">client.organization.usage.<a href="./src/excai/resources/organization/usage.py">images</a>(\*\*<a href="src/excai/types/organization/usage_images_params.py">params</a>) -> <a href="./src/excai/types/organization/usage_images_response.py">UsageImagesResponse</a></code>
- <code title="get /organization/usage/moderations">client.organization.usage.<a href="./src/excai/resources/organization/usage.py">moderations</a>(\*\*<a href="src/excai/types/organization/usage_moderations_params.py">params</a>) -> <a href="./src/excai/types/organization/usage_moderations_response.py">UsageModerationsResponse</a></code>
- <code title="get /organization/usage/vector_stores">client.organization.usage.<a href="./src/excai/resources/organization/usage.py">vector_stores</a>(\*\*<a href="src/excai/types/organization/usage_vector_stores_params.py">params</a>) -> <a href="./src/excai/types/organization/usage_vector_stores_response.py">UsageVectorStoresResponse</a></code>

## Users

Types:

```python
from excai.types.organization import (
    UserRetrieveResponse,
    UserUpdateResponse,
    UserListResponse,
    UserDeleteResponse,
)
```

Methods:

- <code title="get /organization/users/{user_id}">client.organization.users.<a href="./src/excai/resources/organization/users.py">retrieve</a>(user_id) -> <a href="./src/excai/types/organization/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="post /organization/users/{user_id}">client.organization.users.<a href="./src/excai/resources/organization/users.py">update</a>(user_id, \*\*<a href="src/excai/types/organization/user_update_params.py">params</a>) -> <a href="./src/excai/types/organization/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /organization/users">client.organization.users.<a href="./src/excai/resources/organization/users.py">list</a>(\*\*<a href="src/excai/types/organization/user_list_params.py">params</a>) -> <a href="./src/excai/types/organization/user_list_response.py">UserListResponse</a></code>
- <code title="delete /organization/users/{user_id}">client.organization.users.<a href="./src/excai/resources/organization/users.py">delete</a>(user_id) -> <a href="./src/excai/types/organization/user_delete_response.py">UserDeleteResponse</a></code>

# Realtime

Types:

```python
from excai.types import RealtimeCreateSessionResponse, RealtimeCreateTranscriptionSessionResponse
```

Methods:

- <code title="post /realtime/sessions">client.realtime.<a href="./src/excai/resources/realtime.py">create_session</a>(\*\*<a href="src/excai/types/realtime_create_session_params.py">params</a>) -> <a href="./src/excai/types/realtime_create_session_response.py">RealtimeCreateSessionResponse</a></code>
- <code title="post /realtime/transcription_sessions">client.realtime.<a href="./src/excai/resources/realtime.py">create_transcription_session</a>(\*\*<a href="src/excai/types/realtime_create_transcription_session_params.py">params</a>) -> <a href="./src/excai/types/realtime_create_transcription_session_response.py">RealtimeCreateTranscriptionSessionResponse</a></code>

# Responses

Types:

```python
from excai.types import (
    ResponseCreateResponse,
    ResponseRetrieveResponse,
    ResponseListInputItemsResponse,
)
```

Methods:

- <code title="post /responses">client.responses.<a href="./src/excai/resources/responses.py">create</a>(\*\*<a href="src/excai/types/response_create_params.py">params</a>) -> <a href="./src/excai/types/response_create_response.py">ResponseCreateResponse</a></code>
- <code title="get /responses/{response_id}">client.responses.<a href="./src/excai/resources/responses.py">retrieve</a>(response_id, \*\*<a href="src/excai/types/response_retrieve_params.py">params</a>) -> <a href="./src/excai/types/response_retrieve_response.py">ResponseRetrieveResponse</a></code>
- <code title="delete /responses/{response_id}">client.responses.<a href="./src/excai/resources/responses.py">delete</a>(response_id) -> None</code>
- <code title="get /responses/{response_id}/input_items">client.responses.<a href="./src/excai/resources/responses.py">list_input_items</a>(response_id, \*\*<a href="src/excai/types/response_list_input_items_params.py">params</a>) -> <a href="./src/excai/types/response_list_input_items_response.py">ResponseListInputItemsResponse</a></code>

# Threads

Types:

```python
from excai.types import (
    ThreadCreateResponse,
    ThreadRetrieveResponse,
    ThreadUpdateResponse,
    ThreadDeleteResponse,
)
```

Methods:

- <code title="post /threads">client.threads.<a href="./src/excai/resources/threads/threads.py">create</a>(\*\*<a href="src/excai/types/thread_create_params.py">params</a>) -> <a href="./src/excai/types/thread_create_response.py">ThreadCreateResponse</a></code>
- <code title="get /threads/{thread_id}">client.threads.<a href="./src/excai/resources/threads/threads.py">retrieve</a>(thread_id) -> <a href="./src/excai/types/thread_retrieve_response.py">ThreadRetrieveResponse</a></code>
- <code title="post /threads/{thread_id}">client.threads.<a href="./src/excai/resources/threads/threads.py">update</a>(thread_id, \*\*<a href="src/excai/types/thread_update_params.py">params</a>) -> <a href="./src/excai/types/thread_update_response.py">ThreadUpdateResponse</a></code>
- <code title="delete /threads/{thread_id}">client.threads.<a href="./src/excai/resources/threads/threads.py">delete</a>(thread_id) -> <a href="./src/excai/types/thread_delete_response.py">ThreadDeleteResponse</a></code>

## Runs

Types:

```python
from excai.types.threads import (
    RunCreateResponse,
    RunRetrieveResponse,
    RunListResponse,
    RunCancelRunResponse,
    RunCreateRunResponse,
    RunSubmitToolOutputsResponse,
    RunUpdateRunResponse,
)
```

Methods:

- <code title="post /threads/runs">client.threads.runs.<a href="./src/excai/resources/threads/runs/runs.py">create</a>(\*\*<a href="src/excai/types/threads/run_create_params.py">params</a>) -> <a href="./src/excai/types/threads/run_create_response.py">RunCreateResponse</a></code>
- <code title="get /threads/{thread_id}/runs/{run_id}">client.threads.runs.<a href="./src/excai/resources/threads/runs/runs.py">retrieve</a>(run_id, \*, thread_id) -> <a href="./src/excai/types/threads/run_retrieve_response.py">RunRetrieveResponse</a></code>
- <code title="get /threads/{thread_id}/runs">client.threads.runs.<a href="./src/excai/resources/threads/runs/runs.py">list</a>(thread_id, \*\*<a href="src/excai/types/threads/run_list_params.py">params</a>) -> <a href="./src/excai/types/threads/run_list_response.py">RunListResponse</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}/cancel">client.threads.runs.<a href="./src/excai/resources/threads/runs/runs.py">cancel_run</a>(run_id, \*, thread_id) -> <a href="./src/excai/types/threads/run_cancel_run_response.py">RunCancelRunResponse</a></code>
- <code title="post /threads/{thread_id}/runs">client.threads.runs.<a href="./src/excai/resources/threads/runs/runs.py">create_run</a>(thread_id, \*\*<a href="src/excai/types/threads/run_create_run_params.py">params</a>) -> <a href="./src/excai/types/threads/run_create_run_response.py">RunCreateRunResponse</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}/submit_tool_outputs">client.threads.runs.<a href="./src/excai/resources/threads/runs/runs.py">submit_tool_outputs</a>(run_id, \*, thread_id, \*\*<a href="src/excai/types/threads/run_submit_tool_outputs_params.py">params</a>) -> <a href="./src/excai/types/threads/run_submit_tool_outputs_response.py">RunSubmitToolOutputsResponse</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}">client.threads.runs.<a href="./src/excai/resources/threads/runs/runs.py">update_run</a>(run_id, \*, thread_id, \*\*<a href="src/excai/types/threads/run_update_run_params.py">params</a>) -> <a href="./src/excai/types/threads/run_update_run_response.py">RunUpdateRunResponse</a></code>

### Steps

Types:

```python
from excai.types.threads.runs import StepRetrieveResponse, StepListResponse
```

Methods:

- <code title="get /threads/{thread_id}/runs/{run_id}/steps/{step_id}">client.threads.runs.steps.<a href="./src/excai/resources/threads/runs/steps.py">retrieve</a>(step_id, \*, thread_id, run_id, \*\*<a href="src/excai/types/threads/runs/step_retrieve_params.py">params</a>) -> <a href="./src/excai/types/threads/runs/step_retrieve_response.py">StepRetrieveResponse</a></code>
- <code title="get /threads/{thread_id}/runs/{run_id}/steps">client.threads.runs.steps.<a href="./src/excai/resources/threads/runs/steps.py">list</a>(run_id, \*, thread_id, \*\*<a href="src/excai/types/threads/runs/step_list_params.py">params</a>) -> <a href="./src/excai/types/threads/runs/step_list_response.py">StepListResponse</a></code>

## Messages

Types:

```python
from excai.types.threads import (
    MessageCreateResponse,
    MessageRetrieveResponse,
    MessageUpdateResponse,
    MessageListResponse,
    MessageDeleteResponse,
)
```

Methods:

- <code title="post /threads/{thread_id}/messages">client.threads.messages.<a href="./src/excai/resources/threads/messages.py">create</a>(thread_id, \*\*<a href="src/excai/types/threads/message_create_params.py">params</a>) -> <a href="./src/excai/types/threads/message_create_response.py">MessageCreateResponse</a></code>
- <code title="get /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/excai/resources/threads/messages.py">retrieve</a>(message_id, \*, thread_id) -> <a href="./src/excai/types/threads/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="post /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/excai/resources/threads/messages.py">update</a>(message_id, \*, thread_id, \*\*<a href="src/excai/types/threads/message_update_params.py">params</a>) -> <a href="./src/excai/types/threads/message_update_response.py">MessageUpdateResponse</a></code>
- <code title="get /threads/{thread_id}/messages">client.threads.messages.<a href="./src/excai/resources/threads/messages.py">list</a>(thread_id, \*\*<a href="src/excai/types/threads/message_list_params.py">params</a>) -> <a href="./src/excai/types/threads/message_list_response.py">MessageListResponse</a></code>
- <code title="delete /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/excai/resources/threads/messages.py">delete</a>(message_id, \*, thread_id) -> <a href="./src/excai/types/threads/message_delete_response.py">MessageDeleteResponse</a></code>

# Uploads

Types:

```python
from excai.types import (
    UploadCreateResponse,
    UploadAddPartResponse,
    UploadCancelResponse,
    UploadCompleteResponse,
)
```

Methods:

- <code title="post /uploads">client.uploads.<a href="./src/excai/resources/uploads.py">create</a>(\*\*<a href="src/excai/types/upload_create_params.py">params</a>) -> <a href="./src/excai/types/upload_create_response.py">UploadCreateResponse</a></code>
- <code title="post /uploads/{upload_id}/parts">client.uploads.<a href="./src/excai/resources/uploads.py">add_part</a>(upload_id, \*\*<a href="src/excai/types/upload_add_part_params.py">params</a>) -> <a href="./src/excai/types/upload_add_part_response.py">UploadAddPartResponse</a></code>
- <code title="post /uploads/{upload_id}/cancel">client.uploads.<a href="./src/excai/resources/uploads.py">cancel</a>(upload_id) -> <a href="./src/excai/types/upload_cancel_response.py">UploadCancelResponse</a></code>
- <code title="post /uploads/{upload_id}/complete">client.uploads.<a href="./src/excai/resources/uploads.py">complete</a>(upload_id, \*\*<a href="src/excai/types/upload_complete_params.py">params</a>) -> <a href="./src/excai/types/upload_complete_response.py">UploadCompleteResponse</a></code>

# VectorStores

Types:

```python
from excai.types import (
    VectorStoreCreateResponse,
    VectorStoreRetrieveResponse,
    VectorStoreUpdateResponse,
    VectorStoreListResponse,
    VectorStoreDeleteResponse,
    VectorStoreSearchResponse,
)
```

Methods:

- <code title="post /vector_stores">client.vector_stores.<a href="./src/excai/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/excai/types/vector_store_create_params.py">params</a>) -> <a href="./src/excai/types/vector_store_create_response.py">VectorStoreCreateResponse</a></code>
- <code title="get /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/excai/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/excai/types/vector_store_retrieve_response.py">VectorStoreRetrieveResponse</a></code>
- <code title="post /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/excai/resources/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/excai/types/vector_store_update_params.py">params</a>) -> <a href="./src/excai/types/vector_store_update_response.py">VectorStoreUpdateResponse</a></code>
- <code title="get /vector_stores">client.vector_stores.<a href="./src/excai/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/excai/types/vector_store_list_params.py">params</a>) -> <a href="./src/excai/types/vector_store_list_response.py">VectorStoreListResponse</a></code>
- <code title="delete /vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/excai/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/excai/types/vector_store_delete_response.py">VectorStoreDeleteResponse</a></code>
- <code title="post /vector_stores/{vector_store_id}/search">client.vector_stores.<a href="./src/excai/resources/vector_stores/vector_stores.py">search</a>(vector_store_id, \*\*<a href="src/excai/types/vector_store_search_params.py">params</a>) -> <a href="./src/excai/types/vector_store_search_response.py">VectorStoreSearchResponse</a></code>

## FileBatches

Types:

```python
from excai.types.vector_stores import (
    FileBatchCreateResponse,
    FileBatchRetrieveResponse,
    FileBatchCancelResponse,
    FileBatchListFilesResponse,
)
```

Methods:

- <code title="post /vector_stores/{vector_store_id}/file_batches">client.vector_stores.file_batches.<a href="./src/excai/resources/vector_stores/file_batches.py">create</a>(vector_store_id, \*\*<a href="src/excai/types/vector_stores/file_batch_create_params.py">params</a>) -> <a href="./src/excai/types/vector_stores/file_batch_create_response.py">FileBatchCreateResponse</a></code>
- <code title="get /vector_stores/{vector_store_id}/file_batches/{batch_id}">client.vector_stores.file_batches.<a href="./src/excai/resources/vector_stores/file_batches.py">retrieve</a>(batch_id, \*, vector_store_id) -> <a href="./src/excai/types/vector_stores/file_batch_retrieve_response.py">FileBatchRetrieveResponse</a></code>
- <code title="post /vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel">client.vector_stores.file_batches.<a href="./src/excai/resources/vector_stores/file_batches.py">cancel</a>(batch_id, \*, vector_store_id) -> <a href="./src/excai/types/vector_stores/file_batch_cancel_response.py">FileBatchCancelResponse</a></code>
- <code title="get /vector_stores/{vector_store_id}/file_batches/{batch_id}/files">client.vector_stores.file_batches.<a href="./src/excai/resources/vector_stores/file_batches.py">list_files</a>(batch_id, \*, vector_store_id, \*\*<a href="src/excai/types/vector_stores/file_batch_list_files_params.py">params</a>) -> <a href="./src/excai/types/vector_stores/file_batch_list_files_response.py">FileBatchListFilesResponse</a></code>

## Files

Types:

```python
from excai.types.vector_stores import (
    FileCreateResponse,
    FileRetrieveResponse,
    FileUpdateResponse,
    FileListResponse,
    FileDeleteResponse,
    FileRetrieveContentResponse,
)
```

Methods:

- <code title="post /vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/excai/resources/vector_stores/files.py">create</a>(vector_store_id, \*\*<a href="src/excai/types/vector_stores/file_create_params.py">params</a>) -> <a href="./src/excai/types/vector_stores/file_create_response.py">FileCreateResponse</a></code>
- <code title="get /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/excai/resources/vector_stores/files.py">retrieve</a>(file_id, \*, vector_store_id) -> <a href="./src/excai/types/vector_stores/file_retrieve_response.py">FileRetrieveResponse</a></code>
- <code title="post /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/excai/resources/vector_stores/files.py">update</a>(file_id, \*, vector_store_id, \*\*<a href="src/excai/types/vector_stores/file_update_params.py">params</a>) -> <a href="./src/excai/types/vector_stores/file_update_response.py">FileUpdateResponse</a></code>
- <code title="get /vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/excai/resources/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/excai/types/vector_stores/file_list_params.py">params</a>) -> <a href="./src/excai/types/vector_stores/file_list_response.py">FileListResponse</a></code>
- <code title="delete /vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/excai/resources/vector_stores/files.py">delete</a>(file_id, \*, vector_store_id) -> <a href="./src/excai/types/vector_stores/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /vector_stores/{vector_store_id}/files/{file_id}/content">client.vector_stores.files.<a href="./src/excai/resources/vector_stores/files.py">retrieve_content</a>(file_id, \*, vector_store_id) -> <a href="./src/excai/types/vector_stores/file_retrieve_content_response.py">FileRetrieveContentResponse</a></code>
