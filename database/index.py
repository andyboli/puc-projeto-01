def main():
    cnx = connect()
    create_database(cnx)
    close(cnx)