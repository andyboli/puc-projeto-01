from ast import If
from http.client import INSUFFICIENT_STORAGE
from controller import (reader)
import os
import pandas as pd
import pprint


def lang(key: str) -> str:
    return pd.read_json(path_or_buf='static/json/lang.json', orient='index').to_dict()[0][key]


def read_csv_header(filepath: str):
    csv = pd.read_csv(
        filepath_or_buffer=filepath, sep=';', header=0, encoding='latin-1')
    return csv.columns.array


def read_csv_values(filepath: str):
    csv = pd.read_csv(
        filepath_or_buffer=filepath, sep=';', header=0, encoding='latin-1')
    return csv.values


def read_data(table: str):
    try:
        dir = 'static/csv/{}'.format(table)
        print(reader.lang('reader_read_data_start').format(dir))
        files_path = os.listdir(dir)
        data: dict[str, list] = {}
        data['header'] = read_csv_header(dir + "/{}".format(files_path[1]))
        data['values'] = []
        for path in files_path:
            data['values'].extend(read_csv_values(
                filepath=dir + "/{}".format(path)))
    except Exception as err:
        print(reader.lang('reader_read_data_error').format(dir, err))
    else:
        print(reader.lang('reader_read_data_done').format(
            dir, str(data['header']), len(data['values'])))
        return data


def map_field(field):
    if type(field) is str:
        string_split = field.split(sep=" ")
        if string_split[0][0].lower() == "n" and string_split[0][-1].lower() == "o":
            string_split[0] = "Não"
            field = " ".join(string_split)
        return field
    else:
        return "Não Informado"


def map_age(age):
    if type(age) is str:
        return int(float(age.replace(",", '.')))
    elif type(age) is int:
        return age
    else:
        return None


def map_bolsa_familia(bolsa_familia):
    if (bolsa_familia == 'SIM'):
        return True
    else:
        return False


def map_year(date):
    if type(date) is str:
        raw_date: list = date.split('/')
        raw_year: str = raw_date[len(raw_date) - 1]
        return int(raw_year[len(raw_year) - 4] + raw_year[len(raw_year) - 3] +
                   raw_year[len(raw_year) - 2] + raw_year[len(raw_year) - 1])
    else:
        raw_year: str = str(date)
        return int(raw_year[len(raw_year) - 4] + raw_year[len(raw_year) - 3] +
                   raw_year[len(raw_year) - 2] + raw_year[len(raw_year) - 1])

def map_age_bracket(age_bracket):
    if type(age_bracket) is str:
        age_bracket = int(age_bracket.split(sep=",")[0])
    if age_bracket < 12: 
        return '0-11' 
    elif age_bracket >= 12 and age_bracket <18:
         return '12-17'
    elif age_bracket >= 18 and age_bracket <30:
         return '18-29'
    elif age_bracket >= 30 and age_bracket <60:
         return '30-59'
    else: 
        return '>60'

def map_homeless_data(data: dict)->dict:
    try:
        print(reader.lang('reader_map_data_start').format('static/csv/homeless'))
        mapped_data = []
        periods: set = set()
        genders: set = set()
        schoolings: set = set()
        ethinicities: set = set()
        regions: set = set()
        for values in data['values']:
            period = map_field(values[0])
            periods.add(period)
            birthday = map_field(values[2])
            age = map_age(values[3])
            gender = map_field(values[4])
            genders.add(gender)
            bolsa_familia = map_bolsa_familia(values[5])
            schooling = map_field(values[7])
            schoolings.add(schooling)
            ethnicity = map_field(values[8])
            ethinicities.add(ethnicity)
            region = map_field(values[12])
            regions.add(region)
            year = map_year(values[14])
            age_bracket = map_age_bracket(values[3])
            mapped_data.append((period, birthday, age, gender,
                                bolsa_familia, schooling, ethnicity, region, year, age_bracket))
    except Exception as err:
        print(reader.lang('reader_read_data_error').format(
            'static/csv/homeless', err))
    
    final_data = {'ranges':
                    {"periods": periods, "genders": genders,
                    "schoolings": schoolings, "ethinicities": ethinicities, "regions": regions},
                    "data": mapped_data}
    pprint.pprint(reader.lang('reader_read_data_done').format(
        'static/csv/homeless', str(final_data['ranges']), len(final_data['data'])))
    return final_data
