import sqlite3

from config.db_constants import DbConstants
from config.singleton import Singleton


class PersistenceManager(metaclass=Singleton):

    def __init__(self):
        self._db = sqlite3.connect("FlaskBerryPersistence.sqlite")
        self._cursor = self._db.cursor()
        self._cursor.execute(
            "CREATE TABLE IF NOT EXISTS {}(id INT PRIMARY KEY, user_name TEXT, user_address TEXT);".format(
                DbConstants.USER_ACCESS_TABLE.value))

    def setup_db(self):
        pass

    def register_guest(self, name: str, ip: str):
        pass

    def is_unknown_user(self, name: str) -> bool:
        return self.db[name] is None
