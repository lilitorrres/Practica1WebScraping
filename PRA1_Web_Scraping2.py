# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:03:47 2020

@author: ltorresbo y jcsola
"""

#Importamos  las librerias necesarias

import random
import pandas as pd
import urllib.request

from time import sleep
from selenium import webdriver

#decidimos usar la driver de chrome
web1 = webdriver.Chrome('./chromedriver.exe')
web2 = webdriver.Chrome('./chromedriver.exe')
web3 = webdriver.Chrome('./chromedriver.exe')

#Definición variable donde se almace la URL para realizar el web scraping
url1 = 'https://www.ktronix.com/'
url2 = 'https://www.fnac.es/'
url3 = 'https://www.worten.es/'

#Abrimos la pagina
web1.get(url1)
web2.get(url2)
web3.get(url3)

#Esperamos un tiempo aleario entre 5 y 10 segundos para no usar siempre el mismo tiempo de espera de consulta
sleep(random.uniform(5.0,10.0))

#En la barra de busqueda de la pagina enviamos "iphone 11"
web1.find_element_by_id('js-site-search-input').send_keys('iphone 11')
web1.find_element_by_id('js-site-search-input').submit()

web2.find_element_by_class_name('Header__search-input').send_keys('iphone 11')
web2.find_element_by_class_name('Header__search-input').submit()
web2.find_element_by_class_name('Header__search-input').clear()

web3.find_element_by_id('search-input').send_keys('iphone 11')
web3.find_element_by_id('search-input').submit()
web3.find_element_by_id('search-input').clear()

#Almacenamos los elementos con las etiquetas correspondientes para nombre, precio y caracteristicas
celular = web1.find_elements_by_class_name("product__information--name")
celular2 = web2.find_elements_by_class_name("Article-infoContent")
celular3 = web3.find_elements_by_class_name("w-product__description")

precio = web1.find_elements_by_class_name("product__price--discounts__price")
precio2 = web2.find_elements_by_class_name("Article-price")
precio3 = web3.find_elements_by_class_name("w-currentPrice")

caracteristica = web1.find_elements_by_class_name("product__information--specifications__block")
caracteristica2 = web2.find_elements_by_class_name("moreInfos-list")
caracteristica3 = web3.find_elements_by_class_name("w-product__description-excerpt")

#Definimos las listas que almaceran los elementos encontrados con las class_nam definidas anteriormente
productolist=list()
preciolist=list()
caracteristicalist=list()

productolist2=list()
preciolist2=list()
caracteristicalist2=list()

productolist3=list()
preciolist3=list()
caracteristicalist3=list()

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

#FNAC
for celulares2 in celular2:
    nombre2 = celulares2.find_element_by_xpath('.//p[@class="Article-desc"]').text
    productolist2.append(nombre2)
    
for precios2 in precio2:
    precio2 = precios2.find_element_by_xpath('.//strong[@class="userPrice"]').text
    preciolist2.append(precio2)
    
for caracteristicas2 in caracteristica2:
    caracteristica2 = caracteristicas2.find_element_by_xpath('.//span[@class="label"]').text +" - "+ caracteristicas2.find_element_by_xpath('.//span[@class="data"]').text
    caracteristicalist2.append(caracteristica2)

#Worten
for celulares3 in celular3:
    nombre3 = celulares3.find_element_by_xpath('.//h3[@class="w-product__title"]').text
    productolist3.append(nombre3)
    
for precios3 in precio3:
    precio3 = precios3.find_element_by_xpath('.//span[@class="w-product-price__main"]').text +'.'+ precios3.find_element_by_xpath('.//sup[@class="w-product-price__dec"]').text + precios3.find_element_by_xpath('.//span[@class="w-product-price__currency small"]').text 
    preciolist3.append(precio3)  

#Definimos los dataFrame con las listas obtenidas anteriormente   

df = pd.DataFrame(list(zip(productolist, preciolist, caracteristicalist)), 
               columns =['Name', 'val', 'caracteristica'])

df2 = pd.DataFrame(list(zip(productolist2, preciolist2, caracteristicalist2)), 
               columns =['Nombre', 'precio', 'caracteristica'])

df3 = pd.DataFrame(list(zip(productolist3, preciolist3)), 
               columns =['Nombre', 'precio'])

#Imprimimos el df
print(df)
print(df2)
print(df3)

#Almacenamos el  resultado  en un archivo CSV con ,  como separador
df.to_csv('Resultado_iphone11.csv', index=False, sep=',')
df2.to_csv('Resultado_iphone11Fnac.csv', index=False, sep=',')
df3.to_csv('Resultado_iphone11Worten.csv', index=False, sep=',')


#Campturamos el  logo el almacen con nombre logo.png
img = web1.find_element_by_xpath('//img[@loading="lazy"]')
try:
    img.screenshot('logo.png')
except Exception as ex:
    web1.get_screenshot_as_file('error.png')

#Cerramos la sesión abierta al incio
web1.close()
web2.close()
web3.close()
