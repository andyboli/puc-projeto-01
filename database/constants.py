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
    ENGINE = InnoDB'''.format(db_name=PUC_DB, table_name=PUC_DB_HOMELESS, *PUC_DB_HOMELESS_COLUMNS)

PUC_DB_HOMELESS_INSERT_QUERY = 'INSERT INTO {db_name}.{table_name} (month_year, age, gender, birthday, schooling, ethnicity, region, period, social_welfare) '.format(
    db_name=PUC_DB, table_name=PUC_DB_HOMELESS) + '''VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''


PUC_DB_HOMELESS_SELECT_QUERY_COLUMNS = 'SELECT amount, {second_column} FROM (SELECT COUNT(*) AS amount, {first_column}, {second_column} ' + 'FROM {db_name}.{table_name} '.format(
    db_name=PUC_DB, table_name=PUC_DB_HOMELESS) + "GROUP BY {first_column}, {second_column}) AS filted_columns WHERE {first_column} = '{first_column_value}'"

PUC_DB_HOMELESS_MAP_YEAR = 'CAST(SUBSTRING({column}, -4, 4) AS SIGNED)'.format(
    column=MONTH_YEAR_COLUMN)

PUC_DB_HOMELESS_MAP_MONTH = 'CAST(SUBSTRING({column}, -7, 2) AS SIGNED)'.format(
    column=MONTH_YEAR_COLUMN)

PUC_DB_HOMELESS_SELECT_QUERY_PERIOD = 'SELECT amount, {second_column} FROM (SELECT COUNT(*) AS amount, {first_column}, {second_column} ' + 'FROM {db_name}.{table_name} '.format(
    db_name=PUC_DB, table_name=PUC_DB_HOMELESS) + 'WHERE {mapped_year} '.format(
        mapped_year=PUC_DB_HOMELESS_MAP_YEAR) + '>= {min_year} ' + 'and {mapped_year} '.format(
            mapped_year=PUC_DB_HOMELESS_MAP_YEAR) + '<= {max_year} ' + 'and {mapped_month} '.format(
                mapped_month=PUC_DB_HOMELESS_MAP_MONTH) + '>= {min_month} ' + 'and {mapped_month} '.format(
                    mapped_month=PUC_DB_HOMELESS_MAP_MONTH) + "<= {max_month} GROUP BY {first_column}, {second_column}) AS filted_columns_period WHERE {first_column} = '{first_column_value}'"


PUC_DB_HOMELESS_SELECT_QUERY = 'SELECT * FROM {db_name}.{table_name} '.format(
    db_name=PUC_DB, table_name=PUC_DB_HOMELESS) + 'LIMIT 25'


PUC_DB_HOMELESS_COLUMNS_LABELS = {
    'age': 'Idade',
    'ethnicity': 'Etnia',
    'gender': 'Gênero',
    'period': 'Período nas ruas',
    'region': 'Região',
    'schooling': 'Escolaridade',
    'social_welfare': 'Benefícios sociais',
}


PUC_DB_HOMELESS_COLUMNS_TABLE_LABELS = {
    'age': 'Idade',
    'ethnicity': 'Etnia',
    'gender': 'Gênero',
    'period': 'Período nas ruas',
    'region': 'Região',
    'schooling': 'Escolaridade',
    'social_welfare': 'Benefícios sociais',
    'month_year': 'Data da coleta',
    'birthday': "Data de nascimento"
}

HOMELESS_GENDERS = ['Masculino', 'Feminino']

HOMELESS_REGIONS = ['Oeste', 'Noroeste', 'Norte', 'Venda Nova',
                    'Nordeste', 'Pampulha', 'Barreiro', 'Leste', 'Centro Sul']

HOMELESS_ETHINICITIES = ['Parda',
                         'Indigena', 'Branca', 'Amarela', 'Preta']

HOMELESS_SCHOOLINGS = ['Superior incompleto ou mais',  'Medio incompleto',
                       'Sem instrucao', 'Medio completo', 'Fundamental completo', 'Fundamental incompleto']

HOMELESS_PERIODS = ['Mais de dez anos', 'Entre dois e cinco anos', 'Ate seis meses',
                    'Entre um e dois anos', 'Entre seis meses e um ano', 'Entre cinco e dez anos']


HOMELESS_SOCIAL_WELFARES = [False, True]


HOMELESS_AGES_RANGE = ['Menor de 1 ano', '1 a 4 anos', '5 a 9 anos', '10 a 14 anos', '15 a 19 anos', '20 a 29 anos', '30 a 39 anos',
                       '40 a 49 anos', '50 a 59 anos', '60 a 69 anos', '70 a 79 anos', '80 anos e mais']

HOMELESS_YEARS_RANGE = ['2019', '2020', '2021', '2022']

HOMELESS_MONTHS_RANGE = ['01', '02', '03', '04', '05',
                         '06', '07', '08', '09', '10', '11', '12']


PUC_DB_HOMELESS_COLUMNS_RANGES = {
    'age': HOMELESS_AGES_RANGE,
    'ethnicity': HOMELESS_ETHINICITIES,
    'gender': HOMELESS_GENDERS,
    'period': HOMELESS_PERIODS,
    'region': HOMELESS_REGIONS,
    'schooling': HOMELESS_SCHOOLINGS,
    'social_welfare': HOMELESS_SOCIAL_WELFARES,
}
