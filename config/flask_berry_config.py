from config.singleton import Singleton


class FlaskBerryConfig(metaclass=Singleton):
    _num_of_response: int

    def __init__(self):
        self._version = 0.1
        self._num_of_response = 0

    def version(self) -> float:
        return self._version

    def handle_response_number(self) -> int:
        self._num_of_response += 1
        return self._num_of_response
