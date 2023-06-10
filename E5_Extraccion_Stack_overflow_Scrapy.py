from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Pregunta(Item):
    Pregunta = Field()
    descripcion = Field


class StackOverFlowSpider(Spider):
    name = "MiPrimerSpider"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }

    start_urls = ['https://stackoverflow.com/questions']

    def parse(self, response):
        sel = Selector(response)
        