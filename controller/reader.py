import os
import pandas as pd


def lang(key: str) -> str:
    """reads the file from assets/json/lang.json

    return an app's text
    """
    return pd.read_json(path_or_buf='assets/json/lang.json', orient='index').to_dict()[0][key]


def read_csv(filepath: str):
    """reads a csv file from filepath
    headers: csv file data headers
    values: csv file data values

    return { headers: list, values: list }
    """
    csv = pd.read_csv(
        filepath_or_buffer=filepath, sep=';', header=0, encoding='latin-1')
    csv_headers: list = csv.columns.tolist()
    csv_values: list = csv.values.tolist()
    return {"headers": csv_headers, "values": csv_values}


def read_data(table: str):
    """reads all csv files from a diretory in assets/csv
    data: csv file data
    success: success message
    error: error message

    return data: list, success: str, error: str
    """
    try:
        success = ''
        error = ''
        data = []
        data_length = 0
        dir = 'assets/csv/{}'.format(table)
        files_path = os.listdir(dir)
        for filepath in files_path:
            csv_data = read_csv(dir + "/{}".format(filepath))
            data.append(csv_data)
            data_length += len(csv_data['values'])
    except Exception as err:
        error = lang('read_data_error').format(dir, err)
    else:
        success = lang('read_data_done').format(
            dir, data_length)
    finally:
        return data,  success,  error
