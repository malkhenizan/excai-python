# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .costs_result import CostsResult
from .usage_images_result import UsageImagesResult
from .usage_embeddings_result import UsageEmbeddingsResult
from .usage_completions_result import UsageCompletionsResult
from .usage_moderations_result import UsageModerationsResult
from .usage_vector_stores_result import UsageVectorStoresResult
from .usage_audio_speeches_result import UsageAudioSpeechesResult
from .usage_audio_transcriptions_result import UsageAudioTranscriptionsResult
from .usage_code_interpreter_sessions_result import UsageCodeInterpreterSessionsResult

__all__ = ["UsageTimeBucket", "Result"]

Result: TypeAlias = Annotated[
    Union[
        UsageCompletionsResult,
        UsageEmbeddingsResult,
        UsageModerationsResult,
        UsageImagesResult,
        UsageAudioSpeechesResult,
        UsageAudioTranscriptionsResult,
        UsageVectorStoresResult,
        UsageCodeInterpreterSessionsResult,
        CostsResult,
    ],
    PropertyInfo(discriminator="object"),
]


class UsageTimeBucket(BaseModel):
    end_time: int

    object: Literal["bucket"]

    result: List[Result]

    start_time: int
