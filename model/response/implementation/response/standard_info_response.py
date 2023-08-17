import datetime as dt
import json
from config.flask_berry_config import FlaskBerryConfig
from model.response.base_payload import BasePayload
from model.response.base_response import BaseResponse
from model.system_counter.system_counter_manager import SystemCounterManager


class StandardInfoResponse(BaseResponse):
    def __init__(self, payload: BasePayload):
        config = FlaskBerryConfig()
        self.datetime = dt.datetime.now().__str__()
        self.version = config.version()
        self.response_num = SystemCounterManager().read()
        if payload.require_json_array():
            self.payload = [payload.jsonify()]
        else:
            self.payload = payload.jsonify()

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
