import json

from config.singleton import Singleton
from model.http.http_methods import HttpMethod


# Singleton class
class SystemCounterManager(object, metaclass=Singleton):
    def __init__(self):
        self.total = 0
        self.httpCounter = {
            'ok': 0, 'error': 0, 'redirect': 0
        }
        self.httpMethodCounter = {
            'CONNECT': 0,
            'DELETE': 0,
            'GET': 0,
            'HEAD': 0,
            'OPTIONS': 0,
            'PATCH': 0,
            'POST': 0,
            'PUT': 0,
            'TRACE': 0
        }

    def read(self) -> int:
        return self.total

    def increment(self, http_method: HttpMethod | None = None) -> int:
        self.total += 1
        self.httpCounter['ok'] += 1

        if http_method is not None:
            self.httpMethodCounter[http_method.name] += 1

        return self.total

    def to_json(self) -> str:
        return json.dumps(self.__dict__).replace("\"", "")
