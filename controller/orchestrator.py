from controller.mapper import map_homeless_data
from controller.reader import lang, read_data
from database.connection import connect_database, create_database, create_tables, insert_table, drop_database, close_database
from database.constants import DB_NAME


def connect_app_iterator():
    """ create database connection
    connection: mysql oppened connection
    message: success message
    error: error message

    return connection: MySQLConnection | None, message: str | None, error: str | None
    """
    connection, message, error = connect_database()
    while True:
        yield connection, message, error


connect_app = connect_app_iterator()


start_app_iterations = 12


def start_app_iterator():
    """ create database, create tables, read homeless data, map homeless data and insert homeless data in homeless table
    data_range: return homeless data range with all distinct values and headers
    success: success message
    loading: loading message
    error: error message

    return success: str, loading: str, error: str
    """
    yield '', lang('database_connect_start'), ''
    connection, success, error = next(connect_app)
    yield success, '', error

    yield '', lang(
        'database_create_database_start').format(DB_NAME), ''
    success, error = create_database(connection)
    yield success, '', error

    yield '', lang('database_create_tables_start'), ''
    success, error = create_tables(connection)
    yield success, '', error

    yield '', lang('read_data_start').format('assets/csv/{}'.format('homeless')), ''
    homeless_data_raw, success, error = read_data(table='homeless')
    yield success, '', error

    yield '', lang('map_data_start').format('assets/csv/{}'.format('homeless')), ''
    homeless_data, success, error = map_homeless_data(
        data=homeless_data_raw)
    yield success, '', error

    yield '', lang('database_insert_table_start').format('homeless'), ''
    success, error = insert_table(connection=connection,
                                  table='homeless', data=homeless_data)
    yield success, '', error


start_app = start_app_iterator()


def end_app_iterator():
    """ drop database and close connection
    success: success message
    error: error message

    return success: str, error: str
    """
    try:
        start_app.close()
        connection, _, _ = next(connect_app)
        success, error = drop_database(connection)
        yield success, error
        success = close_database(connection)
        yield success, ''
    except:
        yield '', lang("end_app_error")


end_app = end_app_iterator()


def select_app_iterator():
    yield 'select_app'
