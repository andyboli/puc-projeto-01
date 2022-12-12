from controller.reader import lang
from database.constants import (HOMELESS_AGES_RANGE)


def map_age(age):
    """Map age value from csv file to insert in homeless table.

    Args:
        age (any): Age value from csv file.

    Returns:
        mapped_age (int | None): Age mapped value to insert in homeless table.
    """
    if type(age) is str:
        return int(float(age.replace(",", '.')))
    elif type(age) is int:
        return age
    else:
        return None


def map_birthday(birthday):
    """Map birthday value from csv file to insert in homeless table.

    Args:
        birthday (any): Birthday value from csv file.

    Returns:
        mapped_birthday (str | None): Birthday mapped value to insert in homeless table.
    """
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


def map_ethnicity(ethnicity):
    """Map ethnicity value from csv file to insert in homeless table.

    Args:
        ethnicity (any): Ethnicity value from csv file.

    Returns:
        mapped_ethnicity (str | None): Ethnicity mapped value to insert in homeless table.
    """
    if type(ethnicity) is str and ethnicity == 'Parda':
        return ethnicity
    if type(ethnicity) is str and ethnicity == 'Branca':
        return ethnicity
    if type(ethnicity) is str and ethnicity == 'Amarela':
        return ethnicity
    if type(ethnicity) is str and ethnicity == 'Indigena':
        return ethnicity
    if type(ethnicity) is str and ethnicity == 'Preta':
        return ethnicity
    return None


def map_gender(gender):
    if gender == 'FEMININO':
        return 'Feminino'
    if gender == 'MASCULINO':
        return 'Masculino'
    return None


def map_date(dateString: str):
    split_date = dateString.split('-')
    year = split_date[0]
    month = split_date[1]
    return year, month


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
    """Map month_year value from csv file to insert in homeless table.

    Args:
        month_year (any): Month year value from csv file.

    Returns:
        mapped_month_year (str | None): Month year value to insert in homeless table.
    """
    if type(month_year) is int:
        month_year_str = str(month_year)
        return '0' + month_year_str[0] + '/' + month_year_str[1:5]
    if type(month_year) is str:
        month_year_list = month_year.split("/")
        if len(month_year_list) == 3:
            return month_year_list[1] + '/' + month_year_list[2]
        if len(month_year_list) == 2:
            return map_month(month_year_list[0]) + '/' + map_year(month_year_list[1])
        if len(month_year_list) == 1:
            month_year_str = month_year_list[0]
            return map_month(month_year_str[0:3]) + '/' + month_year_str[3:7]
    return None


def map_region(region):
    """Map region value from csv file to insert in homeless table.

    Args:
        region (any): Region value from csv file.

    Returns:
        mapped_region (str | None): Region value to insert in homeless table.
    """
    if type(region) is str and region == 'LESTE':
        return 'Leste'
    if type(region) is str and region == 'NOROESTE':
        return 'Noroeste'
    if type(region) is str and region == 'BARREIRO':
        return 'Barreiro'
    if type(region) is str and region == 'NORDESTE':
        return 'Nordeste'
    if type(region) is str and region == 'VENDA NOVA':
        return 'Venda Nova'
    if type(region) is str and region == 'PAMPULHA':
        return 'Pampulha'
    if type(region) is str and (region == 'CENTRO-SUL' or region == 'CENTRO SUL'):
        return 'Centro Sul'
    if type(region) is str and region == 'OESTE':
        return 'Oeste'
    if type(region) is str and region == 'NORTE':
        return 'Norte'
    return None


def map_schooling(schooling):
    """Map schooling value from csv file to insert in homeless table.

    Args:
        schooling (any): Schooling value from csv file.

    Returns:
        mapped_schooling (str | None): Schooling mapped value to insert in homeless table.
    """
    if type(schooling) is str and schooling == 'Medio incompleto':
        return schooling
    if type(schooling) is str and schooling == 'Fundamental completo':
        return schooling
    if type(schooling) is str and schooling == 'Fundamental incompleto':
        return schooling
    if type(schooling) is str and schooling == 'Medio completo':
        return schooling
    if type(schooling) is str and schooling == 'Superior incompleto ou mais':
        return schooling
    if type(schooling) is str and schooling == 'Sem instrucao':
        return schooling
    return None


