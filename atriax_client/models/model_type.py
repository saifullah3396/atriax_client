from enum import Enum


class ModelType(str, Enum):
    DIFFUSERS = "diffusers"
    MMDET = "mmdet"
    TIMM = "timm"
    TORCHVISION = "torchvision"
    TRANSFORMERSIMAGE_CLASSIFICATION = "transformers/image_classification"
    TRANSFORMERSQUESTION_ANSWERING = "transformers/question_answering"
    TRANSFORMERSSEQUENCE_CLASSIFICATION = "transformers/sequence_classification"
    TRANSFORMERSTOKEN_CLASSIFICATION = "transformers/token_classification"

    def __str__(self) -> str:
        return str(self.value)
