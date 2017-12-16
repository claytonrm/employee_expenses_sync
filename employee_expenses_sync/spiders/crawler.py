import scrapy

class Crawler(scrapy.Spider):
    name = "transparencia"

    start_url = ['https://transparencia.campogrande.ms.gov.br/servidores/']

    def parse(self, response):
        print(response)
