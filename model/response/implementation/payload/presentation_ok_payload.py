from model.response.base_payload import BasePayload
from model.response.implementation.payload.presentation_error_payload_type import PresentationPayloadType


class PresentationOkPayload(BasePayload):
    def __init__(self, presentation_type: PresentationPayloadType):
        self.message = presentation_type.value

    def jsonify(self) -> {}:
        return self.__dict__

    def require_json_array(self) -> bool:
        return False
