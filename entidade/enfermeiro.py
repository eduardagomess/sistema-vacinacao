from entidade.pessoa import Pessoa


class Enfermeiro(Pessoa):
    def __init__(self, nome: str, telefone: int, cpf: int, coren: int):
        super().__init__(nome, telefone, cpf)
        self.__lista_enfermeiros = []
        self.__lista_pacientes = []
        self.__coren = coren


    @property
    def lista_enfermeiros(self):
        return self.__lista_enfermeiros

    @property
    def lista_pacientes(self):
        return self.__lista_pacientes

    @property
    def coren(self):
        return self.__coren

    @coren.setter
    def coren(self, coren):
        self.__coren = coren