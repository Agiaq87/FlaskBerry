class BasePayload:
    def jsonify(self) -> {}:
        pass

    def require_json_array(self) -> bool:
        pass
