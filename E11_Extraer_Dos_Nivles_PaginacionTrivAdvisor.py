from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose, Join
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess

class Opinion(Item):
    titulo = Field()
    calificacion = Field()
    contenido = Field()
    autor = ()

class TripAdvisor(CrawlSpider):
    name = "OpinionesTripAdvisor"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 100 # Para colocarle máximo 30 páginas
    }

    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']

    download_delay = 2

    rules = (
        #Paginacion de hoteles
        Rule(
            LinkExtractor(
                allow=r'-oa\d+-'
            ),  follow=True
        ),
        #Detalle de hoteles
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-g303845-d',
                restrict_xpaths=['//div[@class="EJmPL _T bADWL _T PnJDh"]//a[@class="BMQDV _F G- wSSLS SwZTJ FGwzt ukgoS"]']
            ),  follow=True
        
        ),
        #Paginacion de Opiniones Dentro de un hotel
        Rule(
            LinkExtractor(
                allow=r'-or\d+-'
            ),  follow=True
            
        ),
        #Detalle de perfil de usuario
        Rule(
            LinkExtractor(
                allow=r'/Profile/',
                restrict_xpaths=['//div[@class="was-ssr-only"]//a[@class="ui_header_link uyyBf"]']
            ),  follow=True, callback='parse_opinion'
        )
    )

    def parse_opinion(self, response):
        sel = Selector(response)
        opiniones = sel.xpath
