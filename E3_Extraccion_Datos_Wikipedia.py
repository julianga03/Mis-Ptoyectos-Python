import requests                     #para hacer peticiones a la WEB 
from lxml import html               #Para poder parsear lo extraido del requests

encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

url = "https://www.wikipedia.org/"  #url semilla puede llamarse como sea es una variable

respuesta = requests.get(url, headers=encabezados)       #Para hacer el requerimiento a la url y almacenar lo que devueve (el arbol HTML) y se le encia el header

#Hay una informacion adicional que va atada al requerimiento son "Encabezados" Estos son un grupo de variables que le sirven al
#servidor para obtener informacion adicional de quien esta haciendo el requerimiento o como esta haciendo el requerimiento.

parser = html.fromstring(respuesta.text)               #Convierte lo que trae en un parseador

print(parser)

"""""
ingles = parser.get_element_by_id("js-link-box-en") 
print(ingles.text_content())
"""


"""
ingles = parser.xpath("//div[@class='central-featured-lang lang1']//strong/text()")
print(ingles)
"""


"""
idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
for idio in idiomas:
    print(idio)
"""

idiomas = parser.find_class('central-featured-lang')
for idio in idiomas:
    print(idio.text_content())