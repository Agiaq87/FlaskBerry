from typing import Optional

from flask.views import MethodView
from flask_smorest import Blueprint

from model.response.implementation.payload.invalid_http_method_message_payload import InvalidHttpMethodMessagePayload
from model.response.implementation.response.restricted_info_response import RestrictedInfoResponse
from model.response.implementation.response.standard_info_response import StandardInfoResponse
from model.response.implementation.payload.system_info_payload import SystemInfoPayload
from model.response.implementation.payload.unimplemented_message_payload import UnimplementedMessagePayload
from route.base_route import BaseRoute

system_blueprint = Blueprint("system", __name__, description="system information")


@system_blueprint.route("/system")
class SystemBlueprint(MethodView, BaseRoute):

    def connect(self, data: str | None) -> str:
        super().connect(data)
        return StandardInfoResponse(UnimplementedMessagePayload()).to_json()

    def delete(self) -> str:
        super().delete()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def head(self):
        super().head()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def get(self) -> str:
        super().get()
        return StandardInfoResponse(SystemInfoPayload()).to_json()

    def options(self) -> str:
        super().options()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def patch(self) -> str:
        super().patch()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def post(self) -> str:
        super().post()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def put(self) -> str:
        super().put()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def trace(self) -> str:
        super().trace()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()
