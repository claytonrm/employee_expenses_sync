import csv
from collections import namedtuple

TRANSPARENCIA = 'https://transparencia.campogrande.ms.gov.br/servidores/?controller=servidores&action=download_csv&ano={year}&mes={month}'


TransparenciaRecord = namedtuple('TransparenciaRecord', 'nome periodo cpf cargo admissao')


class Service:

    def get_transparencia(self, year: int, month: int):
        pass