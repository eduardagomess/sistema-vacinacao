from entidade.pessoa import Pessoa
import datetime
from entidade.endereco import Endereco


class Paciente(Pessoa):
    def __init__(self, nome: str, telefone: str, cpf: int, bairro: str, rua: str, numero: str, complemento: str, data_nascimento: datetime, dose: int):
        super().__init__(nome, telefone, cpf)
        self.__dose = dose
        self.__data_nascimento = data_nascimento
        self.__endereco = Endereco(bairro, rua, numero, complemento)

    @property
    def dose(self):
        return self.__dose

    @dose.setter
    def dose(self, dose):
        self.__dose = dose

    @property
    def data_nascimento(self) -> datetime:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    def determinar_endereco(self, bairro: str, rua: str, numero: str, complemento: str):
        self.__endereco = Endereco(bairro, rua, numero, complemento)

    @property
    def endereco(self):
        return self.__endereco.mostrar_endereco()

