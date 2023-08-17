import pickle

from config.singleton import Singleton


class PersistenceManager(metaclass=Singleton):

    def __init__(self):
        self._db = None
        self._db_name = None

    def setup_db(self):
        self._db_name = "FlaskBerryPersistence.fs"
        self._db = open(self._db_name, "wb")

    def register_guest(self, name: str, ip: str):
        pickle.dumps()

    def is_unknown_user(self, name: str) -> bool:
        return self.db[name] is None
