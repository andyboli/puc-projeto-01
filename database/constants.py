from dotenv import dotenv_values

env = dotenv_values(".env")

CONFIG = {
    'user': env["USER"],
    'password': env["PASSWORD"],
    'host': env["HOST"],
    'raise_on_warnings': True
}

DATABASE = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'UTF8MB4'"

DB_NAME = 'puc'

TABLES = {}

TABLES['employees'] = (
    "CREATE TABLE IF NOT EXISTS `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")


'''It doesn't matter if this string contains 'single'
or "double" quotes, as long as there aren't 3 in a
row.'''
