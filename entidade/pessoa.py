from abc import ABC, abstractmethod
import datetime

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, telefone: str, cpf: int, endereco: str, data_nascimento: datetime):
        self.__nome = nome
        self.__telefone = telefone
        self.__cpf = cpf
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def cpf(self) -> int:
        return self.__cpf

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


