from enum import Enum


class DatasetProcessingRequestTypes(str, Enum):
    PREPARE_SHARDS = "prepare_shards"
    PROCESS_SHARDS = "process_shards"

    def __str__(self) -> str:
        return str(self.value)
