from enum import Enum


class UserTaskType(str, Enum):
    DATASET_PROCESSING = "dataset_processing"
    INFERENCER = "inferencer"
    TRAINER = "trainer"

    def __str__(self) -> str:
        return str(self.value)
