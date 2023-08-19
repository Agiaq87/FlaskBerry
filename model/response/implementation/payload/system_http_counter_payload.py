from di.system_counter.system_counter_manager import SystemCounterManager
from model.response.base_payload import BasePayload


class SystemHttpCounterPayload(BasePayload):

    def __init__(self):
        pass

    def jsonify(self) -> str:
        return SystemCounterManager().to_json()

    def require_json_array(self) -> bool:
        return False

