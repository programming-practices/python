
# El Web Scraping son un conjunto de tecnicas que se utilisan para obtener de forma automatica el contenido que hay en
# paginas web a traves de su codigo HTML. Alguno de los usos son:
    # la comparacion de precios en tienda.
    # la monitorizacion de datos ralacionaodos con el clima de cierta region
    # la deteccion de cambios en sitios web
# La libreria Beatiful Soup nos ayuda realizar web scraping en Python. Esta disponible en PIP (line de coandos de vuestro
# sistema operativo) pip install beautifulsoup4
# Sin embargo, es un proceso laborioso y si existe una API publica tipo ReST se suele preferir Web Scraping.

# A continuacion adjunto una funcion capaz de hacer una conexion HTTP para acceder a una pagina web y extraer informacion.
import requests
url = "https://es.wikipedia.org/wiki/Anexo:Municipios_de_la_Comunidad_de_Madrid"
# Realizamos la peticion HTTP a la web
req  = requests.get(url)
# Comprobamos que la peticion nos devuelve una Status Code = 200
statusCode = req.status_code
if statusCode == 200:
    print('La peticion ha ido bien')
else:
    print('Problemas con la peticion....')

# En primer lugar hacemos una peticion HTTP a la pagina web para obtener su codigo HTML, mediante la libreira request.
# Utilizado el methodo get, con parametro la direccion URL, nos dar el objeto req.
# Este objeto almacena muchos datos relacionados con la peticion HTTP (cabeceras, cookies, etc.), de donde obtenemos el
# Status Code y el HTML (como un string) de la web.

htmlText = req.text
# A partir del string htmlText que representa el codigo interno de la pagina web, usamos la libreria Beatiful Soup para
# hacer scraping de la pagina. Para importarla, se anade esta linea al principio del codigo.

from bs4 import BeautifulSoup

# Beatiful Soup nos aporta los methodos necesarios y optimizados par obtener el contenido que hay entre las etiquetas HTML.
if statusCode != 200:
    print('Algo fue mal obteniendo la web')
    quit()
# Pasamos el contenido HTML de al web a un objeto BeautifulSoup()
html = BeautifulSoup(req.text, 'html.parser')

# Si echamos un vistaso al HTML, es una tabla, donde cada fila es un municipio.
content = {}
# Obtenemos cada una de las filas de la tabla
rows = html.find_all('tr')
for municipio in rows:
    # Seleccionamos las celdas de cada fila (td)
    celdas = municipio.find_all('td')
    # ignoramos la primera celda, que no tiene elementos td sino th
    if len(celdas) > 0:
        # En lugar de un separador de miles, se ha usado un caracter parecido a un espacio en blanco por lo que en la
        # celda de habitantes hay que eliminar todos los caracterres que no sean numeros.
        content[celdas[0].string] = {'poblacion': int(''.join(c for c in celdas[1].string if c.isdigit())),
                                     'superficie': int(''.join(c for c in celdas[2].string if c.isdigit())),
                                     'altitud': int(''.join(c for c in celdas[6].string if c.isdigit()))}


# Ejercicio
# 1. Calcula la poblacion total de todos los municipios
# 2. Obten un listado de los municipios cuya altitud sea por encima de los 900 metros.

# 1
# print(content)
pobTotal = 0
for municipio in content.values():
    pobTotal += 1
print(pobTotal)

# 2
listaMunicipios = []
for (municipio, datos) in content.items():
    if datos['altitud'] > 900:
        listaMunicipios.append(municipio)
print(listaMunicipios)










