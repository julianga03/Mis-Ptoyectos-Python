from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess

class Articulo(Item):
    titulo = Field()
    precio = Field()
    descripcion = Field()

class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadoLibre'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20 #Para colocarle maximo 20 paginas
    }

    dowload_delay = 2

    #allowed_domains = ['https://carros.mercadolibre.com.co', 'https://carro.mercadolibre.com.co']  #urls que estan permitidos nos aseguramos que scrapy no valla a paginas que no pertenezcan a este dominio

    start_urls = ['https://carros.mercadolibre.com.co/bmw/tipo-de-carroceria-coupe']

    rules = (
        Rule(
            #Paginacion
            LinkExtractor(
                allow=r'_Desde_'
            ),follow=True
            
        ),
        Rule(
            #Detalles de los productos
            LinkExtractor(
                allow=r'/MCO-'
            ),follow=True, callback='parse_items'
        ),
    )

    def parse_items(self, response):
        item = ItemLoader(Articulo(), response)

        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('descripcion', '//p[@class="ui-pdp-description__content"]/text()')
        item.add_xpath('precio', '//span[@class="andes-money-amount__fraction"]/text()')

        yield item.load_item()

process = CrawlerProcess({
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'Datos.csv'
})
process.crawl(MercadoLibreCrawler)
process.start()