import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)

from controller.reader import lang
from database.constants import (CONNECTION_CONFIG, PUC_DB, PUC_DB_CREATE_QUERY, PUC_DB_DROP_QUERY, PUC_DB_HOMELESS_CREATE_QUERY, PUC_DB_HOMELESS_INSERT_QUERY,
                                PUC_DB_HOMELESS_SELECT_QUERY_COLUMNS, PUC_DB_HOMELESS_SELECT_QUERY_PERIOD, PUC_DB_HOMELESS_SELECT_QUERY, PUC_DB_HOMELESS, AGE_COLUMN, PUC_DB_HOMELESS_SELECT_QUERY_CUSTON_PERIOD, PUC_DB_HOMELESS_SELECT_QUERY_CUSTON_COLUMNS, PUC_DB_HOMELESS_AGE_RANGES_QUERY, SOCIAL_WELFARE_COLUMN, PUC_DB_HOMELESS_SOCIAL_WELFARE_RANGES_QUERY)


def open_connection():
    """Opens a connection to the MySQL server.

    Returns:
        connection (MySQLConnection): MySQL oppened connection.
        success (str): Success message.
        error (str): Error message.
    """
    connection = None
    success = ''
    error = ''
    try:
        connection: MySQLConnection = mysql.connector.connect(
            **CONNECTION_CONFIG)
        if not connection.is_connected():
            error = lang('open_connection_error').format(err)
        server_info = connection.get_server_info()
        success = lang('open_connection_success').format(server_info)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            error = lang('open_connection_crendentials_error')
        else:
            error = lang('open_connection_error').format(err)
    finally:
        return connection, success, error


def open_connection_iterator():
    """Calls open_connection once and returns the same connection each time called.

    Yields:
        connection (MySQLConnection): MySQL oppened connection.
        success (str): Success message.
        error (str): Error message.
    """
    connection, message, error = open_connection()
    while True:
        yield connection, message, error


connect_mysql = open_connection_iterator()


def close_connection():
    """Closes the MySQLConnection created by open_connection_iterator.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connect_mysql)
    success = ''
    error = ''
    try:
        if connection.is_connected():
            server_info = connection.get_server_info()
            connection.close()
            success = lang('close_connection_success').format(server_info)
        error = lang('close_connection_error').format(errorcode.ER_NO_DB_ERROR)
        connect_mysql.close()
    except Exception as err:

        error = lang('close_connection_error').format(err)
    finally:
        return success, error


def create_database(db_name: str = PUC_DB, db_query=PUC_DB_CREATE_QUERY):
    """Creates a database in the MySQLConnection created by open_connection_iterator.

    Args:
        db_name (str, optional): Database name. Defaults to PUC_DB.
        db_query (str, optional): Create database query. Defaults to PUC_DB_CREATE_QUERY.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connect_mysql)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.execute(db_query)
        connection.database = db_name
        cursor.close()
        success = lang('create_database_success').format(db_name)
    except mysql.connector.Error as err:
        error = lang('create_database_error').format(db_name, err)
    finally:
        return success, error


def drop_database(db_name: str = PUC_DB, db_query=PUC_DB_DROP_QUERY):
    """Drops a database in the MySQLConnection created by open_connection_iterator.

    Args:
        db_name (str, optional): Database name. Defaults to PUC_DB.
        db_query (str, optional): Create database query. Defaults to PUC_DB_DROP_QUERY.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connect_mysql)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.execute(db_query.format(db_name))
        cursor.close()
        success = lang('drop_database_success').format(db_name)
    except mysql.connector.Error as err:
        error = lang('drop_database_error').format(db_name, err)
    finally:
        return success, error


def create_table(table_name: str = PUC_DB_HOMELESS, table_query=PUC_DB_HOMELESS_CREATE_QUERY):
    """Creates a table in the MySQLConnection created by open_connection_iterator

    Args:
        table_name (str, optional): Table name. Defaults to PUC_DB_HOMELESS.
        table_query (str, optional): Create table query. Defaults to PUC_DB_HOMELESS_CREATE_QUERY.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connect_mysql)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.execute(table_query)
        cursor.close()
        success = lang('create_table_success').format(table_name)
    except mysql.connector.Error as err:
        error = lang(
            'create_table_error').format(table_name, err)
    finally:
        return success, error


