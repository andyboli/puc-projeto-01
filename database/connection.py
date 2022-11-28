import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)
from controller import (reader)
from database import (constants, queries)


def connect():
    try:
        print(reader.lang('database_connect_start'))
        connection = mysql.connector.connect(**constants.CONFIG)
        if connection.is_connected():
            print(reader.lang('database_connect_done').format(
                connection.get_server_info()))
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(reader.lang('database_connect_crendentials_error'))
        else:
            print(reader.lang('database_connect_error').format(err))
        exit(1)


def close(connection: MySQLConnection):
    if connection.is_connected():
        connection.close()
    print(reader.lang('database_connect_close'))


def run():
    connection = connect()
    queries.create_database(connection)
    queries.create_tables(connection)
    homeless_data_raw = reader.read_data(table='homeless')
    homeless_data = reader.map_homeless_data(data=homeless_data_raw)
    queries.insert_table(connection=connection,
                         table='homeless', data=homeless_data)
    close(connection)
