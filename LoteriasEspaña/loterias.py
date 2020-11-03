
import requests
from bs4 import BeautifulSoup
import pandas as pd

fuente = 'https://www.loteriasyapuestas.es/es'
pagina = requests.get(fuente)
libreria = BeautifulSoup(pagina.content, 'html.parser')

fec = libreria.find_all('td', class_='views-field views-field-field-fecha')

fecha = list()

for i in fec:
    fecha.append(i.text)

res = libreria.find_all('td', class_='views-field views-field-field-cifra6')

resultado = list()

for i in res:
    resultado.append(i.text)

sor = libreria.find_all('td', class_='views-field views-field-field-sorteo')

sorteo = list()

for i in sor:
    sorteo.append(i.text)

df = pd.DataFrame({'fecha': fecha, 'resultado': resultado,
                  'sorteo': sorteo})

df.fecha = df.fecha.fuente.strip()
df.resultado = df.resultado.fuente.strip()
df.sorteo = df.sorteo.fuente.strip()

print (df)

df.to_csv('Resultados_Loteria.csv', index=False, sep=',')
