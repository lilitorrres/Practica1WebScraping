# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:03:47 2020

@author: ltorresbo y jcsola
"""

#Importamos  las librerias necesarias

import random
from time import sleep
from selenium import webdriver
import pandas as pd
import urllib.request

#decidimos usar la driver de chrome
web1 = webdriver.Chrome('./chromedriver.exe')
web2 = webdriver.Chrome('./chromedriver.exe')

#Definición variable donde se almace la URL para realizar el web scraping
url1 = 'https://www.ktronix.com/'
url2 = 'https://www.amazon.es/'

#Abrimos la pagina
web1.get(url1)
web2.get(url2)

#Esperamos un tiempo aleario entre 5 y 10 segundos para no usar siempre el mismo tiempo de espera de consulta
sleep(random.uniform(5.0,10.0))

#En la barra de busqueda de la pagina enviamos "iphone 11"
web1.find_element_by_id('js-site-search-input').send_keys("iphone 11")
web1.find_element_by_id("js-site-search-input").submit()

web2.find_element_by_id('twotabsearchtextbox').send_keys('iphone 11')
web2.find_element_by_id('twotabsearchtextbox').submit()

#Almacenamos los elementos con las etiquetas correspondientes para nombre, precio y caracteristicas
celular = web1.find_elements_by_class_name("product__information--name")
celular2 = web2.find_elements_by_class_name("a-size-mini")

precio = web1.find_elements_by_class_name("product__price--discounts__price")
precio2 = web2.find_elements_by_class_name("a-price-whole")

caracteristica = web1.find_elements_by_class_name("product__information--specifications__block")
caracteristica2 = web2.find_elements_by_class_name("a-size-base-plus")

#Definimos las listas que almaceran los elementos encontrados con las class_nam definidas anteriormente
productolist=list()
preciolist=list()
caracteristicalist=list()

productolist2=list()
preciolist2=list()
caracteristicalist2=list()

#Ciclos para obtener los nombres de los productos y almacenarlos en la lista correspindiente
for celulares in celular:
    nombre= celulares.find_element_by_xpath('.//a[@class="js-product-click-datalayer"]').text
    productolist.append(nombre)
    

for precios in precio:
    precio= precios.find_element_by_xpath('.//span[@class="price"]').text
    preciolist.append(precio)


for caracteristicas in caracteristica:
    caracteristica= caracteristicas.find_element_by_xpath('.//div[@class="item--key"]').text +" - "+ caracteristicas.find_element_by_xpath('.//div[@class="item--value"]').text
    caracteristicalist.append(caracteristica)
        
#Definimos los dataFrame con las listas obtenidas anteriormente   

df = pd.DataFrame(list(zip(productolist, preciolist, caracteristicalist)), 
               columns =['Name', 'val', 'caracteristica'])

#Imprimimos el df
print(df)

#Almacenamos el  resultado  en un archivo CSV con ,  como separador
df.to_csv('Resultado_iphone11.csv', index=False, sep=',')


#Campturamos el  logo el almacen con nombre logo.png
img = web1.find_element_by_xpath('//img[@loading="lazy"]')
try:
    img.screenshot('logo.png')
except Exception as ex:
    web1.get_screenshot_as_file('error.png')

#Cerramos la sesión abierta al incio
web1.close()
