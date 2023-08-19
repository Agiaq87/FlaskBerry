from abc import ABC

from di.persistence.persistence_manager import PersistenceManager
from di.system_counter.system_counter_manager import SystemCounterManager
from model.http.http_methods import HttpMethod


class BaseRoute(ABC):

    def __init__(self):
        self._systemManagerCounter = SystemCounterManager()
        self._persistence = PersistenceManager()

    def connect(self, data: str | None):
        self._systemManagerCounter.increment(HttpMethod.CONNECT)
        pass

    def delete(self):
        self._systemManagerCounter.increment(HttpMethod.DELETE)
        pass

    def get(self):
        # if self._persistence.is_unknown_user(request.remote_user):
        #    return RestrictedInfoResponse(PresentYourselfPayload()).to_json()
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
