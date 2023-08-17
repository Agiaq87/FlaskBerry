import json
from typing import Optional

from model.response.base_payload import BasePayload
from model.response.base_response import BaseResponse


class RestrictedInfoResponse(BaseResponse):
    def __init__(self, payload: BasePayload, info: str | None = None):
        if payload.require_json_array():
            self.message = [payload.jsonify()]
        else:
            self.message = payload.jsonify()
        if info is not None:
            self.info = info

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
