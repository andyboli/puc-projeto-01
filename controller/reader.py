import pandas as pd


def lang(key: str) -> str:
    return pd.read_json(path_or_buf='static/json/lang.json', orient='index').to_dict()[0][key]
