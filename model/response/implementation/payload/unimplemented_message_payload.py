from model.response.base_payload import BasePayload


class UnimplementedMessagePayload(BasePayload):
    def jsonify(self) -> str:
        return "Unimplemented"

    def require_json_array(self) -> bool:
        return False
