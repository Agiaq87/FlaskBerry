from model.response.base_payload import BasePayload


class SimpleMessagePayload(BasePayload):
    def __init__(self, message: str):
        self.message = message

    def jsonify(self) -> {}:
        return self.__dict__

    def require_json_array(self) -> bool:
        return False
