"""
Database creator with <pymssql> wheel
"""
import pymssql
from db.db_creator import DbCreator

class MSSQLServerDbCreator(DbCreator):
    """Class SQLServerDbCreator - concrete abstract class"""

    def __init__(self, arg) -> None:
        super().__init__("")
        self._entity = arg
        print(self._entity.server)

    # def __init__(self, entity) -> None:
    #     super.__init__("")
    #     self._entity = entity

    def db_factory(self):
        """
            Function implement db_factory method
            - Connect string example: <'127.0.0.1', 'username', 'password', 'database'>
            - Connect string example: <'DRIVER={ODBC Driver 13 for SQL Server};SERVER=127.0.0.1;DATABASE=freshwater;UID=username;PWD=password'>
        """
        # self._db_connection = None
        print(self._db_connection)
        self._db_connection = pymssql.connect(host='10.203.224.55', user='sa', password='emcnsupport', database='seabass')
        # self._db_connection = pymssql.connect(
        #     self._entity.server, self._entity.username, 
        #     self._entity.password, self._entity.database) 
        return self._db_connection
