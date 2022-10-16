import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)
from controller import (reader)
import database.constants as constants


def connect():
    print(reader.lang('database_connect'))
    try:
        cnx = mysql.connector.connect(**constants.CONFIG)
        print(reader.lang('database_connect_done'))
        return cnx
    except mysql.connector.Error as err:
        print(reader.lang('database_connect_error'))
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(reader.lang('database_connect_error_crendentials'))
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(reader.lang('database_connect_error_database'))
        else:
            print(err)
        exit(1)


def close(cnx: MySQLConnection):
    cnx.close()
    print(reader.lang('database_connect_close'))


def run():
    cnx = connect()
    data = reader.read_data()
    print("DATA \n", data)
    close(cnx)
