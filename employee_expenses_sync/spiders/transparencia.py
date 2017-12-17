import scrapy
from scrapy import Selector
from selenium import webdriver


class TransparenciaSpider(scrapy.Spider):
    name = "transparencia"
    start_url = 'https://transparencia.campogrande.ms.gov.br/servidores/'

    def start_requests(self):
        driver = webdriver.Chrome()
        driver.get(self.start_url)
        search_button = driver.find_element_by_xpath('//button[@id="btn-search-servidor"]')
        self.parse(driver.page_source)

        search_button.click()

        driver.close()

    def parse(self, response):
        rows = response.xpath('//table[@id="table_id"]/tbody/tr')
        for row in rows:
            print(row)
