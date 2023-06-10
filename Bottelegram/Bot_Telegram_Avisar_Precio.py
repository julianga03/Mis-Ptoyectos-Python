from bs4 import BeautifulSoup
import requests

url = 'https://www.mercadolibre.com.co/laptop-asus-x515ea-slate-gray-156-intel-core-i7-1165g7-8gb-de-ram-512gb-ssd-intel-iris-xe-graphics-g7-96eus-1920x1080px-freedos/p/MCO19854585?pdp_filters=category:MCO1652#searchVariation=MCO19854585&position=3&search_layout=stack&type=product&tracking_id=645b11ca-22ae-4f65-8fab-d72e819b217f'

respuesta = requests.get(url)

soup = BeautifulSoup(respuesta.content, 'html.parser')


resultado = soup.find('span', {"class":'andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact'}).text
palabras = resultado.split()
precio = palabras[0]
precio = int(precio)
print(precio)

precioDeseado = 3000000

if precio <= precioDeseado:
    print("Ofertaaaaaaa")

else:
    print("Envia bien cuando hay oferta primero")

