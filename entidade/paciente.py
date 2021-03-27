from entidade.pessoa import Pessoa
import datetime

class Paciente(Pessoa):
    def __init__(self, nome: str, telefone: str, cpf: int, endereco: str, data_nascimento: datetime, dose: int):
        super().__init__(nome, telefone, cpf, endereco, data_nascimento)
        self.__dose = dose
        self.__pacientes = []

    @property
    def dose(self):
        return self.__dose

    @dose.setter
    def dose(self, dose):
        self.__dose = dose

    @property
    def lista_pecientes(self):
        return self.__pacientes
