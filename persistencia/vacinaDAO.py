from entidade import vacina
from entidade.vacina import TipoVacina
from persistencia.DAO import DAO


class VacinaDAO(DAO):
    def __init__(self):
        super().__init__('vacinas.pkl')

    def add(self, nome, vacina: TipoVacina):
        if isinstance(vacina.nome, str) and (vacina is not None) and isinstance(vacina, TipoVacina):
            super().add(vacina.nome, vacina)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
