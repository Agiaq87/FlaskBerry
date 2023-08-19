from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

from di.persistence.persistence_presentation_manager import PersistencePresentationManager
from model.response.implementation.payload.invalid_http_method_message_payload import InvalidHttpMethodMessagePayload
from model.response.implementation.payload.presentation_error_payload import PresentationErrorPayload
from model.response.implementation.payload.presentation_error_payload_type import PresentationErrorPayloadType
from model.response.implementation.response.restricted_info_response import RestrictedInfoResponse
from route.base_route import BaseRoute

presentation_blueprint = Blueprint("presentation", __name__, description="presentation")


@presentation_blueprint.route("/presentation")
class PresentationBlueprint(MethodView, BaseRoute):

    def __init__(self):
        super().__init__()
        self._requestCounter = 0
        self._macAddress = None

    def connect(self, data: str | None):
        super().connect(data)
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def delete(self):
        super().delete()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def get(self) -> str:
        super().get()
        mac_address = request.args.get('mac')

        if not PersistencePresentationManager().check_try_presentation():
            return RestrictedInfoResponse(
                PresentationErrorPayload(PresentationErrorPayloadType.REQUEST_ERROR_TRY)).to_json()

        if mac_address is None:
            return RestrictedInfoResponse(
                PresentationErrorPayload(PresentationErrorPayloadType.MAC_ADDRESS_NOT_DEFINED)).to_json()

    def head(self):
        super().head()

    def options(self):
        super().options()

    def patch(self):
        super().patch()

    def post(self):
        super().post()

    def put(self):
        super().put()

    def trace(self):
        super().trace()
