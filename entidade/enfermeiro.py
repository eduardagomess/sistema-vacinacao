from entidade.pessoa import Pessoa
import datetime

class Enfermeiro(Pessoa):
    def __init__(self, nome: str, telefone: int, cpf: int, bairro: str, endereco: str, data_nascimento: datetime, lista_enfermeiros:[]):
        super().__init__(nome, telefone, cpf, bairro, endereco, data_nascimento)
        self.__lista_enfermeiros = lista_enfermeiros

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> str:
        self.__nome = nome

    @property
    def telefone(self) -> int:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone) -> int:
        self.__telefone = telefone

    @property
    def cpf(self) -> int:
        return self.__cpf

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco) -> str:
        self.__endereco = endereco

    @property
    def data_nascimento(self) -> datetime:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento) -> datetime:
        self.__data_nascimento = data_nascimento

    @property
    def lista_enfermeiros(self):
        return self.__lista_enfermeiros