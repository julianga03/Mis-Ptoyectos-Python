from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose, Join
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess


class Noticia(Item):
    titulo = Field()
    contenido = Field()


class Video(Item):
    titulo = Field()
    descripcion = Field()


class Galeria(Item):
    titulo = Field()
    fecha_de_publicacion = Field()


class IGNCrawler(CrawlSpider):
    name = 'ign'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 30 # Para colocarle máximo 30 páginas
    }

    allowed_domains = ['latam.ign.com']
    download_delay = 1

    start_urls = ['https://latam.ign.com/se/?model=article&q=ps5&order_by=']

    rules = (
        # Horizontalidad por tipo de información
        Rule(LinkExtractor(allow=r'/se/?'), follow=True),
        # Horizontalidad por paginación
        Rule(LinkExtractor(allow=r'&page=\d+'), follow=True),
        # Reglas por cada tipo de contenido donde ire verticalmente
        # 1. Noticia
        Rule(LinkExtractor(allow=r'/news/'), follow=True, callback='parse_noticia'),
        # 2. Video
        Rule(LinkExtractor(allow=r'/video/'), follow=True, callback='parse_video'),
        # 3. Galería
        Rule(LinkExtractor(allow=r'/gallery/'), follow=True, callback='parse_galeria')
    )

    def parse_noticia(self, response):
        item = ItemLoader(Noticia(), response)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('contenido', '//div[@id="id_text"]//text()', MapCompose(str.strip), Join())

        yield item.load_item()

    def parse_video(self, response):
        item = ItemLoader(Video(), response)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('descripcion', '//section[@class="video-details"]//p | //i | //div[@itemprop="articleBody"]/text() | //div[@id="id_deck"]/text()', MapCompose(str.strip), Join())

        yield item.load_item()

    def parse_galeria(self, response):
        item = ItemLoader(Galeria(), response)
        item.add_xpath('titulo', '//h1[@id="gallery_title"]/text()')
        item.add_xpath('fecha_de_publicacion', '//span[@class="publish-date"]/text()', MapCompose(str.strip))

        yield item.load_item()

process = CrawlerProcess({
    'FEED_FORMAT': 'json',
    'FEED_URI': 'Datos.json'
})
process.crawl(IGNCrawler)
process.start()