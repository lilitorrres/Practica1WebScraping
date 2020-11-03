import urllib.request

fuente = urllib.request.urlopen('https://www.loteriasyapuestas.es/es').read().decode()

from bs4 import BeautifulSoup
soup =  BeautifulSoup(fuente)
tags = soup('a')

for tag in tags:
	print(tag.get('href'))
