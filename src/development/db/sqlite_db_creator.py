"""
Concrete DbCreator override the factory method for SQLite database
"""
# import pymssql
import sqlite3
from db.db_creator import DbCreator

class SQLiteDbCreator(DbCreator):
    """Class SQLiteDbCreator - concrete abstract class"""

    def db_factory(self):
        """
            Function implement db_factory method
            - Connect string example: <'127.0.0.1', 'username', 'password', 'database'>
            - Connect string example: <'DRIVER={ODBC Driver 13 for SQL Server};SERVER=127.0.0.1;DATABASE=freshwater;UID=username;PWD=password'>
        """
        # self._db_connection = None
        # self._db_connection = pymssql.connect('10.203.224.55','sa','emcnsupport','seabass')
        self._db_connection = sqlite3.connect(self.conn_str) 
        return self._db_connection
