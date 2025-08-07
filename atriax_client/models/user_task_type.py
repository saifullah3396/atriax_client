from enum import Enum


class UserTaskType(str, Enum):
    EVALUATION = "evaluation"

    def __str__(self) -> str:
        return str(self.value)
