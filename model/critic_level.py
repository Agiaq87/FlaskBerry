from enum import Enum


class CriticLevel(Enum):
    INFO = 0
    LOW = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4
    FAILURE = 5
