import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)
from controller import (reader)
from database import (constants, queries)


def connect():
    print(reader.lang('database_connect'))
    try:
        cnx = mysql.connector.connect(**constants.CONFIG)
        if cnx.is_connected():
            print(reader.lang('database_connect_done').format(
                cnx.get_server_info()))
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
    if cnx.is_connected():
        cnx.close()
    print(reader.lang('database_connect_close'))


def run():
    cnx = connect()
    data = reader.read_data()
    print("DATA \n", data)
    queries.create_database(cnx)
    close(cnx)
