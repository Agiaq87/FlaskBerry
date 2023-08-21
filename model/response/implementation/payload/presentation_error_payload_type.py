from enum import Enum


class PresentationPayloadType(Enum):
    # Error
    ARGS_NOT_PRESENT = "All presentation require client send an unique identifier",
    INCORRECT_ARGS = "Incorrect unique identifier",
    ARGS_NOT_EQ = "Unique identifier detected not equals to args",
    MAXIMUM_NUMBER_OF_TRY = "Three is out."

    # Warning
    ALREADY_ATTEMPT_FIRST_STEP = "Already complete first step, continue"

    # OK
    FIRST_STEP_GET_OK = "Accomplished first step, continue"
