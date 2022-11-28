import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)
from controller import (reader)
from database import (constants)


def create_database(connection: MySQLConnection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            constants.CREATE_DB_QUERY.format(constants.DB_NAME))
        connection.database = constants.DB_NAME
    except mysql.connector.Error as err:
        if err.errno != errorcode.ER_DB_CREATE_EXISTS:
            return None, reader.lang('database_create_database_error').format(err)
        return reader.lang('database_create_database_done').format(
            constants.DB_NAME), None
    else:
        return reader.lang('database_create_database_done').format(
            constants.DB_NAME), None
    finally:
        cursor.close()


def create_tables(connection: MySQLConnection):
    try:
        cursor = connection.cursor()
        tables: dict[str, str] = constants.TABLES
        for table in tables:
            try:
                CREATE_TABLE_QUERY = tables[table]["create_query"]
                cursor.execute(CREATE_TABLE_QUERY.format(
                    constants.DB_NAME))
            except mysql.connector.Error as err:
                if err.errno != errorcode.ER_TABLE_EXISTS_ERROR:
                    return None, reader.lang(
                        'database_create_tables_table_error').format(table, err)
    except mysql.connector.Error as err:
        return None, reader.lang('database_create_tables_error').format(err)
    else:
        return reader.lang('database_create_tables_done'), None
    finally:
        cursor.close()


def insert_table(connection: MySQLConnection, table: str, data: list):
    try:
        cursor = connection.cursor()
        INSERT_DATABASE_QUERY: str = constants.TABLES[table]["insert_query"].format(
            constants.DB_NAME)
        cursor.executemany(INSERT_DATABASE_QUERY, data)
        connection.commit()
    except mysql.connector.Error as err:
        return None, reader.lang('database_insert_table_error').format(table, err)
    else:
        return reader.lang('database_insert_table_done').format(
            table, cursor.rowcount), None
    finally:
        cursor.close()
