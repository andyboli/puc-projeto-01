from controller import (reader)
from database import (connection)


def app():
    print(reader.lang('main_title'))
    connection.run()
