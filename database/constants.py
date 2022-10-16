from dotenv import dotenv_values

env = dotenv_values(".env")

CONFIG = {
    'user': env["USER"],
    'password': env["PASSWORD"],
    'host': env["HOST"],
    'raise_on_warnings': True
}


CREATE_DATABASE_QUERY = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'UTF8MB4'"

DROP_DATABASE_QUERY = "DROP DATABASE IF EXISTS {}"

DB_NAME = 'puc_database'

TABLES = {}


TABLES['homeless'] = (
    '''CREATE TABLE IF NOT EXISTS `mydb`.`homeless` (
    `id` INT NOT NULL,
    `data_nascimento` DATE NOT NULL,
    `data_referencia` DATE NOT NULL,
    `idade` INT NOT NULL,
    `dias` INT NOT NULL,
    `bolsa_familia` TINYINT NOT NULL,
    `regiao` VARCHAR(45) NOT NULL,
    `genero` VARCHAR(45) NULL,
    `etinia` VARCHAR(45) NULL,
    `escolaridade` VARCHAR(45) NULL,
    PRIMARY KEY (`id`),
    UNIQUE INDEX `idhomeless_UNIQUE` (`id` ASC) VISIBLE)
    ENGINE = InnoDB''')
