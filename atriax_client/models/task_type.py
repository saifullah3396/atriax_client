from enum import Enum


class TaskType(str, Enum):
    IMAGE_CLASSIFICATION = "image_classification"
    LAYOUT_ANALYSIS = "layout_analysis"
    LAYOUT_ENTITY_RECOGNITION = "layout_entity_recognition"
    QUESTION_ANSWERING = "question_answering"
    SEMANTIC_ENTITY_RECOGNITION = "semantic_entity_recognition"
    SEQUENCE_CLASSIFICATION = "sequence_classification"
    VISUAL_QUESTION_ANSWERING = "visual_question_answering"

    def __str__(self) -> str:
        return str(self.value)
