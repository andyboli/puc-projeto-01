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
    PRIMARY KEY (`id`),
    UNIQUE INDEX `idhomeless_UNIQUE` (`id` ASC) VISIBLE)
    ENGINE = InnoDB''')


TABLES['homeless']["insert"] = (
    '''INSERT INTO `{0}`.`homeless`
    (period, birthday, age, gender, bolsa_familia, schooling, ethnicity, region, year)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''')


TABLES['homeless']['header'] = ['period', 'birthday', 'age', 'gender',
                                'bolsa_familia', 'schooling', 'ethnicity', 'region', 'year']
