from enum import Enum


class PresentationErrorPayloadType(Enum):
    ARGS_NOT_PRESENT = 2,
    INCORRECT_ARGS = 3,
    ARGS_NOT_EQ = 4,
    MAXIMUM_NUMBER_OF_TRY = 100,
    PERMABAN = 111
