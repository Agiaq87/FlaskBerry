from sqlite3 import Connection

from config.singleton import Singleton


class PersistenceSessionManager(metaclass=Singleton):

    def __init__(self, connection: Connection):
        self._db = connection
        self._cursor = self._db.cursor()
        self._cursor.execute("CREATE TABLE IF NOT EXISTS ")
