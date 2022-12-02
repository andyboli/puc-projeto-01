from dotenv import dotenv_values


env = dotenv_values(".env")

DB_CONFIG = {
    'host': env["HOST"],
    'password': env["PASSWORD"],
    'raise_on_warnings': True,
    'user': env["USER"],
}

DB_NAME = 'puc_database'

CREATE_DB_QUERY = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'UTF8MB4'"

DROP_DB_QUERY = "DROP DATABASE IF EXISTS {}"

TABLES = {}

TABLES['homeless'] = {}

TABLES['homeless']['header'] = ['month_year', 'age', 'gender', 'birthday',
                                'schooling', 'ethnicity', 'region', 'period', 'social_welfare']

TABLES['homeless']["create_query"] = (
    '''CREATE TABLE IF NOT EXISTS `{}`.`homeless` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `month_year` VARCHAR(45) NOT NULL,
    `age` INT NULL,
    `gender` VARCHAR(45) NULL,
    `birthday` VARCHAR(45) NULL,
    `schooling` VARCHAR(45) NULL,
    `ethnicity` VARCHAR(45) NULL,
    `region` VARCHAR(45) NULL,
    `period` VARCHAR(45) NOT NULL,
    `social_welfare` TINYINT NULL,
    PRIMARY KEY (`id`),
    UNIQUE INDEX `idhomeless_UNIQUE` (`id` ASC) VISIBLE)
    ENGINE = InnoDB''')


TABLES['homeless']["insert_query"] = (
    '''INSERT INTO `{0}`.`homeless`
    (month_year, age, gender, birthday, schooling, ethnicity, region, period, social_welfare)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''')

TABLES['homeless']["select_query"] = ("SELECT * FROM homeless")


HOMELESS_GENDERS = ['Masculino', 'Feminino']

HOMELESS_REGIONS = [None, 'Oeste', 'Noroeste', 'Norte', 'Venda Nova',
                    'Nordeste', 'Pampulha', 'Barreiro', 'Leste', 'Centro Sul']

HOMELESS_ETHINICITIES = [None, 'Parda',
                         'Indigena', 'Branca', 'Amarela', 'Preta']

HOMELESS_SCHOOLINGS = ['Superior incompleto ou mais', None, 'Medio incompleto',
                       'Sem instrucao', 'Medio completo', 'Fundamental completo', 'Fundamental incompleto']

HOMELESS_PERIODS = ['Mais de dez anos', 'Entre dois e cinco anos', 'Ate seis meses',
                    'Entre um e dois anos', 'Entre seis meses e um ano', 'Entre cinco e dez anos']


HOMELESS_SOCIAL_WELFARES = [False, True]


HOMELESS_AGES_RANGE = ['Menor de 1 ano', '1 a 4 anos', '5 a 9 anos', '10 a 14 anos', '15 a 19 anos', '20 a 29 anos', '30 a 39 anos',
                       '40 a 49 anos', '50 a 59 anos', '60 a 69 anos', '70 a 79 anos', '80 anos e mais']

HOMELESS_YEARS_RANGE = ['2019', '2020', '2021', '2022']

HOMELESS_MONTHS_RANGE = ['01', '02', '03', '04', '05',
                         '06', '07', '08', '09', '10', '11', '12']


TABLES['homeless']['headers'] = ["month_year", "age", "gender",
                                 "birthday", "schooling", "ethnicity", "region", "period", "social_welfare"]


TABLES['homeless']['headers_label'] = {"age": 'Idade', "gender": "Gênero",
                                       "schooling": 'Escolaridade', "ethnicity": "Etnia", "region": "Região", "period": "Período nas ruas", "month_year": "Período de referência", "social_welfare": "Benefícios sociais "}

TABLES['homeless']['headers_ranges'] = {
    "age": HOMELESS_AGES_RANGE,
    "ethnicity": HOMELESS_ETHINICITIES,
    "gender": HOMELESS_GENDERS,
    "month_year": {'years_range': HOMELESS_YEARS_RANGE, 'months_range': HOMELESS_MONTHS_RANGE},
    "period": HOMELESS_PERIODS,
    "region": HOMELESS_REGIONS,
    "schooling": HOMELESS_SCHOOLINGS,
    "social_welfare": HOMELESS_SOCIAL_WELFARES,
}
