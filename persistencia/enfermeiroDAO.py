from persistencia.DAO import DAO
from entidade.enfermeiro import Enfermeiro


class EnfermeiroDAO(DAO):
    def __init__(self):
        super().__init__('enfermeiro.pkl')

    def add(self, enfermeiro: Enfermeiro):
        if enfermeiro is not None and isinstance(enfermeiro, Enfermeiro) and isinstance(enfermeiro.coren, str):
            super().add(enfermeiro.coren, enfermeiro)

    def remove(self, enfermeiro: Enfermeiro):
        if enfermeiro is not None and isinstance(enfermeiro, Enfermeiro) and isinstance(enfermeiro.coren, str):
            super().remove(enfermeiro.coren)