def insert_table(data: list, table_name: str = PUC_DB_HOMELESS, table_query: str = PUC_DB_HOMELESS_INSERT_QUERY):
    """Populates a table in the MySQLConnection created by open_connection_iterator

    Args:
        data (list): Data to be populated in table
        table_name (str, optional): Table name. Defaults to PUC_DB_HOMELESS.
        table_query (str, optional): Create table query. Defaults to PUC_DB_HOMELESS_INSERT_QUERY.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connect_mysql)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.executemany(table_query, data)
        connection.commit()
        cursor.close()
        success = lang('insert_table_success').format(
            table_name, cursor.rowcount)
    except mysql.connector.Error as err:
        error = lang('insert_table_error').format(table_name, err)
    finally:
        return success, error


def get_query(first_column: str = '', second_column: str = '', first_column_value: str = '', max_year: str = '', min_year: str = '', min_month: str = '', max_month: str = ''):
    """Get table query depending on the parameters

    Args:
        first_column (str, optional): First column to group data. Defaults to ''.
        second_column (str, optional): Second column to group data. Defaults to ''.
        first_column_value (str, optional): First column value to filter data. Defaults to ''.
        max_year (str, optional): Max year to filter data. Defaults to ''.
        min_year (str, optional): Min year to filter data. Defaults to ''.
        min_month (str, optional): Min month to filter data. Defaults to ''.
        max_month (str, optional): Max month to filter data. Defaults to ''.

    Returns:
        table_query (str): Correct table query
    """
    table_query = PUC_DB_HOMELESS_SELECT_QUERY
    hasColumns = bool(first_column and second_column and first_column_value)
    hasPeriod = bool(max_year and min_year and min_month and max_month)
    if hasColumns and hasPeriod and first_column != AGE_COLUMN and first_column != SOCIAL_WELFARE_COLUMN:
        table_query = PUC_DB_HOMELESS_SELECT_QUERY_PERIOD.format(
            first_column=first_column, second_column=second_column, first_column_value=first_column_value, max_year=max_year, min_year=min_year, min_month=min_month, max_month=max_month)
    if hasColumns and not hasPeriod and first_column != AGE_COLUMN and first_column != SOCIAL_WELFARE_COLUMN:
        table_query = PUC_DB_HOMELESS_SELECT_QUERY_COLUMNS.format(
            first_column=first_column, second_column=second_column, first_column_value=first_column_value)
    if hasColumns and hasPeriod and first_column == AGE_COLUMN:
        table_query = PUC_DB_HOMELESS_SELECT_QUERY_CUSTON_PERIOD.format(
            first_column=first_column, second_column=second_column, custon_filter=PUC_DB_HOMELESS_AGE_RANGES_QUERY[first_column_value], max_year=max_year, min_year=min_year, min_month=min_month, max_month=max_month)
    if hasColumns and not hasPeriod and first_column == AGE_COLUMN:
        table_query = PUC_DB_HOMELESS_SELECT_QUERY_CUSTON_COLUMNS.format(
            first_column=first_column, second_column=second_column, custon_filter=PUC_DB_HOMELESS_AGE_RANGES_QUERY[first_column_value])
    if hasColumns and hasPeriod and first_column == SOCIAL_WELFARE_COLUMN:
        table_query = PUC_DB_HOMELESS_SELECT_QUERY_CUSTON_PERIOD.format(
            first_column=first_column, second_column=second_column, custon_filter=PUC_DB_HOMELESS_SOCIAL_WELFARE_RANGES_QUERY[first_column_value], max_year=max_year, min_year=min_year, min_month=min_month, max_month=max_month)
    if hasColumns and not hasPeriod and first_column == SOCIAL_WELFARE_COLUMN:
        table_query = PUC_DB_HOMELESS_SELECT_QUERY_CUSTON_COLUMNS.format(
            first_column=first_column, second_column=second_column, custon_filter=PUC_DB_HOMELESS_SOCIAL_WELFARE_RANGES_QUERY[first_column_value])

    return table_query


def select_table(table_name: str = PUC_DB_HOMELESS, table_query: str = PUC_DB_HOMELESS_SELECT_QUERY):
    """Select data from a table in the MySQLConnection created by open_connection_iterator

    Args:
        table_name (str, optional): Table name. Defaults to PUC_DB_HOMELESS.
        table_query (str, optional): Create table query. Defaults to PUC_DB_HOMELESS_SELECT_QUERY.

    Returns:
        data (list): Data filtered from table
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connect_mysql)
    data = []
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.execute(table_query)
        data = list(cursor.fetchall())
        cursor.close()
        success = lang('select_table_success').format(
            table_name, cursor.rowcount)
    except mysql.connector.Error as err:
        error = lang('select_table_error').format(table_name, err)
    finally:
        return data, success, error
