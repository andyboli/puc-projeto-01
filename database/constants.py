from dotenv import dotenv_values


env = dotenv_values('.env')

CONNECTION_CONFIG = {
    'host': env['HOST'],
    'password': env['PASSWORD'],
    'raise_on_warnings': True,
    'user': env['USER'],
}

PUC_DB = 'puc_database'

PUC_DB_CREATE_QUERY = 'CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET "UTF8MB4"'.format(
    db_name=PUC_DB)

PUC_DB_DROP_QUERY = 'DROP DATABASE IF EXISTS {db_name}'.format(db_name=PUC_DB)

PUC_DB_HOMELESS = 'homeless'

AGE_COLUMN = 'age'
BIRTHDAY_COLUMN = 'birthday'
ETHNICITY_COLUMN = 'ethnicity'
GENDER_COLUMN = 'gender'
MONTH_YEAR_COLUMN = 'month_year'
PERIOD_COLUMN = 'period'
REGION_COLUMN = 'region'
SCHOOLING_COLUMN = 'schooling'
SOCIAL_WELFARE_COLUMN = 'social_welfare'

PUC_DB_HOMELESS_COLUMNS = (MONTH_YEAR_COLUMN, AGE_COLUMN, GENDER_COLUMN, BIRTHDAY_COLUMN,
                           SCHOOLING_COLUMN, ETHNICITY_COLUMN, REGION_COLUMN, PERIOD_COLUMN, SOCIAL_WELFARE_COLUMN)

PUC_DB_HOMELESS_CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS {db_name}.{table_name}(
    id INT NOT NULL AUTO_INCREMENT,
    {0} VARCHAR(45) NOT NULL,
    {1} INT NULL,
    {2} VARCHAR(45) NULL,
    {3} VARCHAR(45) NULL,
    {4} VARCHAR(45) NULL,
    {5} VARCHAR(45) NULL,
    {6} VARCHAR(45) NULL,
    {7} VARCHAR(45) NOT NULL,
    {8} TINYINT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX idhomeless_UNIQUE (id ASC) VISIBLE)
    ENGINE = InnoDB)'''.format(db_name=PUC_DB, table_name=PUC_DB_HOMELESS, *PUC_DB_HOMELESS_COLUMNS)

PUC_DB_HOMELESS_INSERT_QUERY = 'INSERT INTO {db_name}.{table_name} {db_headers} '.format(
    db_name=PUC_DB, table_name=PUC_DB_HOMELESS, db_headers=PUC_DB_HOMELESS_COLUMNS) + '''VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''


PUC_DB_HOMELESS_SELECT_QUERY_COLUMNS = 'SELECT COUNT(*) AS amount, {first_column}, {second_column} ' + 'FROM {db_name}.{table_name} '.format(
    db_name=PUC_DB, table_name=PUC_DB_HOMELESS) + 'GROUP BY {first_column}, {second_column}'

PUC_DB_HOMELESS_MAP_YEAR = 'CAST(SUBSTRING({column}, -4, 4) AS SIGNED)'.format(
    column=MONTH_YEAR_COLUMN)

PUC_DB_HOMELESS_MAP_MONTH = 'CAST(SUBSTRING({column}, -7, 2) AS SIGNED)'.format(
    column=MONTH_YEAR_COLUMN)

PUC_DB_HOMELESS_SELECT_QUERY_PERIOD = 'SELECT amount, {second_column} FROM (SELECT COUNT(*) AS amount, {first_column}, {second_column} ' + 'FROM {db_name}.{table_name} '.format(
    db_name=PUC_DB, table_name=PUC_DB_HOMELESS) + 'WHERE {mapped_year} '.format(
        mapped_year=PUC_DB_HOMELESS_MAP_YEAR) + '>= {min_year} ' + 'and {mapped_year} '.format(
            mapped_year=PUC_DB_HOMELESS_MAP_YEAR) + '<= {max_year} ' + 'and {mapped_month} '.format(
                mapped_month=PUC_DB_HOMELESS_MAP_MONTH) + '>= {min_month} ' + 'and {mapped_month} '.format(
                    mapped_month=PUC_DB_HOMELESS_MAP_MONTH) + '<= {max_month} GROUP BY {first_column}, {second_column}) AS filted_columns WHERE {first_column} = {first_column_value}'


PUC_DB_HOMELESS_SELECT_QUERY = 'SELECT * FROM {db_name}.{table_name} '.format(
    db_name=PUC_DB, table_name=PUC_DB_HOMELESS) + 'LIMIT {limit} ORDER BY {column}'


PUC_DB_HOMELESS_COLUMNS_LABELS = {
    'age': 'Idade',
    'ethnicity': 'Etnia',
    'gender': 'Gênero',
    'period': 'Período nas ruas',
    'region': 'Região',
    'schooling': 'Escolaridade',
    'social_welfare': 'Benefícios sociais',
}
