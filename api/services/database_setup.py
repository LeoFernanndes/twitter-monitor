import mysql.connector
from decouple import config


def mysql_rds_database_authentication(host, user, port, password, database):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        port=port,
        password=password,
        database=database
    )
    return mydb


mydb = mysql_rds_database_authentication(
    config('DB_HOST'),
    config('DB_USER'),
    config('DB_PORT'),
    config('DB_PASSWORD'),
    config('DB_DATABASE')
)
cursor = mydb.cursor()
