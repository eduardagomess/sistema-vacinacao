from entidade import paciente, enfermeiro, vacinacao
from entidade.vacinacao import Vacinacao


class TipoVacina():
    def __init__(self, nome: str, num_doses: str, qtd: str):
        self.__nome = nome
        self.__num_doses = num_doses
        self.__qtd = qtd
        self.__vacinacao = None

    @property
    def nome(self):
        return self.__nome

    @property
    def num_doses(self):
        return self.__num_doses

    @property
    def qtd(self):
        return self.__qtd

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @num_doses.setter
    def num_doses(self, num_doses):
        self.__num_doses = num_doses

    @qtd.setter
    def qtd(self, qtd):
        self.__qtd = qtd

    def determinar_vacinacao(self, paciente, enfermeiro, dose, tipo_dose):
        self.__vacinacao = Vacinacao(paciente, enfermeiro, dose, tipo_dose)
