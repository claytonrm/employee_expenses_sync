import csv
from collections import namedtuple

import requests


TRANSPARENCIA = 'https://transparencia.campogrande.ms.gov.br/servidores/?controller=servidores&action=download_csv&ano={year}&mes={month}'


TransparenciaRecord = namedtuple('TransparenciaRecord', 'nome periodo cpf cargo admissao')


class Service:

    def get_transparencia(self, year: int, month: int):
        response = requests.get(TRANSPARENCIA.format(year=2017, month=11), stream=True)
        response.raise_for_status()

        lines = [line.decode() for line in response.content.splitlines()]
        reader = csv.reader(lines, dialect='excel')
        return [TransparenciaRecord(*row) for row in reader]