from dotenv import dotenv_values

env = dotenv_values(".env")

CONFIG = {
    'user': env["USER"],
    'password': env["PASSWORD"],
    'host': env["HOST"],
    'raise_on_warnings': True
}

DB_NAME = 'puc_database'

CREATE_DATABASE_QUERY = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'UTF8MB4'"

DROP_DATABASE_QUERY = "DROP DATABASE IF EXISTS {}"
