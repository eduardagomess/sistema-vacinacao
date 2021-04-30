from excecao import erro_de_tipo
from entidade.vacina import TipoVacina


class Estoque(TipoVacina):
    def __init__(self, nome: str, num_doses, qtd: int):
        super().__init__(nome, num_doses, qtd)
        self.__nome = nome
        self.__qtd = qtd
        self.__num_doses = num_doses

    @property
    def qtd(self):
        return self.__qtd

    @qtd.setter
    def qtd(self, qtd):
        self.__qtd = qtd
