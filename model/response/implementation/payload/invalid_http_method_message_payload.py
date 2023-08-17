from model.response.base_payload import BasePayload


class InvalidHttpMethodMessagePayload(BasePayload):
    def jsonify(self) -> str:
        return "Invalid HTTP method"

    def require_json_array(self) -> bool:
        return False
