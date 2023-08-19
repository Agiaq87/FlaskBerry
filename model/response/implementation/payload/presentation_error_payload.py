from model.response.base_payload import BasePayload
from model.response.implementation.payload.presentation_error_payload_type import PresentationErrorPayloadType


class PresentationErrorPayload(BasePayload):
    def __init__(self, presentation_type: PresentationErrorPayloadType):
        match presentation_type:
            case PresentationErrorPayloadType.ARGS_NOT_PRESENT:
                self.message = "All presentation require client send an unique identifier"
            case PresentationErrorPayloadType.MAXIMUM_NUMBER_OF_TRY:
                self.message = "Three is out."
            case PresentationErrorPayloadType.INCORRECT_ARGS:
                self.message = "Incorrect unique identifier"
            case PresentationErrorPayloadType.ARGS_NOT_EQ:
                self.message = "Unique identifier detected not equals to args"

    def jsonify(self) -> {}:
        return self.__dict__

    def require_json_array(self) -> bool:
        return False
