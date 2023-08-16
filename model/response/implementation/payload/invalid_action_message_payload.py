from model.response.base_payload import BasePayload


class InvalidActionMessagePayload(BasePayload):
    def jsonify(self) -> str:
        return "Invalid action"

    def require_json_array(self) -> bool:
        return False
