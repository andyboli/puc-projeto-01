import os
import pandas as pd


def lang(key: str) -> str:
    return pd.read_json(path_or_buf='static/json/lang.json', orient='index').to_dict()[0][key]


def read_data() -> str:
    files_path = os.listdir('static/csv')
    csv = pd.read_csv(
        filepath_or_buffer="static/csv/{}".format(files_path[0]), sep=';', header=0)
    header = csv.columns
    values = csv.values
    print(header)
    print(values[0])

    # for path in files_path:
    #     print(pd.read_csv())
    return
