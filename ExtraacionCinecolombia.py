from scrapy.item import Item
from scrapy.item import Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import Selector

#------------------------------
#Iniciallizacion de vatriables
#------------------------------

#urlSemilla




class TitulosCartelera(Item):
    nombre = Field()
    estreno = Field()
    genero = Field()

class Cinecolombia(Spider):
    name = "cine"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }

    start_urls =["https://www.cinecolombia.com/bogota/cartelera"]

    def parse(self, response):
        sel = Selector(response)
