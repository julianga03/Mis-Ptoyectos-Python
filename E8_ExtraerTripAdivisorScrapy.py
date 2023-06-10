from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import itemloaders

#1 Paso (definir nuestra astraccion de las cosas que se van a extraer)
#se define la primera clase que nos ayuda a la extraccion de la informacion

class Hotel(Item):
    nombre = Field()
    precio = Field()
    descripcion = Field()
    aminities = Field()

#2 Definir la clase COR

class TripAdvisor(CrawlSpider):     #en el crawling vertical u horizontal ya no heredamos de spider, si no, de CrawlSpider
    name = "Hoteles"                #Poner combres a los scrapers
    custom_settings = {
        'USER_AGENT': 'user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']

    download_delay = 2              #mecanismo antibaneo, tiempo que va a esperar scrapu luego de hacer un requerimiento antes de hacer otro requerimiento

    #la variable rules es una tupla vasicamente le van a decir al spider a donde tiene que ir y a donde no tiene que ir
    #Los liks al que vamos a visitar hay que buscar cuales son los que se repiten en cada uno de ellos
    rules = (
        Rule(
            LinkExtractor(              #permine extraer los links dentro de un pagina
                allow=r'/Hotel_Review-'     #El link solo extraera si tiene esta palabra /Hotel_Review-    
            ), follow=True, callback="parse_hotel"  #Este parametro es dice que si estos links que se a permitido los tengo que seguir en este caso si, collbakc se coloca el nombre de alguna funcion que quiero llamar cuando se haga un requerimiento a las uls que venga con el patron
        ),
    )

    def parse_hotel(self, response):
        sel = Selector(response)        #Parseador del arbol
        item_loader = itemloaders.ItemLoader(item=Hotel(), selector=sel)
        #item = itemloaders(Hotel(), sel)

        #Aca ya puedo jugar con las sexpresiones xpath para traer lo que quiero

        item_loader.add_xpath('nombre', '//h1[@id="HEADING"]/text()')
        item_loader.add_xpath('precio', '//div[@class="WXMFC b autoResize"]/text()')
        item_loader.add_xpath('descripcion', '//div[1][@class="fIrGe _T"]/text()')
        item_loader.add_xpath('aminities', '//div[@class="yplav f ME H3 _c"]/text()')

        yield item_loader.load_item()



