from excecao import erro_de_tipo
from entidade.vacina import TipoVacina
from datetime import datetime


class Estoque(TipoVacina):
    def __init__(self, nome: str, num_doses, qtd: int, data_recebimento: datetime, lote: str): #, tipo_vacina)
        super().__init__(nome, num_doses)
        self.__nome = nome
        self.__qtd = qtd
        self.__num_doses = num_doses
        self.__data_recebimento = data_recebimento
        self.__lote = lote
        #self.__tipo_vacina = tipo_vacina

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
