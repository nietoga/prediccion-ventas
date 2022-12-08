import requests
from datetime import datetime

def obtenerPrendas (tienda):
    now = datetime.now()
    semana = (datetime.date(now).isocalendar()[1]) + 1
    if(semana == 54):
        semana = 1
    params = {'tienda': tienda, 'semana': semana}
    response = requests.get('http://predventas.ml/predecir', params=params)
    return response.json()


a = obtenerPrendas('CAMINO REAL')
print(a)
# print(len(a))
# b = a[0]['PRENDA']
# c = a[0]['UNIDADES']
# print(b + ': ' + str(c))
