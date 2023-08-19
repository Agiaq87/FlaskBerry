from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

from di.persistence.persistence_presentation_manager import PersistenceUserSessionManager
from model.response.implementation.payload.invalid_http_method_message_payload import InvalidHttpMethodMessagePayload
from model.response.implementation.payload.presentation_error_payload import PresentationErrorPayload
from model.response.implementation.payload.presentation_error_payload_type import PresentationErrorPayloadType
from model.response.implementation.response.restricted_info_response import RestrictedInfoResponse
from model.state.user_session_state import UserSessionState
from route.base_route import BaseRoute
from util.net_converter import mac_from_ip
from util.regex_validator import check_mac_address

presentation_blueprint = Blueprint("presentation", __name__, description="presentation")


@presentation_blueprint.route("/presentation")
class PresentationBlueprint(MethodView, BaseRoute):

    def __init__(self):
        super().__init__()
        self._requestCounter = 0
        self._macAddress = None
        self._persistence = PersistenceUserSessionManager()

    def connect(self, data: str | None):
        super().connect(data)
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def delete(self):
        super().delete()
        return RestrictedInfoResponse(InvalidHttpMethodMessagePayload()).to_json()

    def get(self) -> str:
        super().get()
        mac_address_client = request.args.get('mac')
        mac_address_read = mac_from_ip(request.remote_addr)
        print(mac_address_client)
        print(mac_address_read)

        # Check for perma ban
        if self._persistence.check_is_perma_ban(request.remote_addr):
            return ""

        # Check if presentation have correct argument
        if mac_address_client is None:
            return self.persistence_user_session_response(
                PresentationErrorPayloadType.ARGS_NOT_PRESENT,
                PresentationErrorPayloadType.MAXIMUM_NUMBER_OF_TRY
            )

        # Check if client mac is okay with regex
        if not check_mac_address(mac_address_client):
            return self.persistence_user_session_response(
                PresentationErrorPayloadType.INCORRECT_ARGS,
                PresentationErrorPayloadType.MAXIMUM_NUMBER_OF_TRY
            )

        # Check if mac client equals retrieved mac
        if not mac_address_read == mac_from_ip(mac_address_client):
            return self.persistence_user_session_response(
                PresentationErrorPayloadType.ARGS_NOT_EQ,
                PresentationErrorPayloadType.MAXIMUM_NUMBER_OF_TRY
            )

        # First session ok
        self._persistence.register_correct_presentation(mac_address_client)

        return "OK"

    def head(self):
        super().head()

    def options(self):
        super().options()

    def patch(self):
        super().patch()

    def post(self):
        super().post()

        if not self._persistence.check_is_correct_presentation(request.remote_addr):
            return self.persistence_user_session_response(
                PresentationErrorPayloadType.ARGS_NOT_PRESENT,
                PresentationErrorPayloadType.MAXIMUM_NUMBER_OF_TRY
            )


    def put(self):
        super().put()

    def trace(self):
        super().trace()

    def persistence_user_session_response(self, shadow_ban: PresentationErrorPayloadType,
                                          ban: PresentationErrorPayloadType):
        match self._persistence.register_incident(request.remote_addr):
            case UserSessionState.SHADOW_BAN:
                return RestrictedInfoResponse(
                    PresentationErrorPayload(shadow_ban)
                ).to_json()
            case UserSessionState.BAN:
                return RestrictedInfoResponse(
                    PresentationErrorPayload(ban)
                ).to_json()
            case UserSessionState.PERMA_BAN:
                return ""
