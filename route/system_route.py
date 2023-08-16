from typing import Optional

from flask.views import MethodView
from flask_smorest import Blueprint

from model.response.implementation.response.simple_info_response import SimpleInfoResponse
from model.response.implementation.payload.system_info_payload import SystemInfoPayload
from model.response.implementation.payload.unimplemented_message_payload import UnimplementedMessagePayload
from route.base_route import BaseRoute

system_blueprint = Blueprint("system", __name__, description="system information")


@system_blueprint.route("/system")
class SystemBlueprint(MethodView, BaseRoute):

    def connect(self, data: Optional[Optional[str]]) -> str:
        return SimpleInfoResponse(UnimplementedMessagePayload()).to_json()

    def delete(self) -> str:
        return SimpleInfoResponse(UnimplementedMessagePayload()).to_json()

    def head(self):
        pass

    def get(self) -> str:
        return SimpleInfoResponse(SystemInfoPayload()).to_json()

    def options(self) -> str:
        pass

    def patch(self) -> str:
        pass

    def post(self) -> str:
        pass

    def put(self) -> str:
        pass

    def trace(self) -> str:
        pass
