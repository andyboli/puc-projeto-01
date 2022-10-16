import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)
from controller import (reader)
from database import (constants)


def create_database(connection: MySQLConnection):
    try:
        print(reader.lang('database_create_database_start').format(constants.DB_NAME))
        cursor = connection.cursor()
        cursor.execute(
            constants.CREATE_DATABASE_QUERY.format(constants.DB_NAME))
        connection.database = constants.DB_NAME
    except mysql.connector.Error as err:
        if err.errno != errorcode.ER_DB_CREATE_EXISTS:
            print(reader.lang('database_create_database_error').format(err))
            exit(1)
    else:
        print(reader.lang('database_create_database_done').format(constants.DB_NAME))
    finally:
        cursor.close()
