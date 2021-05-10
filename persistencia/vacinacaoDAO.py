from entidade import vacina, paciente, enfermeiro, pessoa
from entidade.enfermeiro import Enfermeiro
from entidade.paciente import Paciente
from entidade.vacina import TipoVacina
from entidade.vacinacao import Vacinacao
from persistencia.DAO import DAO


class VacinacaoDAO(DAO):
    def __init__(self):
        super().__init__('vacinacao.pkl')

    def add(self, cpf, vacinacao):
        if isinstance(cpf, str) and (vacinacao is not None) and isinstance(vacinacao, Vacinacao):
            super().add(cpf, vacinacao)
        else:
            print("problema")

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
