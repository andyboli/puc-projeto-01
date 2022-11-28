import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)
from controller import (reader)
from database import (constants, queries)


def connect():
    try:
        connection = mysql.connector.connect(**constants.DB_CONFIG)
        if connection.is_connected():
            return connection, reader.lang('database_connect_done').format(
                connection.get_server_info()), None
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return None, None, reader.lang('database_connect_crendentials_error')
        else:
            return None, None, reader.lang('database_connect_error').format(err)


def close(connection: MySQLConnection):
    if connection.is_connected():
        connection.close()
    return reader.lang('database_connect_close')


def run():
    yield reader.lang('database_connect_start'), None
    connection, message, error = connect()
    yield message, error

    yield reader.lang(
        'database_create_database_start').format(constants.DB_NAME), None
    message, error = queries.create_database(connection)

    yield message, error

    yield reader.lang('database_create_tables_start'), None
    message, error = queries.create_tables(connection)
    yield message, error

    yield reader.lang('reader_read_data_start').format('assets/csv/{}'.format('homeless')), None
    homeless_data_raw, message, error = reader.read_data(table='homeless')
    yield message, error

    yield reader.lang('reader_map_data_start').format('assets/csv/{}'.format('homeless')), None
    homeless_data, message, error = reader.map_homeless_data(
        data=homeless_data_raw)
    yield message, error

    data_range = reader.data_range(homeless_data)

    yield reader.lang('database_insert_table_start').format('homeless'), None
    message, error = queries.insert_table(connection=connection,
                                          table='homeless', data=homeless_data)
    yield message, error

    message = close(connection)
    yield message
