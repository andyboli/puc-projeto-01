import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)
from reader import (json)
import database.constants as constants

def connect():
    print(json.lang('database_connect'))
    try:
        cnx = mysql.connector.connect(**constants.CONFIG)
        print(json.lang('database_connect_done'))
        return cnx
    except mysql.connector.Error as err:
        print(json.lang('database_connect_error'))
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(json.lang('database_connect_error_crendentials'))
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(json.lang('database_connect_error_database'))
        else:
            print(err)
        exit(1)

def close(cnx: MySQLConnection):
    cnx.close()
    print(json.lang('database_connect_close'))












