import os
import pandas as pd

from database.constants import PUC_DB_HOMELESS


def lang(key: str) -> str:
    """Reads the file from assets/json/lang.json.

    Args:
        key (str): A key existing in lang.json.

    Returns:
        str: An application text.
    """
    return pd.read_json(path_or_buf='assets/json/lang.json', orient='index').to_dict()[0][key]


def read_csv(filepath: str):
    """Reads a csv file from filepath.

    Args:
        filepath (str): Csv file path.

    Returns:
        csv_data (dict[str, list]): csv file data headers and values
    """
    csv = pd.read_csv(
        filepath_or_buffer=filepath, sep=';', header=0, encoding='latin-1')
    csv_headers: list = csv.columns.tolist()
    csv_values: list = csv.values.tolist()
    return {'headers': csv_headers, 'values': csv_values}


def read_data(table_name: str = PUC_DB_HOMELESS):
    """Reads all csv files from a diretory in assets/csv/table_name

    Args:
        table_name (str, optional): The directory name that have the files, should match a table name. Defaults to PUC_DB_HOMELESS.

    Returns:
        data (list): All csv files data headers and values
        success: success message
        error: error message
    """
    data = []
    data_length = 0
    success = ''
    error = ''
    try:
        dir = 'assets/csv/{}'.format(table_name)
        files_path = os.listdir(dir)
        for filepath in files_path:
            csv_data = read_csv(dir + "/{}".format(filepath))
            data.append(csv_data)
            data_length += len(csv_data['values'])
        success = lang('read_data_success').format(
            dir, data_length)
    except Exception as err:
        error = lang('read_data_error').format(dir, err)
    finally:
        return data, success,  error
