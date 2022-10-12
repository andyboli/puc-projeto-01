# trocar para .env

CONFIG = {
  'user': 'xxxx',
  'password': 'xxxxxx',
  'host': 'xxxxxx',
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

