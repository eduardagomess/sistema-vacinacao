from entidade.pessoa import Pessoa
import datetime

class Paciente(Pessoa):
    def __init__(self, nome: str, telefone: str, cpf: int, endereco: str, data_nascimento: datetime, dose: int):
        super().__init__(nome, telefone, cpf)
        self.__dose = dose
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco
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

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def data_nascimento(self) -> datetime:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
