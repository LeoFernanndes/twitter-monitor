import mysql.connector
import abc


class BaseTwitterDatabaseManager(abc.ABC):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def set_up(self):
        pass





def mysql_rds_database_authentication(host, user, port, password, database):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        port=port,
        password=password,
        database=database
    )
    return mydb
