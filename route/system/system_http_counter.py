from flask.views import MethodView
from flask_smorest import Blueprint

from model.response.implementation.payload.invalid_http_method_message_payload import InvalidHttpMethodMessagePayload
from model.response.implementation.payload.system_http_counter_payload import SystemHttpCounterPayload
from model.response.implementation.response.restricted_info_response import RestrictedInfoResponse
from model.response.implementation.response.standard_info_response import StandardInfoResponse
from route.base_route import BaseRoute

system_http_counter_blueprint = Blueprint("counter", __name__, description="system http counter")


@system_http_counter_blueprint.route("/system/counter")
class SystemHttpCounterBlueprint(MethodView, BaseRoute):
    def connect(self, data: str | None):
        super().connect(data)
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def delete(self):
        super().delete()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def get(self):
        super().get()
        return StandardInfoResponse(SystemHttpCounterPayload()).to_json()

    def head(self):
        super().head()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def options(self):
        super().options()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def patch(self):
        super().patch()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def post(self):
        super().post()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def put(self):
        super().put()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def trace(self):
        super().trace()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()
