from mysql.connector import (errorcode, MySQLConnection)
import mysql.connector

from controller.reader import lang
from database.constants import DB_CONFIG, CREATE_DB_QUERY, DROP_DB_QUERY, DB_NAME, TABLES


def connect_database():
    """open a connection with mysql
    connection: mysql oppened connection
    success: success message
    error: error message

    return data: MySQLConnection | None, success: str, error: str
    """
    try:
        success = ''
        error = ''
        connection: MySQLConnection = mysql.connector.connect(**DB_CONFIG)
        if not connection.is_connected():
            raise errorcode.ER_HOST_IS_BLOCKED
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            error = lang('database_connect_crendentials_error')
        else:
            error = lang('database_connect_error').format(err)
    else:
        success = lang('database_connect_done').format(
            connection.get_server_info())
    finally:
        return connection, success, error


def close_database(connection: MySQLConnection):
    """close a connection with mysql

    return a success message
    """
    if connection.is_connected():
        connection.close()
    return lang('database_connect_close')


def create_database(connection: MySQLConnection):
    """create the puc_database database
    success: success message
    error: error message

    return success: str, error: str
    """
    try:
        success = ''
        error = ''
        cursor = connection.cursor()
        cursor.execute(
            CREATE_DB_QUERY.format(DB_NAME))
        connection.database = DB_NAME
    except mysql.connector.Error as err:
        error = lang('database_create_database_error').format(
            DB_NAME, err)
    else:
        success = lang('database_create_database_done').format(
            DB_NAME)
    finally:
        cursor.close()
        return success, error


def drop_database(connection: MySQLConnection):
    """drop the puc_database database
    success: success message
    error: error message

    return success: str, error: str
    """
    try:
        success = ''
        error = ''
        cursor = connection.cursor()
        cursor.execute(
            DROP_DB_QUERY.format(DB_NAME))
    except mysql.connector.Error as err:
        error = lang('database_drop_error').format(DB_NAME, err)
    else:
        success = lang('database_drop_done').format(DB_NAME)
    finally:
        cursor.close()
        return success, error


def create_tables(connection: MySQLConnection):
    """create all tables from tables constant in puc_database database
    message: success message
    error: error message

    return success: str, error: str
    """
    try:
        success = ''
        error = ''
        cursor = connection.cursor()
        tables: dict[str, str] = TABLES
        for table in tables:
            try:
                CREATE_TABLE_QUERY = tables[table]["create_query"]
                cursor.execute(CREATE_TABLE_QUERY.format(
                    DB_NAME))
            except mysql.connector.Error as err:
                error = lang(
                    'database_create_tables_table_error').format(table, err)
                break
    except mysql.connector.Error as err:
        error = lang('database_create_tables_error').format(err)
    else:
        success = lang('database_create_tables_done')
    finally:
        cursor.close()
        return success, error


def insert_table(connection: MySQLConnection, table: str, data: list):
    """insert a list of data in a table
    message: success message
    error: error message

    return success: str, error: str
    """
    try:
        success = ''
        error = ''
        cursor = connection.cursor()
        INSERT_TABLE_QUERY: str = TABLES[table]["insert_query"].format(
            DB_NAME)
        cursor.executemany(INSERT_TABLE_QUERY, data)
        connection.commit()
    except mysql.connector.Error as err:
        error = lang('database_insert_table_error').format(table, err)
    else:
        success = lang('database_insert_table_done').format(
            table, cursor.rowcount)
    finally:
        cursor.close()
        return success, error
