from entidade.pessoa import Pessoa
import datetime
from entidade.endereco import Endereco


class Paciente(Pessoa):
    def __init__(self, nome: str, telefone: str, cpf: int, data_nascimento: datetime):
        super().__init__(nome, telefone, cpf)
        self.__dose = 0
        self.__tipo_dose = None
        self.__data_nascimento = data_nascimento
        self.__endereco = None

    @property
    def dose(self):
        return self.__dose

    @dose.setter
    def dose(self, dose):
        self.__dose = dose

    @property
    def tipo_dose(self):
        return self.__tipo_dose

    @tipo_dose.setter
    def tipo_dose(self, tipo):
        self.__tipo_dose = tipo

    @property
    def data_nascimento(self) -> datetime:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def endereco(self):
        return self.__endereco

    def determinar_endereco(self, bairro: str, rua: str, numero: int, complemento: str):
        self.__endereco = Endereco(bairro, rua, numero, complemento)



