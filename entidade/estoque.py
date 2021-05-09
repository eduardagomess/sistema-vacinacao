from excecao import erro_de_tipo
from entidade.vacina import TipoVacina
from datetime import datetime


class Estoque:
    def __init__(self, tipo_vacina: TipoVacina, qtd: int, data_recebimento: datetime, lote: str):
        self.__qtd = qtd
        if isinstance(tipo_vacina, TipoVacina):
            self.__tipo_vacina = tipo_vacina
        self.__data_recebimento = data_recebimento
        self.__lote = lote

    @property
    def tipo_vacina(self):
        return self.__tipo_vacina

    @property
    def qtd(self):
        return self.__qtd

    @property
    def lote(self):
        return self.__lote

    @qtd.setter
    def qtd(self, qtd):
        self.__qtd = qtd

    @property
    def data_recebimento(self):
        return self.__data_recebimento
