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


TABLES['homeless']["insert"] = (
    '''INSERT INTO `{0}`.`homeless`
    (month_year, age, gender, birthday, schooling, ethnicity, region, period, social_welfare)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''')


TABLES['homeless']['header'] = ['month_year', 'age', 'gender', 'birthday',
                                'schooling', 'ethnicity', 'region', 'period', 'social_welfare']
