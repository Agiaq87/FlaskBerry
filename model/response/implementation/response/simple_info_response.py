import datetime as dt
import json
from config.flask_berry_config import FlaskBerryConfig
from model.response.base_payload import BasePayload
from model.response.base_response import BaseResponse


class SimpleInfoResponse(BaseResponse):
    def __init__(self, payload: BasePayload):
        config = FlaskBerryConfig()
        self.datetime = dt.datetime.now().__str__()
        self.version = config.version()
        self.response_num = config.handle_response_number()
        if payload.require_json_array():
            self.payload = [payload.jsonify()]
        else:
            self.payload = payload.jsonify()
        pass

    def to_json(self):
        return json.dumps(self.__dict__)
