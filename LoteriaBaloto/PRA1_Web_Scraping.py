#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Wed Oct 28 19:48:47 2020

@author: ltorresbo y jcsola
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

str = 'https://www.loteriasdehoy.com/baloto'
page = requests.get(str)
soup = BeautifulSoup(page.content, 'html.parser')

fec = soup.find_all('td', class_='views-field views-field-field-fecha')

fecha = list()

for i in fec:
    fecha.append(i.text)

res = soup.find_all('td', class_='views-field views-field-field-cifra6')

resultado = list()

for i in res:
    resultado.append(i.text)

sor = soup.find_all('td', class_='views-field views-field-field-sorteo')

sorteo = list()

for i in sor:
    sorteo.append(i.text)

df = pd.DataFrame({'fecha': fecha, 'resultado': resultado,
                  'sorteo': sorteo})

df.fecha = df.fecha.str.strip()
df.resultado = df.resultado.str.strip()
df.sorteo = df.sorteo.str.strip()

print (df)

df.to_csv('Resultado_baloto.csv', index=False, sep=',')
