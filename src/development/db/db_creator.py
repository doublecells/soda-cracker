"""
Database factory method
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class DbCreator(ABC):
    """Class DbCreator - an abstract class"""
    def __init__(self, arg) -> None:
        self._db_connection = None
        self.conn_str = arg

    @abstractmethod
    def db_factory(self):
        pass

    """Method connection - database connection"""
    def connection(self):
        # db_entity = self.db_factory()
        # return db_entity.cursor()
        return self.db_factory().cursor()
    
    def commit(self):
        self._db_connection.commit()
    
    def __del__(self):
        print("Clean up the database connections.")
        if self._db_connection is not None: self._db_connection.close()
        self._db_connection = None
