import scrapy
from scrapy import Request
from selenium import webdriver


class TransparenciaSpider(scrapy.Spider):
    name = "transparencia"
    start_urls = ['https://transparencia.campogrande.ms.gov.br/servidores/']

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        url = self.start_urls[0]
        self.driver.get(self.start_urls[0])
        search_button = self.driver.find_element_by_xpath('//button[@id="btn-search-servidor"]')
        yield Request(url, callback=self.parse_table)
        search_button.click()

        self.driver.close()

    def parse_table(self, response):
        print(response.body)