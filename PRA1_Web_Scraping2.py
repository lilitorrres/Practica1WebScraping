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
driver = webdriver.Chrome('./chromedriver.exe')

#Definición variable donde se almace la URL para realizar el web scraping
url='https://www.ktronix.com/?fuente=google&medio=cpc&campaign=KT_COL_SEM_PEF_CPC_B_AON_TLP_TLP_Brand-General-AON_PAC&keyword=ktronix&gclid=Cj0KCQjwlvT8BRDeARIsAACRFiW9ZLLQehFIl7vztzG12gbU_bZem_5FsBXVRdUdBdyIb48eYOz2sboaAuEqEALw_wcB'

#Abrimos la pagina
driver.get(url)

#Esperamos un tiempo aleario entre 5 y 10 segundos para no usar siempre el mismo tiempo de espera de consulta
sleep(random.uniform(5.0,10.0))

#En la barra de busqueda de la pagina enviamos "iphone 11"
driver.find_element_by_id('js-site-search-input').send_keys("iphone 11")
driver.find_element_by_id("js-site-search-input").submit()

#Almacenamos los elementos con las etiquetas correspondientes para nombre, precio y caracteristicas
celular = driver.find_elements_by_class_name("product__information--name")
precio = driver.find_elements_by_class_name("product__price--discounts__price")
caracteristica = driver.find_elements_by_class_name("product__information--specifications__block")

#Definimos las listas que almaceran los elementos encontrados con las class_nam definidas anteriormente
productolist=list()
preciolist=list()
caracteristicalist=list()

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
img = driver.find_element_by_xpath('//img[@loading="lazy"]')
try:
    img.screenshot('logo.png')
except Exception as ex:
    driver.get_screenshot_as_file('error.png')

#Cerramos la sesión abierta al incio
driver.close()
