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

    def number_of_try_for_presentation(self) -> int:
        return 3

    def number_for_permaban(self) -> int:
        return 3

    def delay_of_try_for_presentation(self) -> int:
        return 5

    def delta_for_delay_try_presentation(self, counted: int) -> float:
        default = self.number_of_try_for_presentation()
        if default < counted < (default * 2):
            return 1.5

        if (default * 2) < counted < (default * 3):
            return 2.5

        if (default * 3) < counted < (default * 4):
            return 5

        if (default * 4) < counted < (default * 5):
            return 10
        else:
            return 100
