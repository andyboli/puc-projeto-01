from reader import (json)
from database import (connection)

def main():
    print(json.lang('main_title'))
    connection.main()