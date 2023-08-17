from abc import ABC
from typing import Optional

from flask import request

from di.persistence.persistence_manager import PersistenceManager
from di.system_counter.system_counter_manager import SystemCounterManager
from model.http.http_methods import HttpMethod
from model.response.implementation.payload.present_yourself_payload import PresentYourselfPayload
from model.response.implementation.response.restricted_info_response import RestrictedInfoResponse


class BaseRoute(ABC):

    def __init__(self):
        self._systemManagerCounter = SystemCounterManager()
        self._persistence = PersistenceManager()

    def connect(self, data: Optional[str]):
        self._systemManagerCounter.increment(HttpMethod.CONNECT)
        pass

    def delete(self):
        self._systemManagerCounter.increment(HttpMethod.DELETE)
        pass

    def get(self):
        if self._persistence.is_unknown_user(request.remote_user):
            return RestrictedInfoResponse(PresentYourselfPayload()).to_json()
        self._systemManagerCounter.increment(HttpMethod.GET)
        pass

    def head(self):
        self._systemManagerCounter.increment(HttpMethod.HEAD)
        pass

    def options(self):
        self._systemManagerCounter.increment(HttpMethod.OPTIONS)
        pass

    def patch(self):
        self._systemManagerCounter.increment(HttpMethod.PATCH)
        pass

    def post(self):
        self._systemManagerCounter.increment(HttpMethod.POST)
        pass

    def put(self):
        self._systemManagerCounter.increment(HttpMethod.PUT)
        pass

    def trace(self):
        self._systemManagerCounter.increment(HttpMethod.TRACE)
        pass
