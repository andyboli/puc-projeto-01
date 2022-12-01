import pandas as pd


def faixa_etaria(fe):
    if fe['IDADE'] < 12:
        return '0-11'
    elif fe['IDADE'] >= 12 and fe['IDADE'] < 18:
        return '12-17'
    elif fe['IDADE'] >= 18 and fe['IDADE'] < 30:
        return '18-29'
    elif fe['IDADE'] >= 30 and fe['IDADE'] < 60:
        return '30-59'
    else:
        return '>60'


rua = pd.read_csv(r'C:\Users\gusta\OneDrive\Documentos\Curso - TBD\1º Semestre\Projeto\data_set_poprua_cadunico-07-2022.csv',
                  encoding='cp860', delimiter=';', usecols=[0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12])
rua['Faixa_etaria'] = rua.apply(faixa_etaria, axis=1)
print(rua)

# def map_homeless_data_range(mapped_data: list):
#     """receive all mapped csv data from assets/csv/homeless
#     headers: a list of homeless headers
#     header: a set with distinct values from a homeless header

#     return  {headers: list, [header]: set}
#     """
#
#     month_years: set = set()
#     ages: set = set()
#     genders: set = set()
#     birthdays: set = set()
#     schoolings: set = set()
#     ethinicities: set = set()
#     regions: set = set()
#     periods: set = set()
#     social_welfares: set = set()
#     for data in mapped_data:
#         month_years.add(data[0])
#         ages.add(data[1])
#         genders.add(data[2])
#         birthdays.add(data[3])
#         schoolings.add(data[4])
#         ethinicities.add(data[5])
#         regions.add(data[6])
#         periods.add(data[7])
#         social_welfares.add(data[8])
#     return {
#         "headers": headers,
#         "month_years": month_years,
#         "ages": ages,
#         "genders": genders,
#         "birthdays": birthdays,
#         "schoolings": schoolings,
#         "ethinicities": ethinicities,
#         "regions": regions,
#         "periods": periods,
#         "social_welfares": social_welfares,
#     }
