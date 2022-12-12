from controller.mapper import map_homeless_data
from controller.reader import lang, read_data
from database.connection import close_connection, connect_mysql, create_database, create_table, drop_database, get_query, insert_table, select_table
from database.constants import PUC_DB, PUC_DB_HOMELESS


max_start_app_iterations = 12


def start_app_iterator():
    """Calls create_database, create_table, read_data, map_homeless_data and insert_table with default values.

    Yields:
        success (str): Success message.
        loading (str): Loading message.
        error (str): Error message.
    """
    yield '', lang('open_connection_start'), ''
    _, success, error = next(connect_mysql)
    yield success, '', error

    yield '', lang('create_database_start').format(PUC_DB), ''
    success, error = create_database()
    yield success, '', error

    yield '', lang('create_table_start').format(PUC_DB_HOMELESS), ''
    success, error = create_table()
    yield success, '', error

    yield '', lang('read_data_start').format('assets/csv/{}'.format(PUC_DB_HOMELESS)), ''
    homeless_raw_data, success, error = read_data()
    yield success, '', error

    yield '', lang('map_data_start').format('assets/csv/{}'.format(PUC_DB_HOMELESS)), ''
    homeless_data, success, error = map_homeless_data(data=homeless_raw_data)
    yield success, '', error

    yield '', lang('insert_table_start').format(PUC_DB_HOMELESS), ''
    success, error = insert_table(data=homeless_data)
    yield success, '', error


start_app = start_app_iterator()


def select_data(first_column: str = '', second_column: str = '', first_column_value: str = '', max_year: str = '', min_year: str = '', min_month: str = '', max_month: str = ''):
    """Calls select_table and with data filter params.

    Args:
        first_column (str, optional): First column to group data. Defaults to ''.
        second_column (str, optional): Second column to group data. Defaults to ''.
        first_column_value (str, optional): First column value to filter data. Defaults to ''.
        max_year (str, optional): Max year to filter data. Defaults to ''.
        min_year (str, optional): Min year to filter data. Defaults to ''.
        min_month (str, optional): Min month to filter data. Defaults to ''.
        max_month (str, optional): Max month to filter data. Defaults to ''.

    Returns:
        data (list): Data result from select_table query.
        error (str): Error message.
    """
    table_query = get_query(first_column=first_column, second_column=second_column, first_column_value=first_column_value, max_year=max_year,
                            min_year=min_year, min_month=min_month, max_month=max_month)
    data, _, error = select_table(table_query=table_query)
    return data, error


max_select_table_iterations = 2


def select_table_iterator(select_table_callback):
    """Call select_table_callback with a initial loading state

    Args:
        select_table_callback (function): select_table function

    Yields:
        data (list): Data result from select_table query.
        loading (str): Loading message.
        error (str): Error message.
    """
    yield None, lang('select_table_start').format(PUC_DB_HOMELESS), ''
    data, error = select_table_callback()
    yield data, '', error


def restart_app_iterator():
    """Calls drop_database and close_connection with default values.

    Yields:
        success (str): Success message.
        loading (str): Loading message.
        error (str): Error message.
    """
    try:
        yield '', lang('drop_database_start'), ''
        success, error = drop_database()
        yield success, '', error

        yield '', lang('close_connection_start'), ''
        success, error = close_connection()
        yield success, '', error
    except Exception as err:
        yield '', '', lang("restart_app_error").format(err)


restart_app = restart_app_iterator()
