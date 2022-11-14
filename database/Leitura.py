import pandas as pd

def faixa_etaria(fe):
    if fe['IDADE'] < 12: 
        return '0-11' 
    elif fe['IDADE']>= 12 and fe['IDADE'] <18:
         return '12-17'
    elif fe['IDADE']>= 18 and fe['IDADE'] <30:
         return '18-29'
    elif fe['IDADE']>= 30 and fe['IDADE'] <60:
         return '30-59'
    else: 
        return '>60'

rua = pd.read_csv(r'C:\Users\gusta\OneDrive\Documentos\Curso - TBD\1º Semestre\Projeto\data_set_poprua_cadunico-07-2022.csv',encoding='cp860',delimiter=';',usecols=[0,1,2,3,4,5,7,8,9,10,11,12])
rua['Faixa_etaria'] = rua.apply(faixa_etaria, axis=1)
print(rua)
