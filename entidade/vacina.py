from entidade.vacinacao import Vacinacao

class TipoVacina():
    def __init__(self, nome: str, num_doses: str):
        self.__nome = nome
        self.__num_doses = num_doses
        self.__vacinacao = None

    @property
    def nome(self):
        return self.__nome

    @property
    def num_doses(self):
        return self.__num_doses

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @num_doses.setter
    def num_doses(self, num_doses):
        self.__num_doses = num_doses

#ARRUMAR
    def determinar_vacinacao(self):
        self.__vacinacao = Vacinacao()
