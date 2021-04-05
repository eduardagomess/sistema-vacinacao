from abc import ABC, abstractmethod


class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, telefone: str, cpf: int):
        self.__nome = nome
        self.__telefone = telefone
        self.__cpf = cpf

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

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

