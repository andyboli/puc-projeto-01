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

TABLES = {}

TABLES['homeless'] = {}

TABLES['homeless']["create"] = (
    '''CREATE TABLE IF NOT EXISTS `{}`.`homeless` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `year` INT NOT NULL,
    `age` INT NULL,
    `bolsa_familia` TINYINT NOT NULL,
    `region` VARCHAR(45) NULL,
    `period` VARCHAR(45) NOT NULL,
    `birthday` VARCHAR(45) NULL,
    `gender` VARCHAR(45) NULL,
    `ethnicity` VARCHAR(45) NULL,
    `schooling` VARCHAR(45) NULL, 
    `age_bracket` VARCHAR(45) NULL,
    PRIMARY KEY (`id`),
    UNIQUE INDEX `idhomeless_UNIQUE` (`id` ASC) VISIBLE)
    ENGINE = InnoDB''')


TABLES['homeless']["insert"] = (
    '''INSERT INTO `{0}`.`homeless`
    (period, birthday, age, gender, bolsa_familia, schooling, ethnicity, region, year, age_bracket)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''')


TABLES['homeless']['header'] = ['period', 'birthday', 'age', 'gender',
                                'bolsa_familia', 'schooling', 'ethnicity', 'region', 'year', 'age_bracket']

# TABLES['homeless_raw'] = {}

# TABLES['homeless_raw']["create"] = (
#     '''CREATE TABLE IF NOT EXISTS `{}`.`homeless_raw` (
#     `id` INT NOT NULL AUTO_INCREMENT,
#     `POP_RUA` INT NOT NULL,
#     `IDADE` INT NULL,
#     `VAL_REMUNERACAO_MES_PASSADO` FLOAT NULL,
#     `AUXILIO_BRASIL` TINYINT NOT NULL,
#     `TEMPO_VIVE_NA_RUA` VARCHAR(45) NULL,
#     `CONTATO_PARENTE_FORA_RUAS` VARCHAR(45) NOT NULL,
#     `DATA_NASCIMENTO` DATE NULL,
#     `SEXO` VARCHAR(45) NULL,
#     `COR_RACA` VARCHAR(45) NULL,
#     `GRAU_INSTRUCAO` VARCHAR(45) NULL, 
#     `Faixa da renda familiar per capita` VARCHAR(45) NULL,
#     `MES_ANO_REFERENCIA` DATE NULL,
#     `CRAS` VARCHAR(45) NULL,
#     `REGIONAL` VARCHAR(45) NULL,
#     `FAIXA_DESATUALICACAO_CADASTRAL` VARCHAR(45) NULL,
#     PRIMARY KEY (`id`),
#     UNIQUE INDEX `idhomeless_UNIQUE` (`id` ASC) VISIBLE)
#     ENGINE = InnoDB''')


# TABLES['homeless_raw']["insert"] = (
#     '''INSERT INTO `{0}`.`homeless_raw`
#     (POP_RUA, IDADE, VAL_REMUNERACAO_MES_PASSADO, AUXILIO_BRASIL, TEMPO_VIVE_NA_RUA, CONTATO_PARENTE_FORA_RUAS, DATA_NASCIMENTO, SEXO, COR_RACA, GRAU_INSTRUCAO, Faixa da renda familiar per capita, MES_ANO_REFERENCIA, CRAS, REGIONAL, FAIXA_DESATUALICACAO_CADASTRAL)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''')


# TABLES['homeless_raw']['header'] = ['POP_RUA`', 'IDADE', 'VAL_REMUNERACAO_MES_PASSADO', 'AUXILIO_BRASIL',
#                                 'TEMPO_VIVE_NA_RUA', 'CONTATO_PARENTE_FORA_RUAS', 'DATA_NASCIMENTO', 'SEXO', 'COR_RACA', 'GRAU_INSTRUCAO', 'Faixa da renda familiar per capita', 'MES_ANO_REFERENCIA', 'CRAS', 'REGIONAL', 'FAIXA_DESATUALICACAO_CADASTRAL']
