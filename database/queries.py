import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)
from controller import (reader)
import database.constants as constants


def create_database(cnx: MySQLConnection):
    try:
        cursor = cnx.cursor()
        cursor.execute(
            constants.CREATE_DATABASE_QUERY.format(constants.DB_NAME))
        cnx.database = constants.DB_NAME
    except mysql.connector.Error as err:
        if err.errno != errorcode.ER_DB_CREATE_EXISTS:
            print(reader.lang('database_create_error').format(err))
    else:
        print(reader.lang('database_create_done').format(constants.DB_NAME))
    finally:
        cursor.close()


def create_tables(cnx: MySQLConnection):
    try:
        cursor = cnx.cursor()
        for table_name in constants.TABLES:
            table_description = constants.TABLE[table_name]
            cursor.execute(table_description)
    except mysql.connector.Error as err:
        print(reader.lang('database_create_tables_error').format(err))
        exit(1)
    else:
        print(reader.lang('database_create_tables_done').format(err))
        cursor.close()
