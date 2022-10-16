import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)
from controller import (reader)
from database import (constants)


def create_database(connection: MySQLConnection):
    try:
        print(reader.lang('database_create_database_start').format(constants.DB_NAME))
        cursor = connection.cursor()
        cursor.execute(
            constants.CREATE_DATABASE_QUERY.format(constants.DB_NAME))
        connection.database = constants.DB_NAME
    except mysql.connector.Error as err:
        if err.errno != errorcode.ER_DB_CREATE_EXISTS:
            print(reader.lang('database_create_database_error').format(err))
            exit(1)
    else:
        print(reader.lang('database_create_database_done').format(constants.DB_NAME))
    finally:
        cursor.close()


def create_tables(connection: MySQLConnection):
    try:
        print(reader.lang('database_create_tables_start'))
        cursor = connection.cursor()
        tables: dict[str, str] = constants.TABLES
        for table in tables:
            try:
                CREATE_TABLE_QUERY = tables[table]["create"]
                cursor.execute(CREATE_TABLE_QUERY.format(
                    constants.DB_NAME))
            except mysql.connector.Error as err:
                if err.errno != errorcode.ER_TABLE_EXISTS_ERROR:
                    print(reader.lang(
                        'database_create_tables_table_error').format(table, err))
                    exit(1)
    except mysql.connector.Error as err:
        print(reader.lang('database_create_tables_error').format(err))
    else:
        print(reader.lang('database_create_tables_done'))
    finally:
        cursor.close()


def insert_table(connection: MySQLConnection, table: str, data: list):
    try:
        print(reader.lang('database_insert_table_start').format(table))
        cursor = connection.cursor()
        INSERT_DATABASE_QUERY: str = constants.TABLES[table]["insert"].format(
            constants.DB_NAME)
        cursor.executemany(INSERT_DATABASE_QUERY, data)
        connection.commit()
    except mysql.connector.Error as err:
        print(reader.lang('database_insert_table_error').format(table, err))
    else:
        print(reader.lang('database_insert_table_done').format(
            table, cursor.rowcount))
    finally:
        cursor.close()
