from model.response.base_payload import BasePayload


class PresentYourselfPayload(BasePayload):
    def jsonify(self) -> str:
        return "Present yourself if you want to interact with me"

    def require_json_array(self) -> bool:
        return False
