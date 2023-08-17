from abc import ABC, abstractmethod
from typing import Optional

from model.http.http_methods import HttpMethod
from model.system_counter.system_counter_manager import SystemCounterManager


class BaseRoute(ABC):

    def __init__(self):
        self._systemManagerCounter = SystemCounterManager()

    def connect(self, data: Optional[str]):
        self._systemManagerCounter.increment(HttpMethod.CONNECT)
        pass

    def delete(self):
        self._systemManagerCounter.increment(HttpMethod.DELETE)
        pass

    def get(self):
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
