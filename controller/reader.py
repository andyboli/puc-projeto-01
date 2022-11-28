from ast import If
from http.client import INSUFFICIENT_STORAGE
from controller import (reader)
import os
import pandas as pd
import datetime


def lang(key: str) -> str:
    return pd.read_json(path_or_buf='assets/json/lang.json', orient='index').to_dict()[0][key]


def read_csv(filepath: str):
    data: dict[str, list] = {}
    csv = pd.read_csv(
        filepath_or_buffer=filepath, sep=';', header=0, encoding='latin-1')
    data['headers'] = csv.columns.tolist()
    data['values'] = csv.values.tolist()
    return data


def read_data(table: str):
    try:
        dir = 'assets/csv/{}'.format(table)
        files_path = os.listdir(dir)
        data = []
        data_length = 0
        for filepath in files_path:
            csv_data = read_csv(dir + "/{}".format(filepath))
            data.append(csv_data)
            data_length += len(csv_data['values'])
    except Exception as err:
        return None, None, reader.lang('reader_read_data_error').format(dir, err)
    else:
        return data, reader.lang('reader_read_data_done').format(
            dir, data_length), None


def map_region(region):
    if region == 'LESTE':
        return 'Leste'
    if region == 'NOROESTE':
        return 'Noroeste'
    if region == 'BARREIRO':
        return 'Barreiro'
    if region == 'NORDESTE':
        return 'Nordeste'
    if region == 'VENDA NOVA':
        return 'Venda Nova'
    if region == 'PAMPULHA':
        return 'Pampulha'
    if region == 'CENTRO-SUL' or region == 'CENTRO SUL':
        return 'Centro Sul'
    if region == 'OESTE':
        return 'Oeste'
    if region == 'NORTE':
        return 'Norte'
    return None


def map_age(age):
    if type(age) is str:
        return int(float(age.replace(",", '.')))
    elif type(age) is int:
        return age
    else:
        return None


def map_ethnicity(ethnicity):
    if ethnicity == 'Parda':
        return ethnicity
    if ethnicity == 'Branca':
        return ethnicity
    if ethnicity == 'Amarela':
        return ethnicity
    if ethnicity == 'Indigena':
        return ethnicity
    if ethnicity == 'Preta':
        return ethnicity
    return None


def map_schooling(schooling):
    if schooling == 'Medio incompleto':
        return schooling
    if schooling == 'Fundamental completo':
        return schooling
    if schooling == 'Fundamental incompleto':
        return schooling
    if schooling == 'Medio completo':
        return schooling
    if schooling == 'Superior incompleto ou mais':
        return schooling
    if schooling == 'Sem instrucao':
        return schooling
    return None


def map_birthday(birthday):
    if type(birthday) is str:
        birthday_list: list = birthday.split(' ')[0].split('/')
        birtday_day = birthday_list[0]
        if len(birtday_day) == 1:
            birtday_day = '0' + birtday_day
        birtday_month = birthday_list[1]
        if len(birtday_month) == 1:
            birtday_month = '0' + birtday_month
        birtday_year = birthday_list[2]
        return birtday_day + '/' + birtday_month + '/' + birtday_year
    return None


def get_period_index(headers: list):
    try:
        period_index = headers.index('TEMPO_VIVE_NA_RUA')
        return period_index
    except:
        try:
            period_index = headers.index('TEMPO_VIVIE_NA_RUA')
            return period_index
        except:
            period_index = headers.index('ï»¿TEMPO_VIVE_NA_RUA')
            return period_index


def get_social_welfare_index(headers: list):
    try:
        social_welfare_index = headers.index('BOLSA_FAMILIA')
        return social_welfare_index
    except:
        social_welfare_index = headers.index('AUXILIO_BRASIL')
        return social_welfare_index


def map_social_welfare(social_welfare):
    if social_welfare == 'SIM':
        return True
    return False


def map_month(month: str):
    if month == 'JAN':
        return '01'
    if month == 'FEV':
        return '02'
    if month == 'MAR':
        return '03'
    if month == 'ABR':
        return '04'
    if month == 'MAI':
        return '05'
    if month == 'JUN':
        return '06'
    if month == 'JUL':
        return '07'
    if month == 'AGO':
        return '08'
    if month == 'SET':
        return '09'
    if month == 'out':
        return '10'
    if month == 'NOV':
        return '11'
    if month == 'DEZ':
        return '12'
    return month


def map_year(year: str):
    if len(year) == 2:
        return '20' + year
    return year


def map_month_year(month_year):
    if type(month_year) == int:
        month_year_str = str(month_year)
        return '0' + month_year_str[0] + '/' + month_year_str[1:5]
    month_year_list = month_year.split("/")
    if len(month_year_list) == 3:
        return month_year_list[1] + '/' + month_year_list[2]
    if len(month_year_list) == 2:
        return map_month(month_year_list[0]) + '/' + map_year(month_year_list[1])
    if len(month_year_list) == 1:
        month_year_str = month_year_list[0]
        return map_month(month_year_str[0:3]) + '/' + month_year_str[3:7]
    return month_year


def map_gender(gender):
    if gender == 'FEMININO':
        return 'Feminino'
    if gender == 'MASCULINO':
        return 'Masculino'
    return None


def map_homeless_data(data: list):
    try:
        mapped_data = []
        headers: set = set()
        for file_data in data:
            headers.update(file_data['headers'])
            gender_index = file_data['headers'].index('SEXO')
            region_index = file_data['headers'].index('REGIONAL')
            age_index = file_data['headers'].index('IDADE')
            ethnicity_index = file_data['headers'].index('COR_RACA')
            schooling_index = file_data['headers'].index('GRAU_INSTRUCAO')
            birthday_index = file_data['headers'].index('DATA_NASCIMENTO')
            period_index = get_period_index(file_data['headers'])
            social_welfare_index = get_social_welfare_index(
                file_data['headers'])
            month_year_index = file_data['headers'].index('MES_ANO_REFERENCIA')
            for values in file_data['values']:
                gender = map_gender(values[gender_index])
                region = map_region(values[region_index])
                age = map_age(values[age_index])
                ethnicity = map_ethnicity(values[ethnicity_index])
                schooling = map_schooling(values[schooling_index])
                birthday = map_birthday(values[birthday_index])
                period = values[period_index]
                social_welfare = map_social_welfare(
                    values[social_welfare_index])
                month_year = map_month_year(values[month_year_index])
                mapped_data.append((month_year, age,  gender, birthday,
                                    schooling, ethnicity, region, period, social_welfare))
    except Exception as err:
        return None, None, reader.lang('reader_map_data_error').format(
            'assets/csv/homeless', err)
    else:
        return mapped_data, reader.lang('reader_map_data_done').format(
            'assets/csv/homeless', len(mapped_data)), None


def data_range(mapped_data: list):
    headers = ["month_year", "age",  "gender", "birthday",
               "schooling", "ethnicity", "region", "period", "social_welfare"]
    month_years: set = set()
    ages: set = set()
    genders: set = set()
    birthdays: set = set()
    schoolings: set = set()
    ethinicities: set = set()
    regions: set = set()
    periods: set = set()
    social_welfares: set = set()
    for data in mapped_data:
        month_years.add(data[0])
        ages.add(data[1])
        genders.add(data[2])
        birthdays.add(data[3])
        schoolings.add(data[4])
        ethinicities.add(data[5])
        regions.add(data[6])
        periods.add(data[7])
        social_welfares.add(data[8])
    return {
        headers,
        month_years,
        ages,
        genders,
        birthdays,
        schoolings,
        ethinicities,
        regions,
        periods,
        social_welfares,
    }
