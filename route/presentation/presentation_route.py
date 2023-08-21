from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

from di.persistence.persistence_presentation_manager import PersistenceUserSessionManager
from model.http.http_methods import HttpMethod
from model.response.implementation.payload.invalid_http_method_message_payload import InvalidHttpMethodMessagePayload
from model.response.implementation.payload.presentation_error_payload import PresentationErrorPayload
from model.response.implementation.payload.presentation_error_payload_type import PresentationPayloadType
from model.response.implementation.payload.presentation_ok_payload import PresentationOkPayload
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
                None,
                PresentationPayloadType.ARGS_NOT_PRESENT,
                PresentationPayloadType.MAXIMUM_NUMBER_OF_TRY
            )

        # Check if client mac is okay with regex
        if not check_mac_address(mac_address_client):
            return self.persistence_user_session_response(
                None,
                PresentationPayloadType.INCORRECT_ARGS,
                PresentationPayloadType.MAXIMUM_NUMBER_OF_TRY
            )

        # Check if mac client equals retrieved mac
        if not mac_address_read == mac_address_client:
            return self.persistence_user_session_response(
                None,
                PresentationPayloadType.ARGS_NOT_EQ,
                PresentationPayloadType.MAXIMUM_NUMBER_OF_TRY
            )

        # First session ok, count how much try user attempt and it's first try
        self._persistence.register_correct_presentation(mac_address_client, HttpMethod.GET)

        return self.persistence_user_session_response(
            PresentationPayloadType.FIRST_STEP_GET_OK,
            PresentationPayloadType.ALREADY_ATTEMPT_FIRST_STEP,
            PresentationPayloadType.MAXIMUM_NUMBER_OF_TRY
        )

    def head(self):
        super().head()

    def options(self):
        super().options()

    def patch(self):
        super().patch()

    def post(self):
        super().post()

        # Check if first step it's ok
        if not self._persistence.check_is_correct_presentation(request.remote_addr):
            return self.persistence_user_session_response(
                None,
                PresentationPayloadType.ARGS_NOT_PRESENT,
                PresentationPayloadType.MAXIMUM_NUMBER_OF_TRY
            )

        # obtain post and check:
        # 1) calculated time
        # 2) device's name
        # 3) mac address
        post = request.form



    def put(self):
        super().put()

    def trace(self):
        super().trace()

    def persistence_user_session_response(
            self,
            ok: PresentationPayloadType | None,
            shadow_ban: PresentationPayloadType,
            ban: PresentationPayloadType
    ):
        match self._persistence.register_incident(request.remote_addr):
            case UserSessionState.OK:
                return RestrictedInfoResponse(
                    PresentationOkPayload(ok)
                )
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
