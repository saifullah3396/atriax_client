from enum import Enum


class UserTaskStatus(str, Enum):
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
