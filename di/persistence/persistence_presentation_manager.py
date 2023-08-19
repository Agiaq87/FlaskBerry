from config.flask_berry_config import FlaskBerryConfig
from config.singleton import Singleton


class PersistencePresentationManager(metaclass=Singleton):
    def __init__(self):
        self._retrieveCounter = 0

    def check_try_presentation(self) -> bool:
        self._retrieveCounter += 1
        return self._retrieveCounter < FlaskBerryConfig().number_of_try_for_presentation()