def map_social_welfare(social_welfare):
    """Map social welfare value from csv file to insert in homeless table.

    Args:
        social_welfare (any): Social welfare value from csv file.

    Returns:
        mapped_social_welfare (bool): Social welfare mapped value to insert in homeless table.
    """
    if social_welfare == 'SIM':
        return True
    return False


def get_period_index(headers: list):
    """Get the period index from a file headers.

    Args:
        headers (list): List of all headers in file.

    Returns:
        index: The index of the period value in the file.
    """
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
    """Get the social_welfare index from a file headers.

    Args:
        headers (list): List of all headers in file.

    Returns:
        index: The index of the social_welfare value in the file.
    """
    try:
        social_welfare_index = headers.index('BOLSA_FAMILIA')
        return social_welfare_index
    except:
        social_welfare_index = headers.index('AUXILIO_BRASIL')
        return social_welfare_index


def map_homeless_data(data: list):
    """Map all csv data from assets/csv/homeless.

    Args:
        data (list): Raw csv data from assets/csv/homeless.

    Returns:
        mapped_data (list): Mapped homeless csv data to populate homeless table.
        success (str): Success message.
        error (str): Error message.
    """
    mapped_data = []
    success = ''
    error = ''
    try:
        for csv_data in data:
            gender_index: int = csv_data['headers'].index('SEXO')
            region_index: int = csv_data['headers'].index('REGIONAL')
            age_index: int = csv_data['headers'].index('IDADE')
            ethnicity_index: int = csv_data['headers'].index('COR_RACA')
            schooling_index: int = csv_data['headers'].index('GRAU_INSTRUCAO')
            birthday_index: int = csv_data['headers'].index('DATA_NASCIMENTO')
            month_year_index: int = csv_data['headers'].index(
                'MES_ANO_REFERENCIA')
            period_index = get_period_index(csv_data['headers'])
            social_welfare_index = get_social_welfare_index(
                csv_data['headers'])
            for raw_data in csv_data['values']:
                period: str = raw_data[period_index]
                gender = map_gender(raw_data[gender_index])
                region = map_region(raw_data[region_index])
                age = map_age(raw_data[age_index])
                ethnicity = map_ethnicity(raw_data[ethnicity_index])
                schooling = map_schooling(raw_data[schooling_index])
                birthday = map_birthday(raw_data[birthday_index])
                social_welfare = map_social_welfare(
                    raw_data[social_welfare_index])
                month_year = map_month_year(raw_data[month_year_index])
                mapped_data.append((month_year, age,  gender, birthday,
                                    schooling, ethnicity, region, period, social_welfare))
        success = lang('map_data_success').format('assets/csv/homeless')
    except Exception as err:
        error = lang('map_data_error').format('assets/csv/homeless', err)
    finally:
        return mapped_data, success, error


def map_bar_chart_data(data):
    columns = {}
    mapped_data = []
    for amout, first_column, second_column in data:
        if first_column not in columns.keys():
            columns[first_column] = {}
        if second_column not in columns[first_column].keys():
            columns[first_column][second_column] = amout
        else:
            columns[first_column][second_column] = [
                *columns[first_column][second_column], amout]
    for first_column in columns.keys():
        second_columns = columns[first_column].keys()
        amouts = columns[first_column].values()
        mapped_data.append(
            {'type': 'bar', 'name': first_column, 'x': list(second_columns), 'y': list(amouts)})
    return mapped_data


# def map_age_range(age):
#     if age < 12:
#         return '0-11'
#     elif age >= 12 and age < 18:
#         return '12-17'
#     elif age >= 18 and age < 30:
#         return '18-29'
#     elif age >= 30 and age < 60:
#         return '30-59'
#     else:
#         return '>60'


# def map_column_range():
